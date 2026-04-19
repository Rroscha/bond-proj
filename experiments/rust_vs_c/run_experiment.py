#!/fs/ess/PAS1888/bond/bond-proj/.venv/bin/python
"""Rust vs C: Binary Matching Experiment

Compares function matching accuracy between Rust and C binaries compiled
at O0 and O2. The hypothesis: Rust-specific language features (bounds checks,
Option/Result discriminants, Drop glue, iterator state machines, rich enums)
act as "anchor blocks" that survive optimization and improve matching accuracy.

Experiment structure:
  - 100 functions, 5 categories x 20 functions each
  - Rust O0 <-> Rust O2: matching with Rust safety features
  - C O0 <-> C O2: matching on equivalent algorithms without safety features
  - Compare: overall accuracy and per-category accuracy
"""

import json
import logging
import os
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from pathlib import Path

import numpy as np

# Setup project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor
from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.analysis.rust_qualitative import (
    RustQualitativeAnalyzer,
    compute_per_feature_similarity,
    classify_stability,
)
from rustdiff.analysis.block_case_analysis import classify_block, BlockType

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)-8s %(name)s: %(message)s',
)
logger = logging.getLogger('rust_vs_c')

# Experiment directory
EXP_DIR = Path(__file__).resolve().parent
RUST_O0 = EXP_DIR / 'rust_bench_O0'
RUST_O2 = EXP_DIR / 'rust_bench_O2'
C_O0 = EXP_DIR / 'c_bench_O0'
C_O2 = EXP_DIR / 'c_bench_O2'

# Function categories
CATEGORIES = {
    'bounds_check': 'bc_',
    'ownership_drop': 'own_',
    'option_result': 'opt_',
    'iterators': 'iter_',
    'enum_match': 'em_',
}


FUNC_NAME_RE = re.compile(r'((?:bc|own|opt|iter|em)_\d{2})')


def categorize_function(name: str) -> str:
    """Map a function name to its category."""
    m = FUNC_NAME_RE.search(name)
    if not m:
        return 'unknown'
    base = m.group(1)
    for cat, prefix in CATEGORIES.items():
        if base.startswith(prefix):
            return cat
    return 'unknown'


def get_function_base_name(name: str) -> str:
    """Extract base function name like 'bc_01' from demangled name.

    Rust: "rust_bench::bc_01" -> "bc_01"
    C: "bc_01" -> "bc_01"
    """
    m = FUNC_NAME_RE.search(name)
    return m.group(1) if m else name


@dataclass
class FunctionMatchResult:
    """Result of matching a single O0/O2 function pair."""
    func_name: str
    category: str
    num_blocks_o0: int
    num_blocks_o2: int
    mean_block_similarity: float
    per_feature_sims: dict = field(default_factory=dict)
    block_type_counts_o0: dict = field(default_factory=dict)
    block_type_counts_o2: dict = field(default_factory=dict)


def build_groundtruth_pairs(loader_o0, loader_o2, is_rust: bool):
    """Build groundtruth function pairs by matching on base function names."""
    funcs_o0 = loader_o0.get_all_functions()
    funcs_o2 = loader_o2.get_all_functions()

    name_to_addr_o0 = {}
    name_to_addr_o2 = {}

    for addr, name in funcs_o0:
        base = get_function_base_name(name)
        if FUNC_NAME_RE.fullmatch(base):
            name_to_addr_o0[base] = (addr, name)

    for addr, name in funcs_o2:
        base = get_function_base_name(name)
        if FUNC_NAME_RE.fullmatch(base):
            name_to_addr_o2[base] = (addr, name)

    pairs = []
    for base in sorted(name_to_addr_o0.keys()):
        if base in name_to_addr_o2:
            addr_o0, full_name = name_to_addr_o0[base]
            addr_o2, _ = name_to_addr_o2[base]
            pairs.append((addr_o0, addr_o2, full_name))

    return pairs


