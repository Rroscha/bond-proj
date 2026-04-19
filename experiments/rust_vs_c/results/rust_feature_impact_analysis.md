# Rust Language Features and Their Impact on Binary Function Matching

## What This Document Analyzes

This document examines how Rust-specific language features affect the accuracy of matching functions across compiler optimization levels (O0 vs O2). We compiled 100 pairs of semantically identical functions in both Rust and C at two optimization levels, then measured how well individual basic blocks can be aligned between the unoptimized (O0) and optimized (O2) versions.

**Key question**: When Rust compiles code, do its language-specific features (bounds checking, ownership/drop, Option/Result, iterators, enum matching) leave behind binary patterns that survive optimization and help matching, or do they create noise that hurts matching?

## How the Matching Works

### Basic Blocks

A **basic block** is a straight-line sequence of machine instructions with one entry point and one exit point. When the CPU enters a basic block, it executes every instruction in it before jumping to the next block. A function is made up of many basic blocks connected by jumps and branches.

For example, in this Rust code:

```rust
if data[i] > data[j] {
    data.swap(i, j);
    count += 1;
}
```

The compiler produces roughly three basic blocks:
1. A block that compares `data[i]` and `data[j]` and jumps based on the result
2. A block that performs the swap and increment (entered only if the comparison was true)
3. A block that continues after the if-statement

### Hungarian Algorithm Matching

To compare an O0 function with its O2 version, we align their basic blocks using the **Hungarian algorithm** (also known as the Kuhn-Munkres algorithm). This is an optimal assignment algorithm: given N blocks on one side and M blocks on the other, it finds the pairing that maximizes total similarity.

Each pair of blocks gets a **similarity score** from 0.0 to 1.0, computed by averaging four sub-scores:
- **Opcode similarity**: Do the two blocks use the same types of instructions? (Jaccard similarity of opcode sets)
- **Constant similarity**: Do the two blocks use the same numeric constants? (Jaccard similarity of constant sets)
- **Feature similarity**: Do the blocks have similar structural properties? (instruction count, callee names, memory patterns)
- **Instruction count similarity**: Do the blocks have a similar number of instructions?

We rate each matched pair:
- **GOOD** (score >= 0.7): The block survived optimization well enough to be recognized
- **PARTIAL** (score 0.4-0.7): Some signal remains but the block changed significantly
- **POOR** (score < 0.4): The block is barely recognizable after optimization
- **UNMATCHED**: More blocks on one side than the other; these have no partner

### Block Types

Our analyzer classifies each block by its pattern:
- **BODY**: General computation
- **BOUNDS_CHECK**: A comparison followed by a conditional jump, typically `cmp + jae` or `cmp + jb` (array bounds verification)
- **DROP_GLUE**: Calls to destructors like `drop_in_place<Vec<T>>`
- **ITERATOR_STATE**: Loop counter manipulation (increment, compare, branch)
- **LOOP_HEADER**: Entry point of a loop
- **EPILOGUE**: Function cleanup and return (`add rsp; ret`)
- **PROLOGUE**: Function setup (`push rbp; sub rsp`)

## Overall Results

| Metric | Rust | C | Delta |
|--------|------|---|-------|
| **Mean similarity** | **0.649** | **0.715** | **-0.066** |
| Total O0 blocks (all 100 functions) | 2455 | 2061 | +394 |

| Category | Rust | C | Delta | Rust vs C |
|----------|------|---|-------|-----------|
| bounds_check | 0.730 | 0.700 | **+0.030** | Rust wins |
| ownership_drop | 0.645 | 0.718 | -0.073 | C wins |
| option_result | 0.657 | 0.729 | -0.072 | C wins |
| iterators | 0.593 | 0.679 | -0.086 | C wins |
| enum_match | 0.577 | 0.707 | **-0.130** | C wins (worst) |

Rust wins only in the bounds_check category. The following 20 function deep-dives explain why.

---

## Category 1: Bounds Checking (`bc_` functions)

Rust's bounds checking generates distinctive `cmp + jae/jb` instruction patterns at every array access. These patterns are **optimization-stable anchors**: because the compiler must preserve them for safety (unless it can prove they never trigger), they appear in both O0 and O2 with nearly identical instruction sequences.

### 1.1 `bc_06` — Shell Sort (Rust WINS: 0.802 vs 0.724)

**Rust source:**
```rust
fn bc_06(data: &mut [u64], initial_gap: usize) -> u64 {
    let n = data.len();
    let mut swaps = 0u64;
    let mut gap = initial_gap;
    while gap > 0 {
        for i in gap..n {
            let temp = data[i];        // bounds check here
            let mut j = i;
            while j >= gap && data[j - gap] > temp {  // bounds check here
                data[j] = data[j - gap];               // bounds check x2
                j -= gap;
                swaps += 1;
            }
            data[j] = temp;            // bounds check here
        }
        gap /= 2;
    }
    swaps
}
```

**C source** (same algorithm, no bounds checks):
```c
uint64_t bc_06(uint64_t *data, size_t n, size_t initial_gap) {
    uint64_t swaps = 0;
    size_t gap = initial_gap;
    while (gap > 0) {
        for (size_t i = gap; i < n; i++) {
            uint64_t temp = data[i];           // no check
            size_t j = i;
            while (j >= gap && data[j - gap] > temp) {  // no check
                data[j] = data[j - gap];       // no check
                j -= gap;
                swaps++;
            }
            data[j] = temp;                    // no check
        }
        gap /= 2;
    }
    return swaps;
}
```

**Block counts:**

| | O0 blocks | O2 blocks |
|--|-----------|-----------|
| Rust | 40 | 18 |
| C | 11 | 14 |

Rust has 40 blocks at O0 because each `data[i]`, `data[j-gap]`, `data[j]` access generates a separate bounds-check block. C only has 11 blocks because it directly computes pointer arithmetic without checks.

