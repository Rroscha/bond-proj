#!/usr/bin/env python3
"""CLI entry point for running function-level and block-level case analysis.

Usage:
    python scripts/run_case_analysis.py binary1 binary2 [options]

Runs feature impact analysis at both function and block levels, producing
tables for ablation, feature interaction, block type accuracy, and
failure taxonomy.
"""

import argparse
import json
import logging
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rustdiff  # noqa: E402
from rustdiff.loader import RustBinaryLoader  # noqa: E402
from rustdiff.matching.function_matcher import FunctionMatcher  # noqa: E402
from rustdiff.analysis.case_analysis import FunctionFeatureAnalyzer  # noqa: E402
from rustdiff.analysis.block_case_analysis import BlockFeatureAnalyzer  # noqa: E402
from rustdiff.analysis.block_alignment import BlockAlignmentAnalyzer  # noqa: E402
from eval.groundtruth import GroundtruthGenerator  # noqa: E402


def main():
    parser = argparse.ArgumentParser(
        description='RustDiff case analysis: feature impact study',
    )
    parser.add_argument('binary1', help='Path to first binary')
    parser.add_argument('binary2', help='Path to second binary')
    parser.add_argument(
        '--output-dir', '-o', default=None,
        help='Output directory for results (default: data/results/case_analysis)',
    )
    parser.add_argument(
        '--include-stdlib', action='store_true',
        help='Include standard library functions',
    )
    parser.add_argument(
        '--skip-block-analysis', action='store_true',
        help='Skip block-level analysis (faster)',
    )
    parser.add_argument(
        '--top-n-functions', type=int, default=0,
        help='Limit block analysis to top N matched functions (0=all)',
    )
    parser.add_argument(
        '--verbose', '-v', action='store_true',
        help='Enable verbose logging',
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
    )

    output_dir = args.output_dir or os.path.join(
        'data', 'results', 'case_analysis'
    )
    os.makedirs(output_dir, exist_ok=True)

    # Load binaries
    print(f'Loading binary 1: {args.binary1}')
    loader1 = RustBinaryLoader(
        args.binary1, load_debug_info=True,
        include_stdlib=args.include_stdlib,
    )
    print(f'Loading binary 2: {args.binary2}')
    loader2 = RustBinaryLoader(
        args.binary2, load_debug_info=True,
        include_stdlib=args.include_stdlib,
    )

    # Compute fingerprints
    print('Computing fingerprints...')
    matcher = FunctionMatcher(loader1, loader2)
    fps1 = matcher.compute_fingerprints(loader1)
    fps2 = matcher.compute_fingerprints(loader2)
    print(f'  Binary 1: {len(fps1)} functions')
    print(f'  Binary 2: {len(fps2)} functions')

    # Compute matches
    print('Computing similarity matrix...')
    sim_matrix, addrs1, addrs2 = matcher.compute_similarity_matrix(
        fps1, fps2, method='jaccard',
    )
    matches = matcher.match_functions(
        sim_matrix, addrs1, addrs2, method='hungarian',
    )

    # Generate groundtruth
    print('Generating groundtruth...')
    gt_gen = GroundtruthGenerator(loader1, loader2)
    gt_pairs = gt_gen.generate()
    print(f'  Groundtruth pairs: {len(gt_pairs)}')

    # === Function-level analysis ===
    print('\n=== Function-Level Feature Impact Analysis ===')
    func_analyzer = FunctionFeatureAnalyzer()
    func_results = func_analyzer.run_full_analysis(
        fps1, fps2, gt_pairs, matches,
    )

    # Print contribution summary
    contributions = func_results['contributions']
    correct = [c for c in contributions if c.get('is_correct')]
    incorrect = [c for c in contributions if not c.get('is_correct')]
    print(f'  Correct matches: {len(correct)}')
    print(f'  Incorrect matches: {len(incorrect)}')

    # Print interaction matrix
    print('\nFeature Interaction Matrix (synergy values):')
    print(func_results['interaction_matrix'].to_string(float_format='%.3f'))

    # Save function results
    interaction_path = os.path.join(output_dir, 'feature_interaction_matrix.csv')
    func_results['interaction_matrix'].to_csv(interaction_path)
    print(f'\nSaved interaction matrix to: {interaction_path}')

    # Save mismatch diagnostics
    if func_results['mismatches']:
        print(f'\nMismatch diagnostics ({len(func_results["mismatches"])} cases):')
        for diag in func_results['mismatches'][:5]:
            print(f'  addr1=0x{diag["addr1"]:x}: most_divergent={diag["most_divergent"]}, '
                  f'overall_jaccard={diag["overall_jaccard"]:.3f}')

    mismatches_path = os.path.join(output_dir, 'mismatch_diagnostics.json')
    _save_json(func_results['mismatches'], mismatches_path)

    # === Block-level analysis ===
    if not args.skip_block_analysis:
        print('\n=== Block-Level Feature Impact Analysis ===')
        block_analyzer = BlockFeatureAnalyzer()

        # Select function pairs for block analysis
        func_pairs = matches
        if args.top_n_functions > 0:
            func_pairs = func_pairs[:args.top_n_functions]

        all_block_ablation = []
        all_block_type_acc = []
        all_failure_taxonomy = []

        for addr1, addr2, sim in func_pairs:
            if addr1 not in fps1 or addr2 not in fps2:
                continue

            fp1 = fps1[addr1]
            fp2 = fps2[addr2]
            if fp1.num_blocks == 0 or fp2.num_blocks == 0:
                continue

            block_results = block_analyzer.run_full_analysis(fp1, fp2)

            # Tag results with function info
            for df_list, df in [
                (all_block_ablation, block_results['ablation']),
                (all_block_type_acc, block_results['type_accuracy']),
                (all_failure_taxonomy, block_results['failure_taxonomy']),
            ]:
                if not df.empty:
                    df = df.copy()
                    df['func_addr1'] = addr1
                    df['func_addr2'] = addr2
                    df['func_name'] = fp1.func_name
                    df_list.append(df)

        # Aggregate block results
        if all_block_ablation:
            import pandas as pd
            abl_df = pd.concat(all_block_ablation, ignore_index=True)
            agg_ablation = abl_df.groupby('feature_removed').agg({
                'accuracy': 'mean',
                'mean_similarity': 'mean',
            }).reset_index()
            agg_ablation = agg_ablation.sort_values(
                'accuracy', ascending=False,
            )

            print('\nBlock Feature Ablation (aggregated):')
            print(agg_ablation.to_string(index=False, float_format='%.3f'))

            abl_path = os.path.join(output_dir, 'block_ablation.csv')
            agg_ablation.to_csv(abl_path, index=False)
            print(f'Saved to: {abl_path}')

        if all_block_type_acc:
            type_df = pd.concat(all_block_type_acc, ignore_index=True)
            agg_type = type_df.groupby('block_type').agg({
                'total': 'sum',
                'matched': 'sum',
                'mean_similarity': 'mean',
            }).reset_index()
            agg_type['accuracy'] = agg_type['matched'] / agg_type['total']
            agg_type = agg_type.sort_values('accuracy', ascending=False)

            print('\nBlock Type Accuracy:')
            print(agg_type.to_string(index=False, float_format='%.3f'))

            type_path = os.path.join(output_dir, 'block_type_accuracy.csv')
            agg_type.to_csv(type_path, index=False)
            print(f'Saved to: {type_path}')

        if all_failure_taxonomy:
            fail_df = pd.concat(all_failure_taxonomy, ignore_index=True)
            agg_fail = fail_df.groupby('category').agg({
                'count': 'sum',
            }).reset_index()
            agg_fail = agg_fail.sort_values('count', ascending=False)

            print('\nFailure Taxonomy:')
            print(agg_fail.to_string(index=False))

            fail_path = os.path.join(output_dir, 'failure_taxonomy.csv')
            agg_fail.to_csv(fail_path, index=False)
            print(f'Saved to: {fail_path}')

    print(f'\nAll results saved to: {output_dir}')


def _save_json(data, path):
    """Save data to JSON, converting non-serializable types."""
    def default(obj):
        if isinstance(obj, (set, frozenset)):
            return list(obj)
        if hasattr(obj, 'item'):  # numpy scalar
            return obj.item()
        return str(obj)

    with open(path, 'w') as f:
        json.dump(data, f, indent=2, default=default)


if __name__ == '__main__':
    main()
