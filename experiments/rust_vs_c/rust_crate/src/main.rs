// 100 functions organized by Rust-specific feature category.
// Each function implements a real algorithm with multiple control flow paths.
// Target: >= 5 basic blocks at O0 per function.
//
// Categories (20 each):
//   1. bounds_check (bc_): algorithms that index slices, generating cmp+jcc guards
//   2. ownership_drop (own_): RAII with Vec/String/Box, generating drop_in_place
//   3. option_result (opt_): Option/Result with multi-step unwrapping
//   4. iterators (iter_): iterator chains with closures and state
//   5. enum_match (em_): rich enums with recursive/nested pattern matching

use std::hint::black_box;

fn main() {
    let mut data: Vec<u64> = (0..64).collect();
    let data2: Vec<u64> = (100..200).collect();
    let s = "hello world foo bar baz 123 testing";

    // bounds_check
    black_box(bc_01(black_box(&data), black_box(10)));
    black_box(bc_02(black_box(&mut data.clone())));
    black_box(bc_03(black_box(&data), black_box(3)));
    black_box(bc_04(black_box(&data), black_box(&data2)));
    black_box(bc_05(black_box(&data)));
    black_box(bc_06(black_box(&mut data.clone()), black_box(5)));
    black_box(bc_07(black_box(&data)));
    black_box(bc_08(black_box(&data), black_box(30)));
    black_box(bc_09(black_box(&mut data.clone())));
    black_box(bc_10(black_box(&data), black_box(4)));
    black_box(bc_11(black_box(&mut data.clone())));
    black_box(bc_12(black_box(&data), black_box(7)));
    black_box(bc_13(black_box(&data)));
    black_box(bc_14(black_box(&mut data.clone()), black_box(3)));
    black_box(bc_15(black_box(&data)));
    black_box(bc_16(black_box(&data), black_box(8)));
    black_box(bc_17(black_box(&mut data.clone())));
    black_box(bc_18(black_box(&data), black_box(5)));
    black_box(bc_19(black_box(&data)));
    black_box(bc_20(black_box(&mut data.clone()), black_box(10)));

    // ownership_drop
    black_box(own_01(black_box(20)));
    black_box(own_02(black_box(vec![5,3,8,1,7,2,9,4,6]), black_box(true)));
    black_box(own_03(black_box(s.to_string()), black_box(3)));
    black_box(own_04(black_box(15)));
    black_box(own_05(black_box(vec![10,20,30,40,50]), black_box(vec![5,15,25,35,45])));
    black_box(own_06(black_box("hello world test".to_string())));
    black_box(own_07(black_box(8)));
    black_box(own_08(black_box(vec![1,5,3,8,2,7,4,6]), black_box(4)));
    black_box(own_09(black_box("abcdefghij".to_string()), black_box(3)));
    black_box(own_10(black_box(12)));
    black_box(own_11(black_box(vec![9,1,5,3,7,2,8,4,6]), black_box(true)));
    black_box(own_12(black_box("the quick brown fox".to_string())));
    black_box(own_13(black_box(10)));
    black_box(own_14(black_box(vec![3,1,4,1,5,9,2,6,5,3,5]), black_box(3)));
    black_box(own_15(black_box("rust lang is great".to_string()), black_box('a')));
    black_box(own_16(black_box(6)));
    black_box(own_17(black_box(vec![100,200,50,300,150]), black_box(2)));
    black_box(own_18(black_box("hello".to_string()), black_box("world".to_string())));
    black_box(own_19(black_box(8)));
    black_box(own_20(black_box(vec![7,2,5,1,8,3,6,4]), black_box(true)));

    // option_result
    black_box(opt_01(black_box(&data), black_box(30)));
    black_box(opt_02(black_box(s), black_box(' ')));
    black_box(opt_03(black_box(&[Some(1u64), None, Some(3), Some(4), None, Some(6)])));
    black_box(opt_04(black_box(&data), black_box(50)));
    black_box(opt_05(black_box("123 456 abc 789"), black_box(10)));
    black_box(opt_06(black_box(&data)));
    black_box(opt_07(black_box(s)));
    black_box(opt_08(black_box(&[Ok(1u64), Err("bad"), Ok(3), Ok(4), Err("fail"), Ok(6)])));
    black_box(opt_09(black_box(&data), black_box(5)));
    black_box(opt_10(black_box(s), black_box(3)));
    black_box(opt_11(black_box(&data)));
    black_box(opt_12(black_box(&[Some(10u64), Some(20), None, Some(40)]), black_box(25)));
    black_box(opt_13(black_box(&data), black_box(7)));
    black_box(opt_14(black_box("10 20 abc 30 40 xyz 50")));
    black_box(opt_15(black_box(&data), black_box(3)));
    black_box(opt_16(black_box(&[Ok(5i64), Ok(-3), Err("x"), Ok(7), Err("y"), Ok(-1)])));
    black_box(opt_17(black_box(&data), black_box(10)));
    black_box(opt_18(black_box(s)));
    black_box(opt_19(black_box(&data), black_box(8)));
    black_box(opt_20(black_box("3,1,4,1,5,9,2,6")));

    // iterators
    black_box(iter_01(black_box(&data), black_box(10)));
    black_box(iter_02(black_box(&data), black_box(&data2)));
    black_box(iter_03(black_box(&data), black_box(5)));
    black_box(iter_04(black_box(s)));
    black_box(iter_05(black_box(&data)));
    black_box(iter_06(black_box(&data), black_box(3)));
    black_box(iter_07(black_box(s), black_box(' ')));
    black_box(iter_08(black_box(&data), black_box(4)));
    black_box(iter_09(black_box(&data)));
    black_box(iter_10(black_box(&data), black_box(10)));
    black_box(iter_11(black_box(s)));
    black_box(iter_12(black_box(&data), black_box(8)));
    black_box(iter_13(black_box(&data), black_box(&data2)));
    black_box(iter_14(black_box(&data)));
    black_box(iter_15(black_box(s), black_box(3)));
    black_box(iter_16(black_box(&data), black_box(5)));
    black_box(iter_17(black_box(&data)));
    black_box(iter_18(black_box(&data), black_box(7)));
    black_box(iter_19(black_box(s)));
    black_box(iter_20(black_box(&data), black_box(3)));

    // enum_match
    let tokens = lex(black_box("42 + foo * (bar - 3)"));
    black_box(em_01(black_box(&tokens)));
    let expr = parse_expr(black_box("1 + 2 * 3"));
    black_box(em_02(black_box(&expr)));
    black_box(em_03(black_box(&tokens)));
    black_box(em_04(black_box(&expr)));
    black_box(em_05(black_box(&tokens), black_box(3)));
    black_box(em_06(black_box(&expr)));
    black_box(em_07(black_box(&tokens)));
    black_box(em_08(black_box(&expr)));
    black_box(em_09(black_box(&tokens)));
    let cmds = vec![
        Cmd::Set("x".into(), CVal::Int(10)),
        Cmd::Set("y".into(), CVal::Int(20)),
        Cmd::Add("x".into(), "y".into(), "z".into()),
        Cmd::Print("z".into()),
    ];
    black_box(em_10(black_box(&cmds)));
    black_box(em_11(black_box(&tokens)));
    black_box(em_12(black_box(&expr)));
    black_box(em_13(black_box(&tokens)));
    black_box(em_14(black_box(&expr)));
    black_box(em_15(black_box(&cmds)));
    black_box(em_16(black_box(&tokens)));
    black_box(em_17(black_box(&expr)));
    black_box(em_18(black_box(&tokens), black_box(5)));
    black_box(em_19(black_box(&cmds)));
    black_box(em_20(black_box(&expr)));
}

// ============================================================================
// Category 1: Bounds Check (bc_01 .. bc_20)
// Real algorithms with indexed slice access. Each generates cmp+jcc per access.
// ============================================================================

/// Insertion sort on a slice region [0..idx], return inversions counted
#[inline(never)]
fn bc_01(data: &[u64], limit: usize) -> u64 {
    let n = data.len().min(limit);
    let mut buf: Vec<u64> = data[..n].to_vec();
    let mut inversions = 0u64;
    for i in 1..n {
        let key = buf[i];
        let mut j = i;
        while j > 0 && buf[j - 1] > key {
            buf[j] = buf[j - 1];
            j -= 1;
            inversions += 1;
        }
        buf[j] = key;
    }
    inversions
}

/// Partition around pivot and return pivot index (quicksort partition)
#[inline(never)]
fn bc_02(data: &mut [u64]) -> usize {
    let n = data.len();
    if n <= 1 { return 0; }
    let pivot_idx = n / 2;
    data.swap(pivot_idx, n - 1);
    let pivot = data[n - 1];
    let mut store = 0;
    for i in 0..n - 1 {
        if data[i] < pivot {
            data.swap(i, store);
            store += 1;
        }
    }
    data.swap(store, n - 1);
    store
}

/// Compute histogram with `bins` buckets over the data range
#[inline(never)]
fn bc_03(data: &[u64], bins: usize) -> Vec<u64> {
    if data.is_empty() || bins == 0 { return vec![]; }
    let min_val = data[0];
    let mut max_val = data[0];
    for i in 1..data.len() {
        if data[i] > max_val { max_val = data[i]; }
    }
    let range = max_val - min_val + 1;
    let bin_size = (range + bins as u64 - 1) / bins as u64;
    let mut hist = vec![0u64; bins];
    for i in 0..data.len() {
        let bin = ((data[i] - min_val) / bin_size) as usize;
        if bin < bins {
            hist[bin] += 1;
        }
    }
    hist
}

/// Merge two sorted halves of the data in-place using auxiliary buffer
#[inline(never)]
fn bc_04(a: &[u64], b: &[u64]) -> Vec<u64> {
    let mut result = Vec::with_capacity(a.len() + b.len());
    let mut i = 0;
    let mut j = 0;
    while i < a.len() && j < b.len() {
        if a[i] <= b[j] {
            result.push(a[i]);
            i += 1;
        } else {
            result.push(b[j]);
            j += 1;
        }
    }
    while i < a.len() { result.push(a[i]); i += 1; }
    while j < b.len() { result.push(b[j]); j += 1; }
    result
}

/// Longest increasing subsequence length via patience sorting
#[inline(never)]
fn bc_05(data: &[u64]) -> u64 {
    let mut tails: Vec<u64> = Vec::new();
    for i in 0..data.len() {
        let val = data[i];
        let mut lo = 0usize;
        let mut hi = tails.len();
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if tails[mid] < val { lo = mid + 1; } else { hi = mid; }
        }
        if lo == tails.len() {
            tails.push(val);
        } else {
            tails[lo] = val;
        }
    }
    tails.len() as u64
}

