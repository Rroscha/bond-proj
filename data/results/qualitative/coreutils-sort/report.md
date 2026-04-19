# Rust Qualitative Block Analysis: coreutils-sort

## Overview

| Metric | Value |
|--------|-------|
| Groundtruth pairs | 200 |
| Analyzed (>= min_blocks) | 62 |
| Skipped | 138 |
| Mean block similarity | 0.946 |
| Mean blocks (O0 / O2) | 20.0 / 21.3 |

## Table 1: Feature Stability Summary

How well does each block feature survive O0→O2 optimization?

| feature | total_pairs | %STABLE | %DEGRADED | %DESTROYED | %EMPTY | mean_similarity |
|--------|--------|--------|--------|--------|--------|--------|
| opcodes | 1237 | 97.7 | 1.6 | 0.4 | 0.2 | 1.0 |
| constants | 1237 | 54.1 | 0.3 | 1.5 | 44.1 | 1.0 |
| concrete_values | 1237 | 64.5 | 3.6 | 5.4 | 26.5 | 0.9 |
| memory_pattern | 1237 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| dataflow_edges | 1237 | 99.9 | 0.0 | 0.0 | 0.1 | 1.0 |
| instruction_count | 1237 | 97.9 | 2.0 | 0.1 | 0.0 | 1.0 |
| callee_names | 1237 | 1.9 | 0.0 | 0.5 | 97.6 | 0.8 |
| string_refs | 1237 | 3.2 | 0.0 | 1.5 | 95.3 | 0.7 |

## Table 2: Block Type x Feature Heatmap

Mean per-feature similarity by O0 block type (higher = more stable).

| block_type | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs | count |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| BODY | 0.983 | 0.964 | 0.870 | - | 0.993 | 0.985 | 0.778 | 0.679 | 740 |
| BOUNDS_CHECK | 0.998 | 1.000 | 0.985 | - | 1.000 | 0.998 | - | 1.000 | 382 |
| EPILOGUE | 0.970 | 0.778 | 0.943 | - | 0.992 | 0.957 | - | - | 22 |
| ITERATOR_STATE | 0.981 | 0.949 | 1.000 | - | 1.000 | 0.978 | - | - | 27 |
| LOOP_HEADER | 0.990 | 0.972 | 0.944 | - | 0.994 | 0.992 | 1.000 | - | 62 |
| PANIC_PATH | 1.000 | 1.000 | 0.200 | - | 0.968 | 1.000 | - | 1.000 | 1 |
| PROLOGUE | - | - | - | - | 1.000 | 1.000 | - | - | 3 |

## Table 3: Rust Optimization Effect Impact

| effect | count | pct_affected | mean_block_sim_affected | mean_block_sim_unaffected |
|--------|--------|--------|--------|--------|
| BOUNDS_CHECK_ELIMINATION | 0 | 0.000 | - | 0.946 |
| LOOP_UNROLLING | 3 | 4.839 | 0.687 | 0.959 |
| DROP_GLUE_REMOVAL | 0 | 0.000 | - | 0.946 |
| PANIC_PATH_OPTIMIZATION | 0 | 0.000 | - | 0.946 |
| INLINING_EXPANSION | 3 | 4.839 | 0.687 | 0.959 |
| ITERATOR_LOWERING | 1 | 1.613 | 0.516 | 0.953 |
| BLOCK_MERGING | 1 | 1.613 | 0.658 | 0.951 |
| BLOCK_SPLITTING | 3 | 4.839 | 0.687 | 0.959 |

## Table 4: Feature Contribution by Similarity Tier

Mean per-feature similarity for functions grouped by overall block match quality.

| tier | num_functions | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| high (>0.7) | 56 | 0.994 | 0.991 | 0.917 | - | 0.997 | 0.995 | 0.923 | 0.714 |
| medium (0.4-0.7) | 6 | 0.610 | 0.125 | 0.182 | - | 0.912 | 0.630 | 0.000 | 0.000 |
| low (<0.4) | 0 | - | - | - | - | - | - | - | - |

## Top Function Drilldowns

### 1. `rayon::slice::sort::merge_sort`

