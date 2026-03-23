"""Block-level feature impact analysis for case studies.

Provides tools to understand which block features drive correct block
alignment and what causes misalignment, with Rust-specific block type
classification.
"""

import logging
from collections import defaultdict
from enum import Enum, auto

import numpy as np
import pandas as pd
from scipy.optimize import linear_sum_assignment

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.micro_exec.value_signature import BlockValueSignature
from rustdiff.analysis.block_alignment import (
    BlockAlignmentAnalyzer,
    block_similarity,
)

logger = logging.getLogger(__name__)


class BlockType(Enum):
    """Classification of a basic block's role in the function."""
    BOUNDS_CHECK = auto()
    LOOP_HEADER = auto()
    PROLOGUE = auto()
    EPILOGUE = auto()
    DROP_GLUE = auto()
    PANIC_PATH = auto()
    ITERATOR_STATE = auto()
    BODY = auto()
    UNKNOWN = auto()


class FailureCategory(Enum):
    """Root cause categories for block misalignment."""
    ELIMINATED = auto()       # Block removed by optimization
    SPLIT = auto()            # Block split into multiple
    MERGED = auto()           # Multiple blocks merged into one
    RECOMPUTED = auto()       # Same location, different computation
    REORDERED = auto()        # Block reordered in layout
    NEW_BLOCK = auto()        # Block has no counterpart


# Feature components used for block similarity ablation
BLOCK_FEATURES = [
    'opcodes',
    'constants',
    'concrete_values',
    'memory_pattern',
    'dataflow_edges',
    'instruction_count',
    'callee_names',
    'string_refs',
]


def classify_block(
    sig: BlockValueSignature,
    cfg=None,
    block_addr: int | None = None,
) -> BlockType:
    """Classify a block by its Rust-specific role.

    Args:
        sig: The block's value signature.
        cfg: Optional networkx DiGraph of the function CFG.
        block_addr: The block's address (for CFG lookups).
    """
    ops = set(sig.opcode_sequence)

    # Prologue: push/sub sp only
    if set(sig.opcode_sequence) <= {'push', 'mov', 'sub', 'nop'}:
        if sig.num_instructions <= 5:
            return BlockType.PROLOGUE

    # Epilogue: pop/ret only
    if set(sig.opcode_sequence) <= {'pop', 'mov', 'add', 'ret', 'nop'}:
        if 'ret' in ops and sig.num_instructions <= 5:
            return BlockType.EPILOGUE

    # Drop glue: calls drop_in_place or Drop::drop
    for name in sig.callee_names:
        if 'drop_in_place' in name or 'Drop::drop' in name:
            return BlockType.DROP_GLUE

    # Panic path: calls panic functions or references panic strings
    for name in sig.callee_names:
        if any(p in name for p in (
            'core::panicking', 'rust_begin_unwind',
            'panic_bounds_check', 'panic_fmt',
        )):
            return BlockType.PANIC_PATH
    for s in sig.string_refs:
        if any(p in s.lower() for p in ('panic', 'overflow', 'index out of')):
            return BlockType.PANIC_PATH

    # Bounds check: cmp + jcc with few instructions, typically guards
    if ('cmp' in ops and 'jcc' in ops and sig.num_instructions <= 4
            and sig.out_degree == 2):
        return BlockType.BOUNDS_CHECK

    # Iterator state: cmp + add/sub in a small block (loop counter update)
    if ('cmp' in ops and ('add' in ops or 'sub' in ops) and 'jcc' in ops
            and sig.num_instructions <= 6):
        # Check if this is a loop header via CFG back-edges
        if cfg and block_addr:
            try:
                preds = list(cfg.predecessors(block_addr))
                succs = list(cfg.successors(block_addr))
                # Loop header: has a predecessor that is also reachable from it
                for pred in preds:
                    if pred > block_addr:  # back-edge heuristic
                        return BlockType.LOOP_HEADER
            except Exception:
                pass
        return BlockType.ITERATOR_STATE

    # Loop header via CFG analysis
    if cfg and block_addr:
        try:
            preds = list(cfg.predecessors(block_addr))
            for pred in preds:
                if pred > block_addr:
                    return BlockType.LOOP_HEADER
        except Exception:
            pass

    # Default: body block
    if sig.num_instructions > 0:
        return BlockType.BODY

    return BlockType.UNKNOWN


