#!/usr/bin/env python3
"""Check concrete value overlap directly on a few sample functions."""
import sys, warnings, logging
warnings.filterwarnings('ignore')
logging.disable(logging.WARNING)
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor
import re
import numpy as np

EXP_DIR = Path(__file__).resolve().parent
RUST_RE = re.compile(r'rust_features\d*::(\w+)')

def find_rust(loader, name):
    for addr, n in loader.get_all_functions():
        m = RUST_RE.search(n)
        if m and m.group(1) == name:
            return addr, n
    return None, None

print("Loading binaries...")
r0 = RustBinaryLoader(str(EXP_DIR / 'rust_O0'))
r2 = RustBinaryLoader(str(EXP_DIR / 'rust_O2'))
e0 = BlockMicroExecutor(r0)
e2 = BlockMicroExecutor(r2)

for fn_name in ['bc_01', 'om_01', 'pu_01', 'qm_01', 'dg_01']:
    a0, n0 = find_rust(r0, fn_name)
    a2, n2 = find_rust(r2, fn_name)
    if not a0 or not a2:
        continue

    sigs0 = e0.execute_function(a0)
    sigs2 = e2.execute_function(a2)

    print(f"\n{'='*60}")
    print(f"{fn_name}: O0={len(sigs0)} blocks, O2={len(sigs2)} blocks")

    # Check concrete output values
    o0_vals = set()
    o2_vals = set()
    o0_regs = set()
    o2_regs = set()
    o0_with_out = 0
    o2_with_out = 0
    for sig in sigs0.values():
        if sig.concrete_outputs:
            o0_with_out += 1
            for reg, vals in sig.concrete_outputs.items():
                o0_regs.add(reg)
                for v in vals:
                    o0_vals.add((reg, v))
    for sig in sigs2.values():
        if sig.concrete_outputs:
            o2_with_out += 1
            for reg, vals in sig.concrete_outputs.items():
                o2_regs.add(reg)
                for v in vals:
                    o2_vals.add((reg, v))

    overlap = o0_vals & o2_vals
    union = o0_vals | o2_vals
    print(f"  O0 blocks with outputs: {o0_with_out}/{len(sigs0)}")
    print(f"  O2 blocks with outputs: {o2_with_out}/{len(sigs2)}")
    print(f"  O0 unique (reg,val): {len(o0_vals)}, O2: {len(o2_vals)}")
    print(f"  Overlap: {len(overlap)}/{len(union)} ({len(overlap)/len(union):.0%})" if union else "  No values")
    print(f"  O0 regs: {sorted(o0_regs)}")
    print(f"  O2 regs: {sorted(o2_regs)}")

    # Show a few concrete outputs from each side
    print(f"  Sample O0 outputs:")
    for i, (addr, sig) in enumerate(sorted(sigs0.items())):
        if sig.concrete_outputs and i < 3:
            for reg, vals in list(sig.concrete_outputs.items())[:2]:
                print(f"    0x{addr:x} {reg}: {[hex(v) for v in vals[:5]]}")
    print(f"  Sample O2 outputs:")
    for i, (addr, sig) in enumerate(sorted(sigs2.items())):
        if sig.concrete_outputs and i < 3:
            for reg, vals in list(sig.concrete_outputs.items())[:2]:
                print(f"    0x{addr:x} {reg}: {[hex(v) for v in vals[:5]]}")
