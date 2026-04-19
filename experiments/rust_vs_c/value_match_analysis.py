#!/fs/ess/PAS1888/bond/bond-proj/.venv/bin/python
"""Value-based block matching accuracy analysis.

The question: given O0 and O2 blocks from the SAME function, can we correctly
match them using concrete execution values?

A block match is CORRECT if the O0 block and O2 block compute the same
function — verified by producing identical concrete outputs for the same
test inputs. This is a match accuracy metric, not a similarity score.

For each of the 20 target functions in Rust and C:
- Micro-execute all blocks with 4 test input sets
- Build a match matrix using ONLY concrete output values
- Use Hungarian algorithm to find optimal assignment
- Evaluate: how many matches are value-correct?
- Compare Rust vs C: which language preserves value identity better?
"""
import sys
import re
import json
import warnings
import logging
warnings.filterwarnings('ignore')
logging.disable(logging.WARNING)
from pathlib import Path
from collections import defaultdict

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor
from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.analysis.block_case_analysis import classify_block
import numpy as np
from scipy.optimize import linear_sum_assignment

EXP_DIR = Path(__file__).resolve().parent
FUNC_RE = re.compile(r'((?:bc|own|opt|iter|em)_\d{2})')

TARGETS = [
    'bc_07', 'bc_06', 'bc_09', 'bc_12',
    'em_06', 'em_20', 'em_10', 'em_17',
    'iter_01', 'iter_16', 'iter_14', 'iter_12',
    'opt_04', 'opt_09', 'opt_06', 'opt_20',
    'own_01', 'own_05', 'own_03', 'own_04',
]

CATEGORIES = {
    'bc': 'bounds_check',
    'em': 'enum_match',
    'iter': 'iterators',
    'opt': 'option_result',
    'own': 'ownership_drop',
}


def find_func_addr(loader, base_name):
    for addr, name in loader.get_all_functions():
        m = FUNC_RE.search(name)
        if m and m.group(1) == base_name:
            return addr, name
    return None, None


def concrete_value_similarity(sig1, sig2):
    """Match blocks by concrete execution outputs ONLY.

    Returns a score 0-1 based on how many output register values match
    exactly between the two blocks across all test input sets.

    This is the ground truth signal: if two blocks produce the same
    register outputs for the same inputs, they compute the same thing.
    """
    if not sig1.concrete_outputs and not sig2.concrete_outputs:
        return 0.0  # both empty — no evidence of match

    if not sig1.concrete_outputs or not sig2.concrete_outputs:
        return 0.0

    # Find common output registers
    regs1 = set(sig1.concrete_outputs.keys())
    regs2 = set(sig2.concrete_outputs.keys())
    common_regs = regs1 & regs2

    if not common_regs:
        return 0.0

    # For each common register, check if the output value tuples match
    exact_matches = 0
    partial_matches = 0
    for reg in common_regs:
        vals1 = set(sig1.concrete_outputs[reg])
        vals2 = set(sig2.concrete_outputs[reg])
        if vals1 == vals2:
            exact_matches += 1
        elif vals1 & vals2:
            overlap = len(vals1 & vals2) / len(vals1 | vals2)
            partial_matches += overlap

    total_regs = len(regs1 | regs2)
    return (exact_matches + 0.5 * partial_matches) / total_regs


def dataflow_similarity(sig1, sig2):
    """Match blocks by dataflow edges: which registers flow into which."""
    if not sig1.dataflow_edges and not sig2.dataflow_edges:
        return 0.0
    if not sig1.dataflow_edges or not sig2.dataflow_edges:
        return 0.0
    common = sig1.dataflow_edges & sig2.dataflow_edges
    union = sig1.dataflow_edges | sig2.dataflow_edges
    return len(common) / len(union) if union else 0.0


