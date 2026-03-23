"""Main experiment runner for RustDiff evaluation."""

import logging
import time
from pathlib import Path

import pandas as pd

from rustdiff.loader import RustBinaryLoader
from rustdiff.matching.function_matcher import FunctionMatcher
from rustdiff.matching.diff_report import DiffReport
from eval.groundtruth import GroundtruthGenerator
from eval.metrics import MatchingMetrics

logger = logging.getLogger(__name__)


class ExperimentRunner:
    """Orchestrate RustDiff experiments."""

    def __init__(self, results_dir: str = 'data/results'):
        self.results_dir = Path(results_dir)
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def run_pairwise(
        self,
        bin1_path: str,
        bin2_path: str,
        method: str = 'weighted_jaccard',
        match_method: str = 'hungarian',
        threshold: float = 0.3,
        include_stdlib: bool = False,
    ) -> dict:
        """Run a single pairwise comparison experiment.

        Returns dict with: fingerprints, matches, flagged, report, metrics.
        """
        t0 = time.time()

        # Load binaries
        loader1 = RustBinaryLoader(bin1_path, load_debug_info=True,
                                    include_stdlib=include_stdlib)
        loader2 = RustBinaryLoader(bin2_path, load_debug_info=True,
                                    include_stdlib=include_stdlib)
        t_load = time.time() - t0

        # Compute fingerprints
        matcher = FunctionMatcher(loader1, loader2)
        fps1 = matcher.compute_fingerprints(loader1)
        fps2 = matcher.compute_fingerprints(loader2)
        t_fp = time.time() - t0 - t_load

        # Compute similarity and match
        sim_matrix, addrs1, addrs2 = matcher.compute_similarity_matrix(
            fps1, fps2, method=method,
        )
        matches = matcher.match_functions(
            sim_matrix, addrs1, addrs2, method=match_method,
        )
        t_match = time.time() - t0 - t_load - t_fp

        # Flag suspicious functions
        flagged = matcher.flag_suspicious(matches, fps1, fps2,
                                          threshold=threshold)

        # Generate groundtruth and evaluate
        gt_gen = GroundtruthGenerator(loader1, loader2)
        gt_pairs = gt_gen.generate_addr_pairs()
        gt_counts = gt_gen.get_counts()

        metrics = {}
        if gt_pairs:
            metrics['top_k'] = MatchingMetrics.top_k_accuracy(
                matches, sim_matrix, addrs1, addrs2, gt_pairs,
            )
            metrics['mrr'] = MatchingMetrics.mrr(
                sim_matrix, addrs1, addrs2, gt_pairs,
            )
            metrics['recall@1'] = MatchingMetrics.recall_at_k(
                sim_matrix, addrs1, addrs2, gt_pairs, k=1,
            )
            metrics['recall@5'] = MatchingMetrics.recall_at_k(
                sim_matrix, addrs1, addrs2, gt_pairs, k=5,
            )
            metrics['precision'] = MatchingMetrics.matching_precision(
                matches, gt_pairs,
            )
        metrics['groundtruth'] = gt_counts

        t_total = time.time() - t0

        # Generate report
        report = DiffReport(flagged, fps1, fps2, bin1_path, bin2_path)

        result = {
            'bin1': bin1_path,
            'bin2': bin2_path,
            'method': method,
            'match_method': match_method,
            'num_funcs_bin1': len(fps1),
            'num_funcs_bin2': len(fps2),
            'num_matches': len(matches),
            'flagged': flagged,
            'metrics': metrics,
            'timing': {
                'load_s': t_load,
                'fingerprint_s': t_fp,
                'match_s': t_match,
                'total_s': t_total,
            },
            'report': report,
        }

        logger.info(
            'Experiment done: %s vs %s | '
            'funcs=%d/%d matches=%d MRR=%.3f Recall@1=%.3f | %.1fs',
            Path(bin1_path).name, Path(bin2_path).name,
            len(fps1), len(fps2), len(matches),
            metrics.get('mrr', 0), metrics.get('recall@1', 0),
            t_total,
        )

        return result

    def run_cross_optimization_suite(
        self,
        binary_paths: list[str],
        method: str = 'weighted_jaccard',
    ) -> pd.DataFrame:
        """Run pairwise experiments across all binary pairs.

        Returns a DataFrame with one row per pair.
        """
        rows = []
        for i, bin1 in enumerate(binary_paths):
            for bin2 in binary_paths[i + 1:]:
                result = self.run_pairwise(bin1, bin2, method=method)
                row = {
                    'bin1': Path(bin1).name,
                    'bin2': Path(bin2).name,
                    'num_funcs_bin1': result['num_funcs_bin1'],
                    'num_funcs_bin2': result['num_funcs_bin2'],
                    'num_matches': result['num_matches'],
                    'total_time_s': result['timing']['total_s'],
                }
                row.update({
                    f'top_{k}': v
                    for k, v in result['metrics'].get('top_k', {}).items()
                })
                row['mrr'] = result['metrics'].get('mrr', 0)
                row['recall_at_1'] = result['metrics'].get('recall@1', 0)
                row['recall_at_5'] = result['metrics'].get('recall@5', 0)
                row['precision'] = result['metrics'].get('precision', 0)
                rows.append(row)

        df = pd.DataFrame(rows)
        return df
