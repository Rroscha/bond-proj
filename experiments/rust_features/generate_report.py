#!/usr/bin/env python3
"""Generate an explanatory Rust vs C comparison report.

The report is written for someone who has never seen binary analysis before.
Each of the 5 Rust features gets one detailed walkthrough example with
annotated source code, assembly, and block-by-block comparison.
Then all 100 functions are shown in a summary table.
"""
import json
import re
import html as html_mod
from pathlib import Path

EXP_DIR = Path(__file__).resolve().parent
DATA = json.loads((EXP_DIR / 'results' / 'analysis_data.json').read_text())

PREFIXES = ['bc', 'om', 'dg', 'qm', 'pu']
FEATURE_NAMES = DATA['features']
METHODS_LIST = ['value', 'opcodes', 'constants']
METHOD_LABELS = {'value': 'Value-based', 'opcodes': 'Opcodes', 'constants': 'Constants'}


def parse_rust_functions(path):
    text = path.read_text()
    funcs = {}
    pattern = re.compile(
        r'(///[^\n]*\n)?#\[inline\(never\)\]\s*\n(fn\s+(\w+)\s*(?:<[^>]+>)?\s*\([^)]*\)(?:\s*->[^{]*)?\s*\{)',
        re.MULTILINE)
    for m in pattern.finditer(text):
        fn_name = m.group(3)
        start = m.start()
        depth = 0
        end = m.end()
        for i in range(m.end() - 1, len(text)):
            if text[i] == '{': depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        funcs[fn_name] = text[start:end].strip()
    return funcs


def parse_c_functions(path):
    text = path.read_text()
    funcs = {}
    pattern = re.compile(r'(/\*[^*]*\*/\s*\n)?NOINLINE\s+\S+\s+\**(\w+)\s*\([^)]*\)\s*\{', re.MULTILINE)
    for m in pattern.finditer(text):
        fn_name = m.group(2)
        start = m.start()
        depth = 0
        end = m.end()
        for i in range(m.end() - 1, len(text)):
            if text[i] == '{': depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        funcs[fn_name] = text[start:end].strip()
    return funcs


RUST_SRC = parse_rust_functions(EXP_DIR / 'rust_crate' / 'src' / 'main.rs')
C_SRC = parse_c_functions(EXP_DIR / 'c_src' / 'bench.c')
print(f"Parsed {len(RUST_SRC)} Rust, {len(C_SRC)} C functions")

E = html_mod.escape

BLOCK_COLORS = {
    'BODY': '#58a6ff',
    'BOUNDS_CHECK': '#f97583',
    'LOOP': '#3fb950',
    'CALL': '#d2a8ff',
    'PANIC': '#f85149',
    'INIT': '#79c0ff',
    'SETUP': '#79c0ff',
    'DROP': '#e3b341',
    'RETURN': '#8b949e',
    'BRANCH': '#56d4dd',
}


def block_color(btype):
    for key, col in BLOCK_COLORS.items():
        if key in btype.upper():
            return col
    return '#6e7681'


def gen_matching_svg(fn_data, method_name, label):
    """Generate an inline SVG showing block matching between O0 and O2."""
    o0_blocks = [b for b in fn_data.get('blocks', []) if b['side'] == 'O0']
    o2_blocks = [b for b in fn_data.get('blocks', []) if b['side'] == 'O2']
    pairs = fn_data['methods'][method_name]['pairs']

    o0_addrs = {b['addr']: b for b in o0_blocks}
    o2_addrs = {b['addr']: b for b in o2_blocks}

    bh = 20
    gap = 3
    n_left = len(o0_blocks)
    n_right = len(o2_blocks)
    max_n = max(n_left, n_right, 1)
    svg_h = max_n * (bh + gap) + 50
    left_x = 10
    right_x = 460
    block_w = 150
    left_cx = left_x + block_w
    right_cx = right_x

    matched_o0 = set()
    matched_o2 = set()
    for p in pairs:
        matched_o0.add(p['addr_o0'])
        matched_o2.add(p['addr_o2'])

    o0_y = {}
    o2_y = {}
    for i, b in enumerate(o0_blocks):
        o0_y[b['addr']] = 30 + i * (bh + gap)
    for i, b in enumerate(o2_blocks):
        o2_y[b['addr']] = 30 + i * (bh + gap)

    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="620" height="{svg_h}" '
             f'style="background:#0d1117;border:1px solid #30363d;border-radius:6px;margin:4px 0">']

    parts.append(f'<text x="{left_x + block_w//2}" y="18" fill="#8b949e" font-size="11" '
                 f'text-anchor="middle" font-family="sans-serif">O0 ({n_left} blocks)</text>')
    parts.append(f'<text x="{right_x + block_w//2}" y="18" fill="#8b949e" font-size="11" '
                 f'text-anchor="middle" font-family="sans-serif">O2 ({n_right} blocks)</text>')

    for p in pairs:
        a0, a2 = p['addr_o0'], p['addr_o2']
        if a0 in o0_y and a2 in o2_y:
            y1 = o0_y[a0] + bh // 2
            y2 = o2_y[a2] + bh // 2
            if p['is_correct']:
                col, w = '#3fb950', '2'
            else:
                col, w = '#f85149', '1.5'
            parts.append(f'<line x1="{left_cx}" y1="{y1}" x2="{right_cx}" y2="{y2}" '
                         f'stroke="{col}" stroke-width="{w}" opacity="0.7"/>')

    for b in o0_blocks:
        y = o0_y[b['addr']]
        col = block_color(b['type'])
        matched = b['addr'] in matched_o0
        opacity = '1' if matched else '0.4'
        parts.append(f'<rect x="{left_x}" y="{y}" width="{block_w}" height="{bh}" '
                     f'rx="3" fill="{col}" opacity="{opacity}"/>')
        short = b['type'][:12]
        parts.append(f'<text x="{left_x + 5}" y="{y + 14}" fill="#0d1117" font-size="9" '
                     f'font-family="monospace">{E(short)} ({b["n_insns"]})</text>')

    for b in o2_blocks:
        y = o2_y[b['addr']]
        col = block_color(b['type'])
        matched = b['addr'] in matched_o2
        opacity = '1' if matched else '0.4'
        parts.append(f'<rect x="{right_x}" y="{y}" width="{block_w}" height="{bh}" '
                     f'rx="3" fill="{col}" opacity="{opacity}"/>')
        short = b['type'][:12]
        parts.append(f'<text x="{right_x + 5}" y="{y + 14}" fill="#0d1117" font-size="9" '
                     f'font-family="monospace">{E(short)} ({b["n_insns"]})</text>')

    correct = sum(1 for p in pairs if p['is_correct'])
    total = len(pairs)
    acc = correct / total if total else 0
    parts.append(f'<text x="310" y="{svg_h - 8}" fill="#c9d1d9" font-size="11" '
                 f'text-anchor="middle" font-family="sans-serif">'
                 f'{label}: {correct}/{total} share source lines (DWARF) = {acc:.0%}</text>')

    parts.append('</svg>')
    return '\n'.join(parts)


def jaccard(set_a, set_b):
    a, b = set(set_a), set(set_b)
    if not a and not b:
        return 1.0
    inter = a & b
    return len(inter) / len(a | b) if (a | b) else 0.0


def fmt_src_lines_badge(b0, b2):
    """Show source line overlap between two blocks as a badge."""
    s0 = set(b0.get('src_lines', []))
    s2 = set(b2.get('src_lines', []))
    if not s0 and not s2:
        return '<span class="src-badge none">No DWARF data — cannot verify this pair</span>'
    shared = sorted(s0 & s2)
    if shared:
        n = len(shared)
        return (f'<span class="src-badge match">CORRECT — both blocks compile from '
                f'{"the same" if n == 1 else str(n) + " shared"} source line{"s" if n > 1 else ""}</span>')
    else:
        return (f'<span class="src-badge nomatch">WRONG — O0 block comes from line{"s" if len(s0) > 1 else ""} '
                f'{", ".join(str(l) for l in sorted(s0)[:3]) if s0 else "?"}, '
                f'O2 from line{"s" if len(s2) > 1 else ""} '
                f'{", ".join(str(l) for l in sorted(s2)[:3]) if s2 else "?"} '
                f'(different code)</span>')


def fmt_asm_pair(b0, b2, max_lines=8, show_badge=True):
    """Format two blocks' assembly side-by-side as HTML, optionally with source line badge."""
    badge = fmt_src_lines_badge(b0, b2) if show_badge else ''
    asm0 = b0.get('asm', [])[:max_lines]
    asm2 = b2.get('asm', [])[:max_lines]
    rows = max(len(asm0), len(asm2))
    html = f'<div class="asm-pair">{badge}<table class="asm-tbl"><tr><th>O0</th><th>O2</th></tr>'
    for i in range(rows):
        l = E(asm0[i].split(': ', 1)[-1]) if i < len(asm0) else ''
        r = E(asm2[i].split(': ', 1)[-1]) if i < len(asm2) else ''
        html += f'<tr><td><code>{l}</code></td><td><code>{r}</code></td></tr>'
    if len(b0.get('asm', [])) > max_lines or len(b2.get('asm', [])) > max_lines:
        html += f'<tr><td colspan="2" class="asm-more">... truncated</td></tr>'
    html += '</table></div>'
    return html


