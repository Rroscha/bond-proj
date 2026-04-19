#!/usr/bin/env python3
"""Debug concrete execution on arith_add_u32."""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import angr
import rustdiff
from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor, _TEST_INPUTS

bin_path = 'tmp/rust-corpus/testcrate-O0'
print(f"Loading: {bin_path}")
loader = RustBinaryLoader(bin_path, load_debug_info=False)

# Find arith_add_u32
for addr, name in loader.get_analyzable_functions():
    if 'arith_add' in name:
        print(f"\n{name} @ 0x{addr:x}")
        blocks = loader.get_blocks_for_function(addr)
        for ba, blk in blocks:
            print(f"\n  Block 0x{ba:x}:")
            for insn in blk.capstone.insns:
                print(f"    {insn.mnemonic:8s} {insn.op_str}")

        # Manual test
        ba, blk = blocks[0]
        proj = loader.proj
        test_input = _TEST_INPUTS[0]

        state = proj.factory.blank_state(
            addr=ba,
            add_options={
                angr.sim_options.ZERO_FILL_UNCONSTRAINED_MEMORY,
                angr.sim_options.ZERO_FILL_UNCONSTRAINED_REGISTERS,
                angr.sim_options.TRACK_MEMORY_ACTIONS,
            },
        )

        # Set registers properly
        setattr(state.regs, 'rsp', state.solver.BVV(0x7ffffffffff0000, 64))
        regs = ['rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi',
                'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15']
        pre = {}
        for i, r in enumerate(regs):
            v = test_input[i % len(test_input)]
            setattr(state.regs, r, state.solver.BVV(v, 64))
            pre[r] = v

        print(f"\n  Pre: rdi=0x{pre['rdi']:x}, rsi=0x{pre['rsi']:x}, rax=0x{pre['rax']:x}")

        n = len(list(blk.capstone.insns))
        simgr = proj.factory.simgr(state)
        simgr.step(num_inst=n)

        print(f"  active={len(simgr.active)}, deadended={len(simgr.deadended)}, errored={len(simgr.errored)}")

        ps = simgr.active[0] if simgr.active else (simgr.deadended[0] if simgr.deadended else None)
        if ps:
            for r in regs:
                v = getattr(ps.regs, r)
                if v.concrete:
                    new_v = ps.solver.eval(v)
                    if new_v != pre[r]:
                        print(f"  CHANGED {r}: 0x{pre[r]:x} -> 0x{new_v:x}")

            acts = list(ps.history.actions)
            print(f"  Memory actions: {len(acts)}")
            for a in acts[:20]:
                if a.type == 'mem':
                    addr_v = ps.solver.eval(a.addr.ast) if a.addr.ast.concrete else 'sym'
                    print(f"    {a.action} @ 0x{addr_v:x} size={a.size}")

        # Now test with the executor
        print("\n  Testing via BlockMicroExecutor:")
        executor = BlockMicroExecutor(loader)
        sig = executor.execute_block(ba, blk)
        if sig:
            print(f"    opcodes: {sig.opcode_sequence}")
            print(f"    concrete_outputs: {sig.concrete_outputs}")
            print(f"    memory_pattern: {sig.memory_pattern}")
            print(f"    dataflow_edges: {sig.dataflow_edges}")
            print(f"    callee_names: {sig.callee_names}")

        break
