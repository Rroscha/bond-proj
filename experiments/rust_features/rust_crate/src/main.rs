// 100 functions: 5 Rust-specific features × 20 functions each.
// Each function implements a real algorithm that exercises the target feature.
//
// Categories:
//   om_: Ownership & Move — values moved between owners, no copy
//   dg_: Drop Glue — RAII types (Vec, String, Box) with automatic cleanup
//   bc_: Bounds Checking — slice indexing with cmp+jae+ud2
//   qm_: ? Operator — Option/Result propagation with early return
//   pu_: Panic/Unwind — unwrap(), expect(), index-panic, overflow

use std::hint::black_box;
use std::collections::HashMap;

fn main() {
    let data: Vec<u64> = (0..64).collect();
    let data2: Vec<u64> = (100..200).collect();
    let s = "hello world foo bar baz 123 testing seven";

    // ownership_move
    black_box(om_01(black_box(vec![5,3,8,1,7]), black_box(vec![2,9,4,6,0])));
    black_box(om_02(black_box("hello world".to_string()), black_box("foo bar".to_string())));
    black_box(om_03(black_box(vec![10,20,30,40,50])));
    black_box(om_04(black_box("the quick brown fox".to_string()), black_box(3)));
    black_box(om_05(black_box(vec![1,2,3,4,5]), black_box(vec![6,7,8,9,10]), black_box(vec![11,12,13,14,15])));
    black_box(om_06(black_box("abcdef".to_string())));
    black_box(om_07(black_box(vec![100,50,200,25,75])));
    black_box(om_08(black_box("rust is great".to_string()), black_box(4)));
    black_box(om_09(black_box(vec![3,1,4,1,5,9,2,6])));
    black_box(om_10(black_box("hello".to_string()), black_box("world".to_string()), black_box("!".to_string())));
    black_box(om_11(black_box(vec![7,2,5,1,8,3])));
    black_box(om_12(black_box("testing one two three".to_string())));
    black_box(om_13(black_box(vec![10,20,30]), black_box(vec![40,50,60])));
    black_box(om_14(black_box("abcdefghij".to_string()), black_box(3)));
    black_box(om_15(black_box(vec![9,1,5,3,7,2,8,4,6])));
    black_box(om_16(black_box("hello world test".to_string())));
    black_box(om_17(black_box(vec![1,2,3,4,5,6,7,8])));
    black_box(om_18(black_box("the quick brown".to_string()), black_box("fox jumps over".to_string())));
    black_box(om_19(black_box(vec![5,10,15,20,25,30])));
    black_box(om_20(black_box("abcdefghijklmnop".to_string()), black_box(5)));

    // drop_glue
    black_box(dg_01(black_box(8)));
    black_box(dg_02(black_box("hello world foo".to_string()), black_box(3)));
    black_box(dg_03(black_box(10)));
    black_box(dg_04(black_box(vec![3,1,4,1,5,9,2,6,5,3])));
    black_box(dg_05(black_box(12)));
    black_box(dg_06(black_box("the quick brown fox jumps".to_string())));
    black_box(dg_07(black_box(6)));
    black_box(dg_08(black_box(vec![10,20,30,40,50,60,70,80])));
    black_box(dg_09(black_box(15)));
    black_box(dg_10(black_box("rust lang is great for systems".to_string()), black_box('a')));
    black_box(dg_11(black_box(20)));
    black_box(dg_12(black_box(vec![7,2,5,1,8,3,6,4,9])));
    black_box(dg_13(black_box(8)));
    black_box(dg_14(black_box("abcdefghij".to_string()), black_box(2)));
    black_box(dg_15(black_box(10)));
    black_box(dg_16(black_box(vec![100,50,200,25,75,150])));
    black_box(dg_17(black_box(7)));
    black_box(dg_18(black_box("hello world test data".to_string())));
    black_box(dg_19(black_box(16)));
    black_box(dg_20(black_box(vec![1,3,5,7,9,2,4,6,8,10])));

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

    // question_mark
    black_box(qm_01(black_box(&data), black_box(50)));
    black_box(qm_02(black_box(s)));
    black_box(qm_03(black_box(&[Some(1u64), None, Some(3), Some(4)])));
    black_box(qm_04(black_box(&data), black_box(5)));
    black_box(qm_05(black_box("123 456 abc 789")));
    black_box(qm_06(black_box(&data)));
    black_box(qm_07(black_box(s)));
    black_box(qm_08(black_box(&[Ok(1u64), Err("bad"), Ok(3)])));
    black_box(qm_09(black_box(&data), black_box(5)));
    black_box(qm_10(black_box(s), black_box(3)));
    black_box(qm_11(black_box(&data)));
    black_box(qm_12(black_box(&[Some(10u64), Some(20), None, Some(40)]), black_box(25)));
    black_box(qm_13(black_box(&data), black_box(7)));
    black_box(qm_14(black_box("10 20 abc 30 40")));
    black_box(qm_15(black_box(&data), black_box(3)));
    black_box(qm_16(black_box(&[Ok(5i64), Ok(-3), Err("x"), Ok(7)])));
    black_box(qm_17(black_box(&data), black_box(10)));
    black_box(qm_18(black_box(s)));
    black_box(qm_19(black_box(&data), black_box(8)));
    black_box(qm_20(black_box("3,1,4,1,5,9,2,6")));

    // panic_unwind
    black_box(pu_01(black_box(&data)));
    black_box(pu_02(black_box(s)));
    black_box(pu_03(black_box(&data), black_box(10)));
    black_box(pu_04(black_box("123 456 789")));
    black_box(pu_05(black_box(&data)));
    black_box(pu_06(black_box(s), black_box(3)));
    black_box(pu_07(black_box(&data), black_box(5)));
    black_box(pu_08(black_box("hello world")));
    black_box(pu_09(black_box(&data)));
    black_box(pu_10(black_box(s)));
    black_box(pu_11(black_box(&data), black_box(8)));
    black_box(pu_12(black_box("test data string")));
    black_box(pu_13(black_box(&data)));
    black_box(pu_14(black_box(s), black_box(4)));
    black_box(pu_15(black_box(&data)));
    black_box(pu_16(black_box("1,2,3,4,5")));
    black_box(pu_17(black_box(&data), black_box(3)));
    black_box(pu_18(black_box(s)));
    black_box(pu_19(black_box(&data)));
    black_box(pu_20(black_box("the quick brown fox")));
}

// =============================================================================
// OWNERSHIP & MOVE SEMANTICS (om_01 .. om_20)
// Each function takes owned values (Vec, String) and moves them between
// variables/functions. The compiler must track ownership at each point.
// At the binary level: no copy, values are moved by register/pointer transfer.
// =============================================================================

/// Merge two owned sorted vecs, consuming both
#[inline(never)]
fn om_01(mut a: Vec<u64>, mut b: Vec<u64>) -> Vec<u64> {
    a.sort();
    b.sort();
    let mut result = Vec::with_capacity(a.len() + b.len());
    let (mut i, mut j) = (0, 0);
    while i < a.len() && j < b.len() {
        if a[i] <= b[j] { result.push(a[i]); i += 1; }
        else { result.push(b[j]); j += 1; }
    }
    while i < a.len() { result.push(a[i]); i += 1; }
    while j < b.len() { result.push(b[j]); j += 1; }
    result
    // a, b dropped here (moved into function, not returned)
}

