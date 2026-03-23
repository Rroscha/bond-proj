"""TF-IDF-like corpus-level feature weighting."""

import math
from collections import defaultdict

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint


class FeatureWeightCalculator:
    """Compute corpus-level feature weights.

    Features that appear in many functions (e.g., common constants like 0xFF,
    ubiquitous opcode patterns like push/pop) get lower weight. Rare,
    discriminative features get higher weight.

    Uses the same weighting formula as vSim (pool.py line 68):
        weight = 1 / log(occurrence + 1)
    """

    def __init__(self):
        self._occurrence_map = defaultdict(int)
        self._num_functions = 0

    def update_from_fingerprint(self, fp: FunctionFingerprint):
        """Count feature occurrences from one function's fingerprint."""
        self._num_functions += 1
        for feat in fp.to_feature_set():
            self._occurrence_map[feat] += 1

    def update_from_batch(self, fingerprints: dict[int, FunctionFingerprint]):
        """Process a batch of fingerprints."""
        for fp in fingerprints.values():
            self.update_from_fingerprint(fp)

    def compute_weights(self) -> dict:
        """Return feature -> weight mapping."""
        return {
            feat: 1.0 / math.log(count + 1)
            for feat, count in self._occurrence_map.items()
        }

    @property
    def num_functions(self) -> int:
        return self._num_functions

    def weighted_feature_set(
        self, fp: FunctionFingerprint
    ) -> dict[object, float]:
        """Return feature -> weight dict for a single fingerprint."""
        weights = self.compute_weights()
        return {
            feat: weights.get(feat, 1.0)
            for feat in fp.to_feature_set()
        }