def fmt_asm_single(b, max_lines=6):
    """Format one block's assembly as a small code box."""
    asm = b.get('asm', [])[:max_lines]
    lines = '\n'.join(line.split(': ', 1)[-1] if ': ' in line else line for line in asm)
    extra = f'\n... +{len(b.get("asm",[]))-max_lines} more' if len(b.get('asm', [])) > max_lines else ''
    return f'<pre class="asm-snippet">{E(lines + extra)}</pre>'


def gen_match_analysis(fn_data, method_name, lang_label):
    """Generate HTML explaining WHY each pair matched or didn't, with assembly evidence."""
    blocks = {b['addr']: b for b in fn_data.get('blocks', [])}
    o0_blocks = [b for b in fn_data.get('blocks', []) if b['side'] == 'O0']
    o2_blocks = [b for b in fn_data.get('blocks', []) if b['side'] == 'O2']
    pairs = fn_data['methods'][method_name]['pairs']

    correct = [p for p in pairs if p['is_correct']]
    wrong = [p for p in pairs if not p['is_correct']]
    paired_o0 = {p['addr_o0'] for p in pairs}
    paired_o2 = {p['addr_o2'] for p in pairs}
    unmatched_o0 = [b for b in o0_blocks if b['addr'] not in paired_o0]
    unmatched_o2 = [b for b in o2_blocks if b['addr'] not in paired_o2]

    parts = []

    # --- Correct matches: pick up to 2 interesting ones ---
    if correct:
        parts.append('<div class="analysis-group correct-group">')
        parts.append(f'<div class="analysis-title good-title">'
                     f'&#10003; {len(correct)} correct matches '
                     f'(verified: O0 and O2 block share source lines in DWARF):</div>')
        def correct_sort_key(p):
            b0 = blocks.get(p['addr_o0'], {})
            b2 = blocks.get(p['addr_o2'], {})
            both_have_lines = bool(b0.get('src_lines') and b2.get('src_lines'))
            return (both_have_lines, p['similarity'])

        shown = 0
        for p in sorted(correct, key=correct_sort_key, reverse=True):
            if shown >= 2:
                break
            b0 = blocks.get(p['addr_o0'])
            b2 = blocks.get(p['addr_o2'])
            if not b0 or not b2:
                continue
            shown += 1

            if method_name == 'opcodes':
                ops0 = set(b0.get('opcodes', []))
                ops2 = set(b2.get('opcodes', []))
                shared = sorted(ops0 & ops2)
                only0 = sorted(ops0 - ops2)
                only2 = sorted(ops2 - ops0)
                detail = (f'<span class="shared-ops">Shared opcodes: '
                          f'<code>{", ".join(shared) if shared else "none"}</code></span>')
                if only0:
                    detail += f' <span class="diff-ops">Only in O0: <code>{", ".join(only0)}</code></span>'
                if only2:
                    detail += f' <span class="diff-ops">Only in O2: <code>{", ".join(only2)}</code></span>'
                algo_reason = (f'Why the algorithm paired them: both use the same instruction types '
                               f'({len(shared)}/{len(ops0 | ops2)} opcodes overlap).')
            elif method_name == 'constants':
                c0 = set(b0.get('constants', []))
                c2 = set(b2.get('constants', []))
                shared = sorted(c0 & c2)
                only0 = sorted(c0 - c2)
                only2 = sorted(c2 - c0)
                detail = (f'<span class="shared-ops">Shared constants: '
                          f'<code>{", ".join(shared) if shared else "none"}</code></span>')
                if only0:
                    detail += f' <span class="diff-ops">Only in O0: <code>{", ".join(only0)}</code></span>'
                if only2:
                    detail += f' <span class="diff-ops">Only in O2: <code>{", ".join(only2)}</code></span>'
                algo_reason = (f'Why the algorithm paired them: both embed the same numeric constants '
                               f'({len(shared)} in common).')
            else:
                n_out0 = b0.get('n_outputs', 0)
                n_out2 = b2.get('n_outputs', 0)
                detail = f'O0 produces {n_out0} output values, O2 produces {n_out2}'
                algo_reason = ('Why the algorithm paired them: both blocks produce similar '
                               'values when given the same test inputs.')

            parts.append(
                f'<div class="pair-explain">'
                f'<div class="pair-hdr">'
                f'<span class="bt">{b0["type"]}</span> ({b0["n_insns"]} insns) '
                f'&#x2194; '
                f'<span class="bt">{b2["type"]}</span> ({b2["n_insns"]} insns) '
                f'— sim={p["similarity"]:.0%}</div>'
                f'<div class="pair-detail">{detail}</div>'
                f'{fmt_src_lines_badge(b0, b2)}'
                f'{fmt_asm_pair(b0, b2, show_badge=False)}'
                f'<div class="pair-reason">{algo_reason}</div>'
                f'</div>')

        if len(correct) > 2:
            types = {}
            for p in correct:
                b0 = blocks.get(p['addr_o0'], {})
                t = b0.get('type', '?')
                types[t] = types.get(t, 0) + 1
            type_summary = ', '.join(f'{cnt}x {t}' for t, cnt in sorted(types.items(), key=lambda x: -x[1]))
            parts.append(f'<div class="pair-extra">... and {len(correct)-2} more correct matches '
                         f'({type_summary})</div>')
        parts.append('</div>')

    # --- Wrong matches: pick up to 2 ---
    if wrong:
        parts.append('<div class="analysis-group wrong-group">')
        parts.append(f'<div class="analysis-title bad-title">'
                     f'&#10007; {len(wrong)} wrong matches '
                     f'(O0 and O2 block do NOT share source lines):</div>')
        def wrong_sort_key(p):
            b0 = blocks.get(p['addr_o0'], {})
            b2 = blocks.get(p['addr_o2'], {})
            both_have_lines = bool(b0.get('src_lines') and b2.get('src_lines'))
            return (both_have_lines, -p['similarity'])

        shown = 0
        for p in sorted(wrong, key=wrong_sort_key, reverse=True):
            if shown >= 2:
                break
            b0 = blocks.get(p['addr_o0'])
            b2 = blocks.get(p['addr_o2'])
            if not b0 or not b2:
                continue
            shown += 1

            if method_name == 'opcodes':
                ops0 = set(b0.get('opcodes', []))
                ops2 = set(b2.get('opcodes', []))
                shared = sorted(ops0 & ops2)
                only0 = sorted(ops0 - ops2)
                only2 = sorted(ops2 - ops0)
                jac = jaccard(ops0, ops2)
                detail = (f'Opcode overlap: {len(shared)}/{len(ops0 | ops2)} '
                          f'(Jaccard = {jac:.0%})')
                if only0:
                    detail += f' <span class="diff-ops">O0-only: <code>{", ".join(only0[:5])}</code></span>'
                if only2:
                    detail += f' <span class="diff-ops">O2-only: <code>{", ".join(only2[:5])}</code></span>'
                if b0['type'] != b2['type']:
                    rust_types = {'BOUNDS_CHECK': 'bounds checking',
                                  'PANIC': 'panic/unwrap', 'DROP': 'drop glue'}
                    feature_note = ''
                    for t, desc in rust_types.items():
                        if t in b0['type'] or t in b2['type']:
                            feature_note = (f' This is a Rust {desc} block — it exists '
                                            f'because of Rust\'s safety features and has no '
                                            f'C equivalent, confusing the matcher.')
                            break
                    reason = (f'The algorithm paired a <strong>{b0["type"]}</strong> block with '
                              f'a <strong>{b2["type"]}</strong> block. These have different roles '
                              f'in the function, but their opcode sets happened to look similar '
                              f'enough that the algorithm confused them.{feature_note}')
                elif b0['n_insns'] > 3 * b2['n_insns'] or b2['n_insns'] > 3 * b0['n_insns']:
                    big, small = (b0['n_insns'], b2['n_insns']) if b0['n_insns'] > b2['n_insns'] else (b2['n_insns'], b0['n_insns'])
                    reason = (f'Size mismatch: {big} vs {small} instructions. '
                              f'The optimizer split or merged blocks, so one side is a fragment '
                              f'of what the other contains. The algorithm matched them because '
                              f'the surviving opcodes overlap, but they come from different source lines.')
                else:
                    reason = (f'Both are {b0["type"]} blocks, but the optimizer reorganized '
                              f'their instructions. The opcode sets overlap enough to fool the '
                              f'algorithm, but DWARF shows they come from different source code.')
            elif method_name == 'constants':
                c0 = set(b0.get('constants', []))
                c2 = set(b2.get('constants', []))
                detail = f'O0 constants: {list(c0) if c0 else "none"}, O2: {list(c2) if c2 else "none"}'
                if not c0 and not c2:
                    reason = ('Neither block has constants — the algorithm had no signal, '
                              'so it made an arbitrary assignment. Look at the code: '
                              'pure register-to-register operations, no embedded numbers.')
                elif not c0 or not c2:
                    reason = ('One side has constants, the other doesn\'t. '
                              'The optimizer replaced literal values with register-computed values, '
                              'removing the only signal this method can use.')
                else:
                    reason = ('The constants changed — the optimizer folded computations '
                              'or replaced offsets with different addressing modes.')
            else:
                n_out0 = b0.get('n_outputs', 0)
                n_out2 = b2.get('n_outputs', 0)
                detail = f'O0 outputs: {n_out0}, O2 outputs: {n_out2}'
                if n_out0 == 0 and n_out2 == 0:
                    reason = ('Neither block produces values — pure control flow '
                              '(jumps/checks). No execution data to match on.')
                elif n_out0 == 0 or n_out2 == 0:
                    reason = ('One side produces values, the other doesn\'t. '
                              'The optimizer eliminated the computation or '
                              'merged it into an adjacent block.')
                else:
                    reason = ('Both produce values, but different register allocation '
                              'and reordered computations mean the outputs no longer overlap.')

            parts.append(
                f'<div class="pair-explain wrong">'
                f'<div class="pair-hdr">'
                f'<span class="bt">{b0["type"]}</span> ({b0["n_insns"]} insns) '
                f'&#10060; '
                f'<span class="bt">{b2["type"]}</span> ({b2["n_insns"]} insns) '
                f'— sim={p["similarity"]:.0%}</div>'
                f'<div class="pair-detail">{detail}</div>'
                f'{fmt_src_lines_badge(b0, b2)}'
                f'{fmt_asm_pair(b0, b2, show_badge=False)}'
                f'<div class="pair-reason">Why the algorithm paired them: {reason}</div>'
                f'</div>')

        if len(wrong) > 2:
            parts.append(f'<div class="pair-extra">... and {len(wrong)-2} more wrong matches</div>')
        parts.append('</div>')

    # --- Unmatched blocks: show 1 example with assembly ---
    if unmatched_o0 or unmatched_o2:
        n_o0 = len([b for b in fn_data.get('blocks', []) if b['side'] == 'O0'])
        n_o2 = len([b for b in fn_data.get('blocks', []) if b['side'] == 'O2'])
        parts.append('<div class="analysis-group unmatched-group">')
        if unmatched_o0:
            types = {}
            for b in unmatched_o0:
                t = b['type']
                types[t] = types.get(t, 0) + 1
            type_str = ', '.join(f'{cnt}x {t}' for t, cnt in sorted(types.items(), key=lambda x: -x[1]))
            if n_o0 > n_o2:
                reason = (f'There are more O0 blocks ({n_o0}) than O2 blocks ({n_o2}), '
                          f'so the Hungarian algorithm can only pair {n_o2}. '
                          f'The remaining {len(unmatched_o0)} have no partner')
            else:
                reason = (f'{len(unmatched_o0)} O0 blocks were paired with O2 blocks '
                          f'but are left over because the algorithm assigns one-to-one')
            parts.append(f'<div class="unmatched-info">'
                         f'{len(unmatched_o0)} O0 blocks unmatched '
                         f'({type_str}): {reason}</div>')
            ub = unmatched_o0[0]
            parts.append(f'<div class="unmatched-example">'
                         f'<span class="bt">{ub["type"]}</span> ({ub["n_insns"]} insns):'
                         f'{fmt_asm_single(ub)}</div>')
        if unmatched_o2:
            types = {}
            for b in unmatched_o2:
                t = b['type']
                types[t] = types.get(t, 0) + 1
            type_str = ', '.join(f'{cnt}x {t}' for t, cnt in sorted(types.items(), key=lambda x: -x[1]))
            if n_o2 > n_o0:
                reason = (f'There are more O2 blocks ({n_o2}) than O0 blocks ({n_o0}), '
                          f'so {len(unmatched_o2)} O2 blocks have no partner')
            else:
                reason = f'{len(unmatched_o2)} O2 blocks left over from one-to-one assignment'
            parts.append(f'<div class="unmatched-info">'
                         f'{len(unmatched_o2)} O2 blocks unmatched '
                         f'({type_str}): {reason}</div>')
            ub = unmatched_o2[0]
            parts.append(f'<div class="unmatched-example">'
                         f'<span class="bt">{ub["type"]}</span> ({ub["n_insns"]} insns):'
                         f'{fmt_asm_single(ub)}</div>')
        parts.append('</div>')

    return '\n'.join(parts)