/// Concatenate two owned strings with transformation
#[inline(never)]
fn om_02(a: String, b: String) -> String {
    let mut result = String::with_capacity(a.len() + b.len() + 1);
    for ch in a.chars() { result.push(ch.to_ascii_uppercase()); }
    result.push('-');
    for ch in b.chars().rev() { result.push(ch); }
    result
    // a, b dropped here
}

/// Partition vec into two owned vecs (even/odd), consume original
#[inline(never)]
fn om_03(data: Vec<u64>) -> (Vec<u64>, Vec<u64>) {
    let mut evens = Vec::new();
    let mut odds = Vec::new();
    for val in data.into_iter() {
        if val % 2 == 0 { evens.push(val); }
        else { odds.push(val); }
    }
    (evens, odds)
    // original data consumed by into_iter
}

/// Split owned string into words, rotate, rejoin
#[inline(never)]
fn om_04(s: String, rot: usize) -> String {
    let mut words: Vec<String> = s.split_whitespace().map(|w| w.to_string()).collect();
    if words.is_empty() { return s; }
    let rot = rot % words.len();
    words.rotate_left(rot);
    words.join(" ")
    // s dropped, words dropped
}

/// Chain-move: merge 3 vecs into one, consuming all
#[inline(never)]
fn om_05(a: Vec<u64>, b: Vec<u64>, c: Vec<u64>) -> Vec<u64> {
    let mut combined = a;
    combined.extend(b);
    combined.extend(c);
    combined.sort();
    combined.dedup();
    combined
}

/// Reverse owned string character-by-character
#[inline(never)]
fn om_06(s: String) -> String {
    let chars: Vec<char> = s.chars().collect();
    let mut result = String::with_capacity(s.len());
    for i in (0..chars.len()).rev() {
        result.push(chars[i]);
    }
    result
    // s, chars dropped
}

/// Take owned vec, compute running difference, return new vec
#[inline(never)]
fn om_07(data: Vec<u64>) -> Vec<i64> {
    let mut result = Vec::with_capacity(data.len());
    if data.is_empty() { return result; }
    result.push(data[0] as i64);
    for i in 1..data.len() {
        result.push(data[i] as i64 - data[i - 1] as i64);
    }
    result
    // data dropped
}

/// Take owned string, extract every nth char into new string
#[inline(never)]
fn om_08(s: String, n: usize) -> String {
    let chars: Vec<char> = s.chars().collect();
    let mut result = String::new();
    let mut i = 0;
    while i < chars.len() {
        result.push(chars[i]);
        i += n;
    }
    result
    // s, chars dropped
}

/// Take owned vec, split at pivot, move halves into sorted result
#[inline(never)]
fn om_09(data: Vec<u64>) -> Vec<u64> {
    if data.len() < 2 { return data; }
    let mid = data.len() / 2;
    let mut left: Vec<u64> = data[..mid].to_vec();
    let mut right: Vec<u64> = data[mid..].to_vec();
    left.sort();
    right.sort();
    let mut merged = Vec::with_capacity(data.len());
    let (mut i, mut j) = (0, 0);
    while i < left.len() && j < right.len() {
        if left[i] <= right[j] { merged.push(left[i]); i += 1; }
        else { merged.push(right[j]); j += 1; }
    }
    while i < left.len() { merged.push(left[i]); i += 1; }
    while j < right.len() { merged.push(right[j]); j += 1; }
    merged
    // data, left, right dropped
}

/// Chain three owned strings with interleaved transforms
#[inline(never)]
fn om_10(a: String, b: String, c: String) -> String {
    let mut result = String::with_capacity(a.len() + b.len() + c.len());
    let a_chars: Vec<char> = a.chars().collect();
    let b_chars: Vec<char> = b.chars().collect();
    let c_chars: Vec<char> = c.chars().collect();
    let max_len = a_chars.len().max(b_chars.len()).max(c_chars.len());
    for i in 0..max_len {
        if i < a_chars.len() { result.push(a_chars[i]); }
        if i < b_chars.len() { result.push(b_chars[i]); }
        if i < c_chars.len() { result.push(c_chars[i]); }
    }
    result
}

/// Take owned vec, remove duplicates by consuming into HashMap, return keys
#[inline(never)]
fn om_11(data: Vec<u64>) -> Vec<u64> {
    let mut counts: HashMap<u64, u64> = HashMap::new();
    for val in data.into_iter() {
        *counts.entry(val).or_insert(0) += 1;
    }
    let mut unique: Vec<u64> = counts.into_keys().collect();
    unique.sort();
    unique
}

/// Take owned string, split into words, sort words, rejoin
#[inline(never)]
fn om_12(s: String) -> String {
    let mut words: Vec<&str> = s.split_whitespace().collect();
    words.sort();
    let result = words.join(" ");
    result
    // s dropped after result is built
}

/// Zip two owned vecs by consuming both
#[inline(never)]
fn om_13(a: Vec<u64>, b: Vec<u64>) -> Vec<(u64, u64)> {
    let mut result = Vec::with_capacity(a.len().min(b.len()));
    let a_iter = a.into_iter();
    let b_iter = b.into_iter();
    for (x, y) in a_iter.zip(b_iter) {
        result.push((x, y));
    }
    result
}

/// Rotate string bytes by offset, consuming original
#[inline(never)]
fn om_14(s: String, offset: usize) -> String {
    let bytes = s.into_bytes();
    let n = bytes.len();
    if n == 0 { return String::new(); }
    let offset = offset % n;
    let mut rotated = Vec::with_capacity(n);
    for i in 0..n {
        rotated.push(bytes[(i + offset) % n]);
    }
    String::from_utf8(rotated).unwrap_or_default()
}

/// Selection sort consuming owned vec, producing sorted owned vec
#[inline(never)]
fn om_15(mut data: Vec<u64>) -> Vec<u64> {
    let n = data.len();
    for i in 0..n {
        let mut min_idx = i;
        for j in i + 1..n {
            if data[j] < data[min_idx] {
                min_idx = j;
            }
        }
        data.swap(i, min_idx);
    }
    data
}

/// Take owned string, build frequency map, return as string
#[inline(never)]
fn om_16(s: String) -> String {
    let mut freq: HashMap<char, u32> = HashMap::new();
    for ch in s.chars() {
        if ch.is_alphabetic() {
            *freq.entry(ch.to_ascii_lowercase()).or_insert(0) += 1;
        }
    }
    let mut pairs: Vec<(char, u32)> = freq.into_iter().collect();
    pairs.sort_by_key(|&(c, _)| c);
    let mut result = String::new();
    for (c, count) in pairs {
        result.push(c);
        result.push_str(&count.to_string());
    }
    result
    // s dropped
}

/// Consume vec, produce cumulative sums as new vec
#[inline(never)]
fn om_17(data: Vec<u64>) -> Vec<u64> {
    let mut result = Vec::with_capacity(data.len());
    let mut sum = 0u64;
    for val in data.into_iter() {
        sum = sum.wrapping_add(val);
        result.push(sum);
    }
    result
}

