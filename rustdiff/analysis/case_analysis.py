"""Function-level feature impact analysis for case studies.

Provides tools to understand which fingerprint features drive correct
matches and which cause mismatches, at the function granularity.
"""

import logging
from collections import defaultdict
from itertools import combinations

import numpy as np
import pandas as pd

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.analysis.ablation import (
    FeatureFlag,
    ALL_FEATURES,
    filter_features,
)
from rustdiff.matching.function_matcher import jaccard_similarity
from eval.metrics import MatchingMetrics

logger = logging.getLogger(__name__)

# Map feature tags to their FeatureFlag
_TAG_TO_FLAG = {
    'const': FeatureFlag.CONSTANTS,
    'val': FeatureFlag.CONCRETE_VALUES,
    'op': FeatureFlag.OPCODE_HISTOGRAM,
    'op2': FeatureFlag.OPCODE_HISTOGRAM,
    'mem': FeatureFlag.MEMORY_PATTERN,
    'df': FeatureFlag.DATAFLOW_EDGES,
    'num_blocks': FeatureFlag.CFG_WEIGHTS,
    'num_insns_bucket': FeatureFlag.CFG_WEIGHTS,
    'stack_depth_bucket': FeatureFlag.CFG_WEIGHTS,
    'call': FeatureFlag.CALLEE_NAMES,
    'shape': FeatureFlag.CFG_SHAPE,
    'str': FeatureFlag.STRING_REFS,
}


def _tag_of(feat: tuple) -> str:
    """Extract the tag string from a feature tuple."""
    if isinstance(feat, tuple) and len(feat) >= 1:
        return feat[0]
    return ''


def _flag_of(feat: tuple) -> FeatureFlag | None:
    """Map a feature tuple to its FeatureFlag."""
    tag = _tag_of(feat)
    return _TAG_TO_FLAG.get(tag)