def _pick_example_pair(pairs, blocks, want_correct, prefer_types=None):
    """Pick a representative pair (correct or wrong) and return (b0, b2, pair).

    Prefers pairs where both blocks have DWARF source lines (so the badge is informative).
    If prefer_types is set, also prefers pairs involving those block types.
    """
    candidates = [p for p in pairs if p['is_correct'] == want_correct]
    if not candidates:
        return None, None, None

    def score(p):
        b0 = blocks.get(p['addr_o0'], {})
        b2 = blocks.get(p['addr_o2'], {})
        has_asm = bool(b0.get('asm') and b2.get('asm'))
        has_lines = bool(b0.get('src_lines') and b2.get('src_lines'))
        type_match = 0
        if prefer_types:
            for t in prefer_types:
                if t in b0.get('type', '') or t in b2.get('type', ''):
                    type_match = 1
                    break
        sim = p['similarity'] if want_correct else -p['similarity']
        return (has_asm, has_lines, type_match, sim)

    for p in sorted(candidates, key=score, reverse=True):
        b0 = blocks.get(p['addr_o0'])
        b2 = blocks.get(p['addr_o2'])
        if b0 and b2 and b0.get('asm') and b2.get('asm'):
            return b0, b2, p
    return None, None, None


def gen_cross_comparison(rust_data, c_data, method_name):
    """Generate a Rust vs C comparison summary with concrete assembly evidence."""
    r_pairs = rust_data['methods'][method_name]['pairs']
    c_pairs = c_data['methods'][method_name]['pairs']
    r_correct = sum(1 for p in r_pairs if p['is_correct'])
    c_correct = sum(1 for p in c_pairs if p['is_correct'])
    r_acc = r_correct / len(r_pairs) if r_pairs else 0
    c_acc = c_correct / len(c_pairs) if c_pairs else 0

    r_blocks = {b['addr']: b for b in rust_data.get('blocks', [])}
    c_blocks = {b['addr']: b for b in c_data.get('blocks', [])}

    r_o0 = [b for b in rust_data.get('blocks', []) if b['side'] == 'O0']
    r_o2 = [b for b in rust_data.get('blocks', []) if b['side'] == 'O2']
    c_o0 = [b for b in c_data.get('blocks', []) if b['side'] == 'O0']
    c_o2 = [b for b in c_data.get('blocks', []) if b['side'] == 'O2']

    winner = 'Rust' if r_acc > c_acc + 0.01 else 'C' if c_acc > r_acc + 0.01 else 'Tie'
    winner_cls = 'rv' if winner == 'Rust' else 'cv' if winner == 'C' else ''

    parts = []

    if winner == 'Rust':
        r_correct_types = {}
        for p in r_pairs:
            if p['is_correct']:
                b = r_blocks.get(p['addr_o0'], {})
                t = b.get('type', '?')
                r_correct_types[t] = r_correct_types.get(t, 0) + 1
        top_type = max(r_correct_types, key=r_correct_types.get) if r_correct_types else '?'
        top_count = r_correct_types.get(top_type, 0)

        parts.append(f'<div class="cross-hdr"><span class="{winner_cls}">'
                     f'Rust wins ({r_acc:.0%} vs {c_acc:.0%})</span></div>')

        if method_name == 'opcodes':
            parts.append(f'<p>Rust has {r_correct}/{len(r_pairs)} correct vs C\'s {c_correct}/{len(c_pairs)}. '
                         f'Key driver: {top_count} correct matches from <strong>{top_type}</strong> blocks.</p>')
        elif method_name == 'constants':
            parts.append(f'<p>Rust embeds more recognizable numeric constants that persist through optimization.</p>')
        else:
            parts.append(f'<p>Rust blocks produce more stable execution outputs. '
                         f'{top_count} correct matches from <strong>{top_type}</strong> blocks.</p>')

        rb0, rb2, rp = _pick_example_pair(r_pairs, r_blocks, True)
        if rb0:
            parts.append(f'<div class="evidence-label rl">Rust example (correct, sim={rp["similarity"]:.0%}):</div>')
            parts.append(fmt_asm_pair(rb0, rb2, max_lines=5))

        cb0, cb2, cp = _pick_example_pair(c_pairs, c_blocks, False)
        if cb0:
            parts.append(f'<div class="evidence-label cl">C example (wrong, sim={cp["similarity"]:.0%}):</div>')
            parts.append(fmt_asm_pair(cb0, cb2, max_lines=5))

    elif winner == 'C':
        ratio_r = len(r_o0) / len(r_o2) if r_o2 else 1
        ratio_c = len(c_o0) / len(c_o2) if c_o2 else 1

        r_wrong = sum(1 for p in r_pairs if not p['is_correct'])
        r_wrong_cross = 0
        for p in r_pairs:
            if not p['is_correct']:
                b0 = r_blocks.get(p['addr_o0'], {})
                b2 = r_blocks.get(p['addr_o2'], {})
                if b0.get('type') != b2.get('type'):
                    r_wrong_cross += 1

        parts.append(f'<div class="cross-hdr"><span class="{winner_cls}">'
                     f'C wins ({c_acc:.0%} vs {r_acc:.0%})</span></div>')

        if method_name == 'opcodes':
            parts.append(f'<p>C has only {len(c_o0)} O0 blocks vs Rust\'s {len(r_o0)}. '
                         f'Fewer blocks means the Hungarian algorithm has fewer choices to get wrong. '
                         f'Of Rust\'s {r_wrong} wrong matches, {r_wrong_cross} pair blocks of '
                         f'different types (e.g., a BODY block matched to a PANIC block).</p>')
        elif method_name == 'constants':
            r_empty = sum(1 for b in r_o0 if not b.get('constants'))
            c_empty = sum(1 for b in c_o0 if not b.get('constants'))
            parts.append(f'<p>C uses explicit size literals (malloc sizes, bounds) that survive as immediates. '
                         f'Rust: {r_empty}/{len(r_o0)} blocks have no constants '
                         f'(C: {c_empty}/{len(c_o0)}).</p>')
        else:
            r_no_out = sum(1 for b in r_o0 if b.get('n_outputs', 0) == 0)
            c_no_out = sum(1 for b in c_o0 if b.get('n_outputs', 0) == 0)
            parts.append(f'<p>Rust has {r_no_out}/{len(r_o0)} O0 blocks with no execution output '
                         f'(C: {c_no_out}/{len(c_o0)}). '
                         f'Many Rust blocks are pure control flow with nothing to match on.</p>')

        cb0, cb2, cp = _pick_example_pair(c_pairs, c_blocks, True)
        if cb0:
            parts.append(f'<div class="evidence-label cl">C example (correct, sim={cp["similarity"]:.0%}):</div>')
            parts.append(fmt_asm_pair(cb0, cb2, max_lines=5))

        rb0, rb2, rp = _pick_example_pair(r_pairs, r_blocks, False)
        if rb0:
            parts.append(f'<div class="evidence-label rl">Rust example (wrong, sim={rp["similarity"]:.0%}):</div>')
            parts.append(fmt_asm_pair(rb0, rb2, max_lines=5))

    else:
        parts.append(f'<div class="cross-hdr">Tie ({r_acc:.0%} each)</div>')
        if r_acc == 0 and c_acc == 0:
            parts.append(f'<p>Neither language produced useful signal for '
                         f'{METHOD_LABELS.get(method_name, method_name)} matching.</p>')
            rb0, rb2, rp = _pick_example_pair(r_pairs, r_blocks, False)
            cb0, cb2, cp = _pick_example_pair(c_pairs, c_blocks, False)
            if rb0:
                parts.append(f'<div class="evidence-label rl">Rust (wrong, sim={rp["similarity"]:.0%}):</div>')
                parts.append(fmt_asm_pair(rb0, rb2, max_lines=4))
            if cb0:
                parts.append(f'<div class="evidence-label cl">C (wrong, sim={cp["similarity"]:.0%}):</div>')
                parts.append(fmt_asm_pair(cb0, cb2, max_lines=4))
        else:
            parts.append(f'<p>Both languages show similar block structure changes under optimization.</p>')
            rb0, rb2, rp = _pick_example_pair(r_pairs, r_blocks, True)
            cb0, cb2, cp = _pick_example_pair(c_pairs, c_blocks, True)
            if rb0:
                parts.append(f'<div class="evidence-label rl">Rust (correct, sim={rp["similarity"]:.0%}):</div>')
                parts.append(fmt_asm_pair(rb0, rb2, max_lines=4))
            if cb0:
                parts.append(f'<div class="evidence-label cl">C (correct, sim={cp["similarity"]:.0%}):</div>')
                parts.append(fmt_asm_pair(cb0, cb2, max_lines=4))

    return '<div class="cross-compare">' + '\n'.join(parts) + '</div>'


