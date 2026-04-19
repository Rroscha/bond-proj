# Rust Qualitative Block Analysis: ripgrep

## Overview

| Metric | Value |
|--------|-------|
| Groundtruth pairs | 200 |
| Analyzed (>= min_blocks) | 53 |
| Skipped | 147 |
| Mean block similarity | 0.893 |
| Mean blocks (O0 / O2) | 23.0 / 24.1 |

## Table 1: Feature Stability Summary

How well does each block feature survive O0→O2 optimization?

| feature | total_pairs | %STABLE | %DEGRADED | %DESTROYED | %EMPTY | mean_similarity |
|--------|--------|--------|--------|--------|--------|--------|
| opcodes | 1124 | 91.6 | 5.2 | 2.8 | 0.4 | 0.9 |
| constants | 1124 | 52.3 | 0.7 | 3.1 | 43.9 | 0.9 |
| concrete_values | 1124 | 63.9 | 5.6 | 10.8 | 19.8 | 0.8 |
| memory_pattern | 1124 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| dataflow_edges | 1124 | 99.9 | 0.0 | 0.0 | 0.1 | 1.0 |
| instruction_count | 1124 | 94.8 | 4.4 | 0.7 | 0.0 | 1.0 |
| callee_names | 1124 | 3.2 | 0.0 | 1.0 | 95.8 | 0.8 |
| string_refs | 1124 | 2.8 | 0.0 | 2.6 | 94.6 | 0.5 |

## Table 2: Block Type x Feature Heatmap

Mean per-feature similarity by O0 block type (higher = more stable).

| block_type | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs | count |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| BODY | 0.935 | 0.916 | 0.798 | - | 0.986 | 0.961 | 0.756 | 0.517 | 690 |
| BOUNDS_CHECK | 0.981 | 0.988 | 0.882 | - | 0.995 | 0.988 | - | 1.000 | 322 |
| EPILOGUE | 0.848 | 0.571 | 0.833 | - | 0.982 | 0.948 | - | - | 17 |
| ITERATOR_STATE | 1.000 | 0.952 | 1.000 | - | 1.000 | 1.000 | - | - | 29 |
| LOOP_HEADER | 0.963 | 1.000 | 0.860 | - | 0.989 | 0.949 | 1.000 | 0.500 | 62 |
| PROLOGUE | - | - | - | - | 1.000 | 1.000 | - | - | 4 |

## Table 3: Rust Optimization Effect Impact

| effect | count | pct_affected | mean_block_sim_affected | mean_block_sim_unaffected |
|--------|--------|--------|--------|--------|
| BOUNDS_CHECK_ELIMINATION | 1 | 1.887 | 0.516 | 0.900 |
| LOOP_UNROLLING | 5 | 9.434 | 0.711 | 0.912 |
| DROP_GLUE_REMOVAL | 0 | 0.000 | - | 0.893 |
| PANIC_PATH_OPTIMIZATION | 0 | 0.000 | - | 0.893 |
| INLINING_EXPANSION | 6 | 11.321 | 0.684 | 0.919 |
| ITERATOR_LOWERING | 1 | 1.887 | 0.746 | 0.895 |
| BLOCK_MERGING | 5 | 9.434 | 0.698 | 0.913 |
| BLOCK_SPLITTING | 6 | 11.321 | 0.684 | 0.919 |

## Table 4: Feature Contribution by Similarity Tier

Mean per-feature similarity for functions grouped by overall block match quality.

| tier | num_functions | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| high (>0.7) | 43 | 0.966 | 0.964 | 0.849 | - | 0.992 | 0.981 | 0.837 | 0.533 |
| medium (0.4-0.7) | 10 | 0.486 | 0.158 | 0.215 | - | 0.911 | 0.609 | 0.000 | 0.000 |
| low (<0.4) | 0 | - | - | - | - | - | - | - | - |

## Top Function Drilldowns

### 1. `memchr::arch::x86_64::avx2::packedpair::Finder::find_impl`

