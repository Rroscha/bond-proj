"""Concrete micro-execution engine for per-basic-block value extraction.

This is the core novel component of RustDiff. Unlike vSim's tracelet-based
symbolic execution (bin_executor.py get_intra_block_cfg_run), this engine
performs lightweight concrete execution with N test input sets per block
and collects the resulting register/memory values.
"""

import logging
from collections import defaultdict

import angr
import claripy

from rustdiff.micro_exec.arch_neutralizer import ArchNeutralizer
from rustdiff.micro_exec.value_signature import (
    BlockValueSignature,
    MemoryAccess,
    ValueKind,
    normalize_opcode,
)

logger = logging.getLogger(__name__)

# Test input sets: concrete values to initialize registers with.
# Each set is designed to reveal different computational properties.
_TEST_INPUTS = [
    # Set 0: Small distinct positives — detect basic arithmetic
    [0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48],
    # Set 1: Powers of 2 — detect shifts, masks
    [1, 2, 4, 8, 16, 32, 64, 128],
    # Set 2: Larger values — detect truncation, overflow behavior
    [0x1000, 0x2000, 0x3000, 0x4000, 0x5000, 0x6000, 0x7000, 0x8000],
    # Set 3: Values with high bits set — detect sign extension
    [0xFF00, 0xFE00, 0xFD00, 0xFC00, 0xFB00, 0xFA00, 0xF900, 0xF800],
]