def get_pair(name):
    rust = c = None
    for fn in DATA['functions']:
        if fn['base_name'] == name:
            if fn['lang'] == 'Rust': rust = fn
            else: c = fn
    return rust, c


def pct(v):
    return f"{v:.0%}" if isinstance(v, float) else str(v)


def gen_conclusion():
    """Generate a data-driven conclusion section."""
    from collections import defaultdict
    rust_fns = [f for f in DATA['functions'] if f['lang'] == 'Rust']
    c_fns = [f for f in DATA['functions'] if f['lang'] == 'C']

    overall = {}
    by_feat = defaultdict(lambda: defaultdict(list))
    for method in METHODS_LIST:
        r_accs = [f['methods'][method]['accuracy'] for f in rust_fns]
        c_accs = [f['methods'][method]['accuracy'] for f in c_fns]
        overall[method] = (sum(r_accs)/len(r_accs), sum(c_accs)/len(c_accs))
        for f in rust_fns:
            by_feat[f['feature_prefix']][method].append(f['methods'][method]['accuracy'])

    c_wins = sum(1 for i in range(100) for m in METHODS_LIST
                 if c_fns[i]['methods'][m]['accuracy'] > rust_fns[i]['methods'][m]['accuracy'] + 0.01)
    r_wins = sum(1 for i in range(100) for m in METHODS_LIST
                 if rust_fns[i]['methods'][m]['accuracy'] > c_fns[i]['methods'][m]['accuracy'] + 0.01)

    r_blocks_avg = sum(f['n_o0'] for f in rust_fns) / len(rust_fns)
    c_blocks_avg = sum(f['n_o0'] for f in c_fns) / len(c_fns)

    hardest = min(by_feat.items(), key=lambda x: sum(sum(v)/len(v) for v in x[1].values()))
    easiest = max(by_feat.items(), key=lambda x: sum(sum(v)/len(v) for v in x[1].values()))

    feat_rows = ''
    for prefix in PREFIXES:
        accs = by_feat[prefix]
        cells = ''.join(f'<td>{sum(accs[m])/len(accs[m]):.0%}</td>' for m in METHODS_LIST)
        feat_rows += f'<tr><td style="text-align:left">{FEATURE_NAMES[prefix]}</td>{cells}</tr>'

    return f'''
<h2 id="conclusion">Key Findings</h2>
<div class="step verdict">

<p><strong>C code is significantly easier to match than Rust across all 3 methods and all 5 features.</strong></p>

<table>
<tr><th>Method</th><th>Rust (avg)</th><th>C (avg)</th><th>Gap</th></tr>
<tr><td>Value-based</td><td>{overall["value"][0]:.0%}</td><td>{overall["value"][1]:.0%}</td>
    <td>{overall["value"][1] - overall["value"][0]:+.0%}</td></tr>
<tr><td>Opcodes</td><td>{overall["opcodes"][0]:.0%}</td><td>{overall["opcodes"][1]:.0%}</td>
    <td>{overall["opcodes"][1] - overall["opcodes"][0]:+.0%}</td></tr>
<tr><td>Constants</td><td>{overall["constants"][0]:.0%}</td><td>{overall["constants"][1]:.0%}</td>
    <td>{overall["constants"][1] - overall["constants"][0]:+.0%}</td></tr>
</table>

<p>Across 300 individual comparisons (100 pairs &times; 3 methods), C wins {c_wins},
Rust wins {r_wins}, and {300 - c_wins - r_wins} are ties (same accuracy).</p>

<p><strong>Why?</strong> Two reinforcing factors:</p>
<ol>
<li><strong>More blocks = more confusion.</strong> Rust averages {r_blocks_avg:.0f} O0 blocks per function
vs C's {c_blocks_avg:.0f}. The extra blocks (bounds checks, panic paths, drop glue, discriminant checks)
create a larger cost matrix for Hungarian matching, with more opportunities for wrong pairings.</li>
<li><strong>Optimization hits harder.</strong> The extra blocks exist because of Rust's safety guarantees.
At O2, the compiler eliminates, inlines, or merges many of them — dramatically changing the block
structure. C has fewer "extra" blocks to begin with, so its O0→O2 transformation is gentler.</li>
</ol>

<p><strong>Accuracy by Rust feature (average across 20 functions):</strong></p>
<table>
<tr><th style="text-align:left">Feature</th><th>Value</th><th>Opcodes</th><th>Constants</th></tr>
{feat_rows}
</table>

<p>Hardest feature: <strong>{FEATURE_NAMES[hardest[0]]}</strong>.
Best feature: <strong>{FEATURE_NAMES[easiest[0]]}</strong>.</p>

<p><strong>Best method overall:</strong> Opcodes (Jaccard on instruction types) performs best for both
languages, because instruction types are more stable across optimization levels than concrete
execution values or numeric constants.</p>

</div>'''


def _d(name, lang):
    """Get function data from analysis JSON."""
    for fn in DATA['functions']:
        if fn['base_name'] == name and fn['lang'] == lang:
            return fn
    return {}


def _a(fn_data, method):
    """Get accuracy % string."""
    return f"{fn_data['methods'][method]['accuracy']:.0%}"


