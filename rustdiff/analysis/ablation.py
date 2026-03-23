"""Feature contribution and ablation analysis."""

import logging
from enum import Flag, auto
from copy import deepcopy

import numpy as np
import pandas as pd

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.matching.function_matcher import (
    FunctionMatcher,
    jaccard_similarity,
)
from eval.metrics import MatchingMetrics

logger = logging.getLogger(__name__)


class FeatureFlag(Flag):
    """Feature groups that can be toggled for ablation."""
    CONSTANTS = auto()
    CONCRETE_VALUES = auto()
    OPCODE_HISTOGRAM = auto()
    MEMORY_PATTERN = auto()
    DATAFLOW_EDGES = auto()
    CFG_WEIGHTS = auto()
    CALLEE_NAMES = auto()
    CFG_SHAPE = auto()
    STRING_REFS = auto()


ALL_FEATURES = (
    FeatureFlag.CONSTANTS |
    FeatureFlag.CONCRETE_VALUES |
    FeatureFlag.OPCODE_HISTOGRAM |
    FeatureFlag.MEMORY_PATTERN |
    FeatureFlag.DATAFLOW_EDGES |
    FeatureFlag.CFG_WEIGHTS |
    FeatureFlag.CALLEE_NAMES |
    FeatureFlag.CFG_SHAPE |
    FeatureFlag.STRING_REFS
)


def filter_features(
    feature_set: frozenset, enabled: FeatureFlag
) -> frozenset:
    """Filter a feature set based on enabled flags."""
    filtered = set()
    for feat in feature_set:
        if not isinstance(feat, tuple) or len(feat) < 1:
            continue
        tag = feat[0]
        # Map feature tags to flags
        if tag == 'const' and FeatureFlag.CONSTANTS in enabled:
            filtered.add(feat)
        elif tag == 'val' and FeatureFlag.CONCRETE_VALUES in enabled:
            filtered.add(feat)
        elif tag in ('op', 'op2') and FeatureFlag.OPCODE_HISTOGRAM in enabled:
            filtered.add(feat)
        elif tag == 'mem' and FeatureFlag.MEMORY_PATTERN in enabled:
            filtered.add(feat)
        elif tag == 'df' and FeatureFlag.DATAFLOW_EDGES in enabled:
            filtered.add(feat)
        elif tag in ('num_blocks', 'num_insns_bucket',
                      'stack_depth_bucket') and FeatureFlag.CFG_WEIGHTS in enabled:
            filtered.add(feat)
        elif tag == 'call' and FeatureFlag.CALLEE_NAMES in enabled:
            filtered.add(feat)
        elif tag == 'shape' and FeatureFlag.CFG_SHAPE in enabled:
            filtered.add(feat)
        elif tag == 'str' and FeatureFlag.STRING_REFS in enabled:
            filtered.add(feat)
    return frozenset(filtered)


class AblationStudy:
    """Run ablation experiments removing one feature group at a time."""

    def run_ablation(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        gt_pairs: list[tuple[int, int]],
    ) -> pd.DataFrame:
        """Run matching with all features, then with each removed.

        Returns DataFrame with columns:
        [experiment, removed_feature, mrr, recall_at_1, recall_at_5, top_1, top_5]
        """
        results = []

        # Baseline: all features
        result = self._evaluate_with_flags(
            fps1, fps2, gt_pairs, ALL_FEATURES, 'all_features',
        )
        results.append(result)

        # Remove one feature group at a time
        for flag in FeatureFlag:
            reduced = ALL_FEATURES & ~flag
            name = f'no_{flag.name.lower()}'
            result = self._evaluate_with_flags(
                fps1, fps2, gt_pairs, reduced, name,
            )
            results.append(result)

        # Single feature experiments
        for flag in FeatureFlag:
            name = f'only_{flag.name.lower()}'
            result = self._evaluate_with_flags(
                fps1, fps2, gt_pairs, flag, name,
            )
            results.append(result)

        return pd.DataFrame(results)

    def _evaluate_with_flags(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        gt_pairs: list[tuple[int, int]],
        flags: FeatureFlag,
        experiment_name: str,
    ) -> dict:
        """Evaluate matching accuracy with a specific feature subset."""
        addrs1 = sorted(fps1.keys())
        addrs2 = sorted(fps2.keys())

        # Build filtered feature sets
        feat_sets1 = {
            a: filter_features(fps1[a].to_feature_set(), flags)
            for a in addrs1
        }
        feat_sets2 = {
            a: filter_features(fps2[a].to_feature_set(), flags)
            for a in addrs2
        }

        # Compute similarity matrix
        n1, n2 = len(addrs1), len(addrs2)
        sim_matrix = np.zeros((n1, n2))
        for i, a1 in enumerate(addrs1):
            for j, a2 in enumerate(addrs2):
                sim_matrix[i, j] = jaccard_similarity(
                    feat_sets1[a1], feat_sets2[a2],
                )

        # Compute metrics
        top_k = MatchingMetrics.top_k_accuracy(
            [], sim_matrix, addrs1, addrs2, gt_pairs,
            k_list=[1, 5, 10],
        )
        mrr = MatchingMetrics.mrr(sim_matrix, addrs1, addrs2, gt_pairs)
        r1 = MatchingMetrics.recall_at_k(sim_matrix, addrs1, addrs2, gt_pairs, 1)
        r5 = MatchingMetrics.recall_at_k(sim_matrix, addrs1, addrs2, gt_pairs, 5)

        result = {
            'experiment': experiment_name,
            'enabled_flags': str(flags),
            'mrr': mrr,
            'recall_at_1': r1,
            'recall_at_5': r5,
            'top_1': top_k.get(1, 0),
            'top_5': top_k.get(5, 0),
            'top_10': top_k.get(10, 0),
        }

        logger.info(
            'Ablation [%s]: MRR=%.3f R@1=%.3f R@5=%.3f',
            experiment_name, mrr, r1, r5,
        )
        return result