- Addresses: O0=0xd1da70, O2=0x7fa120
- Blocks: O0=20, O2=130
- Mean block similarity: 0.712
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 15 | 49 |
| BOUNDS_CHECK | 2 | 55 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 0 | 11 |
| LOOP_HEADER | 2 | 9 |
| PROLOGUE | 0 | 6 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xd1dced | 0x7fa232 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xd1f291 | 0x7fa3ac | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xd1e461 | 0x7fa2af | 0.99 | 1.00 | - | 0.00 (!) | - | 0.98 | 1.00 | - | - |
| 0xd1f9f6 | 0x7fa35f | 0.99 | 1.00 | - | 0.00 (!) | - | 0.98 | 1.00 | - | - |
| 0xd1dcd7 | 0x7fa64e | 0.98 | 1.00 | - | 0.00 (!) | - | 0.94 | 1.00 | - | - |
| 0xd1f27b | 0x7fa6be | 0.98 | 1.00 | - | 0.00 (!) | - | 0.94 | 1.00 | - | - |
| 0xd1f05d | 0x7fa32f | 0.76 | 1.00 | - | 0.00 (!) | - | 0.89 | 0.40 (?) | - | - |
| 0xd1e472 | 0x7fa270 | 0.73 | 0.25 (!) | - | 1.00 | - | 0.99 | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 110 new (O2 only)

### 2. `miniz_oxide::inflate::core::decompress`

- Addresses: O0=0xd92b78, O2=0x8476e8
- Blocks: O0=351, O2=351
- Mean block similarity: 0.999

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 228 | 228 |
| BOUNDS_CHECK | 87 | 87 |
| ITERATOR_STATE | 15 | 15 |
| LOOP_HEADER | 21 | 21 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xd92b78 | 0x8476e8 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xd92bc8 | 0x847738 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xd92cbb | 0x84782b | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xd92cc8 | 0x847838 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |
| 0xd92cd4 | 0x847844 | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xd92cfa | 0x84786a | 1.00 | 1.00 | - | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xd92d09 | 0x847879 | 1.00 | 1.00 | 1.00 | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xd92d12 | 0x847882 | 1.00 | 1.00 | - | - | - | 1.00 | 1.00 | - | - |

### 3. `std::sync::mpmc::array::Channel<T>::disconnect_receivers`

- Addresses: O0=0x7755c0, O2=0x5f67a0
- Blocks: O0=6, O2=25
- Mean block similarity: 0.758
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 5 | 14 |
| BOUNDS_CHECK | 0 | 7 |
| DROP_GLUE | 0 | 1 |
| ITERATOR_STATE | 0 | 1 |
| LOOP_HEADER | 1 | 1 |
| PROLOGUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x775634 | 0x5f690a | 1.00 | 0.00 (!) | - | - | - | 1.00 | 1.00 | - | - |
| 0x775678 | 0x5f688f | 0.89 | 1.00 | - | 0.33 (?) | - | 0.94 | 0.75 | 0.00 (!) | - |
| 0x775636 | 0x5f67d7 | 0.76 | 0.75 | - | 1.00 | - | 1.00 | 0.56 (?) | - | - |
| 0x775660 | 0x5f6820 | 0.72 | 1.00 | 0.00 (!) | 0.00 (!) | - | 0.98 | 1.00 | 0.00 (!) | - |
| 0x775608 | 0x5f67c0 | 0.68 | 0.67 (?) | - | 0.17 (!) | - | 0.91 | 0.55 (?) | - | - |
| 0x7755c0 | 0x5f67a0 | 0.50 | 0.56 (?) | 0.00 (!) | 0.12 (!) | - | 0.90 | 0.68 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 19 new (O2 only)

### 4. `hashbrown::raw::RawTableInner::fallible_with_capacity`