class FunctionFeatureAnalyzer:
    """Analyze which features contribute to function matching accuracy."""

    def analyze_feature_contribution(
        self,
        match: tuple[int, int, float],
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
    ) -> dict[str, float]:
        """For a single matched pair, compute per-feature-group similarity.

        Returns dict mapping FeatureFlag name -> Jaccard similarity using
        only that feature group.
        """
        addr1, addr2, overall_sim = match
        fp1 = fps1.get(addr1)
        fp2 = fps2.get(addr2)
        if fp1 is None or fp2 is None:
            return {}

        full_set1 = fp1.to_feature_set()
        full_set2 = fp2.to_feature_set()

        contributions = {}
        for flag in FeatureFlag:
            filtered1 = filter_features(full_set1, flag)
            filtered2 = filter_features(full_set2, flag)
            sim = jaccard_similarity(filtered1, filtered2)
            contributions[flag.name] = sim

        contributions['ALL'] = overall_sim
        return contributions

    def diagnose_mismatch(
        self,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
        gt_pair: tuple[int, int],
    ) -> dict:
        """Diagnose why a groundtruth pair scored low similarity.

        Returns dict with:
        - per_feature_sim: per-group similarity scores
        - most_divergent: feature group with lowest similarity
        - shared_features: count of features in intersection
        - unique_to_1: count of features only in binary 1
        - unique_to_2: count of features only in binary 2
        - divergent_details: specific features that differ most
        """
        full_set1 = fp1.to_feature_set()
        full_set2 = fp2.to_feature_set()

        # Per-feature-group similarity
        per_feature_sim = {}
        for flag in FeatureFlag:
            f1 = filter_features(full_set1, flag)
            f2 = filter_features(full_set2, flag)
            per_feature_sim[flag.name] = jaccard_similarity(f1, f2)

        # Find most divergent group
        most_divergent = min(per_feature_sim, key=per_feature_sim.get)

        # Set analysis
        shared = full_set1 & full_set2
        only1 = full_set1 - full_set2
        only2 = full_set2 - full_set1

        # Group divergent features by tag
        divergent_by_group = defaultdict(int)
        for feat in only1 | only2:
            tag = _tag_of(feat)
            divergent_by_group[tag] += 1

        return {
            'per_feature_sim': per_feature_sim,
            'most_divergent': most_divergent,
            'shared_features': len(shared),
            'unique_to_1': len(only1),
            'unique_to_2': len(only2),
            'overall_jaccard': jaccard_similarity(full_set1, full_set2),
            'divergent_by_group': dict(divergent_by_group),
        }

    def feature_interaction_matrix(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        gt_pairs: list[tuple[int, int]],
    ) -> pd.DataFrame:
        """Compute feature interaction (synergy/redundancy) matrix.

        For each pair of feature groups A, B:
        - Compute accuracy with only A, only B, and A+B
        - Synergy = acc(A+B) - max(acc(A), acc(B))
        - Positive synergy means the combination is better than either alone
        - Negative means redundancy (combination doesn't help)

        Returns a DataFrame indexed by feature group names.
        """
        flags = list(FeatureFlag)
        n = len(flags)

        # Single-feature accuracies
        single_acc = {}
        for flag in flags:
            acc = self._compute_recall_at_1(fps1, fps2, gt_pairs, flag)
            single_acc[flag.name] = acc

        # Pairwise combination accuracies
        matrix = np.zeros((n, n))
        for i, f1 in enumerate(flags):
            matrix[i, i] = single_acc[f1.name]
            for j, f2 in enumerate(flags):
                if i >= j:
                    continue
                combined = f1 | f2
                combined_acc = self._compute_recall_at_1(
                    fps1, fps2, gt_pairs, combined,
                )
                synergy = combined_acc - max(
                    single_acc[f1.name], single_acc[f2.name]
                )
                matrix[i, j] = synergy
                matrix[j, i] = synergy

        names = [f.name for f in flags]
        return pd.DataFrame(matrix, index=names, columns=names)

    def run_full_analysis(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        gt_pairs: list[tuple[int, int]],
        matches: list[tuple[int, int, float]],
    ) -> dict:
        """Run the complete function-level feature analysis.

        Returns dict with:
        - contributions: per-match feature contributions (list of dicts)
        - mismatches: diagnosis for incorrect matches
        - interaction_matrix: DataFrame of pairwise feature synergy
        """
        gt_set = set(gt_pairs)

        # Analyze feature contributions for correct matches
        contributions = []
        mismatches = []
        for addr1, addr2, sim in matches:
            contrib = self.analyze_feature_contribution(
                (addr1, addr2, sim), fps1, fps2,
            )
            contrib['addr1'] = addr1
            contrib['addr2'] = addr2
            contrib['name1'] = fps1[addr1].func_name if addr1 in fps1 else ''
            contrib['name2'] = fps2[addr2].func_name if addr2 in fps2 else ''
            contrib['is_correct'] = (addr1, addr2) in gt_set
            contributions.append(contrib)

            # Diagnose incorrect matches
            if (addr1, addr2) not in gt_set:
                # Find the groundtruth partner for addr1 if it exists
                gt_addr2 = None
                for a1, a2 in gt_pairs:
                    if a1 == addr1:
                        gt_addr2 = a2
                        break
                if gt_addr2 and gt_addr2 in fps2 and addr1 in fps1:
                    diagnosis = self.diagnose_mismatch(
                        fps1[addr1], fps2[gt_addr2], (addr1, gt_addr2),
                    )
                    diagnosis['matched_addr2'] = addr2
                    diagnosis['gt_addr2'] = gt_addr2
                    diagnosis['addr1'] = addr1
                    mismatches.append(diagnosis)

        # Feature interaction matrix
        interaction = self.feature_interaction_matrix(fps1, fps2, gt_pairs)

        return {
            'contributions': contributions,
            'mismatches': mismatches,
            'interaction_matrix': interaction,
        }

    def _compute_recall_at_1(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        gt_pairs: list[tuple[int, int]],
        flags: FeatureFlag,
    ) -> float:
        """Compute Recall@1 with a specific feature subset."""
        addrs1 = sorted(fps1.keys())
        addrs2 = sorted(fps2.keys())

        feat_sets1 = {
            a: filter_features(fps1[a].to_feature_set(), flags)
            for a in addrs1
        }
        feat_sets2 = {
            a: filter_features(fps2[a].to_feature_set(), flags)
            for a in addrs2
        }

        n1, n2 = len(addrs1), len(addrs2)
        sim_matrix = np.zeros((n1, n2))
        for i, a1 in enumerate(addrs1):
            for j, a2 in enumerate(addrs2):
                sim_matrix[i, j] = jaccard_similarity(
                    feat_sets1[a1], feat_sets2[a2],
                )

        return MatchingMetrics.recall_at_k(
            sim_matrix, addrs1, addrs2, gt_pairs, k=1,
        )
