#!/usr/bin/env python3
"""CLI entry point for RustDiff binary diffing."""

import argparse
import logging
import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rustdiff  # noqa: E402
from rustdiff.loader import RustBinaryLoader  # noqa: E402
from rustdiff.matching.function_matcher import FunctionMatcher  # noqa: E402
from rustdiff.matching.diff_report import DiffReport  # noqa: E402


def main():
    parser = argparse.ArgumentParser(
        description='RustDiff: Rust binary function-level diffing',
    )
    parser.add_argument('binary1', help='Path to first binary')
    parser.add_argument('binary2', help='Path to second binary')
    parser.add_argument(
        '--method', default='weighted_jaccard',
        choices=['jaccard', 'weighted_jaccard', 'cosine'],
        help='Similarity method (default: weighted_jaccard)',
    )
    parser.add_argument(
        '--match-method', default='hungarian',
        choices=['hungarian', 'greedy'],
        help='Matching algorithm (default: hungarian)',
    )
    parser.add_argument(
        '--threshold', type=float, default=0.3,
        help='Similarity threshold for flagging modifications (default: 0.3)',
    )
    parser.add_argument(
        '--include-stdlib', action='store_true',
        help='Include standard library functions in analysis',
    )
    parser.add_argument(
        '--output', '-o', help='Output JSON report path',
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

    # Load binaries
    loader1 = RustBinaryLoader(
        args.binary1, load_debug_info=True,
        include_stdlib=args.include_stdlib,
    )
    loader2 = RustBinaryLoader(
        args.binary2, load_debug_info=True,
        include_stdlib=args.include_stdlib,
    )

    # Match
    matcher = FunctionMatcher(loader1, loader2)
    fps1 = matcher.compute_fingerprints(loader1)
    fps2 = matcher.compute_fingerprints(loader2)

    sim_matrix, addrs1, addrs2 = matcher.compute_similarity_matrix(
        fps1, fps2, method=args.method,
    )
    matches = matcher.match_functions(
        sim_matrix, addrs1, addrs2, method=args.match_method,
    )
    flagged = matcher.flag_suspicious(
        matches, fps1, fps2, threshold=args.threshold,
    )

    # Report
    report = DiffReport(flagged, fps1, fps2, args.binary1, args.binary2)
    print(report.format_text_summary())

    if args.output:
        report.to_json(args.output)
        print(f'\nDetailed report written to: {args.output}')


if __name__ == '__main__':
    main()