/// Shell sort with Knuth gap sequence
#[inline(never)]
fn bc_06(data: &mut [u64], initial_gap: usize) -> u64 {
    let n = data.len();
    let mut swaps = 0u64;
    let mut gap = initial_gap;
    while gap > 0 {
        for i in gap..n {
            let temp = data[i];
            let mut j = i;
            while j >= gap && data[j - gap] > temp {
                data[j] = data[j - gap];
                j -= gap;
                swaps += 1;
            }
            data[j] = temp;
        }
        gap /= 2;
    }
    swaps
}

/// Matrix-style convolution: weighted sum with kernel [-1, 2, -1]
#[inline(never)]
fn bc_07(data: &[u64]) -> Vec<i64> {
    let n = data.len();
    if n < 3 { return vec![]; }
    let mut result = Vec::with_capacity(n - 2);
    for i in 1..n - 1 {
        let val = -(data[i - 1] as i64) + 2 * data[i] as i64 - data[i + 1] as i64;
        result.push(val);
    }
    // Second pass: smooth
    let mut smoothed = Vec::with_capacity(result.len());
    for i in 0..result.len() {
        let left = if i > 0 { result[i - 1] } else { result[i] };
        let right = if i + 1 < result.len() { result[i + 1] } else { result[i] };
        smoothed.push((left + result[i] + right) / 3);
    }
    smoothed
}

/// Find all local maxima and return their (index, value) pairs
#[inline(never)]
fn bc_08(data: &[u64], min_prominence: u64) -> Vec<(usize, u64)> {
    let n = data.len();
    if n < 3 { return vec![]; }
    let mut peaks = Vec::new();
    for i in 1..n - 1 {
        if data[i] > data[i - 1] && data[i] > data[i + 1] {
            // Check prominence: distance to nearest higher peak
            let mut left_min = data[i];
            for j in (0..i).rev() {
                if data[j] < left_min { left_min = data[j]; }
                if data[j] > data[i] { break; }
            }
            let prominence = data[i] - left_min;
            if prominence >= min_prominence {
                peaks.push((i, data[i]));
            }
        }
    }
    peaks
}

/// Bubble sort with early termination, counting passes
#[inline(never)]
fn bc_09(data: &mut [u64]) -> u64 {
    let n = data.len();
    let mut passes = 0u64;
    loop {
        let mut swapped = false;
        for i in 1..n {
            if data[i - 1] > data[i] {
                data.swap(i - 1, i);
                swapped = true;
            }
        }
        passes += 1;
        if !swapped { break; }
    }
    passes
}

/// Rotate array left by `k` positions using reversal algorithm
#[inline(never)]
fn bc_10(data: &[u64], k: usize) -> Vec<u64> {
    let n = data.len();
    if n == 0 { return vec![]; }
    let k = k % n;
    let mut result: Vec<u64> = data.to_vec();
    // Reverse first k
    let mut lo = 0;
    let mut hi = if k > 0 { k - 1 } else { 0 };
    while lo < hi { result.swap(lo, hi); lo += 1; hi -= 1; }
    // Reverse rest
    lo = k;
    hi = n - 1;
    while lo < hi { result.swap(lo, hi); lo += 1; hi -= 1; }
    // Reverse all
    lo = 0;
    hi = n - 1;
    while lo < hi { result.swap(lo, hi); lo += 1; hi -= 1; }
    result
}

/// Selection sort: find minimum, swap, repeat
#[inline(never)]
fn bc_11(data: &mut [u64]) -> u64 {
    let n = data.len();
    let mut comparisons = 0u64;
    for i in 0..n {
        let mut min_idx = i;
        for j in i + 1..n {
            comparisons += 1;
            if data[j] < data[min_idx] {
                min_idx = j;
            }
        }
        if min_idx != i {
            data.swap(i, min_idx);
        }
    }
    comparisons
}

/// Compute running median using sorted window
#[inline(never)]
fn bc_12(data: &[u64], window: usize) -> Vec<u64> {
    let n = data.len();
    if window == 0 || window > n { return vec![]; }
    let mut result = Vec::with_capacity(n - window + 1);
    let mut win: Vec<u64> = data[..window].to_vec();
    win.sort();
    result.push(win[window / 2]);
    for i in window..n {
        // Remove data[i - window], insert data[i]
        let old = data[i - window];
        let new_val = data[i];
        // Find and remove old
        if let Ok(pos) = win.binary_search(&old) {
            win.remove(pos);
        }
        // Insert new in sorted position
        let insert_pos = win.partition_point(|&x| x < new_val);
        win.insert(insert_pos, new_val);
        result.push(win[window / 2]);
    }
    result
}

/// Count inversions using merge-sort-like approach (simplified)
#[inline(never)]
fn bc_13(data: &[u64]) -> u64 {
    let n = data.len();
    let mut inv = 0u64;
    for i in 0..n {
        for j in i + 1..n {
            if data[i] > data[j] {
                inv += 1;
            }
        }
    }
    inv
}

/// Three-way partition (Dutch National Flag)
#[inline(never)]
fn bc_14(data: &mut [u64], pivot: u64) -> (usize, usize) {
    let n = data.len();
    let mut lo = 0;
    let mut mid = 0;
    let mut hi = n;
    while mid < hi {
        if data[mid] < pivot {
            data.swap(lo, mid);
            lo += 1;
            mid += 1;
        } else if data[mid] > pivot {
            hi -= 1;
            data.swap(mid, hi);
        } else {
            mid += 1;
        }
    }
    (lo, hi)
}

/// Prefix sum then range query simulation
#[inline(never)]
fn bc_15(data: &[u64]) -> u64 {
    let n = data.len();
    if n == 0 { return 0; }
    let mut prefix = vec![0u64; n + 1];
    for i in 0..n {
        prefix[i + 1] = prefix[i].wrapping_add(data[i]);
    }
    // Simulate range queries
    let mut total = 0u64;
    for len in 1..=n.min(10) {
        for start in 0..n - len + 1 {
            let range_sum = prefix[start + len].wrapping_sub(prefix[start]);
            if range_sum > total { total = range_sum; }
        }
    }
    total
}

/// Interleave two halves of array
#[inline(never)]
fn bc_16(data: &[u64], split: usize) -> Vec<u64> {
    let n = data.len();
    let split = split.min(n);
    let mut result = Vec::with_capacity(n);
    let mut i = 0;
    let mut j = split;
    while i < split || j < n {
        if i < split { result.push(data[i]); i += 1; }
        if j < n { result.push(data[j]); j += 1; }
    }
    // Verify interleaving by computing checksum
    let mut check = 0u64;
    for k in 0..result.len() {
        check = check.wrapping_add(result[k].wrapping_mul((k as u64) + 1));
    }
    result.push(check);
    result
}

/// Heap-sift-down: build max-heap in array
#[inline(never)]
fn bc_17(data: &mut [u64]) -> u64 {
    let n = data.len();
    let mut sifts = 0u64;
    // Build heap
    for i in (0..n / 2).rev() {
        let mut parent = i;
        loop {
            let left = 2 * parent + 1;
            let right = 2 * parent + 2;
            let mut largest = parent;
            if left < n && data[left] > data[largest] { largest = left; }
            if right < n && data[right] > data[largest] { largest = right; }
            if largest == parent { break; }
            data.swap(parent, largest);
            parent = largest;
            sifts += 1;
        }
    }
    sifts
}

/// Compute edit-distance-like score between two regions of the same array
#[inline(never)]
fn bc_18(data: &[u64], split: usize) -> u64 {
    let n = data.len();
    let split = split.min(n);
    let a = &data[..split];
    let b = &data[split..];
    let m = a.len();
    let k = b.len();
    if m == 0 || k == 0 { return (m + k) as u64; }
    let mut prev = vec![0u64; k + 1];
    let mut curr = vec![0u64; k + 1];
    for j in 0..=k { prev[j] = j as u64; }
    for i in 1..=m {
        curr[0] = i as u64;
        for j in 1..=k {
            let cost = if a[i - 1] == b[j - 1] { 0u64 } else { 1 };
            curr[j] = (prev[j] + 1)
                .min(curr[j - 1] + 1)
                .min(prev[j - 1] + cost);
        }
        std::mem::swap(&mut prev, &mut curr);
    }
    prev[k]
}

/// Find longest plateau (consecutive equal values)
#[inline(never)]
fn bc_19(data: &[u64]) -> (usize, u64) {
    let n = data.len();
    if n == 0 { return (0, 0); }
    let mut best_len = 1usize;
    let mut best_val = data[0];
    let mut cur_len = 1usize;
    for i in 1..n {
        if data[i] == data[i - 1] {
            cur_len += 1;
        } else {
            if cur_len > best_len {
                best_len = cur_len;
                best_val = data[i - 1];
            }
            cur_len = 1;
        }
    }
    if cur_len > best_len {
        best_len = cur_len;
        best_val = data[n - 1];
    }
    (best_len, best_val)
}

/// Counting sort on values mod `radix`
#[inline(never)]
fn bc_20(data: &mut [u64], radix: usize) -> Vec<u64> {
    if radix == 0 { return data.to_vec(); }
    let n = data.len();
    let mut count = vec![0usize; radix];
    for i in 0..n {
        count[(data[i] as usize) % radix] += 1;
    }
    // Prefix sum
    for i in 1..radix {
        count[i] += count[i - 1];
    }
    let mut output = vec![0u64; n];
    for i in (0..n).rev() {
        let bucket = (data[i] as usize) % radix;
        count[bucket] -= 1;
        output[count[bucket]] = data[i];
    }
    output
}

// ============================================================================
// Category 2: Ownership / Drop (own_01 .. own_20)
// Functions that create, transform, and consume heap allocations.
// Drop glue generated for Vec, String, Box at scope boundaries.
// ============================================================================

struct OwnedMatrix {
    rows: usize,
    cols: usize,
    data: Vec<u64>,
}

impl OwnedMatrix {
    fn new(rows: usize, cols: usize) -> Self {
        Self { rows, cols, data: vec![0; rows * cols] }
    }
    fn get(&self, r: usize, c: usize) -> u64 { self.data[r * self.cols + c] }
    fn set(&mut self, r: usize, c: usize, v: u64) { self.data[r * self.cols + c] = v; }
}