/// Interleave two owned strings character by character
#[inline(never)]
fn om_18(a: String, b: String) -> String {
    let a_chars: Vec<char> = a.chars().collect();
    let b_chars: Vec<char> = b.chars().collect();
    let mut result = String::with_capacity(a.len() + b.len());
    let max = a_chars.len().max(b_chars.len());
    for i in 0..max {
        if i < a_chars.len() { result.push(a_chars[i]); }
        if i < b_chars.len() { result.push(b_chars[i]); }
    }
    result
}

/// Consume vec, partition into chunks, compute per-chunk stats
#[inline(never)]
fn om_19(data: Vec<u64>) -> Vec<u64> {
    let chunk_size = 3;
    let mut results = Vec::new();
    let mut i = 0;
    while i < data.len() {
        let end = (i + chunk_size).min(data.len());
        let mut sum = 0u64;
        for j in i..end {
            sum = sum.wrapping_add(data[j]);
        }
        results.push(sum);
        i = end;
    }
    results
    // data dropped
}

/// Take owned string, Caesar cipher each char, return new string
#[inline(never)]
fn om_20(s: String, shift: u8) -> String {
    let mut result = String::with_capacity(s.len());
    for ch in s.chars() {
        if ch.is_ascii_lowercase() {
            let shifted = ((ch as u8 - b'a' + shift) % 26 + b'a') as char;
            result.push(shifted);
        } else if ch.is_ascii_uppercase() {
            let shifted = ((ch as u8 - b'A' + shift) % 26 + b'A') as char;
            result.push(shifted);
        } else {
            result.push(ch);
        }
    }
    result
    // s dropped
}

// =============================================================================
// DROP GLUE (dg_01 .. dg_20)
// Each function creates heap-allocated types (Vec, String, Box, nested structs)
// that require compiler-generated drop_in_place<T> calls on scope exit.
// At the binary level: calls to drop_in_place, dealloc, __rust_dealloc.
// =============================================================================

/// Build matrix as Vec<Vec<u64>>, compute trace, all Vecs drop at end
#[inline(never)]
fn dg_01(n: usize) -> u64 {
    let mut matrix: Vec<Vec<u64>> = Vec::with_capacity(n);
    for i in 0..n {
        let mut row = Vec::with_capacity(n);
        for j in 0..n {
            row.push((i as u64).wrapping_mul(j as u64).wrapping_add(1));
        }
        matrix.push(row);
    }
    let mut trace = 0u64;
    for i in 0..n {
        trace = trace.wrapping_add(matrix[i][i]);
    }
    let mut off_diag = 0u64;
    for i in 0..n {
        for j in 0..n {
            if i != j { off_diag = off_diag.wrapping_add(matrix[i][j]); }
        }
    }
    trace.wrapping_mul(off_diag)
    // matrix: Vec<Vec<u64>> dropped → each inner Vec dropped
}

/// Build Vec<String> from splitting, each String drops individually
#[inline(never)]
fn dg_02(s: String, min_len: usize) -> u64 {
    let words: Vec<String> = s.split_whitespace()
        .map(|w| w.to_string())
        .collect();
    let long_words: Vec<String> = words.into_iter()
        .filter(|w| w.len() >= min_len)
        .collect();
    let mut total = 0u64;
    for word in &long_words {
        total = total.wrapping_add(word.len() as u64);
        for ch in word.chars() {
            total = total.wrapping_add(ch as u64);
        }
    }
    total
    // long_words: Vec<String> dropped → each String's buffer freed
}

/// Box-based binary tree, all nodes drop recursively
#[inline(never)]
fn dg_03(depth: u32) -> u64 {
    enum Tree { Leaf(u64), Node(Box<Tree>, u64, Box<Tree>) }
    fn build(d: u32, val: u64) -> Tree {
        if d == 0 { return Tree::Leaf(val); }
        Tree::Node(
            Box::new(build(d - 1, val.wrapping_mul(2))),
            val,
            Box::new(build(d - 1, val.wrapping_mul(2).wrapping_add(1))),
        )
    }
    fn sum(t: &Tree) -> u64 {
        match t {
            Tree::Leaf(v) => *v,
            Tree::Node(l, v, r) => sum(l).wrapping_add(*v).wrapping_add(sum(r)),
        }
    }
    let tree = build(depth, 1);
    let result = sum(&tree);
    result
    // tree dropped recursively: each Box<Tree> freed
}

/// Build histogram as HashMap, temporary Vecs for sorting
#[inline(never)]
fn dg_04(data: Vec<u64>) -> Vec<(u64, u64)> {
    let mut counts: HashMap<u64, u64> = HashMap::new();
    for val in &data {
        *counts.entry(*val).or_insert(0) += 1;
    }
    let mut pairs: Vec<(u64, u64)> = counts.into_iter().collect();
    pairs.sort_by(|a, b| b.1.cmp(&a.1).then(a.0.cmp(&b.0)));
    pairs
    // data: Vec<u64> dropped, counts: HashMap dropped
}

/// Build linked list of Boxes, traverse, all nodes drop
#[inline(never)]
fn dg_05(n: u64) -> u64 {
    enum List { Cons(u64, Box<List>), Nil }
    let mut head = List::Nil;
    for i in (0..n).rev() {
        head = List::Cons(i.wrapping_mul(i).wrapping_add(1), Box::new(head));
    }
    let mut sum = 0u64;
    let mut count = 0u64;
    let mut cur = &head;
    loop {
        match cur {
            List::Cons(val, next) => { sum = sum.wrapping_add(*val); count += 1; cur = next; }
            List::Nil => break,
        }
    }
    sum.wrapping_mul(count)
    // head dropped recursively
}

/// Multiple temporary Strings built and dropped in a loop
#[inline(never)]
fn dg_06(s: String) -> u64 {
    let mut total = 0u64;
    for word in s.split_whitespace() {
        let upper = word.to_uppercase();
        let reversed: String = upper.chars().rev().collect();
        total = total.wrapping_add(reversed.len() as u64);
        for ch in reversed.chars() {
            total = total.wrapping_add(ch as u64);
        }
        // upper and reversed drop each iteration
    }
    total
    // s dropped
}

/// Nested Vec<Vec<Vec<u64>>> — 3 levels of drop glue
#[inline(never)]
fn dg_07(n: usize) -> u64 {
    let mut cube: Vec<Vec<Vec<u64>>> = Vec::with_capacity(n);
    for i in 0..n {
        let mut plane: Vec<Vec<u64>> = Vec::with_capacity(n);
        for j in 0..n {
            let mut line: Vec<u64> = Vec::with_capacity(n);
            for k in 0..n {
                line.push(((i + j + k) as u64).wrapping_mul(7).wrapping_add(1));
            }
            plane.push(line);
        }
        cube.push(plane);
    }
    let mut sum = 0u64;
    for plane in &cube {
        for line in plane {
            for &val in line {
                sum = sum.wrapping_add(val);
            }
        }
    }
    sum
    // 3-level nested Vec dropped
}

/// Temporary Vec and String created per element
#[inline(never)]
fn dg_08(data: Vec<u64>) -> String {
    let mut parts: Vec<String> = Vec::with_capacity(data.len());
    for &val in &data {
        let s = val.to_string();
        let padded = format!("{:>5}", s);
        parts.push(padded);
        // s drops here (but padded takes ownership of format result)
    }
    let result = parts.join(",");
    result
    // data dropped, parts: Vec<String> dropped
}

