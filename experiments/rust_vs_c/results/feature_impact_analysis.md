# Rust Feature Impact on Binary Matching: Detailed Analysis

## Experiment Setup

- 100 functions (5 Rust features × 20 functions each)
- Each Rust function has a semantically equivalent C implementation
- Compiled at O0 and O2 with debug symbols
- Block-level feature extraction + Hungarian matching via RustDiff pipeline

## Summary Table

| Rust Feature | Rust Sim | C Sim | Δ(Rust−C) | Rust Blk Ratio | C Blk Ratio | Key Binary Effect |
|---|---|---|---|---|---|---|
| Slice Safety (Bounds Check) | 0.5697 | 0.6754 | −0.1056 | ×1.6 | ×0.7 | cmp+jcc guard blocks per index |
| Ownership + Drop (RAII) | 0.5704 | 0.6351 | −0.0647 | ×5.1 | ×1.1 | drop_in_place cleanup blocks |
| Option/Result (Sum Type) | 0.5756 | 0.6951 | −0.1195 | ×3.3 | ×0.8 | discriminant cmp+branch blocks |
| Iterator (State Machine) | 0.5029 | 0.6600 | −0.1571 | ×6.3 | ×0.9 | monomorphization → inline lowering |
| Enum Pattern Match | 0.6183 | 0.7413 | −0.1231 | ×0.8 | ×0.7 | exhaustive dispatch, no UB path |
| **Overall** | **0.5672** | **0.6814** | **−0.1142** | | | |

## Per-Feature Findings

### Feature 1: Slice Safety (Bounds Check)

**Rust mechanism:** `&[T]` carries a length field. Every `data[i]` access compiles to `cmp i, len; jae panic_path`. This generates a BOUNDS_CHECK basic block (cmp + conditional jump) before every array access.

**Binary effect:**
- Rust O2 generates **+41 new BOUNDS_CHECK blocks** that did not exist at O0
- BOUNDS_CHECK blocks comprise **23.8%** of all Rust O2 blocks in this category
- C has no compiler-generated bounds checks — raw pointer arithmetic only

**Impact on matching:** Δ = −0.106. The extra blocks at O2 that have no O0 counterpart dilute matching accuracy. However, `instruction_count` similarity is **+0.146 better** for Rust because bounds check blocks have stable, predictable instruction counts.

### Feature 2: Ownership + Drop (RAII)

**Rust mechanism:** When a `Vec`, `String`, or `Box` goes out of scope, the compiler inserts `drop_in_place<T>()` calls. At O0, functions with ownership typically compile to a single block that calls library functions. At O2, LLVM inlines the drop paths, generating cleanup blocks.

**Binary effect:**
- O0→O2 block explosion: **×5.1** (Rust) vs **×1.1** (C)
- 15/20 Rust O0 functions are single-block (entire function = one opaque call)
- O2 inlines Vec/String operations → many new BODY + BOUNDS_CHECK blocks

**Impact on matching:** Δ = −0.065 (smallest gap). The ownership feature causes moderate structural change. `callee_names` similarity drops to 0.000 for Rust (callees are inlined away at O2) vs 0.474 for C (explicit `free()` calls survive).

### Feature 3: Option/Result (Sum Type)

**Rust mechanism:** `Option<T>` and `Result<T,E>` are tagged enums. Every `match`, `unwrap`, `map`, `and_then` compiles to: load discriminant byte → cmp → conditional branch. This generates discriminant-check blocks.

**Binary effect:**
- Rust O0: most functions are 1-2 blocks (pattern matching at O0 is not lowered into separate blocks)
- Rust O2: explodes to 6.2 blocks on average — discriminant checks + payload access + error paths
- C uses simple return codes or NULL — no binary-visible discriminant

**Impact on matching:** Δ = −0.120. The `constants` similarity shows the largest gap: **Rust 0.182 vs C 0.695 (Δ = −0.513)**. This is because Rust's discriminant constants (0/1 for Some/None) are small and get mixed with other optimization constants, while C's sentinel values (like UINT64_MAX) are distinctive and survive optimization.

### Feature 4: Iterator (State Machine)

**Rust mechanism:** `.iter().map().filter().fold()` chains compile to monomorphized adapter structs at O0. At O2, LLVM aggressively inlines the entire chain into a single fused loop with bounds checks.

**Binary effect:**
- **Largest structural divergence**: O0→O2 block ratio = **×6.3** (vs ×0.9 for C)
- 17/20 Rust O0 functions have exactly 1 block
- O2 generates 10+ blocks per function: loop headers, bounds checks, iterator state blocks
- C explicit loops have stable structure across O0/O2

**Impact on matching:** Δ = −0.157 (largest gap). `opcodes` similarity is devastating: **Rust 0.221 vs C 0.542 (Δ = −0.321)**. The O0 single-block has completely different opcodes (call to adapter) vs O2 (arithmetic loop body with bounds checks).

### Feature 5: Enum Pattern Match

**Rust mechanism:** `match` on enums is exhaustive — every variant must be handled, no default/fallthrough. The compiler generates either jump tables or if-chains based on discriminant range. No UB paths exist.

**Binary effect:**
- O0→O2 ratio is moderate: ×0.8 (blocks actually decrease as O2 merges simple arms)
- DROP_GLUE blocks appear at O0 (5 blocks) for enums containing owned data (String, Vec), eliminated at O2
- C switch statements can have default/fallthrough, generating different dispatch patterns

**Impact on matching:** Δ = −0.123. This is where enum-specific DROP_GLUE blocks are observable. `constants` gap is large (Rust 0.249 vs C 0.542) because Rust discriminant values differ from the explicit tag values in C's `enum {...}`.

## Key Insight: O0 Monomorphization Collapse

The dominant effect across all features is **Rust O0's monomorphization collapse**: at O0, the compiler does not inline generic functions. Iterator chains, Option operations, and Vec methods all compile as calls to monomorphized generic instantiations, producing functions with 1-2 blocks. At O2, LLVM inlines everything, generating 5-20+ blocks with bounds checks, iterator state, and cleanup code.

This means:
1. **Rust O0↔O2 matching is inherently harder** than C O0↔O2 because the binary structure changes fundamentally
2. **Rust-specific block types (BOUNDS_CHECK, DROP_GLUE, ITERATOR_STATE) are predominantly O2 phenomena** — they barely exist at O0
3. **For same-optimization-level matching** (O2↔O2 across compiler versions), these anchor blocks would be an advantage

## Quantitative Feature Contribution

| Feature Dimension | Rust advantage | C advantage | Interpretation |
|---|---|---|---|
| `instruction_count` | +0.146 (bc), +0.076 (own) | | Bounds check blocks have stable instruction counts |
| `dataflow_edges` | ~0 | ~0 | Both languages have similar register dataflow stability |
| `opcodes` | | −0.321 (iter), −0.272 (bc) | Monomorphization collapse destroys opcode similarity |
| `constants` | | −0.513 (opt), −0.292 (em) | Discriminant values unstable across opt levels |
| `callee_names` | | −0.800 (opt), −0.474 (own) | Inlining at O2 removes callee information |
