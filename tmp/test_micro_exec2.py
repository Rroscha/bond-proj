#!/usr/bin/env python3
"""Debug micro-execution: diagnose why concrete outputs are empty."""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import angr
import rustdiff
from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.arch_neutralizer import ArchNeutralizer
from rustdiff.micro_exec.block_executor import BlockMicroExecutor, _TEST_INPUTS

bin_path = 'tmp/rust-corpus/testcrate-O0'
if not os.path.exists(bin_path):
    bin_path = 'tmp/coreutils-sort-O0'

print(f"Loading binary: {bin_path}")
loader = RustBinaryLoader(bin_path, load_debug_info=False)
arch = ArchNeutralizer(loader.arch_name)

# Pick a function with actual computation
funcs = loader.get_analyzable_functions()
# Find testcrate::main or something interesting
target = None
for addr, name in funcs:
    if 'arith' in name.lower() or 'add' in name.lower():
        target = (addr, name)
        break
if target is None:
    target = funcs[5] if len(funcs) > 5 else funcs[0]

addr, name = target
print(f"\nTarget function: {name} @ 0x{addr:x}")
blocks = loader.get_blocks_for_function(addr)
print(f"Blocks: {len(blocks)}")

for block_addr, block in blocks[:3]:
    print(f"\n{'='*60}")
    print(f"Block 0x{block_addr:x} ({block.size} bytes, "
          f"{len(list(block.capstone.insns))} insns)")
    for insn in block.capstone.insns:
        print(f"  {insn.mnemonic:8s} {insn.op_str}")

    # Manual concrete execution
    proj = loader.proj
    test_input = _TEST_INPUTS[0]

    state = proj.factory.blank_state(
        addr=block_addr,
        add_options={
            angr.sim_options.ZERO_FILL_UNCONSTRAINED_MEMORY,
            angr.sim_options.ZERO_FILL_UNCONSTRAINED_REGISTERS,
            # Enable action tracking for memory
            angr.sim_options.TRACK_MEMORY_ACTIONS,
            angr.sim_options.TRACK_REGISTER_ACTIONS,
        },
    )

    # Set SP
    state.regs._store(arch.sp_reg,
                      state.solver.BVV(arch.stack_base, arch.ptr_size * 8))

    # Set GP registers
    pre_regs = {}
    for i, reg in enumerate(arch.gp_regs):
        val = test_input[i % len(test_input)]
        try:
            state.regs._store(reg, state.solver.BVV(val, arch.ptr_size * 8))
            pre_regs[reg] = val
        except Exception as e:
            print(f"  Failed to set {reg}: {e}")

    print(f"\n  Pre-registers: {pre_regs}")

    # Step
    num_insns = len(list(block.capstone.insns))
    simgr = proj.factory.simgr(state)
    simgr.step(num_inst=num_insns)

    print(f"  After step: active={len(simgr.active)}, "
          f"deadended={len(simgr.deadended)}, "
          f"errored={len(simgr.errored)}")

    if simgr.active:
        post_state = simgr.active[0]
    elif simgr.deadended:
        post_state = simgr.deadended[0]
    else:
        print("  No post state!")
        if simgr.errored:
            print(f"  Error: {simgr.errored[0].error}")
        continue

    # Read post regs
    post_regs = {}
    changed = {}
    for reg in arch.gp_regs:
        try:
            val = post_state.regs._load(reg)
            if val.concrete:
                v = post_state.solver.eval(val)
                post_regs[reg] = v
                if pre_regs.get(reg) != v:
                    changed[reg] = (pre_regs.get(reg), v)
            else:
                post_regs[reg] = f"symbolic({val})"
        except Exception as e:
            post_regs[reg] = f"error({e})"

    print(f"\n  Post-registers: {post_regs}")
    print(f"  Changed registers: {changed}")

    # Check memory actions
    actions = list(post_state.history.actions)
    print(f"\n  History actions: {len(actions)}")
    for act in actions[:10]:
        print(f"    type={act.type}, action={act.action}")
        if act.type == 'mem':
            try:
                addr_v = post_state.solver.eval(act.addr.ast) if act.addr.ast.concrete else 'symbolic'
                print(f"    addr={addr_v}, size={act.size}")
            except:
                print(f"    addr=?, size=?")

    # Check callee names (what the executor SHOULD be doing)
    print(f"\n  Callees in block:")
    for insn in block.capstone.insns:
        if insn.mnemonic in ('call', 'callq'):
            target_addr = insn.operands[0].imm if insn.operands else None
            if target_addr:
                callee = loader.get_demangled_name(target_addr) or f'sub_{target_addr:x}'
                print(f"    call 0x{target_addr:x} -> {callee}")

    # Check string refs
    print(f"\n  String refs in block:")
    text_lo, text_hi = loader.get_section_range('.text') or (0, 0)
    rodata = loader.get_section_range('.rodata')
    for insn in block.capstone.insns:
        if insn.mnemonic in ('lea', 'adr', 'adrp'):
            for op in insn.operands:
                if hasattr(op, 'mem') and hasattr(op.mem, 'disp'):
                    # RIP-relative addressing
                    target_addr = insn.address + insn.size + op.mem.disp
                    if rodata and rodata[0] <= target_addr <= rodata[1]:
                        try:
                            s = proj.loader.memory.load(target_addr, 64)
                            null_idx = s.index(b'\x00') if b'\x00' in s else 64
                            s = s[:null_idx].decode('utf-8', errors='replace')
                            if s and len(s) > 2:
                                print(f"    lea @ 0x{insn.address:x} -> 0x{target_addr:x}: \"{s[:60]}\"")
                        except:
                            pass