**Rust Hungarian matching** (mean similarity: **0.802**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x4461bf` | BOUNDS_CHECK | `0x422e3f` | BOUNDS_CHECK | **1.000** | GOOD |
| `0x446234` | BODY | `0x422ead` | BODY | **1.000** | GOOD |
| `0x446284` | BOUNDS_CHECK | `0x422e50` | BOUNDS_CHECK | **0.964** | GOOD |
| `0x4462d0` | BOUNDS_CHECK | `0x422e60` | BOUNDS_CHECK | **0.947** | GOOD |
| `0x44636a` | BOUNDS_CHECK | `0x422e75` | BOUNDS_CHECK | **0.855** | GOOD |
| `0x4461f7` | BOUNDS_CHECK | `0x422e99` | BOUNDS_CHECK | 0.716 | GOOD |
| ... | | | | | |
| 22 blocks | | — | — | 0.000 | UNMATCHED |

The BOUNDS_CHECK blocks score 1.000, 0.964, 0.947, 0.855. They are the highest-scoring matches in the entire function. This is because a bounds check at O0 looks like:

```asm
; O0 BOUNDS_CHECK block
    0x4461bf: cmp      rax, rcx      ; compare index against length
    0x4461c2: jb       0x4461e3      ; jump if index < length (in bounds)
```

And at O2, the same check survives:

```asm
; O2 BOUNDS_CHECK block
    0x422e3f: cmp      rax, rcx
    0x422e42: jb       0x422e50
```

The opcode set (`cmp`, `jb`), the constants, and the instruction count are virtually identical. The optimizer cannot remove these checks (it would change program semantics), so they persist as perfect anchors.

**C Hungarian matching** (mean similarity: **0.724**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x401b00` | BOUNDS_CHECK | `0x403bb8` | BOUNDS_CHECK | 0.875 | GOOD |
| `0x401ab7` | BOUNDS_CHECK | `0x403b80` | BOUNDS_CHECK | 0.783 | GOOD |
| `0x401a7a` | LOOP_HEADER | `0x403b8c` | BODY | 0.693 | PARTIAL |
| `0x401a49` | LOOP_HEADER | `0x403bb4` | PROLOGUE | 0.619 | PARTIAL |

C has fewer blocks and no bounds-check anchors. Its best matches (0.875) come from loop comparison patterns like `cmp rax, rcx; jb`, which happen to look similar to bounds checks but are just loop termination conditions. Without the extra anchor blocks that Rust generates, C's mean similarity is lower.

**Why Rust wins here**: Each `data[i]` in Rust generates a mandatory bounds check (`cmp + jae` to a panic path). These checks are structurally identical at O0 and O2 because the compiler cannot optimize them away (it doesn't know the index is always valid). They act as "anchor" blocks that pull up the overall similarity score. C has no such anchors; its blocks are all generic computation that the optimizer freely restructures.

---

### 1.2 `bc_07` — Convolution (Rust WINS: 0.770 vs 0.630)

**Rust source:**
```rust
fn bc_07(data: &[u64]) -> Vec<i64> {
    let n = data.len();
    if n < 3 { return vec![]; }
    let mut result = Vec::with_capacity(n - 2);
    for i in 1..n - 1 {
        let val = -(data[i - 1] as i64) + 2 * data[i] as i64 - data[i + 1] as i64;
        result.push(val);
    }
    let mut smoothed = Vec::with_capacity(result.len());
    for i in 0..result.len() {
        let left = if i > 0 { result[i - 1] } else { result[i] };
        let right = if i + 1 < result.len() { result[i + 1] } else { result[i] };
        smoothed.push((left + result[i] + right) / 3);
    }
    smoothed
}
```

**Block counts**: Rust 99 O0 → 44 O2; C 18 O0 → 11 O2.

Each `data[i-1]`, `data[i]`, `data[i+1]`, `result[i-1]`, `result[i]`, `result[i+1]` generates a bounds check. The two loops with three accesses each produce many BOUNDS_CHECK blocks.

**Rust matching** (mean: **0.770**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x4464e1` | BODY | `0x423000` | BODY | **1.000** | GOOD |
| `0x446625` | BODY | `0x42312f` | BODY | **1.000** | GOOD |
| `0x4468a0` | BODY | `0x4231ce` | BODY | **1.000** | GOOD |
| `0x446a0e` | BOUNDS_CHECK | `0x4230fb` | BOUNDS_CHECK | **0.868** | GOOD |
| `0x446b6d` | BOUNDS_CHECK | `0x4230d3` | BOUNDS_CHECK | **0.858** | GOOD |
| (18 total GOOD matches) | | | | | |
| (55 UNMATCHED O0 blocks) | | | | | |

Even with 55 unmatched blocks (which don't count in the mean), the matched pairs score very high because the bounds checks and core computation blocks are recognizable.

**C matching** (mean: **0.630**): C's 18 blocks compress to 11 at O2. With no bounds-check anchors, its best match is only 0.825, and many blocks score below 0.6.

---

### 1.3 `bc_09` — Bubble Sort (Rust WINS: 0.720 vs 0.651)

**Rust source:**
```rust
fn bc_09(data: &mut [u64]) -> u64 {
    let n = data.len();
    let mut passes = 0u64;
    loop {
        let mut swapped = false;
        for i in 1..n {
            if data[i - 1] > data[i] {    // two bounds checks
                data.swap(i - 1, i);       // two more bounds checks
                swapped = true;
            }
        }
        passes += 1;
        if !swapped { break; }
    }
    passes
}
```

**Rust matching** (mean: **0.720**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x4472d1` | BOUNDS_CHECK | `0x42346d` | BOUNDS_CHECK | **0.983** | GOOD |
| `0x447353` | BOUNDS_CHECK | `0x423427` | BOUNDS_CHECK | **0.938** | GOOD |
| `0x447322` | BOUNDS_CHECK | `0x423419` | BOUNDS_CHECK | **0.860** | GOOD |

Again, the BOUNDS_CHECK blocks are the top matches. The pattern holds: Rust's mandatory bounds checks create optimization-resistant anchors that pull up matching accuracy.

**C matching** (mean: **0.651**): C's bubble sort has only 9 blocks at both O0 and O2, but without distinctive anchor patterns, its best match is 0.987 for one lucky BOUNDS_CHECK block (from the `data[i-1] > data[i]` comparison, which C does have), and the rest average lower.

---

### 1.4 `bc_12` — Running Median (Rust WINS: 0.793 vs 0.734)

**Rust source:**
```rust
fn bc_12(data: &[u64], window: usize) -> Vec<u64> {
    // ...
    win.sort();
    result.push(win[window / 2]);         // bounds check
    for i in window..n {
        let old = data[i - window];        // bounds check
        if let Ok(pos) = win.binary_search(&old) {
            win.remove(pos);               // bounds check inside
        }
        let insert_pos = win.partition_point(|&x| x < new_val);
        win.insert(insert_pos, new_val);   // bounds check inside
        result.push(win[window / 2]);      // bounds check
    }
    result
}
```

**Block counts**: Rust 63 O0 → 93 O2 (O2 has MORE blocks because the optimizer inlines library calls like `binary_search` and `partition_point`, expanding them into many specialized blocks). C: involves `qsort` and manual array manipulation.

**Rust matching** (mean: **0.793**):

8 matches at 1.000, and the BOUNDS_CHECK blocks score 0.968 and 0.959. Despite the unusual block explosion at O2 (from inlining), Rust's bounds checks still anchor the matching.

**Summary of bounds_check category**: Rust wins because `data[i]` in Rust compiles to a mandatory `cmp + conditional_jump` block that is structurally identical at O0 and O2. These blocks act as anchors that the Hungarian algorithm can reliably match with high confidence. C has no equivalent anchor pattern because C array accesses compile to a single pointer dereference instruction embedded within larger blocks.

---

## Category 2: Enum Matching (`em_` functions)

Rust enums with `match` compile to complex dispatch logic involving tag checks, recursive calls through `Box`, and memory allocation for each variant. At O0, the compiler makes separate function calls for each operation. At O2, everything gets inlined into a single massive block.

### 2.1 `em_06` — Constant Folding (Rust LOSES: 0.734 vs 0.819)

**Rust source:**
```rust
fn em_06(expr: &Expr) -> Expr {
    match expr {
        Expr::Lit(n) => Expr::Lit(*n),
        Expr::Var(s) => Expr::Var(s.clone()),
        Expr::BinOp(l, op, r) => {
            let lf = em_06(l);          // recursive call
            let rf = em_06(r);          // recursive call
            match (&lf, op, &rf) {
                (Expr::Lit(a), Op::Add, Expr::Lit(b)) => Expr::Lit(a + b),
                (Expr::Lit(a), Op::Sub, Expr::Lit(b)) => Expr::Lit(a - b),
                // ... 8 more patterns
                _ => Expr::BinOp(Box::new(lf), *op, Box::new(rf)),
            }
        }
        Expr::UnaryMinus(inner) => { ... }
        Expr::Call(name, args) => { ... }
    }
}
```

**Block counts**: Rust **1** O0 → **1** O2. C **82** O0 → **66** O2.

This is the most dramatic asymmetry in the entire experiment. The Rust function has only **1 basic block** at both O0 and O2, while the C equivalent has 82.

**Why Rust has only 1 block**: At O0, Rust compiles `em_06` as a single entry block that:
1. Loads the enum tag
2. Computes a jump table offset
3. Jumps to the matching case

But the jump table dispatch (`jmp rax` at the end) means all the case handlers are reached through an **indirect jump**, which angr's CFGFast analysis cannot follow. So the analysis tool only sees the single entry block.

```asm
; Rust O0: the ONLY block visible
    0x44b7b0: sub      rsp, 0x378
    0x44b7b7: mov      ...          ; setup
    0x44b7ef: mov      rax, [rsi]   ; load enum tag
    0x44b7fc: mov      rcx, rax
    0x44b7ff: add      rcx, rdx     ; compute jump offset
    ... +9 more instructions
    ; ends with indirect jmp through jump table
```

**Rust matching** (mean: **0.734**): With 1 block matching 1 block, the score is a single number: 0.734. The block has similar instruction patterns (both do tag loading and setup), but the constants differ because O2 reorganizes the jump table.

**C matching** (mean: **0.819**): C's `em_06` uses explicit `switch` with 5 cases and `if-else` chains, generating 82 distinct blocks at O0. The C compiler uses cascading `cmp + je/ja` instructions for the switch:

```asm
; C O0 blocks (sample):
    0x409cd0: cmp      eax, 3       ; case 3?
    0x409cd3: je       0x40a0e1
    0x409cd9: cmp      eax, 3       ; fall-through: > 3?
    0x409cdc: ja       0x40a14d
    0x409ce2: cmp      eax, 2       ; case 2?
    0x409ce5: je       0x409d4f
```

These BOUNDS_CHECK-style blocks (`cmp + je`) match well across optimization levels: 13 C blocks score 1.000.

**Why Rust loses here**: The Rust compiler uses a jump table (indirect `jmp rax`) for the `match` expression. CFGFast cannot follow indirect jumps, so it only discovers 1 block. All the actual case-handling code exists in the binary but is invisible to our analysis. The C compiler uses a chain of `cmp + je` instructions, which create many discoverable blocks, many of which match perfectly.

---

### 2.2 `em_20` — Distribution (Rust LOSES: 0.647 vs 0.799)

**Rust source:**
```rust
fn em_20(expr: &Expr) -> Expr {
    match expr {
        Expr::Lit(n) => Expr::Lit(*n),
        Expr::Var(s) => Expr::Var(s.clone()),
        Expr::BinOp(l, Op::Mul, r) => {
            let lf = em_20(l);
            let rf = em_20(r);
            if let Expr::BinOp(b, Op::Add, c) = &rf {
                // a * (b + c) => a*b + a*c (distribution)
                let ab = Expr::BinOp(Box::new(lf.clone()), Op::Mul, Box::new(*b.clone()));
                let ac = Expr::BinOp(Box::new(lf), Op::Mul, Box::new(*c.clone()));
                return Expr::BinOp(Box::new(ab), Op::Add, Box::new(ac));
            }
            Expr::BinOp(Box::new(lf), Op::Mul, Box::new(rf))
        }
        // ...
    }
}
```

Same problem: Rust **1** O0 → **1** O2 (jump table, CFGFast can't follow), C **30** O0 → **25** O2.

**Rust matching**: Score 0.647 (PARTIAL). **C matching**: Score 0.799, with many GOOD matches from the explicit switch dispatch.

---

### 2.3 `em_10` — Command Executor (Rust loss: 0.648 vs 0.700)

**Rust source:**
```rust
fn em_10(cmds: &[Cmd]) -> i64 {
    let mut env: Vec<(String, CVal)> = Vec::new();
    for cmd in cmds {
        match cmd {
            Cmd::Set(name, val) => { env.push(...); }
            Cmd::Add(a, b, dst) => { ... lookup ... }
            Cmd::Print(name) => { ... }
            Cmd::If(cond, then_cmds, else_cmds) => {
                if lookup(&env, cond).unwrap_or(0) > 0 {
                    output += em_10(then_cmds);  // recursive
                } else {
                    output += em_10(else_cmds);  // recursive
                }
            }
        }
    }
    output
}
```

**Block counts**: Rust 9 O0 → 7 O2. C 38 O0 → 29 O2.

Rust has more than 1 block here because `em_10` operates on `&[Cmd]` (a slice), not on a single `Expr`. The iterator over the slice and the match on `Cmd` variants generate some visible blocks. But it still has far fewer than C.

**Rust matching** (mean: **0.648**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x44d460` | DROP_GLUE | `0x4267f1` | BODY | 0.878 | GOOD |
| `0x44d425` | BODY | `0x426104` | BODY | 0.852 | GOOD |
| `0x44d3f6` | BODY | `0x426040` | BODY | 0.498 | PARTIAL |
| `0x44d330` | BODY | `0x426075` | BODY | 0.464 | PARTIAL |
| 2 blocks UNMATCHED | | | | | |

The DROP_GLUE block (calling `drop_in_place<Vec<...>>`) matches well at 0.878 because the drop pattern (`lea rdi, [rsp+...]; call drop_in_place`) is consistent. But the generic BODY blocks score poorly.

---

### 2.4 `em_17` — Linearity Check (Rust WINS: 0.674 vs 0.491)

**Rust source:**
```rust
fn em_17(expr: &Expr) -> bool {
    match expr {
        Expr::Lit(_) | Expr::Var(_) => true,
        Expr::BinOp(l, Op::Add, r) | Expr::BinOp(l, Op::Sub, r) => em_17(l) && em_17(r),
        Expr::BinOp(_, Op::Mul, _) | Expr::BinOp(_, Op::Div, _) => false,
        Expr::UnaryMinus(inner) => em_17(inner),
        Expr::Call(_, args) => args.iter().all(em_17),
    }
}
```

**Block counts**: Rust 1 O0 → 1 O2. C 2 O0 → 1 O2.

Both languages have very few blocks because this function is simple (returns bool, no allocation). Rust's single block scores 0.674 (PARTIAL). C's 2 blocks compress to 1 at O2, and the best match is 0.491 because the O0 version calls a helper (`call is_linear`) while O2 inlines it completely (`jmp 0x4024a0`), changing the block structure.

```asm
; C O0: calls the helper
    0x40c222: mov      rdi, rax
    0x40c225: call     0x40c0f8      ; call is_linear

; C O2: the function is just a jump (fully inlined elsewhere)
    0x409f00: jmp      0x4024a0
```

**Why Rust wins here**: Both have minimal blocks, but Rust's 1-to-1 match preserves more instruction-level similarity (both versions do tag loading + conditional returns). C's function becomes a trivial `jmp` at O2 due to inlining, destroying the original call pattern.

**Summary of enum_match category**: Rust loses badly because `match` on `Expr` (a recursive enum with `Box`) compiles to jump tables with indirect jumps (`jmp rax`). CFGFast cannot follow indirect jumps, so it only sees 1 block per function. C uses cascading `cmp + je` chains that create many discoverable, matchable blocks. This is the **worst category for Rust** (delta -0.130).

---

## Category 3: Iterators (`iter_` functions)

Rust iterator chains (`.iter().filter().map().collect()`) compile very differently at O0 vs O2. At O0, each adapter is a separate function call. At O2, the entire chain is fused into a single loop with all closures inlined.

### 3.1 `iter_01` — Filter + Enumerate + Collect (Rust LOSES: 0.566 vs 0.763)

**Rust source:**
```rust
fn iter_01(data: &[u64], threshold: u64) -> u64 {
    let above: Vec<(usize, &u64)> = data.iter()
        .enumerate()
        .filter(|(_, &v)| v > threshold)
        .collect();
    let mut sum = 0u64;
    for (idx, &val) in &above {
        sum = sum.wrapping_add(val.wrapping_mul(*idx as u64 + 1));
    }
    let prod: u64 = above.iter()
        .take(5)
        .map(|(_, &v)| v)
        .fold(1u64, |a, b| a.wrapping_mul(b));
    sum.wrapping_add(prod)
}
```

**C source** (same algorithm, explicit loops):
```c
uint64_t iter_01(const uint64_t *data, size_t len, uint64_t threshold) {
    // Manual malloc, explicit for loop, no adapters
    for (size_t i = 0; i < len; i++) {
        if (data[i] > threshold) { buf[count] = i; vals[count] = data[i]; count++; }
    }
    // ...
}
```

**Block counts**: Rust 27 O0 → 20 O2. C 17 O0 → 18 O2.

**Rust O0 blocks** — the call chain is visible:

```asm
; Block 1: call core::slice::<impl [T]>::iter
    0x45b3c0: sub      rsp, 0x198
    0x45b3df: call     0x4910a0          ; slice::iter()

; Block 2: call Iterator::enumerate
    0x45b3e4: mov      rsi, rax
    0x45b3f4: call     0x47f3d0          ; .enumerate()

; Block 3: call Iterator::filter
    0x45b3f9: mov      rsi, ...
    0x45b413: call     0x48dcb0          ; .filter()

; Block 4: call Iterator::collect
    0x45b418: mov      rsi, ...
    0x45b42a: call     0x47cc30          ; .collect()
```

Each adapter (`iter`, `enumerate`, `filter`, `collect`) is a separate block with a `call` to a different generic function. At O2, all of these are inlined into fused loops with completely different instruction patterns.

**Rust matching** (mean: **0.566**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x45b445` | BODY | `0x42f76b` | BODY | 0.866 | GOOD |
| `0x45b53c` | BODY | `0x42f773` | BODY | 0.861 | GOOD |
| `0x45b557` | BODY | `0x42f824` | BODY | 0.846 | GOOD |
| `0x45b3e4` | BODY | `0x42f73c` | BOUNDS_CHECK | 0.659 | PARTIAL |
| `0x45b3f9` | BODY | `0x42f74b` | BODY | 0.437 | PARTIAL |
| `0x45b5b1` | DROP_GLUE | `0x42f82d` | BODY | 0.393 | POOR |
| `0x45b418` | BODY | `0x42f790` | BODY | 0.302 | **POOR** |
| `0x45b598` | BODY | `0x42f780` | BODY | 0.251 | **POOR** |
| 7 blocks UNMATCHED | | | | | |

The blocks calling `Iterator::filter` and `Iterator::collect` (0.437, 0.302) match poorly because at O2, these functions don't exist as separate calls — they've been completely inlined and fused. The O0 block has `call 0x48dcb0` (filter) but the O2 code has the filter logic directly as `cmp + jbe`.

**C matching** (mean: **0.763**):

C's explicit loops look very similar at O0 and O2:

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x40749d` | BOUNDS_CHECK | `0x407607` | BOUNDS_CHECK | **1.000** | GOOD |
| `0x4073f7` | BOUNDS_CHECK | `0x40758c` | BOUNDS_CHECK | **0.977** | GOOD |
| `0x407450` | BOUNDS_CHECK | `0x4075a0` | BOUNDS_CHECK | **0.973** | GOOD |

C's simple `for` loop with `if (data[i] > threshold)` generates BOUNDS_CHECK and LOOP_HEADER blocks that the optimizer preserves almost unchanged.

**Why Rust loses**: At O0, each iterator adapter is a separate `call` instruction pointing to a different generic function address. At O2, all adapters are inlined into a single fused loop. The O0 block's defining feature (a `call` to `Iterator::filter`) completely disappears at O2. The callee name feature, which would normally help matching, becomes useless because the callee doesn't exist at O2.

---

### 3.2 `iter_16` — Chunks + Group Stats (Rust LOSES: 0.691 vs 0.766)

**Rust source:**
```rust
fn iter_16(data: &[u64], group_size: usize) -> u64 {
    let groups: Vec<&[u64]> = data.chunks(group_size).collect();
    let group_sums: Vec<u64> = groups.iter().map(|g| g.iter().sum()).collect();
    let group_maxes: Vec<u64> = groups.iter()
        .map(|g| g.iter().max().copied().unwrap_or(0)).collect();
    let total: u64 = group_sums.iter().zip(group_maxes.iter())
        .map(|(&s, &m)| s.wrapping_add(m))
        .sum();
    total
}
```

**Block counts**: Rust 41 O0 → 59 O2 (O2 is larger from inlining). Rust mean similarity 0.691 vs C's 0.766.

The three-layer chain (`chunks → map → collect`, repeated, then `zip → map → sum`) creates many O0 blocks with calls to generic iterator functions. At O2, these are completely restructured into tight arithmetic loops.

---

### 3.3 `iter_14` — Filter_map + Fold (Rust LOSES: 0.598 vs 0.664)

**Rust source:**
```rust
fn iter_14(data: &[u64]) -> u64 {
    let result: u64 = data.iter()
        .enumerate()
        .filter_map(|(i, &v)| {
            if v > i as u64 { Some(v.wrapping_sub(i as u64)) } else { None }
        })
        .fold(0u64, |acc, v| acc.wrapping_add(v.wrapping_mul(v)));
    let rev_result: u64 = data.iter().rev()
        .enumerate()
        .filter_map(|(i, &v)| {
            if i > 0 && v % (i as u64) == 0 { Some(v) } else { None }
        })
        .sum();
    result.wrapping_add(rev_result)
}
```

**Block counts**: Rust 10 O0 → 31 O2. The O2 binary has 3x more blocks because inlining the `filter_map` and `fold` closures creates many new basic blocks with comparison and arithmetic code.

**Rust matching** (mean: **0.598**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x45d6ae` | BODY | `0x43177c` | BODY | 0.724 | GOOD |
| `0x45d6d7` | BODY | `0x43179c` | EPILOGUE | 0.669 | PARTIAL |
| `0x45d69f` | BODY | `0x4315e5` | BOUNDS_CHECK | 0.541 | PARTIAL |
| `0x45d670` | BODY | `0x431755` | ITERATOR_STATE | 0.496 | PARTIAL |
| (21 O2-only UNMATCHED blocks) | | | | | |

The asymmetry is extreme: 10 O0 blocks vs 31 O2 blocks. This means 21 O2 blocks have no partner. The inlining of closures at O2 creates entirely new blocks with no O0 equivalent.

---

### 3.4 `iter_12` — Scan + Windows (Rust LOSES: 0.613 vs 0.743)

**Rust source:**
```rust
fn iter_12(data: &[u64], threshold: u64) -> u64 {
    let running: Vec<u64> = data.iter()
        .scan(0u64, |state, &x| { *state = state.wrapping_add(x); Some(*state) })
        .collect();
    let crossings: u64 = running.windows(2)
        .filter(|w| (w[0] < threshold) != (w[1] < threshold))
        .count() as u64;
    let final_val = running.last().copied().unwrap_or(0);
    final_val.wrapping_add(crossings * 100)
}
```

**Rust matching** (mean: **0.613**): Best match only 1.000 (1 block), followed by 0.862, then drops quickly. 9 blocks UNMATCHED on O0 side, including a DROP_GLUE block for cleaning up the intermediate `running` Vec.

**C matching** (mean: **0.743**): C uses explicit loops with `malloc`, achieving BOUNDS_CHECK matches at 1.000 and 0.949.

**Summary of iterators category**: Rust iterator chains create blocks at O0 that are defined by their `call` to generic adapter functions (`Iterator::filter`, `Iterator::enumerate`, etc.). At O2, these calls are completely inlined and fused. The O0 and O2 blocks share almost nothing in common — different instruction counts, different opcodes (call vs arithmetic), different constants. This causes the worst average degradation in any feature dimension. C's explicit `for` loops, in contrast, produce blocks that look structurally similar at both optimization levels.

---

## Category 4: Option/Result (`opt_` functions)

Rust's `Option<T>` and `Result<T, E>` types, combined with the `?` operator, generate branch blocks that check for `None`/`Err` and either unwrap or propagate the error. These branches can act as anchors (similar to bounds checks) or can create excessive block fragmentation (if method chains are used).

### 4.1 `opt_04` — `?` Operator in Loop (Rust WINS: 0.780 vs 0.736)

**Rust source:**
```rust
fn opt_04(data: &[u64], target: u64) -> Option<(usize, u64)> {
    let win_size = 3;
    if data.len() < win_size { return None; }
    for start in 0..data.len() - win_size + 1 {
        let mut all_above = true;
        let mut win_sum = 0u64;
        for j in 0..win_size {
            let val = data.get(start + j)?;   // ? operator generates branch
            win_sum += val;
            if *val <= target { all_above = false; }
        }
        if all_above { return Some((start, win_sum)); }
    }
    None
}
```

The `?` operator on `data.get(start + j)?` compiles to: check if the Option is None; if so, return None from the whole function; otherwise, unwrap the value. This generates a BOUNDS_CHECK block at each `?` usage.

**Block counts**: Rust 32 O0 → 9 O2. C 14 O0 → 10 O2.

**Rust matching** (mean: **0.780**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x452bea` | BOUNDS_CHECK | `0x4293ca` | BOUNDS_CHECK | **0.900** | GOOD |
| `0x452c65` | BOUNDS_CHECK | `0x4293d4` | BOUNDS_CHECK | **0.892** | GOOD |
| `0x452d5e` | BOUNDS_CHECK | `0x4293bc` | BOUNDS_CHECK | **0.852** | GOOD |
| `0x452b94` | ITERATOR_STATE | `0x4293b0` | BOUNDS_CHECK | 0.833 | GOOD |
| `0x452b6a` | ITERATOR_STATE | `0x429390` | BOUNDS_CHECK | 0.785 | GOOD |
| (23 UNMATCHED O0 blocks) | | | | | |

The `?` operator generates BOUNDS_CHECK blocks that score 0.900, 0.892, 0.852. These are similar to array bounds checks: they compare a discriminant tag (is it Some or None?) and branch. At O2, these checks are preserved because the compiler must maintain the early-return semantics.

```asm
; O0 BOUNDS_CHECK from ? operator
    0x452bea: cmp      qword ptr [rsp + 0x40], 1   ; check if Some
    0x452bf3: jne      0x452c3f                      ; if None, propagate

; O2 equivalent
    0x4293ca: test     rax, rax                      ; check if pointer is null
    0x4293cd: je       0x4293f1                       ; if null, return None
```

**C matching** (mean: **0.736**): C uses return-code checking (manual `if` on index bounds), which creates similar branch patterns but without the systematic discriminant checks that Rust's `?` generates.

---

### 4.2 `opt_09` — Two `?` in While Loop (Rust WINS: 0.723 vs 0.700)

**Rust source:**
```rust
fn opt_09(data: &[u64], target_sum: u64) -> Option<(usize, usize)> {
    if data.len() < 2 { return None; }
    let mut lo = 0usize;
    let mut hi = data.len() - 1;
    while lo < hi {
        let left = data.get(lo)?;       // ? generates BOUNDS_CHECK
        let right = data.get(hi)?;      // ? generates BOUNDS_CHECK
        let sum = left.wrapping_add(*right);
        if sum == target_sum { return Some((lo, hi)); }
        else if sum < target_sum { lo += 1; }
        else { hi -= 1; }
    }
    None
}
```

Two `?` operators per loop iteration generate two BOUNDS_CHECK blocks. These match well: 0.857 and 0.739.

**Rust matching** (mean: **0.723**), **C matching** (mean: **0.700**). Rust's `?`-generated checks are more distinctive than C's simple pointer arithmetic.

---

### 4.3 `opt_06` — Option Method Chain (Rust LOSES: 0.593 vs 0.786)

**Rust source:**
```rust
fn opt_06(data: &[u64]) -> u64 {
    let first_even: Option<&u64> = data.iter().find(|&&x| x % 2 == 0);
    let doubled = first_even.map(|&v| v * 2);
    let clamped = doubled.filter(|&v| v < 100);
    let base = clamped.unwrap_or(42);

    let last_odd: Option<&u64> = data.iter().rev().find(|&&x| x % 2 == 1);
    let tripled = last_odd.map(|&v| v * 3);
    let bounded = tripled.and_then(|v| if v < 200 { Some(v) } else { None });
    let extra = bounded.unwrap_or(7);

    base.wrapping_add(extra)
}
```

**Block counts**: Rust 12 O0 → 10 O2. C 29 O0 → 13 O2.

**Rust matching** (mean: **0.593**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x4531ef` | BODY | `0x429768` | BOUNDS_CHECK | 0.734 | GOOD |
| `0x453203` | BODY | `0x429760` | BOUNDS_CHECK | 0.689 | PARTIAL |
| `0x4531d0` | BODY | `0x429750` | BODY | 0.492 | PARTIAL |
| `0x453210` | BODY | `0x429785` | BOUNDS_CHECK | 0.444 | PARTIAL |

Unlike the `?` operator, which generates explicit branch blocks, the `.map().filter().unwrap_or()` chain compiles to a series of function calls at O0 that get inlined at O2. The same iterator-fusion problem occurs: at O0 you see `call Option::map`, at O2 you see the inlined arithmetic.

**C matching** (mean: **0.786**): C's explicit `for` loop with `if (data[i] % 2 == 0)` generates clean comparison blocks that match well across optimization levels, with 3 blocks at 1.000.

**Key insight**: The `?` operator (opt_04, opt_09) helps matching because it generates explicit branch blocks. But Option method chains like `.map().filter().unwrap_or()` (opt_06) hurt matching because they compile to function calls that get inlined, exactly like iterator chains.

---

### 4.4 `opt_20` — Split + Parse + Map_or Chain (Rust LOSES: 0.676 vs 0.835)

**Rust source:**
```rust
fn opt_20(s: &str) -> u64 {
    for part in s.split(',') {
        let trimmed = part.trim();
        match trimmed.parse::<u64>() {
            Ok(val) => {
                sum = sum.wrapping_add(val);
                count += 1;
                max_val = Some(max_val.map_or(val, |m: u64| m.max(val)));
                min_val = Some(min_val.map_or(val, |m: u64| m.min(val)));
            }
            Err(_) => {}
        }
    }
    // ...
}
```

**Block counts**: Rust 21 O0 → 28 O2. C 37 O0 → 47 O2.

**Rust matching** (mean: **0.676**): The `map_or` calls at O0 become inlined code at O2. The `s.split(',')` iterator also transforms. Best matches include two at 1.000 (for simple comparison blocks), but many score 0.5-0.6.

**C matching** (mean: **0.835**): C has 6 blocks at 1.000 and 8 more above 0.970. C's `strtok`/`strtol` and manual `if` chains produce remarkably stable blocks.

---

## Category 5: Ownership and Drop (`own_` functions)

Rust's ownership system and automatic destructors (Drop trait) generate **drop glue** blocks that call `drop_in_place<T>` to free memory when values go out of scope. These can be helpful (distinctive call targets) or harmful (extra blocks with no C equivalent).

### 5.1 `own_01` — Matrix with Custom Drop (Rust WINS: 0.704 vs 0.627)

**Rust source:**
```rust
fn own_01(n: u64) -> u64 {
    let n = n as usize;
    let mut mat = OwnedMatrix::new(n, n);  // allocates with Vec
    for r in 0..n {
        mat.set(r, 0, (r + 1) as u64);
        if n > 1 { mat.set(r, 1, (r + 2) as u64); }
        for c in 2..n {
            let val = mat.get(r, c - 1).wrapping_add(mat.get(r, c - 2));
            mat.set(r, c, val);
        }
    }
    let mut total = 0u64;
    for r in 0..n {
        for c in 0..n { total = total.wrapping_add(mat.get(r, c)); }
    }
    total
    // mat drops here: OwnedMatrix::drop zeroes data
}
```

**Block counts**: Rust 52 O0 → 42 O2. C 37 O0 → 47 O2.

This function uses **explicit indexing** (`mat.set(r, c, val)` and `mat.get(r, c)`) rather than iterator chains. Each `set` and `get` call generates bounds checks (the matrix validates row/column indices), and the custom `Drop` implementation generates a DROP_GLUE block.

**Rust matching** (mean: **0.704**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x45543a` | BODY | `0x42b07b` | BODY | **1.000** | GOOD |
| `0x45563c` | BODY | `0x42b16a` | BODY | **1.000** | GOOD |
| `0x45576c` | BODY | `0x42b1c3` | BODY | **1.000** | GOOD |
| `0x455652` | BOUNDS_CHECK | `0x42af5a` | BOUNDS_CHECK | **0.954** | GOOD |
| `0x455788` | ITERATOR_STATE | `0x42b03e` | BODY | 0.854 | GOOD |
| `0x455516` | DROP_GLUE | `0x42af6b` | BODY | 0.627 | PARTIAL |

The bounds checks from `mat.get(r, c)` and `mat.set(r, c, val)` serve as anchors (0.954), just like in the bounds_check category. The DROP_GLUE block matches at 0.627, a moderate score — the `drop_in_place` call target changes slightly between O0 and O2 but the pattern is recognizable.

**C matching** (mean: **0.627**): C has no bounds checks on matrix access and no Drop — its blocks are all generic computation with no distinctive anchor patterns.

**Why Rust wins here**: Explicit indexing creates bounds-check anchors (same mechanism as bc_ functions). The ownership/drop patterns add a small additional signal. This function proves that when Rust code uses indexing rather than iterators, its binary matching performance is as good as or better than C.

---

### 5.2 `own_05` — Merge Sorted Vecs (Rust WINS: 0.780 vs 0.720)

**Rust source:**
```rust
fn own_05(a: Vec<u64>, b: Vec<u64>) -> Vec<u64> {
    let mut result = Vec::with_capacity(a.len() + b.len());
    let mut i = 0;
    let mut j = 0;
    while i < a.len() && j < b.len() {
        if a[i] <= b[j] { result.push(a[i]); i += 1; }  // bounds checks
        else { result.push(b[j]); j += 1; }               // bounds checks
    }
    while i < a.len() { result.push(a[i]); i += 1; }
    while j < b.len() { result.push(b[j]); j += 1; }
    // running max with explicit indexing
    for k in 0..result.len() {
        if result[k] > max_so_far { max_so_far = result[k]; }
        result[k] = max_so_far;
    }
    result   // a, b consumed (moved), result returned
}
```

Again, explicit indexing with `a[i]`, `b[j]`, `result[k]`. Each generates bounds checks.

**Rust matching** (mean: **0.780**):

4 blocks at 1.000, BOUNDS_CHECK blocks at 0.986, 0.947. The function also has DROP_GLUE blocks scoring 0.976 and 0.720 — the drop of consumed Vecs `a` and `b` produces recognizable patterns.

**C matching** (mean: **0.720**): Lower because C's pointer arithmetic blocks are generic.

---

### 5.3 `own_03` — String Split + Transform (Rust LOSES: 0.689 vs 0.752)

**Rust source:**
```rust
fn own_03(s: String, rot: usize) -> String {
    let words: Vec<String> = s.split_whitespace().map(|w| w.to_string()).collect();
    let mut transformed: Vec<String> = Vec::with_capacity(words.len());
    for word in &words {
        let bytes = word.as_bytes();
        let mut rotated = String::with_capacity(bytes.len());
        for k in 0..bytes.len() {
            let idx = (k + rot) % bytes.len();
            rotated.push(bytes[idx] as char);
        }
        transformed.push(rotated);
    }
    transformed.join(" ")
    // words, transformed, each String inside drops
}
```

**Rust matching** (mean: **0.689**): The `.split_whitespace().map().collect()` chain suffers the same iterator-fusion problem. At O0, there are calls to `split_whitespace`, `Iterator::map`, `Iterator::collect`. At O2, these are inlined. Additionally, the multiple String allocations and drops create many DROP_GLUE blocks that don't have clean O2 equivalents (the optimizer sometimes eliminates intermediate allocations entirely).

**C matching** (mean: **0.752**): C's `strtok` loop with `malloc`/`free` produces stable block patterns.

**Key insight**: Functions that use `.split().map().collect()` (iterator chains) lose matching accuracy, even when the primary category is "ownership". The iterator usage is the dominant factor, not the drop logic.

---

### 5.4 `own_04` — Box Linked List with Recursive Drop (Rust LOSES: 0.711 vs 0.802)

**Rust source:**
```rust
fn own_04(n: u64) -> u64 {
    enum List { Cons(u64, Box<List>), Nil }
    let mut head = List::Nil;
    for i in (0..n).rev() {
        let val = i.wrapping_mul(i).wrapping_add(1);
        head = List::Cons(val, Box::new(head));  // heap alloc for each node
    }
    let mut sum = 0u64;
    let mut cur = &head;
    loop {
        match cur {
            List::Cons(val, next) => { sum = sum.wrapping_add(*val); cur = next; }
            List::Nil => break,
        }
    }
    sum.wrapping_mul(count)
    // head drops recursively: each Box freed
}
```

**Block counts**: Rust 26 O0 → 13 O2. C 11 O0 → 14 O2.

**Rust matching** (mean: **0.711**):

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x4561a0` | BODY | `0x42bb30` | LOOP_HEADER | **0.987** | GOOD |
| `0x4561ee` | BODY | `0x42bb80` | ITERATOR_STATE | 0.870 | GOOD |
| `0x4563b8` | DROP_GLUE | `0x42bba2` | DROP_GLUE | 0.765 | GOOD |
| (13 UNMATCHED O0 blocks) | | | | | |

The DROP_GLUE block matches at 0.765 — both O0 and O2 call `drop_in_place<List>`. But Rust has 13 extra O0 blocks from iterator state management and Box allocation calls that have no O2 equivalent.

**C matching** (mean: **0.802**): C's linked list with explicit `malloc`/`free` has simple, stable block patterns:

| O0 Block | Type | O2 Block | Type | Score | Verdict |
|----------|------|----------|------|-------|---------|
| `0x4071ed` | BODY | `0x4073da` | BODY | **1.000** | GOOD |
| `0x4072d9` | BOUNDS_CHECK | `0x4073d5` | BOUNDS_CHECK | **1.000** | GOOD |
| `0x407307` | BODY | `0x407402` | BODY | **1.000** | GOOD |
| `0x407309` | PROLOGUE | `0x4074bf` | PROLOGUE | **1.000** | GOOD |
| `0x40730a` | BOUNDS_CHECK | `0x40741e` | BOUNDS_CHECK | **1.000** | GOOD |
| `0x407310` | BOUNDS_CHECK | `0x407465` | BOUNDS_CHECK | **1.000** | GOOD |

C has 6 blocks at 1.000. The `malloc`/`free` calls and the linked-list traversal loop produce consistent patterns because C's optimizer doesn't fundamentally restructure `malloc` calls.

---

## Key Findings

### Features That HELP Matching

1. **Bounds checks from array indexing (`data[i]`)**: The single most helpful Rust feature. Each array access generates a `cmp + conditional_jump` block that is nearly identical at O0 and O2. These blocks score 0.85-1.00 consistently.

2. **The `?` operator on Option/Result**: Generates explicit branch blocks that check discriminant tags and propagate errors. These branch blocks are structurally similar to bounds checks and score 0.85-0.90.

3. **Explicit indexing in ownership code (`a[i]`, `b[j]`)**: When ownership functions use indexing rather than iterators, they benefit from the same bounds-check anchor effect.

4. **Drop glue for simple types**: Calls to `drop_in_place<Vec<T>>` create blocks with a distinctive call target that persists across optimization levels. Scores 0.6-0.9 depending on how much the optimizer transforms the surrounding code.

### Features That HURT Matching

1. **Iterator chains (`.iter().filter().map().collect()`)**: The worst offender. At O0, each adapter is a separate function call. At O2, everything is inlined and fused into a tight loop. The O0 and O2 blocks share almost nothing. Causes the biggest matching degradation.

2. **`match` on recursive enums (Box-based ASTs)**: Compiles to jump tables with indirect jumps (`jmp rax`). CFGFast cannot follow indirect jumps, so only 1 block is visible. This artificially limits matching data.

3. **Option method chains (`.map().filter().unwrap_or()`)**: Same problem as iterators — function calls at O0 are inlined at O2.

4. **Monomorphized generic calls**: At O0, generic functions like `Vec::push::<u64>` exist as separate call targets. At O2, they're inlined. The callee name feature (which helps distinguish blocks at O0) becomes useless at O2.

### The Core Pattern

The fundamental issue is **call-site vs. inline-site asymmetry**:

- At **O0**, Rust generates many `call` instructions to library functions (`Iterator::filter`, `Option::map`, `Vec::push`, etc.). These calls are the defining feature of each block.
- At **O2**, these calls are inlined. The block no longer contains a `call` instruction; instead, it contains the inlined arithmetic/comparison code.

Features that generate **structural patterns** (comparisons, branches, specific instruction sequences) survive optimization because they represent semantics the compiler must preserve. Features that generate **function calls** to generic library code do not survive because inlining transforms them into unrecognizable inline code.

### Practical Implications for Binary Matching

1. **Bounds-check blocks are the best anchors for Rust binary matching.** Any matching algorithm should weight BOUNDS_CHECK-typed blocks higher when matching Rust binaries.

2. **Iterator-heavy Rust functions need different matching strategies.** Traditional block-level matching fails because O0 and O2 have fundamentally different structure. Possible alternatives: semantic matching based on data flow, or matching at the loop level rather than the block level.

3. **The `?` operator creates useful anchors.** Rust code that uses `?` for error handling produces more matchable binaries than code using `.map().and_then()` chains.

4. **Jump-table dispatch limits analysis.** Rust enum `match` compiles to jump tables that CFGFast cannot follow. Improving indirect jump resolution would recover many currently-invisible blocks and likely improve matching for enum-heavy code.

5. **C wins on aggregate because its code structure is more stable across optimization levels.** C's explicit loops, pointer arithmetic, and manual memory management produce blocks that look similar at O0 and O2. Rust's abstractions (iterators, Option methods, generic calls) create dramatic structural changes between O0 and O2.
