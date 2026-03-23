# Untracked Artifacts & Reproducibility Guide

This document records important project artifacts that are **not tracked in git**
(too large, generated, or environment-specific) but are needed to reproduce results.

---

## 1. vSim Submodule Patch (Required)

The `vendor/vSim` submodule requires a one-line API fix for compatibility with
angr >= 9.2. This change lives in the working directory but is not committed to
the submodule (which points to an external repo).

**File:** `vendor/vSim/src/bin_executor.py`, line ~162

```diff
- return self.fast_cfg.get_node(addr)
+ return self.fast_cfg.model.get_any_node(addr)
```

**Why:** angr 9.2+ moved `get_node()` from the CFG object to `cfg.model`. Without
this fix, `RustBinaryLoader.get_blocks_for_function()` raises `AttributeError`.

**To apply manually:**
```bash
cd vendor/vSim
sed -i 's/self\.fast_cfg\.get_node(addr)/self.fast_cfg.model.get_any_node(addr)/' src/bin_executor.py
```

---

## 2. Compiled Test Binaries (Reproducible)

These ELF binaries are too large for git but can be rebuilt from source.

### 2.1 Custom Test Corpus (`tmp/rust-corpus/`)

| Binary | Size | Build Command |
|--------|------|---------------|
| `tmp/rust-corpus/testcrate-O0` | 4.3 MB | See below |
| `tmp/rust-corpus/testcrate-O2` | 4.0 MB | See below |

**Source:** `tmp/rust-corpus/src/lib.rs` (tracked in git)
— 40+ functions across 16 categories: arithmetic, loops, bounds checks, string/slice,
generics, drop glue, panic paths, constants, hashing, control flow, recursion,
closures, dynamic dispatch, unsafe, sorting, bit manipulation.

**Build instructions:**
```bash
cd tmp/rust-corpus

# O0 build (debug, no optimization)
RUSTFLAGS="-C opt-level=0 -C debuginfo=2" cargo build --release
cp target/release/testcrate testcrate-O0

# O2 build (optimized)
RUSTFLAGS="-C opt-level=2 -C debuginfo=2" cargo build --release
cp target/release/testcrate testcrate-O2
```

**Analysis results for this corpus** (committed):
- `data/results/case_analysis/output2.log` — full pipeline output
- `data/results/case_analysis/SUMMARY_REPORT.md` — detailed analysis report
- Baseline: MRR=0.688, Recall@1=0.658

### 2.2 Coreutils Sort (`tmp/coreutils-sort-*`)

| Binary | Size | Build Command |
|--------|------|---------------|
| `tmp/coreutils-sort-O0` | 53 MB | See below |
| `tmp/coreutils-sort-O2` | 61 MB | See below |

**Source:** https://github.com/uutils/coreutils (cloned to `tmp/coreutils/`)

**Build instructions:**
```bash
# Clone (if not present)
git clone https://github.com/uutils/coreutils.git tmp/coreutils
cd tmp/coreutils

# Modify Cargo.toml profiles for analysis compatibility:
# [profile.dev]
# opt-level = 0
# debug = true
#
# [profile.release]
# lto = false          # was: true  (LTO merges functions, complicates analysis)
# panic = "unwind"     # was: abort (unwind preserves more function structure)
# codegen-units = 16   # was: 1     (more codegen units = less cross-function optimization)
# opt-level = 2
# debug = true         # keep debug symbols for groundtruth

# O0 build
cargo build -p uu_sort
cp target/debug/uu_sort ../coreutils-sort-O0

# O2 build
cargo build -p uu_sort --release
cp target/release/uu_sort ../coreutils-sort-O2
```

**Why these profile changes?**
- `lto = false`: LTO merges functions across crates, making function-level matching
  meaningless (no 1-to-1 correspondence).
- `panic = "unwind"`: Abort mode eliminates unwind tables and panic paths, removing
  functions that exist in O0.