/// Build Vec<Box<u64>>, each element is heap-allocated
#[inline(never)]
fn dg_09(n: u64) -> u64 {
    let mut boxes: Vec<Box<u64>> = Vec::with_capacity(n as usize);
    for i in 0..n {
        boxes.push(Box::new(i.wrapping_mul(i)));
    }
    let mut sum = 0u64;
    for b in &boxes {
        sum = sum.wrapping_add(**b);
    }
    let mut product = 1u64;
    for b in &boxes {
        if **b > 0 { product = product.wrapping_mul(**b % 100 + 1); }
    }
    sum.wrapping_add(product)
    // boxes: Vec<Box<u64>> dropped → each Box freed
}

/// Build Vec<String> from char processing
#[inline(never)]
fn dg_10(s: String, target: char) -> u64 {
    let mut segments: Vec<String> = Vec::new();
    let mut current = String::new();
    for ch in s.chars() {
        if ch == target {
            if !current.is_empty() {
                segments.push(current);
                current = String::new();
            }
        } else {
            current.push(ch);
        }
    }
    if !current.is_empty() { segments.push(current); }
    let mut total = 0u64;
    for (i, seg) in segments.iter().enumerate() {
        total = total.wrapping_add(seg.len() as u64 * (i as u64 + 1));
    }
    total
    // s, segments: Vec<String>, current: String — all dropped
}

/// HashMap<String, Vec<u64>> — double-nested drop
#[inline(never)]
fn dg_11(n: usize) -> u64 {
    let mut map: HashMap<String, Vec<u64>> = HashMap::new();
    for i in 0..n {
        let key = format!("key_{}", i % 5);
        map.entry(key).or_insert_with(Vec::new).push(i as u64);
    }
    let mut total = 0u64;
    for (key, vals) in &map {
        total = total.wrapping_add(key.len() as u64);
        for &v in vals {
            total = total.wrapping_add(v);
        }
    }
    total
    // map: HashMap<String, Vec<u64>> dropped
}

/// Sort vec, build intermediate vecs for run-length encoding
#[inline(never)]
fn dg_12(mut data: Vec<u64>) -> Vec<(u64, u64)> {
    data.sort();
    let mut runs: Vec<(u64, u64)> = Vec::new();
    if data.is_empty() { return runs; }
    let mut current = data[0];
    let mut count = 1u64;
    for i in 1..data.len() {
        if data[i] == current {
            count += 1;
        } else {
            runs.push((current, count));
            current = data[i];
            count = 1;
        }
    }
    runs.push((current, count));
    runs
    // data dropped
}

/// Build Vec<(String, u64)> pairs, drop all
#[inline(never)]
fn dg_13(n: usize) -> u64 {
    let mut pairs: Vec<(String, u64)> = Vec::with_capacity(n);
    for i in 0..n {
        let label = format!("item_{}", i);
        let value = (i as u64).wrapping_mul(17).wrapping_add(3);
        pairs.push((label, value));
    }
    let mut sum = 0u64;
    for (label, value) in &pairs {
        sum = sum.wrapping_add(label.len() as u64);
        sum = sum.wrapping_add(*value);
    }
    sum
    // pairs: Vec<(String, u64)> dropped → each String freed
}

/// Build multiple String intermediates via char manipulation
#[inline(never)]
fn dg_14(s: String, shift: usize) -> String {
    let chars: Vec<char> = s.chars().collect();
    let n = chars.len();
    let mut line1 = String::with_capacity(n);
    let mut line2 = String::with_capacity(n);
    for i in 0..n {
        line1.push(chars[i]);
        line2.push(chars[(i + shift) % n]);
    }
    let combined = format!("{}|{}", line1, line2);
    combined
    // s, chars, line1, line2 dropped
}

/// Vec<Box<Vec<u64>>> — Box wrapping Vec
#[inline(never)]
fn dg_15(n: usize) -> u64 {
    let mut outer: Vec<Box<Vec<u64>>> = Vec::with_capacity(n);
    for i in 0..n {
        let mut inner = Vec::with_capacity(i + 1);
        for j in 0..=i {
            inner.push((i as u64).wrapping_add(j as u64));
        }
        outer.push(Box::new(inner));
    }
    let mut sum = 0u64;
    for boxed in &outer {
        for &val in boxed.iter() {
            sum = sum.wrapping_add(val);
        }
    }
    sum
    // outer: Vec<Box<Vec<u64>>> → each Box freed → each Vec freed
}

/// Temporary Vecs in loop body for partitioning
#[inline(never)]
fn dg_16(data: Vec<u64>) -> u64 {
    let mut total = 0u64;
    for pivot in &data {
        let less: Vec<u64> = data.iter().filter(|&&x| x < *pivot).copied().collect();
        let greater: Vec<u64> = data.iter().filter(|&&x| x > *pivot).copied().collect();
        total = total.wrapping_add(less.len() as u64);
        total = total.wrapping_add(greater.len() as u64);
        // less, greater dropped each iteration
    }
    total
    // data dropped
}

/// Build adjacency list as Vec<Vec<usize>>, drop all
#[inline(never)]
fn dg_17(n: usize) -> u64 {
    let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
    for i in 0..n {
        for j in (i + 1)..n {
            if (i + j) % 3 != 0 {
                adj[i].push(j);
                adj[j].push(i);
            }
        }
    }
    let mut total = 0u64;
    for (node, neighbors) in adj.iter().enumerate() {
        total = total.wrapping_add(node as u64 * neighbors.len() as u64);
    }
    total
    // adj: Vec<Vec<usize>> dropped
}

/// Multiple String transformations in sequence
#[inline(never)]
fn dg_18(s: String) -> u64 {
    let words: Vec<String> = s.split_whitespace().map(|w| w.to_string()).collect();
    let mut reversed_words: Vec<String> = Vec::with_capacity(words.len());
    for w in &words {
        let rev: String = w.chars().rev().collect();
        reversed_words.push(rev);
    }
    let joined = reversed_words.join(" ");
    let upper = joined.to_uppercase();
    let mut total = 0u64;
    for ch in upper.chars() {
        total = total.wrapping_add(ch as u64);
    }
    total
    // s, words, reversed_words, joined, upper — all String/Vec dropped
}

/// Vec<Option<Box<u64>>> with mixed Some/None
#[inline(never)]
fn dg_19(n: u64) -> u64 {
    let mut items: Vec<Option<Box<u64>>> = Vec::with_capacity(n as usize);
    for i in 0..n {
        if i % 3 == 0 {
            items.push(Some(Box::new(i.wrapping_mul(i))));
        } else {
            items.push(None);
        }
    }
    let mut sum = 0u64;
    for item in &items {
        if let Some(boxed) = item {
            sum = sum.wrapping_add(**boxed);
        }
    }
    sum
    // items dropped → each Some(Box) freed
}

