// ==========================================================================
// Rust test corpus for RustDiff analysis
// Contains diverse function patterns to exercise binary diffing at O0 vs O2
// ==========================================================================

// ---------------------------------------------------------------------------
// 1. Arithmetic functions on different integer types
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn arith_add_u32(a: u32, b: u32) -> u32 {
    a.wrapping_add(b)
}

#[no_mangle]
#[inline(never)]
pub fn arith_mul_u64(a: u64, b: u64) -> u64 {
    a.wrapping_mul(b)
}

#[no_mangle]
#[inline(never)]
pub fn arith_bitwise_i32(a: i32, b: i32) -> i32 {
    (a ^ b) & (a | b)
}

#[no_mangle]
#[inline(never)]
pub fn arith_shift_ops(val: u64, shift: u32) -> u64 {
    let left = val << (shift % 64);
    let right = val >> (shift % 64);
    left ^ right
}

#[no_mangle]
#[inline(never)]
pub fn arith_mixed_width(a: u8, b: u16, c: u32, d: u64) -> u64 {
    (a as u64) + (b as u64) * (c as u64) ^ d
}

// ---------------------------------------------------------------------------
// 2. Loop patterns
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn loop_for_iterator(data: &[u32]) -> u64 {
    let mut sum: u64 = 0;
    for &val in data.iter() {
        sum = sum.wrapping_add(val as u64);
    }
    sum
}

#[no_mangle]
#[inline(never)]
pub fn loop_while_counter(n: u32) -> u64 {
    let mut i: u32 = 0;
    let mut acc: u64 = 1;
    while i < n {
        acc = acc.wrapping_mul(3).wrapping_add(i as u64);
        i += 1;
    }
    acc
}

#[no_mangle]
#[inline(never)]
pub fn loop_nested(rows: usize, cols: usize) -> u64 {
    let mut total: u64 = 0;
    for r in 0..rows {
        for c in 0..cols {
            total = total.wrapping_add((r * cols + c) as u64);
        }
    }
    total
}

#[no_mangle]
#[inline(never)]
pub fn loop_with_break(data: &[u32], target: u32) -> Option<usize> {
    for (i, &val) in data.iter().enumerate() {
        if val == target {
            return Some(i);
        }
    }
    None
}

// ---------------------------------------------------------------------------
// 3. Bounds-check-heavy array access (elided at O2, present at O0)
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn bounds_check_sum(arr: &[u32; 256]) -> u32 {
    let mut sum = 0u32;
    // Direct indexing triggers bounds checks at O0
    let mut i = 0;
    while i < 256 {
        sum = sum.wrapping_add(arr[i]);
        i += 1;
    }
    sum
}

#[no_mangle]
#[inline(never)]
pub fn bounds_check_lookup_table(input: u8, table: &[u8; 256]) -> u8 {
    // This indexing should be bounds-check-free at O2
    table[input as usize]
}

#[no_mangle]
#[inline(never)]
pub fn bounds_check_matrix(matrix: &[[u32; 16]; 16], row: usize, col: usize) -> u32 {
    if row < 16 && col < 16 {
        matrix[row][col]
    } else {
        0
    }
}

// ---------------------------------------------------------------------------
// 4. String and slice handling
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn string_count_chars(s: &str, target: char) -> usize {
    s.chars().filter(|&c| c == target).count()
}

#[no_mangle]
#[inline(never)]
pub fn slice_reverse_bytes(data: &[u8]) -> Vec<u8> {
    let mut result = data.to_vec();
    result.reverse();
    result
}

#[no_mangle]
#[inline(never)]
pub fn string_to_uppercase_ascii(s: &str) -> String {
    s.chars()
        .map(|c| {
            if c.is_ascii_lowercase() {
                (c as u8 - b'a' + b'A') as char
            } else {
                c
            }
        })
        .collect()
}

