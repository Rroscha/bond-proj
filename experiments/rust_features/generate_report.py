#!/usr/bin/env python3
"""Generate HTML report from analysis_data.json with diagnostic analysis."""
import json
import numpy as np
from pathlib import Path

EXP_DIR = Path(__file__).resolve().parent
DATA = json.loads((EXP_DIR / 'results' / 'analysis_data.json').read_text())

PREFIXES = ['om', 'dg', 'bc', 'qm', 'pu']
METHOD_NAMES = {'value': 'Value-based', 'opcodes': 'Opcodes', 'constants': 'Constants', 'size': 'Size'}
FEATURE_NAMES = DATA['features']


def compute_diagnostics():
    """Compute diagnostic statistics from the raw data."""
    diag = {}

    # Block output coverage
    rust_with = rust_without = c_with = c_without = 0
    for fn in DATA['functions']:
        for b in fn.get('blocks', []):
            has = b['n_outputs'] > 0
            if fn['lang'] == 'Rust':
                if has: rust_with += 1
                else: rust_without += 1
            else:
                if has: c_with += 1
                else: c_without += 1
    diag['rust_output_coverage'] = rust_with / (rust_with + rust_without)
    diag['c_output_coverage'] = c_with / (c_with + c_without)
    diag['rust_blocks_total'] = rust_with + rust_without
    diag['c_blocks_total'] = c_with + c_without

    # Matched pair output coverage
    for lang in ['Rust', 'C']:
        both = one = neither = 0
        for fn in DATA['functions']:
            if fn['lang'] != lang:
                continue
            o0 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O0'}
            o2 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O2'}
            for p in fn['methods']['value']['pairs']:
                b1 = o0.get(p['addr_o0'])
                b2 = o2.get(p['addr_o2'])
                h1 = (b1['n_outputs'] > 0) if b1 else False
                h2 = (b2['n_outputs'] > 0) if b2 else False
                if h1 and h2: both += 1
                elif h1 or h2: one += 1
                else: neither += 1
        total = both + one + neither
        key = lang.lower()
        diag[f'{key}_pairs_both'] = both
        diag[f'{key}_pairs_one'] = one
        diag[f'{key}_pairs_neither'] = neither
        diag[f'{key}_pairs_total'] = total
        diag[f'{key}_pairs_both_pct'] = both / total if total else 0

    # Sim distribution for pairs with both outputs
    for lang in ['Rust', 'C']:
        sims = []
        for fn in DATA['functions']:
            if fn['lang'] != lang:
                continue
            o0 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O0'}
            o2 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O2'}
            for p in fn['methods']['value']['pairs']:
                b1 = o0.get(p['addr_o0'])
                b2 = o2.get(p['addr_o2'])
                h1 = (b1['n_outputs'] > 0) if b1 else False
                h2 = (b2['n_outputs'] > 0) if b2 else False
                if h1 and h2:
                    sims.append(p['similarity'])
        a = np.array(sims) if sims else np.array([0])
        key = lang.lower()
        diag[f'{key}_both_mean'] = float(a.mean())
        diag[f'{key}_both_above30'] = float(np.sum(a > 0.3) / len(a))

    # Overall sim distribution
    for lang in ['Rust', 'C']:
        sims = []
        zero_count = 0
        for fn in DATA['functions']:
            if fn['lang'] != lang:
                continue
            for p in fn['methods']['value']['pairs']:
                sims.append(p['similarity'])
                if p['similarity'] < 0.01:
                    zero_count += 1
        a = np.array(sims) if sims else np.array([0])
        key = lang.lower()
        diag[f'{key}_all_mean'] = float(a.mean())
        diag[f'{key}_all_median'] = float(np.median(a))
        diag[f'{key}_all_above30'] = float(np.sum(a > 0.3) / len(a))
        diag[f'{key}_in_0_15_30'] = float(np.sum((a >= 0.15) & (a <= 0.3)) / len(a))

    # Avg block counts
    rust_o0 = [fn['n_o0'] for fn in DATA['functions'] if fn['lang'] == 'Rust']
    rust_o2 = [fn['n_o2'] for fn in DATA['functions'] if fn['lang'] == 'Rust']
    c_o0 = [fn['n_o0'] for fn in DATA['functions'] if fn['lang'] == 'C']
    c_o2 = [fn['n_o2'] for fn in DATA['functions'] if fn['lang'] == 'C']
    diag['rust_avg_o0'] = float(np.mean(rust_o0))
    diag['rust_avg_o2'] = float(np.mean(rust_o2))
    diag['c_avg_o0'] = float(np.mean(c_o0))
    diag['c_avg_o2'] = float(np.mean(c_o2))

    # Block type breakdown for no-output blocks
    from collections import Counter
    rust_no_by_type = Counter()
    c_no_by_type = Counter()
    for fn in DATA['functions']:
        for b in fn.get('blocks', []):
            if b['n_outputs'] == 0:
                if fn['lang'] == 'Rust':
                    rust_no_by_type[b['type']] += 1
                else:
                    c_no_by_type[b['type']] += 1
    diag['rust_no_output_types'] = dict(rust_no_by_type.most_common())
    diag['c_no_output_types'] = dict(c_no_by_type.most_common())

    return diag