impl Drop for OwnedMatrix {
    #[inline(never)]
    fn drop(&mut self) {
        for v in self.data.iter_mut() { *v = 0; }
    }
}

/// Build a matrix, fill with Fibonacci-like values, compute row sums
#[inline(never)]
fn own_01(n: u64) -> u64 {
    let n = n as usize;
    let mut mat = OwnedMatrix::new(n, n);
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
    // mat drops here → OwnedMatrix::drop zeroes data
}

/// Sort a vec, split into two owned vecs, merge back
#[inline(never)]
fn own_02(mut data: Vec<u64>, ascending: bool) -> Vec<u64> {
    data.sort();
    if !ascending { data.reverse(); }
    let mid = data.len() / 2;
    let left: Vec<u64> = data[..mid].to_vec();
    let right: Vec<u64> = data[mid..].to_vec();
    // Interleave
    let mut result = Vec::with_capacity(data.len());
    let mut i = 0;
    let mut j = 0;
    while i < left.len() || j < right.len() {
        if i < left.len() { result.push(left[i]); i += 1; }
        if j < right.len() { result.push(right[j]); j += 1; }
    }
    result
    // left, right, data all drop
}

/// Split string into words, transform each, rejoin
#[inline(never)]
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

/// Build linked list of Boxes, traverse and sum
#[inline(never)]
fn own_04(n: u64) -> u64 {
    enum List { Cons(u64, Box<List>), Nil }
    let mut head = List::Nil;
    for i in (0..n).rev() {
        let val = i.wrapping_mul(i).wrapping_add(1);
        head = List::Cons(val, Box::new(head));
    }
    let mut sum = 0u64;
    let mut cur = &head;
    let mut count = 0u64;
    loop {
        match cur {
            List::Cons(val, next) => {
                sum = sum.wrapping_add(*val);
                count += 1;
                cur = next;
            }
            List::Nil => break,
        }
    }
    sum.wrapping_mul(count)
    // head drops recursively → each Box freed
}

/// Merge two owned sorted vecs into one, consuming both
#[inline(never)]
fn own_05(a: Vec<u64>, b: Vec<u64>) -> Vec<u64> {
    let mut result = Vec::with_capacity(a.len() + b.len());
    let mut i = 0;
    let mut j = 0;
    while i < a.len() && j < b.len() {
        if a[i] <= b[j] { result.push(a[i]); i += 1; }
        else { result.push(b[j]); j += 1; }
    }
    while i < a.len() { result.push(a[i]); i += 1; }
    while j < b.len() { result.push(b[j]); j += 1; }
    // Compute running max
    let mut max_so_far = 0u64;
    for k in 0..result.len() {
        if result[k] > max_so_far { max_so_far = result[k]; }
        result[k] = max_so_far;
    }
    result
    // a, b consumed (moved), result returned
}

/// Build string by interleaving chars from input with their ASCII codes
#[inline(never)]
fn own_06(s: String) -> String {
    let chars: Vec<char> = s.chars().collect();
    let mut result = String::with_capacity(s.len() * 4);
    for i in 0..chars.len() {
        result.push(chars[i]);
        if chars[i].is_alphabetic() {
            let code = chars[i] as u32;
            let code_str = code.to_string();
            result.push_str(&code_str);
        }
    }
    result
    // s consumed, chars drops, code_str temporaries drop
}

/// Create nested Boxes (binary tree), compute depth-weighted sum
#[inline(never)]
fn own_07(depth: u64) -> u64 {
    struct TreeNode { val: u64, left: Option<Box<TreeNode>>, right: Option<Box<TreeNode>> }
    fn build(d: u64, val: u64) -> Option<Box<TreeNode>> {
        if d == 0 { return None; }
        Some(Box::new(TreeNode {
            val,
            left: build(d - 1, val.wrapping_mul(2).wrapping_add(1)),
            right: build(d - 1, val.wrapping_mul(2).wrapping_add(2)),
        }))
    }
    fn sum_weighted(node: &Option<Box<TreeNode>>, depth: u64) -> u64 {
        match node {
            None => 0,
            Some(n) => {
                n.val.wrapping_mul(depth)
                    .wrapping_add(sum_weighted(&n.left, depth + 1))
                    .wrapping_add(sum_weighted(&n.right, depth + 1))
            }
        }
    }
    let tree = build(depth, 1);
    sum_weighted(&tree, 1)
    // tree drops recursively
}

/// Partition vec into two owned vecs based on predicate, process both
#[inline(never)]
fn own_08(data: Vec<u64>, threshold: u64) -> u64 {
    let mut below = Vec::new();
    let mut above = Vec::new();
    for val in data {
        if val < threshold { below.push(val); } else { above.push(val); }
    }
    // Sort both
    below.sort();
    above.sort();
    // Compute weighted sum
    let mut sum = 0u64;
    for (i, v) in below.iter().enumerate() { sum = sum.wrapping_add(v.wrapping_mul(i as u64 + 1)); }
    for (i, v) in above.iter().enumerate() { sum = sum.wrapping_add(v.wrapping_mul(i as u64 + 10)); }
    sum
    // below, above, data(consumed) all drop
}

/// Build string histogram: count char frequencies, build sorted output
#[inline(never)]
fn own_09(s: String, top_n: usize) -> String {
    let mut freq = [0u32; 256];
    for &b in s.as_bytes() { freq[b as usize] += 1; }
    let mut pairs: Vec<(u8, u32)> = Vec::new();
    for i in 0..256u16 {
        if freq[i as usize] > 0 {
            pairs.push((i as u8, freq[i as usize]));
        }
    }
    pairs.sort_by(|a, b| b.1.cmp(&a.1));
    let mut result = String::new();
    for (i, (ch, count)) in pairs.iter().enumerate() {
        if i >= top_n { break; }
        result.push(*ch as char);
        result.push(':');
        result.push_str(&count.to_string());
        result.push(' ');
    }
    result
    // s, pairs, result(returned), temporaries all managed
}

/// Build Vec of Strings, sort by length then alphabetically
#[inline(never)]
fn own_10(n: u64) -> Vec<String> {
    let mut strings: Vec<String> = Vec::new();
    for i in 0..n {
        let mut s = String::new();
        let len = (i % 5 + 3) as usize;
        for j in 0..len {
            s.push((b'a' + ((i as u8 + j as u8) % 26)) as char);
        }
        strings.push(s);
    }
    strings.sort_by(|a, b| {
        a.len().cmp(&b.len()).then_with(|| a.cmp(b))
    });
    strings
}

/// In-place transform: reverse, then deduplicate adjacent, return both versions
#[inline(never)]
fn own_11(mut data: Vec<u64>, do_reverse: bool) -> (Vec<u64>, Vec<u64>) {
    let original = data.clone();
    if do_reverse { data.reverse(); }
    // Deduplicate adjacent
    let mut deduped = Vec::with_capacity(data.len());
    for i in 0..data.len() {
        if i == 0 || data[i] != data[i - 1] {
            deduped.push(data[i]);
        }
    }
    (original, deduped)
    // data drops, original and deduped returned
}

/// Split string on spaces, reverse each word, rebuild
#[inline(never)]
fn own_12(s: String) -> String {
    let words: Vec<&str> = s.split_whitespace().collect();
    let mut reversed_words: Vec<String> = Vec::with_capacity(words.len());
    for word in &words {
        let mut rev: String = word.chars().rev().collect();
        // Capitalize first char
        if let Some(first) = rev.chars().next() {
            let upper: String = first.to_uppercase().collect();
            rev = upper + &rev[first.len_utf8()..];
        }
        reversed_words.push(rev);
    }
    reversed_words.join(" ")
}

/// Sieve of Eratosthenes, return primes as owned Vec
#[inline(never)]
fn own_13(limit: u64) -> Vec<u64> {
    let n = limit as usize;
    if n < 2 { return vec![]; }
    let mut is_prime = vec![true; n + 1];
    is_prime[0] = false;
    if n >= 1 { is_prime[1] = false; }
    let mut i = 2;
    while i * i <= n {
        if is_prime[i] {
            let mut j = i * i;
            while j <= n {
                is_prime[j] = false;
                j += i;
            }
        }
        i += 1;
    }
    let mut primes = Vec::new();
    for i in 2..=n { if is_prime[i] { primes.push(i as u64); } }
    primes
    // is_prime drops
}

/// Run-length encode a vec, return vec of (value, count) pairs
#[inline(never)]
fn own_14(data: Vec<u64>, min_run: usize) -> Vec<(u64, usize)> {
    let mut runs: Vec<(u64, usize)> = Vec::new();
    let mut i = 0;
    while i < data.len() {
        let val = data[i];
        let mut count = 1;
        while i + count < data.len() && data[i + count] == val {
            count += 1;
        }
        if count >= min_run {
            runs.push((val, count));
        }
        i += count;
    }
    runs
    // data consumed
}

/// Build frequency map of chars, filter and format
#[inline(never)]
fn own_15(s: String, filter_char: char) -> String {
    let filtered: String = s.chars().filter(|&c| c != filter_char).collect();
    let mut freq: Vec<(char, usize)> = Vec::new();
    for ch in filtered.chars() {
        let mut found = false;
        for pair in freq.iter_mut() {
            if pair.0 == ch { pair.1 += 1; found = true; break; }
        }
        if !found { freq.push((ch, 1)); }
    }
    freq.sort_by(|a, b| b.1.cmp(&a.1));
    let mut result = String::new();
    for (ch, count) in &freq {
        for _ in 0..*count { result.push(*ch); }
    }
    result
    // s, filtered, freq, result all drop appropriately
}

/// Build binary heap in vec, extract top k elements
#[inline(never)]
fn own_16(k: u64) -> Vec<u64> {
    let n = 4 * k;
    let mut heap: Vec<u64> = Vec::with_capacity(n as usize);
    for i in 0..n {
        let val = (i.wrapping_mul(7).wrapping_add(13)) % (n * 2);
        heap.push(val);
        // Sift up
        let mut idx = heap.len() - 1;
        while idx > 0 {
            let parent = (idx - 1) / 2;
            if heap[idx] > heap[parent] { heap.swap(idx, parent); idx = parent; }
            else { break; }
        }
    }
    // Extract top k
    let mut result = Vec::with_capacity(k as usize);
    for _ in 0..k.min(n) {
        if heap.is_empty() { break; }
        let top = heap[0];
        let last = heap.len() - 1;
        heap.swap(0, last);
        heap.pop();
        result.push(top);
        // Sift down
        let mut idx = 0;
        loop {
            let left = 2 * idx + 1;
            let right = 2 * idx + 2;
            let mut largest = idx;
            if left < heap.len() && heap[left] > heap[largest] { largest = left; }
            if right < heap.len() && heap[right] > heap[largest] { largest = right; }
            if largest == idx { break; }
            heap.swap(idx, largest);
            idx = largest;
        }
    }
    result
    // heap drops
}