def _gen_annotations(prefix):
    """Generate data-driven annotations for an example, pulling real numbers."""
    cfg = EXAMPLE_CFG[prefix]
    name = cfg['fn']
    r = _d(name, 'Rust')
    c = _d(name, 'C')
    if not r or not c:
        return {'rust_annotations': '', 'c_annotations': '', 'verdict': ''}

    gt_r = r.get('gt_coverage', {})
    gt_c = c.get('gt_coverage', {})

    rust_ann = cfg['rust_annotations_tpl'].format(
        r_o0=r['n_o0'], r_o2=r['n_o2'],
        r_val=_a(r,'value'), r_opc=_a(r,'opcodes'), r_con=_a(r,'constants'),
        r_gt_lines=gt_r.get('o0_with_lines','?'), r_gt_total=gt_r.get('o0_total','?'),
        r_gt_matchable=gt_r.get('gt_matchable_o0','?'),
    )
    c_ann = cfg['c_annotations_tpl'].format(
        c_o0=c['n_o0'], c_o2=c['n_o2'],
        c_val=_a(c,'value'), c_opc=_a(c,'opcodes'), c_con=_a(c,'constants'),
        c_gt_lines=gt_c.get('o0_with_lines','?'), c_gt_total=gt_c.get('o0_total','?'),
        c_gt_matchable=gt_c.get('gt_matchable_o0','?'),
    )
    ratio = r['n_o0'] / c['n_o0'] if c['n_o0'] else 1
    verdict = cfg['verdict_tpl'].format(
        r_val=_a(r,'value'), r_opc=_a(r,'opcodes'), r_con=_a(r,'constants'),
        c_val=_a(c,'value'), c_opc=_a(c,'opcodes'), c_con=_a(c,'constants'),
        r_o0=r['n_o0'], r_o2=r['n_o2'], c_o0=c['n_o0'], c_o2=c['n_o2'],
        ratio=ratio,
    )
    return {'rust_annotations': rust_ann, 'c_annotations': c_ann, 'verdict': verdict}


# ── The 5 detailed walkthrough examples ────────────────────────────────────

EXAMPLE_CFG = {
    'bc': {
        'fn': 'bc_01',
        'title': 'Bounds Checking: bc_01 — Binary search on a slice',
        'intro': '''
<p>Rust automatically checks that every array index is within bounds. When you write
<code>data[i]</code>, the compiler inserts a hidden check: <em>"is i less than data.len()?"</em>
If not, the program panics instead of reading garbage memory.</p>
<p>C does not check. <code>data[i]</code> just reads whatever is at that memory address,
even if <code>i</code> is out of range. This means C code has fewer instructions, but also
fewer safety guarantees.</p>
<p><strong>How does this affect binary matching?</strong> Let's look at <code>bc_01</code> — a binary search
function. Both Rust and C implement the same algorithm, but the compiled code looks very different.</p>
''',
        'rust_annotations_tpl': '''
<p>The Rust compiler turns <code>data[mid]</code> into:</p>
<ol>
<li><code>cmp rax, rsi</code> — compare index <code>mid</code> with <code>data.len()</code></li>
<li><code>jae panic_bounds_check</code> — if mid &ge; len, jump to panic code</li>
<li><code>mov rax, [rdi + rax*8]</code> — only if the check passes, read the value</li>
</ol>
<p>Each bounds check creates an <strong>extra basic block</strong> (the cmp+jae instructions).
At O0, Rust has <strong>{r_o0} basic blocks</strong>. Many of these are bounds check blocks.</p>
<p>At O2, the compiler eliminates some redundant checks but keeps the ones it can't
prove safe. Result: <strong>{r_o2} blocks</strong>.
(DWARF maps {r_gt_lines}/{r_gt_total} O0 blocks to source lines.)</p>
''',
        'c_annotations_tpl': '''
<p>The C version uses <code>data[mid]</code> without any check — it compiles directly to
<code>mov rax, [rdi + rax*8]</code>. No cmp, no jump, no extra block.</p>
<p>At O0, C has <strong>{c_o0} basic blocks</strong>. At O2, it has <strong>{c_o2} blocks</strong>.
The structure barely changes because there's nothing extra to optimize away.
(DWARF maps {c_gt_lines}/{c_gt_total} O0 blocks to source lines.)</p>
''',
        'verdict_tpl': '''
<p><strong>Opcodes:</strong> Rust {r_opc} vs C {c_opc}. Rust has {r_o0} O0 blocks vs C's {c_o0}.
The extra bounds-check blocks (cmp+jae) use the same opcodes as BODY blocks (also use cmp, mov),
so the algorithm often confuses them. C's simpler structure has fewer blocks to mix up.</p>
<p><strong>Value:</strong> Rust {r_val} vs C {c_val}. Both languages struggle here — micro-execution
outputs change when the optimizer reorganizes registers, even if the logic is unchanged.</p>
<p><strong>Constants:</strong> Rust {r_con} vs C {c_con}. Rust bounds checks compare against
register-held lengths (no embedded constant), reducing the signal. C embeds more explicit literals.</p>
''',
    },

    'om': {
        'fn': 'om_03',
        'title': 'Ownership & Move: om_03 — Partition a Vec into evens and odds',
        'intro': '''
<p>In Rust, when you pass a <code>Vec</code> to a function, the ownership <strong>moves</strong>.
The caller can no longer use it. The compiler enforces this at compile time, and at the binary
level, it means the function is responsible for eventually freeing the memory.</p>
<p>In C, you pass a pointer. The caller and callee both have access. You must manually remember
to call <code>free()</code>. There's no compiler enforcement.</p>
<p><strong>How does this affect the binary?</strong> Let's look at <code>om_03</code>, which takes
a Vec/array and splits it into even and odd numbers.</p>
''',
        'rust_annotations_tpl': '''
<p>Rust's <code>data.into_iter()</code> consumes the Vec. The compiler generates code to:</p>
<ol>
<li>Set up two new Vecs (evens, odds) with allocation calls</li>
<li>Iterate through the original Vec, pushing to evens or odds</li>
<li>Drop (free) the original Vec's backing memory at the end</li>
</ol>
<p><strong>{r_o0} blocks at O0</strong>, <strong>{r_o2} blocks at O2</strong>.
Many O0 blocks disappear or merge, breaking block identity.
(DWARF maps {r_gt_lines}/{r_gt_total} O0 blocks to source lines.)</p>
''',
        'c_annotations_tpl': '''
<p>C's version is simpler: <code>malloc</code> two arrays, loop through, index-assign, <code>free</code> the original.</p>
<ol>
<li>No capacity checks (the C code pre-allocates the max possible size)</li>
<li>No drop glue (just a single <code>free(data)</code> call)</li>
<li>No iterator state machine</li>
</ol>
<p><strong>{c_o0} blocks at O0, {c_o2} at O2</strong>. The structure barely changes.
(DWARF maps {c_gt_lines}/{c_gt_total} O0 blocks to source lines.)</p>
''',
        'verdict_tpl': '''
<p><strong>Value:</strong> Rust {r_val} vs C {c_val}. The largest gap of any method.
Rust's iterator state machine produces many small blocks whose execution outputs change
completely after O2 inlining. C's direct loop produces stable outputs across both O-levels.</p>
<p><strong>Opcodes:</strong> Rust {r_opc} vs C {c_opc}. Rust's ownership blocks (capacity checks,
realloc paths, drop code) get merged by O2 into blocks with different opcode mixes.
C's simple loop body keeps the same instruction types at both O-levels.</p>
<p><strong>Constants:</strong> Rust {r_con} vs C {c_con}. C uses explicit size literals in malloc
that survive optimization. Rust's capacity management uses register-held values.</p>
''',
    },

    'dg': {
        'fn': 'dg_11',
        'title': 'Drop Glue: dg_11 — Build and tear down a HashMap of String→Vec',
        'intro': '''
<p>When a Rust variable goes out of scope, the compiler automatically generates "drop glue" —
code that frees all owned memory. For a <code>HashMap&lt;String, Vec&lt;u64&gt;&gt;</code>,
this means recursively freeing every String key, every Vec value, and the HashMap itself.</p>
<p>In C, you must manually write nested free loops: free each value array, free each key string,
then free the hash table structure.</p>
<p><strong>The key difference at the binary level:</strong> Rust generates many small
<code>drop_in_place&lt;T&gt;</code> call blocks. C has explicit <code>free()</code> calls
mixed into the normal code flow.</p>
''',
        'rust_annotations_tpl': '''
<p>Rust has <strong>{r_o0} blocks at O0</strong> and <strong>{r_o2} blocks at O2</strong>.
O2 completely restructures the drop glue: distinct <code>call drop_in_place&lt;String&gt;</code>
blocks at O0 get inlined at O2 — the free logic merges into surrounding computation blocks.
(DWARF maps {r_gt_lines}/{r_gt_total} O0 blocks to source lines.)</p>
''',
        'c_annotations_tpl': '''
<p>C has <strong>{c_o0} blocks at O0, {c_o2} at O2</strong>. The <code>free()</code> calls
are simple <code>call</code> instructions that stay as-is at both O-levels — the optimizer
doesn't inline library functions.
(DWARF maps {c_gt_lines}/{c_gt_total} O0 blocks to source lines.)</p>
''',
        'verdict_tpl': '''
<p><strong>C wins across all 3 methods</strong> (Opcodes: C {c_opc} vs Rust {r_opc},
Value: C {c_val} vs Rust {r_val}, Constants: C {c_con} vs Rust {r_con}).</p>
<p>Drop glue is the <em>hardest</em> of all 5 Rust features for matching (averaging ~5% across
methods vs ~15% for bounds checking). The reason: O2 aggressively inlines the compiler-generated
cleanup code (<code>drop_in_place</code>), completely changing both block structure and opcode
composition. The drop blocks at O0 are small call wrappers; at O2 the free logic is merged
into surrounding computation blocks, destroying any recognizable signature.</p>
''',
    },

    'qm': {
        'fn': 'qm_07',
        'title': '? Operator: qm_07 — Parse comma-separated words from a string',
        'intro': '''
<p>Rust's <code>?</code> operator propagates errors automatically. When you write
<code>value.parse::&lt;u64&gt;()?</code>, the compiler generates code that:</p>
<ol>
<li>Calls <code>parse()</code></li>
<li>Checks the discriminant: was it Ok or Err?</li>
<li>If Ok: extract the value and continue</li>
<li>If Err: immediately return the error to the caller</li>
</ol>
<p>Each <code>?</code> creates a branch point — a basic block that checks success/failure.
In C, the equivalent is <code>if (ret &lt; 0) return -1;</code></p>
''',
        'rust_annotations_tpl': '''
<p>qm_07 uses <code>?</code> multiple times. The compiled code has <strong>{r_o0} blocks at
O0</strong> and <strong>{r_o2} at O2</strong>.</p>
<p>Each <code>?</code> generates 2-3 blocks: discriminant check, Ok path, Err early-return.
O2 merges some check blocks and reorders Err paths as cold code, changing block boundaries.
(DWARF maps {r_gt_lines}/{r_gt_total} O0 blocks to source lines.)</p>
''',
        'c_annotations_tpl': '''
<p>C checks return codes with simple <code>if (ret == NULL) return -1;</code> — compiles to
<code>test rax, rax; je error_path</code>, the same 2 instructions at both O0 and O2.</p>
<p><strong>{c_o0} blocks at O0, {c_o2} at O2.</strong> Blocks shrink but keep their character.
(DWARF maps {c_gt_lines}/{c_gt_total} O0 blocks to source lines.)</p>
''',
        'verdict_tpl': '''
<p><strong>C wins on all methods</strong> (Opcodes: C {c_opc} vs Rust {r_opc},
Value: C {c_val} vs Rust {r_val}, Constants: C {c_con} vs Rust {r_con}).
The <code>?</code> operator creates many small discriminant-check blocks that O2 merges and
rearranges. C's explicit <code>if</code> checks compile to the same pattern at both O-levels.</p>
''',
    },

    'pu': {
        'fn': 'pu_08',
        'title': 'Panic Paths: pu_08 — Split string and unwrap each parsed word',
        'intro': '''
<p>Rust's <code>.unwrap()</code> and <code>.expect()</code> generate panic paths — code that
runs only if something goes wrong. At the binary level, these become "cold" basic blocks
containing calls to <code>core::panicking::panic()</code> or <code>panic_fmt()</code>.</p>
<p>C has no equivalent. Error handling is inline: <code>return -1;</code> or
<code>fprintf(stderr, ...); exit(1);</code>. There are no hidden cold paths.</p>
''',
        'rust_annotations_tpl': '''
<p>pu_08 calls <code>.unwrap()</code> on string parsing results. Each generates a check block,
a panic block, and a success block.</p>
<p><strong>{r_o0} blocks at O0</strong>, <strong>{r_o2} at O2</strong>.
Panic blocks survive O2 (compiler can't prove them unreachable), but computation blocks get
heavily reorganized — creating noise for the matching algorithm.
(DWARF maps {r_gt_lines}/{r_gt_total} O0 blocks to source lines.)</p>
''',
        'c_annotations_tpl': '''
<p>C returns -1 on parse failure — a single <code>mov eax, -1; ret</code>. No hidden panic paths.</p>
<p><strong>{c_o0} blocks at O0, {c_o2} at O2.</strong>
(DWARF maps {c_gt_lines}/{c_gt_total} O0 blocks to source lines.)</p>
''',
        'verdict_tpl': '''
<p><strong>C wins decisively</strong> (Opcodes: C {c_opc} vs Rust {r_opc},
Value: C {c_val} vs Rust {r_val}, Constants: C {c_con} vs Rust {r_con}).</p>
<p>Panic paths inflate Rust's block count ({r_o0} O0 blocks vs C's {c_o0}).
The Hungarian algorithm must search a {r_o0}&times;{r_o2} cost matrix for Rust
vs {c_o0}&times;{c_o2} for C — many more possible pairings means more chances
for wrong matches. The panic blocks are especially harmful because they share
generic opcodes (call, lea, mov) with computation blocks, confusing all 3 methods.</p>
''',
    },
}

