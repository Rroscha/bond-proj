"""Filter Rust standard library and compiler-generated functions."""

import re
from enum import Enum


class FunctionCategory(str, Enum):
    USER = 'user'
    STDLIB = 'stdlib'
    ALLOC = 'alloc'
    GENERATED = 'generated'
    UNKNOWN = 'unknown'


# Prefixes indicating standard library / runtime functions
_STDLIB_PREFIXES = (
    'core::',
    'std::',
    'alloc::',
    'compiler_builtins::',
    'hashbrown::',
    'rustc_demangle::',
    '<core::',
    '<alloc::',
    '<std::',
    '<hashbrown::',
    'panic_',
    '__rust_',
    'rust_begin_unwind',
    'rust_eh_personality',
    'rust_oom',
)

_ALLOC_PREFIXES = (
    'alloc::',
    '<alloc::',
    '__rdl_',
    '__rg_',
)

# Patterns for compiler-generated code
_GENERATED_PATTERNS = [
    re.compile(r'^core::ptr::drop_in_place<'),
    re.compile(r'^<.*\s+as\s+core::ops::drop::Drop>::drop$'),
    re.compile(r'^__rdl_'),
    re.compile(r'^__rg_'),
    re.compile(r'^\$'),
    re.compile(r'^GCC_except_table'),
    re.compile(r'^\.L'),
]

# Patterns for panic/unwinding infrastructure
_PANIC_PATTERNS = [
    re.compile(r'core::panicking::'),
    re.compile(r'std::panicking::'),
    re.compile(r'std::sys::backtrace::'),
    re.compile(r'core::fmt::write'),
    re.compile(r'^rust_begin_unwind'),
]


class RustFunctionFilter:
    """Filter and categorize Rust binary functions."""

    def __init__(self, include_stdlib: bool = False,
                 include_generated: bool = False):
        self.include_stdlib = include_stdlib
        self.include_generated = include_generated

    def should_analyze(self, demangled_name: str) -> bool:
        """Return True if this function should be included in analysis."""
        cat = self.categorize(demangled_name)
        if cat == FunctionCategory.USER:
            return True
        if cat == FunctionCategory.UNKNOWN:
            return True
        if cat == FunctionCategory.STDLIB and self.include_stdlib:
            return True
        if cat == FunctionCategory.GENERATED and self.include_generated:
            return True
        return False

    def categorize(self, demangled_name: str) -> FunctionCategory:
        """Categorize a demangled function name."""
        if not demangled_name:
            return FunctionCategory.UNKNOWN

        for pat in _GENERATED_PATTERNS:
            if pat.search(demangled_name):
                return FunctionCategory.GENERATED

        if demangled_name.startswith(_ALLOC_PREFIXES):
            return FunctionCategory.ALLOC

        if demangled_name.startswith(_STDLIB_PREFIXES):
            return FunctionCategory.STDLIB

        for pat in _PANIC_PATTERNS:
            if pat.search(demangled_name):
                return FunctionCategory.STDLIB

        # If it still looks like a Rust path with known crate prefixes
        # but wasn't caught above, treat as user code
        return FunctionCategory.USER

    def is_panic_path(self, demangled_name: str) -> bool:
        """Check if a function is part of panic/unwinding infrastructure."""
        return any(p.search(demangled_name) for p in _PANIC_PATTERNS)
