"""Generate function-level matching groundtruth from debug symbols."""

import logging
from collections import defaultdict

from rustdiff.loader import RustBinaryLoader
from rustdiff.rust.demangle import RustDemangler
from rustdiff.rust.monomorphize import MonomorphizationGrouper

logger = logging.getLogger(__name__)


class GroundtruthGenerator:
    """Generate function-level matching groundtruth.

    Uses demangled symbol names to establish which functions in binary A
    correspond to which functions in binary B. Both binaries must have
    debug symbols (compiled with debug=true).
    """

    def __init__(self, loader1: RustBinaryLoader, loader2: RustBinaryLoader):
        self.loader1 = loader1
        self.loader2 = loader2
        self.demangler = RustDemangler()
        self.grouper = MonomorphizationGrouper()

    def generate(self) -> dict[str, dict]:
        """Generate groundtruth mapping.

        Returns dict mapping normalized_name -> {
            'addrs1': [addresses in binary 1],
            'addrs2': [addresses in binary 2],
        }

        A function is "matched" if it appears in both binaries with
        the same normalized (type-erased) name.
        """
        # Build name -> [addr] maps for both binaries
        name_to_addrs1 = self._build_name_map(self.loader1)
        name_to_addrs2 = self._build_name_map(self.loader2)

        # Find matches by normalized name
        all_names = set(name_to_addrs1.keys()) | set(name_to_addrs2.keys())
        groundtruth = {}
        for name in all_names:
            groundtruth[name] = {
                'addrs1': name_to_addrs1.get(name, []),
                'addrs2': name_to_addrs2.get(name, []),
            }

        matched = sum(
            1 for gt in groundtruth.values()
            if gt['addrs1'] and gt['addrs2']
        )
        only_in_1 = sum(
            1 for gt in groundtruth.values()
            if gt['addrs1'] and not gt['addrs2']
        )
        only_in_2 = sum(
            1 for gt in groundtruth.values()
            if not gt['addrs1'] and gt['addrs2']
        )
        logger.info(
            'Groundtruth: %d matched, %d only in bin1, %d only in bin2',
            matched, only_in_1, only_in_2,
        )
        return groundtruth

    def generate_addr_pairs(self) -> list[tuple[int, int]]:
        """Generate list of (addr1, addr2) matched pairs.

        For functions with a single address in each binary (the common case),
        produces a direct addr-to-addr mapping.
        """
        gt = self.generate()
        pairs = []
        for name, entry in gt.items():
            if len(entry['addrs1']) == 1 and len(entry['addrs2']) == 1:
                pairs.append((entry['addrs1'][0], entry['addrs2'][0]))
        return pairs

    def get_counts(self) -> dict:
        """Return summary counts."""
        gt = self.generate()
        matched = sum(
            1 for v in gt.values()
            if v['addrs1'] and v['addrs2']
        )
        only1 = sum(
            1 for v in gt.values()
            if v['addrs1'] and not v['addrs2']
        )
        only2 = sum(
            1 for v in gt.values()
            if not v['addrs1'] and v['addrs2']
        )
        return {'matched': matched, 'only_in_bin1': only1, 'only_in_bin2': only2}

    def _build_name_map(
        self, loader: RustBinaryLoader
    ) -> dict[str, list[int]]:
        """Build normalized_name -> [addresses] for a binary."""
        name_map = defaultdict(list)
        for addr, demangled in loader.get_all_functions():
            normalized = self.demangler.normalize_for_matching(demangled)
            name_map[normalized].append(addr)
        return dict(name_map)