class BlockMicroExecutor:
    """Lightweight concrete micro-execution of individual basic blocks.

    For each block, runs N concrete executions with different input values
    and collects output register values, memory accesses, constants, and
    opcode sequences. Produces a BlockValueSignature per block.
    """

    def __init__(self, loader):
        """Initialize with a RustBinaryLoader instance."""
        self.loader = loader
        self.proj = loader.proj
        self._arch = ArchNeutralizer(loader.arch_name)
        self._text_range = self._get_text_range()
        self._data_ranges = self._get_data_ranges()

    def _get_text_range(self) -> tuple[int, int]:
        r = self.loader.get_section_range('.text')
        if r:
            return r
        # Fallback: use main object bounds
        obj = self.proj.loader.main_object
        return (obj.min_addr, obj.max_addr)

    def _get_data_ranges(self) -> list[tuple[int, int]]:
        ranges = []
        for name in ('.data', '.rodata', '.bss'):
            r = self.loader.get_section_range(name)
            if r:
                ranges.append(r)
        return ranges

    def execute_block(self, block_addr: int,
                      block: angr.block.Block) -> BlockValueSignature | None:
        """Micro-execute a single basic block with multiple test inputs.

        Returns a BlockValueSignature or None if the block is too small
        or execution fails for all test inputs.
        """
        if block is None or block.size == 0:
            return None

        num_insns = len(list(block.capstone.insns))
        if num_insns == 0:
            return None

        # Extract static features (no execution needed)
        opcode_seq = self._extract_opcode_sequence(block)
        constants = self._extract_constants(block)
        callee_names = self._extract_callee_names(block)
        string_refs = self._extract_string_refs(block)

        # Run concrete executions with each test input set
        all_outputs = defaultdict(list)  # reg -> [values across inputs]
        all_mem_accesses = []
        dataflow_edges = set()

        successful_runs = 0
        for test_input in _TEST_INPUTS:
            result = self._run_concrete(block_addr, block, test_input)
            if result is None:
                continue
            successful_runs += 1

            pre_regs, post_regs, mem_accesses, df_edges = result

            # Collect output register values
            for reg_name, post_val in post_regs.items():
                pre_val = pre_regs.get(reg_name)
                if pre_val != post_val:
                    neutral_reg = self._arch.normalize_register(reg_name)
                    all_outputs[neutral_reg].append(post_val)

            all_mem_accesses.extend(mem_accesses)
            dataflow_edges.update(df_edges)

        if successful_runs == 0:
            # Couldn't execute at all; return static-only signature
            return BlockValueSignature(
                block_addr=block_addr,
                num_instructions=num_insns,
                constants=tuple(sorted(set(constants))),
                opcode_sequence=tuple(opcode_seq),
                out_degree=0,
                callee_names=tuple(callee_names),
                string_refs=tuple(string_refs),
            )

        # Deduplicate memory accesses by (offset, size, is_write)
        mem_pattern = self._deduplicate_mem_accesses(all_mem_accesses)

        # Convert output values to tuples
        concrete_outputs = {
            reg: tuple(sorted(set(vals)))
            for reg, vals in all_outputs.items()
            if vals
        }

        # Count successors for out_degree
        out_degree = len(self.loader.be.get_bb_successors(block_addr))

        return BlockValueSignature(
            block_addr=block_addr,
            num_instructions=num_insns,
            constants=tuple(sorted(set(constants))),
            opcode_sequence=tuple(opcode_seq),
            memory_pattern=tuple(mem_pattern),
            dataflow_edges=frozenset(dataflow_edges),
            concrete_outputs=concrete_outputs,
            out_degree=out_degree,
            callee_names=tuple(callee_names),
            string_refs=tuple(string_refs),
        )

    def execute_function(
        self, func_addr: int
    ) -> dict[int, BlockValueSignature]:
        """Execute all blocks in a function.

        Returns dict mapping block_addr -> BlockValueSignature.
        """
        blocks = self.loader.get_blocks_for_function(func_addr)
        result = {}

        for addr, block in blocks:
            sig = self.execute_block(addr, block)
            if sig is not None:
                result[addr] = sig

        return result

    def _run_concrete(
        self, block_addr: int, block: angr.block.Block,
        test_input: list[int]
    ) -> tuple | None:
        """Execute a block with concrete register values.

        Returns (pre_regs, post_regs, mem_accesses, dataflow_edges) or None.
        """
        try:
            state = self.proj.factory.blank_state(
                addr=block_addr,
                add_options={
                    angr.sim_options.ZERO_FILL_UNCONSTRAINED_MEMORY,
                    angr.sim_options.ZERO_FILL_UNCONSTRAINED_REGISTERS,
                    angr.sim_options.TRACK_MEMORY_ACTIONS,
                },
            )

            # Initialize stack pointer
            setattr(state.regs, self._arch.sp_reg,
                    claripy.BVV(self._arch.stack_base,
                                     self._arch.ptr_size * 8))

            # Initialize general-purpose registers with test values
            pre_regs = {}
            gp_regs = self._arch.gp_regs
            for i, reg in enumerate(gp_regs):
                val = test_input[i % len(test_input)]
                try:
                    setattr(state.regs, reg,
                            claripy.BVV(val, self._arch.ptr_size * 8))
                    pre_regs[reg] = val
                except Exception:
                    pass

            # Fill stack with sentinel pattern
            sp_val = self._arch.stack_base
            for offset in range(0, 0x100, self._arch.ptr_size):
                sentinel = 0xDEAD0000 + offset
                state.memory.store(
                    sp_val - offset,
                    claripy.BVV(sentinel, self._arch.ptr_size * 8),
                    endness=self.proj.arch.memory_endness,
                )

            # Step through the block
            num_insns = len(list(block.capstone.insns))
            simgr = self.proj.factory.simgr(state)
            simgr.step(num_inst=num_insns)

            if not simgr.active:
                # Execution ended (deadended, errored, etc.)
                # Try to read from deadended states
                if simgr.deadended:
                    post_state = simgr.deadended[0]
                else:
                    return None
            else:
                post_state = simgr.active[0]

            # Read post-execution register values
            post_regs = {}
            for reg in gp_regs:
                try:
                    val = getattr(post_state.regs, reg)
                    if val.concrete:
                        post_regs[reg] = post_state.solver.eval(val)
                except Exception:
                    pass

            # Detect memory accesses by checking state history
            mem_accesses = self._extract_mem_accesses(state, post_state)

            # Build dataflow edges
            df_edges = self._compute_dataflow(pre_regs, post_regs)

            return pre_regs, post_regs, mem_accesses, df_edges

        except Exception as e:
            logger.debug('Block execution failed at 0x%x: %s', block_addr, e)
            return None

    def _extract_opcode_sequence(self, block: angr.block.Block) -> list[str]:
        """Extract normalized opcode sequence from a block."""
        opcodes = []
        for insn in block.capstone.insns:
            normalized = normalize_opcode(insn.mnemonic)
            if normalized != 'nop':
                opcodes.append(normalized)
        return opcodes

    def _extract_constants(self, block: angr.block.Block) -> list[int]:
        """Extract constant immediates from block instructions."""
        constants = []
        for insn in block.capstone.insns:
            for op in insn.operands:
                # Capstone immediate operands
                if hasattr(op, 'imm') and op.type == 2:  # IMM type
                    val = op.imm
                    # Filter out small branch offsets and very common values
                    if abs(val) > 1 and not self._is_address(val):
                        constants.append(val)
        return constants

    def _is_address(self, val: int) -> bool:
        """Check if a value looks like a code or data address."""
        if self._text_range[0] <= val <= self._text_range[1]:
            return True
        for lo, hi in self._data_ranges:
            if lo <= val <= hi:
                return True
        return False

    def _extract_mem_accesses(
        self, pre_state, post_state
    ) -> list[MemoryAccess]:
        """Extract memory accesses from state history."""
        accesses = []
        sp_val = self._arch.stack_base
        try:
            for action in post_state.history.actions:
                if action.type == 'mem':
                    addr_val = action.addr.ast
                    if addr_val.concrete:
                        addr = post_state.solver.eval(addr_val)
                        size = action.size.ast
                        if size.concrete:
                            size_val = post_state.solver.eval(size) // 8
                        else:
                            size_val = self._arch.ptr_size
                        is_write = action.action == 'write'
                        kind = self._classify_addr(addr, sp_val)
                        accesses.append(MemoryAccess(
                            offset=addr - sp_val if kind == ValueKind.STACK_OFFSET else addr,
                            size=size_val,
                            is_write=is_write,
                            kind=kind,
                        ))
        except Exception:
            pass
        return accesses

    def _classify_addr(self, addr: int, sp_val: int) -> ValueKind:
        """Classify a memory address."""
        if self._arch.is_stack_addr(addr):
            return ValueKind.STACK_OFFSET
        if self._arch.is_code_addr(addr, self._text_range):
            return ValueKind.CODE_ADDR
        if self._arch.is_global_addr(addr, self._data_ranges):
            return ValueKind.GLOBAL_ADDR
        return ValueKind.CONSTANT

    def _compute_dataflow(
        self, pre_regs: dict[str, int], post_regs: dict[str, int]
    ) -> set[tuple[str, str]]:
        """Compute dataflow edges by observing which outputs depend on inputs.

        Uses a simple heuristic: if a post-register value is arithmetically
        related to a pre-register value, record a dataflow edge.
        """
        edges = set()
        for out_reg, out_val in post_regs.items():
            out_role = self._arch.normalize_register(out_reg)
            for in_reg, in_val in pre_regs.items():
                in_role = self._arch.normalize_register(in_reg)
                if in_val == 0:
                    continue
                # Check common arithmetic relationships
                if out_val == in_val:
                    edges.add((out_role, in_role))
                elif out_val == in_val + 1 or out_val == in_val - 1:
                    edges.add((out_role, in_role))
                elif in_val != 0 and out_val % in_val == 0:
                    edges.add((out_role, in_role))
                elif out_val == in_val << 1 or out_val == in_val >> 1:
                    edges.add((out_role, in_role))
        return edges

    def _deduplicate_mem_accesses(
        self, accesses: list[MemoryAccess]
    ) -> list[MemoryAccess]:
        """Deduplicate memory accesses across test runs."""
        seen = set()
        result = []
        for ma in accesses:
            key = (ma.offset, ma.size, ma.is_write, ma.kind)
            if key not in seen:
                seen.add(key)
                result.append(ma)
        return sorted(result, key=lambda m: (m.offset, m.is_write))

    def _extract_callee_names(self, block: angr.block.Block) -> list[str]:
        """Extract demangled names of functions called from this block."""
        callees = []
        for insn in block.capstone.insns:
            if insn.mnemonic in ('call', 'callq', 'bl', 'blr'):
                # Try to get immediate target address
                if insn.operands and insn.operands[0].type == 2:  # IMM
                    target_addr = insn.operands[0].imm
                    name = self.loader.get_demangled_name(target_addr)
                    if name:
                        callees.append(name)
                    else:
                        callees.append(f'sub_{target_addr:x}')
        return callees

    def _extract_string_refs(self, block: angr.block.Block) -> list[str]:
        """Extract string constant references from LEA instructions."""
        strings = []
        rodata = self.loader.get_section_range('.rodata')
        if not rodata:
            return strings

        ro_lo, ro_hi = rodata
        for insn in block.capstone.insns:
            if insn.mnemonic not in ('lea', 'adr', 'adrp'):
                continue
            for op in insn.operands:
                if not (hasattr(op, 'mem') and hasattr(op.mem, 'disp')):
                    continue
                # RIP-relative addressing: target = insn_addr + insn_size + disp
                target_addr = insn.address + insn.size + op.mem.disp
                if ro_lo <= target_addr <= ro_hi:
                    try:
                        raw = self.proj.loader.memory.load(target_addr, 128)
                        null_idx = raw.index(b'\x00') if b'\x00' in raw else 128
                        s = raw[:null_idx].decode('utf-8', errors='replace')
                        if s and len(s) > 1:
                            strings.append(s[:80])
                    except Exception:
                        pass
        return strings
