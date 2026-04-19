#!/usr/bin/env python3
"""Debug script to test micro-execution on a small binary."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import rustdiff
from rustdiff.loader import RustBinaryLoader
from rustdiff.micro_exec.block_executor import BlockMicroExecutor

# Use the small toy corpus binary
bin_path = 'tmp/rust-corpus/testcrate-O0'
if not os.path.exists(bin_path):
    # Try coreutils if testcrate not built
    bin_path = 'tmp/coreutils-sort-O0'

print(f"Loading binary: {bin_path}")
loader = RustBinaryLoader(bin_path, load_debug_info=False)
executor = BlockMicroExecutor(loader)

# Get a few user functions
funcs = loader.get_analyzable_functions()[:10]
print(f"\nTesting {len(funcs)} functions:")

for addr, name in funcs:
    print(f"\n{'='*60}")
    print(f"Function: {name} @ 0x{addr:x}")

    blocks = loader.get_blocks_for_function(addr)
    print(f"  Blocks: {len(blocks)}")

    if not blocks:
        continue

    # Test first block
    block_addr, block = blocks[0]
    print(f"\n  Block 0x{block_addr:x}: {block.size} bytes, "
          f"{len(list(block.capstone.insns))} insns")

    # Show instructions
    for insn in list(block.capstone.insns)[:8]:
        print(f"    {insn.mnemonic:8s} {insn.op_str}")

    # Try micro-execution
    sig = executor.execute_block(block_addr, block)
    if sig is None:
        print("  -> execute_block returned None!")
        continue

    print(f"\n  Signature:")
    print(f"    opcodes: {sig.opcode_sequence}")
    print(f"    constants: {sig.constants}")
    print(f"    concrete_outputs: {sig.concrete_outputs}")
    print(f"    memory_pattern: {sig.memory_pattern}")
    print(f"    dataflow_edges: {sig.dataflow_edges}")
    print(f"    callee_names: {sig.callee_names}")
    print(f"    string_refs: {sig.string_refs}")
    print(f"    out_degree: {sig.out_degree}")

    # Also show feature set
    fset = sig.to_feature_set()
    print(f"\n    feature_set ({len(fset)} features):")
    by_tag = {}
    for f in fset:
        tag = f[0] if isinstance(f, tuple) else str(f)
        by_tag.setdefault(tag, []).append(f)
    for tag, feats in sorted(by_tag.items()):
        print(f"      {tag}: {len(feats)} features")
        for feat in feats[:3]:
            print(f"        {feat}")
        if len(feats) > 3:
            print(f"        ... ({len(feats) - 3} more)")
