#!/usr/bin/env python3
"""Dump assembly for interesting function pairs for manual analysis."""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor
from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.analysis.block_alignment import BlockAlignmentAnalyzer
from rustdiff.analysis.block_case_analysis import classify_block
from rustdiff.analysis.rust_qualitative import compute_per_feature_similarity

import argparse

def dump_function_pair(loader1, loader2, addr1, addr2, max_blocks=15):
    """Dump assembly and signatures for a matched function pair."""
    name1 = loader1.get_demangled_name(addr1) or f'sub_{addr1:x}'
    name2 = loader2.get_demangled_name(addr2) or f'sub_{addr2:x}'

    blocks1 = loader1.get_blocks_for_function(addr1)
    blocks2 = loader2.get_blocks_for_function(addr2)

    print(f"\n{'='*80}")
    print(f"FUNCTION: {name1}")
    print(f"  O0: 0x{addr1:x} ({len(blocks1)} blocks)")
    print(f"  O2: 0x{addr2:x} ({len(blocks2)} blocks)")
    print(f"{'='*80}")

    # Compute fingerprints
    exec1 = BlockMicroExecutor(loader1)
    exec2 = BlockMicroExecutor(loader2)

    sigs1 = exec1.execute_function(addr1)
    sigs2 = exec2.execute_function(addr2)

    cfg1 = loader1.get_cfg_for_function(addr1)
    cfg2 = loader2.get_cfg_for_function(addr2)

    fp1 = FunctionFingerprint(addr1, name1, sigs1, cfg1)
    fp2 = FunctionFingerprint(addr2, name2, sigs2, cfg2)

    # Align blocks
    aligner = BlockAlignmentAnalyzer()
    alignment = aligner.align_blocks(fp1, fp2)

    # Dump matched pairs with assembly
    matched = [e for e in alignment if e['status'] == 'matched']
    matched.sort(key=lambda e: e['similarity'])  # worst first

    block_map1 = {ba: blk for ba, blk in blocks1}
    block_map2 = {ba: blk for ba, blk in blocks2}

    for i, entry in enumerate(matched[:max_blocks]):
        a1, a2 = entry['addr1'], entry['addr2']
        sim = entry['similarity']

        print(f"\n{'─'*80}")
        print(f"MATCHED PAIR #{i+1}  (similarity: {sim:.3f})")

        # Per-feature
        if a1 in sigs1 and a2 in sigs2:
            s1, s2 = sigs1[a1], sigs2[a2]
            bt1 = classify_block(s1, cfg1, a1)
            bt2 = classify_block(s2, cfg2, a2)
            pf = compute_per_feature_similarity(s1, s2)
            print(f"  Block types: O0={bt1.name}, O2={bt2.name}")
            print(f"  Per-feature: ", end='')
            for feat, v in pf.items():
                import math
                if math.isnan(v):
                    continue
                marker = '✓' if v > 0.7 else ('~' if v > 0.3 else '✗')
                print(f"{feat}={v:.2f}{marker} ", end='')
            print()

            # Show signatures
            print(f"\n  O0 sig: opcodes={s1.opcode_sequence}")
            print(f"          constants={s1.constants}")
            print(f"          concrete_outputs={s1.concrete_outputs}")
            print(f"          dataflow={s1.dataflow_edges}")
            print(f"          callees={s1.callee_names}")
            print(f"          strings={s1.string_refs}")

            print(f"\n  O2 sig: opcodes={s2.opcode_sequence}")
            print(f"          constants={s2.constants}")
            print(f"          concrete_outputs={s2.concrete_outputs}")
            print(f"          dataflow={s2.dataflow_edges}")
            print(f"          callees={s2.callee_names}")
            print(f"          strings={s2.string_refs}")

        # Assembly - O0
        print(f"\n  O0 Block 0x{a1:x}:")
        if a1 in block_map1:
            blk = block_map1[a1]
            for insn in blk.capstone.insns:
                print(f"    0x{insn.address:x}: {insn.mnemonic:8s} {insn.op_str}")
        else:
            print(f"    (block not found in loader)")

        # Assembly - O2
        print(f"\n  O2 Block 0x{a2:x}:")
        if a2 in block_map2:
            blk = block_map2[a2]
            for insn in blk.capstone.insns:
                print(f"    0x{insn.address:x}: {insn.mnemonic:8s} {insn.op_str}")
        else:
            print(f"    (block not found in loader)")

    # Show unmatched blocks
    removed = [e for e in alignment if e['status'] == 'removed']
    new = [e for e in alignment if e['status'] == 'new']
    if removed:
        print(f"\n  REMOVED blocks (O0 only): {len(removed)}")
        for e in removed[:5]:
            a = e['addr1']
            if a in block_map1:
                blk = block_map1[a]
                insns = list(blk.capstone.insns)
                print(f"    0x{a:x} ({len(insns)} insns): ", end='')
                print(' '.join(i.mnemonic for i in insns[:8]))
    if new:
        print(f"\n  NEW blocks (O2 only): {len(new)}")
        for e in new[:5]:
            a = e['addr2']
            if a in block_map2:
                blk = block_map2[a]
                insns = list(blk.capstone.insns)
                print(f"    0x{a:x} ({len(insns)} insns): ", end='')
                print(' '.join(i.mnemonic for i in insns[:8]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--binary-o0', required=True)
    parser.add_argument('--binary-o2', required=True)
    parser.add_argument('--pairs', required=True,
                        help='Comma-separated hex addr pairs: a1:a2,a1:a2,...')
    parser.add_argument('--max-blocks', type=int, default=10)
    args = parser.parse_args()

    print(f"Loading O0: {args.binary_o0}")
    try:
        loader1 = RustBinaryLoader(args.binary_o0, load_debug_info=True)
    except Exception:
        loader1 = RustBinaryLoader(args.binary_o0, load_debug_info=False)

    print(f"Loading O2: {args.binary_o2}")
    try:
        loader2 = RustBinaryLoader(args.binary_o2, load_debug_info=True)
    except Exception:
        loader2 = RustBinaryLoader(args.binary_o2, load_debug_info=False)

    for pair_str in args.pairs.split(','):
        a1_s, a2_s = pair_str.strip().split(':')
        a1, a2 = int(a1_s, 16), int(a2_s, 16)
        dump_function_pair(loader1, loader2, a1, a2, args.max_blocks)


if __name__ == '__main__':
    main()
