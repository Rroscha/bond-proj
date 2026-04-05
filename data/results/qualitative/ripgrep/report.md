# Rust Qualitative Block Analysis: ripgrep

## Overview

| Metric | Value |
|--------|-------|
| Groundtruth pairs | 200 |
| Analyzed (>= min_blocks) | 54 |
| Skipped | 146 |
| Mean block similarity | 0.828 |
| Mean blocks (O0 / O2) | 18.5 / 26.8 |

## Table 1: Feature Stability Summary

How well does each block feature survive O0→O2 optimization?

| feature | total_pairs | %STABLE | %DEGRADED | %DESTROYED | %EMPTY | mean_similarity |
|--------|--------|--------|--------|--------|--------|--------|
| opcodes | 926 | 84.2 | 11.8 | 3.7 | 0.3 | 0.9 |
| constants | 926 | 39.4 | 1.5 | 10.9 | 48.2 | 0.8 |
| concrete_values | 926 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| memory_pattern | 926 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| dataflow_edges | 926 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| instruction_count | 926 | 87.3 | 10.3 | 2.5 | 0.0 | 0.9 |
| callee_names | 926 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |
| string_refs | 926 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 |

## Table 2: Block Type x Feature Heatmap

Mean per-feature similarity by O0 block type (higher = more stable).

| block_type | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs | count |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| BODY | 0.901 | 0.781 | - | - | - | 0.914 | - | - | 782 |
| EPILOGUE | 0.676 | 0.250 | - | - | - | 0.804 | - | - | 16 |
| ITERATOR_STATE | 0.960 | 0.771 | - | - | - | 0.956 | - | - | 47 |
| LOOP_HEADER | 0.926 | 0.845 | - | - | - | 0.964 | - | - | 78 |
| PROLOGUE | - | - | - | - | - | 1.000 | - | - | 3 |

## Table 3: Rust Optimization Effect Impact

| effect | count | pct_affected | mean_block_sim_affected | mean_block_sim_unaffected |
|--------|--------|--------|--------|--------|
| BOUNDS_CHECK_ELIMINATION | 0 | 0.000 | - | 0.828 |
| LOOP_UNROLLING | 8 | 14.815 | 0.583 | 0.870 |
| DROP_GLUE_REMOVAL | 0 | 0.000 | - | 0.828 |
| PANIC_PATH_OPTIMIZATION | 0 | 0.000 | - | 0.828 |
| INLINING_EXPANSION | 8 | 14.815 | 0.568 | 0.873 |
| ITERATOR_LOWERING | 4 | 7.407 | 0.517 | 0.852 |
| BLOCK_MERGING | 4 | 7.407 | 0.528 | 0.852 |
| BLOCK_SPLITTING | 8 | 14.815 | 0.568 | 0.873 |

## Table 4: Feature Contribution by Similarity Tier

Mean per-feature similarity for functions grouped by overall block match quality.

| tier | num_functions | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| high (>0.7) | 37 | 0.992 | 0.966 | - | - | - | 0.987 | - | - |
| medium (0.4-0.7) | 15 | 0.621 | 0.237 | - | - | - | 0.702 | - | - |
| low (<0.4) | 2 | 0.474 | 0.000 | - | - | - | 0.584 | - | - |

## Top Function Drilldowns

### 1. `encoding_rs::shift_jis::ShiftJisDecoder::decode_to_utf8_raw`

- Addresses: O0=0x903090, O2=0x6a5ef0
- Blocks: O0=100, O2=175
- Mean block similarity: 0.570
- Optimization effects: ITERATOR_LOWERING, BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 96 | 149 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 2 | 6 |
| LOOP_HEADER | 1 | 19 |
| PROLOGUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x903235 | 0x6a6196 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x903d82 | 0x6a63ab | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x903dc3 | 0x6a6180 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x903dd5 | 0x6a6714 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x903f5d | 0x6a685a | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x904034 | 0x6a6904 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x904282 | 0x6a5fb4 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0x9042df | 0x6a5f8e | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 75 new (O2 only)

### 2. `encoding_rs::gb18030::Gb18030Decoder::decode_to_utf8_raw`

- Addresses: O0=0x8ec620, O2=0x6a2930
- Blocks: O0=15, O2=241
- Mean block similarity: 0.701
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 13 | 195 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 0 | 24 |
| LOOP_HEADER | 1 | 21 |
| PROLOGUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x8ec74d | 0x6a2ae0 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8ec75f | 0x6a29f4 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8ec7f6 | 0x6a2af6 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8ec7c8 | 0x6a2a0f | 0.94 | 1.00 | - | - | - | - | 0.83 | - | - |
| 0x8ec76e | 0x6a2ee2 | 0.89 | 1.00 | - | - | - | - | 0.67 (?) | - | - |
| 0x8ec816 | 0x6a3836 | 0.81 | 1.00 | - | - | - | - | 0.44 (?) | - | - |
| 0x8ec708 | 0x6a2a01 | 0.70 | 0.80 | 1.00 | - | - | - | 0.42 (?) | - | - |
| 0x8ec8ba | 0x6a4002 | 0.69 | 1.00 | - | - | - | - | 0.56 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 226 new (O2 only)

