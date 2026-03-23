use std::hint::black_box;
use testcrate::*;

fn main() {
    // 1. Arithmetic
    let r1 = arith_add_u32(black_box(100), black_box(200));
    let r2 = arith_mul_u64(black_box(123456), black_box(789012));
    let r3 = arith_bitwise_i32(black_box(0xFF00FF), black_box(0x00FF00));
    let r4 = arith_shift_ops(black_box(0xABCD1234), black_box(7));
    let r5 = arith_mixed_width(black_box(10), black_box(20), black_box(30), black_box(40));
    println!("Arithmetic: {} {} {} {} {}", r1, r2, r3, r4, r5);

    // 2. Loops
    let data = vec![1u32, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    let r6 = loop_for_iterator(black_box(&data));
    let r7 = loop_while_counter(black_box(20));
    let r8 = loop_nested(black_box(10), black_box(10));
    let r9 = loop_with_break(black_box(&data), black_box(7));
    println!("Loops: {} {} {} {:?}", r6, r7, r8, r9);

    // 3. Bounds checks
    let arr256: [u32; 256] = {
        let mut a = [0u32; 256];
        for i in 0..256 {
            a[i] = i as u32;
        }
        a
    };
    let r10 = bounds_check_sum(black_box(&arr256));
    let table256: [u8; 256] = {
        let mut t = [0u8; 256];
        for i in 0..256 {
            t[i] = (255 - i) as u8;
        }
        t
    };
    let r11 = bounds_check_lookup_table(black_box(42), black_box(&table256));
    let matrix: [[u32; 16]; 16] = {
        let mut m = [[0u32; 16]; 16];
        for r in 0..16 {
            for c in 0..16 {
                m[r][c] = (r * 16 + c) as u32;
            }
        }
        m
    };
    let r12 = bounds_check_matrix(black_box(&matrix), black_box(5), black_box(10));
    println!("Bounds: {} {} {}", r10, r11, r12);

    // 4. String/slice handling
    let r13 = string_count_chars(black_box("hello world, hello rust!"), black_box('l'));
    let r14 = slice_reverse_bytes(black_box(b"abcdef"));
    let r15 = string_to_uppercase_ascii(black_box("hello world"));
    let r16 = slice_find_pattern(black_box(b"the quick brown fox"), black_box(b"brown"));
    println!("Strings: {} {:?} {} {:?}", r13, r14, r15, r16);

    // 5. Generics / monomorphization
    let u32_data = vec![1u32, 2, 3, 4, 5];
    let u64_data = vec![10u64, 20, 30, 40, 50];
    let f64_data = vec![1.1f64, 2.2, 3.3, 4.4, 5.5];
    let i32_data = vec![-5i32, 3, -1, 7, 2];

    let r17 = mono_sum_u32(black_box(&u32_data));
    let r18 = mono_sum_u64(black_box(&u64_data));
    let r19 = mono_sum_f64(black_box(&f64_data));
    let r20 = mono_max_i32(black_box(&i32_data));
    let r21 = mono_max_f64(black_box(&f64_data));
    println!("Generics: {} {} {} {:?} {:?}", r17, r18, r19, r20, r21);

    // 6. Drop glue
    let r22 = drop_glue_create_and_use();
    let r23 = drop_glue_vec_of_handles();
    println!("Drop: {} {}", r22, r23);

    // 7. Panic paths (use safe values to avoid actual panics)
    let r24 = panic_unwrap(black_box(Some(99)));
    let r25 = panic_expect(black_box(Ok(77)));
    let r26 = panic_explicit(black_box(true));
    let r27 = panic_index_oob(black_box(&data), black_box(3));
    println!("Panic: {} {} {} {}", r24, r25, r26, r27);

    // 8. Magic numbers
    let r28 = magic_xor_deadbeef(black_box(0x12345678));
    let r29 = magic_combine_constants(black_box(0xAABBCCDD));
    let r30 = magic_fibonacci_lookup(black_box(5));
    let r31 = magic_circle_area(black_box(5.0));
    println!("Magic: {} {} {} {}", r28, r29, r30, r31);

    // 9. Hash/crypto
    let r32 = hash_fnv1a(black_box(b"hello world"));
    let r33 = hash_xorshift64(black_box(12345));
    let r34 = hash_simple_siphash_round(
        black_box(0x736f6d6570736575),
        black_box(0x646f72616e646f6d),
        black_box(0x6c7967656e657261),
        black_box(0x7465646279746573),
    );
    println!("Hash: {} {} {:?}", r32, r33, r34);

    // 10. Control flow / enum dispatch
    let shapes = [
        Shape::Circle(3.0),
        Shape::Rectangle(4.0, 5.0),
        Shape::Triangle(3.0, 4.0, 5.0),
        Shape::Square(6.0),
    ];
    for shape in &shapes {
        println!("Shape area: {}", shape_area(black_box(shape)));
    }
    println!("Classify: {}", classify_number(black_box(-42)));
    println!("Classify: {}", classify_number(black_box(0)));
    println!("Classify: {}", classify_number(black_box(500)));

    // 11. Recursion
    let r35 = recursive_fibonacci(black_box(15));
    let r36 = recursive_gcd(black_box(48), black_box(18));
    println!("Recursion: fib={} gcd={}", r35, r36);

    // 12. Closures
    let mixed = vec![-3i32, -1, 0, 2, 5, -4, 8];
    let r37 = closure_map_filter(black_box(&mixed));
    let r38 = closure_fold_product(black_box(&u32_data));
    println!("Closures: {:?} {}", r37, r38);

    // 13. Dynamic dispatch
    let r39 = dynamic_dispatch_chain(black_box(42));
    println!("DynDispatch: {}", r39);

    // 14. Unsafe
    let r40 = unsafe_ptr_arithmetic(black_box(&data));
    println!("Unsafe: {}", r40);

    // 15. Sorting
    let mut sort_data = vec![9u32, 3, 7, 1, 5, 8, 2, 6, 4, 10];
    bubble_sort(black_box(&mut sort_data));
    println!("BubbleSort: {:?}", sort_data);

    let sorted = vec![1u32, 3, 5, 7, 9, 11, 13, 15];
    let r41 = binary_search_manual(black_box(&sorted), black_box(7));
    println!("BinSearch: {:?}", r41);

    // 16. Bit manipulation
    let r42 = popcount_naive(black_box(0xDEADBEEF));
    let r43 = next_power_of_two(black_box(1000));
    let r44 = reverse_bits_u32(black_box(0b10110011));
    println!("Bits: {} {} {}", r42, r43, r44);
}
