"""Rust-specific qualitative analysis of basic block matching.

Given groundtruth-matched function pairs, this module drills into
block-level alignment to identify:
- Which block features drive correct matches (feature contribution)
- Which Rust compiler optimizations destroy feature signals
- How feature stability varies across block types and projects
"""

import logging
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

import numpy as np
import pandas as pd

from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.micro_exec.value_signature import BlockValueSignature
from rustdiff.analysis.block_alignment import (
    BlockAlignmentAnalyzer,
    block_similarity,
    _is_drop_glue_block,
    _is_panic_path_block,
)
from rustdiff.analysis.block_case_analysis import (
    BlockType,
    classify_block,
    BLOCK_FEATURES,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class FeatureStability(Enum):
    """Stability of a block feature across O0→O2."""
    STABLE = auto()       # similarity > 0.7
    DEGRADED = auto()     # 0.3 < similarity <= 0.7
    DESTROYED = auto()    # similarity <= 0.3
    EMPTY = auto()        # both sides empty (no signal either way)


class OptimizationEffect(Enum):
    """Rust-specific compiler optimization effects detected at block level."""
    BOUNDS_CHECK_ELIMINATION = auto()
    LOOP_UNROLLING = auto()
    DROP_GLUE_REMOVAL = auto()
    PANIC_PATH_OPTIMIZATION = auto()
    INLINING_EXPANSION = auto()
    ITERATOR_LOWERING = auto()
    BLOCK_MERGING = auto()
    BLOCK_SPLITTING = auto()


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------

@dataclass
class BlockPairDetail:
    """Per-matched-block-pair analysis result."""
    addr1: Optional[int]
    addr2: Optional[int]
    overall_similarity: float
    status: str  # 'matched', 'removed', 'new'
    block_type_o0: Optional[BlockType] = None
    block_type_o2: Optional[BlockType] = None
    per_feature_sim: dict = field(default_factory=dict)
    per_feature_stability: dict = field(default_factory=dict)


@dataclass
class FunctionAnalysisResult:
    """Per-function qualitative analysis result."""
    func_addr_o0: int
    func_addr_o2: int
    func_name: str
    num_blocks_o0: int
    num_blocks_o2: int
    mean_block_similarity: float
    block_pairs: list[BlockPairDetail] = field(default_factory=list)
    optimization_effects: list[OptimizationEffect] = field(default_factory=list)
    block_type_counts_o0: dict = field(default_factory=dict)
    block_type_counts_o2: dict = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Per-feature similarity computation
# ---------------------------------------------------------------------------

def compute_per_feature_similarity(
    sig1: BlockValueSignature,
    sig2: BlockValueSignature,
) -> dict[str, float]:
    """Compute Jaccard similarity for each feature component independently.

    Returns dict mapping feature name -> similarity (0.0 to 1.0).
    For empty-vs-empty features, returns NaN (handled as EMPTY).
    """
    result = {}

    # opcodes
    if sig1.opcode_sequence or sig2.opcode_sequence:
        s1, s2 = set(sig1.opcode_sequence), set(sig2.opcode_sequence)
        union = s1 | s2
        result['opcodes'] = len(s1 & s2) / len(union) if union else 0.0
    else:
        result['opcodes'] = float('nan')

    # constants
    c1, c2 = set(sig1.constants), set(sig2.constants)
    if c1 or c2:
        union = c1 | c2
        result['constants'] = len(c1 & c2) / len(union) if union else 0.0
    else:
        result['constants'] = float('nan')

    # concrete_values
    v1, v2 = set(), set()
    for vals in sig1.concrete_outputs.values():
        v1.update(vals)
    for vals in sig2.concrete_outputs.values():
        v2.update(vals)
    if v1 or v2:
        union = v1 | v2
        result['concrete_values'] = len(v1 & v2) / len(union) if union else 0.0
    else:
        result['concrete_values'] = float('nan')

    # memory_pattern
    m1 = {(m.kind.name, m.size, m.is_write) for m in sig1.memory_pattern}
    m2 = {(m.kind.name, m.size, m.is_write) for m in sig2.memory_pattern}
    if m1 or m2:
        union = m1 | m2
        result['memory_pattern'] = len(m1 & m2) / len(union) if union else 0.0
    else:
        result['memory_pattern'] = float('nan')

    # dataflow_edges
    df1, df2 = sig1.dataflow_edges, sig2.dataflow_edges
    if df1 or df2:
        union = df1 | df2
        result['dataflow_edges'] = len(df1 & df2) / len(union) if union else 0.0
    else:
        result['dataflow_edges'] = float('nan')

    # instruction_count
    max_insns = max(sig1.num_instructions, sig2.num_instructions)
    if max_insns > 0:
        diff = abs(sig1.num_instructions - sig2.num_instructions)
        result['instruction_count'] = 1.0 - diff / max_insns
    else:
        result['instruction_count'] = float('nan')

    # callee_names
    cn1, cn2 = set(sig1.callee_names), set(sig2.callee_names)
    if cn1 or cn2:
        union = cn1 | cn2
        result['callee_names'] = len(cn1 & cn2) / len(union) if union else 0.0
    else:
        result['callee_names'] = float('nan')

    # string_refs
    sr1, sr2 = set(sig1.string_refs), set(sig2.string_refs)
    if sr1 or sr2:
        union = sr1 | sr2
        result['string_refs'] = len(sr1 & sr2) / len(union) if union else 0.0
    else:
        result['string_refs'] = float('nan')

    return result


def classify_stability(sim: float) -> FeatureStability:
    """Classify a per-feature similarity value into stability category."""
    if np.isnan(sim):
        return FeatureStability.EMPTY
    if sim > 0.7:
        return FeatureStability.STABLE
    if sim > 0.3:
        return FeatureStability.DEGRADED
    return FeatureStability.DESTROYED


# ---------------------------------------------------------------------------
# Optimization effect detection
# ---------------------------------------------------------------------------

def detect_optimization_effects(
    alignment: list[dict],
    fp1: FunctionFingerprint,
    fp2: FunctionFingerprint,
) -> list[OptimizationEffect]:
    """Detect Rust-specific optimization effects from block alignment."""
    effects = []
    n1, n2 = fp1.num_blocks, fp2.num_blocks

    # Count block types in each binary
    type_counts_o0 = defaultdict(int)
    type_counts_o2 = defaultdict(int)
    for addr, sig in fp1.block_sigs.items():
        bt = classify_block(sig, fp1.cfg, addr)
        type_counts_o0[bt] += 1
    for addr, sig in fp2.block_sigs.items():
        bt = classify_block(sig, fp2.cfg, addr)
        type_counts_o2[bt] += 1

    # Bounds check elimination: O0 has BOUNDS_CHECK blocks, O2 has fewer/none
    bc_o0 = type_counts_o0.get(BlockType.BOUNDS_CHECK, 0)
    bc_o2 = type_counts_o2.get(BlockType.BOUNDS_CHECK, 0)
    if bc_o0 > 0 and bc_o2 < bc_o0:
        effects.append(OptimizationEffect.BOUNDS_CHECK_ELIMINATION)

    # Drop glue removal
    dg_o0 = type_counts_o0.get(BlockType.DROP_GLUE, 0)
    dg_o2 = type_counts_o2.get(BlockType.DROP_GLUE, 0)
    if dg_o0 > 0 and dg_o2 < dg_o0:
        effects.append(OptimizationEffect.DROP_GLUE_REMOVAL)

    # Panic path optimization
    pp_o0 = type_counts_o0.get(BlockType.PANIC_PATH, 0)
    pp_o2 = type_counts_o2.get(BlockType.PANIC_PATH, 0)
    if pp_o0 > 0 and pp_o2 < pp_o0:
        effects.append(OptimizationEffect.PANIC_PATH_OPTIMIZATION)

    # Iterator lowering
    it_o0 = type_counts_o0.get(BlockType.ITERATOR_STATE, 0)
    it_o2 = type_counts_o2.get(BlockType.ITERATOR_STATE, 0)
    if it_o0 > 0 and it_o0 != it_o2:
        effects.append(OptimizationEffect.ITERATOR_LOWERING)

    # Block merging / splitting
    if n1 > 0 and n2 > 0:
        ratio = n1 / n2
        if ratio > 1.5:
            effects.append(OptimizationEffect.BLOCK_MERGING)
        elif ratio < 0.67:
            effects.append(OptimizationEffect.BLOCK_SPLITTING)

    # Loop unrolling: O2 has significantly more BODY blocks
    body_o0 = type_counts_o0.get(BlockType.BODY, 0)
    body_o2 = type_counts_o2.get(BlockType.BODY, 0)
    if body_o0 > 0 and body_o2 > body_o0 * 1.5:
        effects.append(OptimizationEffect.LOOP_UNROLLING)

    # Inlining expansion: O2 has many more blocks with new callee patterns
    if n2 > n1 * 1.5:
        effects.append(OptimizationEffect.INLINING_EXPANSION)

    return effects


# ---------------------------------------------------------------------------
# Main analyzer
# ---------------------------------------------------------------------------

class RustQualitativeAnalyzer:
    """Qualitative analysis of block matching for Rust binaries."""

    def __init__(self, min_blocks: int = 3):
        self._aligner = BlockAlignmentAnalyzer()
        self._min_blocks = min_blocks

    def analyze_single_pair(
        self,
        fp1: FunctionFingerprint,
        fp2: FunctionFingerprint,
    ) -> FunctionAnalysisResult:
        """Analyze block alignment for a single matched function pair."""
        alignment = self._aligner.align_blocks(fp1, fp2)
        effects = detect_optimization_effects(alignment, fp1, fp2)

        # Block type counts
        btc_o0 = defaultdict(int)
        btc_o2 = defaultdict(int)
        for addr, sig in fp1.block_sigs.items():
            bt = classify_block(sig, fp1.cfg, addr)
            btc_o0[bt.name] += 1
        for addr, sig in fp2.block_sigs.items():
            bt = classify_block(sig, fp2.cfg, addr)
            btc_o2[bt.name] += 1

        # Analyze each block pair
        block_pairs = []
        sim_sum = 0.0
        matched_count = 0

        for entry in alignment:
            bp = BlockPairDetail(
                addr1=entry['addr1'],
                addr2=entry['addr2'],
                overall_similarity=entry['similarity'],
                status=entry['status'],
            )

            # Classify block types
            if entry['addr1'] and entry['addr1'] in fp1.block_sigs:
                bp.block_type_o0 = classify_block(
                    fp1.block_sigs[entry['addr1']], fp1.cfg, entry['addr1']
                )
            if entry['addr2'] and entry['addr2'] in fp2.block_sigs:
                bp.block_type_o2 = classify_block(
                    fp2.block_sigs[entry['addr2']], fp2.cfg, entry['addr2']
                )

            # Per-feature similarity for matched pairs
            if (entry['status'] == 'matched'
                    and entry['addr1'] in fp1.block_sigs
                    and entry['addr2'] in fp2.block_sigs):
                sig1 = fp1.block_sigs[entry['addr1']]
                sig2 = fp2.block_sigs[entry['addr2']]
                bp.per_feature_sim = compute_per_feature_similarity(sig1, sig2)
                bp.per_feature_stability = {
                    feat: classify_stability(sim).name
                    for feat, sim in bp.per_feature_sim.items()
                }
                sim_sum += entry['similarity']
                matched_count += 1

            block_pairs.append(bp)

        mean_sim = sim_sum / matched_count if matched_count > 0 else 0.0

        return FunctionAnalysisResult(
            func_addr_o0=fp1.func_addr,
            func_addr_o2=fp2.func_addr,
            func_name=fp1.func_name,
            num_blocks_o0=fp1.num_blocks,
            num_blocks_o2=fp2.num_blocks,
            mean_block_similarity=mean_sim,
            block_pairs=block_pairs,
            optimization_effects=effects,
            block_type_counts_o0=dict(btc_o0),
            block_type_counts_o2=dict(btc_o2),
        )

    def analyze_corpus(
        self,
        fps1: dict[int, FunctionFingerprint],
        fps2: dict[int, FunctionFingerprint],
        gt_pairs: list[tuple[int, int]],
        project_name: str = '',
        max_functions: int = 0,
    ) -> 'QualitativeReport':
        """Analyze all groundtruth-matched function pairs."""
        results = []
        skipped = 0

        pairs = gt_pairs
        if max_functions > 0:
            pairs = pairs[:max_functions]

        for addr1, addr2 in pairs:
            if addr1 not in fps1 or addr2 not in fps2:
                skipped += 1
                continue
            fp1, fp2 = fps1[addr1], fps2[addr2]
            if fp1.num_blocks < self._min_blocks or fp2.num_blocks < self._min_blocks:
                skipped += 1
                continue

            try:
                result = self.analyze_single_pair(fp1, fp2)
                results.append(result)
            except Exception as e:
                logger.warning(
                    "Failed to analyze %s (0x%x/0x%x): %s",
                    fp1.func_name, addr1, addr2, e,
                )
                skipped += 1

        logger.info(
            "Analyzed %d function pairs, skipped %d (project: %s)",
            len(results), skipped, project_name,
        )

        return QualitativeReport(
            project_name=project_name,
            function_results=results,
            total_gt_pairs=len(gt_pairs),
            skipped=skipped,
        )


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

@dataclass
class QualitativeReport:
    """Container for qualitative analysis results with report generation."""
    project_name: str
    function_results: list[FunctionAnalysisResult]
    total_gt_pairs: int
    skipped: int

    # -- Aggregation methods --

    def feature_stability_summary(self) -> pd.DataFrame:
        """Table 1: For each feature, what % of block pairs are STABLE/DEGRADED/DESTROYED/EMPTY."""
        counts = {feat: defaultdict(int) for feat in BLOCK_FEATURES}
        totals = {feat: 0 for feat in BLOCK_FEATURES}

        for fr in self.function_results:
            for bp in fr.block_pairs:
                if bp.status != 'matched' or not bp.per_feature_stability:
                    continue
                for feat in BLOCK_FEATURES:
                    stab = bp.per_feature_stability.get(feat, 'EMPTY')
                    counts[feat][stab] += 1
                    totals[feat] += 1

        rows = []
        for feat in BLOCK_FEATURES:
            total = totals[feat]
            if total == 0:
                continue
            row = {'feature': feat, 'total_pairs': total}
            for cat in FeatureStability:
                row[f'%{cat.name}'] = counts[feat][cat.name] / total * 100
            # Mean similarity (excluding NaN)
            sims = []
            for fr in self.function_results:
                for bp in fr.block_pairs:
                    if bp.status == 'matched' and feat in bp.per_feature_sim:
                        v = bp.per_feature_sim[feat]
                        if not np.isnan(v):
                            sims.append(v)
            row['mean_similarity'] = np.mean(sims) if sims else 0.0
            rows.append(row)

        return pd.DataFrame(rows)

    def block_type_feature_heatmap(self) -> pd.DataFrame:
        """Table 2: Mean per-feature similarity for each (block_type, feature) pair."""
        # block_type -> feature -> list of similarities
        data = defaultdict(lambda: defaultdict(list))

        for fr in self.function_results:
            for bp in fr.block_pairs:
                if bp.status != 'matched' or not bp.per_feature_sim:
                    continue
                bt = bp.block_type_o0.name if bp.block_type_o0 else 'UNKNOWN'
                for feat, sim in bp.per_feature_sim.items():
                    if not np.isnan(sim):
                        data[bt][feat].append(sim)

        rows = []
        for bt in sorted(data.keys()):
            row = {'block_type': bt}
            for feat in BLOCK_FEATURES:
                sims = data[bt].get(feat, [])
                row[feat] = np.mean(sims) if sims else float('nan')
            # Count
            row['count'] = max(
                len(v) for v in data[bt].values()
            ) if data[bt] else 0
            rows.append(row)

        return pd.DataFrame(rows)

    def optimization_effect_summary(self) -> pd.DataFrame:
        """Table 3: How many functions are affected by each optimization effect."""
        effect_funcs = defaultdict(list)
        for fr in self.function_results:
            for eff in fr.optimization_effects:
                effect_funcs[eff.name].append(fr)

        total = len(self.function_results)
        rows = []
        for eff in OptimizationEffect:
            affected = effect_funcs.get(eff.name, [])
            n = len(affected)
            mean_sim = (
                np.mean([f.mean_block_similarity for f in affected])
                if affected else float('nan')
            )
            # Mean similarity for unaffected functions
            unaffected = [
                f for f in self.function_results
                if eff not in [e for e in f.optimization_effects]
            ]
            mean_sim_unaffected = (
                np.mean([f.mean_block_similarity for f in unaffected])
                if unaffected else float('nan')
            )
            rows.append({
                'effect': eff.name,
                'count': n,
                'pct_affected': n / total * 100 if total > 0 else 0,
                'mean_block_sim_affected': mean_sim,
                'mean_block_sim_unaffected': mean_sim_unaffected,
            })

        return pd.DataFrame(rows)

    def feature_contribution_by_tier(self) -> pd.DataFrame:
        """Table 4: Mean per-feature similarity grouped by function similarity tier."""
        tiers = {
            'high (>0.7)': [],
            'medium (0.4-0.7)': [],
            'low (<0.4)': [],
        }

        for fr in self.function_results:
            if fr.mean_block_similarity > 0.7:
                tiers['high (>0.7)'].append(fr)
            elif fr.mean_block_similarity > 0.4:
                tiers['medium (0.4-0.7)'].append(fr)
            else:
                tiers['low (<0.4)'].append(fr)

        rows = []
        for tier_name, funcs in tiers.items():
            row = {'tier': tier_name, 'num_functions': len(funcs)}
            # Aggregate per-feature similarity across all block pairs in tier
            feat_sims = defaultdict(list)
            for fr in funcs:
                for bp in fr.block_pairs:
                    if bp.status == 'matched' and bp.per_feature_sim:
                        for feat, sim in bp.per_feature_sim.items():
                            if not np.isnan(sim):
                                feat_sims[feat].append(sim)
            for feat in BLOCK_FEATURES:
                sims = feat_sims.get(feat, [])
                row[feat] = np.mean(sims) if sims else float('nan')
            rows.append(row)

        return pd.DataFrame(rows)

    def top_drilldowns(self, n: int = 10) -> list[FunctionAnalysisResult]:
        """Select the N most interesting functions for detailed drilldown.

        Prioritizes: most optimization effects, lowest similarity, most blocks.
        """
        scored = []
        for fr in self.function_results:
            score = (
                len(fr.optimization_effects) * 10
                + (1.0 - fr.mean_block_similarity) * 5
                + max(fr.num_blocks_o0, fr.num_blocks_o2) * 0.1
            )
            scored.append((score, fr))
        scored.sort(key=lambda x: -x[0])
        return [fr for _, fr in scored[:n]]

    # -- Report generation --

    def to_markdown(self) -> str:
        """Generate a full markdown report."""
        lines = []
        lines.append(f'# Rust Qualitative Block Analysis: {self.project_name}')
        lines.append('')

        # Summary
        lines.append('## Overview')
        lines.append('')
        analyzed = len(self.function_results)
        lines.append(f'| Metric | Value |')
        lines.append(f'|--------|-------|')
        lines.append(f'| Groundtruth pairs | {self.total_gt_pairs} |')
        lines.append(f'| Analyzed (>= min_blocks) | {analyzed} |')
        lines.append(f'| Skipped | {self.skipped} |')
        if self.function_results:
            mean_sim = np.mean([
                f.mean_block_similarity for f in self.function_results
            ])
            lines.append(f'| Mean block similarity | {mean_sim:.3f} |')
            mean_blocks_o0 = np.mean([
                f.num_blocks_o0 for f in self.function_results
            ])
            mean_blocks_o2 = np.mean([
                f.num_blocks_o2 for f in self.function_results
            ])
            lines.append(
                f'| Mean blocks (O0 / O2) | {mean_blocks_o0:.1f} / {mean_blocks_o2:.1f} |'
            )
        lines.append('')

        # Table 1: Feature Stability
        lines.append('## Table 1: Feature Stability Summary')
        lines.append('')
        lines.append(
            'How well does each block feature survive O0→O2 optimization?'
        )
        lines.append('')
        df1 = self.feature_stability_summary()
        if not df1.empty:
            lines.append(_df_to_md(df1, float_fmt='.1f'))
        lines.append('')

        # Table 2: Block Type x Feature Heatmap
        lines.append('## Table 2: Block Type x Feature Heatmap')
        lines.append('')
        lines.append(
            'Mean per-feature similarity by O0 block type (higher = more stable).'
        )
        lines.append('')
        df2 = self.block_type_feature_heatmap()
        if not df2.empty:
            lines.append(_df_to_md(df2, float_fmt='.3f'))
        lines.append('')

        # Table 3: Optimization Effects
        lines.append('## Table 3: Rust Optimization Effect Impact')
        lines.append('')
        df3 = self.optimization_effect_summary()
        if not df3.empty:
            lines.append(_df_to_md(df3, float_fmt='.3f'))
        lines.append('')

        # Table 4: Feature Contribution by Tier
        lines.append('## Table 4: Feature Contribution by Similarity Tier')
        lines.append('')
        lines.append(
            'Mean per-feature similarity for functions grouped by overall block match quality.'
        )
        lines.append('')
        df4 = self.feature_contribution_by_tier()
        if not df4.empty:
            lines.append(_df_to_md(df4, float_fmt='.3f'))
        lines.append('')

        # Top drilldowns
        lines.append('## Top Function Drilldowns')
        lines.append('')
        drilldowns = self.top_drilldowns(10)
        for i, fr in enumerate(drilldowns, 1):
            lines.append(f'### {i}. `{fr.func_name}`')
            lines.append('')
            lines.append(
                f'- Addresses: O0=0x{fr.func_addr_o0:x}, O2=0x{fr.func_addr_o2:x}'
            )
            lines.append(
                f'- Blocks: O0={fr.num_blocks_o0}, O2={fr.num_blocks_o2}'
            )
            lines.append(
                f'- Mean block similarity: {fr.mean_block_similarity:.3f}'
            )
            if fr.optimization_effects:
                effs = ', '.join(e.name for e in fr.optimization_effects)
                lines.append(f'- Optimization effects: {effs}')
            lines.append('')

            # Block type breakdown
            lines.append('**Block types (O0 / O2):**')
            lines.append('')
            all_types = sorted(
                set(list(fr.block_type_counts_o0.keys())
                    + list(fr.block_type_counts_o2.keys()))
            )
            if all_types:
                lines.append('| Type | O0 | O2 |')
                lines.append('|------|----|----|')
                for bt in all_types:
                    c0 = fr.block_type_counts_o0.get(bt, 0)
                    c2 = fr.block_type_counts_o2.get(bt, 0)
                    lines.append(f'| {bt} | {c0} | {c2} |')
                lines.append('')

            # Per-block feature detail (top 5 matched pairs)
            matched_pairs = [
                bp for bp in fr.block_pairs
                if bp.status == 'matched' and bp.per_feature_sim
            ]
            if matched_pairs:
                lines.append('**Block-level feature similarity (matched pairs):**')
                lines.append('')
                header = '| O0 Block | O2 Block | Overall'
                for feat in BLOCK_FEATURES:
                    header += f' | {feat}'
                header += ' |'
                lines.append(header)
                sep = '|----------|----------|--------'
                for _ in BLOCK_FEATURES:
                    sep += '|--------'
                sep += '|'
                lines.append(sep)

                for bp in matched_pairs[:8]:
                    a1 = f'0x{bp.addr1:x}' if bp.addr1 else '-'
                    a2 = f'0x{bp.addr2:x}' if bp.addr2 else '-'
                    row = f'| {a1} | {a2} | {bp.overall_similarity:.2f}'
                    for feat in BLOCK_FEATURES:
                        v = bp.per_feature_sim.get(feat, float('nan'))
                        if np.isnan(v):
                            row += ' | -'
                        else:
                            stab = bp.per_feature_stability.get(feat, '')
                            marker = ''
                            if stab == 'DESTROYED':
                                marker = ' (!)'
                            elif stab == 'DEGRADED':
                                marker = ' (?)'
                            row += f' | {v:.2f}{marker}'
                    row += ' |'
                    lines.append(row)
                lines.append('')

            # Unmatched blocks summary
            removed = sum(1 for bp in fr.block_pairs if bp.status == 'removed')
            new = sum(1 for bp in fr.block_pairs if bp.status == 'new')
            if removed or new:
                lines.append(
                    f'**Unmatched blocks:** {removed} removed (O0 only), '
                    f'{new} new (O2 only)'
                )
                lines.append('')

        return '\n'.join(lines)

    def to_csv_bundle(self, output_dir: str):
        """Write all summary tables as CSV files."""
        import os
        os.makedirs(output_dir, exist_ok=True)

        self.feature_stability_summary().to_csv(
            os.path.join(output_dir, 'feature_stability.csv'), index=False,
        )
        self.block_type_feature_heatmap().to_csv(
            os.path.join(output_dir, 'block_type_heatmap.csv'), index=False,
        )
        self.optimization_effect_summary().to_csv(
            os.path.join(output_dir, 'optimization_effects.csv'), index=False,
        )
        self.feature_contribution_by_tier().to_csv(
            os.path.join(output_dir, 'feature_by_tier.csv'), index=False,
        )


def _df_to_md(df: pd.DataFrame, float_fmt: str = '.3f') -> str:
    """Convert a DataFrame to a markdown table."""
    cols = list(df.columns)
    lines = []
    lines.append('| ' + ' | '.join(str(c) for c in cols) + ' |')
    lines.append('|' + '|'.join('--------' for _ in cols) + '|')
    for _, row in df.iterrows():
        cells = []
        for c in cols:
            v = row[c]
            if isinstance(v, float):
                if np.isnan(v):
                    cells.append('-')
                else:
                    cells.append(f'{v:{float_fmt}}')
            else:
                cells.append(str(v))
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines)