def _analyze_batch(args):
    """Analyze a batch of function pairs sharing the same binary load.

    Each worker loads binaries once, then iterates through its assigned pairs.
    """
    bin_o0_path, bin_o2_path, batch = args
    import sys, warnings, logging as _logging
    warnings.filterwarnings('ignore')
    _logging.disable(_logging.WARNING)
    sys.path.insert(0, str(PROJECT_ROOT))

    from rustdiff.loader import RustBinaryLoader
    from rustdiff.micro_exec.block_executor import BlockMicroExecutor
    from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
    from rustdiff.analysis.rust_qualitative import RustQualitativeAnalyzer, compute_per_feature_similarity
    from rustdiff.analysis.block_case_analysis import classify_block

    loader_o0 = RustBinaryLoader(bin_o0_path, load_debug_info=False, include_stdlib=False)
    loader_o2 = RustBinaryLoader(bin_o2_path, load_debug_info=False, include_stdlib=False)
    exec_o0 = BlockMicroExecutor(loader_o0)
    exec_o2 = BlockMicroExecutor(loader_o2)
    analyzer = RustQualitativeAnalyzer(min_blocks=1)

    results = []
    for addr_o0, addr_o2, func_name in batch:
        try:
            sigs_o0 = exec_o0.execute_function(addr_o0)
            sigs_o2 = exec_o2.execute_function(addr_o2)
            cfg_o0 = loader_o0.get_cfg_for_function(addr_o0)
            cfg_o2 = loader_o2.get_cfg_for_function(addr_o2)

            fp_o0 = FunctionFingerprint(addr_o0, func_name, sigs_o0, cfg_o0)
            fp_o2 = FunctionFingerprint(addr_o2, func_name, sigs_o2, cfg_o2)

            result = analyzer.analyze_single_pair(fp_o0, fp_o2)

            feat_accum = defaultdict(list)
            for bp in result.block_pairs:
                if bp.status == 'matched' and bp.per_feature_sim:
                    for feat, sim in bp.per_feature_sim.items():
                        if not np.isnan(sim):
                            feat_accum[feat].append(sim)

            per_feat_means = {
                feat: float(np.mean(sims)) for feat, sims in feat_accum.items()
            }

            btc_o0 = defaultdict(int)
            btc_o2 = defaultdict(int)
            for addr, sig in fp_o0.block_sigs.items():
                bt = classify_block(sig, fp_o0.cfg, addr)
                btc_o0[bt.name] += 1
            for addr, sig in fp_o2.block_sigs.items():
                bt = classify_block(sig, fp_o2.cfg, addr)
                btc_o2[bt.name] += 1

            results.append(FunctionMatchResult(
                func_name=func_name,
                category=categorize_function(func_name),
                num_blocks_o0=fp_o0.num_blocks,
                num_blocks_o2=fp_o2.num_blocks,
                mean_block_similarity=result.mean_block_similarity,
                per_feature_sims=per_feat_means,
                block_type_counts_o0=dict(btc_o0),
                block_type_counts_o2=dict(btc_o2),
            ))
        except Exception as e:
            results.append(FunctionMatchResult(
                func_name=func_name,
                category=categorize_function(func_name),
                num_blocks_o0=0, num_blocks_o2=0,
                mean_block_similarity=0.0,
            ))

    return results


