"""Rust symbol demangling using rustfilt."""

import re
import shutil
import subprocess
import logging

logger = logging.getLogger(__name__)

# Rust hash suffix: ::h followed by 16 hex chars at end of symbol
_HASH_SUFFIX_RE = re.compile(r'::h[0-9a-f]{16}$')

# Type parameters inside angle brackets (greedy, nested)
_TYPE_PARAMS_RE = re.compile(r'<[^<>]*>')

# Crate name is the first path component
_CRATE_NAME_RE = re.compile(r'^([a-zA-Z_][a-zA-Z0-9_]*)')


class RustDemangler:
    """Demangle Rust symbols using rustfilt CLI tool."""

    def __init__(self):
        self._rustfilt_path = shutil.which('rustfilt')
        if not self._rustfilt_path:
            logger.warning(
                'rustfilt not found in PATH. '
                'Install with: cargo install rustfilt'
            )
        self._cache = {}

    def demangle(self, mangled: str) -> str:
        """Demangle a single Rust symbol.

        Returns the demangled name, or the original if demangling fails.
        """
        if mangled in self._cache:
            return self._cache[mangled]

        result = self._demangle_via_rustfilt(mangled)
        self._cache[mangled] = result
        return result

    def demangle_batch(self, symbols: list[str]) -> list[str]:
        """Demangle a batch of symbols in one rustfilt invocation."""
        if not self._rustfilt_path:
            return symbols

        uncached = [s for s in symbols if s not in self._cache]
        if uncached:
            try:
                proc = subprocess.run(
                    [self._rustfilt_path],
                    input='\n'.join(uncached),
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
                if proc.returncode == 0:
                    results = proc.stdout.strip().split('\n')
                    for mangled_sym, demangled in zip(uncached, results):
                        self._cache[mangled_sym] = demangled
            except (subprocess.TimeoutExpired, OSError) as e:
                logger.warning('rustfilt batch demangling failed: %s', e)

        return [self._cache.get(s, s) for s in symbols]

    def _demangle_via_rustfilt(self, mangled: str) -> str:
        if not self._rustfilt_path:
            return mangled
        try:
            proc = subprocess.run(
                [self._rustfilt_path],
                input=mangled,
                capture_output=True,
                text=True,
                timeout=5,
            )
            if proc.returncode == 0:
                return proc.stdout.strip()
        except (subprocess.TimeoutExpired, OSError):
            pass
        return mangled

    @staticmethod
    def normalize_for_matching(demangled: str) -> str:
        """Normalize a demangled symbol for matching.

        Strips:
        - Hash suffixes (::h<hex16>)
        - Type parameters (<T>, <&str, u32>, etc.)
        - Closure markers ({{closure}}, {{closure#0}})
        """
        name = _HASH_SUFFIX_RE.sub('', demangled)
        # Iteratively strip nested type params: Vec<Option<T>> -> Vec
        prev = None
        while prev != name:
            prev = name
            name = _TYPE_PARAMS_RE.sub('', name)
        # Strip closure annotations
        name = re.sub(r'::\{\{closure(#\d+)?\}\}', '', name)
        return name.strip()

    @staticmethod
    def extract_crate_name(demangled: str) -> str | None:
        """Extract the top-level crate name from a demangled symbol."""
        m = _CRATE_NAME_RE.match(demangled)
        return m.group(1) if m else None

    @staticmethod
    def is_rust_symbol(mangled: str) -> bool:
        """Check if a mangled symbol looks like a Rust symbol."""
        return mangled.startswith('_ZN') or mangled.startswith('_R')
