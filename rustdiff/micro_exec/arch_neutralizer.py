"""Architecture-neutral register and memory normalization."""


# Per-architecture register role mappings
_ARCH_CONFIGS = {
    'AMD64': {
        'arg_regs': ['rdi', 'rsi', 'rdx', 'rcx', 'r8', 'r9'],
        'ret_regs': ['rax'],
        'callee_saved': ['rbx', 'r12', 'r13', 'r14', 'r15', 'rbp'],
        'caller_saved': ['rax', 'rcx', 'rdx', 'rsi', 'rdi',
                         'r8', 'r9', 'r10', 'r11'],
        'sp': 'rsp',
        'bp': 'rbp',
        'ptr_size': 8,
        'gp_regs': ['rax', 'rbx', 'rcx', 'rdx', 'rsi', 'rdi',
                     'r8', 'r9', 'r10', 'r11', 'r12', 'r13', 'r14', 'r15'],
        'stack_base': 0x7ffffffffff0000,
        'stack_bottom': 0x7fffffffff000,
    },
    'X86': {
        'arg_regs': [],  # cdecl passes on stack
        'ret_regs': ['eax'],
        'callee_saved': ['ebx', 'esi', 'edi', 'ebp'],
        'caller_saved': ['eax', 'ecx', 'edx'],
        'sp': 'esp',
        'bp': 'ebp',
        'ptr_size': 4,
        'gp_regs': ['eax', 'ebx', 'ecx', 'edx', 'esi', 'edi'],
        'stack_base': 0xfffff0000,
        'stack_bottom': 0xfffff000,
    },
    'AARCH64': {
        'arg_regs': [f'x{i}' for i in range(8)],
        'ret_regs': ['x0'],
        'callee_saved': [f'x{i}' for i in range(19, 29)] + ['x29'],
        'caller_saved': [f'x{i}' for i in range(18)],
        'sp': 'sp',
        'bp': 'x29',
        'ptr_size': 8,
        'gp_regs': [f'x{i}' for i in range(31)],
        'stack_base': 0x7ffffffffff0000,
        'stack_bottom': 0x7fffffffff000,
    },
    'ARMEL': {
        'arg_regs': ['r0', 'r1', 'r2', 'r3'],
        'ret_regs': ['r0'],
        'callee_saved': ['r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11'],
        'caller_saved': ['r0', 'r1', 'r2', 'r3', 'r12'],
        'sp': 'sp',
        'bp': 'r11',
        'ptr_size': 4,
        'gp_regs': [f'r{i}' for i in range(13)],
        'stack_base': 0xfffff0000,
        'stack_bottom': 0xfffff000,
    },
    'ARMHF': {
        'arg_regs': ['r0', 'r1', 'r2', 'r3'],
        'ret_regs': ['r0'],
        'callee_saved': ['r4', 'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r11'],
        'caller_saved': ['r0', 'r1', 'r2', 'r3', 'r12'],
        'sp': 'sp',
        'bp': 'r11',
        'ptr_size': 4,
        'gp_regs': [f'r{i}' for i in range(13)],
        'stack_base': 0xfffff0000,
        'stack_bottom': 0xfffff000,
    },
    'MIPS32': {
        'arg_regs': ['a0', 'a1', 'a2', 'a3'],
        'ret_regs': ['v0'],
        'callee_saved': ['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7'],
        'caller_saved': ['a0', 'a1', 'a2', 'a3', 't0', 't1', 't2', 't3',
                         't4', 't5', 't6', 't7', 't8', 't9', 'v0', 'v1'],
        'sp': 'sp',
        'bp': 'fp',
        'ptr_size': 4,
        'gp_regs': (['v0', 'v1', 'a0', 'a1', 'a2', 'a3'] +
                    [f't{i}' for i in range(10)] +
                    [f's{i}' for i in range(8)]),
        'stack_base': 0xfffff0000,
        'stack_bottom': 0xfffff000,
    },
    'MIPS64': {
        'arg_regs': ['a0', 'a1', 'a2', 'a3'],
        'ret_regs': ['v0'],
        'callee_saved': ['s0', 's1', 's2', 's3', 's4', 's5', 's6', 's7'],
        'caller_saved': ['a0', 'a1', 'a2', 'a3', 't0', 't1', 't2', 't3',
                         't4', 't5', 't6', 't7', 't8', 't9', 'v0', 'v1'],
        'sp': 'sp',
        'bp': 'fp',
        'ptr_size': 8,
        'gp_regs': (['v0', 'v1', 'a0', 'a1', 'a2', 'a3'] +
                    [f't{i}' for i in range(10)] +
                    [f's{i}' for i in range(8)]),
        'stack_base': 0x7ffffffffff0000,
        'stack_bottom': 0x7fffffffff000,
    },
}


class ArchNeutralizer:
    """Normalize architecture-specific register names to neutral roles."""

    def __init__(self, arch_name: str):
        self.arch_name = arch_name
        if arch_name not in _ARCH_CONFIGS:
            raise ValueError(f'Unsupported architecture: {arch_name}')
        self._config = _ARCH_CONFIGS[arch_name]
        self._reg_to_role = self._build_role_map()

    def _build_role_map(self) -> dict[str, str]:
        """Build register name -> neutral role mapping."""
        mapping = {}
        for i, reg in enumerate(self._config['arg_regs']):
            mapping[reg] = f'arg{i}'
        for i, reg in enumerate(self._config['ret_regs']):
            mapping[reg] = f'ret{i}'
        for i, reg in enumerate(self._config['callee_saved']):
            mapping[reg] = f'saved{i}'
        mapping[self._config['sp']] = 'sp'
        mapping[self._config['bp']] = 'bp'
        return mapping

    def normalize_register(self, reg_name: str) -> str:
        """Map an arch-specific register name to a neutral role name."""
        return self._reg_to_role.get(reg_name, reg_name)

    @property
    def arg_regs(self) -> list[str]:
        return self._config['arg_regs']

    @property
    def ret_regs(self) -> list[str]:
        return self._config['ret_regs']

    @property
    def gp_regs(self) -> list[str]:
        return self._config['gp_regs']

    @property
    def sp_reg(self) -> str:
        return self._config['sp']

    @property
    def bp_reg(self) -> str:
        return self._config['bp']

    @property
    def ptr_size(self) -> int:
        return self._config['ptr_size']

    @property
    def stack_base(self) -> int:
        return self._config['stack_base']

    @property
    def stack_bottom(self) -> int:
        return self._config['stack_bottom']

    def is_stack_addr(self, addr: int) -> bool:
        """Check if an address is within the simulated stack region."""
        return abs(addr - self.stack_bottom) < 0x10000

    def is_code_addr(self, addr: int, text_range: tuple[int, int]) -> bool:
        """Check if an address falls within .text section."""
        return text_range[0] <= addr <= text_range[1]

    def is_global_addr(self, addr: int,
                       data_ranges: list[tuple[int, int]]) -> bool:
        """Check if an address falls within a data section."""
        return any(lo <= addr <= hi for lo, hi in data_ranges)