def run_analysis(bin_o0_path, bin_o2_path, label, is_rust, max_workers=4):
    """Run full analysis for one language (Rust or C)."""
    logger.info("=" * 60)
    logger.info("Analyzing: %s", label)
    logger.info("  O0: %s", bin_o0_path)
    logger.info("  O2: %s", bin_o2_path)
    logger.info("=" * 60)

    logger.info("Loading binaries for groundtruth extraction...")
    loader_o0 = RustBinaryLoader(str(bin_o0_path), load_debug_info=False, include_stdlib=False)
    loader_o2 = RustBinaryLoader(str(bin_o2_path), load_debug_info=False, include_stdlib=False)

    pairs = build_groundtruth_pairs(loader_o0, loader_o2, is_rust)
    logger.info("Found %d groundtruth pairs", len(pairs))

    for addr_o0, addr_o2, name in pairs[:5]:
        logger.info("  %s: O0=0x%x, O2=0x%x", name, addr_o0, addr_o2)
    if len(pairs) > 5:
        logger.info("  ... and %d more", len(pairs) - 5)

    del loader_o0, loader_o2

    # Split pairs into batches — each worker loads binaries once then processes its batch
    batch_size = max(1, len(pairs) // max_workers)
    batches = []
    for i in range(0, len(pairs), batch_size):
        batch = pairs[i:i + batch_size]
        batches.append((str(bin_o0_path), str(bin_o2_path), batch))

    logger.info("Dispatching %d batches to %d workers (%d funcs/batch)...",
                len(batches), max_workers, batch_size)
    t0 = time.time()

    results = []
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(_analyze_batch, b): i for i, b in enumerate(batches)}
        for future in as_completed(futures):
            batch_idx = futures[future]
            try:
                batch_results = future.result(timeout=600)
                results.extend(batch_results)
                logger.info(
                    "  [%s] Batch %d done: %d functions (%.1fs elapsed)",
                    label, batch_idx, len(batch_results), time.time() - t0
                )
            except Exception as e:
                logger.error("  Batch %d failed: %s", batch_idx, e)

    elapsed = time.time() - t0
    logger.info("  %s: Analyzed %d functions in %.1fs", label, len(results), elapsed)

    return results


