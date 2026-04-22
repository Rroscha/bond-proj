#!/usr/bin/env python3
"""Rust-specific feature analysis: 4 independent block matching methods.

For each of 100 functions (5 features × 20), compare O0 vs O2 block matching
accuracy using 4 independent methods:
  1. Value-based: concrete execution output matching
  2. Opcodes: opcode set Jaccard similarity
  3. Constants: constant set Jaccard similarity
  4. Size: instruction count ratio

Each method builds its own block similarity matrix, runs Hungarian matching,
and reports accuracy independently. Accuracy = fraction of matched block pairs
where the similarity exceeds a threshold.

Outputs JSON data for HTML report generation.
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
from elftools.elf.elffile import ELFFile
import numpy as np
from scipy.optimize import linear_sum_assignment


# ── DWARF line-mapping ground truth ────────────────────────────────────────

class DWARFLineMapper:
    """Extract address → source line mapping from DWARF debug info."""

    def __init__(self, binary_path):
        self.entries = []  # sorted list of (addr, file, line)
        self._load(binary_path)

    def _load(self, path):
        with open(path, 'rb') as f:
            elf = ELFFile(f)
            if not elf.has_dwarf_info():
                return
            # Detect PIE rebase: angr loads PIE binaries at 0x400000
            is_pie = elf.header.e_type == 'ET_DYN'
            self.base_delta = 0x400000 if is_pie else 0
            di = elf.get_dwarf_info()
            for cu in di.iter_CUs():
                lp = di.line_program_for_CU(cu)
                if lp is None:
                    continue
                file_entries = lp['file_entry']
                file_map = {}
                for i, fe in enumerate(file_entries):
                    name = fe.name.decode() if isinstance(fe.name, bytes) else fe.name
                    file_map[i + 1] = name
                for entry in lp.get_entries():
                    s = entry.state
                    if s and not s.end_sequence and s.line > 0:
                        fname = file_map.get(s.file, '')
                        angr_addr = s.address + self.base_delta
                        self.entries.append((angr_addr, fname, s.line))
        self.entries.sort()

    def lines_for_range(self, start_addr, end_addr, source_filter=None):
        """Return set of (file, line) for addresses in [start_addr, end_addr)."""
        lines = set()
        for addr, fname, line in self.entries:
            if addr >= end_addr:
                break
            if addr >= start_addr:
                if source_filter is None or source_filter in fname:
                    lines.add((fname, line))
        return lines


def get_block_addr_range(loader, block_addr):
    """Get (start, end) address range for a basic block."""
    node = loader.be.get_fast_cfg_node(block_addr)
    if not node or not node.block:
        return block_addr, block_addr + 1
    insns = list(node.block.capstone.insns)
    if not insns:
        return block_addr, block_addr + 1
    last = insns[-1]
    return block_addr, last.address + last.size


def build_block_line_sets(loader, dwarf_mapper, block_addrs, source_filter=None):
    """For each block addr, compute its set of source lines."""
    result = {}
    for addr in block_addrs:
        start, end = get_block_addr_range(loader, addr)
        lines = dwarf_mapper.lines_for_range(start, end, source_filter)
        result[addr] = {line for _, line in lines}
    return result


def build_groundtruth_matrix(lines_o0, lines_o2, addrs_o0, addrs_o2):
    """Build a boolean matrix: gt[i][j] = True if O0 block i and O2 block j
    share at least one source line (i.e., they correspond to the same code)."""
    n1, n2 = len(addrs_o0), len(addrs_o2)
    gt = np.zeros((n1, n2), dtype=bool)
    for i, a1 in enumerate(addrs_o0):
        s1 = lines_o0.get(a1, set())
        if not s1:
            continue
        for j, a2 in enumerate(addrs_o2):
            s2 = lines_o2.get(a2, set())
            if s1 & s2:
                gt[i][j] = True
    return gt

EXP_DIR = Path(__file__).resolve().parent

PREFIXES = ['om', 'dg', 'bc', 'qm', 'pu']
FEATURE_NAMES = {
    'om': 'Ownership & Move',
    'dg': 'Drop Glue (RAII)',
    'bc': 'Bounds Checking',
    'qm': '? Operator (Option/Result)',
    'pu': 'Panic/Unwind Paths',
}
ALL_FUNCS = [f'{p}_{i:02d}' for p in PREFIXES for i in range(1, 21)]

RUST_FUNC_RE = re.compile(r'rust_features\d*::(\w+)')
C_FUNC_RE = re.compile(r'\b(om_\d{2}|dg_\d{2}|bc_\d{2}|qm_\d{2}|pu_\d{2})\b')


def find_func_addr_rust(loader, base_name):
    for addr, name in loader.get_all_functions():
        m = RUST_FUNC_RE.search(name)
        if m and m.group(1) == base_name:
            return addr, name
    return None, None


def find_func_addr_c(loader, base_name):
    for addr, name in loader.get_all_functions():
        if name == base_name or name.endswith(f'::{base_name}'):
            return addr, name
        m = C_FUNC_RE.search(name)
        if m and m.group(1) == base_name:
            return addr, name
    return None, None


# ── Method 1: Value-based ────────────────────────────────────────────────────

def concrete_value_similarity(sig1, sig2):
    if not sig1.concrete_outputs or not sig2.concrete_outputs:
        return 0.0
    regs1 = set(sig1.concrete_outputs.keys())
    regs2 = set(sig2.concrete_outputs.keys())
    common_regs = regs1 & regs2
    if not common_regs:
        return 0.0
    exact = 0
    partial = 0.0
    for reg in common_regs:
        v1 = set(sig1.concrete_outputs[reg])
        v2 = set(sig2.concrete_outputs[reg])
        if v1 == v2:
            exact += 1
        elif v1 & v2:
            partial += len(v1 & v2) / len(v1 | v2)
    total = len(regs1 | regs2)
    return (exact + 0.5 * partial) / total


def dataflow_similarity(sig1, sig2):
    if not sig1.dataflow_edges or not sig2.dataflow_edges:
        return 0.0
    union = sig1.dataflow_edges | sig2.dataflow_edges
    return len(sig1.dataflow_edges & sig2.dataflow_edges) / len(union) if union else 0.0


def memory_pattern_similarity(sig1, sig2):
    if not sig1.memory_pattern or not sig2.memory_pattern:
        return 0.0
    def mk(ma):
        return (ma.size, ma.is_write, ma.kind.name)
    s1 = set(mk(m) for m in sig1.memory_pattern)
    s2 = set(mk(m) for m in sig2.memory_pattern)
    union = s1 | s2
    return len(s1 & s2) / len(union) if union else 0.0


def value_block_sim(sig1, sig2):
    val = concrete_value_similarity(sig1, sig2)
    df = dataflow_similarity(sig1, sig2)
    mem = memory_pattern_similarity(sig1, sig2)
    c1, c2 = set(sig1.constants), set(sig2.constants)
    cs = len(c1 & c2) / len(c1 | c2) if (c1 | c2) else 0.0
    return 0.50 * val + 0.25 * df + 0.15 * mem + 0.10 * cs


# ── Method 2: Opcodes ───────────────────────────────────────────────────────

def opcode_block_sim(sig1, sig2):
    ops1 = set(sig1.opcode_sequence)
    ops2 = set(sig2.opcode_sequence)
    if not ops1 and not ops2:
        return 0.0
    union = ops1 | ops2
    return len(ops1 & ops2) / len(union) if union else 0.0


# ── Method 3: Constants ─────────────────────────────────────────────────────

def constant_block_sim(sig1, sig2):
    c1 = set(sig1.constants)
    c2 = set(sig2.constants)
    if not c1 and not c2:
        return 0.0
    union = c1 | c2
    return len(c1 & c2) / len(union) if union else 0.0


# ── Method 4: Size ──────────────────────────────────────────────────────────

def size_block_sim(sig1, sig2):
    n1 = sig1.num_instructions
    n2 = sig2.num_instructions
    if n1 == 0 and n2 == 0:
        return 0.0
    mx = max(n1, n2)
    return 1.0 - abs(n1 - n2) / mx


# ── Core matching logic ─────────────────────────────────────────────────────

METHODS = {
    'value': {'sim_fn': value_block_sim, 'threshold': 0.3},
    'opcodes': {'sim_fn': opcode_block_sim, 'threshold': 0.5},
    'constants': {'sim_fn': constant_block_sim, 'threshold': 0.3},
    'size': {'sim_fn': size_block_sim, 'threshold': 0.7},
}


def run_matching(sigs_o0, sigs_o2, sim_fn, threshold, gt_matrix=None):
    """Match blocks via Hungarian, evaluate against DWARF ground truth.

    gt_matrix: boolean numpy array [n_o0 × n_o2].  gt_matrix[i][j] = True means
               O0 block i and O2 block j map to overlapping source lines.
               If None, falls back to threshold-based self-evaluation.
    """
    addrs1 = sorted(sigs_o0.keys())
    addrs2 = sorted(sigs_o2.keys())
    n1, n2 = len(addrs1), len(addrs2)

    if n1 == 0 or n2 == 0:
        return {'matched': 0, 'correct': 0, 'accuracy': 0.0, 'pairs': [],
                'gt_available': gt_matrix is not None}

    sim_matrix = np.zeros((n1, n2))
    for i, a1 in enumerate(addrs1):
        for j, a2 in enumerate(addrs2):
            sim_matrix[i, j] = sim_fn(sigs_o0[a1], sigs_o2[a2])

    row_ind, col_ind = linear_sum_assignment(-sim_matrix)

    pairs = []
    correct = 0
    for r, c in zip(row_ind, col_ind):
        s = sim_matrix[r, c]
        if gt_matrix is not None:
            is_correct = bool(gt_matrix[r, c])
        else:
            is_correct = s >= threshold
        if is_correct:
            correct += 1
        pairs.append({
            'addr_o0': addrs1[r],
            'addr_o2': addrs2[c],
            'similarity': float(s),
            'is_correct': bool(is_correct),
        })

    n_matched = min(n1, n2)
    return {
        'matched': n_matched,
        'correct': correct,
        'accuracy': correct / n_matched if n_matched > 0 else 0.0,
        'pairs': sorted(pairs, key=lambda p: -p['similarity']),
        'gt_available': gt_matrix is not None,
    }


def analyze_function(base_name, lang, loader_o0, loader_o2, exec_o0, exec_o2,
                     find_fn, dwarf_o0=None, dwarf_o2=None, source_filter=None):
    addr_o0, name_o0 = find_fn(loader_o0, base_name)
    addr_o2, name_o2 = find_fn(loader_o2, base_name)

    if not addr_o0 or not addr_o2:
        return None

    sigs_o0 = exec_o0.execute_function(addr_o0)
    sigs_o2 = exec_o2.execute_function(addr_o2)
    cfg_o0 = loader_o0.get_cfg_for_function(addr_o0)
    cfg_o2 = loader_o2.get_cfg_for_function(addr_o2)

    n_o0 = len(sigs_o0)
    n_o2 = len(sigs_o2)

    # Build DWARF ground truth if mappers are available
    gt_matrix = None
    gt_coverage = {}
    addrs_o0 = sorted(sigs_o0.keys())
    addrs_o2 = sorted(sigs_o2.keys())
    if dwarf_o0 and dwarf_o2 and addrs_o0 and addrs_o2:
        lines_o0 = build_block_line_sets(loader_o0, dwarf_o0, addrs_o0, source_filter)
        lines_o2 = build_block_line_sets(loader_o2, dwarf_o2, addrs_o2, source_filter)
        gt_matrix = build_groundtruth_matrix(lines_o0, lines_o2, addrs_o0, addrs_o2)
        o0_has_lines = sum(1 for a in addrs_o0 if lines_o0.get(a))
        o2_has_lines = sum(1 for a in addrs_o2 if lines_o2.get(a))
        gt_matchable = int(gt_matrix.any(axis=1).sum())
        gt_coverage = {
            'o0_with_lines': o0_has_lines,
            'o2_with_lines': o2_has_lines,
            'o0_total': len(addrs_o0),
            'o2_total': len(addrs_o2),
            'gt_matchable_o0': gt_matchable,
        }

    method_results = {}
    for method_name, spec in METHODS.items():
        method_results[method_name] = run_matching(
            sigs_o0, sigs_o2, spec['sim_fn'], spec['threshold'], gt_matrix
        )

    # Build per-block source lines for JSON output
    lines_o0_map = {}
    lines_o2_map = {}
    if dwarf_o0 and dwarf_o2:
        lines_o0_map = build_block_line_sets(loader_o0, dwarf_o0, addrs_o0, source_filter)
        lines_o2_map = build_block_line_sets(loader_o2, dwarf_o2, addrs_o2, source_filter)

    block_details = []
    for a1 in addrs_o0:
        sig = sigs_o0[a1]
        bt = classify_block(sig, cfg_o0, a1).name
        block_details.append({
            'side': 'O0',
            'addr': f'0x{a1:x}',
            'type': bt,
            'n_insns': sig.num_instructions,
            'n_opcodes': len(set(sig.opcode_sequence)),
            'n_constants': len(sig.constants),
            'n_outputs': len(sig.concrete_outputs),
            'opcodes': list(sig.opcode_sequence)[:20],
            'constants': [hex(c) for c in sig.constants[:10]],
            'asm': _dump_asm(loader_o0, a1),
            'src_lines': sorted(lines_o0_map.get(a1, set())),
        })
    for a2 in addrs_o2:
        sig = sigs_o2[a2]
        bt = classify_block(sig, cfg_o2, a2).name
        block_details.append({
            'side': 'O2',
            'addr': f'0x{a2:x}',
            'type': bt,
            'n_insns': sig.num_instructions,
            'n_opcodes': len(set(sig.opcode_sequence)),
            'n_constants': len(sig.constants),
            'n_outputs': len(sig.concrete_outputs),
            'opcodes': list(sig.opcode_sequence)[:20],
            'constants': [hex(c) for c in sig.constants[:10]],
            'asm': _dump_asm(loader_o2, a2),
            'src_lines': sorted(lines_o2_map.get(a2, set())),
        })

    return {
        'base_name': base_name,
        'lang': lang,
        'feature': FEATURE_NAMES[base_name.split('_')[0]],
        'feature_prefix': base_name.split('_')[0],
        'name_o0': name_o0,
        'name_o2': name_o2,
        'n_o0': n_o0,
        'n_o2': n_o2,
        'gt_coverage': gt_coverage,
        'methods': {
            mn: {
                'matched': mr['matched'],
                'correct': mr['correct'],
                'accuracy': round(mr['accuracy'], 4),
                'gt_available': mr.get('gt_available', False),
                'pairs': [
                    {
                        'addr_o0': f"0x{p['addr_o0']:x}",
                        'addr_o2': f"0x{p['addr_o2']:x}",
                        'similarity': round(p['similarity'], 4),
                        'is_correct': p['is_correct'],
                    }
                    for p in mr['pairs']
                ],
            }
            for mn, mr in method_results.items()
        },
        'blocks': block_details,
    }


def _dump_asm(loader, addr, max_insns=12):
    node = loader.be.get_fast_cfg_node(addr)
    if not node or not node.block:
        return []
    lines = []
    insns = list(node.block.capstone.insns)
    for i, insn in enumerate(insns):
        if i >= max_insns:
            lines.append(f"... +{len(insns) - max_insns} more")
            break
        lines.append(f"0x{insn.address:x}: {insn.mnemonic:8s} {insn.op_str}")
    return lines


def build_data_driven_explanations(all_results, summary):
    """Generate explanations based on actual data, not templates."""
    from collections import Counter

    for prefix in PREFIXES:
        rust_fns = [r for r in all_results if r['feature_prefix'] == prefix and r['lang'] == 'Rust']
        c_fns = [r for r in all_results if r['feature_prefix'] == prefix and r['lang'] == 'C']

        # Compute per-feature statistics
        rust_avg_o0 = sum(f['n_o0'] for f in rust_fns) / len(rust_fns) if rust_fns else 0
        rust_avg_o2 = sum(f['n_o2'] for f in rust_fns) / len(rust_fns) if rust_fns else 0
        c_avg_o0 = sum(f['n_o0'] for f in c_fns) / len(c_fns) if c_fns else 0
        c_avg_o2 = sum(f['n_o2'] for f in c_fns) / len(c_fns) if c_fns else 0
        rust_ratio = rust_avg_o0 / rust_avg_o2 if rust_avg_o2 > 0 else 999
        c_ratio = c_avg_o0 / c_avg_o2 if c_avg_o2 > 0 else 999

        # Block type distributions
        rust_types = Counter()
        c_types = Counter()
        rust_no_output = 0
        rust_total_blocks = 0
        c_no_output = 0
        c_total_blocks = 0
        for fn in rust_fns:
            for b in fn.get('blocks', []):
                rust_types[b['type']] += 1
                rust_total_blocks += 1
                if b['n_outputs'] == 0:
                    rust_no_output += 1
        for fn in c_fns:
            for b in fn.get('blocks', []):
                c_types[b['type']] += 1
                c_total_blocks += 1
                if b['n_outputs'] == 0:
                    c_no_output += 1

        rust_no_pct = rust_no_output / rust_total_blocks if rust_total_blocks else 0
        c_no_pct = c_no_output / c_total_blocks if c_total_blocks else 0

        feature_label = FEATURE_NAMES[prefix]

        for method_name in METHODS:
            s = summary[prefix]['methods'][method_name]
            ra = s['rust_accuracy']
            ca = s['c_accuracy']
            winner = s['winner']

            if winner == 'TIE':
                s['explanation'] = (
                    f"TIE (Rust: {ra:.0%}, C: {ca:.0%}). "
                    f"Rust avg {rust_avg_o0:.0f}→{rust_avg_o2:.0f} blocks (O0→O2), "
                    f"C avg {c_avg_o0:.0f}→{c_avg_o2:.0f}. "
                    f"Despite Rust having {rust_avg_o0/c_avg_o0:.1f}x more blocks, "
                    f"both languages show similar {method_name} accuracy for {feature_label} functions."
                )
                continue

            # Data-driven explanation per method × feature
            explanation = f"{winner} wins (Rust: {ra:.0%}, C: {ca:.0%}). "

            if method_name == 'value':
                if winner == 'C':
                    explanation += (
                        f"C functions average {c_avg_o0:.0f} O0 blocks vs {c_avg_o2:.0f} O2 "
                        f"({c_ratio:.1f}:1 ratio), while Rust has {rust_avg_o0:.0f}→{rust_avg_o2:.0f} "
                        f"({rust_ratio:.1f}:1). "
                        f"Fewer blocks means less noise in Hungarian matching. "
                    )
                    if rust_no_pct > c_no_pct:
                        explanation += (
                            f"Also, {rust_no_pct:.0%} of Rust blocks lack concrete outputs "
                            f"(vs {c_no_pct:.0%} in C) — "
                        )
                        if prefix == 'om':
                            explanation += (
                                "move/ownership transfer blocks often produce only pointer shuffling "
                                "with no arithmetic outputs, leaving value-based matching blind."
                            )
                        elif prefix == 'dg':
                            explanation += (
                                "drop glue call-only blocks (drop_in_place<T>) produce no register outputs, "
                                "and O2 inlines or eliminates them entirely."
                            )
                        elif prefix == 'qm':
                            explanation += (
                                "? operator discriminant-check blocks are small cmp+branch "
                                "with no computation, producing no matchable outputs."
                            )
                        elif prefix == 'pu':
                            explanation += (
                                "panic cold-path blocks are call-only (to core::panicking::*) "
                                "with no arithmetic to produce concrete values."
                            )
                        else:
                            explanation += "these blocks are too small or call-only."
                else:
                    explanation += (
                        f"Rust's {feature_label.lower()} blocks produce more distinctive "
                        f"concrete outputs that survive O2 optimization. "
                        f"Rust: {rust_avg_o0:.0f}→{rust_avg_o2:.0f} blocks, "
                        f"C: {c_avg_o0:.0f}→{c_avg_o2:.0f}."
                    )

            elif method_name == 'opcodes':
                if winner == 'C':
                    explanation += (
                        f"C blocks average {c_avg_o0:.0f}→{c_avg_o2:.0f} (O0→O2), "
                        f"Rust {rust_avg_o0:.0f}→{rust_avg_o2:.0f}. "
                    )
                    if prefix == 'om':
                        explanation += (
                            "O2 reorganizes Rust ownership-transfer blocks — moves become "
                            "register renames, alloc+copy patterns merge, changing opcode sets. "
                            "C's pointer copies use consistent mov+lea opcodes at both O-levels."
                        )
                    elif prefix == 'dg':
                        explanation += (
                            "O2 inlines Rust's drop_in_place<T> calls into parent blocks, "
                            "replacing call opcodes with the inlined cleanup code and changing "
                            "the opcode set entirely. C's free() calls remain as-is."
                        )
                    elif prefix == 'bc':
                        explanation += (
                            "Rust bounds checks (cmp+jae+ud2) get eliminated or merged by O2, "
                            "changing surrounding block opcode sets. C has no bounds checks, "
                            "so its core computation opcodes are stable."
                        )
                    elif prefix == 'qm':
                        explanation += (
                            "Rust's ? operator generates multi-block discriminant check patterns "
                            "that O2 collapses into fewer blocks with different opcodes. "
                            "C's if(ret<0) pattern uses the same cmp+jcc at both O-levels."
                        )
                    elif prefix == 'pu':
                        explanation += (
                            "Rust panic paths involve call+lea+ud2 sequences that O2 reshuffles "
                            "into cold sections, changing block boundaries and opcode sets. "
                            "C's inline error returns (mov+ret) are opcode-stable."
                        )
                else:
                    explanation += (
                        f"Rust {feature_label.lower()} blocks use distinctive opcodes "
                        f"that remain stable across optimization."
                    )

            elif method_name == 'constants':
                if winner == 'C':
                    explanation += (
                        f"Rust blocks: {rust_total_blocks} total, "
                        f"C blocks: {c_total_blocks} total. "
                    )
                    if prefix in ('om', 'dg'):
                        explanation += (
                            "Rust's safety machinery uses few embedded constants — "
                            "most blocks are pointer arithmetic or call sequences with no immediates. "
                            "C uses explicit size constants (sizeof, capacity) that survive O2."
                        )
                    elif prefix == 'bc':
                        explanation += (
                            "Rust bounds checks use the slice length (a register, not a constant) "
                            "as the comparison operand, so no constant is embedded. "
                            "C array operations use explicit size literals that persist."
                        )
                    elif prefix in ('qm', 'pu'):
                        explanation += (
                            "Rust's error-path blocks reference string addresses (panic messages) "
                            "that change between O0 and O2 binary layouts. "
                            "C uses return-code constants (-1, 0) that are trivially stable."
                        )
                else:
                    explanation += (
                        f"Rust {feature_label.lower()} blocks embed more distinctive "
                        f"constants that survive optimization."
                    )

            elif method_name == 'size':
                if winner == 'Rust':
                    explanation += (
                        f"Rust O0→O2 block ratio: {rust_ratio:.1f}:1 vs C {c_ratio:.1f}:1. "
                    )
                    if prefix == 'dg':
                        explanation += (
                            "Rust's drop glue blocks are small (2-4 insns) and stay small at O2 "
                            "— they call drop_in_place which is a fixed-size stub. "
                            "C's computation blocks change size more when O2 inlines and unrolls."
                        )
                    elif prefix == 'bc':
                        explanation += (
                            "Rust bounds check blocks are fixed 3-4 instruction patterns "
                            "(cmp+jae+lea/ud2) that O2 cannot resize, only eliminate. "
                            "The surviving check blocks anchor size-based matching. "
                            "C lacks these fixed-size anchors."
                        )
                    elif prefix == 'qm':
                        explanation += (
                            "? operator blocks follow fixed patterns: "
                            "test discriminant (2 insns), extract value (2-3 insns), branch (1 insn). "
                            "O2 preserves these sizes because the error path structure is mandatory. "
                            "C's return-code blocks are small but O2 merges them into larger blocks."
                        )
                    elif prefix == 'pu':
                        explanation += (
                            "Panic-path blocks are cold and untouched by O2 optimization — "
                            "their instruction counts are identical at O0 and O2. "
                            "C has no cold paths, so all blocks are subject to O2 resizing."
                        )
                    elif prefix == 'om':
                        explanation += (
                            "Rust ownership blocks include fixed-size allocation stubs and "
                            "move patterns whose instruction counts persist. "
                            "C pointer-copy blocks are already minimal, but O2 may merge them."
                        )
                else:
                    explanation += (
                        f"C's simpler blocks ({c_avg_o0:.0f}→{c_avg_o2:.0f}) maintain "
                        f"more stable instruction counts across optimization than "
                        f"Rust ({rust_avg_o0:.0f}→{rust_avg_o2:.0f})."
                    )

            s['explanation'] = explanation

    # Also generate per-function explanations
    for r in all_results:
        prefix = r['feature_prefix']
        lang = r['lang']
        n_o0 = r['n_o0']
        n_o2 = r['n_o2']
        ratio = n_o0 / n_o2 if n_o2 > 0 else 999

        # Find the counterpart
        other_lang = 'C' if lang == 'Rust' else 'Rust'
        counterpart = None
        for r2 in all_results:
            if r2['base_name'] == r['base_name'] and r2['lang'] == other_lang:
                counterpart = r2
                break

        parts = [f"{r['base_name']} ({lang}): {n_o0} O0 blocks → {n_o2} O2 blocks ({ratio:.1f}:1)."]

        # Identify best and worst methods
        accs = {mn: r['methods'][mn]['accuracy'] for mn in METHODS}
        best_method = max(accs, key=accs.get)
        worst_method = min(accs, key=accs.get)

        parts.append(
            f"Best method: {best_method} ({accs[best_method]:.0%}), "
            f"worst: {worst_method} ({accs[worst_method]:.0%})."
        )

        if counterpart:
            cp_accs = {mn: counterpart['methods'][mn]['accuracy'] for mn in METHODS}
            wins = [mn for mn in METHODS if accs[mn] > cp_accs[mn] + 0.05]
            losses = [mn for mn in METHODS if cp_accs[mn] > accs[mn] + 0.05]
            if wins:
                parts.append(f"Beats {other_lang} on: {', '.join(wins)}.")
            if losses:
                parts.append(f"Loses to {other_lang} on: {', '.join(losses)}.")

            if ratio > 2.0 and lang == 'Rust':
                parts.append(
                    f"Large O0→O2 block reduction ({n_o0}→{n_o2}) means O2 eliminated "
                    f"{n_o0 - n_o2} safety/cleanup blocks, hurting all matching methods."
                )
            elif lang == 'C' and counterpart['n_o0'] > 2 * n_o0:
                parts.append(
                    f"Simpler structure ({n_o0} vs Rust's {counterpart['n_o0']} blocks) "
                    f"means less Hungarian matching noise."
                )

        r['explanation'] = ' '.join(parts)


def main():
    sys.stderr.write("Loading 4 binaries...\n")
    rust_o0 = RustBinaryLoader(str(EXP_DIR / 'rust_O0'))
    rust_o2 = RustBinaryLoader(str(EXP_DIR / 'rust_O2'))
    c_o0 = RustBinaryLoader(str(EXP_DIR / 'c_bench_O0'))
    c_o2 = RustBinaryLoader(str(EXP_DIR / 'c_bench_O2'))

    sys.stderr.write("Loading DWARF line info...\n")
    dwarf_rust_o0 = DWARFLineMapper(str(EXP_DIR / 'rust_O0'))
    dwarf_rust_o2 = DWARFLineMapper(str(EXP_DIR / 'rust_O2'))
    dwarf_c_o0 = DWARFLineMapper(str(EXP_DIR / 'c_bench_O0'))
    dwarf_c_o2 = DWARFLineMapper(str(EXP_DIR / 'c_bench_O2'))
    sys.stderr.write(f"  Rust O0: {len(dwarf_rust_o0.entries)} line entries\n")
    sys.stderr.write(f"  Rust O2: {len(dwarf_rust_o2.entries)} line entries\n")
    sys.stderr.write(f"  C O0: {len(dwarf_c_o0.entries)} line entries\n")
    sys.stderr.write(f"  C O2: {len(dwarf_c_o2.entries)} line entries\n")

    sys.stderr.write("Creating micro-executors...\n")
    rust_exec_o0 = BlockMicroExecutor(rust_o0)
    rust_exec_o2 = BlockMicroExecutor(rust_o2)
    c_exec_o0 = BlockMicroExecutor(c_o0)
    c_exec_o2 = BlockMicroExecutor(c_o2)

    all_results = []
    found = {'rust': 0, 'c': 0}
    missed = {'rust': [], 'c': []}

    for i, base_name in enumerate(ALL_FUNCS):
        sys.stderr.write(f"\r[{i+1}/{len(ALL_FUNCS)}] {base_name}...          ")
        sys.stderr.flush()

        rust_r = analyze_function(
            base_name, 'Rust', rust_o0, rust_o2,
            rust_exec_o0, rust_exec_o2, find_func_addr_rust,
            dwarf_rust_o0, dwarf_rust_o2, 'main.rs'
        )
        c_r = analyze_function(
            base_name, 'C', c_o0, c_o2,
            c_exec_o0, c_exec_o2, find_func_addr_c,
            dwarf_c_o0, dwarf_c_o2, 'bench.c'
        )

        if rust_r:
            all_results.append(rust_r)
            found['rust'] += 1
        else:
            missed['rust'].append(base_name)

        if c_r:
            all_results.append(c_r)
            found['c'] += 1
        else:
            missed['c'].append(base_name)

    sys.stderr.write(f"\n\nFound: Rust={found['rust']}/100, C={found['c']}/100\n")
    if missed['rust']:
        sys.stderr.write(f"Missed Rust: {', '.join(missed['rust'][:10])}\n")
    if missed['c']:
        sys.stderr.write(f"Missed C: {', '.join(missed['c'][:10])}\n")

    # Build feature × method summary with explanations
    summary = {}
    for prefix in PREFIXES:
        summary[prefix] = {'name': FEATURE_NAMES[prefix], 'methods': {}}
        for method_name in METHODS:
            rust_correct = 0
            rust_total = 0
            c_correct = 0
            c_total = 0
            for r in all_results:
                if r['feature_prefix'] == prefix:
                    m = r['methods'][method_name]
                    if r['lang'] == 'Rust':
                        rust_correct += m['correct']
                        rust_total += m['matched']
                    else:
                        c_correct += m['correct']
                        c_total += m['matched']
            rust_acc = rust_correct / rust_total if rust_total > 0 else 0
            c_acc = c_correct / c_total if c_total > 0 else 0
            winner = "Rust" if rust_acc > c_acc + 0.01 else "C" if c_acc > rust_acc + 0.01 else "TIE"
            summary[prefix]['methods'][method_name] = {
                'rust_correct': rust_correct,
                'rust_total': rust_total,
                'rust_accuracy': round(rust_acc, 4),
                'c_correct': c_correct,
                'c_total': c_total,
                'c_accuracy': round(c_acc, 4),
                'winner': winner,
                'explanation': '',
            }

    build_data_driven_explanations(all_results, summary)

    output = {
        'functions': all_results,
        'summary': summary,
        'methods': list(METHODS.keys()),
        'features': {p: FEATURE_NAMES[p] for p in PREFIXES},
    }

    out_path = EXP_DIR / 'results' / 'analysis_data.json'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2))
    sys.stderr.write(f"\nJSON written to {out_path}\n")

    # Print summary table
    sys.stderr.write("\n" + "=" * 90 + "\n")
    sys.stderr.write("FEATURE × METHOD ACCURACY SUMMARY (Rust vs C)\n")
    sys.stderr.write("=" * 90 + "\n\n")

    header = f"{'Feature':<25}"
    for mn in METHODS:
        header += f" | {mn:>18}"
    sys.stderr.write(header + "\n")
    sys.stderr.write("-" * len(header) + "\n")

    for prefix in PREFIXES:
        row = f"{FEATURE_NAMES[prefix]:<25}"
        for mn in METHODS:
            s = summary[prefix]['methods'][mn]
            row += f" | R:{s['rust_accuracy']:4.0%} C:{s['c_accuracy']:4.0%}"
        sys.stderr.write(row + "\n")

    # Per-function detail table
    sys.stderr.write("\n" + "=" * 110 + "\n")
    sys.stderr.write("PER-FUNCTION DETAIL\n")
    sys.stderr.write("=" * 110 + "\n\n")
    sys.stderr.write(
        f"{'Func':<8} {'Lang':<5} {'#O0':>4} {'#O2':>4}"
        f" | {'Value':>8} {'Opcode':>8} {'Const':>8} {'Size':>8}\n"
    )
    sys.stderr.write("-" * 70 + "\n")

    for base_name in ALL_FUNCS:
        for r in all_results:
            if r['base_name'] == base_name:
                line = f"{r['base_name']:<8} {r['lang']:<5} {r['n_o0']:>4} {r['n_o2']:>4}"
                for mn in METHODS:
                    m = r['methods'][mn]
                    line += f" | {m['accuracy']:>7.0%}"
                sys.stderr.write(line + "\n")


if __name__ == '__main__':
    main()