#[no_mangle]
#[inline(never)]
pub fn slice_find_pattern(haystack: &[u8], needle: &[u8]) -> Option<usize> {
    if needle.is_empty() || needle.len() > haystack.len() {
        return None;
    }
    for i in 0..=(haystack.len() - needle.len()) {
        if &haystack[i..i + needle.len()] == needle {
            return Some(i);
        }
    }
    None
}

// ---------------------------------------------------------------------------
// 5. Generics / monomorphization
// ---------------------------------------------------------------------------

#[inline(never)]
pub fn generic_sum<T: Copy + Default + std::ops::Add<Output = T>>(items: &[T]) -> T {
    let mut acc = T::default();
    for &item in items {
        acc = acc + item;
    }
    acc
}

#[inline(never)]
pub fn generic_max<T: Copy + PartialOrd>(items: &[T]) -> Option<T> {
    let mut max = None;
    for &item in items {
        max = Some(match max {
            None => item,
            Some(current) => {
                if item > current {
                    item
                } else {
                    current
                }
            }
        });
    }
    max
}

// Force monomorphization by calling with different types
#[no_mangle]
#[inline(never)]
pub fn mono_sum_u32(data: &[u32]) -> u32 {
    generic_sum(data)
}

#[no_mangle]
#[inline(never)]
pub fn mono_sum_u64(data: &[u64]) -> u64 {
    generic_sum(data)
}

#[no_mangle]
#[inline(never)]
pub fn mono_sum_f64(data: &[f64]) -> f64 {
    generic_sum(data)
}

#[no_mangle]
#[inline(never)]
pub fn mono_max_i32(data: &[i32]) -> Option<i32> {
    generic_max(data)
}

#[no_mangle]
#[inline(never)]
pub fn mono_max_f64(data: &[f64]) -> Option<f64> {
    generic_max(data)
}

// ---------------------------------------------------------------------------
// 6. Drop glue - struct implementing Drop
// ---------------------------------------------------------------------------

pub struct ResourceHandle {
    pub id: u64,
    pub name: String,
    pub data: Vec<u8>,
}

impl Drop for ResourceHandle {
    fn drop(&mut self) {
        // Simulate cleanup - the compiler must generate drop glue
        // This is visible in the binary as a distinct function
        let _cleanup_marker = self.id.wrapping_mul(0xDEAD);
    }
}

#[no_mangle]
#[inline(never)]
pub fn drop_glue_create_and_use() -> u64 {
    let handle = ResourceHandle {
        id: 42,
        name: String::from("test_resource"),
        data: vec![1, 2, 3, 4, 5],
    };
    let result = handle.id + handle.data.len() as u64;
    // handle is dropped here - generates drop glue
    result
}

#[no_mangle]
#[inline(never)]
pub fn drop_glue_vec_of_handles() -> u64 {
    let mut handles = Vec::new();
    for i in 0..5u64 {
        handles.push(ResourceHandle {
            id: i,
            name: format!("resource_{}", i),
            data: vec![i as u8; (i + 1) as usize],
        });
    }
    let total: u64 = handles.iter().map(|h| h.id).sum();
    // All handles dropped here
    total
}

// ---------------------------------------------------------------------------
// 7. Panic paths - unwrap, expect, explicit panic
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn panic_unwrap(val: Option<u32>) -> u32 {
    val.unwrap()
}

#[no_mangle]
#[inline(never)]
pub fn panic_expect(val: Result<u32, &str>) -> u32 {
    val.expect("expected a valid u32 value")
}

#[no_mangle]
#[inline(never)]
pub fn panic_explicit(condition: bool) -> u32 {
    if !condition {
        panic!("condition was false, cannot proceed");
    }
    42
}

#[no_mangle]
#[inline(never)]
pub fn panic_index_oob(data: &[u32], idx: usize) -> u32 {
    data[idx] // may panic with index out of bounds
}

// ---------------------------------------------------------------------------
// 8. Constants and magic numbers
// ---------------------------------------------------------------------------