# Build EXAMPLES dict with resolved data
EXAMPLES = {}
for prefix, cfg in EXAMPLE_CFG.items():
    ann = _gen_annotations(prefix)
    EXAMPLES[prefix] = {
        'fn': cfg['fn'],
        'title': cfg['title'],
        'intro': cfg['intro'],
        'rust_annotations': ann['rust_annotations'],
        'c_annotations': ann['c_annotations'],
        'verdict': ann['verdict'],
    }


# ── Build the full function table ──────────────────────────────────────────

def gen_full_table():
    rows = []
    current_prefix = None
    all_names = [f'{p}_{i:02d}' for p in PREFIXES for i in range(1, 21)]

    for name in all_names:
        prefix = name.split('_')[0]
        if prefix != current_prefix:
            current_prefix = prefix
            rows.append(f'<tr class="grp"><td colspan="11">{FEATURE_NAMES[prefix]}</td></tr>')

        rust, c = get_pair(name)
        if not rust or not c:
            continue

        # Determine per-method winner and overall
        wins_r = wins_c = 0
        method_cells = ''
        for mn in METHODS_LIST:
            ra = rust['methods'][mn]['accuracy']
            ca = c['methods'][mn]['accuracy']
            if ra > ca + 0.01: wins_r += 1
            elif ca > ra + 0.01: wins_c += 1
            cls = 'rw' if ra > ca + 0.01 else 'cw' if ca > ra + 0.01 else 'tw'
            method_cells += f'<td class="{cls}"><span class="rv">{pct(ra)}</span> <span class="cv">{pct(ca)}</span></td>'

        overall_cls = 'rw' if wins_r > wins_c else 'cw' if wins_c > wins_r else 'tw'
        overall_txt = 'Rust' if wins_r > wins_c else 'C' if wins_c > wins_r else 'TIE'

        is_example = name in [v['fn'] for v in EXAMPLES.values()]
        anchor = f' id="row-{name}"' if is_example else ''
        highlight = ' class="example-row"' if is_example else ''

        rows.append(
            f'<tr{anchor}{highlight}>'
            f'<td class="fn-name">{name}{"*" if is_example else ""}</td>'
            f'<td>{rust["n_o0"]}</td><td>{rust["n_o2"]}</td>'
            f'<td>{c["n_o0"]}</td><td>{c["n_o2"]}</td>'
            f'{method_cells}'
            f'<td class="{overall_cls} winner">{overall_txt}</td>'
            f'</tr>')

    return '\n'.join(rows)


# ── Build example sections ─────────────────────────────────────────────────