/// Chunk vec, transform each chunk independently, flatten
#[inline(never)]
fn own_17(data: Vec<u64>, chunk_size: usize) -> Vec<u64> {
    if chunk_size == 0 { return data; }
    let chunks: Vec<Vec<u64>> = data.chunks(chunk_size).map(|c| c.to_vec()).collect();
    let mut result = Vec::new();
    for mut chunk in chunks {
        chunk.sort();
        chunk.reverse();
        result.extend(chunk);
    }
    result
    // data consumed, individual chunks drop
}

/// Interleave two strings char-by-char, handling different lengths
#[inline(never)]
fn own_18(a: String, b: String) -> String {
    let a_chars: Vec<char> = a.chars().collect();
    let b_chars: Vec<char> = b.chars().collect();
    let max_len = a_chars.len().max(b_chars.len());
    let mut result = String::with_capacity(max_len * 2);
    for i in 0..max_len {
        if i < a_chars.len() { result.push(a_chars[i]); }
        if i < b_chars.len() { result.push(b_chars[i]); }
    }
    // Also compute reverse
    let rev: String = result.chars().rev().collect();
    if rev.len() > result.len() { rev } else { result }
}

/// Build adjacency matrix in vec, compute reachability
#[inline(never)]
fn own_19(n: u64) -> u64 {
    let n = n as usize;
    let mut adj = vec![false; n * n];
    for i in 0..n {
        if i + 1 < n { adj[i * n + i + 1] = true; }
        if i + 2 < n { adj[i * n + i + 2] = true; }
    }
    // Floyd-Warshall-like reachability
    let mut reach = adj.clone();
    for k in 0..n {
        for i in 0..n {
            for j in 0..n {
                if reach[i * n + k] && reach[k * n + j] {
                    reach[i * n + j] = true;
                }
            }
        }
    }
    reach.iter().filter(|&&b| b).count() as u64
    // adj, reach drop
}

/// Sort vec, remove duplicates, compute cumulative product (mod 2^64)
#[inline(never)]
fn own_20(mut data: Vec<u64>, do_sort: bool) -> Vec<u64> {
    if do_sort { data.sort(); }
    data.dedup();
    let mut cum = Vec::with_capacity(data.len());
    let mut prod = 1u64;
    for val in &data {
        prod = prod.wrapping_mul(val.wrapping_add(1));
        cum.push(prod);
    }
    cum
    // data drops
}

// ============================================================================
// Category 3: Option / Result (opt_01 .. opt_20)
// Multi-step computations using Option/Result with real error handling.
// ============================================================================

/// Binary search returning Option, then probe neighbors
#[inline(never)]
fn opt_01(data: &[u64], target: u64) -> u64 {
    let mut lo = 0usize;
    let mut hi = data.len();
    let mut found: Option<usize> = None;
    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        match data[mid].cmp(&target) {
            std::cmp::Ordering::Equal => { found = Some(mid); break; }
            std::cmp::Ordering::Less => lo = mid + 1,
            std::cmp::Ordering::Greater => hi = mid,
        }
    }
    match found {
        Some(idx) => {
            let left = if idx > 0 { data.get(idx - 1).copied() } else { None };
            let right = data.get(idx + 1).copied();
            let sum = left.unwrap_or(0) + data[idx] + right.unwrap_or(0);
            sum
        }
        None => {
            // Return nearest value
            data.get(lo).copied()
                .or_else(|| data.last().copied())
                .unwrap_or(0)
        }
    }
}

/// Split string on delimiter, parse segments as usize, return valid token count
#[inline(never)]
fn opt_02(s: &str, delim: char) -> u64 {
    let mut count = 0u64;
    let mut total = 0u64;
    let mut max_val: Option<u64> = None;
    for part in s.split(delim) {
        let trimmed = part.trim();
        if trimmed.is_empty() { continue; }
        match trimmed.parse::<u64>() {
            Ok(val) => {
                count += 1;
                total += val;
                max_val = Some(match max_val {
                    Some(cur) => if val > cur { val } else { cur },
                    None => val,
                });
            }
            Err(_) => {
                // Count non-numeric tokens
                count += trimmed.len() as u64;
            }
        }
    }
    total.wrapping_add(max_val.unwrap_or(0)).wrapping_add(count)
}

/// Process array of Option<u64>: compute running sum skipping None
#[inline(never)]
fn opt_03(data: &[Option<u64>]) -> u64 {
    let mut sum = 0u64;
    let mut prev: Option<u64> = None;
    let mut transitions = 0u64;
    for item in data {
        match (prev, item) {
            (Some(p), Some(v)) => {
                sum = sum.wrapping_add(*v);
                if *v > p { transitions += 1; }
                prev = Some(*v);
            }
            (None, Some(v)) => {
                sum = sum.wrapping_add(*v);
                transitions += 1;
                prev = Some(*v);
            }
            (Some(_), None) => {
                transitions += 1;
                prev = None;
            }
            (None, None) => {}
        }
    }
    sum.wrapping_mul(transitions + 1)
}

/// Sliding window search: find first window where all elements > target
#[inline(never)]
fn opt_04(data: &[u64], target: u64) -> Option<(usize, u64)> {
    let win_size = 3;
    if data.len() < win_size { return None; }
    for start in 0..data.len() - win_size + 1 {
        let mut all_above = true;
        let mut win_sum = 0u64;
        for j in 0..win_size {
            let val = data.get(start + j)?;
            win_sum += val;
            if *val <= target { all_above = false; }
        }
        if all_above {
            return Some((start, win_sum));
        }
    }
    None
}

/// Parse space-separated tokens: numbers are Ok, words are Err, compute stats
#[inline(never)]
fn opt_05(s: &str, limit: usize) -> u64 {
    let mut numbers: Vec<u64> = Vec::new();
    let mut errors = 0u64;
    let mut count = 0usize;
    for token in s.split_whitespace() {
        if count >= limit { break; }
        match token.parse::<u64>() {
            Ok(val) => numbers.push(val),
            Err(_) => errors += 1,
        }
        count += 1;
    }
    if numbers.is_empty() { return errors; }
    numbers.sort();
    let median = numbers.get(numbers.len() / 2).copied().unwrap_or(0);
    let sum: u64 = numbers.iter().sum();
    sum.wrapping_add(median).wrapping_add(errors)
}

/// Chain of Option transformations: find, filter, map, with fallback at each step
#[inline(never)]
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

/// Parse key=value pairs from string, accumulate valid ones
#[inline(never)]
fn opt_07(s: &str) -> u64 {
    let mut total = 0u64;
    let mut count = 0u64;
    for part in s.split_whitespace() {
        let kv: Option<(&str, &str)> = part.split_once('=');
        match kv {
            Some((key, val)) => {
                if let Ok(v) = val.parse::<u64>() {
                    total = total.wrapping_add(v);
                    count += 1;
                } else {
                    total = total.wrapping_add(key.len() as u64);
                }
            }
            None => {
                if let Some(first_char) = part.chars().next() {
                    total = total.wrapping_add(first_char as u64);
                }
            }
        }
    }
    total.wrapping_mul(count.wrapping_add(1))
}

/// Process array of Result<u64, &str>: accumulate Oks, count errors, handle streaks
#[inline(never)]
fn opt_08(data: &[Result<u64, &str>]) -> u64 {
    let mut sum = 0u64;
    let mut err_streak = 0u64;
    let mut max_streak = 0u64;
    let mut last_ok: Option<u64> = None;
    for item in data {
        match item {
            Ok(v) => {
                if err_streak > max_streak { max_streak = err_streak; }
                err_streak = 0;
                sum = sum.wrapping_add(*v);
                last_ok = Some(match last_ok {
                    Some(prev) => prev.wrapping_add(*v),
                    None => *v,
                });
            }
            Err(msg) => {
                err_streak += 1;
                sum = sum.wrapping_add(msg.len() as u64);
            }
        }
    }
    if err_streak > max_streak { max_streak = err_streak; }
    sum.wrapping_add(max_streak).wrapping_add(last_ok.unwrap_or(0))
}

/// Two-pointer search on sorted data with Option-based bounds checking
#[inline(never)]
fn opt_09(data: &[u64], target_sum: u64) -> Option<(usize, usize)> {
    if data.len() < 2 { return None; }
    let mut lo = 0usize;
    let mut hi = data.len() - 1;
    while lo < hi {
        let left = data.get(lo)?;
        let right = data.get(hi)?;
        let sum = left.wrapping_add(*right);
        if sum == target_sum {
            return Some((lo, hi));
        } else if sum < target_sum {
            lo += 1;
        } else {
            hi -= 1;
        }
    }
    None
}

/// Extract nth word, then nth character, with Option chaining
#[inline(never)]
fn opt_10(s: &str, n: usize) -> u64 {
    let word: Option<&str> = s.split_whitespace().nth(n);
    let ch: Option<char> = word.and_then(|w| w.chars().nth(n % w.len().max(1)));
    let code = ch.map(|c| c as u64).unwrap_or(0);

    // Also try from the end
    let rword: Option<&str> = s.split_whitespace().rev().nth(n);
    let rch: Option<char> = rword.and_then(|w| w.chars().rev().nth(n % w.len().max(1)));
    let rcode = rch.map(|c| c as u64).unwrap_or(0);

    code.wrapping_add(rcode)
}

/// Find first pair of adjacent elements with given property
#[inline(never)]
fn opt_11(data: &[u64]) -> u64 {
    let n = data.len();
    let ascending_pair: Option<(u64, u64)> = (0..n.saturating_sub(1))
        .find_map(|i| {
            let a = *data.get(i)?;
            let b = *data.get(i + 1)?;
            if b > a + 5 { Some((a, b)) } else { None }
        });
    let descending_pair: Option<(u64, u64)> = (0..n.saturating_sub(1))
        .find_map(|i| {
            let a = *data.get(i)?;
            let b = *data.get(i + 1)?;
            if a > b + 5 { Some((a, b)) } else { None }
        });
    let asc_sum = ascending_pair.map(|(a, b)| a + b).unwrap_or(0);
    let desc_sum = descending_pair.map(|(a, b)| a + b).unwrap_or(0);
    asc_sum.wrapping_add(desc_sum)
}