const MAGIC_DEADBEEF: u32 = 0xDEADBEEF;
const MAGIC_CAFEBABE: u32 = 0xCAFEBABE;
const MAGIC_8BADF00D: u64 = 0x8BADF00D;
const FIBONACCI_SEED: [u32; 8] = [1, 1, 2, 3, 5, 8, 13, 21];
const PI_APPROX: f64 = 3.14159265358979323846;

#[no_mangle]
#[inline(never)]
pub fn magic_xor_deadbeef(val: u32) -> u32 {
    val ^ MAGIC_DEADBEEF
}

#[no_mangle]
#[inline(never)]
pub fn magic_combine_constants(a: u32) -> u64 {
    let low = (a ^ MAGIC_CAFEBABE) as u64;
    let high = MAGIC_8BADF00D;
    (high << 32) | low
}

#[no_mangle]
#[inline(never)]
pub fn magic_fibonacci_lookup(idx: usize) -> u32 {
    if idx < FIBONACCI_SEED.len() {
        FIBONACCI_SEED[idx]
    } else {
        0
    }
}

#[no_mangle]
#[inline(never)]
pub fn magic_circle_area(radius: f64) -> f64 {
    PI_APPROX * radius * radius
}

// ---------------------------------------------------------------------------
// 9. Hash / crypto-like functions
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn hash_fnv1a(data: &[u8]) -> u64 {
    const FNV_OFFSET: u64 = 0xcbf29ce484222325;
    const FNV_PRIME: u64 = 0x100000001b3;

    let mut hash = FNV_OFFSET;
    for &byte in data {
        hash ^= byte as u64;
        hash = hash.wrapping_mul(FNV_PRIME);
    }
    hash
}

#[no_mangle]
#[inline(never)]
pub fn hash_xorshift64(mut state: u64) -> u64 {
    state ^= state << 13;
    state ^= state >> 7;
    state ^= state << 17;
    state
}

#[no_mangle]
#[inline(never)]
pub fn hash_simple_siphash_round(v0: u64, v1: u64, v2: u64, v3: u64) -> (u64, u64, u64, u64) {
    let mut v0 = v0;
    let mut v1 = v1;
    let mut v2 = v2;
    let mut v3 = v3;

    v0 = v0.wrapping_add(v1);
    v1 = v1.rotate_left(13);
    v1 ^= v0;
    v0 = v0.rotate_left(32);

    v2 = v2.wrapping_add(v3);
    v3 = v3.rotate_left(16);
    v3 ^= v2;

    v0 = v0.wrapping_add(v3);
    v3 = v3.rotate_left(21);
    v3 ^= v0;

    v2 = v2.wrapping_add(v1);
    v1 = v1.rotate_left(17);
    v1 ^= v2;
    v2 = v2.rotate_left(32);

    (v0, v1, v2, v3)
}

// ---------------------------------------------------------------------------
// 10. Control flow - match, if-else chains, enum dispatch
// ---------------------------------------------------------------------------

#[derive(Debug, Clone, Copy)]
pub enum Shape {
    Circle(f64),
    Rectangle(f64, f64),
    Triangle(f64, f64, f64),
    Square(f64),
}

#[no_mangle]
#[inline(never)]
pub fn shape_area(shape: &Shape) -> f64 {
    match shape {
        Shape::Circle(r) => PI_APPROX * r * r,
        Shape::Rectangle(w, h) => w * h,
        Shape::Triangle(a, b, c) => {
            // Heron's formula
            let s = (a + b + c) / 2.0;
            (s * (s - a) * (s - b) * (s - c)).sqrt()
        }
        Shape::Square(side) => side * side,
    }
}

#[no_mangle]
#[inline(never)]
pub fn classify_number(n: i64) -> &'static str {
    match n {
        i64::MIN..=-100 => "very negative",
        -99..=-1 => "negative",
        0 => "zero",
        1..=99 => "positive",
        100..=i64::MAX => "very positive",
    }
}

// ---------------------------------------------------------------------------
// 11. Recursive functions
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn recursive_fibonacci(n: u32) -> u64 {
    if n <= 1 {
        return n as u64;
    }
    recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
}