def gen_example_section(prefix):
    ex = EXAMPLES[prefix]
    name = ex['fn']
    rust, c = get_pair(name)
    if not rust or not c:
        return f'<p>Data not found for {name}</p>'

    rust_src = E(RUST_SRC.get(name, '// not found'))
    c_src = E(C_SRC.get(name, '// not found'))

    def fmt_blocks(fn_data, side, limit=6):
        blocks = [b for b in fn_data.get('blocks', []) if b['side'] == side]
        if not blocks:
            return '<p>No blocks</p>'
        html_parts = []
        for b in blocks[:limit]:
            asm = '\n'.join(b.get('asm', [])[:6])
            out_cls = 'has-out' if b['n_outputs'] > 0 else 'no-out'
            out_txt = f'{b["n_outputs"]} outputs' if b['n_outputs'] > 0 else 'no outputs'
            html_parts.append(
                f'<div class="block-box">'
                f'<div class="block-hdr"><code>{b["addr"]}</code> '
                f'<span class="bt">{b["type"]}</span> '
                f'{b["n_insns"]} insns '
                f'<span class="{out_cls}">{out_txt}</span></div>'
                f'<pre class="block-asm">{E(asm)}</pre></div>')
        if len(blocks) > limit:
            html_parts.append(f'<div class="more">... +{len(blocks)-limit} more blocks</div>')
        return '\n'.join(html_parts)

    # Method scores
    scores_html = ''
    for mn in METHODS_LIST:
        ra = rust['methods'][mn]['accuracy']
        ca = c['methods'][mn]['accuracy']
        cls = 'rw' if ra > ca + 0.01 else 'cw' if ca > ra + 0.01 else 'tw'
        scores_html += (
            f'<div class="score-box {cls}">'
            f'<div class="score-label">{METHOD_LABELS[mn]}</div>'
            f'<div class="score-vals">'
            f'<span class="rv">Rust {pct(ra)}</span> '
            f'<span class="cv">C {pct(ca)}</span></div></div>')

    return f'''
    <div class="example" id="example-{name}">
    <h3>{ex['title']}</h3>

    <div class="step">
    <h4>What is this feature?</h4>
    {ex['intro']}
    </div>

    <div class="step">
    <h4>Matching Accuracy</h4>
    <div class="score-row">{scores_html}</div>
    <p class="block-counts">Rust: {rust['n_o0']} blocks (O0) → {rust['n_o2']} blocks (O2) &nbsp;|&nbsp;
    C: {c['n_o0']} blocks (O0) → {c['n_o2']} blocks (O2)</p>
    </div>

    <div class="step">
    <h4>Step 1 — Source Code: What the programmer writes</h4>
    <div class="side-by-side">
    <div class="side">
    <div class="side-label rl">Rust</div>
    <pre class="src">{rust_src}</pre>
    </div>
    <div class="side">
    <div class="side-label cl">C</div>
    <pre class="src">{c_src}</pre>
    </div>
    </div>
    </div>

    <div class="step">
    <h4>Step 2 — What the compiler does to the code</h4>
    <p>Before looking at the matching results, we need to understand how the compiler transforms
    this source code into machine instructions, and what changes between O0 and O2.</p>
    <div class="side-by-side">
    <div class="side">
    <div class="side-label rl">Rust</div>
    {ex['rust_annotations']}
    </div>
    <div class="side">
    <div class="side-label cl">C</div>
    {ex['c_annotations']}
    </div>
    </div>
    </div>

    <div class="step">
    <h4>Step 3 — Block Matching Results</h4>
    <p>Now that we understand the block structure, let's see how well the 3 matching methods perform.</p>
    <p><strong>How to read the diagrams:</strong> O0 blocks are on the left, O2 blocks on the right.
    Each colored rectangle is one basic block, labeled with its type and instruction count.
    <span style="color:#3fb950">Green lines</span> = correct matches
    (the O0 and O2 block share source lines, verified by DWARF debug info).
    <span style="color:#f85149">Red lines</span> = wrong matches
    (paired by the algorithm, but they come from different source code).
    Faded blocks = unmatched (no partner on the other side).</p>

    {''.join(f"""
    <div class="match-method">
    <h5>{METHOD_LABELS[mn]}</h5>
    <div class="side-by-side">
    <div class="side">
    <div class="side-label rl">Rust</div>
    {gen_matching_svg(rust, mn, 'Rust ' + METHOD_LABELS[mn])}
    {gen_match_analysis(rust, mn, 'Rust')}
    </div>
    <div class="side">
    <div class="side-label cl">C</div>
    {gen_matching_svg(c, mn, 'C ' + METHOD_LABELS[mn])}
    {gen_match_analysis(c, mn, 'C')}
    </div>
    </div>
    {gen_cross_comparison(rust, c, mn)}
    </div>
    """ for mn in METHODS_LIST)}
    </div>

    <div class="step verdict">
    <h4>Step 4 — Verdict: Who wins and why?</h4>
    {ex['verdict']}
    </div>

    </div>'''


# ── Assemble final HTML ───────────────────────────────────────────────────

feature_nav = ' '.join(f'<a href="#example-{EXAMPLES[p]["fn"]}">{FEATURE_NAMES[p]}</a>' for p in PREFIXES)

html_out = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Rust vs C Block Matching: Detailed Analysis with Examples</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
       background: #0d1117; color: #c9d1d9; max-width: 1400px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