### 3. `encoding_rs::utf_16::Utf16Decoder::decode_to_utf8_raw`

- Addresses: O0=0x8e4820, O2=0x6a6d60
- Blocks: O0=23, O2=151
- Mean block similarity: 0.738
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 21 | 135 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 0 | 5 |
| LOOP_HEADER | 1 | 11 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x8e4932 | 0x6a6e78 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8e4944 | 0x6a6f90 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8e4a67 | 0x6a6db0 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0x8e4a79 | 0x6a6ffb | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x8e4d4e | 0x6a6fc2 | 1.00 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0x8e4aa8 | 0x6a75f2 | 0.89 | 1.00 | 1.00 | - | - | - | 1.00 | - | - |
| 0x8e49db | 0x6a751f | 0.81 | 1.00 | - | - | - | - | 0.44 (?) | - | - |
| 0x8e4d0f | 0x6a6d96 | 0.81 | 1.00 | 1.00 | - | - | - | 0.67 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 128 new (O2 only)

### 4. `regex_automata::util::look::LookMatcher::is_word_start_half_unicode`

- Addresses: O0=0xab0040, O2=0x77d020
- Blocks: O0=7, O2=46
- Mean block similarity: 0.614
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 5 | 40 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 0 | 3 |
| LOOP_HEADER | 1 | 3 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xab0164 | 0x77d105 | 0.90 | 1.00 | - | - | - | - | 0.71 | - | - |
| 0xab0143 | 0x77d2aa | 0.85 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xab0092 | 0x77d090 | 0.66 | 1.00 | - | - | - | - | 0.14 (!) | - | - |
| 0xab0040 | 0x77d020 | 0.58 | 0.80 | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0xab0085 | 0x77d08b | 0.51 | 0.33 (?) | - | - | - | - | 1.00 | - | - |
| 0xab0974 | 0x77d1b0 | 0.43 | 0.75 | 0.00 (!) | - | - | - | 0.60 (?) | - | - |
| 0xab12b4 | 0x77d26d | 0.36 | 0.75 | 0.00 (!) | - | - | - | 0.33 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 39 new (O2 only)

### 5. `regex_syntax::hir::literal::Seq::cross_preamble`

- Addresses: O0=0xbca700, O2=0x7a2520
- Blocks: O0=7, O2=41
- Mean block similarity: 0.671
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 6 | 34 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 0 | 1 |
| LOOP_HEADER | 0 | 6 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xbca774 | 0x7a2648 | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0xbca779 | 0x7a2692 | 0.81 | 1.00 | - | - | - | - | 0.67 (?) | - | - |
| 0xbca849 | 0x7a2784 | 0.69 | 1.00 | - | - | - | - | 0.33 (?) | - | - |
| 0xbca867 | 0x7a26e2 | 0.65 | 0.67 (?) | - | - | - | - | 1.00 | - | - |
| 0xbca73e | 0x7a2520 | 0.63 | 0.43 (?) | 1.00 | - | - | - | 0.71 | - | - |
| 0xbca700 | 0x7a2596 | 0.47 | 0.62 (?) | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0xbca837 | 0x7a25f0 | 0.44 | 0.50 (?) | 0.00 (!) | - | - | - | 1.00 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 34 new (O2 only)

### 6. `regex_syntax::ast::parse::specialize_err`

- Addresses: O0=0xc0f550, O2=0x7889d0
- Blocks: O0=3, O2=15
- Mean block similarity: 0.379
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 14 |
| LOOP_HEADER | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xc0f5a0 | 0x788aa5 | 0.50 | 0.50 (?) | - | - | - | - | 0.51 (?) | - | - |
| 0xc0f550 | 0x788a16 | 0.36 | 0.38 (?) | 0.00 (!) | - | - | - | 0.83 | - | - |
| 0xc0f60a | 0x788a57 | 0.27 | 0.20 (!) | 0.00 (!) | - | - | - | 0.80 | - | - |

**Unmatched blocks:** 0 removed (O0 only), 12 new (O2 only)

### 7. `anyhow::chain::<impl core::iter::traits::iterator::Iterator for anyhow::Chain>::next`