/// Process optional values with threshold filtering
#[inline(never)]
fn opt_12(data: &[Option<u64>], threshold: u64) -> u64 {
    let mut above = 0u64;
    let mut below = 0u64;
    let mut none_count = 0u64;
    for item in data {
        match item {
            Some(v) if *v > threshold => { above = above.wrapping_add(*v); }
            Some(v) => { below = below.wrapping_add(*v); }
            None => { none_count += 1; }
        }
    }
    above.wrapping_mul(2).wrapping_add(below).wrapping_add(none_count * 100)
}

/// Chained get() calls with cascading fallbacks
#[inline(never)]
fn opt_13(data: &[u64], step: usize) -> u64 {
    let mut idx = 0usize;
    let mut acc = 0u64;
    let mut hops = 0u64;
    loop {
        match data.get(idx) {
            Some(&val) => {
                acc = acc.wrapping_add(val);
                hops += 1;
                let next = idx.wrapping_add(step);
                if next >= data.len() || next <= idx && step == 0 { break; }
                idx = next;
            }
            None => break,
        }
    }
    acc.wrapping_mul(hops)
}

/// Parse multiple number formats from a string
#[inline(never)]
fn opt_14(s: &str) -> u64 {
    let mut total = 0u64;
    let mut parsed = 0u64;
    let mut failed = 0u64;
    for token in s.split_whitespace() {
        let result: Result<u64, _> = if token.starts_with("0x") {
            u64::from_str_radix(&token[2..], 16)
        } else if token.starts_with("0b") {
            u64::from_str_radix(&token[2..], 2)
        } else {
            token.parse()
        };
        match result {
            Ok(val) => { total = total.wrapping_add(val); parsed += 1; }
            Err(_) => { failed += 1; }
        }
    }
    total.wrapping_add(parsed * 10).wrapping_add(failed)
}

/// Sliding window with Option-based boundary handling
#[inline(never)]
fn opt_15(data: &[u64], window: usize) -> u64 {
    let mut best_sum = 0u64;
    let mut best_start: Option<usize> = None;
    for start in 0..data.len().saturating_sub(window - 1) {
        let mut win_sum = 0u64;
        let mut valid = true;
        for j in 0..window {
            match data.get(start + j) {
                Some(&v) => win_sum = win_sum.wrapping_add(v),
                None => { valid = false; break; }
            }
        }
        if valid && win_sum > best_sum {
            best_sum = win_sum;
            best_start = Some(start);
        }
    }
    best_sum.wrapping_add(best_start.unwrap_or(0) as u64)
}

/// Process Result array: compute running positive/negative balance
#[inline(never)]
fn opt_16(data: &[Result<i64, &str>]) -> i64 {
    let mut balance = 0i64;
    let mut max_balance = 0i64;
    let mut min_balance = 0i64;
    let mut last_valid: Option<i64> = None;
    for item in data {
        match item {
            Ok(v) => {
                balance += v;
                if balance > max_balance { max_balance = balance; }
                if balance < min_balance { min_balance = balance; }
                last_valid = Some(balance);
            }
            Err(_) => {
                balance = last_valid.unwrap_or(0);
            }
        }
    }
    max_balance - min_balance + last_valid.unwrap_or(0)
}

/// Find k-th element using Option for bounds safety
#[inline(never)]
fn opt_17(data: &[u64], k: usize) -> u64 {
    let mut sorted = data.to_vec();
    sorted.sort();
    let kth = sorted.get(k).copied();
    let rev_kth = sorted.get(sorted.len().saturating_sub(k + 1)).copied();
    let median = sorted.get(sorted.len() / 2).copied();
    kth.unwrap_or(0)
        .wrapping_add(rev_kth.unwrap_or(0))
        .wrapping_add(median.unwrap_or(0))
}

/// Longest word and shortest word via Option chaining
#[inline(never)]
fn opt_18(s: &str) -> u64 {
    let words: Vec<&str> = s.split_whitespace().collect();
    let longest: Option<&&str> = words.iter().max_by_key(|w| w.len());
    let shortest: Option<&&str> = words.iter().min_by_key(|w| w.len());
    let long_val = longest.map(|w| w.len() as u64).unwrap_or(0);
    let short_val = shortest.map(|w| w.len() as u64).unwrap_or(0);
    let mid_word = words.get(words.len() / 2).map(|w| w.len() as u64).unwrap_or(0);
    long_val.wrapping_mul(100).wrapping_add(short_val).wrapping_add(mid_word)
}

/// Binary search with Result: return index or insertion point
#[inline(never)]
fn opt_19(data: &[u64], target: u64) -> u64 {
    let mut lo = 0usize;
    let mut hi = data.len();
    let mut result: Result<usize, usize> = Err(lo);
    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        match data.get(mid) {
            Some(&val) if val == target => { result = Ok(mid); break; }
            Some(&val) if val < target => { lo = mid + 1; result = Err(lo); }
            Some(_) => { hi = mid; result = Err(hi); }
            None => break,
        }
    }
    match result {
        Ok(idx) => idx as u64 * 1000,
        Err(insert) => insert as u64,
    }
}

/// Parse CSV-like string into numbers with comprehensive error handling
#[inline(never)]
fn opt_20(s: &str) -> u64 {
    let mut sum = 0u64;
    let mut count = 0u64;
    let mut max_val: Option<u64> = None;
    let mut min_val: Option<u64> = None;
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
    let range = match (max_val, min_val) {
        (Some(mx), Some(mn)) => mx - mn,
        _ => 0,
    };
    sum.wrapping_add(range).wrapping_add(count)
}

// ============================================================================
// Category 4: Iterators (iter_01 .. iter_20)
// Complex iterator chains that generate state-machine loops.
// Each function uses multiple chained adapters.
// ============================================================================

/// Filter, enumerate, and accumulate with index-weighted sum
#[inline(never)]
fn iter_01(data: &[u64], threshold: u64) -> u64 {
    let above: Vec<(usize, &u64)> = data.iter()
        .enumerate()
        .filter(|(_, &v)| v > threshold)
        .collect();
    let mut sum = 0u64;
    for (idx, &val) in &above {
        sum = sum.wrapping_add(val.wrapping_mul(*idx as u64 + 1));
    }
    // Also compute product of first 5
    let prod: u64 = above.iter()
        .take(5)
        .map(|(_, &v)| v)
        .fold(1u64, |a, b| a.wrapping_mul(b));
    sum.wrapping_add(prod)
}

/// Zip two slices, compute weighted dot product with running max
#[inline(never)]
fn iter_02(a: &[u64], b: &[u64]) -> u64 {
    let mut dot = 0u64;
    let mut max_product = 0u64;
    let mut count = 0u64;
    for (i, (&x, &y)) in a.iter().zip(b.iter()).enumerate() {
        let weight = (i as u64 + 1).min(10);
        let product = x.wrapping_mul(y);
        dot = dot.wrapping_add(product.wrapping_mul(weight));
        if product > max_product { max_product = product; }
        count += 1;
    }
    dot.wrapping_add(max_product).wrapping_add(count)
}

/// Windows + map + filter chain
#[inline(never)]
fn iter_03(data: &[u64], window: usize) -> u64 {
    if window == 0 { return 0; }
    let window_sums: Vec<u64> = data.windows(window)
        .map(|w| {
            let mut s = 0u64;
            for &v in w { s = s.wrapping_add(v); }
            s
        })
        .collect();
    // Find windows where sum exceeds average
    let total: u64 = window_sums.iter().sum();
    let avg = if window_sums.is_empty() { 0 } else { total / window_sums.len() as u64 };
    let above_avg: u64 = window_sums.iter()
        .filter(|&&s| s > avg)
        .count() as u64;
    total.wrapping_add(above_avg)
}

/// Character frequency analysis with iterators
#[inline(never)]
fn iter_04(s: &str) -> u64 {
    let mut freq = [0u64; 256];
    for b in s.bytes() { freq[b as usize] += 1; }
    let max_freq = freq.iter().copied().max().unwrap_or(0);
    let unique: u64 = freq.iter().filter(|&&f| f > 0).count() as u64;
    let total: u64 = freq.iter().sum();
    // Entropy-like measure
    let mut entropy_sum = 0u64;
    for &f in freq.iter() {
        if f > 0 {
            entropy_sum = entropy_sum.wrapping_add(f.wrapping_mul(f));
        }
    }
    max_freq.wrapping_add(unique).wrapping_add(total).wrapping_add(entropy_sum)
}

/// Chunk, transform each chunk, flatten, then reduce
#[inline(never)]
fn iter_05(data: &[u64]) -> u64 {
    let chunk_results: Vec<u64> = data.chunks(4)
        .map(|chunk| {
            let sum: u64 = chunk.iter().sum();
            let max = chunk.iter().max().copied().unwrap_or(0);
            let min = chunk.iter().min().copied().unwrap_or(0);
            sum.wrapping_add(max.wrapping_sub(min))
        })
        .collect();
    let mut running = 0u64;
    let mut peak = 0u64;
    for &v in &chunk_results {
        running = running.wrapping_add(v);
        if running > peak { peak = running; }
    }
    peak
}

/// Step_by + enumerate + scan (stateful iteration)
#[inline(never)]
fn iter_06(data: &[u64], step: usize) -> u64 {
    if step == 0 { return 0; }
    let stepped: Vec<(usize, &u64)> = data.iter().step_by(step).enumerate().collect();
    let mut state = 0u64;
    let mut result = 0u64;
    for (idx, &val) in &stepped {
        state = state.wrapping_add(val);
        if state > *idx as u64 * 10 {
            result = result.wrapping_add(state);
        }
    }
    result
}

/// Split string, map to lengths, filter, fold
#[inline(never)]
fn iter_07(s: &str, delim: char) -> u64 {
    let parts: Vec<&str> = s.split(delim).collect();
    let lengths: Vec<usize> = parts.iter().map(|p| p.trim().len()).collect();
    let long_count: u64 = lengths.iter().filter(|&&l| l > 3).count() as u64;
    let total_len: u64 = lengths.iter().map(|&l| l as u64).sum();
    let max_len = lengths.iter().max().copied().unwrap_or(0) as u64;
    long_count.wrapping_mul(max_len).wrapping_add(total_len)
}