DIAG = compute_diagnostics()

def winner_class(w):
    return 'rust-win' if w == 'Rust' else 'c-win' if w == 'C' else 'tie'

def pct(v):
    return f"{v:.0%}" if isinstance(v, float) else str(v)

def gen_summary_table():
    rows = []
    for prefix in PREFIXES:
        s = DATA['summary'][prefix]
        cells = [f'<td class="feature-name">{FEATURE_NAMES[prefix]}</td>']
        for mn in DATA['methods']:
            m = s['methods'][mn]
            cls = winner_class(m['winner'])
            cells.append(
                f'<td class="{cls}">'
                f'R:{pct(m["rust_accuracy"])} C:{pct(m["c_accuracy"])}'
                f'<br><small>{m["winner"]}</small></td>'
            )
        rows.append('<tr>' + ''.join(cells) + '</tr>')
    return '\n'.join(rows)

def gen_explanation_cards():
    cards = []
    for prefix in PREFIXES:
        s = DATA['summary'][prefix]
        methods_html = ''
        for mn in DATA['methods']:
            m = s['methods'][mn]
            cls = winner_class(m['winner'])
            methods_html += f'''
            <div class="method-card {cls}">
                <h4>{METHOD_NAMES[mn]}</h4>
                <div class="scores">Rust: {pct(m['rust_accuracy'])} ({m['rust_correct']}/{m['rust_total']})
                &nbsp;|&nbsp; C: {pct(m['c_accuracy'])} ({m['c_correct']}/{m['c_total']})</div>
                <p class="explanation">{m['explanation']}</p>
            </div>'''
        cards.append(f'''
        <div class="feature-section" id="feature-{prefix}">
            <h3>{FEATURE_NAMES[prefix]}</h3>
            <div class="method-grid">{methods_html}</div>
        </div>''')
    return '\n'.join(cards)