- Addresses: O0=0xb09af0, O2=0x676290
- Blocks: O0=5, O2=14
- Mean block similarity: 0.603
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 11 |
| BOUNDS_CHECK | 0 | 3 |
| EPILOGUE | 1 | 0 |
| LOOP_HEADER | 1 | 0 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb09b94 | 0x67637a | 0.81 | 1.00 | - | 0.00 (!) | - | 0.96 | 0.50 (?) | 0.00 (!) | - |
| 0xb09b62 | 0x676290 | 0.67 | 0.20 (!) | - | 0.00 (!) | - | 0.88 | 1.00 | - | - |
| 0xb09bc1 | 0x6762c2 | 0.56 | 0.50 (?) | - | - | - | 1.00 | 0.20 (!) | - | - |
| 0xb09e90 | 0x6762dc | 0.53 | 0.20 (!) | 0.00 (!) | 1.00 | - | 1.00 | 1.00 | - | - |
| 0xb09af0 | 0x6762e5 | 0.44 | 0.17 (!) | 0.00 (!) | 0.06 (!) | - | 0.92 | 0.90 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 9 new (O2 only)

### 5. `std::thread::scoped::<impl std::thread::Builder>::spawn_scoped`

- Addresses: O0=0x96e7f0, O2=0x6d5630
- Blocks: O0=3, O2=8
- Mean block similarity: 0.677
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 7 |
| BOUNDS_CHECK | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x96e8bf | 0x6d5a19 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x96e87c | 0x6d5696 | 0.57 | 1.00 | 0.00 (!) | 0.00 (!) | - | 0.79 | 0.57 (?) | - | 0.00 (!) |
| 0x96e7f0 | 0x6d5654 | 0.46 | 0.60 (?) | 0.00 (!) | 0.17 (!) | - | 0.87 | 0.43 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 5 new (O2 only)

### 6. `crossbeam_deque::deque::Stealer<T>::steal_batch_with_limit_and_pop`

- Addresses: O0=0x985bc0, O2=0x6d8920
- Blocks: O0=3, O2=9
- Mean block similarity: 0.804
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 7 |
| BOUNDS_CHECK | 0 | 1 |
| LOOP_HEADER | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x985c0d | 0x6da181 | 0.98 | 1.00 | 1.00 | 0.20 (!) | - | 0.98 | 1.00 | - | 0.00 (!) |
| 0x985c26 | 0x6d92eb | 0.85 | 0.67 (?) | - | 0.00 (!) | - | 0.93 | 1.00 | 0.00 (!) | - |
| 0x985bc0 | 0x6d8920 | 0.59 | 0.60 (?) | 0.00 (!) | - | - | 1.00 | 0.82 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 6 new (O2 only)

### 7. `encoding_rs::iso_2022_jp::Iso2022JpDecoder::decode_to_utf8_raw`

- Addresses: O0=0x914130, O2=0x6a5690
- Blocks: O0=62, O2=13
- Mean block similarity: 0.746
- Optimization effects: ITERATOR_LOWERING, BLOCK_MERGING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 53 | 7 |
| BOUNDS_CHECK | 4 | 6 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 1 | 0 |
| LOOP_HEADER | 3 | 0 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x914454 | 0x6a5ec0 | 0.97 | 1.00 | 1.00 | 0.20 (!) | - | 0.96 | 1.00 | - | 0.00 (!) |
| 0x914212 | 0x6a56e5 | 0.85 | 0.75 | - | 0.50 (?) | - | 0.86 | 1.00 | - | 0.00 (!) |
| 0x9143b7 | 0x6a5dc4 | 0.84 | 1.00 | - | 1.00 | - | 0.97 | 0.56 (?) | - | - |
| 0x9142e1 | 0x6a56da | 0.80 | 0.50 (?) | - | 0.00 (!) | - | 0.94 | 1.00 | - | - |
| 0x914848 | 0x6a56dc | 0.75 | 0.67 (?) | - | 0.00 (!) | - | 0.94 | 0.67 (?) | - | - |
| 0x9142b5 | 0x6a56b5 | 0.75 | 0.60 (?) | 1.00 | 0.50 (?) | - | 0.92 | 0.50 (?) | - | - |
| 0x91442c | 0x6a56a1 | 0.72 | 0.25 (!) | 1.00 | 0.00 (!) | - | 1.00 | 0.67 (?) | - | - |
| 0x914440 | 0x6a56cd | 0.71 | 0.25 (!) | 1.00 | 0.00 (!) | - | 0.99 | 0.67 (?) | - | - |

**Unmatched blocks:** 49 removed (O0 only), 0 new (O2 only)

### 8. `regex_automata::dfa::sparse::State::pattern_id`

