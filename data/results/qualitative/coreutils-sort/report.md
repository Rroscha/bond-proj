# Rust Qualitative Block Analysis: coreutils-sort

## Overview

| Metric | Value |
|--------|-------|
| Groundtruth pairs | 200 |
| Analyzed (>= min_blocks) | 58 |
| Skipped | 142 |
| Mean block similarity | 0.918 |
| Mean blocks (O0 / O2) | 10.7 / 12.3 |

## Table 1: Feature Stability Summary

How well does each block feature survive O0→O2 optimization?

| feature | total_pairs | %STABLE | %DEGRADED | %DESTROYED | %EMPTY | mean_similarity |
|--------|--------|--------|--------|--------|--------|--------|
| opcodes | 615 | 92.2 | 4.1 | 3.3 | 0.5 | 0.9 |
| constants | 615 | 42.0 | 0.3 | 3.3 | 54.5 | 0.9 |
| concrete_values | 615 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| memory_pattern | 615 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| dataflow_edges | 615 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| instruction_count | 615 | 95.3 | 3.6 | 1.1 | 0.0 | 1.0 |
| callee_names | 615 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| string_refs | 615 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |

## Table 2: Block Type x Feature Heatmap

Mean per-feature similarity by O0 block type (higher = more stable).

| block_type | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs | count |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| BODY | 0.944 | 0.925 | - | - | - | 0.964 | - | - | 524 |
| EPILOGUE | 0.867 | 0.667 | - | - | - | 1.000 | - | - | 10 |
| ITERATOR_STATE | 0.973 | 0.917 | - | - | - | 0.973 | - | - | 28 |
| LOOP_HEADER | 1.000 | 1.000 | - | - | - | 1.000 | - | - | 50 |
| PROLOGUE | - | - | - | - | - | 1.000 | - | - | 3 |

## Table 3: Rust Optimization Effect Impact

| effect | count | pct_affected | mean_block_sim_affected | mean_block_sim_unaffected |
|--------|--------|--------|--------|--------|
| BOUNDS_CHECK_ELIMINATION | 0 | 0.000 | - | 0.918 |
| LOOP_UNROLLING | 5 | 8.621 | 0.497 | 0.958 |
| DROP_GLUE_REMOVAL | 0 | 0.000 | - | 0.918 |
| PANIC_PATH_OPTIMIZATION | 0 | 0.000 | - | 0.918 |
| INLINING_EXPANSION | 5 | 8.621 | 0.497 | 0.958 |
| ITERATOR_LOWERING | 1 | 1.724 | 0.199 | 0.931 |
| BLOCK_MERGING | 1 | 1.724 | 0.478 | 0.926 |
| BLOCK_SPLITTING | 5 | 8.621 | 0.497 | 0.958 |

## Table 4: Feature Contribution by Similarity Tier

Mean per-feature similarity for functions grouped by overall block match quality.

| tier | num_functions | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| high (>0.7) | 50 | 1.000 | 0.992 | - | - | - | 0.999 | - | - |
| medium (0.4-0.7) | 5 | 0.535 | 0.318 | - | - | - | 0.749 | - | - |
| low (<0.4) | 3 | 0.359 | 0.000 | - | - | - | 0.562 | - | - |

## Top Function Drilldowns

### 1. `rand_chacha::guts::refill_wide::impl_ssse3`

- Addresses: O0=0x8321b0, O2=0x663c20
- Blocks: O0=3, O2=11
- Mean block similarity: 0.199
- Optimization effects: ITERATOR_LOWERING, BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 2 | 10 |
| ITERATOR_STATE | 1 | 0 |
| LOOP_HEADER | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x8321b0 | 0x663c20 | 0.27 | 0.33 (?) | 0.00 (!) | - | - | - | 0.65 (?) | - | - |
| 0x8321e2 | 0x6641a0 | 0.17 | 0.00 (!) | 0.00 (!) | - | - | - | 0.69 (?) | - | - |
| 0x8321ce | 0x66412f | 0.16 | 0.25 (!) | 0.00 (!) | - | - | - | 0.25 (!) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 8 new (O2 only)