def gen_diagnostic_section():
    d = DIAG
    # Build block-type breakdown rows
    rust_type_rows = ''
    for bt, cnt in d['rust_no_output_types'].items():
        rust_type_rows += f'<tr><td>{bt}</td><td>{cnt}</td></tr>'
    c_type_rows = ''
    for bt, cnt in d['c_no_output_types'].items():
        c_type_rows += f'<tr><td>{bt}</td><td>{cnt}</td></tr>'

    return f'''
    <div class="diagnostic-section">

    <div class="diag-highlight">
    <h3>Root Cause: Why Value-Based Matching Scores Are Low</h3>
    <p>Value-based matching (concrete micro-execution outputs) shows <strong>Rust 25&ndash;31%</strong> vs
    <strong>C 25&ndash;47%</strong> accuracy. Three compounding problems explain this:</p>
    </div>

    <div class="diag-grid">

    <div class="diag-card problem">
    <h4>Problem 1: Register Allocation Diverges</h4>
    <p>O0 uses <code>arg0-arg3 + ret0</code> (5 registers). O2 uses up to 13 registers
    including callee-saved (<code>saved0-4, r10</code>) that don't exist in O0.</p>
    <p><code>concrete_value_similarity()</code> only compares <em>common</em> registers.
    When O2 spills key computations into registers O0 never uses, there's nothing to compare.</p>
    <div class="diag-stat">Empirically: only ~5&ndash;8% of (register, value) pairs overlap between O0 and O2 blocks.</div>
    </div>

    <div class="diag-card problem">
    <h4>Problem 2: 44% of Matched Pairs Lack Comparable Outputs</h4>
    <table class="diag-table">
    <tr><th></th><th>Both Have Outputs</th><th>One Side Only</th><th>Neither</th></tr>
    <tr><td class="lang-rust">Rust</td>
        <td>{d['rust_pairs_both']} ({d['rust_pairs_both_pct']:.0%})</td>
        <td>{d['rust_pairs_one']}</td>
        <td>{d['rust_pairs_neither']}</td></tr>
    <tr><td class="lang-c">C</td>
        <td>{d['c_pairs_both']} ({d['c_pairs_both_pct']:.0%})</td>
        <td>{d['c_pairs_one']}</td>
        <td>{d['c_pairs_neither']}</td></tr>
    </table>
    <p>Prologue, bounds-check-only, and call-only blocks produce no concrete outputs.
    Rust has more such blocks (31% BODY blocks lack outputs vs 18% in C).</p>
    </div>

    <div class="diag-card problem">
    <h4>Problem 3: Even Comparable Pairs Show Low Overlap</h4>
    <p>Among pairs where <em>both</em> blocks have concrete outputs:</p>
    <table class="diag-table">
    <tr><th></th><th>Mean Sim</th><th>Above 0.3 Threshold</th></tr>
    <tr><td class="lang-rust">Rust</td>
        <td>{d['rust_both_mean']:.3f}</td>
        <td>{d['rust_both_above30']:.0%}</td></tr>
    <tr><td class="lang-c">C</td>
        <td>{d['c_both_mean']:.3f}</td>
        <td>{d['c_both_above30']:.0%}</td></tr>
    </table>
    <p>O2 restructures computations (constant folding, loop invariant hoisting, operation merging),
    so even blocks computing the &ldquo;same thing&rdquo; produce different intermediate register values.</p>
    </div>

    <div class="diag-card stats">
    <h4>Overall Similarity Distribution</h4>
    <table class="diag-table">
    <tr><th></th><th>Mean</th><th>Median</th><th>&gt;0.3</th><th>In [0.15, 0.30]</th></tr>
    <tr><td class="lang-rust">Rust</td>
        <td>{d['rust_all_mean']:.3f}</td><td>{d['rust_all_median']:.3f}</td>
        <td>{d['rust_all_above30']:.0%}</td><td>{d['rust_in_0_15_30']:.0%}</td></tr>
    <tr><td class="lang-c">C</td>
        <td>{d['c_all_mean']:.3f}</td><td>{d['c_all_median']:.3f}</td>
        <td>{d['c_all_above30']:.0%}</td><td>{d['c_in_0_15_30']:.0%}</td></tr>
    </table>
    <p>Median sim = 0.25 means the 50%-weighted value component contributes ~0.
    The 0.25 comes entirely from dataflow (25%) + memory (15%) + constants (10%).</p>
    </div>

    <div class="diag-card stats">
    <h4>Block Count: Rust vs C</h4>
    <table class="diag-table">
    <tr><th></th><th>Avg O0 Blocks</th><th>Avg O2 Blocks</th><th>Ratio</th></tr>
    <tr><td class="lang-rust">Rust</td>
        <td>{d['rust_avg_o0']:.0f}</td><td>{d['rust_avg_o2']:.0f}</td>
        <td>{d['rust_avg_o0']/d['rust_avg_o2']:.2f}x</td></tr>
    <tr><td class="lang-c">C</td>
        <td>{d['c_avg_o0']:.0f}</td><td>{d['c_avg_o2']:.0f}</td>
        <td>{d['c_avg_o0']/d['c_avg_o2']:.2f}x</td></tr>
    </table>
    <p>Rust has 2.5&times; more blocks on average. More blocks = more pairwise comparisons
    = more noise in Hungarian matching = lower accuracy. O2 also eliminates/merges
    Rust safety blocks, creating large O0:O2 block count mismatches (up to 12:1).</p>
    </div>

    <div class="diag-card stats">
    <h4>Blocks Without Concrete Outputs (by Type)</h4>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div>
    <strong class="lang-rust">Rust</strong> ({d['rust_blocks_total']} total, {1-d['rust_output_coverage']:.0%} no outputs)
    <table class="diag-table"><tr><th>Type</th><th>Count</th></tr>{rust_type_rows}</table>
    </div>
    <div>
    <strong class="lang-c">C</strong> ({d['c_blocks_total']} total, {1-d['c_output_coverage']:.0%} no outputs)
    <table class="diag-table"><tr><th>Type</th><th>Count</th></tr>{c_type_rows}</table>
    </div>
    </div>
    </div>

    </div>

    <div class="diag-highlight takeaway">
    <h3>Why C Wins on Value-Based but Rust Wins on Size</h3>
    <p><strong>Value-based (C wins):</strong> C functions have fewer, simpler blocks (avg 14 vs 36).
    With fewer blocks, Hungarian matching has less noise. C's straightforward register usage
    means more output overlap survives O2 optimization.</p>
    <p><strong>Size (Rust wins):</strong> Rust's extra safety blocks (bounds checks, drop glue, panic paths)
    are small, fixed-pattern blocks whose instruction counts barely change between O0 and O2.
    They act as &ldquo;anchors&rdquo; for size-based matching. C lacks these anchors, and its core
    computation blocks change size more dramatically under O2.</p>
    </div>

    </div>'''