def _block_similarity_without(
    sig1: BlockValueSignature,
    sig2: BlockValueSignature,
    exclude: str,
) -> float:
    """Compute block similarity with one feature component excluded.

    Args:
        sig1, sig2: Block signatures to compare.
        exclude: Name of the feature to exclude (from BLOCK_FEATURES).
    """
    scores = []

    # Opcode set similarity
    if exclude != 'opcodes':
        if sig1.opcode_sequence and sig2.opcode_sequence:
            common = set(sig1.opcode_sequence) & set(sig2.opcode_sequence)
            total = set(sig1.opcode_sequence) | set(sig2.opcode_sequence)
            if total:
                scores.append(len(common) / len(total))

    # Constant overlap
    if exclude != 'constants':
        c1, c2 = set(sig1.constants), set(sig2.constants)
        if c1 or c2:
            union = c1 | c2
            if union:
                scores.append(len(c1 & c2) / len(union))

    # Concrete value overlap
    if exclude != 'concrete_values':
        v1 = set()
        for vals in sig1.concrete_outputs.values():
            v1.update(vals)
        v2 = set()
        for vals in sig2.concrete_outputs.values():
            v2.update(vals)
        if v1 or v2:
            union = v1 | v2
            if union:
                scores.append(len(v1 & v2) / len(union))

    # Memory pattern
    if exclude != 'memory_pattern':
        m1 = {(m.kind.name, m.size, m.is_write) for m in sig1.memory_pattern}
        m2 = {(m.kind.name, m.size, m.is_write) for m in sig2.memory_pattern}
        if m1 or m2:
            union = m1 | m2
            if union:
                scores.append(len(m1 & m2) / len(union))

    # Dataflow edges
    if exclude != 'dataflow_edges':
        df1, df2 = sig1.dataflow_edges, sig2.dataflow_edges
        if df1 or df2:
            union = df1 | df2
            if union:
                scores.append(len(df1 & df2) / len(union))

    # Instruction count
    if exclude != 'instruction_count':
        max_insns = max(sig1.num_instructions, sig2.num_instructions)
        if max_insns > 0:
            diff = abs(sig1.num_instructions - sig2.num_instructions)
            scores.append(1.0 - diff / max_insns)

    # Callee names
    if exclude != 'callee_names':
        cn1, cn2 = set(sig1.callee_names), set(sig2.callee_names)
        if cn1 or cn2:
            union = cn1 | cn2
            if union:
                scores.append(len(cn1 & cn2) / len(union))

    # String refs
    if exclude != 'string_refs':
        sr1, sr2 = set(sig1.string_refs), set(sig2.string_refs)
        if sr1 or sr2:
            union = sr1 | sr2
            if union:
                scores.append(len(sr1 & sr2) / len(union))

    if not scores:
        return 0.0
    return sum(scores) / len(scores)