/// Chain two iterators, take_while, skip, enumerate
#[inline(never)]
fn iter_08(data: &[u64], split: usize) -> u64 {
    let split = split.min(data.len());
    let first_half = data[..split].iter();
    let second_half = data[split..].iter();
    let chained: Vec<&u64> = first_half.chain(second_half)
        .skip(2)
        .take_while(|&&v| v < 50)
        .collect();
    let mut weighted_sum = 0u64;
    for (i, &&v) in chained.iter().enumerate() {
        weighted_sum = weighted_sum.wrapping_add(v.wrapping_mul(i as u64 + 1));
    }
    weighted_sum.wrapping_add(chained.len() as u64)
}

/// Peekable iterator: detect patterns
#[inline(never)]
fn iter_09(data: &[u64]) -> u64 {
    let mut iter = data.iter().peekable();
    let mut ascending_runs = 0u64;
    let mut current_run = 1u64;
    let mut max_run = 0u64;
    while let Some(&val) = iter.next() {
        if let Some(&&next) = iter.peek() {
            if next > val {
                current_run += 1;
            } else {
                if current_run > max_run { max_run = current_run; }
                if current_run > 1 { ascending_runs += 1; }
                current_run = 1;
            }
        }
    }
    if current_run > max_run { max_run = current_run; }
    if current_run > 1 { ascending_runs += 1; }
    max_run.wrapping_mul(ascending_runs)
}

/// Flat_map with conditional expansion
#[inline(never)]
fn iter_10(data: &[u64], factor: u64) -> u64 {
    let expanded: Vec<u64> = data.iter()
        .flat_map(|&v| {
            if v % 2 == 0 {
                vec![v, v.wrapping_mul(factor)]
            } else {
                vec![v]
            }
        })
        .collect();
    let mut sum = 0u64;
    let mut prev = 0u64;
    for &v in &expanded {
        sum = sum.wrapping_add(v.wrapping_sub(prev));
        prev = v;
    }
    sum.wrapping_add(expanded.len() as u64)
}

/// Multi-pass string analysis with iterators
#[inline(never)]
fn iter_11(s: &str) -> u64 {
    let words: Vec<&str> = s.split_whitespace().collect();
    let total_chars: u64 = words.iter().map(|w| w.len() as u64).sum();
    let vowel_words: u64 = words.iter()
        .filter(|w| w.chars().any(|c| "aeiouAEIOU".contains(c)))
        .count() as u64;
    let longest_word_len: u64 = words.iter()
        .map(|w| w.len())
        .max()
        .unwrap_or(0) as u64;
    let cap_count: u64 = words.iter()
        .flat_map(|w| w.chars())
        .filter(|c| c.is_uppercase())
        .count() as u64;
    total_chars.wrapping_add(vowel_words * 10).wrapping_add(longest_word_len).wrapping_add(cap_count)
}

/// Scan (running accumulation) with threshold detection
#[inline(never)]
fn iter_12(data: &[u64], threshold: u64) -> u64 {
    let running: Vec<u64> = data.iter()
        .scan(0u64, |state, &x| {
            *state = state.wrapping_add(x);
            Some(*state)
        })
        .collect();
    let crossings: u64 = running.windows(2)
        .filter(|w| (w[0] < threshold) != (w[1] < threshold))
        .count() as u64;
    let final_val = running.last().copied().unwrap_or(0);
    final_val.wrapping_add(crossings * 100)
}

/// Zip, map, filter, collect with statistics
#[inline(never)]
fn iter_13(a: &[u64], b: &[u64]) -> u64 {
    let diffs: Vec<i64> = a.iter().zip(b.iter())
        .map(|(&x, &y)| x as i64 - y as i64)
        .collect();
    let positive: u64 = diffs.iter().filter(|&&d| d > 0).count() as u64;
    let negative: u64 = diffs.iter().filter(|&&d| d < 0).count() as u64;
    let abs_sum: u64 = diffs.iter().map(|d| d.unsigned_abs()).sum();
    positive.wrapping_mul(100).wrapping_add(negative).wrapping_add(abs_sum)
}

/// Enumerate + filter_map + fold
#[inline(never)]
fn iter_14(data: &[u64]) -> u64 {
    let result: u64 = data.iter()
        .enumerate()
        .filter_map(|(i, &v)| {
            if v > i as u64 {
                Some(v.wrapping_sub(i as u64))
            } else {
                None
            }
        })
        .fold(0u64, |acc, v| acc.wrapping_add(v.wrapping_mul(v)));
    let rev_result: u64 = data.iter()
        .rev()
        .enumerate()
        .filter_map(|(i, &v)| {
            if i > 0 && v % (i as u64) == 0 { Some(v) } else { None }
        })
        .sum();
    result.wrapping_add(rev_result)
}

/// Split, map, interleave with zip, collect
#[inline(never)]
fn iter_15(s: &str, n: usize) -> u64 {
    let words: Vec<&str> = s.split_whitespace().collect();
    let lengths: Vec<usize> = words.iter().map(|w| w.len()).collect();
    let shifted: Vec<usize> = lengths.iter().skip(n).chain(lengths.iter().take(n)).copied().collect();
    let paired: u64 = lengths.iter().zip(shifted.iter())
        .map(|(&a, &b)| (a as u64).wrapping_mul(b as u64))
        .sum();
    paired.wrapping_add(words.len() as u64)
}

/// Group consecutive elements, compute per-group stats
#[inline(never)]
fn iter_16(data: &[u64], group_size: usize) -> u64 {
    if group_size == 0 { return 0; }
    let groups: Vec<&[u64]> = data.chunks(group_size).collect();
    let group_sums: Vec<u64> = groups.iter().map(|g| g.iter().sum()).collect();
    let group_maxes: Vec<u64> = groups.iter().map(|g| g.iter().max().copied().unwrap_or(0)).collect();
    let total: u64 = group_sums.iter().zip(group_maxes.iter())
        .map(|(&s, &m)| s.wrapping_add(m))
        .sum();
    total
}

/// Dedup with counting via iterator
#[inline(never)]
fn iter_17(data: &[u64]) -> u64 {
    let mut sorted = data.to_vec();
    sorted.sort();
    let mut runs: Vec<(u64, u64)> = Vec::new();
    let mut i = 0;
    while i < sorted.len() {
        let val = sorted[i];
        let mut count = 0u64;
        while i < sorted.len() && sorted[i] == val { count += 1; i += 1; }
        runs.push((val, count));
    }
    runs.iter()
        .filter(|(_, c)| *c > 1)
        .map(|(v, c)| v.wrapping_mul(*c))
        .sum()
}

/// Rev + take + skip + enumerate + fold
#[inline(never)]
fn iter_18(data: &[u64], k: usize) -> u64 {
    let tail: Vec<(usize, &u64)> = data.iter()
        .rev()
        .skip(k)
        .take(k * 2)
        .enumerate()
        .collect();
    let weighted: u64 = tail.iter()
        .map(|(i, &v)| v.wrapping_mul(*i as u64 + 1))
        .sum();
    let max_val: u64 = tail.iter()
        .map(|(_, &v)| v)
        .max()
        .unwrap_or(0);
    weighted.wrapping_add(max_val)
}

/// Multi-pass: byte analysis of string with iterators
#[inline(never)]
fn iter_19(s: &str) -> u64 {
    let bytes = s.as_bytes();
    let alpha: u64 = bytes.iter().filter(|b| b.is_ascii_alphabetic()).count() as u64;
    let digit: u64 = bytes.iter().filter(|b| b.is_ascii_digit()).count() as u64;
    let space: u64 = bytes.iter().filter(|b| b.is_ascii_whitespace()).count() as u64;
    let xor_sum: u64 = bytes.iter().fold(0u64, |acc, &b| acc ^ (b as u64));
    let byte_sum: u64 = bytes.iter().map(|&b| b as u64).sum();
    alpha.wrapping_mul(100).wrapping_add(digit * 10).wrapping_add(space).wrapping_add(xor_sum).wrapping_add(byte_sum)
}

/// Partition + separate processing + merge
#[inline(never)]
fn iter_20(data: &[u64], modulus: u64) -> u64 {
    if modulus == 0 { return 0; }
    let (evens, odds): (Vec<&u64>, Vec<&u64>) = data.iter()
        .partition(|&&v| v % modulus == 0);
    let even_sum: u64 = evens.iter().enumerate()
        .map(|(i, &&v)| v.wrapping_mul(i as u64 + 1))
        .sum();
    let odd_sum: u64 = odds.iter().enumerate()
        .map(|(i, &&v)| v.wrapping_add(i as u64))
        .sum();
    even_sum.wrapping_add(odd_sum)
}

// ============================================================================
// Category 5: Enum / Pattern Matching (em_01 .. em_20)
// A mini expression language with lexer, parser, evaluator, and transformers.
// ============================================================================

#[derive(Debug, Clone)]
enum Token {
    Num(i64),
    Ident(String),
    Plus, Minus, Star, Slash,
    LParen, RParen,
    Eof,
}

#[derive(Debug, Clone)]
enum Expr {
    Lit(i64),
    Var(String),
    BinOp(Box<Expr>, Op, Box<Expr>),
    UnaryMinus(Box<Expr>),
    Call(String, Vec<Expr>),
}

#[derive(Debug, Clone, Copy)]
enum Op { Add, Sub, Mul, Div }

#[derive(Debug, Clone)]
enum Cmd {
    Set(String, CVal),
    Add(String, String, String),
    Print(String),
    If(String, Vec<Cmd>, Vec<Cmd>),
}

#[derive(Debug, Clone)]
enum CVal {
    Int(i64),
    Str(String),
    List(Vec<i64>),
}

/// Lexer: tokenize expression string
#[inline(never)]
fn lex(input: &str) -> Vec<Token> {
    let mut tokens = Vec::new();
    let bytes = input.as_bytes();
    let mut i = 0;
    while i < bytes.len() {
        match bytes[i] {
            b' ' | b'\t' => { i += 1; }
            b'+' => { tokens.push(Token::Plus); i += 1; }
            b'-' => { tokens.push(Token::Minus); i += 1; }
            b'*' => { tokens.push(Token::Star); i += 1; }
            b'/' => { tokens.push(Token::Slash); i += 1; }
            b'(' => { tokens.push(Token::LParen); i += 1; }
            b')' => { tokens.push(Token::RParen); i += 1; }
            b'0'..=b'9' => {
                let start = i;
                while i < bytes.len() && bytes[i].is_ascii_digit() { i += 1; }
                let num: i64 = input[start..i].parse().unwrap_or(0);
                tokens.push(Token::Num(num));
            }
            b'a'..=b'z' | b'A'..=b'Z' | b'_' => {
                let start = i;
                while i < bytes.len() && (bytes[i].is_ascii_alphanumeric() || bytes[i] == b'_') { i += 1; }
                tokens.push(Token::Ident(input[start..i].to_string()));
            }
            _ => { i += 1; }
        }
    }
    tokens.push(Token::Eof);
    tokens
}

