#!/usr/bin/env bash
# Demo script for RustDiff — intended to be driven by asciinema.
#
# Usage:
#   asciinema rec -c scripts/demo.sh demo.cast
#
# What it does (~90 s total):
#   1. Show the project structure (what we're about to run)
#   2. docker run with --quick (2 funcs × 5 features = 10 functions)
#   3. Tail the summary table that the run prints to stderr
#   4. Show the analysis_data.json that was just generated
#
# The image `rustdiff:latest` must already be built:
#     docker build -t rustdiff .

set -e

# Pacing — if you don't have `pv`, fall back to raw echo.
say() {
    echo
    echo "\$ $*"
    sleep 1
}

run() {
    echo
    echo "\$ $*"
    sleep 1
    eval "$*"
}

# ── 1. show repo ────────────────────────────────────────────────────────────
clear
cat <<'BANNER'
╔═══════════════════════════════════════════════════════════════════════╗
║  RustDiff — cross-optimization basic-block matching                   ║
║  100 Rust fns vs 100 equivalent C fns, O0 ↔ O2, DWARF ground truth    ║
╚═══════════════════════════════════════════════════════════════════════╝
BANNER
sleep 2

run "ls experiments/rust_features/*_O{0,2} 2>/dev/null"
sleep 1

# ── 2. run analysis (--quick: 10 funcs in ~60 s) ────────────────────────────
echo
echo "── Running the full pipeline inside Docker (quick mode, ~60 s) ──"
sleep 1
mkdir -p /tmp/rustdiff-demo
run "docker run --rm \\
    -v \"\$PWD/experiments/rust_features/run_analysis.py:/app/experiments/rust_features/run_analysis.py\" \\
    -v /tmp/rustdiff-demo:/app/experiments/rust_features/results \\
    rustdiff python experiments/rust_features/run_analysis.py --quick 2>&1 | tail -40"

# ── 3. show what was produced ───────────────────────────────────────────────
echo
echo "── Output ──"
sleep 1
run "ls -lh /tmp/rustdiff-demo/"

echo
echo "── Headline numbers (feature × method, Rust vs C) ──"
sleep 1
run "python3 -c \"
import json
d = json.load(open('/tmp/rustdiff-demo/analysis_data.json'))
for p, fn in d['features'].items():
    row = f'{fn:<28}'
    for m in d['methods']:
        mm = d['summary'][p]['methods'][m]
        row += f'  {m}: R={mm[\\\"rust_accuracy\\\"]:4.0%} C={mm[\\\"c_accuracy\\\"]:4.0%}'
    print(row)
\""

echo
echo "── done. Full (100-function) run: ~4 min, same invocation without --quick ──"
sleep 3