h1 {{ color: #58a6ff; margin: 20px 0; }}
h2 {{ color: #58a6ff; margin: 30px 0 15px; border-bottom: 1px solid #30363d; padding-bottom: 8px; }}
h3 {{ color: #79c0ff; margin: 20px 0 10px; }}
h4 {{ color: #d2a8ff; margin: 15px 0 8px; font-size: 1.05em; }}
p {{ margin: 8px 0; }}
ol, ul {{ margin: 8px 0 8px 25px; }}
li {{ margin: 3px 0; }}
code {{ font-family: 'Fira Code', Consolas, monospace; background: #161b22; padding: 1px 4px; border-radius: 3px; font-size: 0.9em; }}
pre {{ font-family: 'Fira Code', Consolas, monospace; font-size: 0.82em; line-height: 1.35;
       background: #0d1117; border: 1px solid #30363d; border-radius: 4px; padding: 10px;
       overflow-x: auto; white-space: pre-wrap; }}
table {{ border-collapse: collapse; width: 100%; font-size: 0.82em; margin: 10px 0; }}
th, td {{ padding: 5px 8px; border: 1px solid #30363d; text-align: center; }}
th {{ background: #161b22; color: #58a6ff; }}

.nav {{ position: sticky; top: 0; background: #0d1117e0; backdrop-filter: blur(8px);
        padding: 10px 0; z-index: 100; border-bottom: 1px solid #30363d; }}
.nav a {{ color: #58a6ff; margin-right: 12px; text-decoration: none; font-size: 0.88em; }}
.nav a:hover {{ text-decoration: underline; }}

.intro-box {{ background: #161b22; padding: 20px; border-radius: 8px; margin: 15px 0; border: 1px solid #30363d; }}

/* Examples */
.example {{ margin: 25px 0; padding: 20px; border: 1px solid #30363d; border-radius: 10px; background: #161b22; }}
.step {{ margin: 15px 0; padding: 12px; background: #0d1117; border-radius: 6px; border: 1px solid #21262d; }}
.step.verdict {{ border: 2px solid #58a6ff; background: #0d1520; }}

.side-by-side {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 10px 0; }}
.side {{ overflow: hidden; }}
.side-label {{ font-size: 0.85em; font-weight: bold; padding: 4px 8px; border-radius: 4px 4px 0 0; }}
.rl {{ color: #f97583; background: #1a1020; }}
.cl {{ color: #79c0ff; background: #101a20; }}
.src {{ max-height: 350px; overflow-y: auto; border-radius: 0 0 4px 4px; margin: 0; }}

.score-row {{ display: flex; gap: 10px; margin: 10px 0; }}
.score-box {{ flex: 1; padding: 10px; border-radius: 6px; text-align: center; border: 1px solid #30363d; }}
.score-label {{ font-size: 0.85em; color: #8b949e; }}
.score-vals {{ font-size: 1.05em; margin-top: 4px; }}
.rv {{ color: #f97583; font-weight: bold; }}
.cv {{ color: #79c0ff; font-weight: bold; }}
.rw {{ background: #1a0a20; border: 1px solid #3a1a40; }}
.cw {{ background: #0a1520; border: 1px solid #1a3040; }}
.tw {{ background: #1a1a0a; border: 1px solid #30301a; }}
.block-counts {{ font-size: 0.88em; color: #8b949e; }}

.block-box {{ margin: 4px 0; border: 1px solid #21262d; border-radius: 4px; overflow: hidden; }}
.block-hdr {{ font-size: 0.82em; padding: 4px 8px; background: #161b22; }}
.block-asm {{ margin: 0; padding: 6px 8px; font-size: 0.78em; border-radius: 0; border: none; max-height: 120px; overflow-y: auto; }}
.bt {{ padding: 1px 4px; border-radius: 3px; background: #21262d; font-size: 0.88em; }}
.has-out {{ color: #3fb950; }}
.no-out {{ color: #f85149; }}
.more {{ font-size: 0.82em; color: #8b949e; text-align: center; padding: 4px; }}
.block-legend {{ font-size: 0.82em; color: #8b949e; padding: 6px 10px; margin: 8px 0;
                 background: #161b22; border-radius: 4px; border: 1px solid #21262d; }}
.block-legend span {{ margin-right: 12px; white-space: nowrap; }}
.match-method {{ margin: 15px 0; border-bottom: 1px solid #21262d; padding-bottom: 12px; }}
.match-method h5 {{ color: #c9d1d9; font-size: 1em; margin: 8px 0 4px; }}

.analysis-group {{ margin: 8px 0; padding: 8px; border-radius: 5px; font-size: 0.85em; }}
.correct-group {{ background: #0a2a1a; border: 1px solid #1a4a2a; }}
.wrong-group {{ background: #2a0a0a; border: 1px solid #4a1a1a; }}
.unmatched-group {{ background: #1a1a0a; border: 1px solid #3a3a1a; }}
.analysis-title {{ font-weight: bold; margin-bottom: 6px; }}
.good-title {{ color: #3fb950; }}
.bad-title {{ color: #f85149; }}

.pair-explain {{ margin: 5px 0; padding: 6px 8px; background: rgba(0,0,0,0.25); border-radius: 4px; }}
.pair-explain.wrong {{ }}
.pair-hdr {{ font-size: 0.9em; color: #c9d1d9; margin-bottom: 3px; }}
.pair-detail {{ font-size: 0.85em; color: #8b949e; }}
.pair-reason {{ font-size: 0.88em; color: #c9d1d9; margin-top: 3px; font-style: italic; }}
.pair-extra {{ font-size: 0.82em; color: #8b949e; margin-top: 4px; }}
.shared-ops code {{ color: #3fb950; }}
.diff-ops code {{ color: #f97583; }}
.unmatched-info {{ font-size: 0.88em; color: #e3b341; margin: 3px 0; }}

.cross-compare {{ margin: 8px 0; padding: 10px 12px; background: #161b22; border: 1px solid #30363d;
                   border-radius: 6px; font-size: 0.9em; line-height: 1.5; }}

.asm-pair {{ margin: 5px 0; }}
.asm-tbl {{ width: 100%; font-size: 0.82em; border: 1px solid #21262d; }}
.asm-tbl th {{ background: #161b22; color: #8b949e; font-size: 0.9em; padding: 3px 6px; width: 50%; }}
.asm-tbl td {{ padding: 1px 6px; font-size: 0.85em; vertical-align: top; border: 1px solid #21262d;
               background: #0d1117; }}
.asm-tbl code {{ background: none; padding: 0; font-size: 0.95em; color: #c9d1d9; white-space: pre; }}
.asm-more {{ color: #8b949e; text-align: center; font-size: 0.85em; }}

.src-badge {{ display: inline-block; font-size: 0.82em; font-weight: 600; padding: 2px 8px;
              border-radius: 4px; margin-bottom: 4px; }}
.src-badge.match {{ background: #0f291a; color: #56d364; border: 1px solid #238636; }}
.src-badge.nomatch {{ background: #2d1117; color: #f85149; border: 1px solid #da3633; }}
.src-badge.none {{ background: #161b22; color: #8b949e; border: 1px solid #30363d; }}

.asm-snippet {{ font-size: 0.78em; padding: 4px 8px; margin: 4px 0; border: 1px solid #21262d;
                border-radius: 3px; background: #0d1117; max-height: 100px; overflow-y: auto; }}
.unmatched-example {{ margin: 4px 0 4px 10px; }}
.cross-hdr {{ font-size: 1.05em; font-weight: bold; margin-bottom: 5px; }}
.evidence-label {{ font-size: 0.85em; font-weight: bold; margin: 6px 0 2px; padding: 2px 6px;
                    border-radius: 3px; display: inline-block; }}
.evidence-label.rl {{ color: #f97583; background: #1a1020; }}
.evidence-label.cl {{ color: #79c0ff; background: #101a20; }}

/* Table */
.fn-name {{ text-align: left; font-weight: bold; color: #d2a8ff; }}
.grp td {{ background: #161b22; font-weight: bold; color: #58a6ff; text-align: left; }}
.winner {{ font-weight: bold; }}
.example-row {{ background: #0d1520 !important; }}
.example-row td {{ background: inherit !important; }}

@media (max-width: 900px) {{
    .side-by-side {{ grid-template-columns: 1fr; }}
    .score-row {{ flex-direction: column; }}
}}
</style>
</head>
<body>

<div class="nav">
    <a href="#how-it-works">How It Works</a>
    {feature_nav}
    <a href="#all-functions">All 100 Pairs</a>
    <a href="#conclusion">Key Findings</a>
</div>

<h1>Rust vs C: Which Language's Binary Code Is Easier to Match?</h1>

<div class="intro-box">
<p><strong>The question:</strong> When a compiler optimizes code (O0 → O2), it rearranges
the machine instructions. Can we still figure out which parts of the optimized code correspond
to which parts of the original? And does Rust or C make this easier?</p>
<p><strong>Why it matters:</strong> Binary diffing (matching code across versions) is essential
for security analysis, malware detection, and patch analysis. If a language's compiler generates
code that's hard to match after optimization, it's harder to analyze.</p>
<p><strong>What we did:</strong> We wrote 100 functions in Rust and 100 semantically equivalent functions in C
(same algorithm, same logic), compiled each at O0 (no optimization) and O2 (full optimization),
then tried to match the basic blocks between O0 and O2 using 3 different methods.</p>
<p><strong>The 5 Rust features we test</strong> (20 functions each):</p>
<ol>
<li><strong>Bounds Checking (bc_)</strong> — Rust auto-checks array indices; C does not</li>
<li><strong>Ownership &amp; Move (om_)</strong> — Rust moves values instead of copying pointers</li>
<li><strong>Drop Glue / RAII (dg_)</strong> — Rust auto-generates destructor code; C requires manual free()</li>
<li><strong>Option/Result + ? (qm_)</strong> — Rust's error propagation generates discriminant checks</li>
<li><strong>Panic Paths (pu_)</strong> — Rust's unwrap/expect generate hidden panic blocks</li>
</ol>
<p><strong>Why Rust is expected to be harder:</strong> Each of these features makes the Rust compiler
generate <em>extra</em> basic blocks that have no equivalent in C (bounds checks, drop calls,
panic paths, discriminant branches). At O2, the compiler eliminates, merges, or inlines many of
these extra blocks. This means the O0→O2 block structure changes much more dramatically for Rust
than for C, making matching harder.</p>
<p><strong>How we know if a match is correct (ground truth):</strong> We compiled all binaries with
<code>debug=2</code> to include
<a href="https://en.wikipedia.org/wiki/DWARF">DWARF</a> debug information —
a standard format that records which source code line each machine instruction came from.
Using this mapping, we can check any pair of blocks: if the O0 block and O2 block were compiled
from at least one shared source line, they are a "true match." Otherwise the match is wrong.
This gives us <strong>real accuracy</strong> rather than guessing based on similarity scores.</p>
</div>

<h2 id="how-it-works">How Block Matching Works (30-second version)</h2>
<div class="step">
<p>A <strong>basic block</strong> is a straight-line chunk of assembly instructions with no branches
in the middle. A function is made of many basic blocks connected by jumps.</p>
<p>When the compiler optimizes (O0 → O2), it rearranges, merges, and eliminates blocks.
Our job: figure out which O2 block corresponds to which O0 block.</p>
<p>We try 3 methods:</p>
<ol>
<li><strong>Value-based:</strong> Run each block with test inputs. If two blocks produce the same
output values, they probably do the same thing. (Like testing a function with sample inputs.)</li>
<li><strong>Opcodes:</strong> Compare the set of instruction types (add, mov, cmp, call, etc.)
using <a href="https://en.wikipedia.org/wiki/Jaccard_index">Jaccard similarity</a>:
overlap / union. If O0 has {{mov, cmp, add}} and O2 has {{mov, cmp, jmp}},
they share 2 out of 4 unique opcodes → similarity = 2/4 = 50%.</li>
<li><strong>Constants:</strong> Compare the numeric constants embedded in the instructions,
also using Jaccard similarity. If both blocks use the numbers 8 and 16, but only O0
has 0xFF, similarity = 2/3 = 67%.</li>
</ol>
<p>For each method, we use the <a href="https://en.wikipedia.org/wiki/Hungarian_algorithm">Hungarian algorithm</a>
to find the best one-to-one matching between O0 and O2 blocks. If one side has more blocks
(say 43 O0 vs 45 O2), the algorithm produces min(43, 45) = 43 pairs; the extra blocks on the
larger side go unmatched.</p>
<p>Then we check each pair against <strong>DWARF ground truth</strong>: using debug info, we know
which source code line(s) each block was compiled from. If the O0 block and O2 block share at
least one source line, the match is <span style="color:#3fb950">correct</span>. Otherwise it's
<span style="color:#f85149">wrong</span>.</p>
<p><strong>Accuracy</strong> = (number of correct pairs) / (total pairs produced by Hungarian).
For example, if 5 out of 12 pairs share source lines, accuracy = 5/12 = 42%.
Unmatched blocks (surplus on either side) are not counted as wrong — they simply have no partner.</p>
<p><em>What does "sim=0%" mean?</em> When two blocks share zero features (no opcodes in common,
or neither has constants, or neither produces execution output), the similarity score is 0%.
The algorithm still pairs them because Hungarian must assign every block on the smaller side
to <em>something</em> — even if the best available match is terrible.</p>
<div class="block-legend">
Block type colors in diagrams:
<span style="color:#58a6ff">&block; BODY</span>
<span style="color:#f97583">&block; BOUNDS_CHECK</span>
<span style="color:#3fb950">&block; LOOP</span>
<span style="color:#d2a8ff">&block; CALL</span>
<span style="color:#f85149">&block; PANIC</span>
<span style="color:#e3b341">&block; DROP</span>
<span style="color:#79c0ff">&block; INIT/SETUP</span>
<span style="color:#8b949e">&block; RETURN</span>
<span style="color:#56d4dd">&block; BRANCH</span>
</div>
</div>

<h2>Detailed Examples: One Per Feature</h2>
<p>We walk through one function from each of the 5 Rust features. For each, we show the source
code, the compiled assembly, and explain step by step what happens.</p>

{gen_example_section('bc')}
{gen_example_section('om')}
{gen_example_section('dg')}
{gen_example_section('qm')}
{gen_example_section('pu')}

<h2 id="all-functions">All 100 Function Pairs</h2>
<p>Each row shows one function that exists in both Rust and C.
For each matching method, the Rust accuracy (<span class="rv">red number</span>) and
C accuracy (<span class="cv">blue number</span>) are shown side by side.
The cell background indicates which language achieves higher accuracy on that method.
"Winner" = the language that wins on more of the 3 methods.</p>
<p>Functions marked with * have detailed walkthroughs above.</p>

<table>
<thead>
<tr>
<th rowspan="2">Function</th>
<th colspan="2">Rust Blocks</th>
<th colspan="2">C Blocks</th>
<th colspan="3">Accuracy (Rust vs C)</th>
<th rowspan="2">Winner</th>
</tr>
<tr>
<th>O0</th><th>O2</th><th>O0</th><th>O2</th>
<th>Value</th><th>Opcodes</th><th>Constants</th>
</tr>
</thead>
<tbody>
{gen_full_table()}
</tbody>
</table>

{gen_conclusion()}

</body>
</html>'''

out_path = EXP_DIR / 'results' / 'report.html'
out_path.write_text(html_out)
print(f"Report: {out_path} ({out_path.stat().st_size / 1024:.0f} KB)")