- `codegen-units = 16`: Single codegen unit enables aggressive cross-function
  optimization that destroys function boundaries.
- `debug = true`: DWARF info provides symbol names for groundtruth generation.

**Analysis results for this corpus** (committed):
- `data/results/coreutils_sort_analysis/full_output.log` — full pipeline output
- `data/results/coreutils_sort_analysis/ablation_results.csv`
- Baseline: MRR=0.192, Recall@1=0.171

---

## 3. Earlier Run Logs (Superseded)

Two earlier log files from development runs exist on disk but are not committed
because they contain the same experiments as the committed `output2.log` (which
has the final, correct results).

| File | Content | Why Not Committed |
|------|---------|-------------------|
| `data/results/case_analysis/output.log` (632 lines) | First run; crashed at Phase 5 with `ValueError: too many values to unpack` due to groundtruth format bug (expected `(addr1, addr2)` tuples, got `(addr1, addr2, name)` triples). Phases 1-4 data matches `output2.log`. | Bug was fixed; `output2.log` has complete successful run |
| `data/results/case_analysis/full_analysis_output.log` (264 lines) | Second run; completed successfully but without verbose logging. Same final metrics as `output2.log`. | `output2.log` is the canonical version with full detail |

**Key data from these logs** (preserved here for reference):

First run (`output.log`) error — the groundtruth format bug:
```
File "eval/metrics.py", line 32, in top_k_accuracy
    for a1, a2 in gt_pairs:
ValueError: too many values to unpack (expected 2)
```
Fixed by changing the groundtruth generator to emit `(addr1, addr2)` pairs instead
of `(addr1, addr2, name)` triples.

---

## 4. angr Caches (Regenerated Automatically)

| Path Pattern | Content |
|-------------|---------|
| `*_angr_rtdb/` | angr's LMDB-based CFG cache (data.mdb + lock.mdb) |
| `pyvex_ffi_parser_cache*` | pyvex FFI header parse cache |

These are auto-generated by angr on first binary load and speed up subsequent runs.
Safe to delete; they regenerate in ~30 seconds per binary.

---

## 5. Environment & Toolchain

Experiments were run with:

| Tool | Version |
|------|---------|
| Python | 3.10.13 |
| angr | 9.2.204 |
| scipy | 1.17.1 |
| networkx | 3.6.1 |
| numpy | 2.4.2 |
| rustc | 1.92.0 (ded5c06cf 2025-12-08) |
| cargo | 1.92.0 (344c4567c 2025-10-21) |
| OS | RHEL 9.4 (Linux 5.14.0-427.102.1.el9_4.x86_64) |

**Python virtual environment:** `.venv/` (not tracked, ~2GB with angr + z3 + dependencies)

**To recreate:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install angr scipy networkx numpy
pip install -e .  # install rustdiff in editable mode
```

---

## 6. Results Summary (Cross-Reference)

| Corpus | MRR | Recall@1 | Recall@5 | Top-10 | Functions (O0→O2) | Report Location |
|--------|-----|----------|----------|--------|-------------------|-----------------|
| Custom testcrate (40 fns) | 0.688 | 0.658 | 0.711 | 0.737 | 196→162 fingerprinted | `data/results/case_analysis/` |
| Coreutils sort (real-world) | 0.192 | 0.171 | 0.242 | 0.292 | 6,630→1,200 fingerprinted | `data/results/coreutils_sort_analysis/` |

**Key finding:** Real-world Rust binary diffing is significantly harder than toy
corpora. The dominant challenge is **function inlining** — O2 reduces the function
count by ~80% (20,193→3,901 in coreutils sort), meaning most O0 functions have no
corresponding O2 counterpart.

**Most important features:**
1. **Opcode histogram** — dominant in both corpora
2. **Constants** — increasingly important for real-world code with many similar-structured functions
3. **CFG shape** — useful for toy corpus, actively harmful for real-world (optimization drastically changes CFG topology)
