# RustDiff: How Rust Language Features Affect Binary Block Matching

## Research Question

Which block-level matching features remain stable across compiler optimizations (O0 → O2), and how does Rust's safety overhead affect each feature compared to equivalent C?

Binary diffing is a key technique for security analysis, patch diffing, and malware comparison. Tools like BinDiff and Diaphora were designed with C/C++ binaries in mind. As Rust adoption grows in systems software, we need to understand whether existing matching features still work on Rust binaries.

## Experiment Setup

We wrote 100 Rust functions and 100 semantically equivalent C functions, covering 4 Rust-specific features (20 functions each):

| Feature | Rust Behavior | C Equivalent |
|---------|--------------|--------------|
| Bounds Checking (`bc_`) | `data[i]` inserts `cmp index, len; jae panic` | Raw pointer, no checks |
| Drop Glue (`dg_`) | Auto-generated `drop_in_place<T>` calls on scope exit | Manual `free()` calls |
| ? Operator (`qm_`) | Each `?` generates discriminant check + error-return block | Return code + `if` check |
| Panic / Unwrap (`pu_`) | `.unwrap()` generates check + panic block | Direct access, no panic |

Each function pair implements the same algorithm, differing only in language idiom.

**Compilation**: Both Rust and C are compiled at O0 (unoptimized) and O2 (optimized) with DWARF debug info enabled (`debug=2` / `-g`). Debug info does not affect optimization but provides source line mapping for ground truth validation.

**3 matching methods** (all standard in binary diffing):

1. **Value-based (micro-execution)**: Run each block with concrete test inputs via angr; compare register outputs, dataflow, memory patterns, constants. Weighted combination (Jaccard).
2. **Opcode Jaccard**: Compare instruction type sets — `|opcodes_O0 ∩ opcodes_O2| / |opcodes_O0 ∪ opcodes_O2|`.
3. **Constant Jaccard**: Compare embedded numeric constants — `|constants_O0 ∩ constants_O2| / |constants_O0 ∪ constants_O2|`.

**Matching**: For each function, build a similarity matrix between O0 and O2 blocks, then use the Hungarian algorithm to find the optimal 1-to-1 assignment. Accuracy = correct pairs / min(n_O0, n_O2).

**Ground truth**: Two blocks are "correctly matched" iff they share at least one DWARF source line.

## The Core Problem: Safety Blocks Look Too Similar

Rust's safety features generate large numbers of blocks that are nearly identical to each other — and to real computation blocks:

- **Bounds check blocks**: `cmp rax, rcx; jae panic` — all share opcodes {cmp, jcc, mov}
- **Drop glue blocks**: `lea rdi, [rsp+X]; call drop_in_place` — all share opcodes {lea, call}
- **Panic path blocks**: `lea rdi, [panic_msg]; call panic` — opcodes {lea, mov, call}, same as normal function calls
- **Error-return blocks** (from `?`): `mov ...; jmp epilogue` — all share opcodes {jmp, mov}

These blocks appear at high frequency. A single function with several `data[i]` accesses can generate 9+ identical bounds check blocks. A function with 6 uses of `?` generates 8 identical error-return blocks. The matcher cannot distinguish them from each other or from computation blocks.

## Example 1: Bounds Checking (bc_08)

**Rust source** (peak finding with prominence):
```rust
for i in 1..n-1 {
    if data[i] > data[i-1] && data[i] > data[i+1] {
        let mut left_min = data[i];
        for j in (0..i).rev() {
            if data[j] < left_min { left_min = data[j]; }
```

Every `data[x]` access inserts a bounds check: load index, load `slice.len()`, `cmp index, len`, `jae panic_handler`. If index < len, fall through to memory access. If index >= len, jump to panic.

**C source** (same algorithm): raw pointer access `data[i]` — no bounds checking at all.

**Result**: Rust O0 has 75 blocks (9 are bounds checks with identical opcodes {cmp, jcc, mov}). C O0 has 16 blocks, all diverse.

| Method | Rust | C |
|--------|------|---|
| Value | 11% | 25% |
| Opcodes | 32% | 42% |
| Constants | 11% | 25% |

## Example 2: ? Operator (qm_06)

