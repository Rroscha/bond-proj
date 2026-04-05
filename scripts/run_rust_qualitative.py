#!/usr/bin/env python3
"""Rust-specific qualitative analysis of basic block matching.

Assumes functions are already matched (via groundtruth from debug symbols),
then drills into block-level alignment to analyze feature stability and
Rust optimization effects.

Usage:
    python scripts/run_rust_qualitative.py --binary-o0 <path> --binary-o2 <path> \
        --project-name coreutils-sort [options]
"""

import argparse
import logging
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rustdiff  # noqa: E402
from rustdiff.loader import RustBinaryLoader  # noqa: E402
from rustdiff.micro_exec.block_executor import BlockMicroExecutor  # noqa: E402
from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint  # noqa: E402
from rustdiff.analysis.rust_qualitative import RustQualitativeAnalyzer  # noqa: E402
from eval.groundtruth import GroundtruthGenerator  # noqa: E402


def main():
    parser = argparse.ArgumentParser(
        description='Rust-specific qualitative block analysis',
    )
    parser.add_argument('--binary-o0', required=True, help='Path to O0 binary')
    parser.add_argument('--binary-o2', required=True, help='Path to O2 binary')
    parser.add_argument(
        '--project-name', default='unknown',
        help='Project label for the report',
    )
    parser.add_argument(
        '--output-dir', '-o', default=None,
        help='Output directory (default: data/results/qualitative/<project-name>)',
    )
    parser.add_argument(
        '--min-blocks', type=int, default=3,
        help='Minimum blocks per function to include (default: 3)',
    )
    parser.add_argument(
        '--max-functions', type=int, default=0,
        help='Limit analysis to N functions (0=all)',
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
    logger = logging.getLogger('qualitative')

    output_dir = args.output_dir or os.path.join(
        'data', 'results', 'qualitative', args.project_name,
    )
    os.makedirs(output_dir, exist_ok=True)

    t0 = time.time()

    # ---- Phase 1: Load binaries ----
    print('=' * 70)
    print('PHASE 1: Loading Binaries')
    print('=' * 70)

    try:
        loader1 = RustBinaryLoader(args.binary_o0, load_debug_info=True)
    except Exception:
        logger.warning('Debug info load failed for O0; retrying without')
        loader1 = RustBinaryLoader(args.binary_o0, load_debug_info=False)

    try:
        loader2 = RustBinaryLoader(args.binary_o2, load_debug_info=True)
    except Exception:
        logger.warning('Debug info load failed for O2; retrying without')
        loader2 = RustBinaryLoader(args.binary_o2, load_debug_info=False)

    funcs1 = loader1.get_analyzable_functions()
    funcs2 = loader2.get_analyzable_functions()
    print(f'  O0: {len(funcs1)} analyzable functions')
    print(f'  O2: {len(funcs2)} analyzable functions')

    t1 = time.time()
    print(f'  Load time: {t1 - t0:.1f}s')
    print()

    # ---- Phase 2: Generate groundtruth ----
    print('=' * 70)
    print('PHASE 2: Generating Groundtruth')
    print('=' * 70)

    gt_gen = GroundtruthGenerator(loader1, loader2)
    gt_pairs = gt_gen.generate_addr_pairs()
    gt_counts = gt_gen.get_counts()
    print(f'  Matched functions: {gt_counts["matched"]}')
    print(f'  Only in O0: {gt_counts["only_in_bin1"]}')
    print(f'  Only in O2: {gt_counts["only_in_bin2"]}')
    print(f'  1-to-1 address pairs: {len(gt_pairs)}')
    print()

    # Limit groundtruth pairs if max_functions is set
    if args.max_functions > 0 and len(gt_pairs) > args.max_functions:
        gt_pairs = gt_pairs[:args.max_functions]
        print(f'  (limited to {args.max_functions} pairs)')

    # ---- Phase 3: Compute fingerprints (only for GT pairs) ----
    print('=' * 70)
    print('PHASE 3: Computing Fingerprints (GT pairs only)')
    print('=' * 70)

    # Only fingerprint functions that appear in groundtruth pairs
    needed_o0 = {a1 for a1, a2 in gt_pairs}
    needed_o2 = {a2 for a1, a2 in gt_pairs}
    print(f'  Need {len(needed_o0)} O0 + {len(needed_o2)} O2 fingerprints')

    def compute_fingerprints_for(loader, addrs, label):
        executor = BlockMicroExecutor(loader)
        fps = {}
        done = 0
        for addr in addrs:
            try:
                name = loader.get_demangled_name(addr) or f'sub_{addr:x}'
                block_sigs = executor.execute_function(addr)
                if not block_sigs:
                    continue
                cfg = loader.get_cfg_for_function(addr)
                fp = FunctionFingerprint(addr, name, block_sigs, cfg)
                fps[addr] = fp
            except Exception as e:
                logger.debug('Fingerprint failed for 0x%x: %s', addr, e)
            done += 1
            if done % 50 == 0:
                print(f'  [{label}] {done}/{len(addrs)}...')
        return fps

    print('  Computing fingerprints for O0...')
    fps1 = compute_fingerprints_for(loader1, needed_o0, 'O0')
    print(f'  -> {len(fps1)} fingerprints')
    print('  Computing fingerprints for O2...')
    fps2 = compute_fingerprints_for(loader2, needed_o2, 'O2')
    print(f'  -> {len(fps2)} fingerprints')

    t2 = time.time()
    print(f'  Fingerprint time: {t2 - t1:.1f}s')
    print()

    # ---- Phase 4: Qualitative analysis ----
    print('=' * 70)
    print('PHASE 4: Qualitative Block Analysis')
    print('=' * 70)

    analyzer = RustQualitativeAnalyzer(min_blocks=args.min_blocks)
    report = analyzer.analyze_corpus(
        fps1, fps2, gt_pairs,
        project_name=args.project_name,
    )

    t3 = time.time()
    print(f'  Analyzed: {len(report.function_results)} function pairs')
    print(f'  Skipped: {report.skipped}')
    print(f'  Analysis time: {t3 - t2:.1f}s')
    print()

    # ---- Phase 5: Generate report ----
    print('=' * 70)
    print('PHASE 5: Generating Report')
    print('=' * 70)

    # Summary tables to stdout
    print()
    print('--- Feature Stability Summary ---')
    df1 = report.feature_stability_summary()
    if not df1.empty:
        print(df1.to_string(index=False, float_format='%.1f'))
    print()

    print('--- Optimization Effect Impact ---')
    df3 = report.optimization_effect_summary()
    if not df3.empty:
        print(df3.to_string(index=False, float_format='%.3f'))
    print()

    print('--- Feature Contribution by Tier ---')
    df4 = report.feature_contribution_by_tier()
    if not df4.empty:
        print(df4.to_string(index=False, float_format='%.3f'))
    print()

    # Write outputs
    report_path = os.path.join(output_dir, 'report.md')
    with open(report_path, 'w') as f:
        f.write(report.to_markdown())
    print(f'  Markdown report: {report_path}')

    report.to_csv_bundle(output_dir)
    print(f'  CSV files: {output_dir}/')

    t4 = time.time()
    print()
    print(f'Total time: {t4 - t0:.1f}s')
    print('Done.')


if __name__ == '__main__':
    main()
