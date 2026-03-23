"""Data classes for block-level and function-level value signatures."""

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Optional


class ValueKind(IntEnum):
    """Classification of an observed value during micro-execution."""
    CONSTANT = 0
    STACK_OFFSET = 1
    GLOBAL_ADDR = 2
    CODE_ADDR = 3
    COMPUTED = 4
    INPUT_PASSTHROUGH = 5


# Normalized opcode categories for architecture-neutral representation
OPCODE_CATEGORIES = {
    # Data movement
    'mov': 'mov', 'movzx': 'mov', 'movsx': 'mov', 'movsxd': 'mov',
    'movabs': 'mov', 'cmov': 'cmov', 'cmove': 'cmov', 'cmovne': 'cmov',
    'cmovl': 'cmov', 'cmovg': 'cmov', 'cmovle': 'cmov', 'cmovge': 'cmov',
    'ldr': 'mov', 'str': 'store', 'ldp': 'mov', 'stp': 'store',
    'lw': 'mov', 'sw': 'store', 'lb': 'mov', 'sb': 'store',
    # Arithmetic
    'add': 'add', 'sub': 'sub', 'mul': 'mul', 'imul': 'mul',
    'div': 'div', 'idiv': 'div', 'neg': 'neg', 'inc': 'add', 'dec': 'sub',
    'adc': 'add', 'sbb': 'sub',
    'madd': 'mul', 'msub': 'mul',
    # Bitwise
    'and': 'and', 'or': 'or', 'xor': 'xor', 'not': 'not',
    'shl': 'shl', 'shr': 'shr', 'sar': 'shr', 'rol': 'rol', 'ror': 'ror',
    'lsl': 'shl', 'lsr': 'shr', 'asr': 'shr',
    # Comparison / test
    'cmp': 'cmp', 'test': 'cmp', 'tst': 'cmp',
    # Control flow
    'call': 'call', 'bl': 'call', 'blr': 'call', 'jal': 'call',
    'ret': 'ret', 'retn': 'ret',
    'jmp': 'jmp', 'je': 'jcc', 'jne': 'jcc', 'jl': 'jcc', 'jg': 'jcc',
    'jle': 'jcc', 'jge': 'jcc', 'ja': 'jcc', 'jb': 'jcc',
    'jae': 'jcc', 'jbe': 'jcc', 'js': 'jcc', 'jns': 'jcc',
    'b': 'jmp', 'b.eq': 'jcc', 'b.ne': 'jcc', 'b.lt': 'jcc',
    'b.gt': 'jcc', 'b.le': 'jcc', 'b.ge': 'jcc',
    'cbz': 'jcc', 'cbnz': 'jcc', 'tbz': 'jcc', 'tbnz': 'jcc',
    'beq': 'jcc', 'bne': 'jcc',
    # Stack
    'push': 'push', 'pop': 'pop',
    # LEA / address computation
    'lea': 'lea', 'adr': 'lea', 'adrp': 'lea',
    # Nop
    'nop': 'nop',
}


def normalize_opcode(mnemonic: str) -> str:
    """Map an architecture-specific mnemonic to a normalized category."""
    m = mnemonic.lower().strip()
    if m in OPCODE_CATEGORIES:
        return OPCODE_CATEGORIES[m]
    # Check prefix matches for conditional moves, etc.
    for prefix in ('cmov', 'set', 'b.'):
        if m.startswith(prefix):
            return OPCODE_CATEGORIES.get(prefix, m)
    return m


@dataclass
class MemoryAccess:
    """A single memory access observed during block execution."""
    offset: int          # Offset from stack pointer (or absolute if global)
    size: int            # Access size in bytes
    is_write: bool       # True for store, False for load
    kind: ValueKind      # STACK_OFFSET, GLOBAL_ADDR, etc.


@dataclass
class BlockValueSignature:
    """Architecture-neutral signature for a single basic block.

    Produced by concrete micro-execution with multiple test input sets.
    """
    block_addr: int
    num_instructions: int

    # Constant immediates appearing in the block (deduplicated, sorted)
    constants: tuple[int, ...] = ()

    # Normalized opcode sequence
    opcode_sequence: tuple[str, ...] = ()

    # Memory access pattern
    memory_pattern: tuple[MemoryAccess, ...] = ()

    # Register dataflow: (output_reg_class, input_reg_class) pairs
    dataflow_edges: frozenset[tuple[str, str]] = frozenset()

    # Concrete output values per output register across test inputs
    # Maps normalized reg name -> tuple of observed values
    concrete_outputs: dict[str, tuple[int, ...]] = field(default_factory=dict)

    # Branch factor
    out_degree: int = 0

    # Callee names: demangled names of functions called from this block
    callee_names: tuple[str, ...] = ()

    # String references: string constants referenced by this block
    string_refs: tuple[str, ...] = ()

    def to_feature_set(self) -> frozenset:
        """Convert to a set of hashable features for Jaccard similarity."""
        features = set()
        # Constants as features
        for c in self.constants:
            features.add(('const', c))
        # Opcode bigrams
        for i in range(len(self.opcode_sequence) - 1):
            features.add(('op2', self.opcode_sequence[i],
                          self.opcode_sequence[i + 1]))
        # Individual opcodes
        for op in self.opcode_sequence:
            features.add(('op', op))
        # Memory access pattern features
        for ma in self.memory_pattern:
            features.add(('mem', ma.kind.name, ma.size, ma.is_write))
        # Dataflow edges
        for edge in self.dataflow_edges:
            features.add(('df', edge[0], edge[1]))
        # Concrete value features (use sorted tuples for determinism)
        for reg, vals in sorted(self.concrete_outputs.items()):
            for v in vals:
                features.add(('val', reg, v))

        # Callee name features
        for name in self.callee_names:
            features.add(('call', name))

        # String reference features
        for s in self.string_refs:
            features.add(('str', s))

        return frozenset(features)

    @property
    def opcode_histogram(self) -> dict[str, int]:
        """Count of each normalized opcode in this block."""
        hist = {}
        for op in self.opcode_sequence:
            hist[op] = hist.get(op, 0) + 1
        return hist