- Addresses: O0=0x93db70, O2=0x6afc70
- Blocks: O0=3, O2=7
- Mean block similarity: 0.460
- Optimization effects: BLOCK_SPLITTING, LOOP_UNROLLING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 6 |
| EPILOGUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x93db98 | 0x6afc9f | 0.87 | 1.00 | - | - | - | - | 0.60 (?) | - | - |
| 0x93db70 | 0x6afc7b | 0.27 | 0.50 (?) | 0.00 (!) | - | - | - | 0.30 (?) | - | - |
| 0x93dbb7 | 0x6afc85 | 0.25 | 0.20 (!) | 0.00 (!) | - | - | - | 0.62 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 4 new (O2 only)

### 8. `encoding_rs::data::jis0208_symbol_decode`

- Addresses: O0=0x912b80, O2=0x6a0d20
- Blocks: O0=32, O2=17
- Mean block similarity: 0.545
- Optimization effects: ITERATOR_LOWERING, BLOCK_MERGING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 27 | 15 |
| EPILOGUE | 1 | 0 |
| ITERATOR_STATE | 3 | 2 |
| LOOP_HEADER | 1 | 0 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0x912ba2 | 0x6a0d2b | 1.00 | 1.00 | - | - | - | - | 1.00 | - | - |
| 0x912d6e | 0x6a0e1d | 0.78 | 0.75 | 1.00 | - | - | - | 1.00 | - | - |
| 0x912c89 | 0x6a0dde | 0.73 | 1.00 | 0.33 (?) | - | - | - | 0.83 | - | - |
| 0x912c18 | 0x6a0d20 | 0.66 | 1.00 | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0x912b9a | 0x6a0d84 | 0.65 | 1.00 | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0x912bab | 0x6a0d46 | 0.55 | 0.75 | 0.00 (!) | - | - | - | 1.00 | - | - |
| 0x912d4e | 0x6a0e0a | 0.54 | 0.50 (?) | - | - | - | - | 0.67 (?) | - | - |
| 0x912ca1 | 0x6a0df3 | 0.52 | 0.80 | 0.00 (!) | - | - | - | 0.83 | - | - |

**Unmatched blocks:** 15 removed (O0 only), 0 new (O2 only)

### 9. `regex_automata::util::look::LookMatcher::is_word_ascii`

- Addresses: O0=0xaa9dc0, O2=0x768210
- Blocks: O0=17, O2=7
- Mean block similarity: 0.528
- Optimization effects: ITERATOR_LOWERING, BLOCK_MERGING

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 14 | 6 |
| ITERATOR_STATE | 1 | 0 |
| LOOP_HEADER | 2 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xaa9f0e | 0x768250 | 0.68 | 0.75 | - | - | - | - | 1.00 | - | - |
| 0xaa9df7 | 0x76821e | 0.62 | 0.60 (?) | - | - | - | - | 0.83 | - | - |
| 0xaa9e10 | 0x768210 | 0.56 | 0.67 (?) | - | - | - | - | 0.50 (?) | - | - |
| 0xaa9e25 | 0x768215 | 0.54 | 0.50 (?) | - | - | - | - | 0.75 | - | - |
| 0xaa9ea8 | 0x768244 | 0.54 | 0.50 (?) | - | - | - | - | 0.75 | - | - |
| 0xaa9e8a | 0x768232 | 0.49 | 0.40 (?) | - | - | - | - | 0.80 | - | - |
| 0xaa9eb9 | 0x76824b | 0.26 | 0.40 (?) | 0.00 (!) | - | - | - | 0.50 (?) | - | - |

**Unmatched blocks:** 10 removed (O0 only), 0 new (O2 only)

### 10. `regex_automata::dfa::sparse::State::pattern_id`

- Addresses: O0=0xb4e0b0, O2=0x728e70
- Blocks: O0=3, O2=5
- Mean block similarity: 0.407
- Optimization effects: BLOCK_SPLITTING, INLINING_EXPANSION

**Block types (O0 / O2):**

| Type | O0 | O2 |
|------|----|----|
| BODY | 3 | 4 |
| EPILOGUE | 0 | 1 |

**Block-level feature similarity (matched pairs):**

| O0 Block | O2 Block | Overall | opcodes | constants | concrete_values | memory_pattern | dataflow_edges | instruction_count | callee_names | string_refs |
|----------|----------|--------|--------|--------|--------|--------|--------|--------|--------|--------|
| 0xb4e0d8 | 0x728e90 | 0.67 | 1.00 | - | - | - | - | 0.50 (?) | - | - |
| 0xb4e11b | 0x728ea6 | 0.31 | 0.50 (?) | 0.00 (!) | - | - | - | 0.50 (?) | - | - |
| 0xb4e0b0 | 0x728e70 | 0.25 | 0.25 (!) | 0.00 (!) | - | - | - | 0.60 (?) | - | - |

**Unmatched blocks:** 0 removed (O0 only), 2 new (O2 only)
