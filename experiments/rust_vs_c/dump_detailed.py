#!/fs/ess/PAS1888/bond/bond-proj/.venv/bin/python
"""Dump detailed block-level alignment for selected functions.

Outputs: source code context, disassembly of each block, Hungarian matching
results showing which O0 blocks matched which O2 blocks and why.
"""
import sys
import re
import warnings
import logging
warnings.filterwarnings('ignore')
logging.disable(logging.WARNING)
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor
from rustdiff.fingerprint.function_fingerprint import FunctionFingerprint
from rustdiff.analysis.block_alignment import BlockAlignmentAnalyzer, block_similarity
from rustdiff.analysis.block_case_analysis import classify_block
import numpy as np
from scipy.optimize import linear_sum_assignment

EXP_DIR = Path(__file__).resolve().parent
FUNC_RE = re.compile(r'((?:bc|own|opt|iter|em)_\d{2})')

TARGETS = [
    # bounds_check: 4 (best Rust win, typical win, C win, edge case)
    'bc_07',   # Rust biggest win: convolution, many bounds checks
    'bc_06',   # Rust win: shell sort, nested loop bounds checks
    'bc_09',   # Rust win: bubble sort, simple loop
    'bc_12',   # Rust LOSS: running median uses generic methods -> 1 block O0

    # enum_match: 4 (catastrophic, bad, good, reversal)
    'em_06',   # Rust catastrophic loss: recursive expr constant folding, 2 blocks O0
    'em_20',   # Rust bad loss: recursive expr distribution, 2 blocks O0
    'em_10',   # Rust ~tie: command executor, Vec + loop + match
    'em_17',   # Rust WIN: linearity check, both 1 block but Rust match more stable

    # iterators: 4 (typical loss, bad loss, rare win, moderate)
    'iter_01', # Rust loss: filter+enumerate+collect, 1 block O0
    'iter_16', # Rust bad loss: 3-layer iterator chain, 1:59 ratio
    'iter_14', # Rust WIN: filter_map+fold, complex closures partially inlined
    'iter_12', # Rust loss: scan+windows, 1 block O0

    # option_result: 4 (? operator win, method chain loss, match win, bad loss)
    'opt_04',  # Rust WIN: ? in loop, generates branch blocks
    'opt_09',  # Rust WIN: two ? in while loop
    'opt_06',  # Rust loss: Option method chain .find().map().filter().unwrap_or()
    'opt_20',  # Rust bad loss: split+parse+map_or chain

    # ownership_drop: 4 (index win, method loss, Box recursion, heap heavy)
    'own_01',  # Rust WIN: matrix with explicit indexing + custom Drop
    'own_05',  # Rust WIN: merge vecs with explicit indexing
    'own_03',  # Rust loss: split_whitespace().map().collect()
    'own_04',  # Rust loss: Box linked list, recursive Drop
]


def find_func_addr(loader, base_name):
    for addr, name in loader.get_all_functions():
        m = FUNC_RE.search(name)
        if m and m.group(1) == base_name:
            return addr, name
    return None, None


def dump_block_asm(loader, addr, max_insns=20):
    node = loader.be.get_fast_cfg_node(addr)
    if not node or not node.block:
        return ["    (no block)"]
    lines = []
    insns = list(node.block.capstone.insns)
    for i, insn in enumerate(insns):
        if i >= max_insns:
            lines.append(f"    ... +{len(insns) - max_insns} more instructions")
            break
        lines.append(f"    0x{insn.address:x}: {insn.mnemonic:8s} {insn.op_str}")
    return lines