/// Build temp vecs for two-pass algorithm
#[inline(never)]
fn dg_20(data: Vec<u64>) -> u64 {
    let prefix_sums: Vec<u64> = {
        let mut sums = Vec::with_capacity(data.len());
        let mut acc = 0u64;
        for &v in &data {
            acc = acc.wrapping_add(v);
            sums.push(acc);
        }
        sums
    };
    let suffix_sums: Vec<u64> = {
        let mut sums = vec![0u64; data.len()];
        let mut acc = 0u64;
        for i in (0..data.len()).rev() {
            acc = acc.wrapping_add(data[i]);
            sums[i] = acc;
        }
        sums
    };
    let mut max_diff = 0u64;
    for i in 0..data.len() {
        let diff = if prefix_sums[i] > suffix_sums[i] {
            prefix_sums[i] - suffix_sums[i]
        } else {
            suffix_sums[i] - prefix_sums[i]
        };
        if diff > max_diff { max_diff = diff; }
    }
    max_diff
    // data, prefix_sums, suffix_sums dropped
}

// =============================================================================
// BOUNDS CHECKING (bc_01 .. bc_20)
// Each function uses slice indexing (data[i]) which generates:
//   cmp i, len; jae panic_bounds_check; ... ud2
// The C equivalents use raw pointer arithmetic with no checks.
// =============================================================================

/// Binary search with explicit indexing
#[inline(never)]
fn bc_01(data: &[u64], target: u64) -> Option<usize> {
    let mut lo = 0usize;
    let mut hi = data.len();
    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        if data[mid] == target { return Some(mid); }
        else if data[mid] < target { lo = mid + 1; }
        else { hi = mid; }
    }
    None
}

/// Insertion sort via indexing
#[inline(never)]
fn bc_02(data: &mut [u64]) -> u64 {
    let n = data.len();
    let mut swaps = 0u64;
    for i in 1..n {
        let key = data[i];
        let mut j = i;
        while j > 0 && data[j - 1] > key {
            data[j] = data[j - 1];
            j -= 1;
            swaps += 1;
        }
        data[j] = key;
    }
    swaps
}

/// Sliding window maximum
#[inline(never)]
fn bc_03(data: &[u64], window: usize) -> Vec<u64> {
    let n = data.len();
    if window == 0 || window > n { return vec![]; }
    let mut result = Vec::with_capacity(n - window + 1);
    for i in 0..=n - window {
        let mut max_val = data[i];
        for j in 1..window {
            if data[i + j] > max_val { max_val = data[i + j]; }
        }
        result.push(max_val);
    }
    result
}

/// Dot product of two slices
#[inline(never)]
fn bc_04(a: &[u64], b: &[u64]) -> u64 {
    let n = a.len().min(b.len());
    let mut sum = 0u64;
    for i in 0..n {
        sum = sum.wrapping_add(a[i].wrapping_mul(b[i]));
    }
    sum
}

/// Count inversions with nested indexing
#[inline(never)]
fn bc_05(data: &[u64]) -> u64 {
    let n = data.len();
    let mut inv = 0u64;
    for i in 0..n {
        for j in i + 1..n {
            if data[i] > data[j] { inv += 1; }
        }
    }
    inv
}

/// Shell sort
#[inline(never)]
fn bc_06(data: &mut [u64], initial_gap: usize) -> u64 {
    let n = data.len();
    let mut moves = 0u64;
    let mut gap = initial_gap;
    while gap > 0 {
        for i in gap..n {
            let temp = data[i];
            let mut j = i;
            while j >= gap && data[j - gap] > temp {
                data[j] = data[j - gap];
                j -= gap;
                moves += 1;
            }
            data[j] = temp;
        }
        gap /= 2;
    }
    moves
}

/// Convolution kernel [-1, 2, -1] then smooth
#[inline(never)]
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

/// Find peaks with prominence check
#[inline(never)]
fn bc_08(data: &[u64], min_prominence: u64) -> Vec<(usize, u64)> {
    let n = data.len();
    if n < 3 { return vec![]; }
    let mut peaks = Vec::new();
    for i in 1..n - 1 {
        if data[i] > data[i - 1] && data[i] > data[i + 1] {
            let mut left_min = data[i];
            for j in (0..i).rev() {
                if data[j] < left_min { left_min = data[j]; }
                if data[j] > data[i] { break; }
            }
            if data[i] - left_min >= min_prominence {
                peaks.push((i, data[i]));
            }
        }
    }
    peaks
}

/// Bubble sort
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

/// Matrix multiply (nested triple indexing)
#[inline(never)]
fn bc_10(data: &[u64], dim: usize) -> u64 {
    let n = dim.min(data.len());
    let mut sum = 0u64;
    for i in 0..n {
        for j in 0..n {
            let mut cell = 0u64;
            for k in 0..n {
                let a_idx = i * n + k;
                let b_idx = k * n + j;
                if a_idx < data.len() && b_idx < data.len() {
                    cell = cell.wrapping_add(data[a_idx].wrapping_mul(data[b_idx]));
                }
            }
            sum = sum.wrapping_add(cell);
        }
    }
    sum
}

/// Three-way partition (Dutch National Flag)
#[inline(never)]
fn bc_11(data: &mut [u64]) -> (usize, usize) {
    let n = data.len();
    if n == 0 { return (0, 0); }
    let pivot = data[n / 2];
    let mut lo = 0;
    let mut mid = 0;
    let mut hi = n;
    while mid < hi {
        if data[mid] < pivot { data.swap(lo, mid); lo += 1; mid += 1; }
        else if data[mid] > pivot { hi -= 1; data.swap(mid, hi); }
        else { mid += 1; }
    }
    (lo, hi)
}

/// Running median with sorted window
#[inline(never)]
fn bc_12(data: &[u64], window: usize) -> Vec<u64> {
    let n = data.len();
    if window == 0 || window > n { return vec![]; }
    let mut result = Vec::with_capacity(n - window + 1);
    let mut win: Vec<u64> = data[..window].to_vec();
    win.sort();
    result.push(win[window / 2]);
    for i in window..n {
        let old = data[i - window];
        let new_val = data[i];
        if let Ok(pos) = win.binary_search(&old) { win.remove(pos); }
        let insert_pos = win.partition_point(|&x| x < new_val);
        win.insert(insert_pos, new_val);
        result.push(win[window / 2]);
    }
    result
}

/// Prefix sum query via indexing
#[inline(never)]
fn bc_13(data: &[u64]) -> u64 {
    let n = data.len();
    let mut prefix = Vec::with_capacity(n + 1);
    prefix.push(0u64);
    for i in 0..n {
        prefix.push(prefix[i].wrapping_add(data[i]));
    }
    let mut total = 0u64;
    for i in 0..n {
        for j in i + 1..=n {
            total = total.wrapping_add(prefix[j].wrapping_sub(prefix[i]));
        }
    }
    total
}

/// Comb sort
#[inline(never)]
fn bc_14(data: &mut [u64], shrink: u64) -> u64 {
    let n = data.len();
    let mut gap = n;
    let mut swaps = 0u64;
    let mut sorted = false;
    while !sorted {
        gap = ((gap as f64 / shrink as f64) as usize).max(1);
        sorted = gap == 1;
        for i in 0..n - gap {
            if data[i] > data[i + gap] {
                data.swap(i, i + gap);
                sorted = false;
                swaps += 1;
            }
        }
    }
    swaps
}

/// Local average (3-element window)
#[inline(never)]
fn bc_15(data: &[u64]) -> Vec<u64> {
    let n = data.len();
    let mut result = Vec::with_capacity(n);
    for i in 0..n {
        let left = if i > 0 { data[i - 1] } else { data[i] };
        let right = if i + 1 < n { data[i + 1] } else { data[i] };
        result.push((left + data[i] + right) / 3);
    }
    result
}

