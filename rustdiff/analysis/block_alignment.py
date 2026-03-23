"""Block-level alignment analysis for matched function pairs."""

import logging

import numpy as np
from scipy.optimize import linear_sum_assignment

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.micro_exec.value_signature import BlockValueSignature

logger = logging.getLogger(__name__)


def block_similarity(sig1: BlockValueSignature,
                     sig2: BlockValueSignature) -> float:
    """Compute similarity between two block signatures."""
    scores = []

    # Opcode sequence similarity (normalized LCS-like)
    if sig1.opcode_sequence and sig2.opcode_sequence:
        common_ops = set(sig1.opcode_sequence) & set(sig2.opcode_sequence)
        all_ops = set(sig1.opcode_sequence) | set(sig2.opcode_sequence)
        if all_ops:
            scores.append(len(common_ops) / len(all_ops))

    # Constant overlap
    c1 = set(sig1.constants)
    c2 = set(sig2.constants)
    if c1 or c2:
        if c1 | c2:
            scores.append(len(c1 & c2) / len(c1 | c2))

    # Feature set Jaccard
    f1 = sig1.to_feature_set()
    f2 = sig2.to_feature_set()
    if f1 or f2:
        union = len(f1 | f2)
        if union > 0:
            scores.append(len(f1 & f2) / union)

    # Instruction count similarity
    max_insns = max(sig1.num_instructions, sig2.num_instructions)
    if max_insns > 0:
        diff = abs(sig1.num_instructions - sig2.num_instructions)
        scores.append(1.0 - diff / max_insns)

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


