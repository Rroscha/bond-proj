#!/fs/ess/PAS1888/bond/bond-proj/.venv/bin/python
"""Diagnose why Rust O0 functions show only 1 block."""
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from rustdiff.loader import RustBinaryLoader

FUNCS_TO_CHECK = ['bc_05', 'bc_01', 'bc_09', 'bc_03', 'em_01', 'iter_02', 'opt_01']

def diagnose(binary_path, label):
    print(f"\n{'='*70}")
    print(f"  {label}: {binary_path}")
    print(f"{'='*70}")
    loader = RustBinaryLoader(str(binary_path), load_debug_info=False, include_stdlib=False)
    funcs = loader.get_all_functions()

    import re
    name_re = re.compile(r'((?:bc|own|opt|iter|em)_\d{2})')

    name_to_addr = {}
    for addr, name in funcs:
        m = name_re.search(name)
        if m:
            base = m.group(1)
            if base in FUNCS_TO_CHECK:
                name_to_addr[base] = (addr, name)

    for base in sorted(FUNCS_TO_CHECK):
        if base not in name_to_addr:
            print(f"\n  {base}: NOT FOUND")
            continue
        addr, full_name = name_to_addr[base]
        func_obj = loader.be.fast_cfg.functions.get(addr)
        if func_obj is None:
            print(f"\n  {base} ({full_name}): NO CFG FUNCTION OBJECT")
            continue

        cfg_blocks = list(func_obj.block_addrs)
        bfs_blocks = loader.get_blocks_for_function(addr)
        cfg_graph = loader.get_cfg_for_function(addr)

        print(f"\n  {base} ({full_name}) @ 0x{addr:x}")
        print(f"    angr func.block_addrs: {len(cfg_blocks)}")
        print(f"    BFS get_blocks_for_function: {len(bfs_blocks)}")
        print(f"    CFG DiGraph nodes: {cfg_graph.number_of_nodes()}, edges: {cfg_graph.number_of_edges()}")

        # Show block details
        for blk_addr in sorted(cfg_blocks)[:15]:
            node = loader.be.get_fast_cfg_node(blk_addr)
            if node and node.block:
                insns = list(node.block.capstone.insns)
                succs = loader.be.get_bb_successors(blk_addr)
                # Show first few instructions
                insn_strs = [f"{i.mnemonic} {i.op_str}" for i in insns[:4]]
                if len(insns) > 4:
                    insn_strs.append(f"...+{len(insns)-4} more")
                print(f"    blk 0x{blk_addr:x}: {len(insns)} insns, {len(succs)} succs | {'; '.join(insn_strs)}")
            else:
                print(f"    blk 0x{blk_addr:x}: NO NODE/BLOCK")

        if len(cfg_blocks) > 15:
            print(f"    ... +{len(cfg_blocks)-15} more blocks")

        # Check function size
        if hasattr(func_obj, 'size'):
            print(f"    function size: {func_obj.size} bytes")

EXP_DIR = Path(__file__).resolve().parent

print("\n" + "="*70)
print("RUST O0 DIAGNOSIS")
print("="*70)
diagnose(EXP_DIR / 'rust_bench_O0', 'Rust O0')

print("\n" + "="*70)
print("RUST O2 DIAGNOSIS")
print("="*70)
diagnose(EXP_DIR / 'rust_bench_O2', 'Rust O2')

print("\n" + "="*70)
print("C O0 DIAGNOSIS")
print("="*70)
diagnose(EXP_DIR / 'c_bench_O0', 'C O0')