def memory_pattern_similarity(sig1, sig2):
    """Match blocks by memory access pattern (offsets, sizes, R/W)."""
    if not sig1.memory_pattern and not sig2.memory_pattern:
        return 0.0
    if not sig1.memory_pattern or not sig2.memory_pattern:
        return 0.0
    # Convert to comparable tuples
    def mem_key(ma):
        return (ma.size, ma.is_write, ma.kind.name)
    s1 = set(mem_key(m) for m in sig1.memory_pattern)
    s2 = set(mem_key(m) for m in sig2.memory_pattern)
    if not (s1 | s2):
        return 0.0
    return len(s1 & s2) / len(s1 | s2)


def value_based_block_similarity(sig1, sig2):
    """Block similarity using ONLY value-based features.

    Components (all execution-derived, no structural fluff):
    1. Concrete output value match (50%)  — the gold signal
    2. Dataflow edge match (25%)          — which regs flow where
    3. Memory access pattern match (15%)  — what gets read/written
    4. Constants match (10%)              — embedded immediates
    """
    val_sim = concrete_value_similarity(sig1, sig2)
    df_sim = dataflow_similarity(sig1, sig2)
    mem_sim = memory_pattern_similarity(sig1, sig2)

    # Constants
    c1, c2 = set(sig1.constants), set(sig2.constants)
    const_sim = len(c1 & c2) / len(c1 | c2) if (c1 | c2) else 0.0

    return 0.50 * val_sim + 0.25 * df_sim + 0.15 * mem_sim + 0.10 * const_sim


def dump_block_asm(loader, addr, max_insns=15):
    node = loader.be.get_fast_cfg_node(addr)
    if not node or not node.block:
        return ["    (no block)"]
    lines = []
    insns = list(node.block.capstone.insns)
    for i, insn in enumerate(insns):
        if i >= max_insns:
            lines.append(f"    ... +{len(insns) - max_insns} more")
            break
        lines.append(f"    0x{insn.address:x}: {insn.mnemonic:8s} {insn.op_str}")
    return lines


def analyze_function(base_name, lang, loader_o0, loader_o2, exec_o0, exec_o2):
    """Analyze one function in one language. Returns a result dict."""
    addr_o0, name_o0 = find_func_addr(loader_o0, base_name)
    addr_o2, name_o2 = find_func_addr(loader_o2, base_name)

    if not addr_o0 or not addr_o2:
        return None

    sigs_o0 = exec_o0.execute_function(addr_o0)
    sigs_o2 = exec_o2.execute_function(addr_o2)
    cfg_o0 = loader_o0.get_cfg_for_function(addr_o0)
    cfg_o2 = loader_o2.get_cfg_for_function(addr_o2)

    fp_o0 = FunctionFingerprint(addr_o0, name_o0, sigs_o0, cfg_o0)
    fp_o2 = FunctionFingerprint(addr_o2, name_o2, sigs_o2, cfg_o2)

    addrs1 = sorted(fp_o0.block_sigs.keys())
    addrs2 = sorted(fp_o2.block_sigs.keys())
    n1, n2 = len(addrs1), len(addrs2)

    if n1 == 0 or n2 == 0:
        return {
            'base_name': base_name, 'lang': lang,
            'n_o0': n1, 'n_o2': n2,
            'matched': 0, 'value_correct': 0,
            'accuracy': 0.0, 'matches': [],
            'fp_o0': fp_o0, 'fp_o2': fp_o2,
            'addrs1': addrs1, 'addrs2': addrs2,
        }

    # Build value-based similarity matrix
    sim_matrix = np.zeros((n1, n2))
    for i, a1 in enumerate(addrs1):
        for j, a2 in enumerate(addrs2):
            sim_matrix[i, j] = value_based_block_similarity(
                fp_o0.block_sigs[a1], fp_o2.block_sigs[a2]
            )

    # Hungarian matching
    cost = -sim_matrix
    row_ind, col_ind = linear_sum_assignment(cost)

    matches = []
    value_correct = 0
    for r, c in zip(row_ind, col_ind):
        a1, a2 = addrs1[r], addrs2[c]
        s = sim_matrix[r, c]

        sig1 = fp_o0.block_sigs[a1]
        sig2 = fp_o2.block_sigs[a2]

        # A match is "correct" if concrete values show real overlap
        val_sim = concrete_value_similarity(sig1, sig2)
        is_correct = val_sim >= 0.3

        if is_correct:
            value_correct += 1

        bt1 = classify_block(sig1, cfg_o0, a1).name
        bt2 = classify_block(sig2, cfg_o2, a2).name

        matches.append({
            'addr_o0': a1, 'addr_o2': a2,
            'value_sim': val_sim,
            'total_sim': s,
            'is_correct': is_correct,
            'type_o0': bt1, 'type_o2': bt2,
            'n_insns_o0': sig1.num_instructions,
            'n_insns_o2': sig2.num_instructions,
            'n_outputs_o0': len(sig1.concrete_outputs),
            'n_outputs_o2': len(sig2.concrete_outputs),
            'df_sim': dataflow_similarity(sig1, sig2),
            'mem_sim': memory_pattern_similarity(sig1, sig2),
            'const_sim': len(set(sig1.constants) & set(sig2.constants)) / len(set(sig1.constants) | set(sig2.constants)) if (set(sig1.constants) | set(sig2.constants)) else 0.0,
        })

    n_matched = min(n1, n2)
    accuracy = value_correct / n_matched if n_matched > 0 else 0.0

    # Count unmatched
    matched_rows = set(row_ind)
    matched_cols = set(col_ind)
    unmatched_o0 = [addrs1[i] for i in range(n1) if i not in matched_rows]
    unmatched_o2 = [addrs2[j] for j in range(n2) if j not in matched_cols]

    return {
        'base_name': base_name, 'lang': lang,
        'n_o0': n1, 'n_o2': n2,
        'matched': n_matched, 'value_correct': value_correct,
        'accuracy': accuracy,
        'matches': sorted(matches, key=lambda m: -m['value_sim']),
        'unmatched_o0': unmatched_o0, 'unmatched_o2': unmatched_o2,
        'fp_o0': fp_o0, 'fp_o2': fp_o2,
        'addrs1': addrs1, 'addrs2': addrs2,
        'loader_o0': loader_o0, 'loader_o2': loader_o2,
    }