def generate_report(rust_results, c_results, output_dir):
    """Generate comparison report."""
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# Rust vs C: Binary Matching Experiment Report")
    lines.append("")

    # --- Overall Summary ---
    lines.append("## 1. Overall Comparison")
    lines.append("")

    def summarize(results, label):
        if not results:
            return f"**{label}**: No results"
        sims = [r.mean_block_similarity for r in results if r.num_blocks_o0 > 0]
        total_blocks_o0 = sum(r.num_blocks_o0 for r in results)
        total_blocks_o2 = sum(r.num_blocks_o2 for r in results)

        # Count anchor block types
        anchor_count_o0 = 0
        anchor_count_o2 = 0
        for r in results:
            for bt in ('BOUNDS_CHECK', 'PANIC_PATH', 'DROP_GLUE'):
                anchor_count_o0 += r.block_type_counts_o0.get(bt, 0)
                anchor_count_o2 += r.block_type_counts_o2.get(bt, 0)

        return (
            f"| {label} | {len(sims)} | {np.mean(sims):.4f} | {np.median(sims):.4f} | "
            f"{np.std(sims):.4f} | {total_blocks_o0} | {total_blocks_o2} | {anchor_count_o0} | {anchor_count_o2} |"
        )

    lines.append("| Language | Functions | Mean Sim | Median Sim | Std | Blocks O0 | Blocks O2 | Anchor O0 | Anchor O2 |")
    lines.append("|----------|-----------|----------|------------|-----|-----------|-----------|-----------|-----------|")
    lines.append(summarize(rust_results, "Rust"))
    lines.append(summarize(c_results, "C"))
    lines.append("")

    # Delta
    rust_sims = [r.mean_block_similarity for r in rust_results if r.num_blocks_o0 > 0]
    c_sims = [r.mean_block_similarity for r in c_results if r.num_blocks_o0 > 0]
    if rust_sims and c_sims:
        delta = np.mean(rust_sims) - np.mean(c_sims)
        lines.append(f"**Delta (Rust - C): {delta:+.4f}** ({'Rust better' if delta > 0 else 'C better'})")
        lines.append("")

    # --- Per-Category Comparison ---
    lines.append("## 2. Per-Category Comparison")
    lines.append("")
    lines.append("| Category | Rust Mean Sim | C Mean Sim | Delta | Rust Anchor Blocks | C Anchor Blocks |")
    lines.append("|----------|---------------|------------|-------|--------------------|-----------------|")

    for cat_name, prefix in CATEGORIES.items():
        r_cat = [r for r in rust_results if r.category == cat_name and r.num_blocks_o0 > 0]
        c_cat = [r for r in c_results if r.category == cat_name and r.num_blocks_o0 > 0]

        r_sim = np.mean([r.mean_block_similarity for r in r_cat]) if r_cat else 0
        c_sim = np.mean([r.mean_block_similarity for r in c_cat]) if c_cat else 0
        delta = r_sim - c_sim

        # Count anchor blocks
        r_anchors = sum(
            r.block_type_counts_o0.get('BOUNDS_CHECK', 0)
            + r.block_type_counts_o0.get('PANIC_PATH', 0)
            + r.block_type_counts_o0.get('DROP_GLUE', 0)
            for r in r_cat
        )
        c_anchors = sum(
            r.block_type_counts_o0.get('BOUNDS_CHECK', 0)
            + r.block_type_counts_o0.get('PANIC_PATH', 0)
            + r.block_type_counts_o0.get('DROP_GLUE', 0)
            for r in c_cat
        )

        lines.append(
            f"| {cat_name} | {r_sim:.4f} | {c_sim:.4f} | {delta:+.4f} | {r_anchors} | {c_anchors} |"
        )

    lines.append("")

    # --- Per-Feature Comparison ---
    lines.append("## 3. Per-Feature Comparison (Mean Similarity)")
    lines.append("")

    features = ['opcodes', 'constants', 'concrete_values', 'dataflow_edges',
                'instruction_count', 'callee_names', 'string_refs']

    lines.append("| Feature | Rust Mean | C Mean | Delta |")
    lines.append("|---------|-----------|--------|-------|")
    for feat in features:
        r_vals = [r.per_feature_sims.get(feat, float('nan')) for r in rust_results
                  if feat in r.per_feature_sims and not np.isnan(r.per_feature_sims.get(feat, float('nan')))]
        c_vals = [r.per_feature_sims.get(feat, float('nan')) for r in c_results
                  if feat in r.per_feature_sims and not np.isnan(r.per_feature_sims.get(feat, float('nan')))]
        r_mean = np.mean(r_vals) if r_vals else float('nan')
        c_mean = np.mean(c_vals) if c_vals else float('nan')
        delta = r_mean - c_mean if not (np.isnan(r_mean) or np.isnan(c_mean)) else float('nan')
        r_str = f"{r_mean:.4f}" if not np.isnan(r_mean) else "-"
        c_str = f"{c_mean:.4f}" if not np.isnan(c_mean) else "-"
        d_str = f"{delta:+.4f}" if not np.isnan(delta) else "-"
        lines.append(f"| {feat} | {r_str} | {c_str} | {d_str} |")
    lines.append("")

    # --- Block Type Distribution ---
    lines.append("## 4. Block Type Distribution")
    lines.append("")
    lines.append("### Rust (O0)")
    all_bt = set()
    rust_bt_o0 = defaultdict(int)
    rust_bt_o2 = defaultdict(int)
    for r in rust_results:
        for bt, cnt in r.block_type_counts_o0.items():
            rust_bt_o0[bt] += cnt
            all_bt.add(bt)
        for bt, cnt in r.block_type_counts_o2.items():
            rust_bt_o2[bt] += cnt
            all_bt.add(bt)

    c_bt_o0 = defaultdict(int)
    c_bt_o2 = defaultdict(int)
    for r in c_results:
        for bt, cnt in r.block_type_counts_o0.items():
            c_bt_o0[bt] += cnt
            all_bt.add(bt)
        for bt, cnt in r.block_type_counts_o2.items():
            c_bt_o2[bt] += cnt
            all_bt.add(bt)

    lines.append("| Block Type | Rust O0 | Rust O2 | C O0 | C O2 |")
    lines.append("|------------|---------|---------|------|------|")
    for bt in sorted(all_bt):
        lines.append(
            f"| {bt} | {rust_bt_o0[bt]} | {rust_bt_o2[bt]} | {c_bt_o0[bt]} | {c_bt_o2[bt]} |"
        )
    total_r0 = sum(rust_bt_o0.values())
    total_r2 = sum(rust_bt_o2.values())
    total_c0 = sum(c_bt_o0.values())
    total_c2 = sum(c_bt_o2.values())
    lines.append(f"| **TOTAL** | **{total_r0}** | **{total_r2}** | **{total_c0}** | **{total_c2}** |")
    lines.append("")

    # Anchor block percentage
    rust_anchor_o0 = rust_bt_o0.get('BOUNDS_CHECK', 0) + rust_bt_o0.get('PANIC_PATH', 0) + rust_bt_o0.get('DROP_GLUE', 0)
    c_anchor_o0 = c_bt_o0.get('BOUNDS_CHECK', 0) + c_bt_o0.get('PANIC_PATH', 0) + c_bt_o0.get('DROP_GLUE', 0)
    r_pct = rust_anchor_o0 / total_r0 * 100 if total_r0 > 0 else 0
    c_pct = c_anchor_o0 / total_c0 * 100 if total_c0 > 0 else 0
    lines.append(f"**Anchor block proportion:** Rust {r_pct:.1f}% ({rust_anchor_o0}/{total_r0}), C {c_pct:.1f}% ({c_anchor_o0}/{total_c0})")
    lines.append("")

    # --- Per-Function Details ---
    lines.append("## 5. Per-Function Details")
    lines.append("")
    lines.append("| Function | Category | Rust Sim | C Sim | Delta | Rust Blk O0 | Rust Blk O2 | C Blk O0 | C Blk O2 |")
    lines.append("|----------|----------|----------|-------|-------|-------------|-------------|----------|----------|")

    # Build lookup by base name
    rust_by_name = {}
    for r in rust_results:
        base = get_function_base_name(r.func_name)
        rust_by_name[base] = r

    c_by_name = {}
    for r in c_results:
        base = get_function_base_name(r.func_name)
        c_by_name[base] = r

    all_names = sorted(set(rust_by_name.keys()) | set(c_by_name.keys()))
    for name in all_names:
        rr = rust_by_name.get(name)
        cr = c_by_name.get(name)
        cat = categorize_function(name)
        r_sim = rr.mean_block_similarity if rr and rr.num_blocks_o0 > 0 else float('nan')
        c_sim = cr.mean_block_similarity if cr and cr.num_blocks_o0 > 0 else float('nan')
        delta = r_sim - c_sim if not (np.isnan(r_sim) or np.isnan(c_sim)) else float('nan')

        r_str = f"{r_sim:.3f}" if not np.isnan(r_sim) else "-"
        c_str = f"{c_sim:.3f}" if not np.isnan(c_sim) else "-"
        d_str = f"{delta:+.3f}" if not np.isnan(delta) else "-"

        r_b0 = rr.num_blocks_o0 if rr else 0
        r_b2 = rr.num_blocks_o2 if rr else 0
        c_b0 = cr.num_blocks_o0 if cr else 0
        c_b2 = cr.num_blocks_o2 if cr else 0

        lines.append(f"| {name} | {cat} | {r_str} | {c_str} | {d_str} | {r_b0} | {r_b2} | {c_b0} | {c_b2} |")

    lines.append("")

    # Write report
    report_text = "\n".join(lines)
    report_path = output_dir / "report.md"
    report_path.write_text(report_text)
    logger.info("Report written to %s", report_path)

    # Also write raw JSON data
    json_data = {
        'rust': [asdict(r) for r in rust_results],
        'c': [asdict(r) for r in c_results],
    }
    json_path = output_dir / "raw_results.json"
    json_path.write_text(json.dumps(json_data, indent=2, default=str))
    logger.info("Raw data written to %s", json_path)

    return report_text


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Rust vs C matching experiment')
    parser.add_argument('--workers', type=int, default=4,
                        help='Number of parallel workers')
    parser.add_argument('--output', type=str,
                        default=str(EXP_DIR / 'results'),
                        help='Output directory for results')
    args = parser.parse_args()

    # Verify binaries exist
    for p in [RUST_O0, RUST_O2, C_O0, C_O2]:
        if not p.exists():
            logger.error("Binary not found: %s", p)
            sys.exit(1)

    # Run Rust analysis
    rust_results = run_analysis(
        RUST_O0, RUST_O2, "Rust", is_rust=True, max_workers=args.workers
    )

    # Run C analysis
    c_results = run_analysis(
        C_O0, C_O2, "C", is_rust=False, max_workers=args.workers
    )

    # Generate report
    report = generate_report(rust_results, c_results, args.output)
    print("\n" + report)


if __name__ == '__main__':
    main()
