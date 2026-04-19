#!/fs/ess/PAS1888/bond/bond-proj/.venv/bin/python
"""Diagnose why BFS only finds 1 block: trace successors."""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from rustdiff.loader import RustBinaryLoader

EXP_DIR = Path(__file__).resolve().parent
loader = RustBinaryLoader(str(EXP_DIR / 'rust_bench_O0'), load_debug_info=False, include_stdlib=False)

import re
name_re = re.compile(r'((?:bc|own|opt|iter|em)_\d{2})')
for addr, name in loader.get_all_functions():
    m = name_re.search(name)
    if m and m.group(1) == 'bc_05':
        func_addr = addr
        break

func = loader.be.fast_cfg.functions[func_addr]
print(f"bc_05 @ 0x{func_addr:x}")
print(f"func.block_addrs ({len(list(func.block_addrs))} total): {[hex(a) for a in sorted(func.block_addrs)[:10]]}...")
print()

# Trace BFS from entry
entry = func_addr
node = loader.be.get_fast_cfg_node(entry)
if node and node.block:
    insns = list(node.block.capstone.insns)
    print(f"Entry block 0x{entry:x}: {len(insns)} insns, size={node.block.size}")
    for i in insns:
        print(f"  0x{i.address:x}: {i.mnemonic} {i.op_str}")

    succs = loader.be.get_bb_successors(entry)
    print(f"\nSuccessors from get_bb_successors: {[hex(s) for s in succs]}")
    for s in succs:
        in_func = s in func.block_addrs_set
        print(f"  0x{s:x}: in function? {in_func}")
        snode = loader.be.get_fast_cfg_node(s)
        if snode:
            sfunc = loader.be.fast_cfg.functions.get(s)
            if sfunc:
                print(f"    -> this is the ENTRY of function: {sfunc.name}")
else:
    print("No block for entry node!")

# Also check angr's CFG model successors directly
print("\n--- Direct CFG model successors for entry ---")
cfg_node = loader.be.fast_cfg.model.get_any_node(entry)
if cfg_node:
    for s in cfg_node.successors:
        print(f"  -> 0x{s.addr:x} (in func? {s.addr in func.block_addrs_set})")

# Check second block
second_block = sorted(func.block_addrs)[1]
print(f"\nSecond block in function: 0x{second_block:x}")
succs2 = loader.be.get_bb_successors(second_block)
print(f"  Its successors: {[hex(s) for s in succs2]}")
for s in succs2:
    print(f"  0x{s:x}: in function? {s in func.block_addrs_set}")