/// Simple recursive descent parser
fn parse_expr(input: &str) -> Expr {
    let tokens = lex(input);
    let mut pos = 0;
    parse_add(&tokens, &mut pos)
}

fn parse_add(tokens: &[Token], pos: &mut usize) -> Expr {
    let mut left = parse_mul(tokens, pos);
    loop {
        match tokens.get(*pos) {
            Some(Token::Plus) => { *pos += 1; let right = parse_mul(tokens, pos); left = Expr::BinOp(Box::new(left), Op::Add, Box::new(right)); }
            Some(Token::Minus) => { *pos += 1; let right = parse_mul(tokens, pos); left = Expr::BinOp(Box::new(left), Op::Sub, Box::new(right)); }
            _ => return left,
        }
    }
}

fn parse_mul(tokens: &[Token], pos: &mut usize) -> Expr {
    let mut left = parse_atom(tokens, pos);
    loop {
        match tokens.get(*pos) {
            Some(Token::Star) => { *pos += 1; let right = parse_atom(tokens, pos); left = Expr::BinOp(Box::new(left), Op::Mul, Box::new(right)); }
            Some(Token::Slash) => { *pos += 1; let right = parse_atom(tokens, pos); left = Expr::BinOp(Box::new(left), Op::Div, Box::new(right)); }
            _ => return left,
        }
    }
}

fn parse_atom(tokens: &[Token], pos: &mut usize) -> Expr {
    match tokens.get(*pos) {
        Some(Token::Num(n)) => { let v = *n; *pos += 1; Expr::Lit(v) }
        Some(Token::Ident(name)) => { let n = name.clone(); *pos += 1; Expr::Var(n) }
        Some(Token::Minus) => { *pos += 1; let inner = parse_atom(tokens, pos); Expr::UnaryMinus(Box::new(inner)) }
        Some(Token::LParen) => { *pos += 1; let e = parse_add(tokens, pos); if matches!(tokens.get(*pos), Some(Token::RParen)) { *pos += 1; } e }
        _ => Expr::Lit(0),
    }
}

/// Evaluate expression with variable environment
#[inline(never)]
fn em_01(tokens: &[Token]) -> i64 {
    let mut sum = 0i64;
    let mut depth = 0i64;
    let mut max_depth = 0i64;
    let mut num_count = 0i64;
    for tok in tokens {
        match tok {
            Token::Num(n) => { sum += n; num_count += 1; }
            Token::LParen => { depth += 1; if depth > max_depth { max_depth = depth; } }
            Token::RParen => { depth -= 1; }
            Token::Plus | Token::Star => { sum += 1; }
            Token::Minus | Token::Slash => { sum -= 1; }
            Token::Ident(name) => { sum += name.len() as i64; }
            Token::Eof => {}
        }
    }
    sum * (max_depth + 1) + num_count
}

/// Evaluate expression tree recursively
#[inline(never)]
fn em_02(expr: &Expr) -> i64 {
    match expr {
        Expr::Lit(n) => *n,
        Expr::Var(name) => name.len() as i64,
        Expr::BinOp(l, op, r) => {
            let lv = em_02(l);
            let rv = em_02(r);
            match op {
                Op::Add => lv.wrapping_add(rv),
                Op::Sub => lv.wrapping_sub(rv),
                Op::Mul => lv.wrapping_mul(rv),
                Op::Div => if rv != 0 { lv / rv } else { 0 },
            }
        }
        Expr::UnaryMinus(inner) => -em_02(inner),
        Expr::Call(name, args) => {
            let mut sum = name.len() as i64;
            for arg in args { sum += em_02(arg); }
            sum
        }
    }
}

/// Count nodes by type in token stream
#[inline(never)]
fn em_03(tokens: &[Token]) -> u64 {
    let mut nums = 0u64;
    let mut idents = 0u64;
    let mut ops = 0u64;
    let mut parens = 0u64;
    for tok in tokens {
        match tok {
            Token::Num(_) => nums += 1,
            Token::Ident(_) => idents += 1,
            Token::Plus | Token::Minus | Token::Star | Token::Slash => ops += 1,
            Token::LParen | Token::RParen => parens += 1,
            Token::Eof => {}
        }
    }
    nums * 1000 + idents * 100 + ops * 10 + parens
}

/// Count expression tree depth and node count
#[inline(never)]
fn em_04(expr: &Expr) -> u64 {
    fn depth(e: &Expr) -> u64 {
        match e {
            Expr::Lit(_) | Expr::Var(_) => 1,
            Expr::BinOp(l, _, r) => 1 + depth(l).max(depth(r)),
            Expr::UnaryMinus(inner) => 1 + depth(inner),
            Expr::Call(_, args) => 1 + args.iter().map(depth).max().unwrap_or(0),
        }
    }
    fn count(e: &Expr) -> u64 {
        match e {
            Expr::Lit(_) | Expr::Var(_) => 1,
            Expr::BinOp(l, _, r) => 1 + count(l) + count(r),
            Expr::UnaryMinus(inner) => 1 + count(inner),
            Expr::Call(_, args) => 1 + args.iter().map(count).sum::<u64>(),
        }
    }
    depth(expr) * 100 + count(expr)
}

/// Extract all numbers from token stream, compute stats
#[inline(never)]
fn em_05(tokens: &[Token], top_n: usize) -> i64 {
    let mut nums: Vec<i64> = Vec::new();
    for tok in tokens {
        if let Token::Num(n) = tok { nums.push(*n); }
    }
    nums.sort();
    let sum: i64 = nums.iter().sum();
    let top_sum: i64 = nums.iter().rev().take(top_n).sum();
    let median = nums.get(nums.len() / 2).copied().unwrap_or(0);
    sum + top_sum * 10 + median
}

/// Constant-fold an expression tree
#[inline(never)]
fn em_06(expr: &Expr) -> Expr {
    match expr {
        Expr::Lit(n) => Expr::Lit(*n),
        Expr::Var(s) => Expr::Var(s.clone()),
        Expr::BinOp(l, op, r) => {
            let lf = em_06(l);
            let rf = em_06(r);
            match (&lf, op, &rf) {
                (Expr::Lit(a), Op::Add, Expr::Lit(b)) => Expr::Lit(a + b),
                (Expr::Lit(a), Op::Sub, Expr::Lit(b)) => Expr::Lit(a - b),
                (Expr::Lit(a), Op::Mul, Expr::Lit(b)) => Expr::Lit(a * b),
                (Expr::Lit(a), Op::Div, Expr::Lit(b)) if *b != 0 => Expr::Lit(a / b),
                (Expr::Lit(0), Op::Add, _) => rf,
                (_, Op::Add, Expr::Lit(0)) => lf,
                (Expr::Lit(0), Op::Mul, _) => Expr::Lit(0),
                (_, Op::Mul, Expr::Lit(0)) => Expr::Lit(0),
                (Expr::Lit(1), Op::Mul, _) => rf,
                (_, Op::Mul, Expr::Lit(1)) => lf,
                _ => Expr::BinOp(Box::new(lf), *op, Box::new(rf)),
            }
        }
        Expr::UnaryMinus(inner) => {
            let folded = em_06(inner);
            match &folded {
                Expr::Lit(n) => Expr::Lit(-n),
                _ => Expr::UnaryMinus(Box::new(folded)),
            }
        }
        Expr::Call(name, args) => {
            Expr::Call(name.clone(), args.iter().map(em_06).collect())
        }
    }
}

/// Pretty-print token stream with formatting
#[inline(never)]
fn em_07(tokens: &[Token]) -> String {
    let mut result = String::new();
    let mut prev_was_num = false;
    for tok in tokens {
        match tok {
            Token::Num(n) => {
                if prev_was_num { result.push(' '); }
                result.push_str(&n.to_string());
                prev_was_num = true;
            }
            Token::Ident(name) => {
                if prev_was_num { result.push(' '); }
                result.push_str(name);
                prev_was_num = true;
            }
            Token::Plus => { result.push_str(" + "); prev_was_num = false; }
            Token::Minus => { result.push_str(" - "); prev_was_num = false; }
            Token::Star => { result.push_str(" * "); prev_was_num = false; }
            Token::Slash => { result.push_str(" / "); prev_was_num = false; }
            Token::LParen => { result.push('('); prev_was_num = false; }
            Token::RParen => { result.push(')'); prev_was_num = false; }
            Token::Eof => {}
        }
    }
    result
}

/// Serialize expression tree to string
#[inline(never)]
fn em_08(expr: &Expr) -> String {
    match expr {
        Expr::Lit(n) => n.to_string(),
        Expr::Var(s) => s.clone(),
        Expr::BinOp(l, op, r) => {
            let op_str = match op { Op::Add => "+", Op::Sub => "-", Op::Mul => "*", Op::Div => "/" };
            format!("({} {} {})", em_08(l), op_str, em_08(r))
        }
        Expr::UnaryMinus(inner) => format!("(-{})", em_08(inner)),
        Expr::Call(name, args) => {
            let arg_strs: Vec<String> = args.iter().map(em_08).collect();
            format!("{}({})", name, arg_strs.join(", "))
        }
    }
}

/// Validate token stream (balanced parens, valid sequences)
#[inline(never)]
fn em_09(tokens: &[Token]) -> u64 {
    let mut depth = 0i64;
    let mut max_depth = 0i64;
    let mut errors = 0u64;
    let mut prev_was_op = true; // start counts as "after op"
    for tok in tokens {
        match tok {
            Token::Num(_) | Token::Ident(_) => {
                if !prev_was_op { errors += 1; }
                prev_was_op = false;
            }
            Token::Plus | Token::Minus | Token::Star | Token::Slash => {
                if prev_was_op { errors += 1; }
                prev_was_op = true;
            }
            Token::LParen => { depth += 1; if depth > max_depth { max_depth = depth; } prev_was_op = true; }
            Token::RParen => { depth -= 1; if depth < 0 { errors += 1; } prev_was_op = false; }
            Token::Eof => {}
        }
    }
    if depth != 0 { errors += depth.unsigned_abs(); }
    errors * 100 + max_depth as u64
}