def gen_per_function_table():
    rows = []
    current_prefix = None
    for fn_data in sorted(DATA['functions'], key=lambda x: (x['feature_prefix'], x['base_name'], x['lang'])):
        prefix = fn_data['feature_prefix']
        if prefix != current_prefix:
            current_prefix = prefix
            rows.append(f'<tr class="group-header"><td colspan="8">{FEATURE_NAMES[prefix]}</td></tr>')

        cells = [
            f'<td>{fn_data["base_name"]}</td>',
            f'<td class="lang-{fn_data["lang"].lower()}">{fn_data["lang"]}</td>',
            f'<td>{fn_data["n_o0"]}</td>',
            f'<td>{fn_data["n_o2"]}</td>',
        ]
        for mn in DATA['methods']:
            m = fn_data['methods'][mn]
            acc = m['accuracy']
            cls = 'high' if acc >= 0.6 else 'mid' if acc >= 0.3 else 'low'
            cells.append(f'<td class="acc-{cls}">{pct(acc)}</td>')
        rows.append('<tr class="fn-row" data-name="' + fn_data['base_name'] + '" data-lang="' + fn_data['lang'] + '">' + ''.join(cells) + '</tr>')
    return '\n'.join(rows)

def gen_function_details():
    details = []
    for fn_data in DATA['functions']:
        name = fn_data['base_name']
        lang = fn_data['lang']
        detail_id = f"detail-{name}-{lang}"

        methods_detail = ''
        for mn in DATA['methods']:
            m = fn_data['methods'][mn]
            pair_rows = ''
            for p in m['pairs'][:15]:
                cls = 'correct' if p['is_correct'] else 'incorrect'
                pair_rows += f'''<tr class="{cls}">
                    <td>{p['addr_o0']}</td><td>{p['addr_o2']}</td>
                    <td>{p['similarity']:.3f}</td>
                    <td>{'Y' if p['is_correct'] else 'N'}</td></tr>'''
            methods_detail += f'''
            <div class="method-detail">
                <h5>{METHOD_NAMES[mn]}: {m['correct']}/{m['matched']} correct ({pct(m['accuracy'])})</h5>
                <table class="pair-table"><thead>
                <tr><th>O0 Block</th><th>O2 Block</th><th>Sim</th><th>Correct</th></tr>
                </thead><tbody>{pair_rows}</tbody></table>
            </div>'''

        block_rows = ''
        for b in fn_data.get('blocks', [])[:30]:
            asm_text = '<br>'.join(b.get('asm', [])[:8])
            block_rows += f'''<tr>
                <td>{b['side']}</td><td>{b['addr']}</td><td>{b['type']}</td>
                <td>{b['n_insns']}</td><td>{b['n_outputs']}</td>
                <td class="asm-cell"><code>{asm_text}</code></td></tr>'''

        details.append(f'''
        <div class="function-detail" id="{detail_id}" style="display:none">
            <h4>{name} ({lang}) — O0: {fn_data['n_o0']} blocks, O2: {fn_data['n_o2']} blocks</h4>
            <div class="methods-row">{methods_detail}</div>
            <details><summary>Block Details (first 30)</summary>
            <table class="block-table"><thead>
            <tr><th>Side</th><th>Addr</th><th>Type</th><th>#Insns</th><th>#Outputs</th><th>Assembly</th></tr>
            </thead><tbody>{block_rows}</tbody></table>
            </details>
        </div>''')
    return '\n'.join(details)

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Rust Feature Analysis: 4-Method Block Matching (100 Functions)</title>
<style>
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
       background: #0d1117; color: #c9d1d9; max-width: 1400px; margin: 0 auto; padding: 20px; }}