### 2. `rayon::slice::sort::merge_sort`

- Addresses: O0=0x752db0, O2=0x656560
- Blocks: O0=3, O2=54
- Mean block similarity: 0.731
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 49 |
| ITERATOR_STATE | 0 | 3 |
| LOOP_HEADER | 0 | 2 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x752e5d | 0x656620 | 0.85 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x752e25 | 0x656c2a | 0.76 | 1.00 | - | - | - | - | 0.67 (?) | - | - |
| 0x752db0 | 0x656945 | 0.58 | 1.00 | 0.00 (!) | - | - | - | 0.84 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 51 new (O2 only)

### 3. `num_bigint::biguint::multiplication::scalar_mul`

- Addresses: O0=0xaf8d20, O2=0x7353e0
- Blocks: O0=10, O2=24
- Mean block similarity: 0.483
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 9 | 22 |
| EPILOGUE | 1 | 2 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xaf8dcd | 0x735540 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xaf8e20 | 0x735492 | 0.70 | 0.60 (?) | 1.00 | - | - | - | 0.73 | - | - |
| 0xaf8d46 | 0x735451 | 0.58 | 0.50 (?) | - | - | - | - | 1.00 | - | - |
| 0xaf8ddf | 0x735550 | 0.45 | 0.25 (!) | - | - | - | - | 1.00 | - | - |
| 0xaf8d20 | 0x73545e | 0.45 | 0.50 (?) | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0xaf8d57 | 0x7354cb | 0.42 | 0.50 (?) | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0xaf8dd7 | 0x735448 | 0.38 | 0.33 (?) | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0xaf8d44 | 0x735450 | 0.33 | 0.00 (!) | - | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 14 new (O2 only)

### 4. `icu_locale_core::subtags::region::Region::try_from_utf8`

- Addresses: O0=0xaba540, O2=0x71ca00
- Blocks: O0=5, O2=16
- Mean block similarity: 0.530
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 5 | 12 |
| ITERATOR_STATE | 0 | 1 |
| LOOP_HEADER | 0 | 3 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xaba55e | 0x71ca3f | 0.71 | 1.00 | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0xaba6b7 | 0x71caf6 | 0.60 | 0.80 | 0.33 (?) | - | - | - | 0.75 | - | - |
| 0xaba540 | 0x71ca00 | 0.49 | 0.60 (?) | 0.25 (!) | - | - | - | 0.71 | - | - |
| 0xaba569 | 0x71cb0a | 0.44 | 0.67 (?) | 0.00 (!) | - | - | - | 0.75 | - | - |
| 0xaba578 | 0x71ca32 | 0.42 | 0.17 (!) | - | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 11 new (O2 only)

### 5. `bigdecimal::arithmetic::pow::pow_u64_with_context`

- Addresses: O0=0xad09b0, O2=0x72ba20
- Blocks: O0=6, O2=15
- Mean block similarity: 0.541
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 6 | 14 |
| LOOP_HEADER | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xad0ad2 | 0x72ba3a | 0.92 | 1.00 | - | - | - | - | 0.75 | - | - |
| 0xad0a37 | 0x72bbc1 | 0.64 | 0.67 (?) | - | - | - | - | 0.67 (?) | - | - |
| 0xad0a47 | 0x72bbf1 | 0.54 | 0.67 (?) | - | - | - | - | 0.38 (?) | - | - |
| 0xad09b0 | 0x72ba20 | 0.41 | 0.67 (?) | 0.00 (!) | - | - | - | 0.56 (?) | - | - |
| 0xad0a84 | 0x72bd3d | 0.40 | 0.67 (?) | 0.00 (!) | - | - | - | 0.55 (?) | - | - |
| 0xad0a42 | 0x72bb1f | 0.33 | 0.00 (!) | - | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 9 new (O2 only)

### 6. `rand_chacha::guts::init_chacha::impl_avx`