def analyze_function(base_name, lang, loader_o0, loader_o2, exec_o0, exec_o2, out):
    addr_o0, name_o0 = find_func_addr(loader_o0, base_name)
    addr_o2, name_o2 = find_func_addr(loader_o2, base_name)

    if not addr_o0 or not addr_o2:
        out.append(f"  Function {base_name} not found in {lang} binaries")
        return

    sigs_o0 = exec_o0.execute_function(addr_o0)
    sigs_o2 = exec_o2.execute_function(addr_o2)
    cfg_o0 = loader_o0.get_cfg_for_function(addr_o0)
    cfg_o2 = loader_o2.get_cfg_for_function(addr_o2)

    fp_o0 = FunctionFingerprint(addr_o0, name_o0, sigs_o0, cfg_o0)
    fp_o2 = FunctionFingerprint(addr_o2, name_o2, sigs_o2, cfg_o2)

    # Classify blocks
    types_o0 = {}
    for a in sorted(fp_o0.block_sigs.keys()):
        types_o0[a] = classify_block(fp_o0.block_sigs[a], fp_o0.cfg, a).name

    types_o2 = {}
    for a in sorted(fp_o2.block_sigs.keys()):
        types_o2[a] = classify_block(fp_o2.block_sigs[a], fp_o2.cfg, a).name

    out.append(f"### {lang} `{base_name}` — O0: {fp_o0.num_blocks} blocks, O2: {fp_o2.num_blocks} blocks")
    out.append("")

    # Dump O0 blocks with disassembly
    out.append(f"**O0 blocks** ({fp_o0.num_blocks} total):")
    out.append("")
    out.append("```asm")
    for a in sorted(fp_o0.block_sigs.keys()):
        sig = fp_o0.block_sigs[a]
        bt = types_o0[a]
        callees = ', '.join(sig.callee_names) if sig.callee_names else '(none)'
        out.append(f"; --- Block 0x{a:x} [{bt}] {sig.num_instructions} insns, callees: {callees}")
        for line in dump_block_asm(loader_o0, a, max_insns=12):
            out.append(line)
        out.append("")
    out.append("```")
    out.append("")

    # Dump O2 blocks with disassembly
    out.append(f"**O2 blocks** ({fp_o2.num_blocks} total):")
    out.append("")
    out.append("```asm")
    for a in sorted(fp_o2.block_sigs.keys()):
        sig = fp_o2.block_sigs[a]
        bt = types_o2[a]
        callees = ', '.join(sig.callee_names) if sig.callee_names else '(none)'
        out.append(f"; --- Block 0x{a:x} [{bt}] {sig.num_instructions} insns, callees: {callees}")
        for line in dump_block_asm(loader_o2, a, max_insns=12):
            out.append(line)
        out.append("")
    out.append("```")
    out.append("")

    # Hungarian matching
    addrs1 = sorted(fp_o0.block_sigs.keys())
    addrs2 = sorted(fp_o2.block_sigs.keys())
    n1, n2 = len(addrs1), len(addrs2)

    if n1 == 0 or n2 == 0:
        out.append("*Cannot align: one side has 0 blocks.*")
        out.append("")
        return

    sim_matrix = np.zeros((n1, n2))
    for i, a1 in enumerate(addrs1):
        for j, a2 in enumerate(addrs2):
            sim_matrix[i, j] = block_similarity(fp_o0.block_sigs[a1], fp_o2.block_sigs[a2])

    cost = -sim_matrix
    row_ind, col_ind = linear_sum_assignment(cost)

    matched_rows = set(row_ind)
    matched_cols = set(col_ind)

    mean_sim = np.mean([sim_matrix[r, c] for r, c in zip(row_ind, col_ind)])

    out.append(f"**Hungarian matching result** (mean similarity: {mean_sim:.3f}):")
    out.append("")
    out.append("| O0 Block | Type | O2 Block | Type | Similarity | Verdict |")
    out.append("|----------|------|----------|------|------------|---------|")

    for r, c in sorted(zip(row_ind, col_ind), key=lambda x: -sim_matrix[x[0], x[1]]):
        a1 = addrs1[r]
        a2 = addrs2[c]
        s = sim_matrix[r, c]
        bt1 = types_o0[a1]
        bt2 = types_o2[a2]
        if s >= 0.7:
            verdict = "GOOD"
        elif s >= 0.4:
            verdict = "PARTIAL"
        else:
            verdict = "POOR"
        out.append(f"| `0x{a1:x}` | {bt1} | `0x{a2:x}` | {bt2} | {s:.3f} | {verdict} |")

    # Unmatched
    for i in range(n1):
        if i not in matched_rows:
            a1 = addrs1[i]
            bt1 = types_o0[a1]
            out.append(f"| `0x{a1:x}` | {bt1} | — | — | 0.000 | UNMATCHED (O0 only) |")
    for j in range(n2):
        if j not in matched_cols:
            a2 = addrs2[j]
            bt2 = types_o2[a2]
            out.append(f"| — | — | `0x{a2:x}` | {bt2} | 0.000 | UNMATCHED (O2 only) |")

    out.append("")


def main():
    import sys
    sys.stderr.write("Loading Rust O0...\n")
    rust_o0 = RustBinaryLoader(str(EXP_DIR / 'rust_bench_O0'), load_debug_info=False, include_stdlib=False)
    sys.stderr.write("Loading Rust O2...\n")
    rust_o2 = RustBinaryLoader(str(EXP_DIR / 'rust_bench_O2'), load_debug_info=False, include_stdlib=False)
    sys.stderr.write("Loading C O0...\n")
    c_o0 = RustBinaryLoader(str(EXP_DIR / 'c_bench_O0'), load_debug_info=False, include_stdlib=False)
    sys.stderr.write("Loading C O2...\n")
    c_o2 = RustBinaryLoader(str(EXP_DIR / 'c_bench_O2'), load_debug_info=False, include_stdlib=False)

    rust_exec_o0 = BlockMicroExecutor(rust_o0)
    rust_exec_o2 = BlockMicroExecutor(rust_o2)
    c_exec_o0 = BlockMicroExecutor(c_o0)
    c_exec_o2 = BlockMicroExecutor(c_o2)

    lines = []

    for i, base_name in enumerate(TARGETS):
        sys.stderr.write(f"[{i+1}/{len(TARGETS)}] {base_name}...\n")
        lines.append(f"## Function `{base_name}`")
        lines.append("")

        analyze_function(base_name, "Rust", rust_o0, rust_o2, rust_exec_o0, rust_exec_o2, lines)
        analyze_function(base_name, "C", c_o0, c_o2, c_exec_o0, c_exec_o2, lines)

        lines.append("---")
        lines.append("")

    output_path = EXP_DIR / 'results' / 'detailed_block_analysis.md'
    output_path.write_text('\n'.join(lines))
    sys.stderr.write(f"Written to {output_path}\n")


if __name__ == '__main__':
    main()