/// Stride access pattern
#[inline(never)]
fn bc_16(data: &[u64], stride: usize) -> u64 {
    if stride == 0 { return 0; }
    let n = data.len();
    let mut sum = 0u64;
    let mut i = 0;
    while i < n {
        sum = sum.wrapping_add(data[i]);
        if i + stride < n {
            sum = sum.wrapping_add(data[i].wrapping_mul(data[i + stride]));
        }
        i += stride;
    }
    sum
}

/// Odd-even sort
#[inline(never)]
fn bc_17(data: &mut [u64]) -> u64 {
    let n = data.len();
    let mut sorted = false;
    let mut passes = 0u64;
    while !sorted {
        sorted = true;
        for i in (1..n - 1).step_by(2) {
            if data[i] > data[i + 1] { data.swap(i, i + 1); sorted = false; }
        }
        for i in (0..n - 1).step_by(2) {
            if data[i] > data[i + 1] { data.swap(i, i + 1); sorted = false; }
        }
        passes += 1;
    }
    passes
}

/// Zigzag traversal
#[inline(never)]
fn bc_18(data: &[u64], width: usize) -> u64 {
    if width == 0 { return 0; }
    let n = data.len();
    let rows = (n + width - 1) / width;
    let mut sum = 0u64;
    for r in 0..rows {
        if r % 2 == 0 {
            for c in 0..width {
                let idx = r * width + c;
                if idx < n { sum = sum.wrapping_add(data[idx]); }
            }
        } else {
            for c in (0..width).rev() {
                let idx = r * width + c;
                if idx < n { sum = sum.wrapping_add(data[idx].wrapping_mul(2)); }
            }
        }
    }
    sum
}

/// Reverse pairs count
#[inline(never)]
fn bc_19(data: &[u64]) -> u64 {
    let n = data.len();
    let mut count = 0u64;
    for i in 0..n {
        for j in i + 1..n {
            if data[i] > 2 * data[j] { count += 1; }
        }
    }
    count
}

/// Cyclic permutation in-place
#[inline(never)]
fn bc_20(data: &mut [u64], k: usize) -> u64 {
    let n = data.len();
    if n == 0 { return 0; }
    let k = k % n;
    data.reverse();
    data[..k].reverse();
    data[k..].reverse();
    let mut sum = 0u64;
    for i in 0..n {
        sum = sum.wrapping_add(data[i].wrapping_mul(i as u64));
    }
    sum
}

// =============================================================================
// ? OPERATOR / OPTION / RESULT (qm_01 .. qm_20)
// Each function uses ? for early return on None/Err.
// At the binary level: discriminant check + conditional branch + unwrap.
// The C equivalents use if-null / if-error checks with goto/return.
// =============================================================================

/// Binary search returning Option, using .get()?
#[inline(never)]
fn qm_01(data: &[u64], target: u64) -> Option<usize> {
    if data.is_empty() { return None; }
    let mut lo = 0usize;
    let mut hi = data.len() - 1;
    while lo <= hi {
        let mid = lo + (hi - lo) / 2;
        let val = *data.get(mid)?;
        if val == target { return Some(mid); }
        else if val < target { lo = mid + 1; }
        else { if mid == 0 { return None; } hi = mid - 1; }
    }
    None
}

/// Parse key=value pairs, ? on split and parse
#[inline(never)]
fn qm_02(s: &str) -> Option<u64> {
    let mut total = 0u64;
    for part in s.split_whitespace() {
        let (key, val_str) = part.split_once('=')?;
        let val: u64 = val_str.parse().ok()?;
        total = total.wrapping_add(key.len() as u64 + val);
    }
    Some(total)
}

/// Sum of Option array using ?
#[inline(never)]
fn qm_03(data: &[Option<u64>]) -> Option<u64> {
    let mut sum = 0u64;
    let mut count = 0u64;
    for item in data {
        let val = (*item)?;
        sum = sum.wrapping_add(val);
        count += 1;
    }
    Some(sum.wrapping_mul(count))
}

/// Sliding window with .get()? bounds checking
#[inline(never)]
fn qm_04(data: &[u64], target: u64) -> Option<(usize, u64)> {
    let win = 3;
    for start in 0..data.len().checked_sub(win - 1)? {
        let mut all_above = true;
        let mut wsum = 0u64;
        for j in 0..win {
            let val = *data.get(start + j)?;
            wsum = wsum.wrapping_add(val);
            if val <= target { all_above = false; }
        }
        if all_above { return Some((start, wsum)); }
    }
    None
}

/// Parse numbers from string, ? on each parse
#[inline(never)]
fn qm_05(s: &str) -> Option<u64> {
    let mut sum = 0u64;
    let mut count = 0u64;
    for token in s.split_whitespace() {
        let val: u64 = token.parse().ok()?;
        sum = sum.wrapping_add(val);
        count += 1;
    }
    if count == 0 { return None; }
    Some(sum / count)
}

/// Find first/last with conditions using ?
#[inline(never)]
fn qm_06(data: &[u64]) -> Option<u64> {
    let first = data.first()?;
    let last = data.last()?;
    if data.len() < 3 { return None; }
    let mid_idx = data.len() / 2;
    let mid = data.get(mid_idx)?;
    let range = last.checked_sub(*first)?;
    let deviation = if *mid > *first + range / 2 {
        mid.checked_sub(*first + range / 2)?
    } else {
        (*first + range / 2).checked_sub(*mid)?
    };
    Some(range.wrapping_add(deviation))
}

/// Chain of string operations with ?
#[inline(never)]
fn qm_07(s: &str) -> Option<u64> {
    let first_word = s.split_whitespace().next()?;
    let last_word = s.split_whitespace().last()?;
    let first_char = first_word.chars().next()?;
    let last_char = last_word.chars().last()?;
    let sum = first_char as u64 + last_char as u64;
    let mid_word = s.split_whitespace().nth(s.split_whitespace().count() / 2)?;
    let mid_len = mid_word.len() as u64;
    Some(sum.wrapping_mul(mid_len))
}

