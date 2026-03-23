"""Cross-binary function matching using Hungarian algorithm."""

import logging

import networkx as nx
import numpy as np
from scipy.optimize import linear_sum_assignment

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.fingerprint.feature_weights import FeatureWeightCalculator
from rustdiff.micro_exec.block_executor import BlockMicroExecutor

logger = logging.getLogger(__name__)


def jaccard_similarity(set1: frozenset, set2: frozenset) -> float:
    """Compute Jaccard similarity between two feature sets."""
    if not set1 and not set2:
        return 1.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    if union == 0:
        return 0.0
    return intersection / union


def weighted_jaccard_similarity(
    weighted1: dict, weighted2: dict
) -> float:
    """Compute weighted Jaccard similarity.

    weighted1, weighted2: feature -> weight dicts.
    """
    all_features = set(weighted1.keys()) | set(weighted2.keys())
    if not all_features:
        return 0.0
    intersection = 0.0
    union = 0.0
    for feat in all_features:
        w1 = weighted1.get(feat, 0.0)
        w2 = weighted2.get(feat, 0.0)
        intersection += min(w1, w2)
        union += max(w1, w2)
    if union == 0.0:
        return 0.0
    return intersection / union


def cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Compute cosine similarity between two vectors."""
    dot = np.dot(v1, v2)
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    if n1 == 0 or n2 == 0:
        return 0.0
    return float(dot / (n1 * n2))


class FunctionMatcher:
    """Match functions between two Rust binaries.

    Computes fingerprints for both binaries, builds a similarity matrix,
    and solves the assignment problem using the Hungarian algorithm.
    """

    def __init__(self, loader1, loader2):
        self.loader1 = loader1
        self.loader2 = loader2

    def compute_fingerprints(
        self, loader
    ) -> dict[int, FunctionFingerprint]:
        """Compute fingerprints for all analyzable functions in a binary."""
        executor = BlockMicroExecutor(loader)
        funcs = loader.get_analyzable_functions()
        fingerprints = {}

        for addr, name in funcs:
            block_sigs = executor.execute_function(addr)
            if not block_sigs:
                continue
            cfg = loader.get_cfg_for_function(addr)
            fp = FunctionFingerprint(addr, name, block_sigs, cfg)
            fingerprints[addr] = fp

        logger.info(
            'Computed %d fingerprints for %s',
            len(fingerprints), loader.bin_path,
        )
        return fingerprints

    def compute_similarity_matrix(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        method: str = 'jaccard',
    ) -> tuple[np.ndarray, list[int], list[int]]:
        """Compute pairwise similarity between all function pairs.

        Returns (sim_matrix, addrs1, addrs2).
        """
        addrs1 = sorted(fps1.keys())
        addrs2 = sorted(fps2.keys())
        n1, n2 = len(addrs1), len(addrs2)
        sim_matrix = np.zeros((n1, n2))

        if method == 'jaccard':
            feat_sets1 = {a: fps1[a].to_feature_set() for a in addrs1}
            feat_sets2 = {a: fps2[a].to_feature_set() for a in addrs2}
            for i, a1 in enumerate(addrs1):
                for j, a2 in enumerate(addrs2):
                    sim_matrix[i, j] = jaccard_similarity(
                        feat_sets1[a1], feat_sets2[a2]
                    )

        elif method == 'weighted_jaccard':
            # Build corpus-level weights from both binaries
            weight_calc = FeatureWeightCalculator()
            weight_calc.update_from_batch(fps1)
            weight_calc.update_from_batch(fps2)
            weights = weight_calc.compute_weights()

            for i, a1 in enumerate(addrs1):
                wf1 = {f: weights.get(f, 1.0)
                        for f in fps1[a1].to_feature_set()}
                for j, a2 in enumerate(addrs2):
                    wf2 = {f: weights.get(f, 1.0)
                            for f in fps2[a2].to_feature_set()}
                    sim_matrix[i, j] = weighted_jaccard_similarity(wf1, wf2)

        elif method == 'cosine':
            vecs1 = {a: fps1[a].to_dense_vector() for a in addrs1}
            vecs2 = {a: fps2[a].to_dense_vector() for a in addrs2}
            for i, a1 in enumerate(addrs1):
                for j, a2 in enumerate(addrs2):
                    sim_matrix[i, j] = cosine_similarity(
                        vecs1[a1], vecs2[a2]
                    )

        else:
            raise ValueError(f'Unknown similarity method: {method}')

        return sim_matrix, addrs1, addrs2

    def match_functions(
        self,
        sim_matrix: np.ndarray,
        addrs1: list[int],
        addrs2: list[int],
        method: str = 'hungarian',
    ) -> list[tuple[int, int, float]]:
        """Produce 1-to-1 function matching.

        Returns list of (addr1, addr2, similarity_score).
        """
        if method == 'hungarian':
            return self._hungarian_match(sim_matrix, addrs1, addrs2)
        elif method == 'greedy':
            return self._greedy_match(sim_matrix, addrs1, addrs2)
        else:
            raise ValueError(f'Unknown matching method: {method}')

    def _hungarian_match(
        self, sim_matrix: np.ndarray, addrs1: list[int], addrs2: list[int]
    ) -> list[tuple[int, int, float]]:
        """Solve optimal 1-to-1 matching via Hungarian algorithm."""
        # scipy's linear_sum_assignment minimizes cost; negate similarity
        cost_matrix = -sim_matrix

        # Handle rectangular matrices
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        matches = []
        for r, c in zip(row_ind, col_ind):
            matches.append((addrs1[r], addrs2[c], sim_matrix[r, c]))

        return sorted(matches, key=lambda x: -x[2])

    def _greedy_match(
        self, sim_matrix: np.ndarray, addrs1: list[int], addrs2: list[int]
    ) -> list[tuple[int, int, float]]:
        """Greedily assign highest-similarity pairs first."""
        n1, n2 = sim_matrix.shape
        # Build (sim, i, j) list sorted by descending similarity
        pairs = []
        for i in range(n1):
            for j in range(n2):
                pairs.append((sim_matrix[i, j], i, j))
        pairs.sort(reverse=True)

        used_rows = set()
        used_cols = set()
        matches = []
        for sim, i, j in pairs:
            if i in used_rows or j in used_cols:
                continue
            used_rows.add(i)
            used_cols.add(j)
            matches.append((addrs1[i], addrs2[j], sim))

        return sorted(matches, key=lambda x: -x[2])

    def flag_suspicious(
        self,
        matches: list[tuple[int, int, float]],
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        threshold: float = 0.3,
    ) -> dict:
        """Flag functions for supply chain attack detection.

        Returns dict with keys: 'matched', 'modified', 'new', 'removed'.
        """
        matched_addrs1 = {m[0] for m in matches}
        matched_addrs2 = {m[1] for m in matches}

        result = {
            'matched': [],
            'modified': [],
            'new': [],
            'removed': [],
        }

        for addr1, addr2, sim in matches:
            entry = {
                'addr1': addr1,
                'addr2': addr2,
                'name1': fps1[addr1].func_name,
                'name2': fps2[addr2].func_name,
                'similarity': sim,
            }
            if sim >= threshold:
                result['matched'].append(entry)
            else:
                result['modified'].append(entry)

        # Functions only in binary 2 (new)
        for addr in fps2:
            if addr not in matched_addrs2:
                result['new'].append({
                    'addr': addr,
                    'name': fps2[addr].func_name,
                })

        # Functions only in binary 1 (removed)
        for addr in fps1:
            if addr not in matched_addrs1:
                result['removed'].append({
                    'addr': addr,
                    'name': fps1[addr].func_name,
                })

        return result