- Addresses: O0=0x828220, O2=0x663560
- Blocks: O0=13, O2=6
- Mean block similarity: 0.478
- Optimization effects: BLOCK_MERGING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 13 | 6 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x82844a | 0x6635a5 | 0.62 | 0.75 | - | - | - | - | 0.71 | - | - |
| 0x828332 | 0x663569 | 0.61 | 0.33 (?) | 1.00 | - | - | - | 0.83 | - | - |
| 0x82838e | 0x66356c | 0.55 | 0.60 (?) | 1.00 | - | - | - | 0.22 (!) | - | - |
| 0x828401 | 0x66357e | 0.39 | 0.14 (!) | - | - | - | - | 0.92 | - | - |
| 0x828220 | 0x663560 | 0.36 | 0.40 (?) | 0.50 (?) | - | - | - | 0.21 (!) | - | - |
| 0x8284a3 | 0x663579 | 0.33 | 0.00 (!) | - | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 7 removed (O0 only), 0 new (O2 only)

### 7. `miniz_oxide::inflate::core::init_tree`

- Addresses: O0=0xb52ef8, O2=0x78d188
- Blocks: O0=55, O2=55
- Mean block similarity: 1.000

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 40 | 40 |
| ITERATOR_STATE | 8 | 8 |
| LOOP_HEADER | 7 | 7 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb52ef8 | 0x78d188 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb52f69 | 0x78d1f9 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb52f77 | 0x78d207 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb52f81 | 0x78d211 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb52f8a | 0x78d21a | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb52fb1 | 0x78d241 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb52fc3 | 0x78d253 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb52fd5 | 0x78d265 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |

### 8. `alloc::vec::Vec<T,A>::dedup_by`

- Addresses: O0=0x8f9710, O2=0x6ae250
- Blocks: O0=17, O2=24
- Mean block similarity: 0.394

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 13 | 18 |
| EPILOGUE | 1 | 2 |
| ITERATOR_STATE | 0 | 2 |
| LOOP_HEADER | 3 | 2 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x8f9782 | 0x6ae283 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8f97ea | 0x6ae28f | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8f986d | 0x6ae2bf | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8f9879 | 0x6ae25b | 0.81 | 1.00 | - | - | - | - | 0.43 (?) | - | - |
| 0x8f9842 | 0x6ae347 | 0.49 | 0.40 (?) | - | - | - | - | 0.75 | - | - |
| 0x8f9710 | 0x6ae278 | 0.39 | 0.75 | 0.00 (!) | - | - | - | 0.27 (!) | - | - |
| 0x8f996d | 0x6ae35a | 0.38 | 0.33 (?) | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0x8f978e | 0x6ae25a | 0.33 | 0.00 (!) | - | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 7 new (O2 only)

### 9. `std::path::Components::as_path`

- Addresses: O0=0xb1e4f0, O2=0x758860
- Blocks: O0=50, O2=50
- Mean block similarity: 1.000

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 38 | 38 |
| ITERATOR_STATE | 4 | 4 |
| LOOP_HEADER | 7 | 7 |
| PROLOGUE | 1 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb1e4f0 | 0x758860 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb1e514 | 0x758884 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb1e535 | 0x7588a5 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb1e584 | 0x7588f4 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb1e58d | 0x7588fd | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb1e591 | 0x758901 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb1e595 | 0x758905 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb1e5a0 | 0x758910 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |

### 10. `core::num::dec2flt::decimal_seq::DecimalSeq::right_shift`

- Addresses: O0=0xb5a610, O2=0x7943e0
- Blocks: O0=38, O2=38
- Mean block similarity: 1.000

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 30 | 30 |
| EPILOGUE | 1 | 1 |
| ITERATOR_STATE | 2 | 2 |
| LOOP_HEADER | 5 | 5 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb5a610 | 0x7943e0 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb5a630 | 0x794400 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb5a635 | 0x794405 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb5a641 | 0x794411 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb5a65a | 0x79442a | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb5a65f | 0x79442f | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0xb5a67c | 0x79444c | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xb5a67e | 0x79444e | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