- Addresses: O0=0xb4e0b0, O2=0x728e70
- Blocks: O0=3, O2=5
- Mean block similarity: 0.550
- Optimization effects: BLOCK_SPLITTING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 3 |
| BOUNDS_CHECK | 0 | 1 |
| EPILOGUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb4e0d8 | 0x728e90 | 0.73 | 1.00 | - | 0.00 (!) | - | 0.77 | 0.50 (?) | - | - |
| 0xb4e11b | 0x728e81 | 0.48 | 0.00 (!) | 0.00 (!) | 0.00 (!) | - | 0.97 | 1.00 | - | - |
| 0xb4e0b0 | 0x728ea6 | 0.44 | 0.12 (!) | 0.50 (?) | 0.33 (?) | - | 0.87 | 0.40 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 2 new (O2 only)

### 9. `encoding_rs::utf_8::Utf8Decoder::decode_to_utf8_raw`

- Addresses: O0=0x8e9e10, O2=0x6a0450
- Blocks: O0=84, O2=53
- Mean block similarity: 0.742
- Optimization effects: BLOCK_MERGING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 62 | 30 |
| BOUNDS_CHECK | 17 | 20 |
| EPILOGUE | 1 | 0 |
| LOOP_HEADER | 4 | 3 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x8ea860 | 0x6a0698 | 0.97 | 1.00 | 1.00 | 0.33 (?) | - | 0.91 | 1.00 | - | - |
| 0x8ea8de | 0x6a066c | 0.97 | 1.00 | 1.00 | 0.33 (?) | - | 0.91 | 1.00 | - | - |
| 0x8eafb8 | 0x6a07aa | 0.97 | 1.00 | 1.00 | 0.00 (!) | - | 0.88 | 1.00 | - | - |
| 0x8ea540 | 0x6a08da | 0.96 | 1.00 | - | 0.00 (!) | - | 0.97 | 1.00 | - | - |
| 0x8ea786 | 0x6a063d | 0.95 | 1.00 | 1.00 | 0.33 (?) | - | 0.93 | 0.88 | - | - |
| 0x8ea896 | 0x6a06ec | 0.94 | 1.00 | 1.00 | 0.50 (?) | - | 0.92 | 0.88 | - | - |
| 0x8ea5eb | 0x6a0625 | 0.92 | 1.00 | 1.00 | 0.20 (!) | - | 0.97 | 0.75 | - | - |
| 0x8ea87d | 0x6a06a4 | 0.91 | 1.00 | 1.00 | 1.00 | - | 0.91 | 0.75 | - | - |

**Unmatched blocks:** 31 removed (O0 only), 0 new (O2 only)

### 10. `memmap2::os::MmapInner::map`

- Addresses: O0=0x8e0790, O2=0x69f240
- Blocks: O0=8, O2=6
- Mean block similarity: 0.516
- Optimization effects: BOUNDS_CHECK_ELIMINATION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 6 | 6 |
| BOUNDS_CHECK | 2 | 0 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x8e081a | 0x69f2b7 | 0.61 | 0.25 (!) | - | 0.18 (!) | - | 0.81 | 0.90 | 0.00 (!) | - |
| 0x8e0808 | 0x69f2a0 | 0.57 | 0.50 (?) | - | 0.00 (!) | - | 0.89 | 0.40 (?) | - | - |
| 0x8e07fe | 0x69f240 | 0.56 | 0.75 | - | 0.06 (!) | - | 0.84 | 0.19 (!) | - | - |
| 0x8e07ec | 0x69f268 | 0.56 | 0.33 (?) | 0.00 (!) | 0.00 (!) | - | 0.94 | 1.00 | - | - |
| 0x8e0812 | 0x69f286 | 0.43 | 0.25 (!) | 0.00 (!) | 0.06 (!) | - | 0.82 | 0.80 | 0.00 (!) | - |
| 0x8e0790 | 0x69f2ad | 0.37 | 0.30 (!) | 0.00 (!) | 0.41 (?) | - | 0.84 | 0.56 (?) | - | - |

**Unmatched blocks:** 2 removed (O0 only), 0 new (O2 only)