class BlockFeatureAnalyzer:
    """Analyze feature impact on block-level matching accuracy."""

    def __init__(self):
        self._aligner = BlockAlignmentAnalyzer()

    def block_ablation_study(
        self,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
        gt_block_pairs: list[tuple[int, int]] | None = None,
    ) -> pd.DataFrame:
        """Run block-level ablation: remove each feature, measure accuracy.

        If gt_block_pairs is not provided, uses the full-feature alignment
        as pseudo-groundtruth.

        Returns DataFrame with columns:
        [feature_removed, mean_similarity, accuracy, accuracy_drop]
        """
        addrs1 = sorted(fp1.block_sigs.keys())
        addrs2 = sorted(fp2.block_sigs.keys())

        if not addrs1 or not addrs2:
            return pd.DataFrame()

        # Establish groundtruth alignment using full features
        if gt_block_pairs is None:
            alignment = self._aligner.align_blocks(fp1, fp2)
            gt_block_pairs = [
                (e['addr1'], e['addr2'])
                for e in alignment
                if e['status'] == 'matched' and e['similarity'] > 0.5
            ]

        # Baseline: full-feature block similarity
        baseline = self._evaluate_block_matching(
            fp1, fp2, addrs1, addrs2, gt_block_pairs, exclude=None,
        )

        results = [{'feature_removed': 'none (baseline)', **baseline}]

        # Remove each feature
        for feat_name in BLOCK_FEATURES:
            row = self._evaluate_block_matching(
                fp1, fp2, addrs1, addrs2, gt_block_pairs, exclude=feat_name,
            )
            row['feature_removed'] = feat_name
            row['accuracy_drop'] = baseline['accuracy'] - row['accuracy']
            results.append(row)

        return pd.DataFrame(results)

    def block_type_accuracy(
        self,
        alignment: list[dict],
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
    ) -> pd.DataFrame:
        """Compute match accuracy broken down by block type.

        Returns DataFrame with columns:
        [block_type, total, matched, accuracy, mean_similarity]
        """
        type_stats = defaultdict(lambda: {
            'total': 0, 'matched': 0, 'sim_sum': 0.0,
        })

        for entry in alignment:
            addr = entry.get('addr1') or entry.get('addr2')
            if addr is None:
                continue

            # Classify the block
            if entry['addr1'] and entry['addr1'] in fp1.block_sigs:
                sig = fp1.block_sigs[entry['addr1']]
                btype = classify_block(sig, fp1.cfg, entry['addr1'])
            elif entry['addr2'] and entry['addr2'] in fp2.block_sigs:
                sig = fp2.block_sigs[entry['addr2']]
                btype = classify_block(sig, fp2.cfg, entry['addr2'])
            else:
                btype = BlockType.UNKNOWN

            stats = type_stats[btype.name]
            stats['total'] += 1
            if entry['status'] == 'matched' and entry['similarity'] > 0.5:
                stats['matched'] += 1
            stats['sim_sum'] += entry['similarity']

        rows = []
        for btype_name, stats in sorted(type_stats.items()):
            rows.append({
                'block_type': btype_name,
                'total': stats['total'],
                'matched': stats['matched'],
                'accuracy': (stats['matched'] / stats['total']
                             if stats['total'] > 0 else 0.0),
                'mean_similarity': (stats['sim_sum'] / stats['total']
                                    if stats['total'] > 0 else 0.0),
            })

        return pd.DataFrame(rows)

    def failure_taxonomy(
        self,
        alignment: list[dict],
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
    ) -> pd.DataFrame:
        """Categorize root causes of block misalignment.

        Returns DataFrame with columns:
        [category, count, example_addr1, example_addr2]
        """
        categories = defaultdict(lambda: {'count': 0, 'examples': []})

        n1 = fp1.num_blocks
        n2 = fp2.num_blocks

        for entry in alignment:
            if entry['status'] == 'matched' and entry['similarity'] > 0.5:
                continue  # Skip well-matched blocks

            cat = self._classify_failure(entry, fp1, fp2, n1, n2)
            info = categories[cat.name]
            info['count'] += 1
            if len(info['examples']) < 3:
                info['examples'].append(
                    (entry.get('addr1'), entry.get('addr2'))
                )

        rows = []
        for cat_name, info in sorted(categories.items()):
            example = info['examples'][0] if info['examples'] else (None, None)
            rows.append({
                'category': cat_name,
                'count': info['count'],
                'example_addr1': example[0],
                'example_addr2': example[1],
            })

        return pd.DataFrame(rows)

    def run_full_analysis(
        self,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
        gt_block_pairs: list[tuple[int, int]] | None = None,
    ) -> dict:
        """Run the complete block-level feature analysis.

        Returns dict with:
        - alignment: block alignment results
        - ablation: DataFrame of feature ablation results
        - type_accuracy: DataFrame of per-block-type accuracy
        - failure_taxonomy: DataFrame of failure categories
        """
        alignment = self._aligner.align_blocks(fp1, fp2)

        ablation = self.block_ablation_study(fp1, fp2, gt_block_pairs)
        type_acc = self.block_type_accuracy(alignment, fp1, fp2)
        failures = self.failure_taxonomy(alignment, fp1, fp2)

        return {
            'alignment': alignment,
            'ablation': ablation,
            'type_accuracy': type_acc,
            'failure_taxonomy': failures,
        }

    def _evaluate_block_matching(
        self,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
        addrs1: list[int],
        addrs2: list[int],
        gt_pairs: list[tuple[int, int]],
        exclude: str | None,
    ) -> dict:
        """Evaluate block matching accuracy with optional feature exclusion."""
        n1, n2 = len(addrs1), len(addrs2)
        sim_matrix = np.zeros((n1, n2))

        for i, a1 in enumerate(addrs1):
            for j, a2 in enumerate(addrs2):
                if exclude:
                    sim_matrix[i, j] = _block_similarity_without(
                        fp1.block_sigs[a1], fp2.block_sigs[a2], exclude,
                    )
                else:
                    sim_matrix[i, j] = block_similarity(
                        fp1.block_sigs[a1], fp2.block_sigs[a2],
                    )

        # Hungarian matching
        cost = -sim_matrix
        row_ind, col_ind = linear_sum_assignment(cost)

        # Build predicted matching
        predicted = {}
        for r, c in zip(row_ind, col_ind):
            predicted[addrs1[r]] = addrs2[c]

        # Evaluate against groundtruth
        gt_dict = dict(gt_pairs)
        correct = 0
        total = len(gt_pairs)
        for a1, a2 in gt_pairs:
            if predicted.get(a1) == a2:
                correct += 1

        accuracy = correct / total if total > 0 else 0.0
        mean_sim = float(np.mean([
            sim_matrix[r, c] for r, c in zip(row_ind, col_ind)
        ])) if len(row_ind) > 0 else 0.0

        return {
            'accuracy': accuracy,
            'mean_similarity': mean_sim,
            'correct': correct,
            'total': total,
        }

    def _classify_failure(
        self,
        entry: dict,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
        n1: int,
        n2: int,
    ) -> FailureCategory:
        """Classify the root cause of a block alignment failure."""
        if entry['status'] == 'removed':
            # Block in binary 1 but not matched in binary 2
            if n2 < n1:
                return FailureCategory.ELIMINATED
            return FailureCategory.MERGED

        if entry['status'] == 'new':
            # Block in binary 2 but not in binary 1
            if n2 > n1:
                return FailureCategory.SPLIT
            return FailureCategory.NEW_BLOCK

        # Matched but low similarity
        if entry['addr1'] and entry['addr2']:
            sig1 = fp1.block_sigs.get(entry['addr1'])
            sig2 = fp2.block_sigs.get(entry['addr2'])
            if sig1 and sig2:
                # Check if opcodes differ significantly
                ops1 = set(sig1.opcode_sequence)
                ops2 = set(sig2.opcode_sequence)
                op_overlap = (len(ops1 & ops2) / len(ops1 | ops2)
                              if ops1 | ops2 else 0)
                if op_overlap < 0.3:
                    return FailureCategory.RECOMPUTED
                # Similar opcodes but different arrangement
                if op_overlap > 0.7 and entry['similarity'] < 0.5:
                    return FailureCategory.REORDERED

        return FailureCategory.RECOMPUTED
