"""Group monomorphized instances of Rust generic functions."""

import re
from collections import defaultdict


# Type parameter patterns in demangled names
_TYPE_PARAMS_RE = re.compile(r'<[^<>]*>')


class MonomorphizationGrouper:
    """Group monomorphized instances back to their generic source function.

    Rust monomorphizes generics: Vec<u8>::push and Vec<String>::push
    become separate binary functions. This class groups them by their
    generic parent for matching purposes.
    """

    @staticmethod
    def erase_types(demangled_name: str) -> str:
        """Erase type parameters to get a canonical generic form.

        Examples:
            'alloc::vec::Vec<u8>::push' -> 'alloc::vec::Vec::push'
            'core::option::Option<T>::unwrap' -> 'core::option::Option::unwrap'
            '<serde::de::Deserialize<T> as ...>' -> '<serde::de::Deserialize as ...>'
        """
        prev = None
        result = demangled_name
        while prev != result:
            prev = result
            result = _TYPE_PARAMS_RE.sub('', result)
        # Clean up any resulting double colons
        result = re.sub(r'::+', '::', result)
        return result.strip(':')

    def group_by_generic(
        self, func_names: list[tuple[int, str]]
    ) -> dict[str, list[tuple[int, str]]]:
        """Group functions by their type-erased generic parent.

        Args:
            func_names: List of (address, demangled_name) pairs.

        Returns:
            Dict mapping canonical name -> list of (addr, original_name).
        """
        groups = defaultdict(list)
        for addr, name in func_names:
            canonical = self.erase_types(name)
            groups[canonical].append((addr, name))
        return dict(groups)

    def are_monomorphic_siblings(self, name1: str, name2: str) -> bool:
        """Check if two function names are instances of the same generic."""
        return self.erase_types(name1) == self.erase_types(name2)

    def get_monomorphized_sets(
        self, func_names: list[tuple[int, str]]
    ) -> list[list[tuple[int, str]]]:
        """Return only the groups with more than one instance.

        These are the monomorphized sets where a single generic function
        produced multiple binary functions.
        """
        groups = self.group_by_generic(func_names)
        return [g for g in groups.values() if len(g) > 1]