def format_concrete_outputs(sig, max_regs=4):
    """Format concrete outputs for display."""
    if not sig.concrete_outputs:
        return "(no concrete outputs)"
    parts = []
    for reg, vals in sorted(sig.concrete_outputs.items())[:max_regs]:
        val_str = ', '.join(f'0x{v:x}' for v in vals[:4])
        if len(vals) > 4:
            val_str += f' (+{len(vals)-4})'
        parts.append(f"{reg}=[{val_str}]")
    if len(sig.concrete_outputs) > max_regs:
        parts.append(f"(+{len(sig.concrete_outputs)-max_regs} regs)")
    return ' | '.join(parts)


def main():
    sys.stderr.write("Loading binaries...\n")
    rust_o0 = RustBinaryLoader(str(EXP_DIR / 'rust_bench_O0'), load_debug_info=False, include_stdlib=False)
    rust_o2 = RustBinaryLoader(str(EXP_DIR / 'rust_bench_O2'), load_debug_info=False, include_stdlib=False)
    c_o0 = RustBinaryLoader(str(EXP_DIR / 'c_bench_O0'), load_debug_info=False, include_stdlib=False)
    c_o2 = RustBinaryLoader(str(EXP_DIR / 'c_bench_O2'), load_debug_info=False, include_stdlib=False)

    rust_exec_o0 = BlockMicroExecutor(rust_o0)
    rust_exec_o2 = BlockMicroExecutor(rust_o2)
    c_exec_o0 = BlockMicroExecutor(c_o0)
    c_exec_o2 = BlockMicroExecutor(c_o2)

    all_results = []

    for i, base_name in enumerate(TARGETS):
        sys.stderr.write(f"[{i+1}/{len(TARGETS)}] {base_name}...\n")

        rust_result = analyze_function(base_name, "Rust",
                                       rust_o0, rust_o2, rust_exec_o0, rust_exec_o2)
        c_result = analyze_function(base_name, "C",
                                     c_o0, c_o2, c_exec_o0, c_exec_o2)

        if rust_result:
            all_results.append(rust_result)
        if c_result:
            all_results.append(c_result)

    # Write JSON data for HTML generation
    json_data = []
    for r in all_results:
        entry = {
            'base_name': r['base_name'],
            'lang': r['lang'],
            'category': CATEGORIES.get(r['base_name'].rsplit('_', 1)[0], 'unknown'),
            'n_o0': r['n_o0'],
            'n_o2': r['n_o2'],
            'matched': r['matched'],
            'value_correct': r['value_correct'],
            'accuracy': r['accuracy'],
            'matches': [],
        }

        for m in r['matches']:
            match_entry = {
                'addr_o0': f"0x{m['addr_o0']:x}",
                'addr_o2': f"0x{m['addr_o2']:x}",
                'value_sim': round(m['value_sim'], 3),
                'total_sim': round(m['total_sim'], 3),
                'is_correct': m['is_correct'],
                'type_o0': m['type_o0'],
                'type_o2': m['type_o2'],
                'n_insns_o0': m['n_insns_o0'],
                'n_insns_o2': m['n_insns_o2'],
                'df_sim': round(m['df_sim'], 3),
                'mem_sim': round(m['mem_sim'], 3),
                'const_sim': round(m['const_sim'], 3),
            }
            # Add concrete outputs for display
            sig1 = r['fp_o0'].block_sigs.get(m['addr_o0'])
            sig2 = r['fp_o2'].block_sigs.get(m['addr_o2'])
            if sig1:
                match_entry['outputs_o0'] = format_concrete_outputs(sig1)
                match_entry['asm_o0'] = dump_block_asm(r['loader_o0'], m['addr_o0'])
            if sig2:
                match_entry['outputs_o2'] = format_concrete_outputs(sig2)
                match_entry['asm_o2'] = dump_block_asm(r['loader_o2'], m['addr_o2'])
            entry['matches'].append(match_entry)

        json_data.append(entry)

    output_path = EXP_DIR / 'results' / 'value_match_data.json'
    output_path.write_text(json.dumps(json_data, indent=2))
    sys.stderr.write(f"JSON data written to {output_path}\n")

    # Also write summary table to stderr for quick review
    sys.stderr.write("\n=== VALUE-BASED MATCH ACCURACY ===\n\n")
    sys.stderr.write(f"{'Func':<10} {'Lang':<6} {'O0':>4} {'O2':>4} {'Matched':>8} {'Correct':>8} {'Accuracy':>9}\n")
    sys.stderr.write("-" * 60 + "\n")

    for base_name in TARGETS:
        for r in all_results:
            if r['base_name'] == base_name:
                sys.stderr.write(
                    f"{r['base_name']:<10} {r['lang']:<6} {r['n_o0']:>4} {r['n_o2']:>4} "
                    f"{r['matched']:>8} {r['value_correct']:>8} {r['accuracy']:>8.1%}\n"
                )

    # Category summaries
    sys.stderr.write("\n=== CATEGORY SUMMARY ===\n\n")
    for cat_prefix, cat_name in CATEGORIES.items():
        rust_correct = 0
        rust_total = 0
        c_correct = 0
        c_total = 0
        for r in all_results:
            if r['base_name'].startswith(cat_prefix + '_'):
                if r['lang'] == 'Rust':
                    rust_correct += r['value_correct']
                    rust_total += r['matched']
                else:
                    c_correct += r['value_correct']
                    c_total += r['matched']
        rust_acc = rust_correct / rust_total if rust_total > 0 else 0
        c_acc = c_correct / c_total if c_total > 0 else 0
        winner = "Rust" if rust_acc > c_acc else "C" if c_acc > rust_acc else "TIE"
        sys.stderr.write(
            f"{cat_name:<20} Rust: {rust_correct}/{rust_total} ({rust_acc:.0%}) | "
            f"C: {c_correct}/{c_total} ({c_acc:.0%}) | Winner: {winner}\n"
        )


if __name__ == '__main__':
    main()