- Addresses: O0=0x752db0, O2=0x656560
- Blocks: O0=3, O2=54
- Mean block similarity: 0.801
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 31 |
| BOUNDS_CHECK | 0 | 21 |
| ITERATOR_STATE | 0 | 1 |
| LOOP_HEADER | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x752e5d | 0x656620 | 0.90 | 1.00 | - | 0.00 (!) | - | 0.80 | 1.00 | 0.00 (!) | - |
| 0x752e25 | 0x656a70 | 0.84 | 0.67 (?) | - | 0.50 (?) | - | 0.89 | 1.00 | - | - |
| 0x752db0 | 0x656945 | 0.66 | 1.00 | 0.00 (!) | 0.00 (!) | - | 0.90 | 0.84 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 51 new (O2 only)

### 2. `num_bigint::biguint::shift::biguint_shl2`

- Addresses: O0=0xaeafb0, O2=0x73d870
- Blocks: O0=3, O2=27
- Mean block similarity: 0.745
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 23 |
| BOUNDS_CHECK | 0 | 4 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xaeb04f | 0x73da4e | 0.87 | 1.00 | - | 0.00 (!) | - | 0.95 | 0.67 (?) | - | - |
| 0xaeb00d | 0x73dbea | 0.72 | 0.50 (?) | - | 0.20 (!) | - | 0.86 | 0.90 | 0.00 (!) | - |
| 0xaeafb0 | 0x73d870 | 0.65 | 0.80 | 0.00 (!) | 0.20 (!) | - | 0.88 | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 24 new (O2 only)

### 3. `clap_builder::util::flat_map::Entry<K,V>::or_insert`

- Addresses: O0=0x9d7510, O2=0x6d1120
- Blocks: O0=3, O2=12
- Mean block similarity: 0.516
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 9 |
| BOUNDS_CHECK | 0 | 2 |
| DROP_GLUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x9d7586 | 0x6d11fc | 0.54 | 0.17 (!) | - | 0.14 (!) | - | 0.85 | 0.70 (?) | - | - |
| 0x9d7510 | 0x6d1120 | 0.53 | 0.43 (?) | 0.00 (!) | 0.17 (!) | - | 0.87 | 0.92 | - | - |
| 0x9d754b | 0x6d1152 | 0.48 | 0.29 (!) | 0.00 (!) | 0.08 (!) | - | 0.87 | 0.90 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 9 new (O2 only)

### 4. `gimli::read::rnglists::RngListIter<R>::next`

- Addresses: O0=0xb40b10, O2=0x77ae80
- Blocks: O0=145, O2=145
- Mean block similarity: 0.999

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 89 | 89 |
| BOUNDS_CHECK | 46 | 46 |
| ITERATOR_STATE | 5 | 5 |
| LOOP_HEADER | 4 | 4 |
| PROLOGUE | 1 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb40b10 | 0x77ae80 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb40bad | 0x77af1d | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb40bb8 | 0x77af28 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb40bdf | 0x77af4f | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb40be8 | 0x77af58 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb40c00 | 0x77af70 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb40c09 | 0x77af79 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb40c12 | 0x77af82 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |

### 5. `rayon_core::ThreadPoolBuildError::is_unsupported`

- Addresses: O0=0x80e030, O2=0x65e4a0
- Blocks: O0=3, O2=3
- Mean block similarity: 0.516
- Optimization effects: ITERATOR_LOWERING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 2 | 2 |
| BOUNDS_CHECK | 0 | 1 |
| ITERATOR_STATE | 1 | 0 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x80e030 | 0x65e4a0 | 0.59 | 0.50 (?) | 0.50 (?) | - | - | 1.00 | 0.40 (?) | - | - |
| 0x80e044 | 0x65e4a5 | 0.57 | 0.50 (?) | 0.00 (!) | 0.00 (!) | - | 0.87 | 1.00 | 0.00 (!) | 0.00 (!) |
| 0x80e083 | 0x65e4c4 | 0.38 | 0.20 (!) | 0.00 (!) | 1.00 | - | 1.00 | 0.40 (?) | - | - |

### 6. `std::io::default_read_exact`

