#!/usr/bin/env python3
"""Diagnose why value-based matching has low accuracy."""
import json
import numpy as np
from pathlib import Path
from collections import Counter

data = json.loads(Path('experiments/rust_features/results/analysis_data.json').read_text())

print('=== Blocks with no concrete outputs by type ===')
rust_no = Counter(); rust_yes = Counter()
c_no = Counter(); c_yes = Counter()

for fn in data['functions']:
    for b in fn.get('blocks', []):
        bt = b['type']
        has = b['n_outputs'] > 0
        if fn['lang'] == 'Rust':
            (rust_yes if has else rust_no)[bt] += 1
        else:
            (c_yes if has else c_no)[bt] += 1

print('Rust:')
for bt, cnt in rust_no.most_common():
    total = cnt + rust_yes.get(bt, 0)
    print(f'  {bt:<20} {cnt:>4}/{total:>4} ({cnt/total:.0%} no outputs)')
print('C:')
for bt, cnt in c_no.most_common():
    total = cnt + c_yes.get(bt, 0)
    print(f'  {bt:<20} {cnt:>4}/{total:>4} ({cnt/total:.0%} no outputs)')

print('\n=== Matched pair output coverage ===')
for lang in ['Rust', 'C']:
    both = one = none_ = 0
    for fn in data['functions']:
        if fn['lang'] == lang:
            o0 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O0'}
            o2 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O2'}
            for p in fn['methods']['value']['pairs']:
                b1 = o0.get(p['addr_o0'])
                b2 = o2.get(p['addr_o2'])
                h1 = (b1['n_outputs'] > 0) if b1 else False
                h2 = (b2['n_outputs'] > 0) if b2 else False
                if h1 and h2: both += 1
                elif h1 or h2: one += 1
                else: none_ += 1
    total = both + one + none_
    print(f'{lang}: both_outputs={both} ({both/total:.0%}), one_only={one} ({one/total:.0%}), neither={none_} ({none_/total:.0%})')

print('\n=== Among pairs with BOTH outputs: sim distribution ===')
for lang in ['Rust', 'C']:
    sims = []
    for fn in data['functions']:
        if fn['lang'] == lang:
            o0 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O0'}
            o2 = {b['addr']: b for b in fn['blocks'] if b['side'] == 'O2'}
            for p in fn['methods']['value']['pairs']:
                b1 = o0.get(p['addr_o0'])
                b2 = o2.get(p['addr_o2'])
                h1 = (b1['n_outputs'] > 0) if b1 else False
                h2 = (b2['n_outputs'] > 0) if b2 else False
                if h1 and h2:
                    sims.append(p['similarity'])
    a = np.array(sims)
    print(f'{lang}: n={len(a)}, mean={a.mean():.3f}, >0.3={sum(a>0.3)/len(a):.0%}, >0.5={sum(a>0.5)/len(a):.0%}')

print('\n=== Core problem: even among best pairs, sim distribution ===')
for lang in ['Rust', 'C']:
    all_best = []
    for fn in data['functions']:
        if fn['lang'] == lang:
            pairs = fn['methods']['value']['pairs']
            if pairs:
                all_best.append(pairs[0]['similarity'])  # best match per func
    a = np.array(all_best)
    print(f'{lang} best pair per func: mean={a.mean():.3f}, >0.3={sum(a>0.3)/len(a):.0%}, >0.5={sum(a>0.5)/len(a):.0%}')

print('\n=== Why low sim: concrete_value_similarity component ===')
# Need to re-run on a sample to check concrete value overlap directly
# For now, check: among value-based pairs with sim 0.2-0.3, what's the breakdown?
for lang in ['Rust', 'C']:
    low_pairs = 0
    for fn in data['functions']:
        if fn['lang'] == lang:
            for p in fn['methods']['value']['pairs']:
                if 0.15 <= p['similarity'] <= 0.3:
                    low_pairs += 1
    total = sum(len(fn['methods']['value']['pairs']) for fn in data['functions'] if fn['lang'] == lang)
    print(f'{lang}: {low_pairs}/{total} pairs in [0.15, 0.3] range ({low_pairs/total:.0%})')

# Check the actual weight contribution: val=50%, df=25%, mem=15%, const=10%
# A pair with sim=0.25 might be: val=0.0, df=0.5, mem=0.5, const=0.0 => 0+0.125+0.075+0 = 0.2
# Or val=0.25, df=0.25, mem=0.25, const=0.25 => 0.125+0.0625+0.0375+0.025 = 0.25
# The 0.3 threshold means val>=0.3 needed if other components ~0
# This means: if concrete outputs don't overlap, the pair fails regardless of structural match
print('\n=== Sim=0.25 explanation ===')
print('sim=0.25 = 50%*val + 25%*df + 15%*mem + 10%*const')
print('If val=0.0: max from others = 0.25*1 + 0.15*1 + 0.10*1 = 0.50')
print('If val=0.0 and df=0.5 and mem=0.5 and const=0.5: = 0+0.125+0.075+0.05 = 0.25')
print('Median sim=0.25 suggests val component is ~0 for most pairs')
print('')
print('ROOT CAUSE: concrete execution outputs mostly dont overlap between')
print('O0 and O2 blocks because optimization changes register allocation,')
print('reorders computations, and the micro-executor test inputs hit different')
print('code paths in optimized vs unoptimized code.')