/// Process Result array with ?
#[inline(never)]
fn qm_08<'a>(data: &'a [Result<u64, &'a str>]) -> Result<u64, &'a str> {
    let mut sum = 0u64;
    let mut max = 0u64;
    for item in data {
        let val = (*item)?;
        sum = sum.wrapping_add(val);
        if val > max { max = val; }
    }
    Ok(sum.wrapping_add(max))
}

/// Two-pointer with .get()? on both ends
#[inline(never)]
fn qm_09(data: &[u64], target_sum: u64) -> Option<(usize, usize)> {
    if data.len() < 2 { return None; }
    let mut lo = 0;
    let mut hi = data.len() - 1;
    while lo < hi {
        let left = *data.get(lo)?;
        let right = *data.get(hi)?;
        let sum = left.wrapping_add(right);
        if sum == target_sum { return Some((lo, hi)); }
        else if sum < target_sum { lo += 1; }
        else { hi -= 1; }
    }
    None
}

/// Extract nth word, nth char, using ?
#[inline(never)]
fn qm_10(s: &str, n: usize) -> Option<u64> {
    let word = s.split_whitespace().nth(n)?;
    let ch = word.chars().nth(n % word.len().max(1))?;
    let rword = s.split_whitespace().rev().nth(n)?;
    let rch = rword.chars().rev().nth(n % rword.len().max(1))?;
    Some(ch as u64 + rch as u64)
}

/// Adjacent pair search with ?
#[inline(never)]
fn qm_11(data: &[u64]) -> Option<(usize, u64)> {
    for i in 0..data.len().checked_sub(1)? {
        let a = *data.get(i)?;
        let b = *data.get(i + 1)?;
        if a > 0 && b > 0 && a.checked_add(b)?.is_power_of_two() {
            return Some((i, a + b));
        }
    }
    None
}

/// Filter and aggregate with Option chain
#[inline(never)]
fn qm_12(data: &[Option<u64>], threshold: u64) -> Option<u64> {
    let mut sum = 0u64;
    let mut count = 0u64;
    for item in data {
        let val = (*item)?;
        if val > threshold {
            sum = sum.wrapping_add(val);
            count += 1;
        }
    }
    if count == 0 { return None; }
    Some(sum / count)
}

/// Running computation with checked arithmetic using ?
#[inline(never)]
fn qm_13(data: &[u64], divisor: u64) -> Option<u64> {
    let mut acc = 0u64;
    for i in 0..data.len() {
        let val = *data.get(i)?;
        acc = acc.checked_add(val)?;
        if (i + 1) % divisor as usize == 0 {
            acc = acc.checked_div(divisor)?;
        }
    }
    Some(acc)
}

/// Parse mixed tokens with Result→Option chain
#[inline(never)]
fn qm_14(s: &str) -> Option<u64> {
    let mut numbers = Vec::new();
    for token in s.split_whitespace() {
        let val: u64 = token.parse().ok()?;
        numbers.push(val);
    }
    let first = *numbers.first()?;
    let last = *numbers.last()?;
    let mid = *numbers.get(numbers.len() / 2)?;
    Some(first.wrapping_add(last).wrapping_add(mid))
}

/// Nested Option chain for 2D access
#[inline(never)]
fn qm_15(data: &[u64], stride: usize) -> Option<u64> {
    if stride == 0 { return None; }
    let rows = data.len().checked_div(stride)?;
    let mut sum = 0u64;
    for r in 0..rows {
        for c in 0..stride {
            let idx = r.checked_mul(stride)?.checked_add(c)?;
            let val = *data.get(idx)?;
            sum = sum.wrapping_add(val);
        }
    }
    Some(sum)
}

/// Process Result<i64> array, accumulate with ?
#[inline(never)]
fn qm_16<'a>(data: &'a [Result<i64, &'a str>]) -> Result<i64, &'a str> {
    let mut sum: i64 = 0;
    let mut positive_count: i64 = 0;
    let mut negative_count: i64 = 0;
    for item in data {
        let val = (*item)?;
        sum += val;
        if val > 0 { positive_count += 1; }
        else if val < 0 { negative_count += 1; }
    }
    Ok(sum.wrapping_mul(positive_count - negative_count))
}

/// Windowed comparison with bounds via ?
#[inline(never)]
fn qm_17(data: &[u64], window: usize) -> Option<u64> {
    if window == 0 { return None; }
    let mut crossings = 0u64;
    let threshold = *data.get(0)?;
    for i in 0..data.len().checked_sub(1)? {
        let a = *data.get(i)?;
        let b = *data.get(i + 1)?;
        if (a < threshold) != (b < threshold) {
            crossings += 1;
        }
    }
    Some(crossings)
}

/// String splitting with multiple ? points
#[inline(never)]
fn qm_18(s: &str) -> Option<u64> {
    let first_space = s.find(' ')?;
    let last_space = s.rfind(' ')?;
    if first_space >= last_space { return None; }
    let middle = &s[first_space + 1..last_space];
    let middle_word = middle.split_whitespace().next()?;
    let first_char = middle_word.chars().next()?;
    let len = middle_word.len() as u64;
    Some((first_char as u64).wrapping_mul(len))
}

/// Accumulate with overflow checking via ?
#[inline(never)]
fn qm_19(data: &[u64], chunk_size: usize) -> Option<u64> {
    if chunk_size == 0 { return None; }
    let mut results = Vec::new();
    let mut i = 0;
    while i < data.len() {
        let end = (i + chunk_size).min(data.len());
        let mut chunk_sum = 0u64;
        for j in i..end {
            let val = *data.get(j)?;
            chunk_sum = chunk_sum.checked_add(val)?;
        }
        results.push(chunk_sum);
        i = end;
    }
    let total = results.first()?.wrapping_add(*results.last()?);
    Some(total)
}

/// Parse CSV with ? on each step
#[inline(never)]
fn qm_20(s: &str) -> Option<u64> {
    let mut sum = 0u64;
    let mut count = 0u64;
    let mut max = 0u64;
    for part in s.split(',') {
        let val: u64 = part.trim().parse().ok()?;
        sum = sum.wrapping_add(val);
        if val > max { max = val; }
        count += 1;
    }
    if count == 0 { return None; }
    Some(sum.wrapping_add(max).wrapping_add(count))
}

// =============================================================================
// PANIC / UNWIND PATHS (pu_01 .. pu_20)
// Each function uses .unwrap(), .expect(), direct indexing that may panic,
// or checked arithmetic that overflows. These create cold panic paths:
//   call core::panicking::panic / panic_bounds_check / panic_fmt
// The C equivalents simply proceed without checks (undefined behavior).
// =============================================================================

/// Sum with .unwrap() on checked_add
#[inline(never)]
fn pu_01(data: &[u64]) -> u64 {
    let mut sum = 0u64;
    for i in 0..data.len() {
        let val = data.get(i).unwrap();
        sum = sum.wrapping_add(*val);
    }
    let mean = sum / data.len() as u64;
    let first = *data.first().unwrap();
    let last = *data.last().unwrap();
    mean.wrapping_add(first).wrapping_add(last)
}

/// String processing with .unwrap() and .expect()
#[inline(never)]
fn pu_02(s: &str) -> u64 {
    let first_word = s.split_whitespace().next().unwrap();
    let last_word = s.split_whitespace().last().unwrap();
    let first_char = first_word.chars().next().expect("empty first word");
    let last_char = last_word.chars().last().expect("empty last word");
    (first_char as u64).wrapping_add(last_char as u64)
        .wrapping_mul(first_word.len() as u64 + last_word.len() as u64)
}

/// Direct indexing (panic on out of bounds)
#[inline(never)]
fn pu_03(data: &[u64], window: usize) -> u64 {
    let n = data.len();
    let mut sum = 0u64;
    for i in 0..n - window + 1 {
        let mut w_sum = 0u64;
        for j in 0..window {
            w_sum += data[i + j]; // panics if out of bounds
        }
        sum = sum.wrapping_add(w_sum);
    }
    sum
}

/// Parse with .unwrap() on each conversion
#[inline(never)]
fn pu_04(s: &str) -> u64 {
    let mut sum = 0u64;
    for token in s.split_whitespace() {
        let val: u64 = token.parse().unwrap(); // panics on non-numeric
        sum = sum.wrapping_add(val);
    }
    sum
}

/// Array operations with multiple unwrap points
#[inline(never)]
fn pu_05(data: &[u64]) -> u64 {
    let first = *data.first().unwrap();
    let last = *data.last().unwrap();
    let mid = *data.get(data.len() / 2).unwrap();
    let quarter = *data.get(data.len() / 4).unwrap();
    let three_q = *data.get(3 * data.len() / 4).unwrap();
    first.wrapping_add(last).wrapping_add(mid)
        .wrapping_add(quarter).wrapping_add(three_q)
}

/// String nth char access with expect
#[inline(never)]
fn pu_06(s: &str, n: usize) -> u64 {
    let mut total = 0u64;
    for word in s.split_whitespace() {
        let ch = word.chars().nth(n % word.len()).expect("char access failed");
        total = total.wrapping_add(ch as u64);
    }
    total
}

/// Stride access with direct indexing
#[inline(never)]
fn pu_07(data: &[u64], stride: usize) -> u64 {
    let n = data.len();
    let mut sum = 0u64;
    let mut i = 0;
    while i < n {
        sum = sum.wrapping_add(data[i]); // direct index, panics if invalid
        if i + stride < n {
            sum = sum.wrapping_add(data[i] * data[i + stride]);
        }
        i += stride;
    }
    sum
}

/// Split and unwrap
#[inline(never)]
fn pu_08(s: &str) -> u64 {
    let parts: Vec<&str> = s.split_whitespace().collect();
    let first = parts.first().unwrap();
    let last = parts.last().unwrap();
    let mid = parts.get(parts.len() / 2).unwrap();
    let mut sum = 0u64;
    for ch in first.chars().chain(mid.chars()).chain(last.chars()) {
        sum = sum.wrapping_add(ch as u64);
    }
    sum
}

/// Nested indexing with two arrays
#[inline(never)]
fn pu_09(data: &[u64]) -> u64 {
    let n = data.len();
    let mut result = 0u64;
    for i in 0..n {
        let idx = (data[i] as usize) % n;
        result = result.wrapping_add(data[idx]); // indirect index, may panic
    }
    result
}

/// Multiple unwrap/expect on string operations
#[inline(never)]
fn pu_10(s: &str) -> u64 {
    let upper = s.to_uppercase();
    let words: Vec<&str> = upper.split_whitespace().collect();
    let first = words.first().unwrap();
    let second = words.get(1).unwrap();
    let last = words.last().unwrap();
    let f_ch = first.chars().next().unwrap();
    let s_ch = second.chars().next().unwrap();
    let l_ch = last.chars().last().unwrap();
    (f_ch as u64).wrapping_add(s_ch as u64).wrapping_add(l_ch as u64)
}

/// Windowed sum with direct indexing
#[inline(never)]
fn pu_11(data: &[u64], window: usize) -> Vec<u64> {
    let mut result = Vec::with_capacity(data.len());
    for i in 0..data.len() {
        let start = if i >= window { i - window } else { 0 };
        let mut sum = 0u64;
        for j in start..=i {
            sum = sum.wrapping_add(data[j]);
        }
        result.push(sum);
    }
    result
}

/// String indexing with .unwrap() on byte access
#[inline(never)]
fn pu_12(s: &str) -> u64 {
    let bytes = s.as_bytes();
    let n = bytes.len();
    let mut sum = 0u64;
    for i in 0..n {
        let b = *bytes.get(i).unwrap();
        if b.is_ascii_alphabetic() {
            let next = *bytes.get((i + 1) % n).unwrap();
            sum = sum.wrapping_add(b as u64 + next as u64);
        }
    }
    sum
}

/// Cross-referencing with direct indexing
#[inline(never)]
fn pu_13(data: &[u64]) -> u64 {
    let n = data.len();
    let mut sum = 0u64;
    for i in 0..n {
        let j = (n - 1 - i) % n;
        sum = sum.wrapping_add(data[i].wrapping_mul(data[j]));
    }
    let mid = data[n / 2];
    sum.wrapping_add(mid)
}

/// Multi-word extraction with expect
#[inline(never)]
fn pu_14(s: &str, count: usize) -> u64 {
    let words: Vec<&str> = s.split_whitespace().collect();
    let mut sum = 0u64;
    for i in 0..count.min(words.len()) {
        let word = words.get(i).expect("word index out of range");
        let first = word.chars().next().expect("empty word");
        let last = word.chars().last().expect("empty word");
        sum = sum.wrapping_add(first as u64 + last as u64);
    }
    sum
}

/// Scan with .unwrap() on accumulator
#[inline(never)]
fn pu_15(data: &[u64]) -> u64 {
    let mut running = Vec::with_capacity(data.len());
    let mut acc = 0u64;
    for i in 0..data.len() {
        acc = acc.wrapping_add(data[i]);
        running.push(acc);
    }
    let last = *running.last().unwrap();
    let first = *running.first().unwrap();
    let mid = *running.get(running.len() / 2).unwrap();
    last.wrapping_sub(first).wrapping_add(mid)
}

/// Parse CSV with unwrap
#[inline(never)]
fn pu_16(s: &str) -> u64 {
    let mut sum = 0u64;
    let mut count = 0u64;
    for part in s.split(',') {
        let val: u64 = part.trim().parse().unwrap();
        sum = sum.wrapping_add(val);
        count += 1;
    }
    sum.wrapping_mul(count)
}

/// Chunk processing with direct indexing
#[inline(never)]
fn pu_17(data: &[u64], chunk_size: usize) -> u64 {
    let n = data.len();
    let mut sum = 0u64;
    let mut i = 0;
    while i + chunk_size <= n {
        let mut chunk_sum = 0u64;
        for j in 0..chunk_size {
            chunk_sum = chunk_sum.wrapping_add(data[i + j]);
        }
        let chunk_max = data[i]; // first element, direct index
        sum = sum.wrapping_add(chunk_sum.wrapping_mul(chunk_max));
        i += chunk_size;
    }
    sum
}

/// Multiple .unwrap() on string search
#[inline(never)]
fn pu_18(s: &str) -> u64 {
    let words: Vec<&str> = s.split_whitespace().collect();
    let mut total = 0u64;
    for i in 0..words.len() {
        let w = words[i]; // direct index
        let len = w.len() as u64;
        let first = w.chars().next().unwrap() as u64;
        let last = w.chars().last().unwrap() as u64;
        total = total.wrapping_add(len.wrapping_mul(first + last));
    }
    total
}

/// Reverse-indexed access pattern
#[inline(never)]
fn pu_19(data: &[u64]) -> u64 {
    let n = data.len();
    let mut sum = 0u64;
    for i in 0..n {
        let fwd = data[i];
        let bwd = data[n - 1 - i];
        sum = sum.wrapping_add(fwd.wrapping_mul(bwd));
    }
    sum
}

/// Word-by-word processing with unwrap chains
#[inline(never)]
fn pu_20(s: &str) -> u64 {
    let words: Vec<&str> = s.split_whitespace().collect();
    let n = words.len();
    let mut result = 0u64;
    for i in 0..n {
        let current = words.get(i).unwrap();
        let next = words.get((i + 1) % n).unwrap();
        let c_first = current.chars().next().unwrap();
        let n_last = next.chars().last().unwrap();
        result = result.wrapping_add(c_first as u64 ^ n_last as u64);
    }
    result
}