- Addresses: O0=0xa09740, O2=0x5ea1d0
- Blocks: O0=9, O2=4
- Mean block similarity: 0.658
- Optimization effects: BLOCK_MERGING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 7 | 3 |
| EPILOGUE | 1 | 0 |
| LOOP_HEADER | 1 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xa097a4 | 0x5ea220 | 0.97 | 1.00 | - | 0.00 (!) | - | 0.94 | 1.00 | - | - |
| 0xa09842 | 0x5ea1e7 | 0.75 | 1.00 | - | 0.00 (!) | - | 0.89 | 0.43 (?) | - | 0.00 (!) |
| 0xa097d0 | 0x5ea1d0 | 0.48 | 0.40 (?) | 0.00 (!) | 0.00 (!) | - | 0.91 | 0.67 (?) | - | - |
| 0xa09850 | 0x5ea2ab | 0.43 | 0.60 (?) | 0.00 (!) | 1.00 | - | 0.89 | 0.30 (?) | - | - |

**Unmatched blocks:** 5 removed (O0 only), 0 new (O2 only)

### 7. `gimli::read::line::parse_attribute`

- Addresses: O0=0xb39da0, O2=0x774110
- Blocks: O0=125, O2=125
- Mean block similarity: 1.000

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 75 | 75 |
| BOUNDS_CHECK | 42 | 42 |
| EPILOGUE | 2 | 2 |
| ITERATOR_STATE | 2 | 2 |
| LOOP_HEADER | 4 | 4 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb39da0 | 0x774110 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb39dc4 | 0x774134 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb39dd5 | 0x774145 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb39df1 | 0x774161 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb39df6 | 0x774166 | 1.00 | 1.00 | 1.00 | - | - | 1.00 | 1.00 | - | - |
| 0xb39dfd | 0x77416d | 1.00 | 1.00 | 1.00 | - | - | 1.00 | 1.00 | - | - |
| 0xb39e08 | 0x774178 | 1.00 | 1.00 | 1.00 | - | - | 1.00 | 1.00 | - | - |
| 0xb39e11 | 0x774181 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |

### 8. `gimli::read::unit::skip_attributes`

- Addresses: O0=0xb3bf90, O2=0x776300
- Blocks: O0=101, O2=101
- Mean block similarity: 0.999

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 66 | 66 |
| BOUNDS_CHECK | 24 | 24 |
| ITERATOR_STATE | 2 | 2 |
| LOOP_HEADER | 9 | 9 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb3bf90 | 0x776300 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb3bfe0 | 0x776350 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3bff7 | 0x776367 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3c001 | 0x776371 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3c00b | 0x77637b | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3c018 | 0x776388 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3c020 | 0x776390 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb3c025 | 0x776395 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |

### 9. `gimli::read::index::UnitIndex<R>::parse`

- Addresses: O0=0xb3fd20, O2=0x77a090
- Blocks: O0=97, O2=97
- Mean block similarity: 1.000

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 58 | 58 |
| BOUNDS_CHECK | 26 | 26 |
| ITERATOR_STATE | 6 | 6 |
| LOOP_HEADER | 7 | 7 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb3fd20 | 0x77a090 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb3fd25 | 0x77a095 | 1.00 | 1.00 | 1.00 | - | - | 1.00 | 1.00 | - | - |
| 0xb3fd38 | 0x77a0a8 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3fd44 | 0x77a0b4 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3fd4e | 0x77a0be | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3fd5b | 0x77a0cb | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3fd61 | 0x77a0d1 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb3fda0 | 0x77a110 | 1.00 | 1.00 | 1.00 | - | - | 1.00 | 1.00 | - | - |

### 10. `gimli::read::unit::DebugInfoUnitHeadersIter<R>::next`

- Addresses: O0=0xb3cef0, O2=0x777260
- Blocks: O0=71, O2=71
- Mean block similarity: 1.000

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 39 | 39 |
| BOUNDS_CHECK | 24 | 24 |
| EPILOGUE | 1 | 1 |
| ITERATOR_STATE | 1 | 1 |
| LOOP_HEADER | 6 | 6 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb3cef0 | 0x777260 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3cef9 | 0x777269 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3cf0b | 0x77727b | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3cf2a | 0x77729a | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xb3cf30 | 0x7772a0 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3cf38 | 0x7772a8 | 1.00 | 1.00 | 1.00 | - | - | 1.00 | 1.00 | - | - |
| 0xb3cf40 | 0x7772b0 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb3cf64 | 0x7772d4 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