#[no_mangle]
#[inline(never)]
pub fn recursive_gcd(a: u64, b: u64) -> u64 {
    if b == 0 {
        a
    } else {
        recursive_gcd(b, a % b)
    }
}

// ---------------------------------------------------------------------------
// 12. Closures and higher-order functions
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn closure_map_filter(data: &[i32]) -> Vec<i32> {
    data.iter()
        .filter(|&&x| x > 0)
        .map(|&x| x * x)
        .collect()
}

#[no_mangle]
#[inline(never)]
pub fn closure_fold_product(data: &[u32]) -> u64 {
    data.iter().fold(1u64, |acc, &x| acc.wrapping_mul(x as u64))
}

// ---------------------------------------------------------------------------
// 13. Trait objects / dynamic dispatch
// ---------------------------------------------------------------------------

pub trait Transformer {
    fn transform(&self, input: u64) -> u64;
}

struct Doubler;
impl Transformer for Doubler {
    fn transform(&self, input: u64) -> u64 {
        input.wrapping_mul(2)
    }
}

struct Hasher;
impl Transformer for Hasher {
    fn transform(&self, input: u64) -> u64 {
        hash_xorshift64(input)
    }
}

#[no_mangle]
#[inline(never)]
pub fn dynamic_dispatch_chain(input: u64) -> u64 {
    let transformers: Vec<Box<dyn Transformer>> = vec![
        Box::new(Doubler),
        Box::new(Hasher),
        Box::new(Doubler),
    ];
    let mut val = input;
    for t in &transformers {
        val = t.transform(val);
    }
    val
}

// ---------------------------------------------------------------------------
// 14. Unsafe code block
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn unsafe_ptr_arithmetic(data: &[u32]) -> u64 {
    if data.is_empty() {
        return 0;
    }
    let mut sum: u64 = 0;
    let ptr = data.as_ptr();
    let len = data.len();
    unsafe {
        for i in 0..len {
            sum = sum.wrapping_add(*ptr.add(i) as u64);
        }
    }
    sum
}

// ---------------------------------------------------------------------------
// 15. Sorting / algorithmic function
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn bubble_sort(data: &mut [u32]) {
    let n = data.len();
    for i in 0..n {
        for j in 0..n.saturating_sub(i + 1) {
            if data[j] > data[j + 1] {
                data.swap(j, j + 1);
            }
        }
    }
}

#[no_mangle]
#[inline(never)]
pub fn binary_search_manual(sorted: &[u32], target: u32) -> Option<usize> {
    let mut lo = 0usize;
    let mut hi = sorted.len();
    while lo < hi {
        let mid = lo + (hi - lo) / 2;
        match sorted[mid].cmp(&target) {
            std::cmp::Ordering::Equal => return Some(mid),
            std::cmp::Ordering::Less => lo = mid + 1,
            std::cmp::Ordering::Greater => hi = mid,
        }
    }
    None
}

// ---------------------------------------------------------------------------
// 16. Bit manipulation
// ---------------------------------------------------------------------------

#[no_mangle]
#[inline(never)]
pub fn popcount_naive(mut x: u64) -> u32 {
    let mut count = 0u32;
    while x != 0 {
        count += (x & 1) as u32;
        x >>= 1;
    }
    count
}

#[no_mangle]
#[inline(never)]
pub fn next_power_of_two(mut n: u64) -> u64 {
    if n == 0 {
        return 1;
    }
    n -= 1;
    n |= n >> 1;
    n |= n >> 2;
    n |= n >> 4;
    n |= n >> 8;
    n |= n >> 16;
    n |= n >> 32;
    n + 1
}

#[no_mangle]
#[inline(never)]
pub fn reverse_bits_u32(mut x: u32) -> u32 {
    let mut result = 0u32;
    for _ in 0..32 {
        result = (result << 1) | (x & 1);
        x >>= 1;
    }
    result
}
