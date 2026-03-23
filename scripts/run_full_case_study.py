#!/usr/bin/env python3
"""Standalone case study runner with detailed qualitative output.

Runs the full RustDiff pipeline on two binaries and produces
human-readable qualitative analysis results.
"""

import argparse
import json
import logging
import os
import sys
import traceback

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rustdiff  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
)
logger = logging.getLogger('case_study')


def main():
    parser = argparse.ArgumentParser(description='RustDiff case study')
    parser.add_argument('binary1', help='Path to O0 binary')
    parser.add_argument('binary2', help='Path to O2 binary')
    parser.add_argument('--output-dir', '-o', default='data/results/case_analysis')
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    os.makedirs(args.output_dir, exist_ok=True)

    # === Phase 1: Load binaries ===
    print('=' * 70)
    print('PHASE 1: Loading Binaries')
    print('=' * 70)

    from rustdiff.loader import RustBinaryLoader

    try:
        loader1 = RustBinaryLoader(args.binary1, load_debug_info=True)
    except Exception as e:
        logger.warning('Debug info load failed for binary1: %s; retrying without', e)
        loader1 = RustBinaryLoader(args.binary1, load_debug_info=False)
    try:
        loader2 = RustBinaryLoader(args.binary2, load_debug_info=True)
    except Exception as e:
        logger.warning('Debug info load failed for binary2: %s; retrying without', e)
        loader2 = RustBinaryLoader(args.binary2, load_debug_info=False)

    funcs1 = loader1.get_analyzable_functions()
    funcs2 = loader2.get_analyzable_functions()
    all_funcs1 = loader1.get_all_functions()
    all_funcs2 = loader2.get_all_functions()

    print(f'\nBinary 1 ({os.path.basename(args.binary1)}):')
    print(f'  Total functions: {len(all_funcs1)}')
    print(f'  Analyzable (user code): {len(funcs1)}')
    print(f'  Sample functions:')
    for addr, name in funcs1[:10]:
        print(f'    0x{addr:x}  {name}')

    print(f'\nBinary 2 ({os.path.basename(args.binary2)}):')
    print(f'  Total functions: {len(all_funcs2)}')
    print(f'  Analyzable (user code): {len(funcs2)}')
    print(f'  Sample functions:')
    for addr, name in funcs2[:10]:
        print(f'    0x{addr:x}  {name}')

    # === Phase 2: Extract features (callees, strings) ===
    print('\n' + '=' * 70)
    print('PHASE 2: Extracting Rust-Specific Features')
    print('=' * 70)

    # Sample callee extraction
    for addr, name in funcs1[:5]:
        callees = loader1.get_callees_for_function(addr)
        strings = loader1.get_string_refs_for_function(addr)
        if callees or strings:
            print(f'\n  {name} (0x{addr:x}):')
            if callees:
                print(f'    Callees: {callees[:5]}')
            if strings:
                print(f'    Strings: {strings[:5]}')

    # === Phase 3: Compute fingerprints ===
    print('\n' + '=' * 70)
    print('PHASE 3: Computing Function Fingerprints')
    print('=' * 70)

    from rustdiff.matching.function_matcher import FunctionMatcher

    matcher = FunctionMatcher(loader1, loader2)

    print('  Computing fingerprints for binary 1...')
    fps1 = matcher.compute_fingerprints(loader1)
    print(f'  -> {len(fps1)} fingerprints')

    print('  Computing fingerprints for binary 2...')
    fps2 = matcher.compute_fingerprints(loader2)
    print(f'  -> {len(fps2)} fingerprints')

    # Print fingerprint details for a sample
    print('\n  Sample fingerprint details:')
    for addr, fp in list(fps1.items())[:3]:
        shape = fp.get_cfg_shape_features()
        callees = fp.get_callee_names()
        strings = fp.get_string_refs()
        print(f'\n    {fp.func_name}:')
        print(f'      Blocks: {fp.num_blocks}, Instructions: {fp.num_instructions}')
        print(f'      CFG shape: edges={shape["edge_count"]}, loops={shape["loop_count"]}, '
              f'depth={shape["max_depth"]}, cyclomatic={shape["cyclomatic_complexity"]}')
        print(f'      Constants: {len(fp.get_constant_multiset())}')
        print(f'      Callees: {callees[:5]}')
        print(f'      String refs: {strings[:5]}')
        print(f'      Feature set size: {len(fp.to_feature_set())}')

    # === Phase 4: Function matching ===
    print('\n' + '=' * 70)
    print('PHASE 4: Cross-Binary Function Matching')
    print('=' * 70)

    sim_matrix, addrs1, addrs2 = matcher.compute_similarity_matrix(
        fps1, fps2, method='jaccard',
    )
    matches = matcher.match_functions(sim_matrix, addrs1, addrs2, method='hungarian')
    flagged = matcher.flag_suspicious(matches, fps1, fps2, threshold=0.3)

    print(f'\n  Matched (sim >= 0.3): {len(flagged["matched"])}')
    print(f'  Modified (sim < 0.3): {len(flagged["modified"])}')
    print(f'  New (only in binary 2): {len(flagged["new"])}')
    print(f'  Removed (only in binary 1): {len(flagged["removed"])}')

    print('\n  Top matches by similarity:')
    for m in matches[:10]:
        a1, a2, sim = m
        n1 = fps1[a1].func_name if a1 in fps1 else '?'
        n2 = fps2[a2].func_name if a2 in fps2 else '?'
        print(f'    {sim:.3f}  {n1}  <->  {n2}')

    if flagged['modified']:
        print('\n  Modified functions (potential tampering):')
        for entry in flagged['modified'][:5]:
            print(f'    {entry["similarity"]:.3f}  {entry["name1"]}  <->  {entry["name2"]}')

    # === Phase 5: Groundtruth generation ===
    print('\n' + '=' * 70)
    print('PHASE 5: Groundtruth Generation')
    print('=' * 70)

    from eval.groundtruth import GroundtruthGenerator

    gt_gen = GroundtruthGenerator(loader1, loader2)
    gt_dict = gt_gen.generate()
    gt_pairs = gt_gen.generate_addr_pairs()
    print(f'  Groundtruth entries: {len(gt_dict)}')
    print(f'  Groundtruth addr pairs (1-to-1): {len(gt_pairs)}')

    # Evaluate matching accuracy
    from eval.metrics import MatchingMetrics
    import numpy as np

    if gt_pairs:
        top_k = MatchingMetrics.top_k_accuracy(
            matches, sim_matrix, addrs1, addrs2, gt_pairs, k_list=[1, 3, 5, 10],
        )
        mrr = MatchingMetrics.mrr(sim_matrix, addrs1, addrs2, gt_pairs)
        r1 = MatchingMetrics.recall_at_k(sim_matrix, addrs1, addrs2, gt_pairs, 1)
        precision = MatchingMetrics.matching_precision(matches, gt_pairs)

        print(f'\n  Baseline Matching Accuracy:')
        print(f'    MRR:        {mrr:.3f}')
        print(f'    Recall@1:   {r1:.3f}')
        print(f'    Precision:  {precision:.3f}')
        for k, acc in sorted(top_k.items()):
            print(f'    Top-{k}:     {acc:.3f}')

    # === Phase 6: Function-level ablation ===
    print('\n' + '=' * 70)
    print('PHASE 6: Feature Ablation Study')
    print('=' * 70)

    if gt_pairs:
        from rustdiff.analysis.ablation import AblationStudy

        ablation = AblationStudy()
        abl_df = ablation.run_ablation(fps1, fps2, gt_pairs)

        print('\n  Ablation Results (leave-one-out and single-feature):')
        print(abl_df.to_string(index=False, float_format=lambda x: f'{x:.3f}'))

        abl_path = os.path.join(args.output_dir, 'ablation_results.csv')
        abl_df.to_csv(abl_path, index=False)
        print(f'\n  Saved to: {abl_path}')
    else:
        print('  Skipping (no groundtruth pairs)')

    # === Phase 7: Function-level case analysis ===
    print('\n' + '=' * 70)
    print('PHASE 7: Function-Level Feature Impact Analysis')
    print('=' * 70)

    if gt_pairs:
        from rustdiff.analysis.case_analysis import FunctionFeatureAnalyzer

        func_analyzer = FunctionFeatureAnalyzer()
        func_results = func_analyzer.run_full_analysis(fps1, fps2, gt_pairs, matches)

        # Contribution summary
        contributions = func_results['contributions']
        correct = [c for c in contributions if c.get('is_correct')]
        incorrect = [c for c in contributions if not c.get('is_correct')]
        print(f'\n  Correct matches: {len(correct)}/{len(contributions)}')
        print(f'  Incorrect matches: {len(incorrect)}/{len(contributions)}')

        # Average per-feature contribution for correct matches
        if correct:
            from rustdiff.analysis.ablation import FeatureFlag
            print('\n  Average per-feature similarity (correct matches):')
            for flag in FeatureFlag:
                vals = [c[flag.name] for c in correct if flag.name in c]
                if vals:
                    avg = sum(vals) / len(vals)
                    print(f'    {flag.name:25s}: {avg:.3f}')

        # Feature interaction matrix
        interaction = func_results['interaction_matrix']
        print('\n  Feature Interaction Matrix (synergy values):')
        print(interaction.to_string(float_format=lambda x: f'{x:+.3f}'))

        int_path = os.path.join(args.output_dir, 'interaction_matrix.csv')
        interaction.to_csv(int_path)
        print(f'\n  Saved to: {int_path}')

        # Mismatch diagnostics
        if func_results['mismatches']:
            print(f'\n  Mismatch Diagnostics ({len(func_results["mismatches"])} cases):')
            for diag in func_results['mismatches'][:5]:
                print(f'\n    Function 0x{diag["addr1"]:x}:')
                print(f'      Most divergent feature: {diag["most_divergent"]}')
                print(f'      Overall Jaccard: {diag["overall_jaccard"]:.3f}')
                print(f'      Shared features: {diag["shared_features"]}')
                print(f'      Unique to bin1: {diag["unique_to_1"]}')
                print(f'      Unique to bin2: {diag["unique_to_2"]}')
                print(f'      Divergent by group: {diag["divergent_by_group"]}')
    else:
        print('  Skipping (no groundtruth pairs)')

    # === Phase 8: Block-level case analysis ===
    print('\n' + '=' * 70)
    print('PHASE 8: Block-Level Feature Impact Analysis')
    print('=' * 70)

    from rustdiff.analysis.block_case_analysis import BlockFeatureAnalyzer, classify_block, BlockType
    from rustdiff.analysis.block_alignment import BlockAlignmentAnalyzer

    block_analyzer = BlockFeatureAnalyzer()
    aligner = BlockAlignmentAnalyzer()

    # Run on top matched function pairs
    import pandas as pd
    all_type_acc = []
    all_failures = []
    all_ablation = []
    all_patterns = []

    n_analyzed = 0
    for a1, a2, sim in matches[:20]:
        if a1 not in fps1 or a2 not in fps2:
            continue
        fp1 = fps1[a1]
        fp2 = fps2[a2]
        if fp1.num_blocks == 0 or fp2.num_blocks == 0:
            continue

        n_analyzed += 1
        results = block_analyzer.run_full_analysis(fp1, fp2)

        if not results['type_accuracy'].empty:
            df = results['type_accuracy'].copy()
            df['func_name'] = fp1.func_name
            df['func_sim'] = sim
            all_type_acc.append(df)

        if not results['failure_taxonomy'].empty:
            df = results['failure_taxonomy'].copy()
            df['func_name'] = fp1.func_name
            all_failures.append(df)

        if not results['ablation'].empty:
            df = results['ablation'].copy()
            df['func_name'] = fp1.func_name
            all_ablation.append(df)

        # Rust pattern detection
        alignment = results['alignment']
        patterns = aligner.identify_rust_patterns(alignment, fp1, fp2)
        patterns['func_name'] = fp1.func_name
        patterns['func_sim'] = sim
        all_patterns.append(patterns)

    print(f'\n  Analyzed {n_analyzed} function pairs at block level')

    # Block type accuracy
    if all_type_acc:
        type_df = pd.concat(all_type_acc, ignore_index=True)
        agg = type_df.groupby('block_type').agg({
            'total': 'sum', 'matched': 'sum', 'mean_similarity': 'mean',
        }).reset_index()
        agg['accuracy'] = agg['matched'] / agg['total'].clip(lower=1)
        agg = agg.sort_values('accuracy', ascending=False)

        print('\n  Block Type Matching Accuracy:')
        print(agg.to_string(index=False, float_format=lambda x: f'{x:.3f}'))

        type_path = os.path.join(args.output_dir, 'block_type_accuracy.csv')
        agg.to_csv(type_path, index=False)

    # Failure taxonomy
    if all_failures:
        fail_df = pd.concat(all_failures, ignore_index=True)
        agg_fail = fail_df.groupby('category').agg({'count': 'sum'}).reset_index()
        agg_fail = agg_fail.sort_values('count', ascending=False)

        print('\n  Block Failure Taxonomy:')
        print(agg_fail.to_string(index=False))

        fail_path = os.path.join(args.output_dir, 'failure_taxonomy.csv')
        agg_fail.to_csv(fail_path, index=False)

    # Block ablation
    if all_ablation:
        abl_df = pd.concat(all_ablation, ignore_index=True)
        agg_abl = abl_df.groupby('feature_removed').agg({
            'accuracy': 'mean', 'mean_similarity': 'mean',
        }).reset_index()
        agg_abl = agg_abl.sort_values('accuracy', ascending=False)

        print('\n  Block Feature Ablation (mean accuracy by removed feature):')
        print(agg_abl.to_string(index=False, float_format=lambda x: f'{x:.3f}'))

        babl_path = os.path.join(args.output_dir, 'block_ablation.csv')
        agg_abl.to_csv(babl_path, index=False)

    # Rust pattern summary
    if all_patterns:
        print('\n  Rust-Specific Pattern Detection:')
        n = len(all_patterns)
        for key in ['bounds_check_diff', 'unrolling_diff', 'drop_glue_diff',
                     'panic_path_diff', 'iterator_diff']:
            count = sum(1 for p in all_patterns if p.get(key))
            print(f'    {key:25s}: {count}/{n} functions')

        # Block count ratios
        ratios = [p['block_count_ratio'] for p in all_patterns if p['block_count_ratio'] > 0]
        if ratios:
            print(f'\n    Block count ratio (O0/O2): '
                  f'mean={sum(ratios)/len(ratios):.2f}, '
                  f'min={min(ratios):.2f}, max={max(ratios):.2f}')

    # === Summary ===
    print('\n' + '=' * 70)
    print('SUMMARY')
    print('=' * 70)
    print(f'  Binary 1: {args.binary1}')
    print(f'  Binary 2: {args.binary2}')
    print(f'  Functions analyzed: {len(fps1)} vs {len(fps2)}')
    print(f'  Groundtruth pairs: {len(gt_pairs) if gt_pairs else "N/A"}')
    if gt_pairs:
        print(f'  MRR: {mrr:.3f}')
        print(f'  Recall@1: {r1:.3f}')
    print(f'  Block-level analysis: {n_analyzed} function pairs')
    print(f'  Results saved to: {args.output_dir}')
    print('=' * 70)


if __name__ == '__main__':
    main()