class BlockAlignmentAnalyzer:
    """Drill down into block-level alignment for matched function pairs.

    Uses Hungarian matching on blocks within a matched function pair
    to identify which blocks correspond and where differences arise.
    """

    def align_blocks(
        self,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
    ) -> list[dict]:
        """Produce block-to-block alignment within a matched pair.

        Returns list of dicts with keys:
        - addr1, addr2: block addresses (None if unmatched)
        - similarity: block-level similarity score
        - status: 'matched', 'new', 'removed'
        """
        addrs1 = sorted(fp1.block_sigs.keys())
        addrs2 = sorted(fp2.block_sigs.keys())
        n1, n2 = len(addrs1), len(addrs2)

        if n1 == 0 and n2 == 0:
            return []

        # Build block-level similarity matrix
        sim_matrix = np.zeros((n1, n2))
        for i, a1 in enumerate(addrs1):
            for j, a2 in enumerate(addrs2):
                sim_matrix[i, j] = block_similarity(
                    fp1.block_sigs[a1], fp2.block_sigs[a2],
                )

        # Hungarian matching
        cost = -sim_matrix
        row_ind, col_ind = linear_sum_assignment(cost)

        alignment = []
        matched_rows = set()
        matched_cols = set()

        for r, c in zip(row_ind, col_ind):
            matched_rows.add(r)
            matched_cols.add(c)
            alignment.append({
                'addr1': addrs1[r],
                'addr2': addrs2[c],
                'similarity': sim_matrix[r, c],
                'status': 'matched',
            })

        # Unmatched blocks in binary 1 (removed)
        for i in range(n1):
            if i not in matched_rows:
                alignment.append({
                    'addr1': addrs1[i],
                    'addr2': None,
                    'similarity': 0.0,
                    'status': 'removed',
                })

        # Unmatched blocks in binary 2 (new)
        for j in range(n2):
            if j not in matched_cols:
                alignment.append({
                    'addr1': None,
                    'addr2': addrs2[j],
                    'similarity': 0.0,
                    'status': 'new',
                })

        return sorted(alignment, key=lambda x: -(x['similarity']))

    def identify_rust_patterns(
        self,
        alignment: list[dict],
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
    ) -> dict:
        """Identify Rust-specific patterns in block alignment differences.

        Detects:
        - Bounds check insertion/removal across opt levels
        - Iterator unrolling differences
        - Drop glue changes
        - Panic path differences
        """
        patterns = {
            'bounds_check_diff': False,
            'unrolling_diff': False,
            'drop_glue_diff': False,
            'panic_path_diff': False,
            'iterator_diff': False,
            'block_count_ratio': 0.0,
            'low_similarity_blocks': 0,
            'perfect_match_blocks': 0,
            'drop_glue_blocks_1': 0,
            'drop_glue_blocks_2': 0,
            'panic_path_blocks_1': 0,
            'panic_path_blocks_2': 0,
        }

        if fp1.num_blocks > 0 and fp2.num_blocks > 0:
            patterns['block_count_ratio'] = (
                fp1.num_blocks / fp2.num_blocks
            )

        # Count Rust-specific block types in each binary
        for sig in fp1.block_sigs.values():
            if _is_drop_glue_block(sig):
                patterns['drop_glue_blocks_1'] += 1
            if _is_panic_path_block(sig):
                patterns['panic_path_blocks_1'] += 1
        for sig in fp2.block_sigs.values():
            if _is_drop_glue_block(sig):
                patterns['drop_glue_blocks_2'] += 1
            if _is_panic_path_block(sig):
                patterns['panic_path_blocks_2'] += 1

        if patterns['drop_glue_blocks_1'] != patterns['drop_glue_blocks_2']:
            patterns['drop_glue_diff'] = True
        if patterns['panic_path_blocks_1'] != patterns['panic_path_blocks_2']:
            patterns['panic_path_diff'] = True

        for entry in alignment:
            if entry['status'] != 'matched':
                continue
            if entry['similarity'] < 0.3:
                patterns['low_similarity_blocks'] += 1
            if entry['similarity'] > 0.95:
                patterns['perfect_match_blocks'] += 1

            # Check for bounds-check-like patterns
            if entry['addr1'] and entry['addr2']:
                sig1 = fp1.block_sigs.get(entry['addr1'])
                sig2 = fp2.block_sigs.get(entry['addr2'])
                if sig1 and sig2:
                    ops1 = set(sig1.opcode_sequence)
                    ops2 = set(sig2.opcode_sequence)
                    # Bounds checks typically involve cmp+jcc
                    has_cmp1 = 'cmp' in ops1 and 'jcc' in ops1
                    has_cmp2 = 'cmp' in ops2 and 'jcc' in ops2
                    if has_cmp1 != has_cmp2:
                        patterns['bounds_check_diff'] = True

                    # Iterator state block: cmp + add in a loop-like pattern
                    is_iter1 = _is_iterator_block(sig1)
                    is_iter2 = _is_iterator_block(sig2)
                    if is_iter1 != is_iter2:
                        patterns['iterator_diff'] = True

        # Detect unrolling: significant block count difference
        # with mostly-matched blocks
        if fp1.num_blocks > 0 and fp2.num_blocks > 0:
            ratio = max(fp1.num_blocks, fp2.num_blocks) / min(
                fp1.num_blocks, fp2.num_blocks
            )
            if ratio > 1.5:
                patterns['unrolling_diff'] = True

        return patterns


def _is_drop_glue_block(sig: BlockValueSignature) -> bool:
    """Detect a block that calls drop_in_place<T> or Drop::drop."""
    for name in sig.callee_names:
        if 'drop_in_place' in name or 'Drop::drop' in name or '__rdl_' in name:
            return True
    if 'call' in set(sig.opcode_sequence):
        # Heuristic: very short block with a single call to a drop-like target
        if sig.num_instructions <= 3:
            return False  # Can't confirm without callee info
    return False


def _is_panic_path_block(sig: BlockValueSignature) -> bool:
    """Detect a block on a panic/unwind cold path."""
    for name in sig.callee_names:
        if any(p in name for p in (
            'core::panicking', 'rust_begin_unwind',
            'panic_bounds_check', 'panic_fmt',
            'panic_nounwind', 'panic_cannot_unwind',
        )):
            return True
    # Heuristic: block references a panic-related string
    for s in sig.string_refs:
        if any(p in s.lower() for p in (
            'panic', 'overflow', 'index out of bounds',
            'assertion failed', 'unwrap()',
        )):
            return True
    return False


def _is_iterator_block(sig: BlockValueSignature) -> bool:
    """Detect an iterator state/loop counter block."""
    ops = set(sig.opcode_sequence)
    # Iterator blocks typically: compare loop bound, increment counter, branch
    has_cmp = 'cmp' in ops
    has_arith = 'add' in ops or 'sub' in ops
    has_branch = 'jcc' in ops
    return has_cmp and has_arith and has_branch and sig.num_instructions <= 6