h1 {{ color: #58a6ff; margin: 20px 0 10px; font-size: 1.8em; }}
h2 {{ color: #58a6ff; margin: 30px 0 15px; font-size: 1.4em; border-bottom: 1px solid #30363d; padding-bottom: 8px; }}
h3 {{ color: #79c0ff; margin: 20px 0 10px; font-size: 1.2em; }}
h4 {{ color: #d2a8ff; margin: 10px 0 8px; }}
h5 {{ color: #c9d1d9; margin: 8px 0 5px; }}
p {{ line-height: 1.5; }}
table {{ border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 0.85em; }}
th, td {{ padding: 6px 10px; border: 1px solid #30363d; text-align: center; }}
th {{ background: #161b22; color: #58a6ff; }}
td {{ background: #0d1117; }}
.feature-name {{ text-align: left; font-weight: bold; }}
.rust-win {{ background: #1a3a2a !important; color: #3fb950; }}
.c-win {{ background: #3a1a1a !important; color: #f85149; }}
.tie {{ background: #2d2a1a !important; color: #d29922; }}
.acc-high {{ background: #1a3a2a !important; color: #3fb950; }}
.acc-mid {{ background: #2d2a1a !important; color: #d29922; }}
.acc-low {{ background: #3a1a1a !important; color: #f85149; }}
.lang-rust {{ color: #f97583; font-weight: bold; }}
.lang-c {{ color: #79c0ff; font-weight: bold; }}
.group-header td {{ background: #161b22; font-weight: bold; color: #58a6ff; text-align: left; font-size: 1.05em; }}
.correct {{ background: #1a2a1a !important; }}
.incorrect {{ background: #2a1a1a !important; }}
.method-grid {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 10px 0; }}
.method-card {{ padding: 12px; border-radius: 8px; border: 1px solid #30363d; }}
.method-card h4 {{ margin: 0 0 5px; }}
.scores {{ font-size: 0.95em; margin-bottom: 8px; }}
.explanation {{ font-size: 0.85em; color: #8b949e; }}
.feature-section {{ margin: 20px 0; padding: 15px; border: 1px solid #30363d; border-radius: 8px; background: #161b22; }}
.function-detail {{ margin: 10px 0; padding: 15px; border: 1px solid #30363d; border-radius: 8px; background: #161b22; }}
.methods-row {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }}
.method-detail {{ padding: 8px; }}
.pair-table {{ font-size: 0.8em; }}
.block-table {{ font-size: 0.78em; }}
.asm-cell {{ text-align: left; font-size: 0.82em; max-width: 400px; }}
code {{ font-family: 'Fira Code', monospace; font-size: 0.88em; }}
details {{ margin: 10px 0; }}
summary {{ cursor: pointer; color: #58a6ff; padding: 5px; }}
.fn-row {{ cursor: pointer; }}
.fn-row:hover {{ background: #161b22 !important; }}
.fn-row td {{ transition: background 0.2s; }}
.nav {{ position: sticky; top: 0; background: #0d1117; padding: 10px 0; z-index: 100; border-bottom: 1px solid #30363d; }}
.nav a {{ color: #58a6ff; margin-right: 15px; text-decoration: none; }}
.nav a:hover {{ text-decoration: underline; }}
.intro {{ background: #161b22; padding: 15px; border-radius: 8px; margin: 15px 0; border: 1px solid #30363d; }}
.intro p {{ margin: 5px 0; }}
.diagnostic-section {{ margin: 20px 0; }}
.diag-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin: 15px 0; }}
.diag-card {{ padding: 15px; border-radius: 8px; border: 1px solid #30363d; background: #161b22; }}
.diag-card.problem {{ border-left: 3px solid #f85149; }}
.diag-card.stats {{ border-left: 3px solid #58a6ff; }}
.diag-card h4 {{ color: #d2a8ff; margin: 0 0 8px; font-size: 1em; }}
.diag-card p {{ font-size: 0.88em; margin: 5px 0; color: #c9d1d9; }}
.diag-stat {{ background: #1a1a2a; padding: 8px 12px; border-radius: 4px; margin: 8px 0;
              font-size: 0.85em; color: #f0883e; border: 1px solid #30363d; }}
.diag-table {{ font-size: 0.82em; margin: 8px 0; }}
.diag-table th {{ background: #0d1117; padding: 4px 8px; }}
.diag-table td {{ padding: 4px 8px; }}
.diag-highlight {{ background: #161b22; padding: 18px; border-radius: 8px;
                   border: 1px solid #30363d; margin: 15px 0; }}
.diag-highlight h3 {{ color: #f85149; margin-bottom: 10px; }}
.diag-highlight.takeaway {{ border: 2px solid #58a6ff; }}
.diag-highlight.takeaway h3 {{ color: #58a6ff; }}
.diag-highlight p {{ font-size: 0.9em; margin: 8px 0; }}
@media (max-width: 900px) {{
    .method-grid, .methods-row, .diag-grid {{ grid-template-columns: 1fr; }}
}}
</style>
</head>
<body>
<div class="nav">
    <a href="#summary">Summary</a>
    <a href="#diagnostics">Diagnostics</a>
    <a href="#explanations">Explanations</a>
    <a href="#per-function">Per-Function</a>
    <a href="#details">Details</a>
</div>

<h1>Rust vs C: Block Matching Accuracy Across Optimization Levels</h1>

<div class="intro">
<p><strong>Experiment:</strong> 100 functions &times; 2 languages = 200 function pairs.
Each function pair is analyzed at O0 vs O2 using 4 independent block-matching methods.</p>
<p><strong>Features tested:</strong> Ownership &amp; Move, Drop Glue (RAII), Bounds Checking,
? Operator (Option/Result), Panic/Unwind Paths — 20 functions each.</p>
<p><strong>Methods:</strong> Value-based (concrete execution outputs), Opcodes (opcode set Jaccard),
Constants (constant set Jaccard), Size (instruction count ratio).</p>
<p><strong>Question:</strong> Which language's functions are easier to match across optimization levels,
and WHY does each Rust-specific feature help or hurt matching accuracy?</p>
</div>

<h2 id="summary">Feature &times; Method Summary</h2>
<table>
<thead><tr>
<th>Rust Feature</th>
{''.join(f'<th>{METHOD_NAMES[mn]}</th>' for mn in DATA['methods'])}
</tr></thead>
<tbody>
{gen_summary_table()}
</tbody>
</table>

<h2 id="diagnostics">Diagnostic Analysis: Why Value-Based Matching Is Low</h2>
{gen_diagnostic_section()}

<h2 id="explanations">Per-Feature Explanations</h2>
{gen_explanation_cards()}

<h2 id="per-function">Per-Function Accuracy</h2>
<p style="color:#8b949e;margin-bottom:10px">Click a row to expand block-level details.</p>
<table id="fn-table">
<thead><tr>
<th>Function</th><th>Lang</th><th>#O0</th><th>#O2</th>
{''.join(f'<th>{METHOD_NAMES[mn]}</th>' for mn in DATA['methods'])}
</tr></thead>
<tbody>
{gen_per_function_table()}
</tbody>
</table>

<h2 id="details">Function Details</h2>
{gen_function_details()}

<script>
document.querySelectorAll('.fn-row').forEach(row => {{
    row.addEventListener('click', () => {{
        const name = row.dataset.name;
        const lang = row.dataset.lang;
        const id = 'detail-' + name + '-' + lang;
        const el = document.getElementById(id);
        if (el) {{
            const isVisible = el.style.display !== 'none';
            el.style.display = isVisible ? 'none' : 'block';
            el.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}
    }});
}});
</script>
</body>
</html>'''

out_path = EXP_DIR / 'results' / 'report.html'
out_path.write_text(html)
print(f"Report written to {out_path}")
print(f"Size: {out_path.stat().st_size / 1024:.0f} KB")