**Rust source** (range + deviation calculation):
```rust
fn qm_06(data: &[u64]) -> Option<u64> {
    let first = data.first()?;    // ? generates 2 blocks
    let last = data.last()?;      // ? generates 2 blocks
    let mid = data.get(mid_idx)?; // ? generates 2 blocks
    let range = last.checked_sub(*first)?;
    // ... 6 uses of ? total
```

Each `?` generates a discriminant check block (is it None?) and an error-return block that jumps to the function epilogue. The error-return blocks all have identical opcodes {jmp, mov}.

**C source**: uses return code + out parameter — `if (n < 3) return 0;` — no Option, no `?`.

**Result**: Rust O0 has 49 blocks (8 identical error-return blocks, only 22% unique opcode sets). C has 9 O0 blocks, 89% unique.

| Method | Rust | C |
|--------|------|---|
| Value | 25% | 50% |
| Opcodes | 50% | 50% |
| Constants | 0% | 50% |

## Example 3: Panic Paths (pu_08)

**Rust source** (split + unwrap + char sum):
```rust
let parts: Vec<&str> = s.split_whitespace().collect();
let first = parts.first().unwrap(); // check + panic
let last = parts.last().unwrap();   // check + panic
let mid = parts.get(parts.len()/2).unwrap(); // check + panic
```

Each `.unwrap()` generates 2 blocks: a check block (`cmp rdx, 0; jne success`) and a panic block (`lea panic_msg; call panic`). The panic block uses opcodes {call, lea, mov} — the same opcodes as normal function call blocks like `collect()`. The matcher cannot distinguish panic blocks from real calls.

**C source**: direct array access with `strtok` — no `.unwrap()`, no panic paths.

**Result**: Rust O0 has 43 blocks with only 10 unique opcode sets. 11 blocks share {call, lea, mov} (panic + normal calls mixed). 12 blocks share {jmp, mov}.

| Method | Rust | C |
|--------|------|---|
| Value | 5% | 35% |
| Opcodes | 5% | 71% |
| Constants | 5% | 94% |

## Overall Results

C wins 288 out of 300 individual comparisons (100 function pairs × 3 methods).

| Feature | Rust Avg O0 Blocks | C Avg O0 Blocks | Value (R/C) | Opcodes (R/C) | Constants (R/C) |
|---------|-------------------|-----------------|-------------|---------------|-----------------|
| Bounds Checking | 37 | 13 | 10% / 46% | 24% / 58% | 10% / 62% |
| Drop Glue | 34 | 18 | 4% / 44% | 5% / 51% | 5% / 59% |
| ? Operator | 33 | 14 | 10% / 50% | 22% / 50% | 12% / 39% |
| Panic / Unwrap | 26 | 9 | 10% / 59% | 21% / 74% | 14% / 90% |
| **Average** | **33** | **14** | **7% / 48%** | **17% / 59%** | **9% / 64%** |

Key patterns:

- All Rust features hurt matching — safety blocks (bounds checks, error returns, panic paths) share the same opcodes
- Drop glue creates the most identical blocks — worst Rust accuracy (~5%)
- Opcodes is the best method overall — but still struggles when many blocks share the same instruction types
- C has no equivalent safety overhead → blocks are inherently more diverse → easier to match

## Findings

1. **Rust binaries are significantly harder to match than C.** C wins 288/300 comparisons. The gap ranges from 3× to 10× depending on feature and method.

2. **Root cause: safety blocks are too similar to each other and to computation blocks.** Bounds checks, drop glue, panic paths all use generic opcodes (cmp, call, lea, mov) — the same instructions used in real computation. High frequency + low diversity → wrong matches.

3. **Opcode Jaccard is the most robust method, but still limited.** When many blocks share the same opcode set, even the best method can't tell them apart.

5. **Possible direction: Rust-aware pre-filtering.** Identify safety blocks before matching (by call target, branch pattern) and handle them separately.

## Limitations

- Synthetic corpus — 100 hand-written function pairs may not represent all real-world patterns
- Single compiler (rustc 1.92.0 + gcc 11.4.1) — results may vary across toolchains
- Only O0 vs O2 — O1, Os, Oz not tested
- Block-level matching only — function-level matching not evaluated here
