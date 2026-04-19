"""Rust binary loader wrapping vSim's BinExecutor."""

import logging
import networkx as nx

import rustdiff  # noqa: F401  -- triggers vSim sys.path setup

from src.bin_executor import BinExecutor
from rustdiff.rust.demangle import RustDemangler
from rustdiff.rust.filter import RustFunctionFilter, FunctionCategory
from rustdiff.rust.monomorphize import MonomorphizationGrouper

logger = logging.getLogger(__name__)


class RustBinaryLoader:
    """Load a Rust binary and provide demangled, filtered function access.

    Wraps vSim's BinExecutor for angr Project, CFGFast, and function range
    management. Adds Rust symbol demangling, function filtering, and
    monomorphization grouping on top.
    """

    def __init__(self, bin_path: str, load_debug_info: bool = False,
                 include_stdlib: bool = False):
        logger.info('Loading binary: %s', bin_path)
        self.bin_path = bin_path
        self.be = BinExecutor(bin_path, load_debug_info=load_debug_info)
        self.demangler = RustDemangler()
        self.filter = RustFunctionFilter(include_stdlib=include_stdlib)
        self.grouper = MonomorphizationGrouper()
        self._build_func_map()

    def _build_func_map(self):
        """Build addr -> (mangled, demangled, category) mapping."""
        self._func_map = {}

        # Collect all mangled names
        mangled_names = []
        addrs = []
        for addr in self.be.func_with_symbols:
            name = self.be.get_symbol_name_from_addr(addr)
            mangled_names.append(name)
            addrs.append(addr)

        # Batch demangle
        demangled_names = self.demangler.demangle_batch(mangled_names)

        for addr, mangled, demangled in zip(addrs, mangled_names, demangled_names):
            category = self.filter.categorize(demangled)
            self._func_map[addr] = {
                'mangled': mangled,
                'demangled': demangled,
                'normalized': self.demangler.normalize_for_matching(demangled),
                'category': category,
            }

        logger.info(
            'Loaded %d functions (%d user, %d stdlib, %d generated, %d other)',
            len(self._func_map),
            sum(1 for f in self._func_map.values()
                if f['category'] == FunctionCategory.USER),
            sum(1 for f in self._func_map.values()
                if f['category'] == FunctionCategory.STDLIB),
            sum(1 for f in self._func_map.values()
                if f['category'] == FunctionCategory.GENERATED),
            sum(1 for f in self._func_map.values()
                if f['category'] in (FunctionCategory.ALLOC,
                                     FunctionCategory.UNKNOWN)),
        )

    @property
    def proj(self):
        return self.be.proj

    @property
    def arch(self):
        return self.be.proj.arch

    @property
    def arch_name(self) -> str:
        return self.be.proj.arch.name

    def get_func_info(self, addr: int) -> dict | None:
        """Get full info dict for a function address."""
        return self._func_map.get(addr)

    def get_demangled_name(self, addr: int) -> str:
        """Get demangled name for a function address."""
        info = self._func_map.get(addr)
        if info:
            return info['demangled']
        return self.be.get_symbol_name_from_addr(addr)

    def get_normalized_name(self, addr: int) -> str:
        """Get type-erased normalized name for matching."""
        info = self._func_map.get(addr)
        if info:
            return info['normalized']
        return self.be.get_symbol_name_from_addr(addr)

    def get_analyzable_functions(self) -> list[tuple[int, str]]:
        """Return (addr, demangled_name) for functions passing the filter."""
        result = []
        for addr, info in self._func_map.items():
            if self.filter.should_analyze(info['demangled']):
                result.append((addr, info['demangled']))
        return result

    def get_all_functions(self) -> list[tuple[int, str]]:
        """Return (addr, demangled_name) for all functions."""
        return [(addr, info['demangled'])
                for addr, info in self._func_map.items()]

    def get_cfg_for_function(self, func_addr: int) -> nx.DiGraph:
        """Extract the CFG for a single function as a DiGraph.

        Nodes are basic block addresses. Edges represent control flow.
        Uses both angr's successor info and fall-through inference to
        capture edges that angr's CFGFast misses (e.g., call fall-throughs).
        """
        if func_addr not in self.be.fast_cfg.functions:
            return nx.DiGraph()

        func = self.be.fast_cfg.functions[func_addr]
        g = nx.DiGraph()
        block_addrs_set = set(func.block_addrs)

        for block_addr in func.block_addrs:
            node = self.be.get_fast_cfg_node(block_addr)
            if node is None or node.block is None:
                g.add_node(block_addr, size=0, num_insns=0)
                continue
            g.add_node(
                block_addr,
                size=node.block.size,
                num_insns=len(list(node.block.capstone.insns)),
            )

        for block_addr in func.block_addrs:
            # Add edges from angr's CFG successors (within this function)
            for succ_addr in self.be.get_bb_successors(block_addr):
                if succ_addr in g:
                    g.add_edge(block_addr, succ_addr)

            # Add fall-through edge: block_addr + block_size -> next block
            node = self.be.get_fast_cfg_node(block_addr)
            if node is not None and node.block is not None:
                fall_through = block_addr + node.block.size
                if fall_through in block_addrs_set and fall_through != block_addr:
                    g.add_edge(block_addr, fall_through)

        return g

    def get_blocks_for_function(self, func_addr: int) -> list:
        """Get angr Block objects for all basic blocks in a function.

        Returns list of (block_addr, angr.Block) pairs for all blocks
        in the function, sorted by address.
        """
        if func_addr not in self.be.fast_cfg.functions:
            return []

        func = self.be.fast_cfg.functions[func_addr]
        blocks = []

        for addr in sorted(func.block_addrs):
            node = self.be.get_fast_cfg_node(addr)
            if node is not None and node.block is not None:
                blocks.append((addr, node.block))

        return blocks

    def get_callees_for_function(self, func_addr: int) -> list[str]:
        """Get demangled names of functions called from the given function.

        Inspects call-type instructions in each block to identify callee
        addresses, then resolves them to demangled names.
        """
        if func_addr not in self.be.fast_cfg.functions:
            return []

        func = self.be.fast_cfg.functions[func_addr]
        callee_names = []
        seen_addrs = set()

        for block_addr in func.block_addrs:
            node = self.be.get_fast_cfg_node(block_addr)
            if node is None or node.block is None:
                continue
            block = node.block
            for insn in block.capstone.insns:
                mnemonic = insn.mnemonic.lower()
                if mnemonic in ('call', 'bl', 'blr', 'jal', 'jalr'):
                    # Try to resolve the call target
                    for op in insn.operands:
                        if hasattr(op, 'imm') and op.type == 2:
                            target = op.imm
                            if target not in seen_addrs:
                                seen_addrs.add(target)
                                name = self.get_demangled_name(target)
                                if name:
                                    callee_names.append(name)

        return callee_names

    def get_callees_for_block(self, block_addr: int) -> list[str]:
        """Get demangled names of functions called from a specific block."""
        node = self.be.get_fast_cfg_node(block_addr)
        if node is None or node.block is None:
            return []

        callee_names = []
        block = node.block
        for insn in block.capstone.insns:
            mnemonic = insn.mnemonic.lower()
            if mnemonic in ('call', 'bl', 'blr', 'jal', 'jalr'):
                for op in insn.operands:
                    if hasattr(op, 'imm') and op.type == 2:
                        target = op.imm
                        name = self.get_demangled_name(target)
                        if name:
                            callee_names.append(name)
        return callee_names

    def get_string_refs_for_function(self, func_addr: int) -> list[str]:
        """Extract string constants referenced by blocks in the function.

        Looks for LEA/ADR instructions referencing .rodata addresses, then
        reads the pointed-to string from the binary.
        """
        if func_addr not in self.be.fast_cfg.functions:
            return []

        rodata_range = self.get_section_range('.rodata')
        if rodata_range is None:
            return []

        func = self.be.fast_cfg.functions[func_addr]
        strings = []
        seen_addrs = set()

        for block_addr in func.block_addrs:
            block_strings = self._extract_block_strings(
                block_addr, rodata_range, seen_addrs
            )
            strings.extend(block_strings)

        return strings

    def get_string_refs_for_block(
        self, block_addr: int, rodata_range: tuple[int, int] | None = None
    ) -> list[str]:
        """Extract string constants referenced by a specific block."""
        if rodata_range is None:
            rodata_range = self.get_section_range('.rodata')
        if rodata_range is None:
            return []
        return self._extract_block_strings(block_addr, rodata_range, set())

    def _extract_block_strings(
        self,
        block_addr: int,
        rodata_range: tuple[int, int],
        seen_addrs: set[int],
    ) -> list[str]:
        """Read string constants from instructions that reference .rodata."""
        node = self.be.get_fast_cfg_node(block_addr)
        if node is None or node.block is None:
            return []

        strings = []
        block = node.block
        for insn in block.capstone.insns:
            mnemonic = insn.mnemonic.lower()
            if mnemonic not in ('lea', 'adr', 'adrp', 'mov', 'movabs'):
                continue
            for op in insn.operands:
                if hasattr(op, 'imm') and op.type == 2:
                    addr = op.imm
                    if (rodata_range[0] <= addr <= rodata_range[1]
                            and addr not in seen_addrs):
                        seen_addrs.add(addr)
                        s = self._read_string_at(addr)
                        if s:
                            strings.append(s)
        return strings

    def _read_string_at(self, addr: int, max_len: int = 256) -> str | None:
        """Read a null-terminated or length-prefixed string from binary."""
        try:
            data = self.be.proj.loader.memory.load(addr, max_len)
            # Try null-terminated
            nul = data.find(b'\x00')
            if nul > 0:
                s = data[:nul].decode('utf-8', errors='replace')
                # Filter to printable strings of reasonable length
                if len(s) >= 4 and s.isprintable():
                    return s
        except Exception:
            pass
        return None

    def get_section_range(self, section_name: str) -> tuple[int, int] | None:
        """Get (start, end) address range of a section."""
        section = self.be.proj.loader.main_object.sections_map.get(section_name)
        if section is None:
            return None
        return (section.min_addr, section.max_addr)