/// Execute command list with environment
#[inline(never)]
fn em_10(cmds: &[Cmd]) -> i64 {
    let mut env: Vec<(String, CVal)> = Vec::new();
    fn lookup(env: &[(String, CVal)], name: &str) -> Option<i64> {
        for (k, v) in env.iter().rev() {
            if k == name {
                return match v {
                    CVal::Int(n) => Some(*n),
                    CVal::Str(s) => Some(s.len() as i64),
                    CVal::List(l) => Some(l.iter().sum::<i64>()),
                };
            }
        }
        None
    }
    let mut output = 0i64;
    for cmd in cmds {
        match cmd {
            Cmd::Set(name, val) => { env.push((name.clone(), val.clone())); }
            Cmd::Add(a, b, dst) => {
                let va = lookup(&env, a).unwrap_or(0);
                let vb = lookup(&env, b).unwrap_or(0);
                env.push((dst.clone(), CVal::Int(va + vb)));
            }
            Cmd::Print(name) => {
                output += lookup(&env, name).unwrap_or(-1);
            }
            Cmd::If(cond, then_cmds, else_cmds) => {
                let val = lookup(&env, cond).unwrap_or(0);
                if val > 0 {
                    output += em_10(then_cmds);
                } else {
                    output += em_10(else_cmds);
                }
            }
        }
    }
    output
}

/// Extract unique identifier names from tokens
#[inline(never)]
fn em_11(tokens: &[Token]) -> u64 {
    let mut names: Vec<String> = Vec::new();
    for tok in tokens {
        if let Token::Ident(name) = tok {
            if !names.contains(name) {
                names.push(name.clone());
            }
        }
    }
    names.sort();
    let mut hash = 0u64;
    for name in &names {
        for b in name.bytes() {
            hash = hash.wrapping_mul(31).wrapping_add(b as u64);
        }
    }
    hash.wrapping_add(names.len() as u64)
}

/// Collect all variable references in expression tree
#[inline(never)]
fn em_12(expr: &Expr) -> Vec<String> {
    let mut vars = Vec::new();
    fn collect(e: &Expr, out: &mut Vec<String>) {
        match e {
            Expr::Lit(_) => {}
            Expr::Var(s) => { if !out.contains(s) { out.push(s.clone()); } }
            Expr::BinOp(l, _, r) => { collect(l, out); collect(r, out); }
            Expr::UnaryMinus(inner) => { collect(inner, out); }
            Expr::Call(_, args) => { for a in args { collect(a, out); } }
        }
    }
    collect(expr, &mut vars);
    vars.sort();
    vars
}

/// Compute token stream "complexity score"
#[inline(never)]
fn em_13(tokens: &[Token]) -> u64 {
    let mut score = 0u64;
    let mut nesting = 0u64;
    for tok in tokens {
        match tok {
            Token::Num(n) => { score += 1 + ((*n).unsigned_abs() / 10); }
            Token::Ident(name) => { score += name.len() as u64 * 2; }
            Token::Plus | Token::Minus => { score += 1 + nesting; }
            Token::Star | Token::Slash => { score += 2 + nesting * 2; }
            Token::LParen => { nesting += 1; score += nesting; }
            Token::RParen => { if nesting > 0 { nesting -= 1; } }
            Token::Eof => {}
        }
    }
    score
}

/// Substitute variables in expression tree
#[inline(never)]
fn em_14(expr: &Expr) -> Expr {
    match expr {
        Expr::Lit(n) => Expr::Lit(*n),
        Expr::Var(name) => {
            // Substitute known variables
            match name.as_str() {
                "x" => Expr::Lit(10),
                "y" => Expr::Lit(20),
                "z" => Expr::Lit(30),
                _ => Expr::Var(name.clone()),
            }
        }
        Expr::BinOp(l, op, r) => {
            Expr::BinOp(Box::new(em_14(l)), *op, Box::new(em_14(r)))
        }
        Expr::UnaryMinus(inner) => Expr::UnaryMinus(Box::new(em_14(inner))),
        Expr::Call(name, args) => {
            Expr::Call(name.clone(), args.iter().map(em_14).collect())
        }
    }
}

/// Validate and execute command list, return error count
#[inline(never)]
fn em_15(cmds: &[Cmd]) -> u64 {
    let mut defined: Vec<String> = Vec::new();
    let mut errors = 0u64;
    for cmd in cmds {
        match cmd {
            Cmd::Set(name, _) => { if !defined.contains(name) { defined.push(name.clone()); } }
            Cmd::Add(a, b, dst) => {
                if !defined.contains(a) { errors += 1; }
                if !defined.contains(b) { errors += 1; }
                if !defined.contains(dst) { defined.push(dst.clone()); }
            }
            Cmd::Print(name) => { if !defined.contains(name) { errors += 1; } }
            Cmd::If(cond, then_cmds, else_cmds) => {
                if !defined.contains(cond) { errors += 1; }
                errors += em_15(then_cmds);
                errors += em_15(else_cmds);
            }
        }
    }
    errors
}

/// Reverse-polish notation conversion from tokens
#[inline(never)]
fn em_16(tokens: &[Token]) -> Vec<String> {
    let mut output: Vec<String> = Vec::new();
    let mut op_stack: Vec<&Token> = Vec::new();
    fn precedence(t: &Token) -> u8 {
        match t { Token::Plus | Token::Minus => 1, Token::Star | Token::Slash => 2, _ => 0 }
    }
    for tok in tokens {
        match tok {
            Token::Num(n) => output.push(n.to_string()),
            Token::Ident(name) => output.push(name.clone()),
            Token::Plus | Token::Minus | Token::Star | Token::Slash => {
                while let Some(&top) = op_stack.last() {
                    if matches!(top, Token::LParen) { break; }
                    if precedence(top) >= precedence(tok) {
                        let op = op_stack.pop().unwrap();
                        output.push(match op { Token::Plus => "+", Token::Minus => "-", Token::Star => "*", Token::Slash => "/", _ => "?" }.to_string());
                    } else { break; }
                }
                op_stack.push(tok);
            }
            Token::LParen => op_stack.push(tok),
            Token::RParen => {
                while let Some(top) = op_stack.pop() {
                    if matches!(top, Token::LParen) { break; }
                    output.push(match top { Token::Plus => "+", Token::Minus => "-", Token::Star => "*", Token::Slash => "/", _ => "?" }.to_string());
                }
            }
            Token::Eof => {}
        }
    }
    while let Some(top) = op_stack.pop() {
        output.push(match top { Token::Plus => "+", Token::Minus => "-", Token::Star => "*", Token::Slash => "/", _ => "?" }.to_string());
    }
    output
}

/// Check if expression is "linear" (no Mul/Div)
#[inline(never)]
fn em_17(expr: &Expr) -> bool {
    match expr {
        Expr::Lit(_) | Expr::Var(_) => true,
        Expr::BinOp(l, Op::Add, r) | Expr::BinOp(l, Op::Sub, r) => em_17(l) && em_17(r),
        Expr::BinOp(_, Op::Mul, _) | Expr::BinOp(_, Op::Div, _) => false,
        Expr::UnaryMinus(inner) => em_17(inner),
        Expr::Call(_, args) => args.iter().all(em_17),
    }
}

/// Find matching brackets and compute nesting histogram
#[inline(never)]
fn em_18(tokens: &[Token], max_depth: usize) -> Vec<u64> {
    let mut histogram = vec![0u64; max_depth + 1];
    let mut depth = 0usize;
    for tok in tokens {
        match tok {
            Token::LParen => {
                if depth <= max_depth { histogram[depth] += 1; }
                depth += 1;
            }
            Token::RParen => {
                if depth > 0 { depth -= 1; }
            }
            _ => {
                if depth <= max_depth { histogram[depth.min(max_depth)] += 1; }
            }
        }
    }
    histogram
}

/// Type-check command list (ensure type consistency)
#[inline(never)]
fn em_19(cmds: &[Cmd]) -> u64 {
    let mut types: Vec<(String, &str)> = Vec::new();
    let mut errors = 0u64;
    fn get_type<'a>(types: &'a [(String, &str)], name: &str) -> Option<&'a str> {
        for (k, t) in types.iter().rev() {
            if k == name { return Some(t); }
        }
        None
    }
    for cmd in cmds {
        match cmd {
            Cmd::Set(name, val) => {
                let t = match val {
                    CVal::Int(_) => "int",
                    CVal::Str(_) => "str",
                    CVal::List(_) => "list",
                };
                types.push((name.clone(), t));
            }
            Cmd::Add(a, b, dst) => {
                let ta = get_type(&types, a).map(|s| s.to_string());
                let tb = get_type(&types, b).map(|s| s.to_string());
                match (ta.as_deref(), tb.as_deref()) {
                    (Some("int"), Some("int")) => { types.push((dst.clone(), "int")); }
                    (Some(x), Some(y)) if x == y => { types.push((dst.clone(), "int")); }
                    _ => { errors += 1; types.push((dst.clone(), "int")); }
                }
            }
            Cmd::Print(name) => {
                let found = get_type(&types, name).is_some();
                if !found { errors += 1; }
            }
            Cmd::If(cond, then_cmds, else_cmds) => {
                let is_int = get_type(&types, cond) == Some("int");
                if !is_int { errors += 1; }
                errors += em_19(then_cmds);
                errors += em_19(else_cmds);
            }
        }
    }
    errors
}

/// Transform expression: distribute multiplication over addition
#[inline(never)]
fn em_20(expr: &Expr) -> Expr {
    match expr {
        Expr::Lit(n) => Expr::Lit(*n),
        Expr::Var(s) => Expr::Var(s.clone()),
        Expr::BinOp(l, Op::Mul, r) => {
            let lf = em_20(l);
            let rf = em_20(r);
            // a * (b + c) => a*b + a*c
            if let Expr::BinOp(b, Op::Add, c) = &rf {
                let ab = Expr::BinOp(Box::new(lf.clone()), Op::Mul, Box::new(*b.clone()));
                let ac = Expr::BinOp(Box::new(lf), Op::Mul, Box::new(*c.clone()));
                return Expr::BinOp(Box::new(ab), Op::Add, Box::new(ac));
            }
            Expr::BinOp(Box::new(lf), Op::Mul, Box::new(rf))
        }
        Expr::BinOp(l, op, r) => {
            Expr::BinOp(Box::new(em_20(l)), *op, Box::new(em_20(r)))
        }
        Expr::UnaryMinus(inner) => Expr::UnaryMinus(Box::new(em_20(inner))),
        Expr::Call(name, args) => {
            Expr::Call(name.clone(), args.iter().map(em_20).collect())
        }
    }
}
