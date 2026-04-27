# RustDiff

RustDiff studies how Rust language features affect binary basic-block matching accuracy compared to equivalent C code. It compiles 100 Rust functions and 100 semantically equivalent C functions at O0 and O2 (both with DWARF debug info), extracts basic blocks via angr, matches O0 blocks to O2 blocks using 3 independent similarity methods (value-based micro-execution, opcode Jaccard, constant Jaccard), and validates matches against DWARF ground truth.

## Tested Rust features (20 functions each)

| Prefix | Feature | What Rust generates |
|--------|---------|---------------------|
| `bc_` | Bounds Checking | `data[i]` → `cmp index, len; jae panic` |
| `dg_` | Drop Glue (RAII) | auto `drop_in_place<T>` calls |
| `qm_` | ? Operator | Option/Result → discriminant check + error return |
| `pu_` | Panic / Unwrap | `.unwrap()` → check + panic blocks |

## Project structure

```
rustdiff/                       # core library
  loader.py                     # angr-based binary loader
  micro_exec/                   # block-level concrete execution
  fingerprint/                  # function fingerprinting
  analysis/                     # block classification, alignment
  matching/                     # similarity & Hungarian matching

experiments/rust_features/      # the main experiment
  rust_crate/                   # Rust source (src/main.rs, 100 functions)
  c_src/bench.c                 # C source (100 equivalent functions)
  rust_O0, rust_O2              # compiled Rust binaries (ELF x86-64)
  c_bench_O0, c_bench_O2       # compiled C binaries (ELF x86-64)
  run_analysis.py               # main analysis script → analysis_data.json
  generate_report.py            # JSON → HTML report
  generate_slides.py            # JSON → PowerPoint slides
  results/
    analysis_data.json          # full analysis output
    report.html                 # HTML report
    slides.pptx                 # presentation slides

eval/                           # DWARF ground truth utilities
tests/                          # unit tests
```

## Requirements

- Python >= 3.12
- Rust toolchain (tested with rustc 1.92.0)
- GCC (tested with gcc 11.4.1)
- Linux x86-64

## Setup

```bash
# 1. Clone
git clone <repo-url> && cd bond-proj

# 2. Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

## Reproduce results

### Step 1: Compile the binaries

```bash
cd experiments/rust_features

# ── Rust: O0 (debug) and O2 (release) ──
# Cargo.toml already sets: debug=2, panic="unwind", lto=false
cd rust_crate
cargo build                     # O0 binary → target/debug/rust_features
cargo build --release           # O2 binary → target/release/rust_features
cd ..

# Copy binaries to experiment directory
cp rust_crate/target/debug/rust_features   rust_O0
cp rust_crate/target/release/rust_features rust_O2

# ── C: O0 and O2 ──
gcc -O0 -g -o c_bench_O0 c_src/bench.c
gcc -O2 -g -o c_bench_O2 c_src/bench.c
```

Key compiler flags:
- `-g` / `debug=2`: DWARF debug info for ground truth (does not affect optimization)
- `panic="unwind"`: keep panic paths in binary (not `abort`)
- `lto=false`: no cross-function inlining that would destroy function boundaries

### Step 2: Run the analysis

```bash
cd /path/to/bond-proj

# Activate venv
source .venv/bin/activate

# Run analysis (~10-30 min depending on hardware)
# Loads 4 binaries, micro-executes all blocks, runs Hungarian matching
python experiments/rust_features/run_analysis.py
```

Output: `experiments/rust_features/results/analysis_data.json`

This JSON contains per-function data for all 200 functions (100 Rust + 100 C): block counts, per-block assembly + opcodes + constants + source lines, matching pairs for each method, accuracy scores, and DWARF ground truth coverage.

### Step 3: Generate reports

```bash
# HTML report
python experiments/rust_features/generate_report.py
# → experiments/rust_features/results/report.html

# PowerPoint slides
python experiments/rust_features/generate_slides.py
# → experiments/rust_features/results/slides.pptx
```

## How it works

1. **Load binaries**: angr loads O0 and O2 ELF binaries, recovers CFG and basic blocks
2. **Micro-execute**: each block is run with 4 concrete test inputs; collect register outputs, memory access patterns, dataflow edges, constants
3. **Compute similarity**: for each (O0 block, O2 block) pair, compute similarity using 3 independent methods:
   - **Value-based**: weighted combination of concrete output match, dataflow similarity, memory pattern similarity, constant overlap
   - **Opcode Jaccard**: `|opcodes_O0 ∩ opcodes_O2| / |opcodes_O0 ∪ opcodes_O2|`
   - **Constant Jaccard**: `|constants_O0 ∩ constants_O2| / |constants_O0 ∪ constants_O2|`
4. **Hungarian matching**: build cost matrix, find optimal 1-to-1 block assignment
5. **DWARF validation**: each matched pair is checked against source line mapping — correct iff both blocks map to at least one shared source line
6. **Accuracy**: `correct_pairs / min(n_O0, n_O2)`
