## Function `bc_07`

### Rust `bc_07` — O0: 99 blocks, O2: 44 blocks

**O0 blocks** (99 total):

```asm
; --- Block 0x446470 [BODY] 10 insns, callees: (none)
    0x446470: sub      rsp, 0x1e8
    0x446477: mov      qword ptr [rsp + 0x108], rdx
    0x44647f: mov      qword ptr [rsp + 0x110], rsi
    0x446487: mov      qword ptr [rsp + 0x118], rdi
    0x44648f: mov      qword ptr [rsp + 0x120], rdi
    0x446497: mov      qword ptr [rsp + 0x1a8], rsi
    0x44649f: mov      qword ptr [rsp + 0x1b0], rdx
    0x4464a7: mov      qword ptr [rsp + 0x1b8], rdx
    0x4464af: cmp      rdx, 3
    0x4464b3: jb       0x4464d4

; --- Block 0x4464b5 [ITERATOR_STATE] 6 insns, callees: (none)
    0x4464b5: mov      rax, qword ptr [rsp + 0x108]
    0x4464bd: mov      rcx, rax
    0x4464c0: sub      rcx, 2
    0x4464c4: mov      qword ptr [rsp + 0x100], rcx
    0x4464cc: cmp      rax, 2
    0x4464d0: jb       0x44651a

; --- Block 0x4464d2 [BODY] 1 insns, callees: (none)
    0x4464d2: jmp      0x4464e6

; --- Block 0x4464d4 [BODY] 2 insns, callees: alloc::vec::Vec<T>::new
    0x4464d4: mov      rdi, qword ptr [rsp + 0x118]
    0x4464dc: call     0x4a51e0

; --- Block 0x4464e1 [BODY] 1 insns, callees: (none)
    0x4464e1: jmp      0x44677f

; --- Block 0x4464e6 [BODY] 3 insns, callees: alloc::vec::Vec<T>::with_capacity
    0x4464e6: mov      rsi, qword ptr [rsp + 0x100]
    0x4464ee: lea      rdi, [rsp + 0x128]
    0x4464f6: call     0x4a4fd0

; --- Block 0x4464fb [ITERATOR_STATE] 6 insns, callees: (none)
    0x4464fb: mov      rax, qword ptr [rsp + 0x108]
    0x446503: mov      rcx, rax
    0x446506: sub      rcx, 1
    0x44650a: mov      qword ptr [rsp + 0xf8], rcx
    0x446512: cmp      rax, 1
    0x446516: jb       0x44654b

; --- Block 0x446518 [BODY] 1 insns, callees: (none)
    0x446518: jmp      0x446527

; --- Block 0x44651a [BODY] 2 insns, callees: (none)
    0x44651a: lea      rdi, [rip + 0xa8c07]
    0x446521: call     qword ptr [rip + 0xaec29]

; --- Block 0x446527 [BODY] 3 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x446527: mov      rsi, qword ptr [rsp + 0xf8]
    0x44652f: mov      edi, 1
    0x446534: call     0x49b480

; --- Block 0x446539 [BODY] 3 insns, callees: (none)
    0x446539: mov      qword ptr [rsp + 0xe8], rdx
    0x446541: mov      qword ptr [rsp + 0xf0], rax
    0x446549: jmp      0x446587

; --- Block 0x44654b [BODY] 3 insns, callees: (none)
    0x44654b: lea      rdi, [rip + 0xa8bee]
    0x446552: mov      rax, qword ptr [rip + 0xaebf7]
    0x446559: call     rax

; --- Block 0x446587 [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x446587: mov      rax, qword ptr [rsp + 0xe8]
    0x44658f: mov      rcx, qword ptr [rsp + 0xf0]
    0x446597: mov      qword ptr [rsp + 0x140], rcx
    0x44659f: mov      qword ptr [rsp + 0x148], rax
    0x4465a7: lea      rdi, [rsp + 0x140]
    0x4465af: call     0x49ad10

; --- Block 0x4465a7 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4465a7: lea      rdi, [rsp + 0x140]
    0x4465af: call     0x49ad10

; --- Block 0x4465b4 [BODY] 3 insns, callees: (none)
    0x4465b4: mov      qword ptr [rsp + 0xd8], rdx
    0x4465bc: mov      qword ptr [rsp + 0xe0], rax
    0x4465c4: jmp      0x4465c6

; --- Block 0x4465c6 [BODY] 6 insns, callees: (none)
    0x4465c6: mov      rax, qword ptr [rsp + 0xd8]
    0x4465ce: mov      rcx, qword ptr [rsp + 0xe0]
    0x4465d6: mov      qword ptr [rsp + 0x150], rcx
    0x4465de: mov      qword ptr [rsp + 0x158], rax
    0x4465e6: test     qword ptr [rsp + 0x150], 1
    0x4465f2: je       0x44662a

; --- Block 0x4465f4 [BODY] 8 insns, callees: (none)
    0x4465f4: mov      rax, qword ptr [rsp + 0x158]
    0x4465fc: mov      qword ptr [rsp + 0xc8], rax
    0x446604: mov      qword ptr [rsp + 0x1d8], rax
    0x44660c: mov      rcx, rax
    0x44660f: sub      rcx, 1
    0x446613: mov      qword ptr [rsp + 0xd0], rcx
    0x44661b: cmp      rax, 1
    0x44661f: jb       0x446a25

; --- Block 0x446625 [BODY] 1 insns, callees: (none)
    0x446625: jmp      0x446a0e

; --- Block 0x44662a [BODY] 2 insns, callees: alloc::vec::Vec<T,A>::len
    0x44662a: lea      rdi, [rsp + 0x128]
    0x446632: call     0x4a8e90

; --- Block 0x446637 [BODY] 2 insns, callees: (none)
    0x446637: mov      qword ptr [rsp + 0xc0], rax
    0x44663f: jmp      0x446641

; --- Block 0x446641 [BODY] 3 insns, callees: alloc::vec::Vec<T>::with_capacity
    0x446641: mov      rsi, qword ptr [rsp + 0xc0]
    0x446649: lea      rdi, [rsp + 0x160]
    0x446651: call     0x4a4fd0

; --- Block 0x446656 [BODY] 1 insns, callees: (none)
    0x446656: jmp      0x446658

; --- Block 0x446658 [BODY] 2 insns, callees: alloc::vec::Vec<T,A>::len
    0x446658: lea      rdi, [rsp + 0x128]
    0x446660: call     0x4a8e90

; --- Block 0x446665 [BODY] 2 insns, callees: (none)
    0x446665: mov      qword ptr [rsp + 0xb8], rax
    0x44666d: jmp      0x446697

; --- Block 0x446697 [BODY] 4 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x446697: mov      rsi, qword ptr [rsp + 0xb8]
    0x44669f: xor      eax, eax
    0x4466a1: mov      edi, eax
    0x4466a3: call     0x49b480

; --- Block 0x4466a8 [BODY] 3 insns, callees: (none)
    0x4466a8: mov      qword ptr [rsp + 0xa8], rdx
    0x4466b0: mov      qword ptr [rsp + 0xb0], rax
    0x4466b8: jmp      0x4466ba

; --- Block 0x4466ba [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4466ba: mov      rax, qword ptr [rsp + 0xa8]
    0x4466c2: mov      rcx, qword ptr [rsp + 0xb0]
    0x4466ca: mov      qword ptr [rsp + 0x178], rcx
    0x4466d2: mov      qword ptr [rsp + 0x180], rax
    0x4466da: lea      rdi, [rsp + 0x178]
    0x4466e2: call     0x49ad10

; --- Block 0x4466da [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4466da: lea      rdi, [rsp + 0x178]
    0x4466e2: call     0x49ad10

; --- Block 0x4466e7 [BODY] 3 insns, callees: (none)
    0x4466e7: mov      qword ptr [rsp + 0x98], rdx
    0x4466ef: mov      qword ptr [rsp + 0xa0], rax
    0x4466f7: jmp      0x4466f9

; --- Block 0x4466f9 [BODY] 6 insns, callees: (none)
    0x4466f9: mov      rax, qword ptr [rsp + 0x98]
    0x446701: mov      rcx, qword ptr [rsp + 0xa0]
    0x446709: mov      qword ptr [rsp + 0x188], rcx
    0x446711: mov      qword ptr [rsp + 0x190], rax
    0x446719: test     qword ptr [rsp + 0x188], 1
    0x446725: je       0x446747

; --- Block 0x446727 [BODY] 5 insns, callees: (none)
    0x446727: mov      rax, qword ptr [rsp + 0x190]
    0x44672f: mov      qword ptr [rsp + 0x90], rax
    0x446737: mov      qword ptr [rsp + 0x1d0], rax
    0x44673f: cmp      rax, 0
    0x446743: ja       0x4467b5

; --- Block 0x446745 [BODY] 1 insns, callees: (none)
    0x446745: jmp      0x44678f

; --- Block 0x446747 [DROP_GLUE] 9 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<i64>>
    0x446747: mov      rax, qword ptr [rsp + 0x118]
    0x44674f: mov      rcx, qword ptr [rsp + 0x160]
    0x446757: mov      qword ptr [rax], rcx
    0x44675a: mov      rcx, qword ptr [rsp + 0x168]
    0x446762: mov      qword ptr [rax + 8], rcx
    0x446766: mov      rcx, qword ptr [rsp + 0x170]
    0x44676e: mov      qword ptr [rax + 0x10], rcx
    0x446772: lea      rdi, [rsp + 0x128]
    0x44677a: call     0x4967d0

; --- Block 0x44677f [EPILOGUE] 3 insns, callees: (none)
    0x44677f: mov      rax, qword ptr [rsp + 0x120]
    0x446787: add      rsp, 0x1e8
    0x44678e: ret      

; --- Block 0x44678f [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x44678f: mov      rsi, qword ptr [rsp + 0x90]
    0x446797: lea      rdx, [rip + 0xa89ba]
    0x44679e: lea      rdi, [rsp + 0x128]
    0x4467a6: call     0x4ab8b0

; --- Block 0x4467ab [BODY] 2 insns, callees: (none)
    0x4467ab: mov      qword ptr [rsp + 0x88], rax
    0x4467b3: jmp      0x4467d4

; --- Block 0x4467b5 [ITERATOR_STATE] 6 insns, callees: (none)
    0x4467b5: mov      rax, qword ptr [rsp + 0x90]
    0x4467bd: mov      rcx, rax
    0x4467c0: sub      rcx, 1
    0x4467c4: mov      qword ptr [rsp + 0x80], rcx
    0x4467cc: cmp      rax, 1
    0x4467d0: jb       0x446825

; --- Block 0x4467d2 [BODY] 1 insns, callees: (none)
    0x4467d2: jmp      0x446802

; --- Block 0x4467d4 [BODY] 9 insns, callees: (none)
    0x4467d4: mov      rax, qword ptr [rsp + 0x88]
    0x4467dc: mov      rax, qword ptr [rax]
    0x4467df: mov      qword ptr [rsp + 0x198], rax
    0x4467e7: mov      rcx, qword ptr [rsp + 0x90]
    0x4467ef: mov      rax, rcx
    0x4467f2: add      rax, 1
    0x4467f6: mov      qword ptr [rsp + 0x78], rax
    0x4467fb: cmp      rax, rcx
    0x4467fe: jb       0x446860

; --- Block 0x4467e7 [LOOP_HEADER] 6 insns, callees: (none)
    0x4467e7: mov      rcx, qword ptr [rsp + 0x90]
    0x4467ef: mov      rax, rcx
    0x4467f2: add      rax, 1
    0x4467f6: mov      qword ptr [rsp + 0x78], rax
    0x4467fb: cmp      rax, rcx
    0x4467fe: jb       0x446860

; --- Block 0x446800 [BODY] 1 insns, callees: (none)
    0x446800: jmp      0x44684c

; --- Block 0x446802 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x446802: mov      rsi, qword ptr [rsp + 0x80]
    0x44680a: lea      rdx, [rip + 0xa8977]
    0x446811: lea      rdi, [rsp + 0x128]
    0x446819: call     0x4ab8b0

; --- Block 0x44681e [BODY] 2 insns, callees: (none)
    0x44681e: mov      qword ptr [rsp + 0x70], rax
    0x446823: jmp      0x44683a

; --- Block 0x446825 [BODY] 3 insns, callees: (none)
    0x446825: lea      rdi, [rip + 0xa8944]
    0x44682c: mov      rax, qword ptr [rip + 0xae91d]
    0x446833: call     rax

; --- Block 0x44683a [BODY] 4 insns, callees: (none)
    0x44683a: mov      rax, qword ptr [rsp + 0x70]
    0x44683f: mov      rax, qword ptr [rax]
    0x446842: mov      qword ptr [rsp + 0x198], rax
    0x44684a: jmp      0x4467e7

; --- Block 0x44684c [BODY] 2 insns, callees: alloc::vec::Vec<T,A>::len
    0x44684c: lea      rdi, [rsp + 0x128]
    0x446854: call     0x4a8e90

; --- Block 0x446859 [BODY] 2 insns, callees: (none)
    0x446859: mov      qword ptr [rsp + 0x68], rax
    0x44685e: jmp      0x446875

; --- Block 0x446860 [BODY] 3 insns, callees: (none)
    0x446860: lea      rdi, [rip + 0xa8939]
    0x446867: mov      rax, qword ptr [rip + 0xae8c2]
    0x44686e: call     rax

; --- Block 0x446875 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x446875: mov      rax, qword ptr [rsp + 0x78]
    0x44687a: mov      rcx, qword ptr [rsp + 0x68]
    0x44687f: cmp      rax, rcx
    0x446882: jb       0x4468a7

; --- Block 0x446884 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x446884: mov      rsi, qword ptr [rsp + 0x90]
    0x44688c: lea      rdx, [rip + 0xa8925]
    0x446893: lea      rdi, [rsp + 0x128]
    0x44689b: call     0x4ab8b0

; --- Block 0x4468a0 [BODY] 2 insns, callees: (none)
    0x4468a0: mov      qword ptr [rsp + 0x60], rax
    0x4468a5: jmp      0x4468c2

; --- Block 0x4468a7 [ITERATOR_STATE] 6 insns, callees: (none)
    0x4468a7: mov      rcx, qword ptr [rsp + 0x90]
    0x4468af: mov      rax, rcx
    0x4468b2: add      rax, 1
    0x4468b6: mov      qword ptr [rsp + 0x58], rax
    0x4468bb: cmp      rax, rcx
    0x4468be: jb       0x446922

; --- Block 0x4468c0 [BODY] 1 insns, callees: (none)
    0x4468c0: jmp      0x446902

; --- Block 0x4468c2 [BODY] 9 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x4468c2: mov      rax, qword ptr [rsp + 0x60]
    0x4468c7: mov      rax, qword ptr [rax]
    0x4468ca: mov      qword ptr [rsp + 0x1a0], rax
    0x4468d2: mov      rsi, qword ptr [rsp + 0x90]
    0x4468da: mov      rax, qword ptr [rsp + 0x198]
    0x4468e2: mov      qword ptr [rsp + 0x48], rax
    0x4468e7: lea      rdx, [rip + 0xa8912]
    0x4468ee: lea      rdi, [rsp + 0x128]
    0x4468f6: call     0x4ab8b0

; --- Block 0x4468d2 [LOOP_HEADER] 6 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x4468d2: mov      rsi, qword ptr [rsp + 0x90]
    0x4468da: mov      rax, qword ptr [rsp + 0x198]
    0x4468e2: mov      qword ptr [rsp + 0x48], rax
    0x4468e7: lea      rdx, [rip + 0xa8912]
    0x4468ee: lea      rdi, [rsp + 0x128]
    0x4468f6: call     0x4ab8b0

; --- Block 0x4468fb [BODY] 2 insns, callees: (none)
    0x4468fb: mov      qword ptr [rsp + 0x50], rax
    0x446900: jmp      0x446949

; --- Block 0x446902 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x446902: mov      rsi, qword ptr [rsp + 0x58]
    0x446907: lea      rdx, [rip + 0xa88da]
    0x44690e: lea      rdi, [rsp + 0x128]
    0x446916: call     0x4ab8b0

; --- Block 0x44691b [BODY] 2 insns, callees: (none)
    0x44691b: mov      qword ptr [rsp + 0x40], rax
    0x446920: jmp      0x446937

; --- Block 0x446922 [BODY] 3 insns, callees: (none)
    0x446922: lea      rdi, [rip + 0xa88a7]
    0x446929: mov      rax, qword ptr [rip + 0xae800]
    0x446930: call     rax

; --- Block 0x446937 [BODY] 4 insns, callees: (none)
    0x446937: mov      rax, qword ptr [rsp + 0x40]
    0x44693c: mov      rax, qword ptr [rax]
    0x44693f: mov      qword ptr [rsp + 0x1a0], rax
    0x446947: jmp      0x4468d2

; --- Block 0x446949 [BODY] 6 insns, callees: (none)
    0x446949: mov      rcx, qword ptr [rsp + 0x50]
    0x44694e: mov      rax, qword ptr [rsp + 0x48]
    0x446953: add      rax, qword ptr [rcx]
    0x446956: mov      qword ptr [rsp + 0x38], rax
    0x44695b: seto     al
    0x44695e: jo       0x446979

; --- Block 0x446960 [BODY] 5 insns, callees: (none)
    0x446960: mov      rax, qword ptr [rsp + 0x38]
    0x446965: add      rax, qword ptr [rsp + 0x1a0]
    0x44696d: mov      qword ptr [rsp + 0x30], rax
    0x446972: seto     al
    0x446975: jo       0x446990

; --- Block 0x446977 [BODY] 1 insns, callees: (none)
    0x446977: jmp      0x44698e

; --- Block 0x446979 [BODY] 3 insns, callees: (none)
    0x446979: lea      rdi, [rip + 0xa8898]
    0x446980: mov      rax, qword ptr [rip + 0xae7a9]
    0x446987: call     rax

; --- Block 0x44698e [BODY] 1 insns, callees: (none)
    0x44698e: jmp      0x4469a5

; --- Block 0x446990 [BODY] 3 insns, callees: (none)
    0x446990: lea      rdi, [rip + 0xa8899]
    0x446997: mov      rax, qword ptr [rip + 0xae792]
    0x44699e: call     rax

; --- Block 0x4469a5 [BODY] 7 insns, callees: (none)
    0x4469a5: mov      rax, qword ptr [rsp + 0x30]
    0x4469aa: movabs   rcx, 0x8000000000000000
    0x4469b4: cmp      rax, rcx
    0x4469b7: sete     al
    0x4469ba: and      al, 0
    0x4469bc: test     al, 1
    0x4469be: jne      0x4469ee

; --- Block 0x4469c0 [BODY] 9 insns, callees: alloc::vec::Vec<T,A>::push
    0x4469c0: mov      rax, qword ptr [rsp + 0x30]
    0x4469c5: movabs   rcx, 0x5555555555555556
    0x4469cf: imul     rcx
    0x4469d2: mov      rsi, rdx
    0x4469d5: mov      rdx, rsi
    0x4469d8: shr      rdx, 0x3f
    0x4469dc: add      rsi, rdx
    0x4469df: lea      rdi, [rsp + 0x160]
    0x4469e7: call     0x4a90e0

; --- Block 0x4469ec [BODY] 1 insns, callees: (none)
    0x4469ec: jmp      0x446a03

; --- Block 0x4469ee [BODY] 3 insns, callees: (none)
    0x4469ee: lea      rdi, [rip + 0xa883b]
    0x4469f5: mov      rax, qword ptr [rip + 0xae75c]
    0x4469fc: call     rax

; --- Block 0x446a03 [BODY] 1 insns, callees: (none)
    0x446a03: jmp      0x4466da

; --- Block 0x446a0e [BOUNDS_CHECK] 4 insns, callees: (none)
    0x446a0e: mov      rax, qword ptr [rsp + 0xd0]
    0x446a16: mov      rcx, qword ptr [rsp + 0x108]
    0x446a1e: cmp      rax, rcx
    0x446a21: jb       0x446a3a

; --- Block 0x446a23 [BODY] 1 insns, callees: (none)
    0x446a23: jmp      0x446a64

; --- Block 0x446a25 [BODY] 3 insns, callees: (none)
    0x446a25: lea      rdi, [rip + 0xa881c]
    0x446a2c: mov      rax, qword ptr [rip + 0xae71d]
    0x446a33: call     rax

; --- Block 0x446a3a [BODY] 7 insns, callees: (none)
    0x446a3a: mov      rax, qword ptr [rsp + 0x110]
    0x446a42: mov      rcx, qword ptr [rsp + 0xd0]
    0x446a4a: mov      rax, qword ptr [rax + rcx*8]
    0x446a4e: mov      qword ptr [rsp + 0x28], rax
    0x446a53: movabs   rcx, 0x8000000000000000
    0x446a5d: cmp      rax, rcx
    0x446a60: je       0x446aaf

; --- Block 0x446a62 [BODY] 1 insns, callees: (none)
    0x446a62: jmp      0x446a89

; --- Block 0x446a64 [BODY] 5 insns, callees: (none)
    0x446a64: mov      rsi, qword ptr [rsp + 0x108]
    0x446a6c: mov      rdi, qword ptr [rsp + 0xd0]
    0x446a74: lea      rdx, [rip + 0xa87e5]
    0x446a7b: mov      rax, qword ptr [rip + 0xae616]
    0x446a82: call     rax

; --- Block 0x446a89 [BODY] 8 insns, callees: (none)
    0x446a89: mov      rax, qword ptr [rsp + 0xc8]
    0x446a91: mov      rcx, qword ptr [rsp + 0x108]
    0x446a99: mov      rsi, qword ptr [rsp + 0x28]
    0x446a9e: xor      edx, edx
    0x446aa0: sub      rdx, rsi
    0x446aa3: mov      qword ptr [rsp + 0x20], rdx
    0x446aa8: cmp      rax, rcx
    0x446aab: jb       0x446ac4

; --- Block 0x446aad [BODY] 1 insns, callees: (none)
    0x446aad: jmp      0x446aea

; --- Block 0x446aaf [BODY] 3 insns, callees: (none)
    0x446aaf: lea      rdi, [rip + 0xa87c2]
    0x446ab6: mov      rax, qword ptr [rip + 0xae6a3]
    0x446abd: call     rax

; --- Block 0x446ac4 [BODY] 7 insns, callees: (none)
    0x446ac4: mov      rcx, qword ptr [rsp + 0x110]
    0x446acc: mov      rdx, qword ptr [rsp + 0xc8]
    0x446ad4: mov      eax, 2
    0x446ad9: imul     rax, qword ptr [rcx + rdx*8]
    0x446ade: mov      qword ptr [rsp + 0x18], rax
    0x446ae3: seto     al
    0x446ae6: jo       0x446b28

; --- Block 0x446ae8 [BODY] 1 insns, callees: (none)
    0x446ae8: jmp      0x446b0f

; --- Block 0x446aea [BODY] 5 insns, callees: (none)
    0x446aea: mov      rsi, qword ptr [rsp + 0x108]
    0x446af2: mov      rdi, qword ptr [rsp + 0xc8]
    0x446afa: lea      rdx, [rip + 0xa878f]
    0x446b01: mov      rax, qword ptr [rip + 0xae590]
    0x446b08: call     rax

; --- Block 0x446b0f [BODY] 6 insns, callees: (none)
    0x446b0f: mov      rcx, qword ptr [rsp + 0x18]
    0x446b14: mov      rax, qword ptr [rsp + 0x20]
    0x446b19: add      rax, rcx
    0x446b1c: mov      qword ptr [rsp + 0x10], rax
    0x446b21: seto     al
    0x446b24: jo       0x446b58

; --- Block 0x446b26 [BODY] 1 insns, callees: (none)
    0x446b26: jmp      0x446b3d

; --- Block 0x446b28 [BODY] 3 insns, callees: (none)
    0x446b28: lea      rdi, [rip + 0xa8779]
    0x446b2f: mov      rax, qword ptr [rip + 0xae602]
    0x446b36: call     rax

; --- Block 0x446b3d [ITERATOR_STATE] 6 insns, callees: (none)
    0x446b3d: mov      rcx, qword ptr [rsp + 0xc8]
    0x446b45: mov      rax, rcx
    0x446b48: add      rax, 1
    0x446b4c: mov      qword ptr [rsp + 8], rax
    0x446b51: cmp      rax, rcx
    0x446b54: jb       0x446b81

; --- Block 0x446b56 [BODY] 1 insns, callees: (none)
    0x446b56: jmp      0x446b6d

; --- Block 0x446b58 [BODY] 3 insns, callees: (none)
    0x446b58: lea      rdi, [rip + 0xa8719]
    0x446b5f: mov      rax, qword ptr [rip + 0xae5ca]
    0x446b66: call     rax

; --- Block 0x446b6d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x446b6d: mov      rax, qword ptr [rsp + 8]
    0x446b72: mov      rcx, qword ptr [rsp + 0x108]
    0x446b7a: cmp      rax, rcx
    0x446b7d: jb       0x446b96

; --- Block 0x446b7f [BODY] 1 insns, callees: (none)
    0x446b7f: jmp      0x446bb7

; --- Block 0x446b81 [BODY] 3 insns, callees: (none)
    0x446b81: lea      rdi, [rip + 0xa8738]
    0x446b88: mov      rax, qword ptr [rip + 0xae5a1]
    0x446b8f: call     rax

; --- Block 0x446b96 [BODY] 7 insns, callees: (none)
    0x446b96: mov      rcx, qword ptr [rsp + 0x110]
    0x446b9e: mov      rdx, qword ptr [rsp + 8]
    0x446ba3: mov      rax, qword ptr [rsp + 0x10]
    0x446ba8: sub      rax, qword ptr [rcx + rdx*8]
    0x446bac: mov      qword ptr [rsp], rax
    0x446bb0: seto     al
    0x446bb3: jo       0x446bf4

; --- Block 0x446bb5 [BODY] 1 insns, callees: (none)
    0x446bb5: jmp      0x446bd9

; --- Block 0x446bb7 [BODY] 5 insns, callees: (none)
    0x446bb7: mov      rsi, qword ptr [rsp + 0x108]
    0x446bbf: mov      rdi, qword ptr [rsp + 8]
    0x446bc4: lea      rdx, [rip + 0xa870d]
    0x446bcb: mov      rax, qword ptr [rip + 0xae4c6]
    0x446bd2: call     rax

; --- Block 0x446bd9 [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x446bd9: mov      rsi, qword ptr [rsp]
    0x446bdd: mov      qword ptr [rsp + 0x1e0], rsi
    0x446be5: lea      rdi, [rsp + 0x128]
    0x446bed: call     0x4a90e0

; --- Block 0x446bf2 [BODY] 1 insns, callees: (none)
    0x446bf2: jmp      0x446c09

; --- Block 0x446bf4 [BODY] 3 insns, callees: (none)
    0x446bf4: lea      rdi, [rip + 0xa867d]
    0x446bfb: mov      rax, qword ptr [rip + 0xae54e]
    0x446c02: call     rax

; --- Block 0x446c09 [BODY] 1 insns, callees: (none)
    0x446c09: jmp      0x4465a7

```

**O2 blocks** (44 total):

```asm
; --- Block 0x422ef0 [BODY] 9 insns, callees: (none)
    0x422ef0: push     rbp
    0x422ef1: push     r15
    0x422ef3: push     r14
    0x422ef5: push     r13
    0x422ef7: push     r12
    0x422ef9: push     rbx
    0x422efa: sub      rsp, 0x48
    0x422efe: cmp      rdx, 3
    0x422f02: jae      0x422f20

; --- Block 0x422f04 [BODY] 4 insns, callees: (none)
    0x422f04: mov      qword ptr [rdi], 0
    0x422f0b: mov      qword ptr [rdi + 8], 8
    0x422f13: mov      qword ptr [rdi + 0x10], 0
    0x422f1b: jmp      0x423192

; --- Block 0x422f20 [BODY] 10 insns, callees: (none)
    0x422f20: lea      rbp, [rdx - 2]
    0x422f24: lea      r12, [rdx*8 - 0x10]
    0x422f2c: mov      rax, rbp
    0x422f2f: shr      rax, 0x3d
    0x422f33: setne    al
    0x422f36: movabs   rcx, 0x7ffffffffffffff8
    0x422f40: cmp      r12, rcx
    0x422f43: seta     cl
    0x422f46: or       cl, al
    0x422f48: je       0x422f59

; --- Block 0x422f4a [BODY] 4 insns, callees: (none)
    0x422f4a: xor      r13d, r13d
    0x422f4d: mov      rdi, r13
    0x422f50: mov      rsi, r12
    0x422f53: call     qword ptr [rip + 0x624bf]

; --- Block 0x422f4d [LOOP_HEADER] 3 insns, callees: (none)
    0x422f4d: mov      rdi, r13
    0x422f50: mov      rsi, r12
    0x422f53: call     qword ptr [rip + 0x624bf]

; --- Block 0x422f59 [BODY] 5 insns, callees: (none)
    0x422f59: mov      r15, rsi
    0x422f5c: test     r12, r12
    0x422f5f: mov      qword ptr [rsp + 0x40], rdi
    0x422f64: mov      qword ptr [rsp + 8], rdx
    0x422f69: je       0x422f8f

; --- Block 0x422f6b [BODY] 1 insns, callees: (none)
    0x422f6b: call     qword ptr [rip + 0x62477]

; --- Block 0x422f71 [BODY] 4 insns, callees: (none)
    0x422f71: mov      r13d, 8
    0x422f77: mov      esi, 8
    0x422f7c: mov      rdi, r12
    0x422f7f: call     qword ptr [rip + 0x6246b]

; --- Block 0x422f85 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x422f85: test     rax, rax
    0x422f88: je       0x422f4d

; --- Block 0x422f8a [BODY] 2 insns, callees: (none)
    0x422f8a: mov      rcx, rbp
    0x422f8d: jmp      0x422f96

; --- Block 0x422f8f [BODY] 8 insns, callees: (none)
    0x422f8f: mov      eax, 8
    0x422f94: xor      ecx, ecx
    0x422f96: mov      qword ptr [rsp + 0x28], rcx
    0x422f9b: mov      qword ptr [rsp + 0x30], rax
    0x422fa0: mov      qword ptr [rsp + 0x38], 0
    0x422fa9: xor      r12d, r12d
    0x422fac: xor      ebx, ebx
    0x422fae: jmp      0x422fd3

; --- Block 0x422f96 [BODY] 6 insns, callees: (none)
    0x422f96: mov      qword ptr [rsp + 0x28], rcx
    0x422f9b: mov      qword ptr [rsp + 0x30], rax
    0x422fa0: mov      qword ptr [rsp + 0x38], 0
    0x422fa9: xor      r12d, r12d
    0x422fac: xor      ebx, ebx
    0x422fae: jmp      0x422fd3

; --- Block 0x422fb0 [LOOP_HEADER] 10 insns, callees: (none)
    0x422fb0: add      r13, r13
    0x422fb3: sub      r13, rbp
    0x422fb6: mov      rax, qword ptr [rsp + 0x30]
    0x422fbb: mov      qword ptr [rax + rbx*8], r13
    0x422fbf: inc      rbx
    0x422fc2: mov      qword ptr [rsp + 0x38], rbx
    0x422fc7: add      r12, 8
    0x422fcb: mov      rbp, r14
    0x422fce: cmp      r14, rbx
    0x422fd1: je       0x423002

; --- Block 0x422fd3 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x422fd3: cmp      qword ptr [rsp + 8], rbx
    0x422fd8: je       0x4231a4

; --- Block 0x422fde [ITERATOR_STATE] 6 insns, callees: (none)
    0x422fde: mov      r14, rbp
    0x422fe1: mov      rbp, qword ptr [r15 + rbx*8]
    0x422fe5: mov      r13, qword ptr [r15 + rbx*8 + 8]
    0x422fea: add      rbp, qword ptr [r15 + rbx*8 + 0x10]
    0x422fef: cmp      rbx, qword ptr [rsp + 0x28]
    0x422ff4: jne      0x422fb0

; --- Block 0x422ff6 [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x422ff6: lea      rdi, [rsp + 0x28]
    0x422ffb: call     0x43fe40

; --- Block 0x423000 [BODY] 1 insns, callees: (none)
    0x423000: jmp      0x422fb0

; --- Block 0x423002 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x423002: test     rbx, rbx
    0x423005: je       0x423134

; --- Block 0x42300b [BODY] 1 insns, callees: (none)
    0x42300b: call     qword ptr [rip + 0x623d7]

; --- Block 0x423011 [BODY] 3 insns, callees: (none)
    0x423011: mov      esi, 8
    0x423016: mov      rdi, r12
    0x423019: call     qword ptr [rip + 0x623d1]

; --- Block 0x42301f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42301f: test     rax, rax
    0x423022: je       0x4231e5

; --- Block 0x423028 [BODY] 7 insns, callees: (none)
    0x423028: mov      rcx, rax
    0x42302b: mov      r13, qword ptr [rsp + 0x38]
    0x423030: mov      qword ptr [rsp + 0x10], rbx
    0x423035: mov      qword ptr [rsp + 0x18], rax
    0x42303a: mov      qword ptr [rsp + 0x20], 0
    0x423043: test     r13, r13
    0x423046: je       0x42314f

; --- Block 0x42304c [BODY] 16 insns, callees: (none)
    0x42304c: mov      rdx, qword ptr [rsp + 0x30]
    0x423051: mov      rax, qword ptr [rdx]
    0x423054: xor      esi, esi
    0x423056: cmp      r13, 1
    0x42305a: setne    sil
    0x42305e: add      rax, rax
    0x423061: add      rax, qword ptr [rdx + rsi*8]
    0x423065: movabs   rbp, 0x5555555555555556
    0x42306f: imul     rbp
    0x423072: mov      rax, rdx
    0x423075: shr      rax, 0x3f
    0x423079: add      rax, rdx
    ... +4 more instructions

; --- Block 0x423092 [BODY] 5 insns, callees: (none)
    0x423092: mov      r14d, 2
    0x423098: mov      r15d, 1
    0x42309e: lea      rax, [rip + 0x5f6f3]
    0x4230a5: mov      qword ptr [rsp + 8], rax
    0x4230aa: jmp      0x4230d3

; --- Block 0x4230b0 [LOOP_HEADER] 10 insns, callees: (none)
    0x4230b0: mov      rax, r12
    0x4230b3: shr      rax, 0x3f
    0x4230b7: add      rax, r12
    0x4230ba: mov      rcx, qword ptr [rsp + 0x18]
    0x4230bf: mov      qword ptr [rcx + r15*8], rax
    0x4230c3: mov      qword ptr [rsp + 0x20], rbx
    0x4230c8: inc      r14
    0x4230cb: mov      r15, rbx
    0x4230ce: cmp      r13, rbx
    0x4230d1: je       0x42314f

; --- Block 0x4230d3 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4230d3: lea      rdi, [r15 - 1]
    0x4230d7: mov      rsi, qword ptr [rsp + 0x38]
    0x4230dc: cmp      rdi, rsi
    0x4230df: jae      0x4231c7

; --- Block 0x4230e5 [BODY] 6 insns, callees: (none)
    0x4230e5: lea      rbx, [r15 + 1]
    0x4230e9: mov      rcx, qword ptr [rsp + 0x30]
    0x4230ee: mov      rax, qword ptr [rcx + r15*8 - 8]
    0x4230f3: mov      rdx, r14
    0x4230f6: cmp      rbx, rsi
    0x4230f9: jb       0x423107

; --- Block 0x4230fb [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4230fb: mov      rdx, r15
    0x4230fe: cmp      r15, rsi
    0x423101: jae      0x4231d5

; --- Block 0x423107 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x423107: cmp      r15, rsi
    0x42310a: jae      0x4231bb

; --- Block 0x423110 [ITERATOR_STATE] 6 insns, callees: (none)
    0x423110: add      rax, qword ptr [rcx + rdx*8]
    0x423114: add      rax, qword ptr [rcx + r15*8]
    0x423118: imul     rbp
    0x42311b: mov      r12, rdx
    0x42311e: cmp      r15, qword ptr [rsp + 0x10]
    0x423123: jne      0x4230b0

; --- Block 0x423125 [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x423125: lea      rdi, [rsp + 0x10]
    0x42312a: call     0x43fe40

; --- Block 0x42312f [BODY] 1 insns, callees: (none)
    0x42312f: jmp      0x4230b0

; --- Block 0x423134 [BODY] 13 insns, callees: (none)
    0x423134: mov      qword ptr [rsp + 0x10], 0
    0x42313d: mov      qword ptr [rsp + 0x18], 8
    0x423146: mov      qword ptr [rsp + 0x20], 0
    0x42314f: mov      rax, qword ptr [rsp + 0x20]
    0x423154: mov      rdi, qword ptr [rsp + 0x40]
    0x423159: mov      qword ptr [rdi + 0x10], rax
    0x42315d: mov      rax, qword ptr [rsp + 0x10]
    0x423162: mov      qword ptr [rdi], rax
    0x423165: mov      rax, qword ptr [rsp + 0x18]
    0x42316a: mov      qword ptr [rdi + 8], rax
    0x42316e: mov      rsi, qword ptr [rsp + 0x28]
    0x423173: test     rsi, rsi
    ... +1 more instructions

; --- Block 0x42314f [BODY] 10 insns, callees: (none)
    0x42314f: mov      rax, qword ptr [rsp + 0x20]
    0x423154: mov      rdi, qword ptr [rsp + 0x40]
    0x423159: mov      qword ptr [rdi + 0x10], rax
    0x42315d: mov      rax, qword ptr [rsp + 0x10]
    0x423162: mov      qword ptr [rdi], rax
    0x423165: mov      rax, qword ptr [rsp + 0x18]
    0x42316a: mov      qword ptr [rdi + 8], rax
    0x42316e: mov      rsi, qword ptr [rsp + 0x28]
    0x423173: test     rsi, rsi
    0x423176: je       0x423192

; --- Block 0x423178 [BODY] 5 insns, callees: (none)
    0x423178: shl      rsi, 3
    0x42317c: mov      rbx, rdi
    0x42317f: mov      rdi, qword ptr [rsp + 0x30]
    0x423184: mov      edx, 8
    0x423189: call     qword ptr [rip + 0x62299]

; --- Block 0x42318f [BODY] 10 insns, callees: (none)
    0x42318f: mov      rdi, rbx
    0x423192: mov      rax, rdi
    0x423195: add      rsp, 0x48
    0x423199: pop      rbx
    0x42319a: pop      r12
    0x42319c: pop      r13
    0x42319e: pop      r14
    0x4231a0: pop      r15
    0x4231a2: pop      rbp
    0x4231a3: ret      

; --- Block 0x423192 [BODY] 9 insns, callees: (none)
    0x423192: mov      rax, rdi
    0x423195: add      rsp, 0x48
    0x423199: pop      rbx
    0x42319a: pop      r12
    0x42319c: pop      r13
    0x42319e: pop      r14
    0x4231a0: pop      r15
    0x4231a2: pop      rbp
    0x4231a3: ret      

; --- Block 0x4231a4 [BODY] 4 insns, callees: (none)
    0x4231a4: lea      rdx, [rip + 0x5f61d]
    0x4231ab: mov      rdi, qword ptr [rsp + 8]
    0x4231b0: mov      rsi, rdi
    0x4231b3: call     qword ptr [rip + 0x62277]

; --- Block 0x4231bb [BODY] 3 insns, callees: (none)
    0x4231bb: mov      rdi, r15
    0x4231be: lea      rax, [rip + 0x5f5eb]
    0x4231c5: jmp      0x4231ce

; --- Block 0x4231c7 [BODY] 3 insns, callees: (none)
    0x4231c7: lea      rax, [rip + 0x5f5b2]
    0x4231ce: mov      qword ptr [rsp + 8], rax
    0x4231d3: jmp      0x4231d8

; --- Block 0x4231ce [BODY] 2 insns, callees: (none)
    0x4231ce: mov      qword ptr [rsp + 8], rax
    0x4231d3: jmp      0x4231d8

; --- Block 0x4231d5 [BODY] 3 insns, callees: (none)
    0x4231d5: mov      rdi, r15
    0x4231d8: mov      rdx, qword ptr [rsp + 8]
    0x4231dd: call     qword ptr [rip + 0x6224d]

; --- Block 0x4231d8 [BODY] 2 insns, callees: (none)
    0x4231d8: mov      rdx, qword ptr [rsp + 8]
    0x4231dd: call     qword ptr [rip + 0x6224d]

; --- Block 0x4231e5 [BODY] 3 insns, callees: (none)
    0x4231e5: mov      edi, 8
    0x4231ea: mov      rsi, r12
    0x4231ed: call     qword ptr [rip + 0x62225]

```

**Hungarian matching result** (mean similarity: 0.770):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4464e1` | BODY | `0x423000` | BODY | 1.000 | GOOD |
| `0x446625` | BODY | `0x42312f` | BODY | 1.000 | GOOD |
| `0x4468a0` | BODY | `0x4231ce` | BODY | 1.000 | GOOD |
| `0x44651a` | BODY | `0x422ff6` | BODY | 0.993 | GOOD |
| `0x446637` | BODY | `0x422f8a` | BODY | 0.989 | GOOD |
| `0x4465a7` | LOOP_HEADER | `0x423125` | BODY | 0.987 | GOOD |
| `0x4464d4` | BODY | `0x4231d8` | BODY | 0.985 | GOOD |
| `0x4467e7` | LOOP_HEADER | `0x422fde` | ITERATOR_STATE | 0.968 | GOOD |
| `0x44678f` | BODY | `0x4231a4` | BODY | 0.964 | GOOD |
| `0x446727` | BODY | `0x422f59` | BODY | 0.962 | GOOD |
| `0x446527` | BODY | `0x422f4d` | LOOP_HEADER | 0.954 | GOOD |
| `0x446697` | BODY | `0x422f4a` | BODY | 0.949 | GOOD |
| `0x4466f9` | BODY | `0x4230e5` | BODY | 0.875 | GOOD |
| `0x4468a7` | ITERATOR_STATE | `0x423110` | ITERATOR_STATE | 0.873 | GOOD |
| `0x446a0e` | BOUNDS_CHECK | `0x4230fb` | BOUNDS_CHECK | 0.868 | GOOD |
| `0x446539` | BODY | `0x4231bb` | BODY | 0.864 | GOOD |
| `0x4465b4` | BODY | `0x4231c7` | BODY | 0.860 | GOOD |
| `0x446641` | BODY | `0x4231d5` | BODY | 0.858 | GOOD |
| `0x446b6d` | BOUNDS_CHECK | `0x4230d3` | BOUNDS_CHECK | 0.858 | GOOD |
| `0x4465c6` | BODY | `0x42314f` | BODY | 0.847 | GOOD |
| `0x446b3d` | ITERATOR_STATE | `0x423028` | BODY | 0.823 | GOOD |
| `0x44683a` | BODY | `0x422f04` | BODY | 0.731 | GOOD |
| `0x446937` | BODY | `0x422f96` | BODY | 0.724 | GOOD |
| `0x446470` | BODY | `0x422ef0` | BODY | 0.693 | PARTIAL |
| `0x4469c0` | BODY | `0x42304c` | BODY | 0.691 | PARTIAL |
| `0x4464b5` | ITERATOR_STATE | `0x423092` | BODY | 0.687 | PARTIAL |
| `0x446875` | BOUNDS_CHECK | `0x422f85` | BOUNDS_CHECK | 0.684 | PARTIAL |
| `0x4464d2` | BODY | `0x422f6b` | BODY | 0.662 | PARTIAL |
| `0x446518` | BODY | `0x42300b` | BODY | 0.662 | PARTIAL |
| `0x446665` | BODY | `0x423002` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x4467ab` | BODY | `0x42301f` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x44681e` | BODY | `0x422fd3` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x446859` | BODY | `0x423107` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x4464e6` | BODY | `0x423011` | BODY | 0.635 | PARTIAL |
| `0x446bd9` | BODY | `0x422f71` | BODY | 0.634 | PARTIAL |
| `0x446825` | BODY | `0x4231e5` | BODY | 0.633 | PARTIAL |
| `0x4467d4` | BODY | `0x4230b0` | LOOP_HEADER | 0.627 | PARTIAL |
| `0x446a3a` | BODY | `0x423134` | BODY | 0.609 | PARTIAL |
| `0x4465f4` | BODY | `0x422fb0` | LOOP_HEADER | 0.605 | PARTIAL |
| `0x446aea` | BODY | `0x423178` | BODY | 0.591 | PARTIAL |
| `0x446a89` | BODY | `0x422f8f` | BODY | 0.536 | PARTIAL |
| `0x446747` | DROP_GLUE | `0x422f20` | BODY | 0.481 | PARTIAL |
| `0x4468c2` | BODY | `0x423192` | BODY | 0.474 | PARTIAL |
| `0x44677f` | EPILOGUE | `0x42318f` | BODY | 0.450 | PARTIAL |
| `0x4464fb` | ITERATOR_STATE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44654b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446587` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44662a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446656` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446658` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4466a8` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4466ba` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4466da` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4466e7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446745` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4467b5` | ITERATOR_STATE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4467d2` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446800` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446802` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44684c` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446860` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446884` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4468c0` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4468d2` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4468fb` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446902` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44691b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446922` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446949` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446960` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446977` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446979` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44698e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446990` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4469a5` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4469ec` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4469ee` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446a03` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446a23` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446a25` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446a62` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446a64` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446aad` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446aaf` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446ac4` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446ae8` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b0f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b26` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b28` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b56` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b58` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b7f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b81` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446b96` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446bb5` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446bb7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446bf2` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446bf4` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446c09` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `bc_07` — O0: 19 blocks, O2: 11 blocks

**O0 blocks** (19 total):

```asm
; --- Block 0x401b2a [BODY] 10 insns, callees: (none)
    0x401b2a: push     rbp
    0x401b2b: mov      rbp, rsp
    0x401b2e: sub      rsp, 0x60
    0x401b32: mov      qword ptr [rbp - 0x48], rdi
    0x401b36: mov      qword ptr [rbp - 0x50], rsi
    0x401b3a: mov      qword ptr [rbp - 0x58], rdx
    0x401b3e: mov      rax, qword ptr [rbp - 0x58]
    0x401b42: mov      qword ptr [rax], 0
    0x401b49: cmp      qword ptr [rbp - 0x50], 2
    0x401b4e: ja       0x401b5a

; --- Block 0x401b50 [BODY] 2 insns, callees: (none)
    0x401b50: mov      eax, 0
    0x401b55: jmp      0x401d22

; --- Block 0x401b5a [BODY] 7 insns, callees: sub_4010f0
    0x401b5a: mov      rax, qword ptr [rbp - 0x50]
    0x401b5e: sub      rax, 2
    0x401b62: mov      qword ptr [rbp - 0x18], rax
    0x401b66: mov      rax, qword ptr [rbp - 0x18]
    0x401b6a: shl      rax, 3
    0x401b6e: mov      rdi, rax
    0x401b71: call     0x4010f0

; --- Block 0x401b76 [BODY] 3 insns, callees: (none)
    0x401b76: mov      qword ptr [rbp - 0x20], rax
    0x401b7a: mov      qword ptr [rbp - 8], 1
    0x401b82: jmp      0x401bf2

; --- Block 0x401b84 [LOOP_HEADER] 32 insns, callees: (none)
    0x401b84: mov      rax, qword ptr [rbp - 8]
    0x401b88: lea      rdx, [rax*8]
    0x401b90: mov      rax, qword ptr [rbp - 0x48]
    0x401b94: add      rax, rdx
    0x401b97: mov      rax, qword ptr [rax]
    0x401b9a: lea      rdx, [rax + rax]
    0x401b9e: mov      rax, qword ptr [rbp - 8]
    0x401ba2: shl      rax, 3
    0x401ba6: lea      rcx, [rax - 8]
    0x401baa: mov      rax, qword ptr [rbp - 0x48]
    0x401bae: add      rax, rcx
    0x401bb1: mov      rax, qword ptr [rax]
    ... +20 more instructions

; --- Block 0x401bf2 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x401bf2: mov      rax, qword ptr [rbp - 0x50]
    0x401bf6: sub      rax, 1
    0x401bfa: cmp      qword ptr [rbp - 8], rax
    0x401bfe: jb       0x401b84

; --- Block 0x401c00 [BODY] 4 insns, callees: sub_4010f0
    0x401c00: mov      rax, qword ptr [rbp - 0x18]
    0x401c04: shl      rax, 3
    0x401c08: mov      rdi, rax
    0x401c0b: call     0x4010f0

; --- Block 0x401c10 [BODY] 3 insns, callees: (none)
    0x401c10: mov      qword ptr [rbp - 0x28], rax
    0x401c14: mov      qword ptr [rbp - 0x10], 0
    0x401c1c: jmp      0x401cf9

; --- Block 0x401c21 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x401c21: cmp      qword ptr [rbp - 0x10], 0
    0x401c26: je       0x401c40

; --- Block 0x401c28 [BODY] 7 insns, callees: (none)
    0x401c28: mov      rax, qword ptr [rbp - 0x10]
    0x401c2c: shl      rax, 3
    0x401c30: lea      rdx, [rax - 8]
    0x401c34: mov      rax, qword ptr [rbp - 0x20]
    0x401c38: add      rax, rdx
    0x401c3b: mov      rax, qword ptr [rax]
    0x401c3e: jmp      0x401c56

; --- Block 0x401c40 [BODY] 10 insns, callees: (none)
    0x401c40: mov      rax, qword ptr [rbp - 0x10]
    0x401c44: lea      rdx, [rax*8]
    0x401c4c: mov      rax, qword ptr [rbp - 0x20]
    0x401c50: add      rax, rdx
    0x401c53: mov      rax, qword ptr [rax]
    0x401c56: mov      qword ptr [rbp - 0x30], rax
    0x401c5a: mov      rax, qword ptr [rbp - 0x10]
    0x401c5e: add      rax, 1
    0x401c62: cmp      qword ptr [rbp - 0x18], rax
    0x401c66: jbe      0x401c84

; --- Block 0x401c56 [ITERATOR_STATE] 5 insns, callees: (none)
    0x401c56: mov      qword ptr [rbp - 0x30], rax
    0x401c5a: mov      rax, qword ptr [rbp - 0x10]
    0x401c5e: add      rax, 1
    0x401c62: cmp      qword ptr [rbp - 0x18], rax
    0x401c66: jbe      0x401c84

; --- Block 0x401c68 [BODY] 7 insns, callees: (none)
    0x401c68: mov      rax, qword ptr [rbp - 0x10]
    0x401c6c: add      rax, 1
    0x401c70: lea      rdx, [rax*8]
    0x401c78: mov      rax, qword ptr [rbp - 0x20]
    0x401c7c: add      rax, rdx
    0x401c7f: mov      rax, qword ptr [rax]
    0x401c82: jmp      0x401c9a

; --- Block 0x401c84 [BODY] 30 insns, callees: (none)
    0x401c84: mov      rax, qword ptr [rbp - 0x10]
    0x401c88: lea      rdx, [rax*8]
    0x401c90: mov      rax, qword ptr [rbp - 0x20]
    0x401c94: add      rax, rdx
    0x401c97: mov      rax, qword ptr [rax]
    0x401c9a: mov      qword ptr [rbp - 0x38], rax
    0x401c9e: mov      rax, qword ptr [rbp - 0x10]
    0x401ca2: lea      rdx, [rax*8]
    0x401caa: mov      rax, qword ptr [rbp - 0x20]
    0x401cae: add      rax, rdx
    0x401cb1: mov      rdx, qword ptr [rax]
    0x401cb4: mov      rax, qword ptr [rbp - 0x30]
    ... +18 more instructions

; --- Block 0x401c9a [BODY] 25 insns, callees: (none)
    0x401c9a: mov      qword ptr [rbp - 0x38], rax
    0x401c9e: mov      rax, qword ptr [rbp - 0x10]
    0x401ca2: lea      rdx, [rax*8]
    0x401caa: mov      rax, qword ptr [rbp - 0x20]
    0x401cae: add      rax, rdx
    0x401cb1: mov      rdx, qword ptr [rax]
    0x401cb4: mov      rax, qword ptr [rbp - 0x30]
    0x401cb8: add      rdx, rax
    0x401cbb: mov      rax, qword ptr [rbp - 0x38]
    0x401cbf: lea      rcx, [rdx + rax]
    0x401cc3: mov      rax, qword ptr [rbp - 0x10]
    0x401cc7: lea      rdx, [rax*8]
    ... +13 more instructions

; --- Block 0x401cf9 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x401cf9: mov      rax, qword ptr [rbp - 0x10]
    0x401cfd: cmp      rax, qword ptr [rbp - 0x18]
    0x401d01: jb       0x401c21

; --- Block 0x401d07 [BODY] 3 insns, callees: sub_401030
    0x401d07: mov      rax, qword ptr [rbp - 0x20]
    0x401d0b: mov      rdi, rax
    0x401d0e: call     0x401030

; --- Block 0x401d13 [BODY] 6 insns, callees: (none)
    0x401d13: mov      rax, qword ptr [rbp - 0x58]
    0x401d17: mov      rdx, qword ptr [rbp - 0x18]
    0x401d1b: mov      qword ptr [rax], rdx
    0x401d1e: mov      rax, qword ptr [rbp - 0x28]
    0x401d22: leave    
    0x401d23: ret      

; --- Block 0x401d22 [BODY] 2 insns, callees: (none)
    0x401d22: leave    
    0x401d23: ret      

```

**O2 blocks** (11 total):

```asm
; --- Block 0x403c40 [BODY] 11 insns, callees: (none)
    0x403c40: push     r15
    0x403c42: xor      r15d, r15d
    0x403c45: push     r14
    0x403c47: push     r13
    0x403c49: push     r12
    0x403c4b: push     rbp
    0x403c4c: push     rbx
    0x403c4d: sub      rsp, 0x18
    0x403c51: mov      qword ptr [rdx], 0
    0x403c58: cmp      rsi, 2
    0x403c5c: jbe      0x403d34

; --- Block 0x403c62 [BODY] 7 insns, callees: sub_401100
    0x403c62: lea      r13, [rsi - 2]
    0x403c66: mov      rbp, rdi
    0x403c69: mov      qword ptr [rsp + 8], rsi
    0x403c6e: mov      rbx, rdx
    0x403c71: lea      r14, [r13*8]
    0x403c79: mov      rdi, r14
    0x403c7c: call     0x401100

; --- Block 0x403c81 [BODY] 14 insns, callees: (none)
    0x403c81: mov      rsi, qword ptr [rsp + 8]
    0x403c86: mov      rcx, qword ptr [rbp + 8]
    0x403c8a: mov      r12, rax
    0x403c8d: mov      eax, 1
    0x403c92: sub      rsi, 1
    0x403c96: nop      word ptr cs:[rax + rax]
    0x403ca0: lea      rdx, [rcx + rcx]
    0x403ca4: sub      rdx, qword ptr [rbp + rax*8 - 8]
    0x403ca9: add      rax, 1
    0x403cad: mov      rcx, qword ptr [rbp + rax*8]
    0x403cb2: sub      rdx, rcx
    0x403cb5: mov      qword ptr [r12 + rax*8 - 0x10], rdx
    ... +2 more instructions

; --- Block 0x403ca0 [BODY] 8 insns, callees: (none)
    0x403ca0: lea      rdx, [rcx + rcx]
    0x403ca4: sub      rdx, qword ptr [rbp + rax*8 - 8]
    0x403ca9: add      rax, 1
    0x403cad: mov      rcx, qword ptr [rbp + rax*8]
    0x403cb2: sub      rdx, rcx
    0x403cb5: mov      qword ptr [r12 + rax*8 - 0x10], rdx
    0x403cba: cmp      rax, rsi
    0x403cbd: jne      0x403ca0

; --- Block 0x403cbf [BODY] 3 insns, callees: sub_401100
    0x403cbf: mov      rdi, r14
    0x403cc2: xor      ebp, ebp
    0x403cc4: call     0x401100

; --- Block 0x403cc9 [BODY] 5 insns, callees: (none)
    0x403cc9: mov      rcx, qword ptr [r12]
    0x403ccd: movabs   rdi, 0x5555555555555556
    0x403cd7: mov      r15, rax
    0x403cda: mov      rsi, rcx
    0x403cdd: jmp      0x403cfe

; --- Block 0x403ce0 [LOOP_HEADER] 12 insns, callees: (none)
    0x403ce0: mov      rsi, qword ptr [r12 + rbp*8]
    0x403ce4: add      rcx, rsi
    0x403ce7: mov      rax, rcx
    0x403cea: sar      rcx, 0x3f
    0x403cee: imul     rdi
    0x403cf1: sub      rdx, rcx
    0x403cf4: mov      rcx, qword ptr [r12 + rbp*8 - 8]
    0x403cf9: mov      qword ptr [r15 + rbp*8 - 8], rdx
    0x403cfe: add      rbp, 1
    0x403d02: add      rcx, rsi
    0x403d05: cmp      rbp, r13
    0x403d08: jne      0x403ce0

; --- Block 0x403cfe [BOUNDS_CHECK] 4 insns, callees: (none)
    0x403cfe: add      rbp, 1
    0x403d02: add      rcx, rsi
    0x403d05: cmp      rbp, r13
    0x403d08: jne      0x403ce0

; --- Block 0x403d0a [BODY] 9 insns, callees: sub_401030
    0x403d0a: movabs   rdx, 0x5555555555555556
    0x403d14: add      rsi, rcx
    0x403d17: mov      rdi, r12
    0x403d1a: mov      rax, rsi
    0x403d1d: sar      rsi, 0x3f
    0x403d21: imul     rdx
    0x403d24: sub      rdx, rsi
    0x403d27: mov      qword ptr [r15 + r14 - 8], rdx
    0x403d2c: call     0x401030

; --- Block 0x403d31 [BODY] 10 insns, callees: (none)
    0x403d31: mov      qword ptr [rbx], rbp
    0x403d34: add      rsp, 0x18
    0x403d38: mov      rax, r15
    0x403d3b: pop      rbx
    0x403d3c: pop      rbp
    0x403d3d: pop      r12
    0x403d3f: pop      r13
    0x403d41: pop      r14
    0x403d43: pop      r15
    0x403d45: ret      

; --- Block 0x403d34 [BODY] 9 insns, callees: (none)
    0x403d34: add      rsp, 0x18
    0x403d38: mov      rax, r15
    0x403d3b: pop      rbx
    0x403d3c: pop      rbp
    0x403d3d: pop      r12
    0x403d3f: pop      r13
    0x403d41: pop      r14
    0x403d43: pop      r15
    0x403d45: ret      

```

**Hungarian matching result** (mean similarity: 0.630):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x401c56` | ITERATOR_STATE | `0x403cfe` | BOUNDS_CHECK | 0.825 | GOOD |
| `0x401c40` | BODY | `0x403c81` | BODY | 0.774 | GOOD |
| `0x401b2a` | BODY | `0x403c40` | BODY | 0.736 | GOOD |
| `0x401c68` | BODY | `0x403ca0` | BODY | 0.700 | GOOD |
| `0x401c9a` | BODY | `0x403ce0` | LOOP_HEADER | 0.674 | PARTIAL |
| `0x401d07` | BODY | `0x403cbf` | BODY | 0.627 | PARTIAL |
| `0x401b76` | BODY | `0x403cc9` | BODY | 0.601 | PARTIAL |
| `0x401c84` | BODY | `0x403d0a` | BODY | 0.563 | PARTIAL |
| `0x401b5a` | BODY | `0x403c62` | BODY | 0.531 | PARTIAL |
| `0x401c28` | BODY | `0x403d34` | BODY | 0.458 | PARTIAL |
| `0x401d13` | BODY | `0x403d31` | BODY | 0.446 | PARTIAL |
| `0x401b50` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401b84` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401bf2` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401c00` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401c10` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401c21` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401cf9` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x401d22` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `bc_06`

### Rust `bc_06` — O0: 40 blocks, O2: 18 blocks

**O0 blocks** (40 total):

```asm
; --- Block 0x446180 [BODY] 11 insns, callees: (none)
    0x446180: sub      rsp, 0xc8
    0x446187: mov      qword ptr [rsp + 0x50], rdi
    0x44618c: mov      qword ptr [rsp + 0x58], rsi
    0x446191: mov      qword ptr [rsp + 0x98], rdi
    0x446199: mov      qword ptr [rsp + 0xa0], rsi
    0x4461a1: mov      qword ptr [rsp + 0xa8], rdx
    0x4461a9: mov      qword ptr [rsp + 0xb0], rsi
    0x4461b1: mov      qword ptr [rsp + 0x60], 0
    0x4461ba: mov      qword ptr [rsp + 0x68], rdx
    0x4461bf: cmp      qword ptr [rsp + 0x68], 0
    0x4461c5: ja       0x4461d4

; --- Block 0x4461bf [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4461bf: cmp      qword ptr [rsp + 0x68], 0
    0x4461c5: ja       0x4461d4

; --- Block 0x4461c7 [EPILOGUE] 3 insns, callees: (none)
    0x4461c7: mov      rax, qword ptr [rsp + 0x60]
    0x4461cc: add      rsp, 0xc8
    0x4461d3: ret      

; --- Block 0x4461d4 [BODY] 3 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x4461d4: mov      rsi, qword ptr [rsp + 0x58]
    0x4461d9: mov      rdi, qword ptr [rsp + 0x68]
    0x4461de: call     0x49b480

; --- Block 0x4461e3 [BODY] 4 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4461e3: mov      qword ptr [rsp + 0x70], rax
    0x4461e8: mov      qword ptr [rsp + 0x78], rdx
    0x4461ed: lea      rdi, [rsp + 0x70]
    0x4461f2: call     0x49ad10

; --- Block 0x4461ed [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4461ed: lea      rdi, [rsp + 0x70]
    0x4461f2: call     0x49ad10

; --- Block 0x4461f7 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4461f7: mov      qword ptr [rsp + 0x80], rax
    0x4461ff: mov      qword ptr [rsp + 0x88], rdx
    0x446207: test     qword ptr [rsp + 0x80], 1
    0x446213: je       0x446236

; --- Block 0x446215 [BODY] 6 insns, callees: (none)
    0x446215: mov      rcx, qword ptr [rsp + 0x58]
    0x44621a: mov      rax, qword ptr [rsp + 0x88]
    0x446222: mov      qword ptr [rsp + 0x48], rax
    0x446227: mov      qword ptr [rsp + 0xb8], rax
    0x44622f: cmp      rax, rcx
    0x446232: jb       0x446248

; --- Block 0x446234 [BODY] 1 insns, callees: (none)
    0x446234: jmp      0x44626d

; --- Block 0x446236 [BODY] 4 insns, callees: (none)
    0x446236: mov      rax, qword ptr [rsp + 0x68]
    0x44623b: shr      rax, 1
    0x44623e: mov      qword ptr [rsp + 0x68], rax
    0x446243: jmp      0x4461bf

; --- Block 0x446248 [BODY] 7 insns, callees: (none)
    0x446248: mov      rax, qword ptr [rsp + 0x48]
    0x44624d: mov      rcx, qword ptr [rsp + 0x50]
    0x446252: mov      rcx, qword ptr [rcx + rax*8]
    0x446256: mov      qword ptr [rsp + 0x40], rcx
    0x44625b: mov      qword ptr [rsp + 0xc0], rcx
    0x446263: mov      qword ptr [rsp + 0x90], rax
    0x44626b: jmp      0x446284

; --- Block 0x44626d [BODY] 4 insns, callees: (none)
    0x44626d: mov      rsi, qword ptr [rsp + 0x58]
    0x446272: mov      rdi, qword ptr [rsp + 0x48]
    0x446277: lea      rdx, [rip + 0xa8dd2]
    0x44627e: call     qword ptr [rip + 0xaee14]

; --- Block 0x446284 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x446284: mov      rax, qword ptr [rsp + 0x90]
    0x44628c: cmp      rax, qword ptr [rsp + 0x68]
    0x446291: jae      0x4462b3

; --- Block 0x446293 [LOOP_HEADER] 5 insns, callees: (none)
    0x446293: mov      rcx, qword ptr [rsp + 0x58]
    0x446298: mov      rax, qword ptr [rsp + 0x90]
    0x4462a0: mov      qword ptr [rsp + 0x38], rax
    0x4462a5: cmp      rax, rcx
    0x4462a8: jb       0x44633b

; --- Block 0x4462ae [BODY] 1 insns, callees: (none)
    0x4462ae: jmp      0x446353

; --- Block 0x4462b3 [BODY] 7 insns, callees: (none)
    0x4462b3: mov      rax, qword ptr [rsp + 0x90]
    0x4462bb: mov      rcx, qword ptr [rsp + 0x68]
    0x4462c0: mov      rdx, rax
    0x4462c3: sub      rdx, rcx
    0x4462c6: mov      qword ptr [rsp + 0x30], rdx
    0x4462cb: cmp      rax, rcx
    0x4462ce: jb       0x4462e1

; --- Block 0x4462d0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4462d0: mov      rax, qword ptr [rsp + 0x30]
    0x4462d5: mov      rcx, qword ptr [rsp + 0x58]
    0x4462da: cmp      rax, rcx
    0x4462dd: jb       0x4462ee

; --- Block 0x4462df [BODY] 1 insns, callees: (none)
    0x4462df: jmp      0x446305

; --- Block 0x4462e1 [BODY] 2 insns, callees: (none)
    0x4462e1: lea      rdi, [rip + 0xa8d80]
    0x4462e8: call     qword ptr [rip + 0xaee62]

; --- Block 0x4462ee [BODY] 5 insns, callees: (none)
    0x4462ee: mov      rax, qword ptr [rsp + 0x50]
    0x4462f3: mov      rcx, qword ptr [rsp + 0x30]
    0x4462f8: mov      rdx, qword ptr [rsp + 0x40]
    0x4462fd: cmp      qword ptr [rax + rcx*8], rdx
    0x446301: ja       0x44631c

; --- Block 0x446303 [BODY] 1 insns, callees: (none)
    0x446303: jmp      0x446293

; --- Block 0x446305 [BODY] 4 insns, callees: (none)
    0x446305: mov      rsi, qword ptr [rsp + 0x58]
    0x44630a: mov      rdi, qword ptr [rsp + 0x30]
    0x44630f: lea      rdx, [rip + 0xa8d6a]
    0x446316: call     qword ptr [rip + 0xaed7c]

; --- Block 0x44631c [BODY] 7 insns, callees: (none)
    0x44631c: mov      rax, qword ptr [rsp + 0x90]
    0x446324: mov      rcx, qword ptr [rsp + 0x68]
    0x446329: mov      rdx, rax
    0x44632c: sub      rdx, rcx
    0x44632f: mov      qword ptr [rsp + 0x28], rdx
    0x446334: cmp      rax, rcx
    0x446337: jb       0x44637b

; --- Block 0x446339 [BODY] 1 insns, callees: (none)
    0x446339: jmp      0x44636a

; --- Block 0x44633b [BODY] 5 insns, callees: (none)
    0x44633b: mov      rax, qword ptr [rsp + 0x50]
    0x446340: mov      rcx, qword ptr [rsp + 0x38]
    0x446345: mov      rdx, qword ptr [rsp + 0x40]
    0x44634a: mov      qword ptr [rax + rcx*8], rdx
    0x44634e: jmp      0x4461ed

; --- Block 0x446353 [BODY] 4 insns, callees: (none)
    0x446353: mov      rsi, qword ptr [rsp + 0x58]
    0x446358: mov      rdi, qword ptr [rsp + 0x38]
    0x44635d: lea      rdx, [rip + 0xa8d34]
    0x446364: call     qword ptr [rip + 0xaed2e]

; --- Block 0x44636a [BOUNDS_CHECK] 4 insns, callees: (none)
    0x44636a: mov      rax, qword ptr [rsp + 0x28]
    0x44636f: mov      rcx, qword ptr [rsp + 0x58]
    0x446374: cmp      rax, rcx
    0x446377: jb       0x446388

; --- Block 0x446379 [BODY] 1 insns, callees: (none)
    0x446379: jmp      0x4463b4

; --- Block 0x44637b [BODY] 2 insns, callees: (none)
    0x44637b: lea      rdi, [rip + 0xa8d2e]
    0x446382: call     qword ptr [rip + 0xaedc8]

; --- Block 0x446388 [BODY] 9 insns, callees: (none)
    0x446388: mov      rcx, qword ptr [rsp + 0x58]
    0x44638d: mov      rax, qword ptr [rsp + 0x50]
    0x446392: mov      rdx, qword ptr [rsp + 0x28]
    0x446397: mov      rax, qword ptr [rax + rdx*8]
    0x44639b: mov      qword ptr [rsp + 0x18], rax
    0x4463a0: mov      rax, qword ptr [rsp + 0x90]
    0x4463a8: mov      qword ptr [rsp + 0x20], rax
    0x4463ad: cmp      rax, rcx
    0x4463b0: jb       0x4463cb

; --- Block 0x4463b2 [BODY] 1 insns, callees: (none)
    0x4463b2: jmp      0x4463fd

; --- Block 0x4463b4 [BODY] 4 insns, callees: (none)
    0x4463b4: mov      rsi, qword ptr [rsp + 0x58]
    0x4463b9: mov      rdi, qword ptr [rsp + 0x28]
    0x4463be: lea      rdx, [rip + 0xa8d03]
    0x4463c5: call     qword ptr [rip + 0xaeccd]

; --- Block 0x4463cb [BODY] 11 insns, callees: (none)
    0x4463cb: mov      rax, qword ptr [rsp + 0x50]
    0x4463d0: mov      rcx, qword ptr [rsp + 0x20]
    0x4463d5: mov      rdx, qword ptr [rsp + 0x18]
    0x4463da: mov      qword ptr [rax + rcx*8], rdx
    0x4463de: mov      rcx, qword ptr [rsp + 0x68]
    0x4463e3: mov      rax, qword ptr [rsp + 0x90]
    0x4463eb: mov      rdx, rax
    0x4463ee: sub      rdx, rcx
    0x4463f1: mov      qword ptr [rsp + 0x10], rdx
    0x4463f6: cmp      rax, rcx
    0x4463f9: jb       0x446439

; --- Block 0x4463fb [BODY] 1 insns, callees: (none)
    0x4463fb: jmp      0x446414

; --- Block 0x4463fd [BODY] 4 insns, callees: (none)
    0x4463fd: mov      rsi, qword ptr [rsp + 0x58]
    0x446402: mov      rdi, qword ptr [rsp + 0x20]
    0x446407: lea      rdx, [rip + 0xa8cd2]
    0x44640e: call     qword ptr [rip + 0xaec84]

; --- Block 0x446414 [BODY] 8 insns, callees: (none)
    0x446414: mov      rax, qword ptr [rsp + 0x10]
    0x446419: mov      qword ptr [rsp + 0x90], rax
    0x446421: mov      rcx, qword ptr [rsp + 0x60]
    0x446426: mov      rax, rcx
    0x446429: add      rax, 1
    0x44642d: mov      qword ptr [rsp + 8], rax
    0x446432: cmp      rax, rcx
    0x446435: jb       0x446455

; --- Block 0x446437 [BODY] 1 insns, callees: (none)
    0x446437: jmp      0x446446

; --- Block 0x446439 [BODY] 2 insns, callees: (none)
    0x446439: lea      rdi, [rip + 0xa8cb8]
    0x446440: call     qword ptr [rip + 0xaed0a]

; --- Block 0x446446 [BODY] 3 insns, callees: (none)
    0x446446: mov      rax, qword ptr [rsp + 8]
    0x44644b: mov      qword ptr [rsp + 0x60], rax
    0x446450: jmp      0x446284

; --- Block 0x446455 [BODY] 2 insns, callees: (none)
    0x446455: lea      rdi, [rip + 0xa8cb4]
    0x44645c: call     qword ptr [rip + 0xaecce]

```

**O2 blocks** (18 total):

```asm
; --- Block 0x422e10 [BODY] 6 insns, callees: (none)
    0x422e10: push     r14
    0x422e12: push     rbx
    0x422e13: push     rax
    0x422e14: xor      eax, eax
    0x422e16: test     rdx, rdx
    0x422e19: jne      0x422e3f

; --- Block 0x422e1b [EPILOGUE] 4 insns, callees: (none)
    0x422e1b: add      rsp, 8
    0x422e1f: pop      rbx
    0x422e20: pop      r14
    0x422e22: ret      

; --- Block 0x422e30 [LOOP_HEADER] 5 insns, callees: (none)
    0x422e30: mov      rcx, rdx
    0x422e33: shr      rcx, 1
    0x422e36: cmp      rdx, 2
    0x422e3a: mov      rdx, rcx
    0x422e3d: jb       0x422e1b

; --- Block 0x422e3f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x422e3f: cmp      rdx, rsi
    0x422e42: jae      0x422e30

; --- Block 0x422e44 [BODY] 7 insns, callees: (none)
    0x422e44: lea      r9, [rdi + rdx*8]
    0x422e48: xor      r10d, r10d
    0x422e4b: mov      r11, rdx
    0x422e4e: nop      
    0x422e50: mov      rbx, qword ptr [rdi + r11*8]
    0x422e54: cmp      r11, rdx
    0x422e57: jae      0x422e60

; --- Block 0x422e50 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x422e50: mov      rbx, qword ptr [rdi + r11*8]
    0x422e54: cmp      r11, rdx
    0x422e57: jae      0x422e60

; --- Block 0x422e59 [BODY] 2 insns, callees: (none)
    0x422e59: mov      r8, r11
    0x422e5c: jmp      0x422e99

; --- Block 0x422e60 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x422e60: mov      rcx, r10
    0x422e63: nop      word ptr cs:[rax + rax]
    0x422e70: cmp      rcx, rsi
    0x422e73: jae      0x422eaf

; --- Block 0x422e70 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x422e70: cmp      rcx, rsi
    0x422e73: jae      0x422eaf

; --- Block 0x422e75 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x422e75: lea      r8, [rdx + rcx]
    0x422e79: mov      r14, qword ptr [rdi + rcx*8]
    0x422e7d: cmp      r14, rbx
    0x422e80: jbe      0x422e99

; --- Block 0x422e82 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x422e82: cmp      r8, rsi
    0x422e85: jae      0x422ebf

; --- Block 0x422e87 [BODY] 6 insns, callees: (none)
    0x422e87: mov      qword ptr [r9 + rcx*8], r14
    0x422e8b: inc      rax
    0x422e8e: sub      rcx, rdx
    0x422e91: mov      r8, rdx
    0x422e94: add      r8, rcx
    0x422e97: jae      0x422e70

; --- Block 0x422e99 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x422e99: cmp      r8, rsi
    0x422e9c: jae      0x422ed5

; --- Block 0x422e9e [ITERATOR_STATE] 5 insns, callees: (none)
    0x422e9e: inc      r11
    0x422ea1: mov      qword ptr [rdi + r8*8], rbx
    0x422ea5: inc      r10
    0x422ea8: cmp      r11, rsi
    0x422eab: jne      0x422e50

; --- Block 0x422ead [BODY] 1 insns, callees: (none)
    0x422ead: jmp      0x422e30

; --- Block 0x422eaf [BODY] 3 insns, callees: (none)
    0x422eaf: lea      rdx, [rip + 0x5f882]
    0x422eb6: mov      rdi, rcx
    0x422eb9: call     qword ptr [rip + 0x62571]

; --- Block 0x422ebf [BODY] 5 insns, callees: (none)
    0x422ebf: add      rdx, rcx
    0x422ec2: lea      rax, [rip + 0x5f89f]
    0x422ec9: mov      rdi, rdx
    0x422ecc: mov      rdx, rax
    0x422ecf: call     qword ptr [rip + 0x6255b]

; --- Block 0x422ed5 [BODY] 3 insns, callees: (none)
    0x422ed5: lea      rdx, [rip + 0x5f874]
    0x422edc: mov      rdi, r8
    0x422edf: call     qword ptr [rip + 0x6254b]

```

**Hungarian matching result** (mean similarity: 0.802):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4461bf` | BOUNDS_CHECK | `0x422e3f` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x446234` | BODY | `0x422ead` | BODY | 1.000 | GOOD |
| `0x446284` | BOUNDS_CHECK | `0x422e50` | BOUNDS_CHECK | 0.964 | GOOD |
| `0x4462d0` | BOUNDS_CHECK | `0x422e60` | BOUNDS_CHECK | 0.947 | GOOD |
| `0x44626d` | BODY | `0x422ed5` | BODY | 0.886 | GOOD |
| `0x446353` | BODY | `0x422eaf` | BODY | 0.877 | GOOD |
| `0x446293` | LOOP_HEADER | `0x422e9e` | ITERATOR_STATE | 0.857 | GOOD |
| `0x44636a` | BOUNDS_CHECK | `0x422e75` | BOUNDS_CHECK | 0.855 | GOOD |
| `0x446446` | BODY | `0x422e59` | BODY | 0.844 | GOOD |
| `0x4461e3` | BODY | `0x422ebf` | BODY | 0.797 | GOOD |
| `0x446215` | BODY | `0x422e10` | BODY | 0.775 | GOOD |
| `0x44631c` | BODY | `0x422e87` | BODY | 0.740 | GOOD |
| `0x4462b3` | BODY | `0x422e44` | BODY | 0.739 | GOOD |
| `0x4461f7` | BOUNDS_CHECK | `0x422e99` | BOUNDS_CHECK | 0.716 | GOOD |
| `0x44637b` | BODY | `0x422e82` | BOUNDS_CHECK | 0.645 | PARTIAL |
| `0x446455` | BODY | `0x422e70` | BOUNDS_CHECK | 0.645 | PARTIAL |
| `0x4462ee` | BODY | `0x422e30` | LOOP_HEADER | 0.637 | PARTIAL |
| `0x4461c7` | EPILOGUE | `0x422e1b` | EPILOGUE | 0.520 | PARTIAL |
| `0x446180` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4461d4` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4461ed` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446236` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446248` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4462ae` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4462df` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4462e1` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446303` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446305` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446339` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44633b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446379` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446388` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4463b2` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4463b4` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4463cb` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4463fb` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4463fd` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446414` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446437` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x446439` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `bc_06` — O0: 11 blocks, O2: 14 blocks

**O0 blocks** (11 total):

```asm
; --- Block 0x401a24 [BODY] 9 insns, callees: (none)
    0x401a24: push     rbp
    0x401a25: mov      rbp, rsp
    0x401a28: mov      qword ptr [rbp - 0x38], rdi
    0x401a2c: mov      qword ptr [rbp - 0x40], rsi
    0x401a30: mov      qword ptr [rbp - 0x48], rdx
    0x401a34: mov      qword ptr [rbp - 8], 0
    0x401a3c: mov      rax, qword ptr [rbp - 0x48]
    0x401a40: mov      qword ptr [rbp - 0x10], rax
    0x401a44: jmp      0x401b19

; --- Block 0x401a49 [LOOP_HEADER] 3 insns, callees: (none)
    0x401a49: mov      rax, qword ptr [rbp - 0x10]
    0x401a4d: mov      qword ptr [rbp - 0x18], rax
    0x401a51: jmp      0x401b00

; --- Block 0x401a56 [LOOP_HEADER] 9 insns, callees: (none)
    0x401a56: mov      rax, qword ptr [rbp - 0x18]
    0x401a5a: lea      rdx, [rax*8]
    0x401a62: mov      rax, qword ptr [rbp - 0x38]
    0x401a66: add      rax, rdx
    0x401a69: mov      rax, qword ptr [rax]
    0x401a6c: mov      qword ptr [rbp - 0x28], rax
    0x401a70: mov      rax, qword ptr [rbp - 0x18]
    0x401a74: mov      qword ptr [rbp - 0x20], rax
    0x401a78: jmp      0x401ab7

; --- Block 0x401a7a [LOOP_HEADER] 17 insns, callees: (none)
    0x401a7a: mov      rax, qword ptr [rbp - 0x20]
    0x401a7e: sub      rax, qword ptr [rbp - 0x10]
    0x401a82: lea      rdx, [rax*8]
    0x401a8a: mov      rax, qword ptr [rbp - 0x38]
    0x401a8e: add      rax, rdx
    0x401a91: mov      rdx, qword ptr [rbp - 0x20]
    0x401a95: lea      rcx, [rdx*8]
    0x401a9d: mov      rdx, qword ptr [rbp - 0x38]
    0x401aa1: add      rdx, rcx
    0x401aa4: mov      rax, qword ptr [rax]
    0x401aa7: mov      qword ptr [rdx], rax
    0x401aaa: mov      rax, qword ptr [rbp - 0x10]
    ... +5 more instructions

; --- Block 0x401ab7 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x401ab7: mov      rax, qword ptr [rbp - 0x20]
    0x401abb: cmp      rax, qword ptr [rbp - 0x10]
    0x401abf: jb       0x401ae1

; --- Block 0x401ac1 [BODY] 8 insns, callees: (none)
    0x401ac1: mov      rax, qword ptr [rbp - 0x20]
    0x401ac5: sub      rax, qword ptr [rbp - 0x10]
    0x401ac9: lea      rdx, [rax*8]
    0x401ad1: mov      rax, qword ptr [rbp - 0x38]
    0x401ad5: add      rax, rdx
    0x401ad8: mov      rax, qword ptr [rax]
    0x401adb: cmp      qword ptr [rbp - 0x28], rax
    0x401adf: jb       0x401a7a

; --- Block 0x401ae1 [BODY] 10 insns, callees: (none)
    0x401ae1: mov      rax, qword ptr [rbp - 0x20]
    0x401ae5: lea      rdx, [rax*8]
    0x401aed: mov      rax, qword ptr [rbp - 0x38]
    0x401af1: add      rdx, rax
    0x401af4: mov      rax, qword ptr [rbp - 0x28]
    0x401af8: mov      qword ptr [rdx], rax
    0x401afb: add      qword ptr [rbp - 0x18], 1
    0x401b00: mov      rax, qword ptr [rbp - 0x18]
    0x401b04: cmp      rax, qword ptr [rbp - 0x40]
    0x401b08: jb       0x401a56

; --- Block 0x401b00 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x401b00: mov      rax, qword ptr [rbp - 0x18]
    0x401b04: cmp      rax, qword ptr [rbp - 0x40]
    0x401b08: jb       0x401a56

; --- Block 0x401b0e [BODY] 5 insns, callees: (none)
    0x401b0e: mov      rax, qword ptr [rbp - 0x10]
    0x401b12: shr      rax, 1
    0x401b15: mov      qword ptr [rbp - 0x10], rax
    0x401b19: cmp      qword ptr [rbp - 0x10], 0
    0x401b1e: jne      0x401a49

; --- Block 0x401b19 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x401b19: cmp      qword ptr [rbp - 0x10], 0
    0x401b1e: jne      0x401a49

; --- Block 0x401b24 [EPILOGUE] 3 insns, callees: (none)
    0x401b24: mov      rax, qword ptr [rbp - 8]
    0x401b28: pop      rbp
    0x401b29: ret      

```

**O2 blocks** (14 total):

```asm
; --- Block 0x403b80 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403b80: xor      r10d, r10d
    0x403b83: test     rdx, rdx
    0x403b86: je       0x403c35

; --- Block 0x403b8c [BODY] 14 insns, callees: (none)
    0x403b8c: push     r14
    0x403b8e: mov      r8, rdx
    0x403b91: push     r13
    0x403b93: mov      r13, rsi
    0x403b96: push     r12
    0x403b98: mov      r12, rdi
    0x403b9b: push     rbp
    0x403b9c: push     rbx
    0x403b9d: nop      dword ptr [rax]
    0x403ba0: lea      r9, [r8*8]
    0x403ba8: mov      r14, r8
    0x403bab: lea      rbp, [r12 + r9]
    ... +2 more instructions

; --- Block 0x403ba0 [LOOP_HEADER] 5 insns, callees: (none)
    0x403ba0: lea      r9, [r8*8]
    0x403ba8: mov      r14, r8
    0x403bab: lea      rbp, [r12 + r9]
    0x403baf: cmp      r13, r8
    0x403bb2: jbe      0x403c0e

; --- Block 0x403bb4 [PROLOGUE] 1 insns, callees: (none)
    0x403bb4: nop      dword ptr [rax]

; --- Block 0x403bb8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x403bb8: mov      r11, qword ptr [rbp]
    0x403bbc: mov      rdi, rbp
    0x403bbf: cmp      r8, r14
    0x403bc2: ja       0x403bfe

; --- Block 0x403bc4 [BODY] 5 insns, callees: (none)
    0x403bc4: mov      rax, rbp
    0x403bc7: mov      rcx, rbp
    0x403bca: mov      rdx, r14
    0x403bcd: sub      rax, r9
    0x403bd0: jmp      0x403bed

; --- Block 0x403bd8 [LOOP_HEADER] 7 insns, callees: (none)
    0x403bd8: sub      rdi, r9
    0x403bdb: mov      qword ptr [rcx], rsi
    0x403bde: add      r10, 1
    0x403be2: sub      rax, r9
    0x403be5: mov      rcx, rdi
    0x403be8: cmp      rdx, r8
    0x403beb: jb       0x403c20

; --- Block 0x403bed [ITERATOR_STATE] 6 insns, callees: (none)
    0x403bed: mov      rsi, qword ptr [rax]
    0x403bf0: sub      rdx, r8
    0x403bf3: mov      rbx, rax
    0x403bf6: mov      rdi, rcx
    0x403bf9: cmp      rsi, r11
    0x403bfc: ja       0x403bd8

; --- Block 0x403bfe [ITERATOR_STATE] 5 insns, callees: (none)
    0x403bfe: add      r14, 1
    0x403c02: mov      qword ptr [rdi], r11
    0x403c05: add      rbp, 8
    0x403c09: cmp      r13, r14
    0x403c0c: jne      0x403bb8

; --- Block 0x403c0e [LOOP_HEADER] 2 insns, callees: (none)
    0x403c0e: shr      r8, 1
    0x403c11: jne      0x403ba0

; --- Block 0x403c13 [BODY] 7 insns, callees: (none)
    0x403c13: pop      rbx
    0x403c14: mov      rax, r10
    0x403c17: pop      rbp
    0x403c18: pop      r12
    0x403c1a: pop      r13
    0x403c1c: pop      r14
    0x403c1e: ret      

; --- Block 0x403c20 [ITERATOR_STATE] 6 insns, callees: (none)
    0x403c20: mov      rdi, rbx
    0x403c23: add      r14, 1
    0x403c27: add      rbp, 8
    0x403c2b: mov      qword ptr [rdi], r11
    0x403c2e: cmp      r13, r14
    0x403c31: jne      0x403bb8

; --- Block 0x403c33 [BODY] 1 insns, callees: (none)
    0x403c33: jmp      0x403c0e

; --- Block 0x403c35 [EPILOGUE] 2 insns, callees: (none)
    0x403c35: mov      rax, r10
    0x403c38: ret      

```

**Hungarian matching result** (mean similarity: 0.724):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x401b00` | BOUNDS_CHECK | `0x403bb8` | BOUNDS_CHECK | 0.875 | GOOD |
| `0x401ac1` | BODY | `0x403bd8` | LOOP_HEADER | 0.829 | GOOD |
| `0x401ab7` | BOUNDS_CHECK | `0x403b80` | BOUNDS_CHECK | 0.783 | GOOD |
| `0x401b19` | BOUNDS_CHECK | `0x403c0e` | LOOP_HEADER | 0.758 | GOOD |
| `0x401b24` | EPILOGUE | `0x403c35` | EPILOGUE | 0.747 | GOOD |
| `0x401b0e` | BODY | `0x403bed` | ITERATOR_STATE | 0.732 | GOOD |
| `0x401ae1` | BODY | `0x403ba0` | LOOP_HEADER | 0.726 | GOOD |
| `0x401a7a` | LOOP_HEADER | `0x403b8c` | BODY | 0.693 | PARTIAL |
| `0x401a24` | BODY | `0x403bc4` | BODY | 0.632 | PARTIAL |
| `0x401a49` | LOOP_HEADER | `0x403bb4` | PROLOGUE | 0.619 | PARTIAL |
| `0x401a56` | LOOP_HEADER | `0x403c13` | BODY | 0.564 | PARTIAL |
| — | — | `0x403bfe` | ITERATOR_STATE | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x403c20` | ITERATOR_STATE | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x403c33` | BODY | 0.000 | UNMATCHED (O2 only) |

---

## Function `bc_09`

### Rust `bc_09` — O0: 25 blocks, O2: 16 blocks

**O0 blocks** (25 total):

```asm
; --- Block 0x447280 [BODY] 11 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x447280: sub      rsp, 0x88
    0x447287: mov      qword ptr [rsp + 0x28], rdi
    0x44728c: mov      qword ptr [rsp + 0x30], rsi
    0x447291: mov      qword ptr [rsp + 0x68], rdi
    0x447296: mov      qword ptr [rsp + 0x70], rsi
    0x44729b: mov      qword ptr [rsp + 0x78], rsi
    0x4472a0: mov      qword ptr [rsp + 0x38], 0
    0x4472a9: mov      rsi, qword ptr [rsp + 0x30]
    0x4472ae: mov      byte ptr [rsp + 0x47], 0
    0x4472b3: mov      edi, 1
    0x4472b8: call     0x49b480

; --- Block 0x4472a9 [LOOP_HEADER] 4 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x4472a9: mov      rsi, qword ptr [rsp + 0x30]
    0x4472ae: mov      byte ptr [rsp + 0x47], 0
    0x4472b3: mov      edi, 1
    0x4472b8: call     0x49b480

; --- Block 0x4472bd [BODY] 4 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4472bd: mov      qword ptr [rsp + 0x48], rax
    0x4472c2: mov      qword ptr [rsp + 0x50], rdx
    0x4472c7: lea      rdi, [rsp + 0x48]
    0x4472cc: call     0x49ad10

; --- Block 0x4472c7 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4472c7: lea      rdi, [rsp + 0x48]
    0x4472cc: call     0x49ad10

; --- Block 0x4472d1 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4472d1: mov      qword ptr [rsp + 0x58], rax
    0x4472d6: mov      qword ptr [rsp + 0x60], rdx
    0x4472db: test     qword ptr [rsp + 0x58], 1
    0x4472e4: je       0x44730c

; --- Block 0x4472e6 [BODY] 8 insns, callees: (none)
    0x4472e6: mov      rax, qword ptr [rsp + 0x60]
    0x4472eb: mov      qword ptr [rsp + 0x18], rax
    0x4472f0: mov      qword ptr [rsp + 0x80], rax
    0x4472f8: mov      rcx, rax
    0x4472fb: sub      rcx, 1
    0x4472ff: mov      qword ptr [rsp + 0x20], rcx
    0x447304: cmp      rax, 1
    0x447308: jb       0x447364

; --- Block 0x44730a [BODY] 1 insns, callees: (none)
    0x44730a: jmp      0x447353

; --- Block 0x44730c [ITERATOR_STATE] 6 insns, callees: (none)
    0x44730c: mov      rcx, qword ptr [rsp + 0x38]
    0x447311: mov      rax, rcx
    0x447314: add      rax, 1
    0x447318: mov      qword ptr [rsp + 0x10], rax
    0x44731d: cmp      rax, rcx
    0x447320: jb       0x447339

; --- Block 0x447322 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x447322: mov      rax, qword ptr [rsp + 0x10]
    0x447327: mov      qword ptr [rsp + 0x38], rax
    0x44732c: test     byte ptr [rsp + 0x47], 1
    0x447331: jne      0x4472a9

; --- Block 0x447337 [BODY] 1 insns, callees: (none)
    0x447337: jmp      0x447346

; --- Block 0x447339 [BODY] 2 insns, callees: (none)
    0x447339: lea      rdi, [rip + 0xa8100]
    0x447340: call     qword ptr [rip + 0xaddea]

; --- Block 0x447346 [EPILOGUE] 3 insns, callees: (none)
    0x447346: mov      rax, qword ptr [rsp + 0x38]
    0x44734b: add      rsp, 0x88
    0x447352: ret      

; --- Block 0x447353 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x447353: mov      rax, qword ptr [rsp + 0x20]
    0x447358: mov      rcx, qword ptr [rsp + 0x30]
    0x44735d: cmp      rax, rcx
    0x447360: jb       0x447371

; --- Block 0x447362 [BODY] 1 insns, callees: (none)
    0x447362: jmp      0x447395

; --- Block 0x447364 [BODY] 2 insns, callees: (none)
    0x447364: lea      rdi, [rip + 0xa80ed]
    0x44736b: call     qword ptr [rip + 0xadddf]

; --- Block 0x447371 [BODY] 8 insns, callees: (none)
    0x447371: mov      rax, qword ptr [rsp + 0x18]
    0x447376: mov      rcx, qword ptr [rsp + 0x30]
    0x44737b: mov      rdx, qword ptr [rsp + 0x28]
    0x447380: mov      rsi, qword ptr [rsp + 0x20]
    0x447385: mov      rdx, qword ptr [rdx + rsi*8]
    0x447389: mov      qword ptr [rsp + 8], rdx
    0x44738e: cmp      rax, rcx
    0x447391: jb       0x4473ac

; --- Block 0x447393 [BODY] 1 insns, callees: (none)
    0x447393: jmp      0x4473c6

; --- Block 0x447395 [BODY] 4 insns, callees: (none)
    0x447395: mov      rsi, qword ptr [rsp + 0x30]
    0x44739a: mov      rdi, qword ptr [rsp + 0x20]
    0x44739f: lea      rdx, [rip + 0xa80ca]
    0x4473a6: call     qword ptr [rip + 0xadcec]

; --- Block 0x4473ac [BODY] 5 insns, callees: (none)
    0x4473ac: mov      rax, qword ptr [rsp + 8]
    0x4473b1: mov      rcx, qword ptr [rsp + 0x28]
    0x4473b6: mov      rdx, qword ptr [rsp + 0x18]
    0x4473bb: cmp      rax, qword ptr [rcx + rdx*8]
    0x4473bf: ja       0x4473dd

; --- Block 0x4473c1 [BODY] 1 insns, callees: (none)
    0x4473c1: jmp      0x4472c7

; --- Block 0x4473c6 [BODY] 4 insns, callees: (none)
    0x4473c6: mov      rsi, qword ptr [rsp + 0x30]
    0x4473cb: mov      rdi, qword ptr [rsp + 0x18]
    0x4473d0: lea      rdx, [rip + 0xa80b1]
    0x4473d7: call     qword ptr [rip + 0xadcbb]

; --- Block 0x4473dd [ITERATOR_STATE] 6 insns, callees: (none)
    0x4473dd: mov      rax, qword ptr [rsp + 0x18]
    0x4473e2: mov      rcx, rax
    0x4473e5: sub      rcx, 1
    0x4473e9: mov      qword ptr [rsp], rcx
    0x4473ed: cmp      rax, 1
    0x4473f1: jb       0x44741c

; --- Block 0x4473f3 [BODY] 6 insns, callees: core::slice::<impl [T]>::swap
    0x4473f3: mov      rcx, qword ptr [rsp + 0x18]
    0x4473f8: mov      rdx, qword ptr [rsp]
    0x4473fc: mov      rsi, qword ptr [rsp + 0x30]
    0x447401: mov      rdi, qword ptr [rsp + 0x28]
    0x447406: lea      r8, [rip + 0xa80ab]
    0x44740d: call     0x491110

; --- Block 0x447412 [BODY] 2 insns, callees: (none)
    0x447412: mov      byte ptr [rsp + 0x47], 1
    0x447417: jmp      0x4472c7

; --- Block 0x44741c [BODY] 2 insns, callees: (none)
    0x44741c: lea      rdi, [rip + 0xa807d]
    0x447423: call     qword ptr [rip + 0xadd27]

```

**O2 blocks** (16 total):

```asm
; --- Block 0x4233e0 [BODY] 7 insns, callees: (none)
    0x4233e0: push     rbx
    0x4233e1: lea      rcx, [rsi - 1]
    0x4233e5: mov      rdx, rcx
    0x4233e8: and      rdx, 0xfffffffffffffffe
    0x4233ec: neg      rdx
    0x4233ef: xor      eax, eax
    0x4233f1: jmp      0x42340d

; --- Block 0x423400 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423400: inc      rax
    0x423403: test     r8b, 1
    0x423407: je       0x4234ac

; --- Block 0x42340d [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42340d: cmp      rsi, 2
    0x423411: jb       0x4234a7

; --- Block 0x423417 [BODY] 1 insns, callees: (none)
    0x423417: jne      0x423450

; --- Block 0x423419 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423419: mov      r9d, 1
    0x42341f: xor      r8d, r8d
    0x423422: test     cl, 1
    0x423425: je       0x423400

; --- Block 0x423422 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x423422: test     cl, 1
    0x423425: je       0x423400

; --- Block 0x423427 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423427: mov      r10, qword ptr [rdi + r9*8 - 8]
    0x42342c: mov      r11, qword ptr [rdi + r9*8]
    0x423430: cmp      r10, r11
    0x423433: jbe      0x423400

; --- Block 0x423435 [BODY] 4 insns, callees: (none)
    0x423435: mov      qword ptr [rdi + r9*8 - 8], r11
    0x42343a: mov      qword ptr [rdi + r9*8], r10
    0x42343e: mov      r8b, 1
    0x423441: jmp      0x423400

; --- Block 0x423450 [BODY] 3 insns, callees: (none)
    0x423450: mov      r10d, 1
    0x423456: xor      r8d, r8d
    0x423459: jmp      0x42346d

; --- Block 0x423460 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423460: lea      r11, [rdx + r9]
    0x423464: mov      r10, r9
    0x423467: cmp      r11, 1
    0x42346b: je       0x423422

; --- Block 0x42346d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42346d: mov      r9, qword ptr [rdi + r10*8 - 8]
    0x423472: mov      r11, qword ptr [rdi + r10*8]
    0x423476: cmp      r9, r11
    0x423479: jbe      0x423487

; --- Block 0x42347b [BODY] 8 insns, callees: (none)
    0x42347b: mov      qword ptr [rdi + r10*8 - 8], r11
    0x423480: mov      qword ptr [rdi + r10*8], r9
    0x423484: mov      r8b, 1
    0x423487: lea      r9, [r10 + 2]
    0x42348b: mov      r11, qword ptr [rdi + r10*8]
    0x42348f: mov      rbx, qword ptr [rdi + r10*8 + 8]
    0x423494: cmp      r11, rbx
    0x423497: jbe      0x423460

; --- Block 0x423487 [BODY] 5 insns, callees: (none)
    0x423487: lea      r9, [r10 + 2]
    0x42348b: mov      r11, qword ptr [rdi + r10*8]
    0x42348f: mov      rbx, qword ptr [rdi + r10*8 + 8]
    0x423494: cmp      r11, rbx
    0x423497: jbe      0x423460

; --- Block 0x423499 [BODY] 4 insns, callees: (none)
    0x423499: mov      qword ptr [rdi + r10*8], rbx
    0x42349d: mov      qword ptr [rdi + r9*8 - 8], r11
    0x4234a2: mov      r8b, 1
    0x4234a5: jmp      0x423460

; --- Block 0x4234a7 [EPILOGUE] 3 insns, callees: (none)
    0x4234a7: mov      eax, 1
    0x4234ac: pop      rbx
    0x4234ad: ret      

; --- Block 0x4234ac [EPILOGUE] 2 insns, callees: (none)
    0x4234ac: pop      rbx
    0x4234ad: ret      

```

**Hungarian matching result** (mean similarity: 0.720):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4472d1` | BOUNDS_CHECK | `0x42346d` | BOUNDS_CHECK | 0.983 | GOOD |
| `0x447353` | BOUNDS_CHECK | `0x423427` | BOUNDS_CHECK | 0.938 | GOOD |
| `0x447322` | BOUNDS_CHECK | `0x423419` | BOUNDS_CHECK | 0.860 | GOOD |
| `0x4473ac` | BODY | `0x423487` | BODY | 0.836 | GOOD |
| `0x447371` | BODY | `0x42347b` | BODY | 0.808 | GOOD |
| `0x447412` | BODY | `0x423450` | BODY | 0.765 | GOOD |
| `0x4473c6` | BODY | `0x423460` | BOUNDS_CHECK | 0.730 | GOOD |
| `0x4472a9` | LOOP_HEADER | `0x423435` | BODY | 0.714 | GOOD |
| `0x44730c` | ITERATOR_STATE | `0x423400` | BOUNDS_CHECK | 0.714 | GOOD |
| `0x447395` | BODY | `0x423499` | BODY | 0.698 | PARTIAL |
| `0x44730a` | BODY | `0x423417` | BODY | 0.662 | PARTIAL |
| `0x447339` | BODY | `0x423422` | BOUNDS_CHECK | 0.651 | PARTIAL |
| `0x44741c` | BODY | `0x4234ac` | EPILOGUE | 0.635 | PARTIAL |
| `0x4472bd` | BODY | `0x4234a7` | EPILOGUE | 0.601 | PARTIAL |
| `0x447364` | BODY | `0x42340d` | BOUNDS_CHECK | 0.479 | PARTIAL |
| `0x4473f3` | BODY | `0x4233e0` | BODY | 0.443 | PARTIAL |
| `0x447280` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4472c7` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4472e6` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x447337` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x447346` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x447362` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x447393` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4473c1` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4473dd` | ITERATOR_STATE | — | — | 0.000 | UNMATCHED (O0 only) |

### C `bc_09` — O0: 9 blocks, O2: 9 blocks

**O0 blocks** (9 total):

```asm
; --- Block 0x401f08 [BODY] 8 insns, callees: (none)
    0x401f08: push     rbp
    0x401f09: mov      rbp, rsp
    0x401f0c: mov      qword ptr [rbp - 0x28], rdi
    0x401f10: mov      qword ptr [rbp - 0x30], rsi
    0x401f14: mov      qword ptr [rbp - 8], 0
    0x401f1c: mov      dword ptr [rbp - 0xc], 0
    0x401f23: mov      qword ptr [rbp - 0x18], 1
    0x401f2b: jmp      0x401fcd

; --- Block 0x401f1c [LOOP_HEADER] 3 insns, callees: (none)
    0x401f1c: mov      dword ptr [rbp - 0xc], 0
    0x401f23: mov      qword ptr [rbp - 0x18], 1
    0x401f2b: jmp      0x401fcd

; --- Block 0x401f30 [LOOP_HEADER] 13 insns, callees: (none)
    0x401f30: mov      rax, qword ptr [rbp - 0x18]
    0x401f34: shl      rax, 3
    0x401f38: lea      rdx, [rax - 8]
    0x401f3c: mov      rax, qword ptr [rbp - 0x28]
    0x401f40: add      rax, rdx
    0x401f43: mov      rdx, qword ptr [rax]
    0x401f46: mov      rax, qword ptr [rbp - 0x18]
    0x401f4a: lea      rcx, [rax*8]
    0x401f52: mov      rax, qword ptr [rbp - 0x28]
    0x401f56: add      rax, rcx
    0x401f59: mov      rax, qword ptr [rax]
    0x401f5c: cmp      rdx, rax
    ... +1 more instructions

; --- Block 0x401f61 [BODY] 29 insns, callees: (none)
    0x401f61: mov      rax, qword ptr [rbp - 0x18]
    0x401f65: shl      rax, 3
    0x401f69: lea      rdx, [rax - 8]
    0x401f6d: mov      rax, qword ptr [rbp - 0x28]
    0x401f71: add      rax, rdx
    0x401f74: mov      rax, qword ptr [rax]
    0x401f77: mov      qword ptr [rbp - 0x20], rax
    0x401f7b: mov      rax, qword ptr [rbp - 0x18]
    0x401f7f: lea      rdx, [rax*8]
    0x401f87: mov      rax, qword ptr [rbp - 0x28]
    0x401f8b: add      rax, rdx
    0x401f8e: mov      rdx, qword ptr [rbp - 0x18]
    ... +17 more instructions

; --- Block 0x401fc8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x401fc8: add      qword ptr [rbp - 0x18], 1
    0x401fcd: mov      rax, qword ptr [rbp - 0x18]
    0x401fd1: cmp      rax, qword ptr [rbp - 0x30]
    0x401fd5: jb       0x401f30

; --- Block 0x401fcd [BOUNDS_CHECK] 3 insns, callees: (none)
    0x401fcd: mov      rax, qword ptr [rbp - 0x18]
    0x401fd1: cmp      rax, qword ptr [rbp - 0x30]
    0x401fd5: jb       0x401f30

; --- Block 0x401fdb [BOUNDS_CHECK] 3 insns, callees: (none)
    0x401fdb: add      qword ptr [rbp - 8], 1
    0x401fe0: cmp      dword ptr [rbp - 0xc], 0
    0x401fe4: je       0x401feb

; --- Block 0x401fe6 [BODY] 1 insns, callees: (none)
    0x401fe6: jmp      0x401f1c

; --- Block 0x401feb [EPILOGUE] 4 insns, callees: (none)
    0x401feb: nop      
    0x401fec: mov      rax, qword ptr [rbp - 8]
    0x401ff0: pop      rbp
    0x401ff1: ret      

```

**O2 blocks** (9 total):

```asm
; --- Block 0x403df0 [BODY] 5 insns, callees: (none)
    0x403df0: lea      r8, [rdi + rsi*8 - 8]
    0x403df5: xor      r10d, r10d
    0x403df8: nop      dword ptr [rax + rax]
    0x403e00: cmp      rsi, 1
    0x403e04: jbe      0x403e40

; --- Block 0x403e00 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x403e00: cmp      rsi, 1
    0x403e04: jbe      0x403e40

; --- Block 0x403e06 [BODY] 7 insns, callees: (none)
    0x403e06: mov      rax, rdi
    0x403e09: xor      r9d, r9d
    0x403e0c: nop      dword ptr [rax]
    0x403e10: mov      rdx, qword ptr [rax]
    0x403e13: mov      rcx, qword ptr [rax + 8]
    0x403e17: cmp      rdx, rcx
    0x403e1a: jbe      0x403e29

; --- Block 0x403e10 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x403e10: mov      rdx, qword ptr [rax]
    0x403e13: mov      rcx, qword ptr [rax + 8]
    0x403e17: cmp      rdx, rcx
    0x403e1a: jbe      0x403e29

; --- Block 0x403e1c [ITERATOR_STATE] 6 insns, callees: (none)
    0x403e1c: mov      qword ptr [rax], rcx
    0x403e1f: mov      r9d, 1
    0x403e25: mov      qword ptr [rax + 8], rdx
    0x403e29: add      rax, 8
    0x403e2d: cmp      rax, r8
    0x403e30: jne      0x403e10

; --- Block 0x403e29 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403e29: add      rax, 8
    0x403e2d: cmp      rax, r8
    0x403e30: jne      0x403e10

; --- Block 0x403e32 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403e32: add      r10, 1
    0x403e36: test     r9d, r9d
    0x403e39: jne      0x403e00

; --- Block 0x403e3b [EPILOGUE] 2 insns, callees: (none)
    0x403e3b: mov      rax, r10
    0x403e3e: ret      

; --- Block 0x403e40 [EPILOGUE] 3 insns, callees: (none)
    0x403e40: add      r10, 1
    0x403e44: mov      rax, r10
    0x403e47: ret      

```

**Hungarian matching result** (mean similarity: 0.651):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x401fdb` | BOUNDS_CHECK | `0x403e32` | BOUNDS_CHECK | 0.987 | GOOD |
| `0x401fcd` | BOUNDS_CHECK | `0x403e10` | BOUNDS_CHECK | 0.875 | GOOD |
| `0x401f1c` | LOOP_HEADER | `0x403e40` | EPILOGUE | 0.711 | GOOD |
| `0x401feb` | EPILOGUE | `0x403e3b` | EPILOGUE | 0.691 | PARTIAL |
| `0x401fc8` | BOUNDS_CHECK | `0x403df0` | BODY | 0.653 | PARTIAL |
| `0x401f08` | BODY | `0x403e06` | BODY | 0.618 | PARTIAL |
| `0x401fe6` | BODY | `0x403e00` | BOUNDS_CHECK | 0.491 | PARTIAL |
| `0x401f30` | LOOP_HEADER | `0x403e1c` | ITERATOR_STATE | 0.472 | PARTIAL |
| `0x401f61` | BODY | `0x403e29` | BOUNDS_CHECK | 0.357 | POOR |

---

## Function `bc_12`

### Rust `bc_12` — O0: 63 blocks, O2: 93 blocks

**O0 blocks** (63 total):

```asm
; --- Block 0x447ae0 [BODY] 13 insns, callees: (none)
    0x447ae0: sub      rsp, 0x218
    0x447ae7: mov      qword ptr [rsp + 0xb8], rcx
    0x447aef: mov      qword ptr [rsp + 0xc0], rdx
    0x447af7: mov      qword ptr [rsp + 0xc8], rsi
    0x447aff: mov      qword ptr [rsp + 0xd0], rdi
    0x447b07: mov      qword ptr [rsp + 0xd8], rdi
    0x447b0f: mov      qword ptr [rsp + 0x158], rsi
    0x447b17: mov      qword ptr [rsp + 0x160], rdx
    0x447b1f: mov      qword ptr [rsp + 0x168], rcx
    0x447b27: mov      byte ptr [rsp + 0x157], 0
    0x447b2f: mov      qword ptr [rsp + 0x170], rdx
    0x447b37: cmp      rcx, 0
    ... +1 more instructions

; --- Block 0x447b3d [LOOP_HEADER] 2 insns, callees: alloc::vec::Vec<T>::new
    0x447b3d: mov      rdi, qword ptr [rsp + 0xd0]
    0x447b45: call     0x4a51a0

; --- Block 0x447b4a [BODY] 1 insns, callees: (none)
    0x447b4a: jmp      0x447ea4

; --- Block 0x447b4f [BOUNDS_CHECK] 4 insns, callees: (none)
    0x447b4f: mov      rax, qword ptr [rsp + 0xb8]
    0x447b57: mov      rcx, qword ptr [rsp + 0xc0]
    0x447b5f: cmp      rax, rcx
    0x447b62: ja       0x447b3d

; --- Block 0x447b64 [BODY] 7 insns, callees: (none)
    0x447b64: mov      rax, qword ptr [rsp + 0xc0]
    0x447b6c: mov      rcx, qword ptr [rsp + 0xb8]
    0x447b74: mov      rdx, rax
    0x447b77: sub      rdx, rcx
    0x447b7a: mov      qword ptr [rsp + 0xb0], rdx
    0x447b82: cmp      rax, rcx
    0x447b85: jb       0x447ba9

; --- Block 0x447b87 [ITERATOR_STATE] 6 insns, callees: (none)
    0x447b87: mov      rcx, qword ptr [rsp + 0xb0]
    0x447b8f: mov      rax, rcx
    0x447b92: add      rax, 1
    0x447b96: mov      qword ptr [rsp + 0xa8], rax
    0x447b9e: cmp      rax, rcx
    0x447ba1: jb       0x447ccc

; --- Block 0x447ba7 [BODY] 1 insns, callees: (none)
    0x447ba7: jmp      0x447bb6

; --- Block 0x447ba9 [BODY] 2 insns, callees: (none)
    0x447ba9: lea      rdi, [rip + 0xa7ad0]
    0x447bb0: call     qword ptr [rip + 0xad59a]

; --- Block 0x447bb6 [BODY] 4 insns, callees: alloc::vec::Vec<T>::with_capacity
    0x447bb6: mov      rsi, qword ptr [rsp + 0xa8]
    0x447bbe: mov      byte ptr [rsp + 0x157], 1
    0x447bc6: lea      rdi, [rsp + 0xe0]
    0x447bce: call     0x4a5020

; --- Block 0x447bd3 [BODY] 22 insns, callees: (none)
    0x447bd3: mov      rdx, qword ptr [rsp + 0xc8]
    0x447bdb: mov      rcx, qword ptr [rsp + 0xc0]
    0x447be3: mov      rax, qword ptr [rsp + 0xb8]
    0x447beb: mov      qword ptr [rsp + 0x1a0], rdx
    0x447bf3: mov      qword ptr [rsp + 0x1a8], rcx
    0x447bfb: mov      qword ptr [rsp + 0x1b0], rax
    0x447c03: mov      qword ptr [rsp + 0x1b8], rax
    0x447c0b: mov      qword ptr [rsp + 0x1c0], rdx
    0x447c13: mov      qword ptr [rsp + 0x1c8], rcx
    0x447c1b: mov      qword ptr [rsp + 0x1e0], 0
    0x447c27: mov      qword ptr [rsp + 0x1e8], rax
    0x447c2f: mov      qword ptr [rsp + 0x1f0], rdx
    ... +10 more instructions

; --- Block 0x447c84 [BODY] 6 insns, callees: (none)
    0x447c84: mov      rdx, qword ptr [rsp + 0xc0]
    0x447c8c: mov      rsi, qword ptr [rsp + 0xb8]
    0x447c94: lea      rcx, [rip + 0xa79fd]
    0x447c9b: mov      rax, qword ptr [rip + 0xad416]
    0x447ca2: xor      edi, edi
    0x447ca4: call     rax

; --- Block 0x447caa [BODY] 5 insns, callees: (none)
    0x447caa: mov      rax, qword ptr [rsp + 0xc8]
    0x447cb2: mov      rcx, qword ptr [rsp + 0xa0]
    0x447cba: mov      qword ptr [rsp + 0x90], rcx
    0x447cc2: mov      qword ptr [rsp + 0x98], rax
    0x447cca: jmp      0x447d02

; --- Block 0x447ccc [BODY] 2 insns, callees: (none)
    0x447ccc: lea      rdi, [rip + 0xa79ad]
    0x447cd3: call     qword ptr [rip + 0xad457]

; --- Block 0x447d02 [BODY] 4 insns, callees: alloc::slice::<impl [T]>::to_vec
    0x447d02: mov      rdx, qword ptr [rsp + 0x90]
    0x447d0a: mov      rsi, qword ptr [rsp + 0x98]
    0x447d12: lea      rdi, [rsp + 0xf8]
    0x447d1a: call     0x4632c0

; --- Block 0x447d1f [BODY] 1 insns, callees: (none)
    0x447d1f: jmp      0x447d21

; --- Block 0x447d21 [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::DerefMut>::deref_mut
    0x447d21: lea      rdi, [rsp + 0xf8]
    0x447d29: call     0x4ab8a0

; --- Block 0x447d2e [BODY] 3 insns, callees: (none)
    0x447d2e: mov      qword ptr [rsp + 0x80], rdx
    0x447d36: mov      qword ptr [rsp + 0x88], rax
    0x447d3e: jmp      0x447d65

; --- Block 0x447d65 [BODY] 3 insns, callees: alloc::slice::<impl [T]>::sort
    0x447d65: mov      rsi, qword ptr [rsp + 0x80]
    0x447d6d: mov      rdi, qword ptr [rsp + 0x88]
    0x447d75: call     0x463280

; --- Block 0x447d7a [BODY] 1 insns, callees: (none)
    0x447d7a: jmp      0x447d7c

; --- Block 0x447d7c [BODY] 1 insns, callees: (none)
    0x447d7c: jmp      0x447d7e

; --- Block 0x447d7e [BODY] 5 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x447d7e: mov      rsi, qword ptr [rsp + 0xb8]
    0x447d86: shr      rsi, 1
    0x447d89: lea      rdx, [rip + 0xa7920]
    0x447d90: lea      rdi, [rsp + 0xf8]
    0x447d98: call     0x4abb40

; --- Block 0x447d9d [BODY] 2 insns, callees: (none)
    0x447d9d: mov      qword ptr [rsp + 0x78], rax
    0x447da2: jmp      0x447da4

; --- Block 0x447da4 [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x447da4: mov      rax, qword ptr [rsp + 0x78]
    0x447da9: mov      rsi, qword ptr [rax]
    0x447dac: lea      rdi, [rsp + 0xe0]
    0x447db4: call     0x4a9070

; --- Block 0x447db9 [BODY] 1 insns, callees: (none)
    0x447db9: jmp      0x447dbb

; --- Block 0x447dbb [BODY] 3 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x447dbb: mov      rsi, qword ptr [rsp + 0xc0]
    0x447dc3: mov      rdi, qword ptr [rsp + 0xb8]
    0x447dcb: call     0x49b480

; --- Block 0x447dd0 [BODY] 3 insns, callees: (none)
    0x447dd0: mov      qword ptr [rsp + 0x68], rdx
    0x447dd5: mov      qword ptr [rsp + 0x70], rax
    0x447dda: jmp      0x447ddc

; --- Block 0x447ddc [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x447ddc: mov      rax, qword ptr [rsp + 0x68]
    0x447de1: mov      rcx, qword ptr [rsp + 0x70]
    0x447de6: mov      qword ptr [rsp + 0x110], rcx
    0x447dee: mov      qword ptr [rsp + 0x118], rax
    0x447df6: lea      rdi, [rsp + 0x110]
    0x447dfe: call     0x49ad10

; --- Block 0x447df6 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x447df6: lea      rdi, [rsp + 0x110]
    0x447dfe: call     0x49ad10

; --- Block 0x447e03 [BODY] 3 insns, callees: (none)
    0x447e03: mov      qword ptr [rsp + 0x58], rdx
    0x447e08: mov      qword ptr [rsp + 0x60], rax
    0x447e0d: jmp      0x447e0f

; --- Block 0x447e0f [BODY] 6 insns, callees: (none)
    0x447e0f: mov      rax, qword ptr [rsp + 0x58]
    0x447e14: mov      rcx, qword ptr [rsp + 0x60]
    0x447e19: mov      qword ptr [rsp + 0x120], rcx
    0x447e21: mov      qword ptr [rsp + 0x128], rax
    0x447e29: test     qword ptr [rsp + 0x120], 1
    0x447e35: je       0x447e66

; --- Block 0x447e37 [BODY] 9 insns, callees: (none)
    0x447e37: mov      rcx, qword ptr [rsp + 0xb8]
    0x447e3f: mov      rax, qword ptr [rsp + 0x128]
    0x447e47: mov      qword ptr [rsp + 0x48], rax
    0x447e4c: mov      qword ptr [rsp + 0x188], rax
    0x447e54: mov      rdx, rax
    0x447e57: sub      rdx, rcx
    0x447e5a: mov      qword ptr [rsp + 0x50], rdx
    0x447e5f: cmp      rax, rcx
    0x447e62: jb       0x447ec8

; --- Block 0x447e64 [BODY] 1 insns, callees: (none)
    0x447e64: jmp      0x447eb4

; --- Block 0x447e66 [DROP_GLUE] 8 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<u64>>
    0x447e66: mov      rax, qword ptr [rsp + 0xd0]
    0x447e6e: mov      byte ptr [rsp + 0x157], 0
    0x447e76: mov      rcx, qword ptr [rsp + 0xf0]
    0x447e7e: mov      qword ptr [rax + 0x10], rcx
    0x447e82: movups   xmm0, xmmword ptr [rsp + 0xe0]
    0x447e8a: movups   xmmword ptr [rax], xmm0
    0x447e8d: lea      rdi, [rsp + 0xf8]
    0x447e95: call     0x496820

; --- Block 0x447e9a [BODY] 1 insns, callees: (none)
    0x447e9a: jmp      0x447e9c

; --- Block 0x447e9c [EPILOGUE] 4 insns, callees: (none)
    0x447e9c: mov      byte ptr [rsp + 0x157], 0
    0x447ea4: mov      rax, qword ptr [rsp + 0xd8]
    0x447eac: add      rsp, 0x218
    0x447eb3: ret      

; --- Block 0x447ea4 [EPILOGUE] 3 insns, callees: (none)
    0x447ea4: mov      rax, qword ptr [rsp + 0xd8]
    0x447eac: add      rsp, 0x218
    0x447eb3: ret      

; --- Block 0x447eb4 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x447eb4: mov      rax, qword ptr [rsp + 0x50]
    0x447eb9: mov      rcx, qword ptr [rsp + 0xc0]
    0x447ec1: cmp      rax, rcx
    0x447ec4: jb       0x447edc

; --- Block 0x447ec6 [BODY] 1 insns, callees: (none)
    0x447ec6: jmp      0x447f09

; --- Block 0x447ec8 [BODY] 3 insns, callees: (none)
    0x447ec8: lea      rdi, [rip + 0xa77f9]
    0x447ecf: mov      rax, qword ptr [rip + 0xad27a]
    0x447ed6: call     rax

; --- Block 0x447edc [BODY] 8 insns, callees: (none)
    0x447edc: mov      rax, qword ptr [rsp + 0x48]
    0x447ee1: mov      rcx, qword ptr [rsp + 0xc0]
    0x447ee9: mov      rdx, qword ptr [rsp + 0xc8]
    0x447ef1: mov      rsi, qword ptr [rsp + 0x50]
    0x447ef6: mov      rdx, qword ptr [rdx + rsi*8]
    0x447efa: mov      qword ptr [rsp + 0x130], rdx
    0x447f02: cmp      rax, rcx
    0x447f05: jb       0x447f28

; --- Block 0x447f07 [BODY] 1 insns, callees: (none)
    0x447f07: jmp      0x447f5a

; --- Block 0x447f09 [BODY] 5 insns, callees: (none)
    0x447f09: mov      rsi, qword ptr [rsp + 0xc0]
    0x447f11: mov      rdi, qword ptr [rsp + 0x50]
    0x447f16: lea      rdx, [rip + 0xa77c3]
    0x447f1d: mov      rax, qword ptr [rip + 0xad174]
    0x447f24: call     rax

; --- Block 0x447f28 [BODY] 6 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x447f28: mov      rax, qword ptr [rsp + 0xc8]
    0x447f30: mov      rcx, qword ptr [rsp + 0x48]
    0x447f35: mov      rax, qword ptr [rax + rcx*8]
    0x447f39: mov      qword ptr [rsp + 0x138], rax
    0x447f41: lea      rdi, [rsp + 0xf8]
    0x447f49: call     0x4ab750

; --- Block 0x447f4e [BODY] 3 insns, callees: (none)
    0x447f4e: mov      qword ptr [rsp + 0x38], rdx
    0x447f53: mov      qword ptr [rsp + 0x40], rax
    0x447f58: jmp      0x447f7c

; --- Block 0x447f5a [BODY] 5 insns, callees: (none)
    0x447f5a: mov      rsi, qword ptr [rsp + 0xc0]
    0x447f62: mov      rdi, qword ptr [rsp + 0x48]
    0x447f67: lea      rdx, [rip + 0xa778a]
    0x447f6e: mov      rax, qword ptr [rip + 0xad123]
    0x447f75: call     rax

; --- Block 0x447f7c [BODY] 4 insns, callees: core::slice::<impl [T]>::binary_search
    0x447f7c: mov      rsi, qword ptr [rsp + 0x38]
    0x447f81: mov      rdi, qword ptr [rsp + 0x40]
    0x447f86: lea      rdx, [rsp + 0x130]
    0x447f8e: call     0x48fff0

; --- Block 0x447f93 [BODY] 3 insns, callees: (none)
    0x447f93: mov      qword ptr [rsp + 0x28], rdx
    0x447f98: mov      qword ptr [rsp + 0x30], rax
    0x447f9d: jmp      0x447f9f

; --- Block 0x447f9f [BODY] 6 insns, callees: (none)
    0x447f9f: mov      rax, qword ptr [rsp + 0x28]
    0x447fa4: mov      rcx, qword ptr [rsp + 0x30]
    0x447fa9: mov      qword ptr [rsp + 0x140], rcx
    0x447fb1: mov      qword ptr [rsp + 0x148], rax
    0x447fb9: test     qword ptr [rsp + 0x140], 1
    0x447fc5: je       0x447fe0

; --- Block 0x447fc7 [LOOP_HEADER] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x447fc7: lea      rdi, [rsp + 0xf8]
    0x447fcf: call     0x4ab750

; --- Block 0x447fd4 [BODY] 3 insns, callees: (none)
    0x447fd4: mov      qword ptr [rsp + 0x18], rdx
    0x447fd9: mov      qword ptr [rsp + 0x20], rax
    0x447fde: jmp      0x448008

; --- Block 0x447fe0 [BODY] 5 insns, callees: alloc::vec::Vec<T,A>::remove
    0x447fe0: mov      rsi, qword ptr [rsp + 0x148]
    0x447fe8: mov      qword ptr [rsp + 0x190], rsi
    0x447ff0: lea      rdx, [rip + 0xa7719]
    0x447ff7: lea      rdi, [rsp + 0xf8]
    0x447fff: call     0x4a9220

; --- Block 0x448004 [BODY] 1 insns, callees: (none)
    0x448004: jmp      0x448006

; --- Block 0x448006 [BODY] 1 insns, callees: (none)
    0x448006: jmp      0x447fc7

; --- Block 0x448008 [BODY] 4 insns, callees: core::slice::<impl [T]>::partition_point
    0x448008: mov      rsi, qword ptr [rsp + 0x18]
    0x44800d: mov      rdi, qword ptr [rsp + 0x20]
    0x448012: lea      rdx, [rsp + 0x138]
    0x44801a: call     0x490040

; --- Block 0x44801f [BODY] 2 insns, callees: (none)
    0x44801f: mov      qword ptr [rsp + 0x10], rax
    0x448024: jmp      0x448026

; --- Block 0x448026 [BODY] 6 insns, callees: alloc::vec::Vec<T,A>::insert
    0x448026: mov      rsi, qword ptr [rsp + 0x10]
    0x44802b: mov      qword ptr [rsp + 0x198], rsi
    0x448033: mov      rdx, qword ptr [rsp + 0x138]
    0x44803b: lea      rcx, [rip + 0xa76e6]
    0x448042: lea      rdi, [rsp + 0xf8]
    0x44804a: call     0x4a9200

; --- Block 0x44804f [BODY] 1 insns, callees: (none)
    0x44804f: jmp      0x448051

; --- Block 0x448051 [BODY] 1 insns, callees: (none)
    0x448051: jmp      0x448053

; --- Block 0x448053 [BODY] 5 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x448053: mov      rsi, qword ptr [rsp + 0xb8]
    0x44805b: shr      rsi, 1
    0x44805e: lea      rdx, [rip + 0xa76db]
    0x448065: lea      rdi, [rsp + 0xf8]
    0x44806d: call     0x4abb40

; --- Block 0x448072 [BODY] 2 insns, callees: (none)
    0x448072: mov      qword ptr [rsp + 8], rax
    0x448077: jmp      0x448079

; --- Block 0x448079 [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x448079: mov      rax, qword ptr [rsp + 8]
    0x44807e: mov      rsi, qword ptr [rax]
    0x448081: lea      rdi, [rsp + 0xe0]
    0x448089: call     0x4a9070

; --- Block 0x44808e [BODY] 1 insns, callees: (none)
    0x44808e: jmp      0x448090

; --- Block 0x448090 [BODY] 1 insns, callees: (none)
    0x448090: jmp      0x447df6

```

**O2 blocks** (93 total):

```asm
; --- Block 0x423730 [BODY] 10 insns, callees: (none)
    0x423730: push     rbp
    0x423731: push     r15
    0x423733: push     r14
    0x423735: push     r13
    0x423737: push     r12
    0x423739: push     rbx
    0x42373a: sub      rsp, 0x68
    0x42373e: lea      rax, [rcx - 1]
    0x423742: cmp      rax, rdx
    0x423745: jae      0x423787

; --- Block 0x423747 [BODY] 13 insns, callees: (none)
    0x423747: mov      r12, rcx
    0x42374a: movabs   rbx, 0x7ffffffffffffff8
    0x423754: mov      r14, rdx
    0x423757: sub      r14, rcx
    0x42375a: lea      r13, [r14*8 + 8]
    0x423762: inc      r14
    0x423765: mov      rax, r14
    0x423768: shr      rax, 0x3d
    0x42376c: setne    al
    0x42376f: cmp      r13, rbx
    0x423772: seta     cl
    0x423775: or       cl, al
    ... +1 more instructions

; --- Block 0x423779 [BODY] 4 insns, callees: (none)
    0x423779: xor      ebp, ebp
    0x42377b: mov      rdi, rbp
    0x42377e: mov      rsi, r13
    0x423781: call     qword ptr [rip + 0x61c91]

; --- Block 0x42377b [LOOP_HEADER] 3 insns, callees: (none)
    0x42377b: mov      rdi, rbp
    0x42377e: mov      rsi, r13
    0x423781: call     qword ptr [rip + 0x61c91]

; --- Block 0x423787 [BODY] 12 insns, callees: (none)
    0x423787: mov      qword ptr [rdi], 0
    0x42378e: mov      qword ptr [rdi + 8], 8
    0x423796: mov      qword ptr [rdi + 0x10], 0
    0x42379e: mov      rax, rdi
    0x4237a1: add      rsp, 0x68
    0x4237a5: pop      rbx
    0x4237a6: pop      r12
    0x4237a8: pop      r13
    0x4237aa: pop      r14
    0x4237ac: pop      r15
    0x4237ae: pop      rbp
    0x4237af: ret      

; --- Block 0x42379e [LOOP_HEADER] 9 insns, callees: (none)
    0x42379e: mov      rax, rdi
    0x4237a1: add      rsp, 0x68
    0x4237a5: pop      rbx
    0x4237a6: pop      r12
    0x4237a8: pop      r13
    0x4237aa: pop      r14
    0x4237ac: pop      r15
    0x4237ae: pop      rbp
    0x4237af: ret      

; --- Block 0x4237b0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4237b0: mov      qword ptr [rsp + 0x48], rsi
    0x4237b5: mov      qword ptr [rsp + 0x58], rdx
    0x4237ba: test     r13, r13
    0x4237bd: je       0x4237e5

; --- Block 0x4237bf [BODY] 2 insns, callees: (none)
    0x4237bf: mov      r15, rdi
    0x4237c2: call     qword ptr [rip + 0x61c20]

; --- Block 0x4237c8 [BODY] 4 insns, callees: (none)
    0x4237c8: mov      ebp, 8
    0x4237cd: mov      esi, 8
    0x4237d2: mov      rdi, r13
    0x4237d5: call     qword ptr [rip + 0x61c15]

; --- Block 0x4237db [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4237db: test     rax, rax
    0x4237de: je       0x42377b

; --- Block 0x4237e0 [BODY] 2 insns, callees: (none)
    0x4237e0: mov      rdi, r15
    0x4237e3: jmp      0x4237ed

; --- Block 0x4237e5 [BODY] 13 insns, callees: (none)
    0x4237e5: mov      eax, 8
    0x4237ea: xor      r14d, r14d
    0x4237ed: movabs   rcx, 0x1fffffffffffffff
    0x4237f7: mov      qword ptr [rsp + 0x28], r14
    0x4237fc: mov      qword ptr [rsp + 0x30], rax
    0x423801: mov      qword ptr [rsp + 0x38], 0
    0x42380a: lea      rbp, [r12*8]
    0x423812: cmp      r12, rcx
    0x423815: seta     al
    0x423818: cmp      rbp, rbx
    0x42381b: seta     cl
    0x42381e: or       cl, al
    ... +1 more instructions

; --- Block 0x4237ed [BODY] 11 insns, callees: (none)
    0x4237ed: movabs   rcx, 0x1fffffffffffffff
    0x4237f7: mov      qword ptr [rsp + 0x28], r14
    0x4237fc: mov      qword ptr [rsp + 0x30], rax
    0x423801: mov      qword ptr [rsp + 0x38], 0
    0x42380a: lea      rbp, [r12*8]
    0x423812: cmp      r12, rcx
    0x423815: seta     al
    0x423818: cmp      rbp, rbx
    0x42381b: seta     cl
    0x42381e: or       cl, al
    0x423820: je       0x423836

; --- Block 0x423822 [BODY] 4 insns, callees: (none)
    0x423822: xor      r13d, r13d
    0x423825: mov      rdi, r13
    0x423828: mov      rsi, rbp
    0x42382b: call     qword ptr [rip + 0x61be7]

; --- Block 0x423825 [LOOP_HEADER] 3 insns, callees: (none)
    0x423825: mov      rdi, r13
    0x423828: mov      rsi, rbp
    0x42382b: call     qword ptr [rip + 0x61be7]

; --- Block 0x423836 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423836: test     rbp, rbp
    0x423839: mov      qword ptr [rsp + 0x60], rdi
    0x42383e: je       0x423867

; --- Block 0x423840 [BODY] 1 insns, callees: (none)
    0x423840: call     qword ptr [rip + 0x61ba2]

; --- Block 0x423846 [BODY] 4 insns, callees: (none)
    0x423846: mov      r13d, 8
    0x42384c: mov      esi, 8
    0x423851: mov      rdi, rbp
    0x423854: call     qword ptr [rip + 0x61b96]

; --- Block 0x42385a [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42385a: test     rax, rax
    0x42385d: je       0x423825

; --- Block 0x42385f [BODY] 3 insns, callees: (none)
    0x42385f: mov      r14, rax
    0x423862: mov      rax, r12
    0x423865: jmp      0x42386f

; --- Block 0x423867 [BODY] 8 insns, callees: (none)
    0x423867: mov      r14d, 8
    0x42386d: xor      eax, eax
    0x42386f: mov      qword ptr [rsp + 0x10], rax
    0x423874: mov      qword ptr [rsp + 0x18], r14
    0x423879: mov      rdi, r14
    0x42387c: mov      rsi, qword ptr [rsp + 0x48]
    0x423881: mov      rdx, rbp
    0x423884: call     qword ptr [rip + 0x61b86]

; --- Block 0x42386f [BODY] 6 insns, callees: (none)
    0x42386f: mov      qword ptr [rsp + 0x10], rax
    0x423874: mov      qword ptr [rsp + 0x18], r14
    0x423879: mov      rdi, r14
    0x42387c: mov      rsi, qword ptr [rsp + 0x48]
    0x423881: mov      rdx, rbp
    0x423884: call     qword ptr [rip + 0x61b86]

; --- Block 0x42388a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42388a: mov      qword ptr [rsp + 0x20], r12
    0x42388f: cmp      r12, 2
    0x423893: jae      0x423aff

; --- Block 0x423899 [LOOP_HEADER] 5 insns, callees: (none)
    0x423899: mov      r13, r12
    0x42389c: shr      r13, 1
    0x42389f: mov      rsi, qword ptr [rsp + 0x20]
    0x4238a4: cmp      r13, rsi
    0x4238a7: jae      0x423bfa

; --- Block 0x4238ad [BODY] 5 insns, callees: (none)
    0x4238ad: mov      rax, qword ptr [rsp + 0x18]
    0x4238b2: mov      r14, qword ptr [rax + r13*8]
    0x4238b6: mov      rbx, qword ptr [rsp + 0x38]
    0x4238bb: cmp      rbx, qword ptr [rsp + 0x28]
    0x4238c0: jne      0x4238cc

; --- Block 0x4238c2 [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x4238c2: lea      rdi, [rsp + 0x28]
    0x4238c7: call     0x43fe40

; --- Block 0x4238cc [BODY] 10 insns, callees: (none)
    0x4238cc: mov      rax, qword ptr [rsp + 0x30]
    0x4238d1: mov      qword ptr [rax + rbx*8], r14
    0x4238d5: inc      rbx
    0x4238d8: mov      qword ptr [rsp + 0x38], rbx
    0x4238dd: mov      rax, r12
    0x4238e0: mov      r12, qword ptr [rsp + 0x58]
    0x4238e5: mov      qword ptr [rsp + 0x50], rax
    0x4238ea: cmp      r12, rax
    0x4238ed: mov      rbp, qword ptr [rsp + 0x48]
    0x4238f2: jbe      0x423abc

; --- Block 0x4238f8 [BODY] 4 insns, callees: (none)
    0x4238f8: lea      rax, [rip + 0x5ef89]
    0x4238ff: mov      qword ptr [rsp + 0x40], rax
    0x423904: mov      r15, qword ptr [rsp + 0x50]
    0x423909: jmp      0x42392d

; --- Block 0x423910 [LOOP_HEADER] 7 insns, callees: (none)
    0x423910: inc      r15
    0x423913: mov      rax, qword ptr [rsp + 0x30]
    0x423918: mov      qword ptr [rax + rbx*8], r14
    0x42391c: inc      rbx
    0x42391f: mov      qword ptr [rsp + 0x38], rbx
    0x423924: cmp      r15, r12
    0x423927: je       0x423abc

; --- Block 0x42392d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42392d: mov      rcx, r15
    0x423930: sub      rcx, qword ptr [rsp + 0x50]
    0x423935: cmp      rcx, r12
    0x423938: jae      0x423be4

; --- Block 0x42393e [BODY] 5 insns, callees: (none)
    0x42393e: mov      r12, qword ptr [rbp + r15*8]
    0x423943: mov      rax, qword ptr [rsp + 0x18]
    0x423948: mov      r14, qword ptr [rsp + 0x20]
    0x42394d: test     r14, r14
    0x423950: je       0x423970

; --- Block 0x423952 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423952: mov      rcx, qword ptr [rbp + rcx*8]
    0x423957: cmp      r14, 1
    0x42395b: jne      0x423990

; --- Block 0x42395d [BODY] 2 insns, callees: (none)
    0x42395d: xor      edx, edx
    0x42395f: jmp      0x4239be

; --- Block 0x423970 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423970: mov      rbx, r14
    0x423973: cmp      r14, qword ptr [rsp + 0x10]
    0x423978: je       0x423a3a

; --- Block 0x42397e [BODY] 1 insns, callees: (none)
    0x42397e: jmp      0x423a49

; --- Block 0x423990 [BODY] 12 insns, callees: (none)
    0x423990: mov      rsi, r14
    0x423993: xor      edi, edi
    0x423995: nop      word ptr cs:[rax + rax]
    0x4239a0: mov      r8, rsi
    0x4239a3: shr      r8, 1
    0x4239a6: lea      rdx, [r8 + rdi]
    0x4239aa: cmp      qword ptr [rax + rdx*8], rcx
    0x4239ae: cmova    rdx, rdi
    0x4239b2: sub      rsi, r8
    0x4239b5: mov      rdi, rdx
    0x4239b8: cmp      rsi, 1
    0x4239bc: ja       0x4239a0

; --- Block 0x4239a0 [BODY] 9 insns, callees: (none)
    0x4239a0: mov      r8, rsi
    0x4239a3: shr      r8, 1
    0x4239a6: lea      rdx, [r8 + rdi]
    0x4239aa: cmp      qword ptr [rax + rdx*8], rcx
    0x4239ae: cmova    rdx, rdi
    0x4239b2: sub      rsi, r8
    0x4239b5: mov      rdi, rdx
    0x4239b8: cmp      rsi, 1
    0x4239bc: ja       0x4239a0

; --- Block 0x4239be [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4239be: cmp      qword ptr [rax + rdx*8], rcx
    0x4239c2: jne      0x4239ef

; --- Block 0x4239c4 [BODY] 6 insns, callees: (none)
    0x4239c4: lea      rdi, [rax + rdx*8]
    0x4239c8: lea      rsi, [rdi + 8]
    0x4239cc: not      rdx
    0x4239cf: add      rdx, r14
    0x4239d2: shl      rdx, 3
    0x4239d6: call     qword ptr [rip + 0x61a6c]

; --- Block 0x4239dc [BODY] 4 insns, callees: (none)
    0x4239dc: dec      r14
    0x4239df: mov      qword ptr [rsp + 0x20], r14
    0x4239e4: mov      rax, qword ptr [rsp + 0x18]
    0x4239e9: je       0x423aae

; --- Block 0x4239ef [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4239ef: cmp      r14, 1
    0x4239f3: jne      0x423a00

; --- Block 0x4239f5 [BODY] 2 insns, callees: (none)
    0x4239f5: xor      ebx, ebx
    0x4239f7: jmp      0x423a2b

; --- Block 0x423a00 [BODY] 11 insns, callees: (none)
    0x423a00: mov      rcx, r14
    0x423a03: xor      ebx, ebx
    0x423a05: nop      word ptr cs:[rax + rax]
    0x423a10: mov      rdx, rcx
    0x423a13: shr      rdx, 1
    0x423a16: lea      rsi, [rdx + rbx]
    0x423a1a: cmp      qword ptr [rax + rsi*8], r12
    0x423a1e: cmovb    rbx, rsi
    0x423a22: sub      rcx, rdx
    0x423a25: cmp      rcx, 1
    0x423a29: ja       0x423a10

; --- Block 0x423a10 [BODY] 8 insns, callees: (none)
    0x423a10: mov      rdx, rcx
    0x423a13: shr      rdx, 1
    0x423a16: lea      rsi, [rdx + rbx]
    0x423a1a: cmp      qword ptr [rax + rsi*8], r12
    0x423a1e: cmovb    rbx, rsi
    0x423a22: sub      rcx, rdx
    0x423a25: cmp      rcx, 1
    0x423a29: ja       0x423a10

; --- Block 0x423a2b [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423a2b: cmp      qword ptr [rax + rbx*8], r12
    0x423a2f: adc      rbx, 0
    0x423a33: cmp      r14, qword ptr [rsp + 0x10]
    0x423a38: jne      0x423a49

; --- Block 0x423a3a [LOOP_HEADER] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x423a3a: lea      rdi, [rsp + 0x10]
    0x423a3f: call     0x43fe40

; --- Block 0x423a44 [BODY] 5 insns, callees: (none)
    0x423a44: mov      rax, qword ptr [rsp + 0x18]
    0x423a49: lea      rbp, [rax + rbx*8]
    0x423a4d: mov      rdx, r14
    0x423a50: sub      rdx, rbx
    0x423a53: jbe      0x423a66

; --- Block 0x423a49 [LOOP_HEADER] 4 insns, callees: (none)
    0x423a49: lea      rbp, [rax + rbx*8]
    0x423a4d: mov      rdx, r14
    0x423a50: sub      rdx, rbx
    0x423a53: jbe      0x423a66

; --- Block 0x423a55 [BODY] 4 insns, callees: (none)
    0x423a55: lea      rdi, [rbp + 8]
    0x423a59: shl      rdx, 3
    0x423a5d: mov      rsi, rbp
    0x423a60: call     qword ptr [rip + 0x619e2]

; --- Block 0x423a66 [BODY] 5 insns, callees: (none)
    0x423a66: mov      qword ptr [rbp], r12
    0x423a6a: lea      rsi, [r14 + 1]
    0x423a6e: mov      qword ptr [rsp + 0x20], rsi
    0x423a73: cmp      r13, r14
    0x423a76: ja       0x423bd6

; --- Block 0x423a7c [BODY] 7 insns, callees: (none)
    0x423a7c: mov      rax, qword ptr [rsp + 0x18]
    0x423a81: mov      r14, qword ptr [rax + r13*8]
    0x423a85: mov      rbx, qword ptr [rsp + 0x38]
    0x423a8a: cmp      rbx, qword ptr [rsp + 0x28]
    0x423a8f: mov      r12, qword ptr [rsp + 0x58]
    0x423a94: mov      rbp, qword ptr [rsp + 0x48]
    0x423a99: jne      0x423910

; --- Block 0x423a9f [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x423a9f: lea      rdi, [rsp + 0x28]
    0x423aa4: call     0x43fe40

; --- Block 0x423aa9 [BODY] 1 insns, callees: (none)
    0x423aa9: jmp      0x423910

; --- Block 0x423aae [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423aae: xor      r14d, r14d
    0x423ab1: xor      ebx, ebx
    0x423ab3: cmp      r14, qword ptr [rsp + 0x10]
    0x423ab8: je       0x423a3a

; --- Block 0x423aba [BODY] 1 insns, callees: (none)
    0x423aba: jmp      0x423a49

; --- Block 0x423abc [BODY] 8 insns, callees: (none)
    0x423abc: mov      rax, qword ptr [rsp + 0x38]
    0x423ac1: mov      rdi, qword ptr [rsp + 0x60]
    0x423ac6: mov      qword ptr [rdi + 0x10], rax
    0x423aca: movups   xmm0, xmmword ptr [rsp + 0x28]
    0x423acf: movups   xmmword ptr [rdi], xmm0
    0x423ad2: mov      rsi, qword ptr [rsp + 0x10]
    0x423ad7: test     rsi, rsi
    0x423ada: je       0x42379e

; --- Block 0x423ae0 [BODY] 5 insns, callees: (none)
    0x423ae0: shl      rsi, 3
    0x423ae4: mov      rbx, rdi
    0x423ae7: mov      rdi, qword ptr [rsp + 0x18]
    0x423aec: mov      edx, 8
    0x423af1: call     qword ptr [rip + 0x61931]

; --- Block 0x423af7 [BODY] 2 insns, callees: (none)
    0x423af7: mov      rdi, rbx
    0x423afa: jmp      0x42379e

; --- Block 0x423aff [BOUNDS_CHECK] 2 insns, callees: (none)
    0x423aff: cmp      r12, 0x15
    0x423b03: jae      0x423c03

; --- Block 0x423b09 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423b09: mov      rsi, r12
    0x423b0c: test     r12b, 1
    0x423b10: jne      0x423b40

; --- Block 0x423b12 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b12: mov      rdx, qword ptr [r14]
    0x423b15: mov      rax, qword ptr [r14 + 8]
    0x423b19: cmp      rax, rdx
    0x423b1c: jae      0x423b4c

; --- Block 0x423b1e [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b1e: mov      ecx, 8
    0x423b23: mov      qword ptr [r14 + rcx], rdx
    0x423b27: cmp      rcx, 8
    0x423b2b: je       0x423b46

; --- Block 0x423b23 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423b23: mov      qword ptr [r14 + rcx], rdx
    0x423b27: cmp      rcx, 8
    0x423b2b: je       0x423b46

; --- Block 0x423b2d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b2d: mov      rdx, qword ptr [r14 + rcx - 0x10]
    0x423b32: add      rcx, -8
    0x423b36: cmp      rax, rdx
    0x423b39: jb       0x423b23

; --- Block 0x423b3b [BODY] 2 insns, callees: (none)
    0x423b3b: add      rcx, r14
    0x423b3e: jmp      0x423b49

; --- Block 0x423b40 [BODY] 2 insns, callees: (none)
    0x423b40: lea      rax, [r14 + 8]
    0x423b44: jmp      0x423b50

; --- Block 0x423b46 [BODY] 6 insns, callees: (none)
    0x423b46: mov      rcx, r14
    0x423b49: mov      qword ptr [rcx], rax
    0x423b4c: lea      rax, [r14 + 0x10]
    0x423b50: cmp      rbp, 0x10
    0x423b54: mov      r12, rsi
    0x423b57: je       0x423899

; --- Block 0x423b49 [BODY] 5 insns, callees: (none)
    0x423b49: mov      qword ptr [rcx], rax
    0x423b4c: lea      rax, [r14 + 0x10]
    0x423b50: cmp      rbp, 0x10
    0x423b54: mov      r12, rsi
    0x423b57: je       0x423899

; --- Block 0x423b4c [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b4c: lea      rax, [r14 + 0x10]
    0x423b50: cmp      rbp, 0x10
    0x423b54: mov      r12, rsi
    0x423b57: je       0x423899

; --- Block 0x423b50 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x423b50: cmp      rbp, 0x10
    0x423b54: mov      r12, rsi
    0x423b57: je       0x423899

; --- Block 0x423b5d [BODY] 3 insns, callees: (none)
    0x423b5d: lea      rcx, [r14 + r12*8]
    0x423b61: lea      rdx, [rax + 8]
    0x423b65: jmp      0x423b7e

; --- Block 0x423b67 [LOOP_HEADER] 6 insns, callees: (none)
    0x423b67: mov      r8, r14
    0x423b6a: mov      qword ptr [r8], rsi
    0x423b6d: add      rax, 0x10
    0x423b71: add      rdx, 0x10
    0x423b75: cmp      rax, rcx
    0x423b78: je       0x423899

; --- Block 0x423b6a [LOOP_HEADER] 5 insns, callees: (none)
    0x423b6a: mov      qword ptr [r8], rsi
    0x423b6d: add      rax, 0x10
    0x423b71: add      rdx, 0x10
    0x423b75: cmp      rax, rcx
    0x423b78: je       0x423899

; --- Block 0x423b6d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b6d: add      rax, 0x10
    0x423b71: add      rdx, 0x10
    0x423b75: cmp      rax, rcx
    0x423b78: je       0x423899

; --- Block 0x423b7e [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b7e: mov      rdi, qword ptr [rax - 8]
    0x423b82: mov      rsi, qword ptr [rax]
    0x423b85: cmp      rsi, rdi
    0x423b88: jae      0x423bad

; --- Block 0x423b8a [BODY] 5 insns, callees: (none)
    0x423b8a: mov      r9, rax
    0x423b8d: lea      r8, [r9 - 8]
    0x423b91: mov      qword ptr [r9], rdi
    0x423b94: cmp      r8, r14
    0x423b97: je       0x423ba7

; --- Block 0x423b8d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b8d: lea      r8, [r9 - 8]
    0x423b91: mov      qword ptr [r9], rdi
    0x423b94: cmp      r8, r14
    0x423b97: je       0x423ba7

; --- Block 0x423b99 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423b99: mov      rdi, qword ptr [r9 - 0x10]
    0x423b9d: mov      r9, r8
    0x423ba0: cmp      rsi, rdi
    0x423ba3: jb       0x423b8d

; --- Block 0x423ba5 [BODY] 1 insns, callees: (none)
    0x423ba5: jmp      0x423baa

; --- Block 0x423ba7 [BODY] 6 insns, callees: (none)
    0x423ba7: mov      r8, r14
    0x423baa: mov      qword ptr [r8], rsi
    0x423bad: mov      rdi, qword ptr [rax]
    0x423bb0: mov      rsi, qword ptr [rax + 8]
    0x423bb4: cmp      rsi, rdi
    0x423bb7: jae      0x423b6d

; --- Block 0x423baa [BODY] 5 insns, callees: (none)
    0x423baa: mov      qword ptr [r8], rsi
    0x423bad: mov      rdi, qword ptr [rax]
    0x423bb0: mov      rsi, qword ptr [rax + 8]
    0x423bb4: cmp      rsi, rdi
    0x423bb7: jae      0x423b6d

; --- Block 0x423bad [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423bad: mov      rdi, qword ptr [rax]
    0x423bb0: mov      rsi, qword ptr [rax + 8]
    0x423bb4: cmp      rsi, rdi
    0x423bb7: jae      0x423b6d

; --- Block 0x423bb9 [BODY] 5 insns, callees: (none)
    0x423bb9: mov      r9, rdx
    0x423bbc: lea      r8, [r9 - 8]
    0x423bc0: mov      qword ptr [r9], rdi
    0x423bc3: cmp      r8, r14
    0x423bc6: je       0x423b67

; --- Block 0x423bbc [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423bbc: lea      r8, [r9 - 8]
    0x423bc0: mov      qword ptr [r9], rdi
    0x423bc3: cmp      r8, r14
    0x423bc6: je       0x423b67

; --- Block 0x423bc8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x423bc8: mov      rdi, qword ptr [r9 - 0x10]
    0x423bcc: mov      r9, r8
    0x423bcf: cmp      rsi, rdi
    0x423bd2: jb       0x423bbc

; --- Block 0x423bd4 [BODY] 1 insns, callees: (none)
    0x423bd4: jmp      0x423b6a

; --- Block 0x423bd6 [BODY] 3 insns, callees: (none)
    0x423bd6: lea      rax, [rip + 0x5ecc3]
    0x423bdd: mov      qword ptr [rsp + 0x40], rax
    0x423be2: jmp      0x423bea

; --- Block 0x423bdd [LOOP_HEADER] 2 insns, callees: (none)
    0x423bdd: mov      qword ptr [rsp + 0x40], rax
    0x423be2: jmp      0x423bea

; --- Block 0x423be4 [BODY] 5 insns, callees: (none)
    0x423be4: mov      r13, r12
    0x423be7: mov      rsi, r12
    0x423bea: mov      rdi, r13
    0x423bed: mov      rdx, qword ptr [rsp + 0x40]
    0x423bf2: call     qword ptr [rip + 0x61838]

; --- Block 0x423bea [BODY] 3 insns, callees: (none)
    0x423bea: mov      rdi, r13
    0x423bed: mov      rdx, qword ptr [rsp + 0x40]
    0x423bf2: call     qword ptr [rip + 0x61838]

; --- Block 0x423bfa [BODY] 2 insns, callees: (none)
    0x423bfa: lea      rax, [rip + 0x5ec6f]
    0x423c01: jmp      0x423bdd

; --- Block 0x423c03 [BODY] 4 insns, callees: core::slice::sort::stable::driftsort_main
    0x423c03: lea      rdx, [rsp + 0xf]
    0x423c08: mov      rdi, r14
    0x423c0b: mov      rsi, r12
    0x423c0e: call     0x440620

; --- Block 0x423c13 [BODY] 1 insns, callees: (none)
    0x423c13: jmp      0x423899

```

**Hungarian matching result** (mean similarity: 0.793):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x447b4a` | BODY | `0x42397e` | BODY | 1.000 | GOOD |
| `0x447ba7` | BODY | `0x423aa9` | BODY | 1.000 | GOOD |
| `0x447d1f` | BODY | `0x423aba` | BODY | 1.000 | GOOD |
| `0x447d9d` | BODY | `0x4237e0` | BODY | 1.000 | GOOD |
| `0x447e9a` | BODY | `0x423bd4` | BODY | 1.000 | GOOD |
| `0x448004` | BODY | `0x423ba5` | BODY | 1.000 | GOOD |
| `0x44801f` | BODY | `0x423bdd` | LOOP_HEADER | 1.000 | GOOD |
| `0x44808e` | BODY | `0x423c13` | BODY | 1.000 | GOOD |
| `0x447b3d` | LOOP_HEADER | `0x4237bf` | BODY | 0.993 | GOOD |
| `0x447d21` | BODY | `0x423a9f` | BODY | 0.991 | GOOD |
| `0x447fc7` | LOOP_HEADER | `0x4238c2` | BODY | 0.991 | GOOD |
| `0x447df6` | LOOP_HEADER | `0x423a3a` | LOOP_HEADER | 0.987 | GOOD |
| `0x447d65` | BODY | `0x42377b` | LOOP_HEADER | 0.981 | GOOD |
| `0x447dbb` | BODY | `0x423825` | LOOP_HEADER | 0.981 | GOOD |
| `0x448072` | BODY | `0x423af7` | BODY | 0.980 | GOOD |
| `0x447b4f` | BOUNDS_CHECK | `0x4237b0` | BOUNDS_CHECK | 0.968 | GOOD |
| `0x447eb4` | BOUNDS_CHECK | `0x423b7e` | BOUNDS_CHECK | 0.959 | GOOD |
| `0x447e03` | BODY | `0x42385f` | BODY | 0.955 | GOOD |
| `0x447e0f` | BODY | `0x423ba7` | BODY | 0.945 | GOOD |
| `0x448008` | BODY | `0x423c03` | BODY | 0.940 | GOOD |
| `0x447f9f` | BODY | `0x42393e` | BODY | 0.920 | GOOD |
| `0x447edc` | BODY | `0x423a7c` | BODY | 0.906 | GOOD |
| `0x447b87` | ITERATOR_STATE | `0x423910` | LOOP_HEADER | 0.889 | GOOD |
| `0x447f93` | BODY | `0x423bd6` | BODY | 0.864 | GOOD |
| `0x448026` | BODY | `0x42386f` | BODY | 0.853 | GOOD |
| `0x447ec8` | BODY | `0x423bea` | BODY | 0.839 | GOOD |
| `0x447fe0` | BODY | `0x423be4` | BODY | 0.818 | GOOD |
| `0x447b64` | BODY | `0x42392d` | BOUNDS_CHECK | 0.810 | GOOD |
| `0x447f7c` | BODY | `0x423822` | BODY | 0.807 | GOOD |
| `0x447e37` | BODY | `0x4238cc` | BODY | 0.771 | GOOD |
| `0x447c84` | BODY | `0x423779` | BODY | 0.751 | GOOD |
| `0x447bb6` | BODY | `0x423b8d` | BOUNDS_CHECK | 0.749 | GOOD |
| `0x447f5a` | BODY | `0x423a66` | BODY | 0.748 | GOOD |
| `0x447f09` | BODY | `0x423bb9` | BODY | 0.746 | GOOD |
| `0x447d02` | BODY | `0x423a49` | LOOP_HEADER | 0.740 | GOOD |
| `0x447dd0` | BODY | `0x423836` | BOUNDS_CHECK | 0.735 | GOOD |
| `0x448079` | BODY | `0x423bbc` | BOUNDS_CHECK | 0.731 | GOOD |
| `0x447e66` | DROP_GLUE | `0x423abc` | BODY | 0.730 | GOOD |
| `0x447fd4` | BODY | `0x423952` | BOUNDS_CHECK | 0.725 | GOOD |
| `0x447f4e` | BODY | `0x423b09` | BOUNDS_CHECK | 0.722 | GOOD |
| `0x447d2e` | BODY | `0x423970` | BOUNDS_CHECK | 0.719 | GOOD |
| `0x447bd3` | BODY | `0x423b12` | BOUNDS_CHECK | 0.717 | GOOD |
| `0x448053` | BODY | `0x423899` | LOOP_HEADER | 0.717 | GOOD |
| `0x447caa` | BODY | `0x4238ad` | BODY | 0.711 | GOOD |
| `0x447da4` | BODY | `0x4239dc` | BODY | 0.691 | PARTIAL |
| `0x447f28` | BODY | `0x423a44` | BODY | 0.687 | PARTIAL |
| `0x447d7e` | BODY | `0x423baa` | BODY | 0.671 | PARTIAL |
| `0x447ec6` | BODY | `0x423840` | BODY | 0.662 | PARTIAL |
| `0x44804f` | BODY | `0x42395d` | BODY | 0.653 | PARTIAL |
| `0x447ba9` | BODY | `0x4239be` | BOUNDS_CHECK | 0.649 | PARTIAL |
| `0x447ccc` | BODY | `0x42385a` | BOUNDS_CHECK | 0.649 | PARTIAL |
| `0x447d7a` | BODY | `0x4239f5` | BODY | 0.647 | PARTIAL |
| `0x447e64` | BODY | `0x423bfa` | BODY | 0.647 | PARTIAL |
| `0x448006` | BODY | `0x423b3b` | BODY | 0.647 | PARTIAL |
| `0x447db9` | BODY | `0x423b40` | BODY | 0.645 | PARTIAL |
| `0x447ddc` | BODY | `0x423b8a` | BODY | 0.635 | PARTIAL |
| `0x447d7c` | BODY | `0x423b5d` | BODY | 0.567 | PARTIAL |
| `0x447ae0` | BODY | `0x423990` | BODY | 0.554 | PARTIAL |
| `0x447e9c` | EPILOGUE | `0x423b2d` | BOUNDS_CHECK | 0.554 | PARTIAL |
| `0x447ea4` | EPILOGUE | `0x42388a` | BOUNDS_CHECK | 0.518 | PARTIAL |
| `0x448090` | BODY | `0x4238f8` | BODY | 0.502 | PARTIAL |
| `0x447f07` | BODY | `0x4239ef` | BOUNDS_CHECK | 0.491 | PARTIAL |
| `0x448051` | BODY | `0x4237db` | BOUNDS_CHECK | 0.491 | PARTIAL |
| — | — | `0x423730` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423747` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423787` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42379e` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4237c8` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4237e5` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4237ed` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423846` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423867` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4239a0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4239c4` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423a00` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423a10` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423a2b` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423a55` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423aae` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423ae0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423aff` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b1e` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b23` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b46` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b49` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b4c` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b50` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b67` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b6a` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b6d` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423b99` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423bad` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x423bc8` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |

### C `bc_12` — O0: 27 blocks, O2: 28 blocks

**O0 blocks** (27 total):

```asm
; --- Block 0x402323 [BODY] 11 insns, callees: (none)
    0x402323: push     rbp
    0x402324: mov      rbp, rsp
    0x402327: sub      rsp, 0xa0
    0x40232e: mov      qword ptr [rbp - 0x88], rdi
    0x402335: mov      qword ptr [rbp - 0x90], rsi
    0x40233c: mov      qword ptr [rbp - 0x98], rdx
    0x402343: mov      qword ptr [rbp - 0xa0], rcx
    0x40234a: mov      rax, qword ptr [rbp - 0xa0]
    0x402351: mov      qword ptr [rax], 0
    0x402358: cmp      qword ptr [rbp - 0x98], 0
    0x402360: je       0x402372

; --- Block 0x402362 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x402362: mov      rax, qword ptr [rbp - 0x98]
    0x402369: cmp      rax, qword ptr [rbp - 0x90]
    0x402370: jbe      0x40237c

; --- Block 0x402372 [BODY] 2 insns, callees: (none)
    0x402372: mov      eax, 0
    0x402377: jmp      0x4026b9

; --- Block 0x40237c [BODY] 8 insns, callees: sub_4010f0
    0x40237c: mov      rax, qword ptr [rbp - 0x90]
    0x402383: sub      rax, qword ptr [rbp - 0x98]
    0x40238a: add      rax, 1
    0x40238e: mov      qword ptr [rbp - 0x30], rax
    0x402392: mov      rax, qword ptr [rbp - 0x30]
    0x402396: shl      rax, 3
    0x40239a: mov      rdi, rax
    0x40239d: call     0x4010f0

; --- Block 0x4023a2 [BODY] 5 insns, callees: sub_4010f0
    0x4023a2: mov      qword ptr [rbp - 0x38], rax
    0x4023a6: mov      rax, qword ptr [rbp - 0x98]
    0x4023ad: shl      rax, 3
    0x4023b1: mov      rdi, rax
    0x4023b4: call     0x4010f0

; --- Block 0x4023b9 [BODY] 8 insns, callees: sub_4010e0
    0x4023b9: mov      qword ptr [rbp - 0x40], rax
    0x4023bd: mov      rax, qword ptr [rbp - 0x98]
    0x4023c4: lea      rdx, [rax*8]
    0x4023cc: mov      rcx, qword ptr [rbp - 0x88]
    0x4023d3: mov      rax, qword ptr [rbp - 0x40]
    0x4023d7: mov      rsi, rcx
    0x4023da: mov      rdi, rax
    0x4023dd: call     0x4010e0

; --- Block 0x4023e2 [BODY] 6 insns, callees: sub_401060
    0x4023e2: mov      rsi, qword ptr [rbp - 0x98]
    0x4023e9: mov      rax, qword ptr [rbp - 0x40]
    0x4023ed: mov      ecx, 0x401278
    0x4023f2: mov      edx, 8
    0x4023f7: mov      rdi, rax
    0x4023fa: call     0x401060

; --- Block 0x4023ff [BODY] 11 insns, callees: (none)
    0x4023ff: mov      rax, qword ptr [rbp - 0x98]
    0x402406: shr      rax, 1
    0x402409: lea      rdx, [rax*8]
    0x402411: mov      rax, qword ptr [rbp - 0x40]
    0x402415: add      rax, rdx
    0x402418: mov      rdx, qword ptr [rax]
    0x40241b: mov      rax, qword ptr [rbp - 0x38]
    0x40241f: mov      qword ptr [rax], rdx
    0x402422: mov      rax, qword ptr [rbp - 0x98]
    0x402429: mov      qword ptr [rbp - 8], rax
    0x40242d: jmp      0x40268a

; --- Block 0x402432 [LOOP_HEADER] 18 insns, callees: (none)
    0x402432: mov      rax, qword ptr [rbp - 8]
    0x402436: sub      rax, qword ptr [rbp - 0x98]
    0x40243d: lea      rdx, [rax*8]
    0x402445: mov      rax, qword ptr [rbp - 0x88]
    0x40244c: add      rax, rdx
    0x40244f: mov      rax, qword ptr [rax]
    0x402452: mov      qword ptr [rbp - 0x48], rax
    0x402456: mov      rax, qword ptr [rbp - 8]
    0x40245a: lea      rdx, [rax*8]
    0x402462: mov      rax, qword ptr [rbp - 0x88]
    0x402469: add      rax, rdx
    0x40246c: mov      rax, qword ptr [rax]
    ... +6 more instructions

; --- Block 0x402490 [LOOP_HEADER] 14 insns, callees: (none)
    0x402490: mov      rax, qword ptr [rbp - 0x18]
    0x402494: sub      rax, qword ptr [rbp - 0x10]
    0x402498: shr      rax, 1
    0x40249b: mov      rdx, rax
    0x40249e: mov      rax, qword ptr [rbp - 0x10]
    0x4024a2: add      rax, rdx
    0x4024a5: mov      qword ptr [rbp - 0x78], rax
    0x4024a9: mov      rax, qword ptr [rbp - 0x78]
    0x4024ad: lea      rdx, [rax*8]
    0x4024b5: mov      rax, qword ptr [rbp - 0x40]
    0x4024b9: add      rax, rdx
    0x4024bc: mov      rax, qword ptr [rax]
    ... +2 more instructions

; --- Block 0x4024c5 [BODY] 4 insns, callees: (none)
    0x4024c5: mov      rax, qword ptr [rbp - 0x78]
    0x4024c9: add      rax, 1
    0x4024cd: mov      qword ptr [rbp - 0x10], rax
    0x4024d1: jmp      0x4024db

; --- Block 0x4024d3 [BODY] 5 insns, callees: (none)
    0x4024d3: mov      rax, qword ptr [rbp - 0x78]
    0x4024d7: mov      qword ptr [rbp - 0x18], rax
    0x4024db: mov      rax, qword ptr [rbp - 0x10]
    0x4024df: cmp      rax, qword ptr [rbp - 0x18]
    0x4024e3: jb       0x402490

; --- Block 0x4024db [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4024db: mov      rax, qword ptr [rbp - 0x10]
    0x4024df: cmp      rax, qword ptr [rbp - 0x18]
    0x4024e3: jb       0x402490

; --- Block 0x4024e5 [BODY] 5 insns, callees: (none)
    0x4024e5: mov      rax, qword ptr [rbp - 0x10]
    0x4024e9: mov      qword ptr [rbp - 0x58], rax
    0x4024ed: mov      rax, qword ptr [rbp - 0x58]
    0x4024f1: cmp      rax, qword ptr [rbp - 0x98]
    0x4024f8: jae      0x402562

; --- Block 0x4024fa [BODY] 7 insns, callees: (none)
    0x4024fa: mov      rax, qword ptr [rbp - 0x58]
    0x4024fe: lea      rdx, [rax*8]
    0x402506: mov      rax, qword ptr [rbp - 0x40]
    0x40250a: add      rax, rdx
    0x40250d: mov      rax, qword ptr [rax]
    0x402510: cmp      qword ptr [rbp - 0x48], rax
    0x402514: jne      0x402562

; --- Block 0x402516 [BODY] 16 insns, callees: sub_401100
    0x402516: mov      rax, qword ptr [rbp - 0x98]
    0x40251d: sub      rax, qword ptr [rbp - 0x58]
    0x402521: sub      rax, 1
    0x402525: lea      rdx, [rax*8]
    0x40252d: mov      rax, qword ptr [rbp - 0x58]
    0x402531: add      rax, 1
    0x402535: lea      rcx, [rax*8]
    0x40253d: mov      rax, qword ptr [rbp - 0x40]
    0x402541: add      rcx, rax
    0x402544: mov      rax, qword ptr [rbp - 0x58]
    0x402548: lea      rsi, [rax*8]
    0x402550: mov      rax, qword ptr [rbp - 0x40]
    ... +4 more instructions

; --- Block 0x402562 [BODY] 8 insns, callees: (none)
    0x402562: mov      rax, qword ptr [rbp - 0x98]
    0x402569: sub      rax, 1
    0x40256d: mov      qword ptr [rbp - 0x60], rax
    0x402571: mov      qword ptr [rbp - 0x68], 0
    0x402579: mov      qword ptr [rbp - 0x20], 0
    0x402581: mov      rax, qword ptr [rbp - 0x60]
    0x402585: mov      qword ptr [rbp - 0x28], rax
    0x402589: jmp      0x4025d6

; --- Block 0x40258b [LOOP_HEADER] 14 insns, callees: (none)
    0x40258b: mov      rax, qword ptr [rbp - 0x28]
    0x40258f: sub      rax, qword ptr [rbp - 0x20]
    0x402593: shr      rax, 1
    0x402596: mov      rdx, rax
    0x402599: mov      rax, qword ptr [rbp - 0x20]
    0x40259d: add      rax, rdx
    0x4025a0: mov      qword ptr [rbp - 0x70], rax
    0x4025a4: mov      rax, qword ptr [rbp - 0x70]
    0x4025a8: lea      rdx, [rax*8]
    0x4025b0: mov      rax, qword ptr [rbp - 0x40]
    0x4025b4: add      rax, rdx
    0x4025b7: mov      rax, qword ptr [rax]
    ... +2 more instructions

; --- Block 0x4025c0 [BODY] 4 insns, callees: (none)
    0x4025c0: mov      rax, qword ptr [rbp - 0x70]
    0x4025c4: add      rax, 1
    0x4025c8: mov      qword ptr [rbp - 0x20], rax
    0x4025cc: jmp      0x4025d6

; --- Block 0x4025ce [BODY] 5 insns, callees: (none)
    0x4025ce: mov      rax, qword ptr [rbp - 0x70]
    0x4025d2: mov      qword ptr [rbp - 0x28], rax
    0x4025d6: mov      rax, qword ptr [rbp - 0x20]
    0x4025da: cmp      rax, qword ptr [rbp - 0x28]
    0x4025de: jb       0x40258b

; --- Block 0x4025d6 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4025d6: mov      rax, qword ptr [rbp - 0x20]
    0x4025da: cmp      rax, qword ptr [rbp - 0x28]
    0x4025de: jb       0x40258b

; --- Block 0x4025e0 [BODY] 17 insns, callees: sub_401100
    0x4025e0: mov      rax, qword ptr [rbp - 0x20]
    0x4025e4: mov      qword ptr [rbp - 0x68], rax
    0x4025e8: mov      rax, qword ptr [rbp - 0x60]
    0x4025ec: sub      rax, qword ptr [rbp - 0x68]
    0x4025f0: lea      rdx, [rax*8]
    0x4025f8: mov      rax, qword ptr [rbp - 0x68]
    0x4025fc: lea      rcx, [rax*8]
    0x402604: mov      rax, qword ptr [rbp - 0x40]
    0x402608: add      rcx, rax
    0x40260b: mov      rax, qword ptr [rbp - 0x68]
    0x40260f: add      rax, 1
    0x402613: lea      rsi, [rax*8]
    ... +5 more instructions

; --- Block 0x40262d [BODY] 23 insns, callees: (none)
    0x40262d: mov      rax, qword ptr [rbp - 0x68]
    0x402631: lea      rdx, [rax*8]
    0x402639: mov      rax, qword ptr [rbp - 0x40]
    0x40263d: add      rdx, rax
    0x402640: mov      rax, qword ptr [rbp - 0x50]
    0x402644: mov      qword ptr [rdx], rax
    0x402647: mov      rax, qword ptr [rbp - 0x98]
    0x40264e: shr      rax, 1
    0x402651: lea      rdx, [rax*8]
    0x402659: mov      rax, qword ptr [rbp - 0x40]
    0x40265d: lea      rcx, [rdx + rax]
    0x402661: mov      rax, qword ptr [rbp - 8]
    ... +11 more instructions

; --- Block 0x40268a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40268a: mov      rax, qword ptr [rbp - 8]
    0x40268e: cmp      rax, qword ptr [rbp - 0x90]
    0x402695: jb       0x402432

; --- Block 0x40269b [BODY] 3 insns, callees: sub_401030
    0x40269b: mov      rax, qword ptr [rbp - 0x40]
    0x40269f: mov      rdi, rax
    0x4026a2: call     0x401030

; --- Block 0x4026a7 [BODY] 6 insns, callees: (none)
    0x4026a7: mov      rax, qword ptr [rbp - 0xa0]
    0x4026ae: mov      rdx, qword ptr [rbp - 0x30]
    0x4026b2: mov      qword ptr [rax], rdx
    0x4026b5: mov      rax, qword ptr [rbp - 0x38]
    0x4026b9: leave    
    0x4026ba: ret      

; --- Block 0x4026b9 [BODY] 2 insns, callees: (none)
    0x4026b9: leave    
    0x4026ba: ret      

```

**O2 blocks** (28 total):

```asm
; --- Block 0x403fc0 [BODY] 12 insns, callees: (none)
    0x403fc0: push     r15
    0x403fc2: push     r14
    0x403fc4: push     r13
    0x403fc6: push     r12
    0x403fc8: push     rbp
    0x403fc9: push     rbx
    0x403fca: sub      rsp, 0x48
    0x403fce: mov      qword ptr [rcx], 0
    0x403fd5: mov      qword ptr [rsp + 8], rdi
    0x403fda: mov      qword ptr [rsp + 0x30], rcx
    0x403fdf: test     rdx, rdx
    0x403fe2: je       0x4041db

; --- Block 0x403fe8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x403fe8: mov      r12, rsi
    0x403feb: mov      rbx, rdx
    0x403fee: cmp      rdx, rsi
    0x403ff1: ja       0x4041db

; --- Block 0x403ff7 [BODY] 5 insns, callees: sub_401100
    0x403ff7: lea      rax, [rsi + 1]
    0x403ffb: sub      rax, rdx
    0x403ffe: lea      rdi, [rax*8]
    0x404006: mov      qword ptr [rsp + 0x38], rax
    0x40400b: call     0x401100

; --- Block 0x404010 [BODY] 6 insns, callees: sub_401100
    0x404010: lea      r8, [rbx*8]
    0x404018: mov      rdi, r8
    0x40401b: mov      qword ptr [rsp + 0x10], r8
    0x404020: mov      r15, rax
    0x404023: mov      qword ptr [rsp + 0x28], rax
    0x404028: call     0x401100

; --- Block 0x40402d [BODY] 5 insns, callees: sub_4010f0
    0x40402d: mov      rdx, qword ptr [rsp + 0x10]
    0x404032: mov      rsi, qword ptr [rsp + 8]
    0x404037: mov      rbp, rax
    0x40403a: mov      rdi, rax
    0x40403d: call     0x4010f0

; --- Block 0x404042 [BODY] 5 insns, callees: sub_401060
    0x404042: mov      ecx, 0x4022e0
    0x404047: mov      rsi, rbx
    0x40404a: mov      rdi, rbp
    0x40404d: mov      edx, 8
    0x404052: call     0x401060

; --- Block 0x404057 [BODY] 9 insns, callees: (none)
    0x404057: mov      rax, rbx
    0x40405a: mov      r10, qword ptr [rsp + 8]
    0x40405f: mov      r8, qword ptr [rsp + 0x10]
    0x404064: shr      rax, 1
    0x404067: cmp      rbx, r12
    0x40406a: lea      r13, [rbp + rax*8]
    0x40406f: mov      rax, qword ptr [r13]
    0x404073: mov      qword ptr [r15], rax
    0x404076: jae      0x404174

; --- Block 0x40407c [BODY] 17 insns, callees: (none)
    0x40407c: lea      rax, [rbx - 1]
    0x404080: lea      r14, [r10 + r8]
    0x404084: neg      r8
    0x404087: mov      qword ptr [rsp + 0x10], rbx
    0x40408c: mov      qword ptr [rsp + 8], rax
    0x404091: mov      rax, qword ptr [rsp + 0x28]
    0x404096: mov      qword ptr [rsp + 0x18], r8
    0x40409b: lea      r15, [rax + 8]
    0x40409f: lea      rax, [r10 + r12*8]
    0x4040a3: mov      qword ptr [rsp + 0x20], rax
    0x4040a8: nop      dword ptr [rax + rax]
    0x4040b0: mov      rax, qword ptr [rsp + 0x18]
    ... +5 more instructions

; --- Block 0x4040b0 [LOOP_HEADER] 6 insns, callees: (none)
    0x4040b0: mov      rax, qword ptr [rsp + 0x18]
    0x4040b5: mov      rbx, qword ptr [r14]
    0x4040b8: xor      edx, edx
    0x4040ba: mov      rsi, qword ptr [rsp + 0x10]
    0x4040bf: mov      rdi, qword ptr [r14 + rax]
    0x4040c3: jmp      0x4040e2

; --- Block 0x4040c8 [LOOP_HEADER] 6 insns, callees: (none)
    0x4040c8: mov      rax, rsi
    0x4040cb: sub      rax, rdx
    0x4040ce: shr      rax, 1
    0x4040d1: add      rax, rdx
    0x4040d4: cmp      qword ptr [rbp + rax*8], rdi
    0x4040d9: jb       0x4041a0

; --- Block 0x4040df [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4040df: mov      rsi, rax
    0x4040e2: cmp      rdx, rsi
    0x4040e5: jb       0x4040c8

; --- Block 0x4040e2 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4040e2: cmp      rdx, rsi
    0x4040e5: jb       0x4040c8

; --- Block 0x4040e7 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4040e7: cmp      rdx, qword ptr [rsp + 0x10]
    0x4040ec: jae      0x404104

; --- Block 0x4040ee [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4040ee: lea      rax, [rdx*8]
    0x4040f6: lea      r10, [rbp + rax]
    0x4040fb: cmp      qword ptr [r10], rdi
    0x4040fe: je       0x4041b9

; --- Block 0x404104 [LOOP_HEADER] 3 insns, callees: (none)
    0x404104: mov      rdx, qword ptr [rsp + 8]
    0x404109: xor      esi, esi
    0x40410b: jmp      0x40412a

; --- Block 0x404110 [LOOP_HEADER] 6 insns, callees: (none)
    0x404110: mov      rax, rdx
    0x404113: sub      rax, rsi
    0x404116: shr      rax, 1
    0x404119: add      rax, rsi
    0x40411c: cmp      qword ptr [rbp + rax*8], rbx
    0x404121: jb       0x4041b0

; --- Block 0x404127 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x404127: mov      rdx, rax
    0x40412a: cmp      rsi, rdx
    0x40412d: jb       0x404110

; --- Block 0x40412a [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40412a: cmp      rsi, rdx
    0x40412d: jb       0x404110

; --- Block 0x40412f [BODY] 10 insns, callees: sub_401110
    0x40412f: mov      rdx, qword ptr [rsp + 8]
    0x404134: lea      rax, [rsi*8]
    0x40413c: add      r14, 8
    0x404140: add      r15, 8
    0x404144: lea      r12, [rbp + rax]
    0x404149: lea      rdi, [rbp + rax + 8]
    0x40414e: sub      rdx, rsi
    0x404151: mov      rsi, r12
    0x404154: shl      rdx, 3
    0x404158: call     0x401110

; --- Block 0x40415d [BODY] 5 insns, callees: (none)
    0x40415d: mov      qword ptr [r12], rbx
    0x404161: mov      rax, qword ptr [r13]
    0x404165: mov      qword ptr [r15 - 8], rax
    0x404169: cmp      r14, qword ptr [rsp + 0x20]
    0x40416e: jne      0x4040b0

; --- Block 0x404174 [BODY] 2 insns, callees: sub_401030
    0x404174: mov      rdi, rbp
    0x404177: call     0x401030

; --- Block 0x40417c [BODY] 12 insns, callees: (none)
    0x40417c: mov      rax, qword ptr [rsp + 0x30]
    0x404181: mov      rcx, qword ptr [rsp + 0x38]
    0x404186: mov      qword ptr [rax], rcx
    0x404189: mov      rax, qword ptr [rsp + 0x28]
    0x40418e: add      rsp, 0x48
    0x404192: pop      rbx
    0x404193: pop      rbp
    0x404194: pop      r12
    0x404196: pop      r13
    0x404198: pop      r14
    0x40419a: pop      r15
    0x40419c: ret      

; --- Block 0x404189 [LOOP_HEADER] 9 insns, callees: (none)
    0x404189: mov      rax, qword ptr [rsp + 0x28]
    0x40418e: add      rsp, 0x48
    0x404192: pop      rbx
    0x404193: pop      rbp
    0x404194: pop      r12
    0x404196: pop      r13
    0x404198: pop      r14
    0x40419a: pop      r15
    0x40419c: ret      

; --- Block 0x4041a0 [BODY] 2 insns, callees: (none)
    0x4041a0: lea      rdx, [rax + 1]
    0x4041a4: jmp      0x4040e2

; --- Block 0x4041b0 [BODY] 2 insns, callees: (none)
    0x4041b0: lea      rsi, [rax + 1]
    0x4041b4: jmp      0x40412a

; --- Block 0x4041b9 [BODY] 6 insns, callees: sub_401110
    0x4041b9: mov      rsi, qword ptr [rsp + 8]
    0x4041be: mov      rdi, r10
    0x4041c1: sub      rsi, rdx
    0x4041c4: lea      rdx, [rsi*8]
    0x4041cc: lea      rsi, [rbp + rax + 8]
    0x4041d1: call     0x401110

; --- Block 0x4041d6 [BODY] 1 insns, callees: (none)
    0x4041d6: jmp      0x404104

; --- Block 0x4041db [BODY] 2 insns, callees: (none)
    0x4041db: mov      qword ptr [rsp + 0x28], 0
    0x4041e4: jmp      0x404189

```

**Hungarian matching result** (mean similarity: 0.734):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4024d3` | BODY | `0x40415d` | BODY | 1.000 | GOOD |
| `0x402372` | BODY | `0x4041db` | BODY | 0.977 | GOOD |
| `0x402362` | BOUNDS_CHECK | `0x404127` | BOUNDS_CHECK | 0.955 | GOOD |
| `0x4024db` | BOUNDS_CHECK | `0x4040df` | BOUNDS_CHECK | 0.953 | GOOD |
| `0x4023e2` | BODY | `0x404042` | BODY | 0.918 | GOOD |
| `0x40269b` | BODY | `0x404174` | BODY | 0.898 | GOOD |
| `0x4024e5` | BODY | `0x403fe8` | BOUNDS_CHECK | 0.887 | GOOD |
| `0x4025d6` | BOUNDS_CHECK | `0x4040e7` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x40268a` | BOUNDS_CHECK | `0x40412a` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x4023a2` | BODY | `0x40402d` | BODY | 0.740 | GOOD |
| `0x402490` | LOOP_HEADER | `0x404057` | BODY | 0.729 | GOOD |
| `0x4025e0` | BODY | `0x403ff7` | BODY | 0.722 | GOOD |
| `0x40258b` | LOOP_HEADER | `0x4040c8` | LOOP_HEADER | 0.720 | GOOD |
| `0x4024c5` | BODY | `0x404104` | LOOP_HEADER | 0.719 | GOOD |
| `0x402323` | BODY | `0x403fc0` | BODY | 0.705 | GOOD |
| `0x402432` | LOOP_HEADER | `0x40407c` | BODY | 0.699 | PARTIAL |
| `0x4026a7` | BODY | `0x4040b0` | LOOP_HEADER | 0.695 | PARTIAL |
| `0x402516` | BODY | `0x404010` | BODY | 0.670 | PARTIAL |
| `0x4024fa` | BODY | `0x4040ee` | BOUNDS_CHECK | 0.668 | PARTIAL |
| `0x4025ce` | BODY | `0x4040e2` | BOUNDS_CHECK | 0.660 | PARTIAL |
| `0x40262d` | BODY | `0x404110` | LOOP_HEADER | 0.654 | PARTIAL |
| `0x4026b9` | BODY | `0x4041a0` | BODY | 0.634 | PARTIAL |
| `0x40237c` | BODY | `0x40412f` | BODY | 0.634 | PARTIAL |
| `0x4023b9` | BODY | `0x4041b9` | BODY | 0.574 | PARTIAL |
| `0x4025c0` | BODY | `0x4041b0` | BODY | 0.545 | PARTIAL |
| `0x4023ff` | BODY | `0x40417c` | BODY | 0.496 | PARTIAL |
| `0x402562` | BODY | `0x4041d6` | BODY | 0.466 | PARTIAL |
| — | — | `0x404189` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |

---

## Function `em_06`

### Rust `em_06` — O0: 1 blocks, O2: 1 blocks

**O0 blocks** (1 total):

```asm
; --- Block 0x44b7b0 [BODY] 21 insns, callees: (none)
    0x44b7b0: sub      rsp, 0x378
    0x44b7b7: mov      qword ptr [rsp + 0xe8], rsi
    0x44b7bf: mov      qword ptr [rsp + 0xf0], rdi
    0x44b7c7: mov      qword ptr [rsp + 0xf8], rdi
    0x44b7cf: mov      qword ptr [rsp + 0x2a8], rsi
    0x44b7d7: mov      byte ptr [rsp + 0x2a6], 0
    0x44b7df: mov      byte ptr [rsp + 0x2a5], 0
    0x44b7e7: mov      byte ptr [rsp + 0x2a7], 0
    0x44b7ef: mov      rax, qword ptr [rsi]
    0x44b7f2: movabs   rdx, 0x8000000000000000
    0x44b7fc: mov      rcx, rax
    0x44b7ff: add      rcx, rdx
    ... +9 more instructions

```

**O2 blocks** (1 total):

```asm
; --- Block 0x4253b0 [BODY] 18 insns, callees: (none)
    0x4253b0: push     rbp
    0x4253b1: push     r15
    0x4253b3: push     r14
    0x4253b5: push     r12
    0x4253b7: push     rbx
    0x4253b8: sub      rsp, 0xc0
    0x4253bf: movabs   r15, 0x8000000000000000
    0x4253c9: mov      rax, qword ptr [rsi]
    0x4253cc: mov      rcx, rax
    0x4253cf: xor      rcx, r15
    0x4253d2: test     rax, rax
    0x4253d5: mov      eax, 4
    ... +6 more instructions

```

**Hungarian matching result** (mean similarity: 0.734):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x44b7b0` | BODY | `0x4253b0` | BODY | 0.734 | GOOD |

### C `em_06` — O0: 82 blocks, O2: 66 blocks

**O0 blocks** (82 total):

```asm
; --- Block 0x409c9a [LOOP_HEADER] 6 insns, callees: (none)
    0x409c9a: push     rbp
    0x409c9b: mov      rbp, rsp
    0x409c9e: sub      rsp, 0x40
    0x409ca2: mov      qword ptr [rbp - 0x38], rdi
    0x409ca6: cmp      qword ptr [rbp - 0x38], 0
    0x409cab: jne      0x409cb7

; --- Block 0x409cad [BODY] 2 insns, callees: (none)
    0x409cad: mov      eax, 0
    0x409cb2: jmp      0x40a15b

; --- Block 0x409cb7 [BODY] 3 insns, callees: sub_4010b0
    0x409cb7: mov      esi, 0x58
    0x409cbc: mov      edi, 1
    0x409cc1: call     0x4010b0

; --- Block 0x409cc6 [BODY] 5 insns, callees: (none)
    0x409cc6: mov      qword ptr [rbp - 8], rax
    0x409cca: mov      rax, qword ptr [rbp - 0x38]
    0x409cce: mov      eax, dword ptr [rax]
    0x409cd0: cmp      eax, 3
    0x409cd3: je       0x40a0e1

; --- Block 0x409cd9 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409cd9: cmp      eax, 3
    0x409cdc: ja       0x40a14d

; --- Block 0x409ce2 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409ce2: cmp      eax, 2
    0x409ce5: je       0x409d4f

; --- Block 0x409ce7 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409ce7: cmp      eax, 2
    0x409cea: ja       0x40a14d

; --- Block 0x409cf0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409cf0: test     eax, eax
    0x409cf2: je       0x409cfe

; --- Block 0x409cf4 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409cf4: cmp      eax, 1
    0x409cf7: je       0x409d21

; --- Block 0x409cf9 [BODY] 1 insns, callees: (none)
    0x409cf9: jmp      0x40a14d

; --- Block 0x409cfe [BODY] 8 insns, callees: (none)
    0x409cfe: mov      rax, qword ptr [rbp - 8]
    0x409d02: mov      dword ptr [rax], 0
    0x409d08: mov      rax, qword ptr [rbp - 0x38]
    0x409d0c: mov      rdx, qword ptr [rax + 8]
    0x409d10: mov      rax, qword ptr [rbp - 8]
    0x409d14: mov      qword ptr [rax + 8], rdx
    0x409d18: mov      rax, qword ptr [rbp - 8]
    0x409d1c: jmp      0x40a15b

; --- Block 0x409d21 [BODY] 9 insns, callees: sub_401050
    0x409d21: mov      rax, qword ptr [rbp - 8]
    0x409d25: mov      dword ptr [rax], 1
    0x409d2b: mov      rax, qword ptr [rbp - 0x38]
    0x409d2f: lea      rdx, [rax + 8]
    0x409d33: mov      rax, qword ptr [rbp - 8]
    0x409d37: add      rax, 8
    0x409d3b: mov      rsi, rdx
    0x409d3e: mov      rdi, rax
    0x409d41: call     0x401050

; --- Block 0x409d46 [BODY] 2 insns, callees: (none)
    0x409d46: mov      rax, qword ptr [rbp - 8]
    0x409d4a: jmp      0x40a15b

; --- Block 0x409d4f [BODY] 4 insns, callees: em_06
    0x409d4f: mov      rax, qword ptr [rbp - 0x38]
    0x409d53: mov      rax, qword ptr [rax + 8]
    0x409d57: mov      rdi, rax
    0x409d5a: call     0x409c9a

; --- Block 0x409d5f [LOOP_HEADER] 5 insns, callees: em_06
    0x409d5f: mov      qword ptr [rbp - 0x18], rax
    0x409d63: mov      rax, qword ptr [rbp - 0x38]
    0x409d67: mov      rax, qword ptr [rax + 0x18]
    0x409d6b: mov      rdi, rax
    0x409d6e: call     0x409c9a

; --- Block 0x409d73 [LOOP_HEADER] 5 insns, callees: (none)
    0x409d73: mov      qword ptr [rbp - 0x20], rax
    0x409d77: mov      rax, qword ptr [rbp - 0x18]
    0x409d7b: mov      eax, dword ptr [rax]
    0x409d7d: test     eax, eax
    0x409d7f: jne      0x409ee7

; --- Block 0x409d85 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409d85: mov      rax, qword ptr [rbp - 0x20]
    0x409d89: mov      eax, dword ptr [rax]
    0x409d8b: test     eax, eax
    0x409d8d: jne      0x409ee7

; --- Block 0x409d93 [BODY] 10 insns, callees: (none)
    0x409d93: mov      rax, qword ptr [rbp - 0x18]
    0x409d97: mov      rax, qword ptr [rax + 8]
    0x409d9b: mov      qword ptr [rbp - 0x28], rax
    0x409d9f: mov      rax, qword ptr [rbp - 0x20]
    0x409da3: mov      rax, qword ptr [rax + 8]
    0x409da7: mov      qword ptr [rbp - 0x30], rax
    0x409dab: mov      rax, qword ptr [rbp - 0x38]
    0x409daf: mov      eax, dword ptr [rax + 0x10]
    0x409db2: cmp      eax, 3
    0x409db5: je       0x409e9f

; --- Block 0x409dbb [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409dbb: cmp      eax, 3
    0x409dbe: ja       0x409ee7

; --- Block 0x409dc4 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409dc4: cmp      eax, 2
    0x409dc7: je       0x409e60

; --- Block 0x409dcd [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409dcd: cmp      eax, 2
    0x409dd0: ja       0x409ee7

; --- Block 0x409dd6 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409dd6: test     eax, eax
    0x409dd8: je       0x409de4

; --- Block 0x409dda [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409dda: cmp      eax, 1
    0x409ddd: je       0x409e22

; --- Block 0x409ddf [BODY] 1 insns, callees: (none)
    0x409ddf: jmp      0x409ee7

; --- Block 0x409de4 [BODY] 10 insns, callees: c_free_expr
    0x409de4: mov      rax, qword ptr [rbp - 8]
    0x409de8: mov      dword ptr [rax], 0
    0x409dee: mov      rdx, qword ptr [rbp - 0x28]
    0x409df2: mov      rax, qword ptr [rbp - 0x30]
    0x409df6: add      rdx, rax
    0x409df9: mov      rax, qword ptr [rbp - 8]
    0x409dfd: mov      qword ptr [rax + 8], rdx
    0x409e01: mov      rax, qword ptr [rbp - 0x18]
    0x409e05: mov      rdi, rax
    0x409e08: call     0x409452

; --- Block 0x409e0d [BODY] 3 insns, callees: c_free_expr
    0x409e0d: mov      rax, qword ptr [rbp - 0x20]
    0x409e11: mov      rdi, rax
    0x409e14: call     0x409452

; --- Block 0x409e19 [BODY] 2 insns, callees: (none)
    0x409e19: mov      rax, qword ptr [rbp - 8]
    0x409e1d: jmp      0x40a15b

; --- Block 0x409e22 [BODY] 10 insns, callees: c_free_expr
    0x409e22: mov      rax, qword ptr [rbp - 8]
    0x409e26: mov      dword ptr [rax], 0
    0x409e2c: mov      rax, qword ptr [rbp - 0x28]
    0x409e30: sub      rax, qword ptr [rbp - 0x30]
    0x409e34: mov      rdx, rax
    0x409e37: mov      rax, qword ptr [rbp - 8]
    0x409e3b: mov      qword ptr [rax + 8], rdx
    0x409e3f: mov      rax, qword ptr [rbp - 0x18]
    0x409e43: mov      rdi, rax
    0x409e46: call     0x409452

; --- Block 0x409e4b [BODY] 3 insns, callees: c_free_expr
    0x409e4b: mov      rax, qword ptr [rbp - 0x20]
    0x409e4f: mov      rdi, rax
    0x409e52: call     0x409452

; --- Block 0x409e57 [BODY] 2 insns, callees: (none)
    0x409e57: mov      rax, qword ptr [rbp - 8]
    0x409e5b: jmp      0x40a15b

; --- Block 0x409e60 [BODY] 10 insns, callees: c_free_expr
    0x409e60: mov      rax, qword ptr [rbp - 8]
    0x409e64: mov      dword ptr [rax], 0
    0x409e6a: mov      rax, qword ptr [rbp - 0x28]
    0x409e6e: imul     rax, qword ptr [rbp - 0x30]
    0x409e73: mov      rdx, rax
    0x409e76: mov      rax, qword ptr [rbp - 8]
    0x409e7a: mov      qword ptr [rax + 8], rdx
    0x409e7e: mov      rax, qword ptr [rbp - 0x18]
    0x409e82: mov      rdi, rax
    0x409e85: call     0x409452

; --- Block 0x409e8a [BODY] 3 insns, callees: c_free_expr
    0x409e8a: mov      rax, qword ptr [rbp - 0x20]
    0x409e8e: mov      rdi, rax
    0x409e91: call     0x409452

; --- Block 0x409e96 [BODY] 2 insns, callees: (none)
    0x409e96: mov      rax, qword ptr [rbp - 8]
    0x409e9a: jmp      0x40a15b

; --- Block 0x409e9f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409e9f: cmp      qword ptr [rbp - 0x30], 0
    0x409ea4: je       0x409ee6

; --- Block 0x409ea6 [BODY] 11 insns, callees: c_free_expr
    0x409ea6: mov      rax, qword ptr [rbp - 8]
    0x409eaa: mov      dword ptr [rax], 0
    0x409eb0: mov      rax, qword ptr [rbp - 0x28]
    0x409eb4: cqo      
    0x409eb6: idiv     qword ptr [rbp - 0x30]
    0x409eba: mov      rdx, rax
    0x409ebd: mov      rax, qword ptr [rbp - 8]
    0x409ec1: mov      qword ptr [rax + 8], rdx
    0x409ec5: mov      rax, qword ptr [rbp - 0x18]
    0x409ec9: mov      rdi, rax
    0x409ecc: call     0x409452

; --- Block 0x409ed1 [BODY] 3 insns, callees: c_free_expr
    0x409ed1: mov      rax, qword ptr [rbp - 0x20]
    0x409ed5: mov      rdi, rax
    0x409ed8: call     0x409452

; --- Block 0x409edd [BODY] 2 insns, callees: (none)
    0x409edd: mov      rax, qword ptr [rbp - 8]
    0x409ee1: jmp      0x40a15b

; --- Block 0x409ee6 [PROLOGUE] 1 insns, callees: (none)
    0x409ee6: nop      

; --- Block 0x409ee7 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409ee7: mov      rax, qword ptr [rbp - 0x18]
    0x409eeb: mov      eax, dword ptr [rax]
    0x409eed: test     eax, eax
    0x409eef: jne      0x409f2a

; --- Block 0x409ef1 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409ef1: mov      rax, qword ptr [rbp - 0x18]
    0x409ef5: mov      rax, qword ptr [rax + 8]
    0x409ef9: test     rax, rax
    0x409efc: jne      0x409f2a

; --- Block 0x409efe [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409efe: mov      rax, qword ptr [rbp - 0x38]
    0x409f02: mov      eax, dword ptr [rax + 0x10]
    0x409f05: test     eax, eax
    0x409f07: jne      0x409f2a

; --- Block 0x409f09 [BODY] 3 insns, callees: sub_401030
    0x409f09: mov      rax, qword ptr [rbp - 8]
    0x409f0d: mov      rdi, rax
    0x409f10: call     0x401030

; --- Block 0x409f15 [BODY] 3 insns, callees: c_free_expr
    0x409f15: mov      rax, qword ptr [rbp - 0x18]
    0x409f19: mov      rdi, rax
    0x409f1c: call     0x409452

; --- Block 0x409f21 [BODY] 2 insns, callees: (none)
    0x409f21: mov      rax, qword ptr [rbp - 0x20]
    0x409f25: jmp      0x40a15b

; --- Block 0x409f2a [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409f2a: mov      rax, qword ptr [rbp - 0x20]
    0x409f2e: mov      eax, dword ptr [rax]
    0x409f30: test     eax, eax
    0x409f32: jne      0x409f6d

; --- Block 0x409f34 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409f34: mov      rax, qword ptr [rbp - 0x20]
    0x409f38: mov      rax, qword ptr [rax + 8]
    0x409f3c: test     rax, rax
    0x409f3f: jne      0x409f6d

; --- Block 0x409f41 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409f41: mov      rax, qword ptr [rbp - 0x38]
    0x409f45: mov      eax, dword ptr [rax + 0x10]
    0x409f48: test     eax, eax
    0x409f4a: jne      0x409f6d

; --- Block 0x409f4c [BODY] 3 insns, callees: sub_401030
    0x409f4c: mov      rax, qword ptr [rbp - 8]
    0x409f50: mov      rdi, rax
    0x409f53: call     0x401030

; --- Block 0x409f58 [BODY] 3 insns, callees: c_free_expr
    0x409f58: mov      rax, qword ptr [rbp - 0x20]
    0x409f5c: mov      rdi, rax
    0x409f5f: call     0x409452

; --- Block 0x409f64 [BODY] 2 insns, callees: (none)
    0x409f64: mov      rax, qword ptr [rbp - 0x18]
    0x409f68: jmp      0x40a15b

; --- Block 0x409f6d [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409f6d: mov      rax, qword ptr [rbp - 0x18]
    0x409f71: mov      eax, dword ptr [rax]
    0x409f73: test     eax, eax
    0x409f75: jne      0x409fc7

; --- Block 0x409f77 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409f77: mov      rax, qword ptr [rbp - 0x18]
    0x409f7b: mov      rax, qword ptr [rax + 8]
    0x409f7f: test     rax, rax
    0x409f82: jne      0x409fc7

; --- Block 0x409f84 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409f84: mov      rax, qword ptr [rbp - 0x38]
    0x409f88: mov      eax, dword ptr [rax + 0x10]
    0x409f8b: cmp      eax, 2
    0x409f8e: jne      0x409fc7

; --- Block 0x409f90 [BODY] 7 insns, callees: c_free_expr
    0x409f90: mov      rax, qword ptr [rbp - 8]
    0x409f94: mov      dword ptr [rax], 0
    0x409f9a: mov      rax, qword ptr [rbp - 8]
    0x409f9e: mov      qword ptr [rax + 8], 0
    0x409fa6: mov      rax, qword ptr [rbp - 0x18]
    0x409faa: mov      rdi, rax
    0x409fad: call     0x409452

; --- Block 0x409fb2 [BODY] 3 insns, callees: c_free_expr
    0x409fb2: mov      rax, qword ptr [rbp - 0x20]
    0x409fb6: mov      rdi, rax
    0x409fb9: call     0x409452

; --- Block 0x409fbe [BODY] 2 insns, callees: (none)
    0x409fbe: mov      rax, qword ptr [rbp - 8]
    0x409fc2: jmp      0x40a15b

; --- Block 0x409fc7 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409fc7: mov      rax, qword ptr [rbp - 0x20]
    0x409fcb: mov      eax, dword ptr [rax]
    0x409fcd: test     eax, eax
    0x409fcf: jne      0x40a021

; --- Block 0x409fd1 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409fd1: mov      rax, qword ptr [rbp - 0x20]
    0x409fd5: mov      rax, qword ptr [rax + 8]
    0x409fd9: test     rax, rax
    0x409fdc: jne      0x40a021

; --- Block 0x409fde [BOUNDS_CHECK] 4 insns, callees: (none)
    0x409fde: mov      rax, qword ptr [rbp - 0x38]
    0x409fe2: mov      eax, dword ptr [rax + 0x10]
    0x409fe5: cmp      eax, 2
    0x409fe8: jne      0x40a021

; --- Block 0x409fea [BODY] 7 insns, callees: c_free_expr
    0x409fea: mov      rax, qword ptr [rbp - 8]
    0x409fee: mov      dword ptr [rax], 0
    0x409ff4: mov      rax, qword ptr [rbp - 8]
    0x409ff8: mov      qword ptr [rax + 8], 0
    0x40a000: mov      rax, qword ptr [rbp - 0x18]
    0x40a004: mov      rdi, rax
    0x40a007: call     0x409452

; --- Block 0x40a00c [BODY] 3 insns, callees: c_free_expr
    0x40a00c: mov      rax, qword ptr [rbp - 0x20]
    0x40a010: mov      rdi, rax
    0x40a013: call     0x409452

; --- Block 0x40a018 [BODY] 2 insns, callees: (none)
    0x40a018: mov      rax, qword ptr [rbp - 8]
    0x40a01c: jmp      0x40a15b

; --- Block 0x40a021 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a021: mov      rax, qword ptr [rbp - 0x18]
    0x40a025: mov      eax, dword ptr [rax]
    0x40a027: test     eax, eax
    0x40a029: jne      0x40a066

; --- Block 0x40a02b [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a02b: mov      rax, qword ptr [rbp - 0x18]
    0x40a02f: mov      rax, qword ptr [rax + 8]
    0x40a033: cmp      rax, 1
    0x40a037: jne      0x40a066

; --- Block 0x40a039 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a039: mov      rax, qword ptr [rbp - 0x38]
    0x40a03d: mov      eax, dword ptr [rax + 0x10]
    0x40a040: cmp      eax, 2
    0x40a043: jne      0x40a066

; --- Block 0x40a045 [BODY] 3 insns, callees: sub_401030
    0x40a045: mov      rax, qword ptr [rbp - 8]
    0x40a049: mov      rdi, rax
    0x40a04c: call     0x401030

; --- Block 0x40a051 [BODY] 3 insns, callees: c_free_expr
    0x40a051: mov      rax, qword ptr [rbp - 0x18]
    0x40a055: mov      rdi, rax
    0x40a058: call     0x409452

; --- Block 0x40a05d [BODY] 2 insns, callees: (none)
    0x40a05d: mov      rax, qword ptr [rbp - 0x20]
    0x40a061: jmp      0x40a15b

; --- Block 0x40a066 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a066: mov      rax, qword ptr [rbp - 0x20]
    0x40a06a: mov      eax, dword ptr [rax]
    0x40a06c: test     eax, eax
    0x40a06e: jne      0x40a0ab

; --- Block 0x40a070 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a070: mov      rax, qword ptr [rbp - 0x20]
    0x40a074: mov      rax, qword ptr [rax + 8]
    0x40a078: cmp      rax, 1
    0x40a07c: jne      0x40a0ab

; --- Block 0x40a07e [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a07e: mov      rax, qword ptr [rbp - 0x38]
    0x40a082: mov      eax, dword ptr [rax + 0x10]
    0x40a085: cmp      eax, 2
    0x40a088: jne      0x40a0ab

; --- Block 0x40a08a [BODY] 3 insns, callees: sub_401030
    0x40a08a: mov      rax, qword ptr [rbp - 8]
    0x40a08e: mov      rdi, rax
    0x40a091: call     0x401030

; --- Block 0x40a096 [BODY] 3 insns, callees: c_free_expr
    0x40a096: mov      rax, qword ptr [rbp - 0x20]
    0x40a09a: mov      rdi, rax
    0x40a09d: call     0x409452

; --- Block 0x40a0a2 [BODY] 2 insns, callees: (none)
    0x40a0a2: mov      rax, qword ptr [rbp - 0x18]
    0x40a0a6: jmp      0x40a15b

; --- Block 0x40a0ab [BODY] 14 insns, callees: (none)
    0x40a0ab: mov      rax, qword ptr [rbp - 8]
    0x40a0af: mov      dword ptr [rax], 2
    0x40a0b5: mov      rax, qword ptr [rbp - 8]
    0x40a0b9: mov      rdx, qword ptr [rbp - 0x18]
    0x40a0bd: mov      qword ptr [rax + 8], rdx
    0x40a0c1: mov      rax, qword ptr [rbp - 0x38]
    0x40a0c5: mov      edx, dword ptr [rax + 0x10]
    0x40a0c8: mov      rax, qword ptr [rbp - 8]
    0x40a0cc: mov      dword ptr [rax + 0x10], edx
    0x40a0cf: mov      rax, qword ptr [rbp - 8]
    0x40a0d3: mov      rdx, qword ptr [rbp - 0x20]
    0x40a0d7: mov      qword ptr [rax + 0x18], rdx
    ... +2 more instructions

; --- Block 0x40a0e1 [BODY] 4 insns, callees: em_06
    0x40a0e1: mov      rax, qword ptr [rbp - 0x38]
    0x40a0e5: mov      rax, qword ptr [rax + 8]
    0x40a0e9: mov      rdi, rax
    0x40a0ec: call     0x409c9a

; --- Block 0x40a0f1 [LOOP_HEADER] 5 insns, callees: (none)
    0x40a0f1: mov      qword ptr [rbp - 0x10], rax
    0x40a0f5: mov      rax, qword ptr [rbp - 0x10]
    0x40a0f9: mov      eax, dword ptr [rax]
    0x40a0fb: test     eax, eax
    0x40a0fd: jne      0x40a131

; --- Block 0x40a0ff [BODY] 11 insns, callees: c_free_expr
    0x40a0ff: mov      rax, qword ptr [rbp - 8]
    0x40a103: mov      dword ptr [rax], 0
    0x40a109: mov      rax, qword ptr [rbp - 0x10]
    0x40a10d: mov      rax, qword ptr [rax + 8]
    0x40a111: neg      rax
    0x40a114: mov      rdx, rax
    0x40a117: mov      rax, qword ptr [rbp - 8]
    0x40a11b: mov      qword ptr [rax + 8], rdx
    0x40a11f: mov      rax, qword ptr [rbp - 0x10]
    0x40a123: mov      rdi, rax
    0x40a126: call     0x409452

; --- Block 0x40a12b [BODY] 2 insns, callees: (none)
    0x40a12b: mov      rax, qword ptr [rbp - 8]
    0x40a12f: jmp      0x40a15b

; --- Block 0x40a131 [BODY] 7 insns, callees: (none)
    0x40a131: mov      rax, qword ptr [rbp - 8]
    0x40a135: mov      dword ptr [rax], 3
    0x40a13b: mov      rax, qword ptr [rbp - 8]
    0x40a13f: mov      rdx, qword ptr [rbp - 0x10]
    0x40a143: mov      qword ptr [rax + 8], rdx
    0x40a147: mov      rax, qword ptr [rbp - 8]
    0x40a14b: jmp      0x40a15b

; --- Block 0x40a14d [BODY] 5 insns, callees: (none)
    0x40a14d: mov      rax, qword ptr [rbp - 8]
    0x40a151: mov      dword ptr [rax], 0
    0x40a157: mov      rax, qword ptr [rbp - 8]
    0x40a15b: leave    
    0x40a15c: ret      

; --- Block 0x40a15b [BODY] 2 insns, callees: (none)
    0x40a15b: leave    
    0x40a15c: ret      

```

**O2 blocks** (66 total):

```asm
; --- Block 0x408ae0 [LOOP_HEADER] 7 insns, callees: (none)
    0x408ae0: push     r13
    0x408ae2: push     r12
    0x408ae4: push     rbp
    0x408ae5: push     rbx
    0x408ae6: sub      rsp, 8
    0x408aea: test     rdi, rdi
    0x408aed: je       0x408bf8

; --- Block 0x408af3 [BODY] 4 insns, callees: sub_4010c0
    0x408af3: mov      rbx, rdi
    0x408af6: mov      esi, 0x58
    0x408afb: mov      edi, 1
    0x408b00: call     0x4010c0

; --- Block 0x408b05 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408b05: mov      r12, rax
    0x408b08: mov      eax, dword ptr [rbx]
    0x408b0a: cmp      eax, 2
    0x408b0d: je       0x408ba0

; --- Block 0x408b13 [BODY] 1 insns, callees: (none)
    0x408b13: ja       0x408b40

; --- Block 0x408b15 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408b15: test     eax, eax
    0x408b17: je       0x408b80

; --- Block 0x408b19 [BODY] 4 insns, callees: sub_401050
    0x408b19: mov      dword ptr [r12], 1
    0x408b21: lea      rsi, [rbx + 8]
    0x408b25: lea      rdi, [r12 + 8]
    0x408b2a: call     0x401050

; --- Block 0x408b2f [LOOP_HEADER] 7 insns, callees: (none)
    0x408b2f: add      rsp, 8
    0x408b33: mov      rax, r12
    0x408b36: pop      rbx
    0x408b37: pop      rbp
    0x408b38: pop      r12
    0x408b3a: pop      r13
    0x408b3c: ret      

; --- Block 0x408b40 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408b40: cmp      eax, 3
    0x408b43: jne      0x408b2f

; --- Block 0x408b45 [BODY] 2 insns, callees: em_06
    0x408b45: mov      rdi, qword ptr [rbx + 8]
    0x408b49: call     0x408ae0

; --- Block 0x408b4e [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408b4e: mov      rdi, rax
    0x408b51: mov      eax, dword ptr [rax]
    0x408b53: test     eax, eax
    0x408b55: je       0x408d00

; --- Block 0x408b5b [BODY] 9 insns, callees: (none)
    0x408b5b: mov      dword ptr [r12], 3
    0x408b63: mov      rax, r12
    0x408b66: mov      qword ptr [r12 + 8], rdi
    0x408b6b: add      rsp, 8
    0x408b6f: pop      rbx
    0x408b70: pop      rbp
    0x408b71: pop      r12
    0x408b73: pop      r13
    0x408b75: ret      

; --- Block 0x408b80 [BODY] 9 insns, callees: (none)
    0x408b80: mov      rax, qword ptr [rbx + 8]
    0x408b84: mov      qword ptr [r12 + 8], rax
    0x408b89: add      rsp, 8
    0x408b8d: mov      rax, r12
    0x408b90: pop      rbx
    0x408b91: pop      rbp
    0x408b92: pop      r12
    0x408b94: pop      r13
    0x408b96: ret      

; --- Block 0x408ba0 [BODY] 2 insns, callees: em_06
    0x408ba0: mov      rdi, qword ptr [rbx + 8]
    0x408ba4: call     0x408ae0

; --- Block 0x408ba9 [LOOP_HEADER] 3 insns, callees: em_06
    0x408ba9: mov      rdi, qword ptr [rbx + 0x18]
    0x408bad: mov      r13, rax
    0x408bb0: call     0x408ae0

; --- Block 0x408bb5 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408bb5: mov      ecx, dword ptr [r13]
    0x408bb9: mov      rbp, rax
    0x408bbc: test     ecx, ecx
    0x408bbe: je       0x408c10

; --- Block 0x408bc0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408bc0: mov      esi, dword ptr [rax]
    0x408bc2: mov      edx, dword ptr [rbx + 0x10]
    0x408bc5: test     esi, esi
    0x408bc7: je       0x408cb0

; --- Block 0x408bcd [LOOP_HEADER] 11 insns, callees: (none)
    0x408bcd: mov      dword ptr [r12], 2
    0x408bd5: mov      rax, r12
    0x408bd8: mov      qword ptr [r12 + 8], r13
    0x408bdd: mov      dword ptr [r12 + 0x10], edx
    0x408be2: mov      qword ptr [r12 + 0x18], rbp
    0x408be7: add      rsp, 8
    0x408beb: pop      rbx
    0x408bec: pop      rbp
    0x408bed: pop      r12
    0x408bef: pop      r13
    0x408bf1: ret      

; --- Block 0x408bf8 [BODY] 8 insns, callees: (none)
    0x408bf8: add      rsp, 8
    0x408bfc: xor      r12d, r12d
    0x408bff: pop      rbx
    0x408c00: mov      rax, r12
    0x408c03: pop      rbp
    0x408c04: pop      r12
    0x408c06: pop      r13
    0x408c08: ret      

; --- Block 0x408c10 [BODY] 5 insns, callees: (none)
    0x408c10: mov      esi, dword ptr [rax]
    0x408c12: mov      edx, dword ptr [rbx + 0x10]
    0x408c15: mov      rax, qword ptr [r13 + 8]
    0x408c19: test     esi, esi
    0x408c1b: jne      0x408c60

; --- Block 0x408c1d [BOUNDS_CHECK] 3 insns, callees: (none)
    0x408c1d: mov      rdi, qword ptr [rbp + 8]
    0x408c21: cmp      edx, 2
    0x408c24: je       0x408dd5

; --- Block 0x408c2a [BODY] 1 insns, callees: (none)
    0x408c2a: ja       0x408d70

; --- Block 0x408c30 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408c30: test     edx, edx
    0x408c32: je       0x408db0

; --- Block 0x408c38 [BODY] 5 insns, callees: c_free_expr
    0x408c38: mov      dword ptr [r12], 0
    0x408c40: sub      rax, rdi
    0x408c43: mov      qword ptr [r12 + 8], rax
    0x408c48: mov      rdi, r13
    0x408c4b: call     0x4025b0

; --- Block 0x408c43 [LOOP_HEADER] 3 insns, callees: c_free_expr
    0x408c43: mov      qword ptr [r12 + 8], rax
    0x408c48: mov      rdi, r13
    0x408c4b: call     0x4025b0

; --- Block 0x408c50 [BODY] 2 insns, callees: c_free_expr
    0x408c50: mov      rdi, rbp
    0x408c53: call     0x4025b0

; --- Block 0x408c58 [BODY] 1 insns, callees: (none)
    0x408c58: jmp      0x408b2f

; --- Block 0x408c60 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408c60: test     rax, rax
    0x408c63: jne      0x408c88

; --- Block 0x408c65 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408c65: test     edx, edx
    0x408c67: jne      0x408c88

; --- Block 0x408c69 [LOOP_HEADER] 3 insns, callees: sub_401030
    0x408c69: mov      rdi, r12
    0x408c6c: mov      r12, rbp
    0x408c6f: call     0x401030

; --- Block 0x408c74 [BODY] 2 insns, callees: c_free_expr
    0x408c74: mov      rdi, r13
    0x408c77: call     0x4025b0

; --- Block 0x408c7c [BODY] 1 insns, callees: (none)
    0x408c7c: jmp      0x408b2f

; --- Block 0x408c88 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408c88: test     esi, esi
    0x408c8a: jne      0x408d20

; --- Block 0x408c90 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408c90: cmp      qword ptr [rbp + 8], 0
    0x408c95: je       0x408cb7

; --- Block 0x408c97 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408c97: cmp      qword ptr [r13 + 8], 0
    0x408c9c: jne      0x408d32

; --- Block 0x408ca2 [BODY] 2 insns, callees: (none)
    0x408ca2: xor      esi, esi
    0x408ca4: jmp      0x408d25

; --- Block 0x408cb0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408cb0: cmp      qword ptr [rax + 8], 0
    0x408cb5: jne      0x408cc3

; --- Block 0x408cb7 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408cb7: test     edx, edx
    0x408cb9: je       0x408d55

; --- Block 0x408cbf [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408cbf: test     ecx, ecx
    0x408cc1: je       0x408c97

; --- Block 0x408cc3 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x408cc3: mov      rax, qword ptr [rbp + 8]
    0x408cc7: test     rax, rax
    0x408cca: jne      0x408d42

; --- Block 0x408ccc [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408ccc: cmp      edx, 2
    0x408ccf: jne      0x408bcd

; --- Block 0x408cd5 [LOOP_HEADER] 4 insns, callees: c_free_expr
    0x408cd5: mov      dword ptr [r12], 0
    0x408cdd: mov      rdi, r13
    0x408ce0: mov      qword ptr [r12 + 8], 0
    0x408ce9: call     0x4025b0

; --- Block 0x408cee [BODY] 2 insns, callees: c_free_expr
    0x408cee: mov      rdi, rbp
    0x408cf1: call     0x4025b0

; --- Block 0x408cf6 [BODY] 1 insns, callees: (none)
    0x408cf6: jmp      0x408b2f

; --- Block 0x408d00 [BODY] 5 insns, callees: c_free_expr
    0x408d00: mov      rax, qword ptr [rdi + 8]
    0x408d04: mov      dword ptr [r12], 0
    0x408d0c: neg      rax
    0x408d0f: mov      qword ptr [r12 + 8], rax
    0x408d14: call     0x4025b0

; --- Block 0x408d19 [BODY] 1 insns, callees: (none)
    0x408d19: jmp      0x408b2f

; --- Block 0x408d20 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d20: test     rax, rax
    0x408d23: jne      0x408d98

; --- Block 0x408d25 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d25: cmp      edx, 2
    0x408d28: je       0x408cd5

; --- Block 0x408d2a [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d2a: test     esi, esi
    0x408d2c: jne      0x408bcd

; --- Block 0x408d32 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x408d32: mov      rax, qword ptr [rbp + 8]
    0x408d36: test     rax, rax
    0x408d39: je       0x408ccc

; --- Block 0x408d3b [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d3b: cmp      qword ptr [r13 + 8], 1
    0x408d40: je       0x408da2

; --- Block 0x408d42 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d42: cmp      rax, 1
    0x408d46: jne      0x408bcd

; --- Block 0x408d4c [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d4c: cmp      edx, 2
    0x408d4f: jne      0x408bcd

; --- Block 0x408d55 [BODY] 3 insns, callees: sub_401030
    0x408d55: mov      rdi, r12
    0x408d58: mov      r12, r13
    0x408d5b: call     0x401030

; --- Block 0x408d60 [BODY] 2 insns, callees: c_free_expr
    0x408d60: mov      rdi, rbp
    0x408d63: call     0x4025b0

; --- Block 0x408d68 [BODY] 1 insns, callees: (none)
    0x408d68: jmp      0x408b2f

; --- Block 0x408d70 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d70: cmp      edx, 3
    0x408d73: jne      0x408c60

; --- Block 0x408d79 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d79: test     rdi, rdi
    0x408d7c: je       0x408c60

; --- Block 0x408d82 [BODY] 4 insns, callees: (none)
    0x408d82: cqo      
    0x408d84: mov      dword ptr [r12], 0
    0x408d8c: idiv     rdi
    0x408d8f: jmp      0x408c43

; --- Block 0x408d98 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408d98: cmp      rax, 1
    0x408d9c: jne      0x408bcd

; --- Block 0x408da2 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x408da2: cmp      edx, 2
    0x408da5: jne      0x408bcd

; --- Block 0x408dab [BODY] 1 insns, callees: (none)
    0x408dab: jmp      0x408c69

; --- Block 0x408db0 [BODY] 5 insns, callees: c_free_expr
    0x408db0: mov      dword ptr [r12], 0
    0x408db8: add      rdi, rax
    0x408dbb: mov      qword ptr [r12 + 8], rdi
    0x408dc0: mov      rdi, r13
    0x408dc3: call     0x4025b0

; --- Block 0x408dbb [LOOP_HEADER] 3 insns, callees: c_free_expr
    0x408dbb: mov      qword ptr [r12 + 8], rdi
    0x408dc0: mov      rdi, r13
    0x408dc3: call     0x4025b0

; --- Block 0x408dc8 [BODY] 2 insns, callees: c_free_expr
    0x408dc8: mov      rdi, rbp
    0x408dcb: call     0x4025b0

; --- Block 0x408dd0 [BODY] 1 insns, callees: (none)
    0x408dd0: jmp      0x408b2f

; --- Block 0x408dd5 [BODY] 3 insns, callees: (none)
    0x408dd5: mov      dword ptr [r12], 0
    0x408ddd: imul     rdi, rax
    0x408de1: jmp      0x408dbb

```

**Hungarian matching result** (mean similarity: 0.819):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x409cd9` | BOUNDS_CHECK | `0x408b40` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409ce2` | BOUNDS_CHECK | `0x408d4c` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409ce7` | BOUNDS_CHECK | `0x408da2` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409cf0` | BOUNDS_CHECK | `0x408b15` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409cf4` | BOUNDS_CHECK | `0x408c88` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409cf9` | BODY | `0x408c58` | BODY | 1.000 | GOOD |
| `0x409dbb` | BOUNDS_CHECK | `0x408d70` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409dc4` | BOUNDS_CHECK | `0x408d25` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409dcd` | BOUNDS_CHECK | `0x408ccc` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409dd6` | BOUNDS_CHECK | `0x408c30` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409dda` | BOUNDS_CHECK | `0x408c60` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409ddf` | BODY | `0x408c7c` | BODY | 1.000 | GOOD |
| `0x409e9f` | BOUNDS_CHECK | `0x408c90` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x409ee6` | PROLOGUE | `0x408b13` | BODY | 0.997 | GOOD |
| `0x409d73` | LOOP_HEADER | `0x408c10` | BODY | 0.986 | GOOD |
| `0x409f84` | BOUNDS_CHECK | `0x408b05` | BOUNDS_CHECK | 0.985 | GOOD |
| `0x409d85` | BOUNDS_CHECK | `0x408b4e` | BOUNDS_CHECK | 0.974 | GOOD |
| `0x409ee7` | BOUNDS_CHECK | `0x408bb5` | BOUNDS_CHECK | 0.968 | GOOD |
| `0x409ef1` | BOUNDS_CHECK | `0x408bc0` | BOUNDS_CHECK | 0.964 | GOOD |
| `0x409f09` | BODY | `0x408c69` | LOOP_HEADER | 0.964 | GOOD |
| `0x409ed1` | BODY | `0x408c43` | LOOP_HEADER | 0.962 | GOOD |
| `0x40a051` | BODY | `0x408dbb` | LOOP_HEADER | 0.962 | GOOD |
| `0x409f4c` | BODY | `0x408d55` | BODY | 0.958 | GOOD |
| `0x40a0e1` | BODY | `0x408cd5` | LOOP_HEADER | 0.958 | GOOD |
| `0x409e8a` | BODY | `0x408ba9` | LOOP_HEADER | 0.952 | GOOD |
| `0x409fde` | BOUNDS_CHECK | `0x408c1d` | BOUNDS_CHECK | 0.916 | GOOD |
| `0x409f2a` | BOUNDS_CHECK | `0x408cc3` | BOUNDS_CHECK | 0.915 | GOOD |
| `0x409fc7` | BOUNDS_CHECK | `0x408d32` | BOUNDS_CHECK | 0.915 | GOOD |
| `0x409d5f` | LOOP_HEADER | `0x408d00` | BODY | 0.875 | GOOD |
| `0x409f15` | BODY | `0x408c50` | BODY | 0.864 | GOOD |
| `0x409fb2` | BODY | `0x408cee` | BODY | 0.864 | GOOD |
| `0x40a00c` | BODY | `0x408d60` | BODY | 0.864 | GOOD |
| `0x40a096` | BODY | `0x408dc8` | BODY | 0.864 | GOOD |
| `0x409e0d` | BODY | `0x408b45` | BODY | 0.860 | GOOD |
| `0x409e4b` | BODY | `0x408ba0` | BODY | 0.860 | GOOD |
| `0x409f58` | BODY | `0x408c74` | BODY | 0.849 | GOOD |
| `0x409de4` | BODY | `0x408db0` | BODY | 0.789 | GOOD |
| `0x409e22` | BODY | `0x408c38` | BODY | 0.779 | GOOD |
| `0x409cb7` | BODY | `0x408af3` | BODY | 0.749 | GOOD |
| `0x409cad` | BODY | `0x408ca2` | BODY | 0.741 | GOOD |
| `0x409f64` | BODY | `0x408dd5` | BODY | 0.739 | GOOD |
| `0x409efe` | BOUNDS_CHECK | `0x408d98` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x409f34` | BOUNDS_CHECK | `0x408cb7` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x409f41` | BOUNDS_CHECK | `0x408d20` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x409f6d` | BOUNDS_CHECK | `0x408cb0` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x409f77` | BOUNDS_CHECK | `0x408d2a` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x409fd1` | BOUNDS_CHECK | `0x408d3b` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x40a021` | BOUNDS_CHECK | `0x408d42` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x40a02b` | BOUNDS_CHECK | `0x408cbf` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x40a066` | BOUNDS_CHECK | `0x408c97` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x40a070` | BOUNDS_CHECK | `0x408d79` | BOUNDS_CHECK | 0.693 | PARTIAL |
| `0x40a0f1` | LOOP_HEADER | `0x408c65` | BOUNDS_CHECK | 0.660 | PARTIAL |
| `0x409d21` | BODY | `0x408b80` | BODY | 0.649 | PARTIAL |
| `0x409c9a` | LOOP_HEADER | `0x408ae0` | LOOP_HEADER | 0.649 | PARTIAL |
| `0x409d46` | BODY | `0x408cf6` | BODY | 0.639 | PARTIAL |
| `0x409e19` | BODY | `0x408d19` | BODY | 0.639 | PARTIAL |
| `0x409e57` | BODY | `0x408d68` | BODY | 0.639 | PARTIAL |
| `0x409e96` | BODY | `0x408dab` | BODY | 0.639 | PARTIAL |
| `0x409f21` | BODY | `0x408dd0` | BODY | 0.639 | PARTIAL |
| `0x409edd` | BODY | `0x408d82` | BODY | 0.631 | PARTIAL |
| `0x409d4f` | BODY | `0x408b19` | BODY | 0.603 | PARTIAL |
| `0x409d93` | BODY | `0x408b5b` | BODY | 0.593 | PARTIAL |
| `0x40a0ab` | BODY | `0x408bcd` | LOOP_HEADER | 0.571 | PARTIAL |
| `0x409f90` | BODY | `0x408b2f` | LOOP_HEADER | 0.499 | PARTIAL |
| `0x409cfe` | BODY | `0x408bf8` | BODY | 0.497 | PARTIAL |
| `0x40a15b` | BODY | `0x408c2a` | BODY | 0.491 | PARTIAL |
| `0x409cc6` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x409e60` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x409ea6` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x409fbe` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x409fea` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a018` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a039` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a045` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a05d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a07e` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a08a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a0a2` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a0ff` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a12b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a131` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40a14d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `em_20`

### Rust `em_20` — O0: 1 blocks, O2: 1 blocks

**O0 blocks** (1 total):

```asm
; --- Block 0x450fa0 [BODY] 22 insns, callees: (none)
    0x450fa0: sub      rsp, 0x648
    0x450fa7: mov      qword ptr [rsp + 0x1a0], rsi
    0x450faf: mov      qword ptr [rsp + 0x1a8], rdi
    0x450fb7: mov      qword ptr [rsp + 0x1b0], rdi
    0x450fbf: mov      qword ptr [rsp + 0x520], rsi
    0x450fc7: mov      byte ptr [rsp + 0x51f], 0
    0x450fcf: mov      byte ptr [rsp + 0x51e], 0
    0x450fd7: mov      byte ptr [rsp + 0x51d], 0
    0x450fdf: mov      byte ptr [rsp + 0x51c], 0
    0x450fe7: mov      rax, qword ptr [rsi]
    0x450fea: movabs   rdx, 0x8000000000000000
    0x450ff4: mov      rcx, rax
    ... +10 more instructions

```

**O2 blocks** (1 total):

```asm
; --- Block 0x428770 [BODY] 18 insns, callees: (none)
    0x428770: push     rbp
    0x428771: push     r15
    0x428773: push     r14
    0x428775: push     r12
    0x428777: push     rbx
    0x428778: sub      rsp, 0x100
    0x42877f: movabs   r12, 0x8000000000000002
    0x428789: mov      rax, qword ptr [rsi]
    0x42878c: lea      rcx, [r12 - 2]
    0x428791: xor      rcx, rax
    0x428794: test     rax, rax
    0x428797: mov      eax, 4
    ... +6 more instructions

```

**Hungarian matching result** (mean similarity: 0.647):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x450fa0` | BODY | `0x428770` | BODY | 0.647 | PARTIAL |

### C `em_20` — O0: 30 blocks, O2: 25 blocks

**O0 blocks** (30 total):

```asm
; --- Block 0x40ca2c [LOOP_HEADER] 6 insns, callees: (none)
    0x40ca2c: push     rbp
    0x40ca2d: mov      rbp, rsp
    0x40ca30: sub      rsp, 0x40
    0x40ca34: mov      qword ptr [rbp - 0x38], rdi
    0x40ca38: cmp      qword ptr [rbp - 0x38], 0
    0x40ca3d: jne      0x40ca49

; --- Block 0x40ca3f [BODY] 2 insns, callees: (none)
    0x40ca3f: mov      eax, 0
    0x40ca44: jmp      0x40cc82

; --- Block 0x40ca49 [BODY] 3 insns, callees: sub_4010b0
    0x40ca49: mov      esi, 0x58
    0x40ca4e: mov      edi, 1
    0x40ca53: call     0x4010b0

; --- Block 0x40ca58 [BODY] 5 insns, callees: (none)
    0x40ca58: mov      qword ptr [rbp - 8], rax
    0x40ca5c: mov      rax, qword ptr [rbp - 0x38]
    0x40ca60: mov      eax, dword ptr [rax]
    0x40ca62: cmp      eax, 3
    0x40ca65: je       0x40cc4c

; --- Block 0x40ca6b [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ca6b: cmp      eax, 3
    0x40ca6e: ja       0x40cc74

; --- Block 0x40ca74 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ca74: cmp      eax, 2
    0x40ca77: je       0x40cae1

; --- Block 0x40ca79 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ca79: cmp      eax, 2
    0x40ca7c: ja       0x40cc74

; --- Block 0x40ca82 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ca82: test     eax, eax
    0x40ca84: je       0x40ca90

; --- Block 0x40ca86 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ca86: cmp      eax, 1
    0x40ca89: je       0x40cab3

; --- Block 0x40ca8b [BODY] 1 insns, callees: (none)
    0x40ca8b: jmp      0x40cc74

; --- Block 0x40ca90 [BODY] 8 insns, callees: (none)
    0x40ca90: mov      rax, qword ptr [rbp - 8]
    0x40ca94: mov      dword ptr [rax], 0
    0x40ca9a: mov      rax, qword ptr [rbp - 0x38]
    0x40ca9e: mov      rdx, qword ptr [rax + 8]
    0x40caa2: mov      rax, qword ptr [rbp - 8]
    0x40caa6: mov      qword ptr [rax + 8], rdx
    0x40caaa: mov      rax, qword ptr [rbp - 8]
    0x40caae: jmp      0x40cc82

; --- Block 0x40cab3 [BODY] 9 insns, callees: sub_401050
    0x40cab3: mov      rax, qword ptr [rbp - 8]
    0x40cab7: mov      dword ptr [rax], 1
    0x40cabd: mov      rax, qword ptr [rbp - 0x38]
    0x40cac1: lea      rdx, [rax + 8]
    0x40cac5: mov      rax, qword ptr [rbp - 8]
    0x40cac9: add      rax, 8
    0x40cacd: mov      rsi, rdx
    0x40cad0: mov      rdi, rax
    0x40cad3: call     0x401050

; --- Block 0x40cad8 [BODY] 2 insns, callees: (none)
    0x40cad8: mov      rax, qword ptr [rbp - 8]
    0x40cadc: jmp      0x40cc82

; --- Block 0x40cae1 [BODY] 4 insns, callees: em_20
    0x40cae1: mov      rax, qword ptr [rbp - 0x38]
    0x40cae5: mov      rax, qword ptr [rax + 8]
    0x40cae9: mov      rdi, rax
    0x40caec: call     0x40ca2c

; --- Block 0x40caf1 [LOOP_HEADER] 5 insns, callees: em_20
    0x40caf1: mov      qword ptr [rbp - 0x10], rax
    0x40caf5: mov      rax, qword ptr [rbp - 0x38]
    0x40caf9: mov      rax, qword ptr [rax + 0x18]
    0x40cafd: mov      rdi, rax
    0x40cb00: call     0x40ca2c

; --- Block 0x40cb05 [LOOP_HEADER] 5 insns, callees: (none)
    0x40cb05: mov      qword ptr [rbp - 0x18], rax
    0x40cb09: mov      rax, qword ptr [rbp - 0x38]
    0x40cb0d: mov      eax, dword ptr [rax + 0x10]
    0x40cb10: cmp      eax, 2
    0x40cb13: jne      0x40cc16

; --- Block 0x40cb19 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40cb19: mov      rax, qword ptr [rbp - 0x18]
    0x40cb1d: mov      eax, dword ptr [rax]
    0x40cb1f: cmp      eax, 2
    0x40cb22: jne      0x40cc16

; --- Block 0x40cb28 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40cb28: mov      rax, qword ptr [rbp - 0x18]
    0x40cb2c: mov      eax, dword ptr [rax + 0x10]
    0x40cb2f: test     eax, eax
    0x40cb31: jne      0x40cc16

; --- Block 0x40cb37 [BODY] 3 insns, callees: sub_4010b0
    0x40cb37: mov      esi, 0x58
    0x40cb3c: mov      edi, 1
    0x40cb41: call     0x4010b0

; --- Block 0x40cb46 [BODY] 6 insns, callees: c_clone_expr
    0x40cb46: mov      qword ptr [rbp - 0x20], rax
    0x40cb4a: mov      rax, qword ptr [rbp - 0x20]
    0x40cb4e: mov      dword ptr [rax], 2
    0x40cb54: mov      rax, qword ptr [rbp - 0x10]
    0x40cb58: mov      rdi, rax
    0x40cb5b: call     0x40c936

; --- Block 0x40cb60 [BODY] 8 insns, callees: c_clone_expr
    0x40cb60: mov      rdx, qword ptr [rbp - 0x20]
    0x40cb64: mov      qword ptr [rdx + 8], rax
    0x40cb68: mov      rax, qword ptr [rbp - 0x20]
    0x40cb6c: mov      dword ptr [rax + 0x10], 2
    0x40cb73: mov      rax, qword ptr [rbp - 0x18]
    0x40cb77: mov      rax, qword ptr [rax + 8]
    0x40cb7b: mov      rdi, rax
    0x40cb7e: call     0x40c936

; --- Block 0x40cb83 [BODY] 5 insns, callees: sub_4010b0
    0x40cb83: mov      rdx, qword ptr [rbp - 0x20]
    0x40cb87: mov      qword ptr [rdx + 0x18], rax
    0x40cb8b: mov      esi, 0x58
    0x40cb90: mov      edi, 1
    0x40cb95: call     0x4010b0

; --- Block 0x40cb9a [BODY] 12 insns, callees: c_clone_expr
    0x40cb9a: mov      qword ptr [rbp - 0x28], rax
    0x40cb9e: mov      rax, qword ptr [rbp - 0x28]
    0x40cba2: mov      dword ptr [rax], 2
    0x40cba8: mov      rax, qword ptr [rbp - 0x28]
    0x40cbac: mov      rdx, qword ptr [rbp - 0x10]
    0x40cbb0: mov      qword ptr [rax + 8], rdx
    0x40cbb4: mov      rax, qword ptr [rbp - 0x28]
    0x40cbb8: mov      dword ptr [rax + 0x10], 2
    0x40cbbf: mov      rax, qword ptr [rbp - 0x18]
    0x40cbc3: mov      rax, qword ptr [rax + 0x18]
    0x40cbc7: mov      rdi, rax
    0x40cbca: call     0x40c936

; --- Block 0x40cbcf [BODY] 5 insns, callees: c_free_expr
    0x40cbcf: mov      rdx, qword ptr [rbp - 0x28]
    0x40cbd3: mov      qword ptr [rdx + 0x18], rax
    0x40cbd7: mov      rax, qword ptr [rbp - 0x18]
    0x40cbdb: mov      rdi, rax
    0x40cbde: call     0x409452

; --- Block 0x40cbe3 [BODY] 12 insns, callees: (none)
    0x40cbe3: mov      rax, qword ptr [rbp - 8]
    0x40cbe7: mov      dword ptr [rax], 2
    0x40cbed: mov      rax, qword ptr [rbp - 8]
    0x40cbf1: mov      rdx, qword ptr [rbp - 0x20]
    0x40cbf5: mov      qword ptr [rax + 8], rdx
    0x40cbf9: mov      rax, qword ptr [rbp - 8]
    0x40cbfd: mov      dword ptr [rax + 0x10], 0
    0x40cc04: mov      rax, qword ptr [rbp - 8]
    0x40cc08: mov      rdx, qword ptr [rbp - 0x28]
    0x40cc0c: mov      qword ptr [rax + 0x18], rdx
    0x40cc10: mov      rax, qword ptr [rbp - 8]
    0x40cc14: jmp      0x40cc82

; --- Block 0x40cc16 [BODY] 14 insns, callees: (none)
    0x40cc16: mov      rax, qword ptr [rbp - 8]
    0x40cc1a: mov      dword ptr [rax], 2
    0x40cc20: mov      rax, qword ptr [rbp - 8]
    0x40cc24: mov      rdx, qword ptr [rbp - 0x10]
    0x40cc28: mov      qword ptr [rax + 8], rdx
    0x40cc2c: mov      rax, qword ptr [rbp - 0x38]
    0x40cc30: mov      edx, dword ptr [rax + 0x10]
    0x40cc33: mov      rax, qword ptr [rbp - 8]
    0x40cc37: mov      dword ptr [rax + 0x10], edx
    0x40cc3a: mov      rax, qword ptr [rbp - 8]
    0x40cc3e: mov      rdx, qword ptr [rbp - 0x18]
    0x40cc42: mov      qword ptr [rax + 0x18], rdx
    ... +2 more instructions

; --- Block 0x40cc4c [BODY] 6 insns, callees: em_20
    0x40cc4c: mov      rax, qword ptr [rbp - 8]
    0x40cc50: mov      dword ptr [rax], 3
    0x40cc56: mov      rax, qword ptr [rbp - 0x38]
    0x40cc5a: mov      rax, qword ptr [rax + 8]
    0x40cc5e: mov      rdi, rax
    0x40cc61: call     0x40ca2c

; --- Block 0x40cc66 [LOOP_HEADER] 4 insns, callees: (none)
    0x40cc66: mov      rdx, qword ptr [rbp - 8]
    0x40cc6a: mov      qword ptr [rdx + 8], rax
    0x40cc6e: mov      rax, qword ptr [rbp - 8]
    0x40cc72: jmp      0x40cc82

; --- Block 0x40cc74 [BODY] 5 insns, callees: (none)
    0x40cc74: mov      rax, qword ptr [rbp - 8]
    0x40cc78: mov      dword ptr [rax], 0
    0x40cc7e: mov      rax, qword ptr [rbp - 8]
    0x40cc82: leave    
    0x40cc83: ret      

; --- Block 0x40cc82 [BODY] 2 insns, callees: (none)
    0x40cc82: leave    
    0x40cc83: ret      

```

**O2 blocks** (25 total):

```asm
; --- Block 0x40a320 [LOOP_HEADER] 7 insns, callees: (none)
    0x40a320: push     r14
    0x40a322: push     r13
    0x40a324: push     r12
    0x40a326: push     rbp
    0x40a327: push     rbx
    0x40a328: test     rdi, rdi
    0x40a32b: je       0x40a410

; --- Block 0x40a331 [BODY] 4 insns, callees: sub_4010c0
    0x40a331: mov      rbx, rdi
    0x40a334: mov      esi, 0x58
    0x40a339: mov      edi, 1
    0x40a33e: call     0x4010c0

; --- Block 0x40a343 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a343: mov      r12, rax
    0x40a346: mov      eax, dword ptr [rbx]
    0x40a348: cmp      eax, 2
    0x40a34b: je       0x40a3b0

; --- Block 0x40a34d [BODY] 1 insns, callees: (none)
    0x40a34d: ja       0x40a380

; --- Block 0x40a34f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a34f: test     eax, eax
    0x40a351: je       0x40a3f8

; --- Block 0x40a357 [BODY] 4 insns, callees: sub_401050
    0x40a357: mov      dword ptr [r12], 1
    0x40a35f: lea      rsi, [rbx + 8]
    0x40a363: lea      rdi, [r12 + 8]
    0x40a368: call     0x401050

; --- Block 0x40a36d [LOOP_HEADER] 7 insns, callees: (none)
    0x40a36d: pop      rbx
    0x40a36e: mov      rax, r12
    0x40a371: pop      rbp
    0x40a372: pop      r12
    0x40a374: pop      r13
    0x40a376: pop      r14
    0x40a378: ret      

; --- Block 0x40a380 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a380: cmp      eax, 3
    0x40a383: jne      0x40a36d

; --- Block 0x40a385 [BODY] 3 insns, callees: em_20
    0x40a385: mov      dword ptr [r12], 3
    0x40a38d: mov      rdi, qword ptr [rbx + 8]
    0x40a391: call     0x40a320

; --- Block 0x40a396 [LOOP_HEADER] 8 insns, callees: (none)
    0x40a396: mov      qword ptr [r12 + 8], rax
    0x40a39b: mov      rax, r12
    0x40a39e: pop      rbx
    0x40a39f: pop      rbp
    0x40a3a0: pop      r12
    0x40a3a2: pop      r13
    0x40a3a4: pop      r14
    0x40a3a6: ret      

; --- Block 0x40a3b0 [BODY] 2 insns, callees: em_20
    0x40a3b0: mov      rdi, qword ptr [rbx + 8]
    0x40a3b4: call     0x40a320

; --- Block 0x40a3b9 [LOOP_HEADER] 3 insns, callees: em_20
    0x40a3b9: mov      rdi, qword ptr [rbx + 0x18]
    0x40a3bd: mov      r13, rax
    0x40a3c0: call     0x40a320

; --- Block 0x40a3c5 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40a3c5: mov      rbp, rax
    0x40a3c8: mov      eax, dword ptr [rbx + 0x10]
    0x40a3cb: cmp      eax, 2
    0x40a3ce: je       0x40a420

; --- Block 0x40a3d0 [LOOP_HEADER] 11 insns, callees: (none)
    0x40a3d0: mov      dword ptr [r12 + 0x10], eax
    0x40a3d5: mov      rax, r12
    0x40a3d8: mov      dword ptr [r12], 2
    0x40a3e0: mov      qword ptr [r12 + 8], r13
    0x40a3e5: mov      qword ptr [r12 + 0x18], rbp
    0x40a3ea: pop      rbx
    0x40a3eb: pop      rbp
    0x40a3ec: pop      r12
    0x40a3ee: pop      r13
    0x40a3f0: pop      r14
    0x40a3f2: ret      

; --- Block 0x40a3f8 [BODY] 9 insns, callees: (none)
    0x40a3f8: mov      rax, qword ptr [rbx + 8]
    0x40a3fc: mov      qword ptr [r12 + 8], rax
    0x40a401: mov      rax, r12
    0x40a404: pop      rbx
    0x40a405: pop      rbp
    0x40a406: pop      r12
    0x40a408: pop      r13
    0x40a40a: pop      r14
    0x40a40c: ret      

; --- Block 0x40a410 [BODY] 8 insns, callees: (none)
    0x40a410: xor      r12d, r12d
    0x40a413: pop      rbx
    0x40a414: pop      rbp
    0x40a415: mov      rax, r12
    0x40a418: pop      r12
    0x40a41a: pop      r13
    0x40a41c: pop      r14
    0x40a41e: ret      

; --- Block 0x40a420 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a420: cmp      dword ptr [rbp], 2
    0x40a424: jne      0x40a3d0

; --- Block 0x40a426 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40a426: mov      edx, dword ptr [rbp + 0x10]
    0x40a429: test     edx, edx
    0x40a42b: jne      0x40a3d0

; --- Block 0x40a42d [BODY] 3 insns, callees: sub_4010c0
    0x40a42d: mov      esi, 0x58
    0x40a432: mov      edi, 1
    0x40a437: call     0x4010c0

; --- Block 0x40a43c [BODY] 4 insns, callees: c_clone_expr
    0x40a43c: mov      rdi, r13
    0x40a43f: mov      dword ptr [rax], 2
    0x40a445: mov      r14, rax
    0x40a448: call     0x402670

; --- Block 0x40a44d [BODY] 4 insns, callees: c_clone_expr
    0x40a44d: mov      dword ptr [r14 + 0x10], 2
    0x40a455: mov      qword ptr [r14 + 8], rax
    0x40a459: mov      rdi, qword ptr [rbp + 8]
    0x40a45d: call     0x402670

; --- Block 0x40a462 [BODY] 4 insns, callees: sub_4010c0
    0x40a462: mov      esi, 0x58
    0x40a467: mov      edi, 1
    0x40a46c: mov      qword ptr [r14 + 0x18], rax
    0x40a470: call     0x4010c0

; --- Block 0x40a475 [BODY] 6 insns, callees: c_clone_expr
    0x40a475: mov      rdi, qword ptr [rbp + 0x18]
    0x40a479: mov      dword ptr [rax], 2
    0x40a47f: mov      rbx, rax
    0x40a482: mov      qword ptr [rax + 8], r13
    0x40a486: mov      dword ptr [rax + 0x10], 2
    0x40a48d: call     0x402670

; --- Block 0x40a492 [BODY] 3 insns, callees: c_free_expr
    0x40a492: mov      rdi, rbp
    0x40a495: mov      qword ptr [rbx + 0x18], rax
    0x40a499: call     0x4025b0

; --- Block 0x40a49e [BODY] 5 insns, callees: (none)
    0x40a49e: mov      dword ptr [r12], 2
    0x40a4a6: mov      qword ptr [r12 + 8], r14
    0x40a4ab: mov      dword ptr [r12 + 0x10], 0
    0x40a4b4: mov      qword ptr [r12 + 0x18], rbx
    0x40a4b9: jmp      0x40a36d

```

**Hungarian matching result** (mean similarity: 0.799):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40ca6b` | BOUNDS_CHECK | `0x40a380` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40ca74` | BOUNDS_CHECK | `0x40a420` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40ca82` | BOUNDS_CHECK | `0x40a34f` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40cb19` | BOUNDS_CHECK | `0x40a343` | BOUNDS_CHECK | 0.985 | GOOD |
| `0x40cb46` | BODY | `0x40a475` | BODY | 0.972 | GOOD |
| `0x40cb05` | LOOP_HEADER | `0x40a3c5` | BOUNDS_CHECK | 0.950 | GOOD |
| `0x40cb28` | BOUNDS_CHECK | `0x40a426` | BOUNDS_CHECK | 0.884 | GOOD |
| `0x40cae1` | BODY | `0x40a3b9` | LOOP_HEADER | 0.872 | GOOD |
| `0x40cc4c` | BODY | `0x40a385` | BODY | 0.858 | GOOD |
| `0x40cbcf` | BODY | `0x40a492` | BODY | 0.837 | GOOD |
| `0x40cb60` | BODY | `0x40a43c` | BODY | 0.828 | GOOD |
| `0x40ca49` | BODY | `0x40a42d` | BODY | 0.826 | GOOD |
| `0x40cc16` | BODY | `0x40a49e` | BODY | 0.816 | GOOD |
| `0x40cb9a` | BODY | `0x40a44d` | BODY | 0.811 | GOOD |
| `0x40cb37` | BODY | `0x40a462` | BODY | 0.764 | GOOD |
| `0x40cb83` | BODY | `0x40a331` | BODY | 0.756 | GOOD |
| `0x40cad8` | BODY | `0x40a3b0` | BODY | 0.741 | GOOD |
| `0x40cbe3` | BODY | `0x40a3d0` | LOOP_HEADER | 0.741 | GOOD |
| `0x40ca90` | BODY | `0x40a410` | BODY | 0.674 | PARTIAL |
| `0x40ca8b` | BODY | `0x40a34d` | BODY | 0.662 | PARTIAL |
| `0x40cc74` | BODY | `0x40a396` | LOOP_HEADER | 0.646 | PARTIAL |
| `0x40ca86` | BOUNDS_CHECK | `0x40a320` | LOOP_HEADER | 0.644 | PARTIAL |
| `0x40cab3` | BODY | `0x40a357` | BODY | 0.618 | PARTIAL |
| `0x40caf1` | LOOP_HEADER | `0x40a36d` | LOOP_HEADER | 0.585 | PARTIAL |
| `0x40cc66` | LOOP_HEADER | `0x40a3f8` | BODY | 0.497 | PARTIAL |
| `0x40ca2c` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ca3f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ca58` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ca79` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40cc82` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `em_10`

### Rust `em_10` — O0: 9 blocks, O2: 7 blocks

**O0 blocks** (9 total):

```asm
; --- Block 0x44d330 [BODY] 7 insns, callees: alloc::vec::Vec<T>::new
    0x44d330: sub      rsp, 0x398
    0x44d337: mov      qword ptr [rsp + 0x1d8], rdi
    0x44d33f: mov      qword ptr [rsp + 0x1e0], rsi
    0x44d347: mov      qword ptr [rsp + 0x310], rdi
    0x44d34f: mov      qword ptr [rsp + 0x318], rsi
    0x44d357: lea      rdi, [rsp + 0x1f8]
    0x44d35f: call     0x4a5120

; --- Block 0x44d364 [BODY] 4 insns, callees: core::slice::iter::<impl core::iter::traits::collect::IntoIterator for &[T]>::into_iter
    0x44d364: mov      rdi, qword ptr [rsp + 0x1d8]
    0x44d36c: mov      rsi, qword ptr [rsp + 0x1e0]
    0x44d374: mov      qword ptr [rsp + 0x210], 0
    0x44d380: call     0x4a12a0

; --- Block 0x44d385 [BODY] 3 insns, callees: (none)
    0x44d385: mov      qword ptr [rsp + 0x1e8], rdx
    0x44d38d: mov      qword ptr [rsp + 0x1f0], rax
    0x44d395: jmp      0x44d3bf

; --- Block 0x44d3bf [BODY] 6 insns, callees: <core::slice::iter::Iter<T> as core::iter::traits::iterator::Iterator>::next
    0x44d3bf: mov      rax, qword ptr [rsp + 0x1e8]
    0x44d3c7: mov      rcx, qword ptr [rsp + 0x1f0]
    0x44d3cf: mov      qword ptr [rsp + 0x218], rcx
    0x44d3d7: mov      qword ptr [rsp + 0x220], rax
    0x44d3df: lea      rdi, [rsp + 0x218]
    0x44d3e7: call     0x484790

; --- Block 0x44d3ec [BODY] 2 insns, callees: (none)
    0x44d3ec: mov      qword ptr [rsp + 0x1d0], rax
    0x44d3f4: jmp      0x44d3f6

; --- Block 0x44d3f6 [BODY] 9 insns, callees: (none)
    0x44d3f6: mov      rax, qword ptr [rsp + 0x1d0]
    0x44d3fe: mov      qword ptr [rsp + 0x228], rax
    0x44d406: mov      rdx, qword ptr [rsp + 0x228]
    0x44d40e: mov      eax, 1
    0x44d413: xor      ecx, ecx
    0x44d415: cmp      rdx, 0
    0x44d419: cmove    rax, rcx
    0x44d41d: test     rax, 1
    0x44d423: je       0x44d460

; --- Block 0x44d425 [BODY] 10 insns, callees: (none)
    0x44d425: mov      rax, qword ptr [rsp + 0x228]
    0x44d42d: mov      qword ptr [rsp + 0x1c0], rax
    0x44d435: mov      qword ptr [rsp + 0x330], rax
    0x44d43d: mov      rax, qword ptr [rax]
    0x44d440: mov      qword ptr [rsp + 0x1c8], rax
    0x44d448: mov      rcx, qword ptr [rsp + 0x1c8]
    0x44d450: lea      rax, [rip - 0x4097f]
    0x44d457: movsxd   rcx, dword ptr [rax + rcx*4]
    0x44d45b: add      rax, rcx
    0x44d45e: jmp      rax

; --- Block 0x44d460 [DROP_GLUE] 4 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<(alloc::string::String,rust_bench::CVal)>>
    0x44d460: mov      rax, qword ptr [rsp + 0x210]
    0x44d468: mov      qword ptr [rsp + 0x1b8], rax
    0x44d470: lea      rdi, [rsp + 0x1f8]
    0x44d478: call     0x497720

; --- Block 0x44d47d [EPILOGUE] 3 insns, callees: (none)
    0x44d47d: mov      rax, qword ptr [rsp + 0x1b8]
    0x44d485: add      rsp, 0x398
    0x44d48c: ret      

```

**O2 blocks** (7 total):

```asm
; --- Block 0x426040 [BODY] 12 insns, callees: (none)
    0x426040: push     rbp
    0x426041: push     r15
    0x426043: push     r14
    0x426045: push     r13
    0x426047: push     r12
    0x426049: push     rbx
    0x42604a: sub      rsp, 0x88
    0x426051: mov      qword ptr [rsp + 0x10], 0
    0x42605a: mov      qword ptr [rsp + 0x18], 8
    0x426063: mov      qword ptr [rsp + 0x20], 0
    0x42606c: test     rsi, rsi
    0x42606f: je       0x4267f1

; --- Block 0x426075 [BODY] 9 insns, callees: (none)
    0x426075: mov      r13, rdi
    0x426078: lea      rax, [rsi + rsi*4]
    0x42607c: shl      rax, 4
    0x426080: add      rax, rdi
    0x426083: mov      qword ptr [rsp + 0x80], rax
    0x42608b: lea      rax, [rdi + 0x50]
    0x42608f: movabs   r12, 0x7ffffffffffffff8
    0x426099: mov      qword ptr [rsp + 0x28], 0
    0x4260a2: jmp      0x426104

; --- Block 0x426104 [BODY] 7 insns, callees: (none)
    0x426104: mov      rbp, r13
    0x426107: mov      r13, rax
    0x42610a: mov      rax, qword ptr [rbp]
    0x42610e: lea      rcx, [rip - 0x1f779]
    0x426115: movsxd   rax, dword ptr [rcx + rax*4]
    0x426119: add      rax, rcx
    0x42611c: jmp      rax

; --- Block 0x4267f1 [BODY] 3 insns, callees: <alloc::vec::Vec<T,A> as core::ops::drop::Drop>::drop
    0x4267f1: mov      qword ptr [rsp + 0x28], 0
    0x4267fa: lea      rdi, [rsp + 0x10]
    0x4267ff: call     0x4373c0

; --- Block 0x426804 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x426804: mov      rax, qword ptr [rsp + 0x10]
    0x426809: test     rax, rax
    0x42680c: je       0x426822

; --- Block 0x42680e [BODY] 4 insns, callees: (none)
    0x42680e: imul     rsi, rax, 0x38
    0x426812: mov      rdi, qword ptr [rsp + 0x18]
    0x426817: mov      edx, 8
    0x42681c: call     qword ptr [rip + 0x5ec06]

; --- Block 0x426822 [BODY] 9 insns, callees: (none)
    0x426822: mov      rax, qword ptr [rsp + 0x28]
    0x426827: add      rsp, 0x88
    0x42682e: pop      rbx
    0x42682f: pop      r12
    0x426831: pop      r13
    0x426833: pop      r14
    0x426835: pop      r15
    0x426837: pop      rbp
    0x426838: ret      

```

**Hungarian matching result** (mean similarity: 0.648):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x44d460` | DROP_GLUE | `0x4267f1` | BODY | 0.878 | GOOD |
| `0x44d425` | BODY | `0x426104` | BODY | 0.852 | GOOD |
| `0x44d385` | BODY | `0x426804` | BOUNDS_CHECK | 0.713 | GOOD |
| `0x44d364` | BODY | `0x42680e` | BODY | 0.645 | PARTIAL |
| `0x44d3f6` | BODY | `0x426040` | BODY | 0.498 | PARTIAL |
| `0x44d47d` | EPILOGUE | `0x426822` | BODY | 0.483 | PARTIAL |
| `0x44d330` | BODY | `0x426075` | BODY | 0.464 | PARTIAL |
| `0x44d3bf` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x44d3ec` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `em_10` — O0: 38 blocks, O2: 29 blocks

**O0 blocks** (38 total):

```asm
; --- Block 0x40a899 [LOOP_HEADER] 10 insns, callees: (none)
    0x40a899: push     rbp
    0x40a89a: mov      rbp, rsp
    0x40a89d: push     rbx
    0x40a89e: sub      rsp, 0x3258
    0x40a8a5: mov      qword ptr [rbp - 0x3258], rdi
    0x40a8ac: mov      qword ptr [rbp - 0x3260], rsi
    0x40a8b3: mov      qword ptr [rbp - 0x18], 0
    0x40a8bb: mov      qword ptr [rbp - 0x20], 0
    0x40a8c3: mov      qword ptr [rbp - 0x28], 0
    0x40a8cb: jmp      0x40ad6d

; --- Block 0x40a8d0 [LOOP_HEADER] 13 insns, callees: (none)
    0x40a8d0: mov      rdx, qword ptr [rbp - 0x28]
    0x40a8d4: mov      rax, rdx
    0x40a8d7: add      rax, rax
    0x40a8da: add      rax, rdx
    0x40a8dd: shl      rax, 2
    0x40a8e1: add      rax, rdx
    0x40a8e4: shl      rax, 4
    0x40a8e8: mov      rdx, rax
    0x40a8eb: mov      rax, qword ptr [rbp - 0x3258]
    0x40a8f2: add      rax, rdx
    0x40a8f5: mov      eax, dword ptr [rax]
    0x40a8f7: cmp      eax, 3
    ... +1 more instructions

; --- Block 0x40a900 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a900: cmp      eax, 3
    0x40a903: ja       0x40ad68

; --- Block 0x40a909 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a909: cmp      eax, 2
    0x40a90c: je       0x40abd7

; --- Block 0x40a912 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a912: cmp      eax, 2
    0x40a915: ja       0x40ad68

; --- Block 0x40a91b [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a91b: test     eax, eax
    0x40a91d: je       0x40a92d

; --- Block 0x40a91f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a91f: cmp      eax, 1
    0x40a922: je       0x40aa74

; --- Block 0x40a928 [BODY] 1 insns, callees: (none)
    0x40a928: jmp      0x40ad68

; --- Block 0x40a92d [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40a92d: cmp      qword ptr [rbp - 0x18], 0x3f
    0x40a932: ja       0x40ad64

; --- Block 0x40a938 [BODY] 18 insns, callees: sub_401050
    0x40a938: mov      rdx, qword ptr [rbp - 0x28]
    0x40a93c: mov      rax, rdx
    0x40a93f: add      rax, rax
    0x40a942: add      rax, rdx
    0x40a945: shl      rax, 2
    0x40a949: add      rax, rdx
    0x40a94c: shl      rax, 4
    0x40a950: mov      rdx, rax
    0x40a953: mov      rax, qword ptr [rbp - 0x3258]
    0x40a95a: add      rax, rdx
    0x40a95d: lea      rdx, [rax + 8]
    0x40a961: lea      rcx, [rbp - 0x1050]
    ... +6 more instructions

; --- Block 0x40a97e [BODY] 54 insns, callees: (none)
    0x40a97e: mov      rdx, qword ptr [rbp - 0x28]
    0x40a982: mov      rax, rdx
    0x40a985: add      rax, rax
    0x40a988: add      rax, rdx
    0x40a98b: shl      rax, 2
    0x40a98f: add      rax, rdx
    0x40a992: shl      rax, 4
    0x40a996: mov      rdx, rax
    0x40a999: mov      rax, qword ptr [rbp - 0x3258]
    0x40a9a0: add      rdx, rax
    0x40a9a3: mov      rcx, qword ptr [rbp - 0x18]
    0x40a9a7: mov      rax, rcx
    ... +42 more instructions

; --- Block 0x40aa74 [BODY] 16 insns, callees: c_lookup
    0x40aa74: mov      rdx, qword ptr [rbp - 0x28]
    0x40aa78: mov      rax, rdx
    0x40aa7b: add      rax, rax
    0x40aa7e: add      rax, rdx
    0x40aa81: shl      rax, 2
    0x40aa85: add      rax, rdx
    0x40aa88: shl      rax, 4
    0x40aa8c: mov      rdx, rax
    0x40aa8f: mov      rax, qword ptr [rbp - 0x3258]
    0x40aa96: add      rax, rdx
    0x40aa99: lea      rcx, [rax + 8]
    0x40aa9d: mov      rdx, qword ptr [rbp - 0x18]
    ... +4 more instructions

; --- Block 0x40aab7 [BODY] 17 insns, callees: c_lookup
    0x40aab7: mov      qword ptr [rbp - 0x30], rax
    0x40aabb: mov      rdx, qword ptr [rbp - 0x28]
    0x40aabf: mov      rax, rdx
    0x40aac2: add      rax, rax
    0x40aac5: add      rax, rdx
    0x40aac8: shl      rax, 2
    0x40aacc: add      rax, rdx
    0x40aacf: shl      rax, 4
    0x40aad3: mov      rdx, rax
    0x40aad6: mov      rax, qword ptr [rbp - 0x3258]
    0x40aadd: add      rax, rdx
    0x40aae0: lea      rcx, [rax + 0x48]
    ... +5 more instructions

; --- Block 0x40aafe [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40aafe: mov      qword ptr [rbp - 0x38], rax
    0x40ab02: cmp      qword ptr [rbp - 0x30], -0x1869f
    0x40ab0a: jne      0x40ab14

; --- Block 0x40ab0c [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40ab0c: mov      qword ptr [rbp - 0x30], 0
    0x40ab14: cmp      qword ptr [rbp - 0x38], -0x1869f
    0x40ab1c: jne      0x40ab26

; --- Block 0x40ab14 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ab14: cmp      qword ptr [rbp - 0x38], -0x1869f
    0x40ab1c: jne      0x40ab26

; --- Block 0x40ab1e [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40ab1e: mov      qword ptr [rbp - 0x38], 0
    0x40ab26: cmp      qword ptr [rbp - 0x18], 0x3f
    0x40ab2b: ja       0x40ad67

; --- Block 0x40ab26 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ab26: cmp      qword ptr [rbp - 0x18], 0x3f
    0x40ab2b: ja       0x40ad67

; --- Block 0x40ab31 [BODY] 18 insns, callees: sub_401050
    0x40ab31: mov      rdx, qword ptr [rbp - 0x28]
    0x40ab35: mov      rax, rdx
    0x40ab38: add      rax, rax
    0x40ab3b: add      rax, rdx
    0x40ab3e: shl      rax, 2
    0x40ab42: add      rax, rdx
    0x40ab45: shl      rax, 4
    0x40ab49: mov      rdx, rax
    0x40ab4c: mov      rax, qword ptr [rbp - 0x3258]
    0x40ab53: add      rax, rdx
    0x40ab56: lea      rdx, [rax + 0x88]
    0x40ab5d: lea      rcx, [rbp - 0x1050]
    ... +6 more instructions

; --- Block 0x40ab7a [BODY] 23 insns, callees: (none)
    0x40ab7a: mov      rdx, qword ptr [rbp - 0x18]
    0x40ab7e: mov      rax, rdx
    0x40ab81: shl      rax, 4
    0x40ab85: add      rax, rdx
    0x40ab88: shl      rax, 3
    0x40ab8c: lea      rax, [rax - 0x10]
    0x40ab90: add      rax, rbp
    0x40ab93: sub      rax, 0x3240
    0x40ab99: mov      dword ptr [rax], 0
    0x40ab9f: mov      rdx, qword ptr [rbp - 0x30]
    0x40aba3: mov      rax, qword ptr [rbp - 0x38]
    0x40aba7: lea      rcx, [rdx + rax]
    ... +11 more instructions

; --- Block 0x40abd7 [BODY] 16 insns, callees: c_lookup
    0x40abd7: mov      rdx, qword ptr [rbp - 0x28]
    0x40abdb: mov      rax, rdx
    0x40abde: add      rax, rax
    0x40abe1: add      rax, rdx
    0x40abe4: shl      rax, 2
    0x40abe8: add      rax, rdx
    0x40abeb: shl      rax, 4
    0x40abef: mov      rdx, rax
    0x40abf2: mov      rax, qword ptr [rbp - 0x3258]
    0x40abf9: add      rax, rdx
    0x40abfc: lea      rcx, [rax + 8]
    0x40ac00: mov      rdx, qword ptr [rbp - 0x18]
    ... +4 more instructions

; --- Block 0x40ac1a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40ac1a: mov      qword ptr [rbp - 0x48], rax
    0x40ac1e: cmp      qword ptr [rbp - 0x48], -0x1869f
    0x40ac26: je       0x40ac2e

; --- Block 0x40ac28 [BODY] 2 insns, callees: (none)
    0x40ac28: mov      rax, qword ptr [rbp - 0x48]
    0x40ac2c: jmp      0x40ac35

; --- Block 0x40ac2e [BODY] 3 insns, callees: (none)
    0x40ac2e: mov      rax, 0xffffffffffffffff
    0x40ac35: add      qword ptr [rbp - 0x20], rax
    0x40ac39: jmp      0x40ad68

; --- Block 0x40ac35 [BODY] 2 insns, callees: (none)
    0x40ac35: add      qword ptr [rbp - 0x20], rax
    0x40ac39: jmp      0x40ad68

; --- Block 0x40ac3e [BODY] 16 insns, callees: c_lookup
    0x40ac3e: mov      rdx, qword ptr [rbp - 0x28]
    0x40ac42: mov      rax, rdx
    0x40ac45: add      rax, rax
    0x40ac48: add      rax, rdx
    0x40ac4b: shl      rax, 2
    0x40ac4f: add      rax, rdx
    0x40ac52: shl      rax, 4
    0x40ac56: mov      rdx, rax
    0x40ac59: mov      rax, qword ptr [rbp - 0x3258]
    0x40ac60: add      rax, rdx
    0x40ac63: lea      rcx, [rax + 8]
    0x40ac67: mov      rdx, qword ptr [rbp - 0x18]
    ... +4 more instructions

; --- Block 0x40ac81 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40ac81: mov      qword ptr [rbp - 0x40], rax
    0x40ac85: cmp      qword ptr [rbp - 0x40], -0x1869f
    0x40ac8d: jne      0x40ac97

; --- Block 0x40ac8f [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40ac8f: mov      qword ptr [rbp - 0x40], 0
    0x40ac97: cmp      qword ptr [rbp - 0x40], 0
    0x40ac9c: jle      0x40ad01

; --- Block 0x40ac97 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40ac97: cmp      qword ptr [rbp - 0x40], 0
    0x40ac9c: jle      0x40ad01

; --- Block 0x40ac9e [BODY] 25 insns, callees: em_10
    0x40ac9e: mov      rdx, qword ptr [rbp - 0x28]
    0x40aca2: mov      rax, rdx
    0x40aca5: add      rax, rax
    0x40aca8: add      rax, rdx
    0x40acab: shl      rax, 2
    0x40acaf: add      rax, rdx
    0x40acb2: shl      rax, 4
    0x40acb6: mov      rdx, rax
    0x40acb9: mov      rax, qword ptr [rbp - 0x3258]
    0x40acc0: add      rax, rdx
    0x40acc3: mov      rcx, qword ptr [rax + 0x50]
    0x40acc7: mov      rdx, qword ptr [rbp - 0x28]
    ... +13 more instructions

; --- Block 0x40acfb [LOOP_HEADER] 2 insns, callees: (none)
    0x40acfb: add      qword ptr [rbp - 0x20], rax
    0x40acff: jmp      0x40ad68

; --- Block 0x40ad01 [BODY] 25 insns, callees: em_10
    0x40ad01: mov      rdx, qword ptr [rbp - 0x28]
    0x40ad05: mov      rax, rdx
    0x40ad08: add      rax, rax
    0x40ad0b: add      rax, rdx
    0x40ad0e: shl      rax, 2
    0x40ad12: add      rax, rdx
    0x40ad15: shl      rax, 4
    0x40ad19: mov      rdx, rax
    0x40ad1c: mov      rax, qword ptr [rbp - 0x3258]
    0x40ad23: add      rax, rdx
    0x40ad26: mov      rcx, qword ptr [rax + 0x60]
    0x40ad2a: mov      rdx, qword ptr [rbp - 0x28]
    ... +13 more instructions

; --- Block 0x40ad5e [LOOP_HEADER] 2 insns, callees: (none)
    0x40ad5e: add      qword ptr [rbp - 0x20], rax
    0x40ad62: jmp      0x40ad68

; --- Block 0x40ad64 [BODY] 2 insns, callees: (none)
    0x40ad64: nop      
    0x40ad65: jmp      0x40ad68

; --- Block 0x40ad67 [PROLOGUE] 1 insns, callees: (none)
    0x40ad67: nop      

; --- Block 0x40ad68 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40ad68: add      qword ptr [rbp - 0x28], 1
    0x40ad6d: mov      rax, qword ptr [rbp - 0x28]
    0x40ad71: cmp      rax, qword ptr [rbp - 0x3260]
    0x40ad78: jb       0x40a8d0

; --- Block 0x40ad6d [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40ad6d: mov      rax, qword ptr [rbp - 0x28]
    0x40ad71: cmp      rax, qword ptr [rbp - 0x3260]
    0x40ad78: jb       0x40a8d0

; --- Block 0x40ad7e [BODY] 4 insns, callees: (none)
    0x40ad7e: mov      rax, qword ptr [rbp - 0x20]
    0x40ad82: mov      rbx, qword ptr [rbp - 8]
    0x40ad86: leave    
    0x40ad87: ret      

```

**O2 blocks** (29 total):

```asm
; --- Block 0x409090 [LOOP_HEADER] 10 insns, callees: (none)
    0x409090: push     r15
    0x409092: push     r14
    0x409094: xor      r14d, r14d
    0x409097: push     r13
    0x409099: push     r12
    0x40909b: push     rbp
    0x40909c: push     rbx
    0x40909d: sub      rsp, 0x3218
    0x4090a4: test     rsi, rsi
    0x4090a7: je       0x409140

; --- Block 0x4090ad [BODY] 7 insns, callees: (none)
    0x4090ad: mov      r12, rsi
    0x4090b0: lea      rbx, [rdi + 8]
    0x4090b4: xor      ebp, ebp
    0x4090b6: xor      r13d, r13d
    0x4090b9: mov      eax, dword ptr [rbx - 8]
    0x4090bc: cmp      eax, 2
    0x4090bf: je       0x4091a8

; --- Block 0x4090b9 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4090b9: mov      eax, dword ptr [rbx - 8]
    0x4090bc: cmp      eax, 2
    0x4090bf: je       0x4091a8

; --- Block 0x4090c5 [BODY] 1 insns, callees: (none)
    0x4090c5: ja       0x409158

; --- Block 0x4090cb [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4090cb: test     eax, eax
    0x4090cd: je       0x4091f0

; --- Block 0x4090d3 [BODY] 5 insns, callees: c_lookup
    0x4090d3: mov      rcx, rbx
    0x4090d6: mov      rdx, r13
    0x4090d9: lea      rdi, [rsp + 0x10]
    0x4090de: lea      rsi, [rsp + 0x1010]
    0x4090e6: call     0x402870

; --- Block 0x4090eb [BODY] 6 insns, callees: c_lookup
    0x4090eb: mov      rdx, r13
    0x4090ee: lea      rcx, [rbx + 0x40]
    0x4090f2: lea      rsi, [rsp + 0x1010]
    0x4090fa: lea      rdi, [rsp + 0x10]
    0x4090ff: mov      r15, rax
    0x409102: call     0x402870

; --- Block 0x409107 [BODY] 8 insns, callees: (none)
    0x409107: mov      rdx, rax
    0x40910a: xor      eax, eax
    0x40910c: cmp      r15, -0x1869f
    0x409113: cmove    r15, rax
    0x409117: cmp      rdx, -0x1869f
    0x40911e: cmove    rdx, rax
    0x409122: cmp      r13, 0x3f
    0x409126: jbe      0x4092d0

; --- Block 0x40912c [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40912c: add      rbp, 1
    0x409130: add      rbx, 0xd0
    0x409137: cmp      r12, rbp
    0x40913a: jne      0x4090b9

; --- Block 0x409140 [LOOP_HEADER] 9 insns, callees: (none)
    0x409140: add      rsp, 0x3218
    0x409147: mov      rax, r14
    0x40914a: pop      rbx
    0x40914b: pop      rbp
    0x40914c: pop      r12
    0x40914e: pop      r13
    0x409150: pop      r14
    0x409152: pop      r15
    0x409154: ret      

; --- Block 0x409158 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409158: cmp      eax, 3
    0x40915b: jne      0x40912c

; --- Block 0x40915d [BODY] 5 insns, callees: c_lookup
    0x40915d: mov      rcx, rbx
    0x409160: mov      rdx, r13
    0x409163: lea      rdi, [rsp + 0x10]
    0x409168: lea      rsi, [rsp + 0x1010]
    0x409170: call     0x402870

; --- Block 0x409175 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x409175: test     rax, rax
    0x409178: jg       0x4092a0

; --- Block 0x40917e [BODY] 5 insns, callees: em_10
    0x40917e: mov      rsi, qword ptr [rbx + 0x58]
    0x409182: mov      rdi, qword ptr [rbx + 0x50]
    0x409186: add      rbp, 1
    0x40918a: add      rbx, 0xd0
    0x409191: call     0x409090

; --- Block 0x409196 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x409196: add      r14, rax
    0x409199: cmp      r12, rbp
    0x40919c: jne      0x4090b9

; --- Block 0x4091a2 [BODY] 1 insns, callees: (none)
    0x4091a2: jmp      0x409140

; --- Block 0x4091a8 [BODY] 5 insns, callees: c_lookup
    0x4091a8: mov      rcx, rbx
    0x4091ab: mov      rdx, r13
    0x4091ae: lea      rdi, [rsp + 0x10]
    0x4091b3: lea      rsi, [rsp + 0x1010]
    0x4091bb: call     0x402870

; --- Block 0x4091c0 [BODY] 8 insns, callees: (none)
    0x4091c0: mov      rdx, 0xffffffffffffffff
    0x4091c7: cmp      rax, -0x1869f
    0x4091cd: cmove    rax, rdx
    0x4091d1: add      rbp, 1
    0x4091d5: add      rbx, 0xd0
    0x4091dc: add      r14, rax
    0x4091df: cmp      r12, rbp
    0x4091e2: jne      0x4090b9

; --- Block 0x4091e8 [BODY] 1 insns, callees: (none)
    0x4091e8: jmp      0x409140

; --- Block 0x4091f0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4091f0: cmp      r13, 0x3f
    0x4091f4: ja       0x40912c

; --- Block 0x4091fa [BODY] 7 insns, callees: sub_401050
    0x4091fa: mov      rax, r13
    0x4091fd: mov      rsi, rbx
    0x409200: add      rbp, 1
    0x409204: add      rbx, 0xd0
    0x40920b: shl      rax, 6
    0x40920f: lea      rdi, [rsp + rax + 0x10]
    0x409214: call     0x401050

; --- Block 0x409219 [BODY] 26 insns, callees: (none)
    0x409219: mov      rdx, r13
    0x40921c: movdqu   xmm1, xmmword ptr [rbx - 0x80]
    0x409221: movdqu   xmm0, xmmword ptr [rbx - 0x90]
    0x409229: shl      rdx, 4
    0x40922d: movdqu   xmm2, xmmword ptr [rbx - 0x70]
    0x409232: movdqu   xmm3, xmmword ptr [rbx - 0x60]
    0x409237: add      rdx, r13
    0x40923a: movdqu   xmm4, xmmword ptr [rbx - 0x50]
    0x40923f: movdqu   xmm5, xmmword ptr [rbx - 0x40]
    0x409244: add      r13, 1
    0x409248: shl      rdx, 3
    0x40924c: movdqu   xmm6, xmmword ptr [rbx - 0x30]
    ... +14 more instructions

; --- Block 0x409296 [BODY] 1 insns, callees: (none)
    0x409296: jmp      0x409140

; --- Block 0x4092a0 [BODY] 5 insns, callees: em_10
    0x4092a0: mov      rsi, qword ptr [rbx + 0x48]
    0x4092a4: mov      rdi, qword ptr [rbx + 0x40]
    0x4092a8: add      rbp, 1
    0x4092ac: add      rbx, 0xd0
    0x4092b3: call     0x409090

; --- Block 0x4092b8 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4092b8: add      r14, rax
    0x4092bb: cmp      r12, rbp
    0x4092be: jne      0x4090b9

; --- Block 0x4092c4 [BODY] 1 insns, callees: (none)
    0x4092c4: jmp      0x409140

; --- Block 0x4092d0 [BODY] 9 insns, callees: sub_401050
    0x4092d0: mov      rax, r13
    0x4092d3: lea      rsi, [rbx + 0x80]
    0x4092da: mov      qword ptr [rsp + 8], rdx
    0x4092df: add      rbp, 1
    0x4092e3: shl      rax, 6
    0x4092e7: add      rbx, 0xd0
    0x4092ee: add      rax, 0x10
    0x4092f2: lea      rdi, [rsp + rax]
    0x4092f6: call     0x401050

; --- Block 0x4092fb [BODY] 11 insns, callees: (none)
    0x4092fb: mov      rax, r13
    0x4092fe: mov      rdx, qword ptr [rsp + 8]
    0x409303: shl      rax, 4
    0x409307: add      rax, r13
    0x40930a: add      r15, rdx
    0x40930d: add      r13, 1
    0x409311: shl      rax, 3
    0x409315: mov      dword ptr [rsp + rax + 0x1010], 0
    0x409320: mov      qword ptr [rsp + rax + 0x1018], r15
    0x409328: cmp      r12, rbp
    0x40932b: jne      0x4090b9

; --- Block 0x409331 [BODY] 1 insns, callees: (none)
    0x409331: jmp      0x409140

```

**Hungarian matching result** (mean similarity: 0.700):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40a900` | BOUNDS_CHECK | `0x409158` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40a91b` | BOUNDS_CHECK | `0x4090cb` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40a91f` | BOUNDS_CHECK | `0x409175` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40a928` | BODY | `0x4091e8` | BODY | 1.000 | GOOD |
| `0x40a92d` | BOUNDS_CHECK | `0x4091f0` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40ad67` | PROLOGUE | `0x4090c5` | BODY | 0.997 | GOOD |
| `0x40a8d0` | LOOP_HEADER | `0x4092fb` | BODY | 0.851 | GOOD |
| `0x40ad64` | BODY | `0x4091a2` | BODY | 0.833 | GOOD |
| `0x40a912` | BOUNDS_CHECK | `0x4090b9` | BOUNDS_CHECK | 0.813 | GOOD |
| `0x40ac8f` | BOUNDS_CHECK | `0x4092b8` | BOUNDS_CHECK | 0.812 | GOOD |
| `0x40ac97` | BOUNDS_CHECK | `0x409196` | BOUNDS_CHECK | 0.760 | GOOD |
| `0x40ad68` | BOUNDS_CHECK | `0x40912c` | BOUNDS_CHECK | 0.664 | PARTIAL |
| `0x40ac35` | BODY | `0x409296` | BODY | 0.662 | PARTIAL |
| `0x40acfb` | LOOP_HEADER | `0x4092c4` | BODY | 0.662 | PARTIAL |
| `0x40ad5e` | LOOP_HEADER | `0x409331` | BODY | 0.662 | PARTIAL |
| `0x40a938` | BODY | `0x4092d0` | BODY | 0.646 | PARTIAL |
| `0x40ab31` | BODY | `0x4091fa` | BODY | 0.634 | PARTIAL |
| `0x40ab7a` | BODY | `0x409219` | BODY | 0.630 | PARTIAL |
| `0x40a909` | BOUNDS_CHECK | `0x4090ad` | BODY | 0.626 | PARTIAL |
| `0x40ad7e` | BODY | `0x4090d3` | BODY | 0.593 | PARTIAL |
| `0x40aafe` | BOUNDS_CHECK | `0x409107` | BODY | 0.575 | PARTIAL |
| `0x40ab0c` | BOUNDS_CHECK | `0x4091c0` | BODY | 0.572 | PARTIAL |
| `0x40ac2e` | BODY | `0x40915d` | BODY | 0.547 | PARTIAL |
| `0x40a899` | LOOP_HEADER | `0x409090` | LOOP_HEADER | 0.541 | PARTIAL |
| `0x40ad6d` | BOUNDS_CHECK | `0x4091a8` | BODY | 0.534 | PARTIAL |
| `0x40ac9e` | BODY | `0x4092a0` | BODY | 0.438 | PARTIAL |
| `0x40ad01` | BODY | `0x40917e` | BODY | 0.438 | PARTIAL |
| `0x40ac28` | BODY | `0x4090eb` | BODY | 0.434 | PARTIAL |
| `0x40aa74` | BODY | `0x409140` | LOOP_HEADER | 0.382 | POOR |
| `0x40a97e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40aab7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ab14` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ab1e` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ab26` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40abd7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ac1a` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ac3e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40ac81` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `em_17`

### Rust `em_17` — O0: 1 blocks, O2: 1 blocks

**O0 blocks** (1 total):

```asm
; --- Block 0x44fd80 [BODY] 16 insns, callees: (none)
    0x44fd80: sub      rsp, 0x78
    0x44fd84: mov      qword ptr [rsp + 0x28], rdi
    0x44fd89: mov      qword ptr [rsp + 0x60], rdi
    0x44fd8e: mov      rax, qword ptr [rdi]
    0x44fd91: movabs   rdx, 0x8000000000000000
    0x44fd9b: mov      rcx, rax
    0x44fd9e: add      rcx, rdx
    0x44fda1: test     rax, rax
    0x44fda4: mov      eax, 4
    0x44fda9: cmovs    rax, rcx
    0x44fdad: mov      qword ptr [rsp + 0x30], rax
    0x44fdb2: mov      rcx, qword ptr [rsp + 0x30]
    ... +4 more instructions

```

**O2 blocks** (1 total):

```asm
; --- Block 0x427ce0 [BODY] 19 insns, callees: (none)
    0x427ce0: push     r15
    0x427ce2: push     r14
    0x427ce4: push     r13
    0x427ce6: push     r12
    0x427ce8: push     rbx
    0x427ce9: mov      r14, rdi
    0x427cec: mov      rax, qword ptr [rdi]
    0x427cef: movabs   r15, 0x8000000000000000
    0x427cf9: mov      rdx, rax
    0x427cfc: xor      rdx, r15
    0x427cff: test     rax, rax
    0x427d02: mov      r12d, 4
    ... +7 more instructions

```

**Hungarian matching result** (mean similarity: 0.674):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x44fd80` | BODY | `0x427ce0` | BODY | 0.674 | PARTIAL |

### C `em_17` — O0: 2 blocks, O2: 1 blocks

**O0 blocks** (2 total):

```asm
; --- Block 0x40c212 [BODY] 7 insns, callees: is_linear
    0x40c212: push     rbp
    0x40c213: mov      rbp, rsp
    0x40c216: sub      rsp, 0x10
    0x40c21a: mov      qword ptr [rbp - 8], rdi
    0x40c21e: mov      rax, qword ptr [rbp - 8]
    0x40c222: mov      rdi, rax
    0x40c225: call     0x40c0f8

; --- Block 0x40c22a [BODY] 2 insns, callees: (none)
    0x40c22a: leave    
    0x40c22b: ret      

```

**O2 blocks** (1 total):

```asm
; --- Block 0x409f00 [BODY] 1 insns, callees: (none)
    0x409f00: jmp      0x4024a0

```

**Hungarian matching result** (mean similarity: 0.491):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40c22a` | BODY | `0x409f00` | BODY | 0.491 | PARTIAL |
| `0x40c212` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `iter_01`

### Rust `iter_01` — O0: 27 blocks, O2: 20 blocks

**O0 blocks** (27 total):

```asm
; --- Block 0x45b3c0 [BODY] 5 insns, callees: core::slice::<impl [T]>::iter
    0x45b3c0: sub      rsp, 0x198
    0x45b3c7: mov      qword ptr [rsp + 0x88], rdx
    0x45b3cf: mov      qword ptr [rsp + 0x130], rdi
    0x45b3d7: mov      qword ptr [rsp + 0x138], rsi
    0x45b3df: call     0x4910a0

; --- Block 0x45b3e4 [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::enumerate
    0x45b3e4: mov      rsi, rax
    0x45b3e7: lea      rdi, [rsp + 0xc8]
    0x45b3ef: mov      qword ptr [rsp + 0x60], rdi
    0x45b3f4: call     0x47f3d0

; --- Block 0x45b3f9 [BODY] 5 insns, callees: core::iter::traits::iterator::Iterator::filter
    0x45b3f9: mov      rsi, qword ptr [rsp + 0x60]
    0x45b3fe: lea      rdi, [rsp + 0xa8]
    0x45b406: mov      qword ptr [rsp + 0x68], rdi
    0x45b40b: lea      rdx, [rsp + 0x88]
    0x45b413: call     0x48dcb0

; --- Block 0x45b418 [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::collect
    0x45b418: mov      rsi, qword ptr [rsp + 0x68]
    0x45b41d: lea      rdi, [rsp + 0x90]
    0x45b425: mov      qword ptr [rsp + 0x70], rdi
    0x45b42a: call     0x47cc30

; --- Block 0x45b42f [BODY] 3 insns, callees: <&alloc::vec::Vec<T,A> as core::iter::traits::collect::IntoIterator>::into_iter
    0x45b42f: mov      rdi, qword ptr [rsp + 0x70]
    0x45b434: mov      qword ptr [rsp + 0xe0], 0
    0x45b440: call     0x4ac260

; --- Block 0x45b445 [BODY] 3 insns, callees: (none)
    0x45b445: mov      qword ptr [rsp + 0x78], rdx
    0x45b44a: mov      qword ptr [rsp + 0x80], rax
    0x45b452: jmp      0x45b47c

; --- Block 0x45b47c [BODY] 6 insns, callees: <core::slice::iter::Iter<T> as core::iter::traits::iterator::Iterator>::next
    0x45b47c: mov      rax, qword ptr [rsp + 0x78]
    0x45b481: mov      rcx, qword ptr [rsp + 0x80]
    0x45b489: mov      qword ptr [rsp + 0xe8], rcx
    0x45b491: mov      qword ptr [rsp + 0xf0], rax
    0x45b499: lea      rdi, [rsp + 0xe8]
    0x45b4a1: call     0x484690

; --- Block 0x45b499 [LOOP_HEADER] 2 insns, callees: <core::slice::iter::Iter<T> as core::iter::traits::iterator::Iterator>::next
    0x45b499: lea      rdi, [rsp + 0xe8]
    0x45b4a1: call     0x484690

; --- Block 0x45b4a6 [BODY] 2 insns, callees: (none)
    0x45b4a6: mov      qword ptr [rsp + 0x58], rax
    0x45b4ab: jmp      0x45b4ad

; --- Block 0x45b4ad [BODY] 9 insns, callees: (none)
    0x45b4ad: mov      rax, qword ptr [rsp + 0x58]
    0x45b4b2: mov      qword ptr [rsp + 0xf8], rax
    0x45b4ba: mov      rdx, qword ptr [rsp + 0xf8]
    0x45b4c2: mov      eax, 1
    0x45b4c7: xor      ecx, ecx
    0x45b4c9: cmp      rdx, 0
    0x45b4cd: cmove    rax, rcx
    0x45b4d1: test     rax, 1
    0x45b4d7: je       0x45b52f

; --- Block 0x45b4d9 [BODY] 15 insns, callees: (none)
    0x45b4d9: mov      rax, qword ptr [rsp + 0xf8]
    0x45b4e1: mov      qword ptr [rsp + 0x158], rax
    0x45b4e9: mov      rcx, qword ptr [rsp + 0xf8]
    0x45b4f1: mov      rcx, qword ptr [rcx + 8]
    0x45b4f5: mov      rcx, qword ptr [rcx]
    0x45b4f8: mov      qword ptr [rsp + 0x40], rcx
    0x45b4fd: mov      qword ptr [rsp + 0x160], rcx
    0x45b505: mov      rcx, qword ptr [rsp + 0xe0]
    0x45b50d: mov      qword ptr [rsp + 0x48], rcx
    0x45b512: mov      rcx, qword ptr [rax]
    0x45b515: mov      rax, rcx
    0x45b518: add      rax, 1
    ... +3 more instructions

; --- Block 0x45b52a [BODY] 1 insns, callees: (none)
    0x45b52a: jmp      0x45b5f8

; --- Block 0x45b52f [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45b52f: lea      rdi, [rsp + 0x90]
    0x45b537: call     0x4ab740

; --- Block 0x45b53c [BODY] 3 insns, callees: (none)
    0x45b53c: mov      qword ptr [rsp + 0x30], rdx
    0x45b541: mov      qword ptr [rsp + 0x38], rax
    0x45b546: jmp      0x45b548

; --- Block 0x45b548 [BODY] 3 insns, callees: core::slice::<impl [T]>::iter
    0x45b548: mov      rsi, qword ptr [rsp + 0x30]
    0x45b54d: mov      rdi, qword ptr [rsp + 0x38]
    0x45b552: call     0x491000

; --- Block 0x45b557 [BODY] 3 insns, callees: (none)
    0x45b557: mov      qword ptr [rsp + 0x20], rdx
    0x45b55c: mov      qword ptr [rsp + 0x28], rax
    0x45b561: jmp      0x45b563

; --- Block 0x45b563 [BODY] 5 insns, callees: core::iter::traits::iterator::Iterator::take
    0x45b563: mov      rdx, qword ptr [rsp + 0x20]
    0x45b568: mov      rsi, qword ptr [rsp + 0x28]
    0x45b56d: lea      rdi, [rsp + 0x118]
    0x45b575: mov      ecx, 5
    0x45b57a: call     0x47e6c0

; --- Block 0x45b57f [BODY] 1 insns, callees: (none)
    0x45b57f: jmp      0x45b581

; --- Block 0x45b581 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::map
    0x45b581: lea      rdi, [rsp + 0x100]
    0x45b589: lea      rsi, [rsp + 0x118]
    0x45b591: call     0x463c80

; --- Block 0x45b596 [BODY] 1 insns, callees: (none)
    0x45b596: jmp      0x45b598

; --- Block 0x45b598 [BODY] 3 insns, callees: <core::iter::adapters::map::Map<I,F> as core::iter::traits::iterator::Iterator>::fold
    0x45b598: lea      rdi, [rsp + 0x100]
    0x45b5a0: mov      esi, 1
    0x45b5a5: call     0x486c30

; --- Block 0x45b5aa [BODY] 2 insns, callees: (none)
    0x45b5aa: mov      qword ptr [rsp + 0x18], rax
    0x45b5af: jmp      0x45b5b1

; --- Block 0x45b5b1 [DROP_GLUE] 9 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<(usize,&u64)>>
    0x45b5b1: mov      rcx, qword ptr [rsp + 0x18]
    0x45b5b6: mov      qword ptr [rsp + 0x150], rcx
    0x45b5be: mov      rax, qword ptr [rsp + 0xe0]
    0x45b5c6: mov      qword ptr [rsp + 0x178], rax
    0x45b5ce: mov      qword ptr [rsp + 0x180], rcx
    0x45b5d6: add      rax, rcx
    0x45b5d9: mov      qword ptr [rsp + 0x10], rax
    0x45b5de: lea      rdi, [rsp + 0x90]
    0x45b5e6: call     0x4971b0

; --- Block 0x45b5eb [EPILOGUE] 3 insns, callees: (none)
    0x45b5eb: mov      rax, qword ptr [rsp + 0x10]
    0x45b5f0: add      rsp, 0x198
    0x45b5f7: ret      

; --- Block 0x45b5f8 [BODY] 7 insns, callees: (none)
    0x45b5f8: mov      rcx, qword ptr [rsp + 0x50]
    0x45b5fd: mov      rax, qword ptr [rsp + 0x40]
    0x45b602: mov      qword ptr [rsp + 0x188], rax
    0x45b60a: mov      qword ptr [rsp + 0x190], rcx
    0x45b612: imul     rax, rcx
    0x45b616: mov      qword ptr [rsp + 8], rax
    0x45b61b: jmp      0x45b631

; --- Block 0x45b61d [BODY] 3 insns, callees: (none)
    0x45b61d: lea      rdi, [rip + 0x9610c]
    0x45b624: mov      rax, qword ptr [rip + 0x99b05]
    0x45b62b: call     rax

; --- Block 0x45b631 [BODY] 9 insns, callees: (none)
    0x45b631: mov      rcx, qword ptr [rsp + 8]
    0x45b636: mov      rax, qword ptr [rsp + 0x48]
    0x45b63b: mov      qword ptr [rsp + 0x168], rax
    0x45b643: mov      qword ptr [rsp + 0x170], rcx
    0x45b64b: add      rax, rcx
    0x45b64e: mov      qword ptr [rsp], rax
    0x45b652: mov      rax, qword ptr [rsp]
    0x45b656: mov      qword ptr [rsp + 0xe0], rax
    0x45b65e: jmp      0x45b499

```

**O2 blocks** (20 total):

```asm
; --- Block 0x42f700 [BODY] 13 insns, callees: <alloc::vec::Vec<T> as alloc::vec::spec_from_iter_nested::SpecFromIterNested<T,I>>::from_iter
    0x42f700: push     r14
    0x42f702: push     rbx
    0x42f703: sub      rsp, 0x48
    0x42f707: mov      qword ptr [rsp + 8], rdx
    0x42f70c: lea      rax, [rdi + rsi*8]
    0x42f710: mov      qword ptr [rsp + 0x28], rdi
    0x42f715: mov      qword ptr [rsp + 0x30], rax
    0x42f71a: mov      qword ptr [rsp + 0x38], 0
    0x42f723: lea      rax, [rsp + 8]
    0x42f728: mov      qword ptr [rsp + 0x40], rax
    0x42f72d: lea      rdi, [rsp + 0x10]
    0x42f732: lea      rsi, [rsp + 0x28]
    ... +1 more instructions

; --- Block 0x42f73c [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42f73c: mov      rdi, qword ptr [rsp + 0x18]
    0x42f741: mov      rax, qword ptr [rsp + 0x20]
    0x42f746: test     rax, rax
    0x42f749: je       0x42f773

; --- Block 0x42f74b [BODY] 8 insns, callees: (none)
    0x42f74b: lea      rcx, [rax - 1]
    0x42f74f: movabs   rsi, 0xfffffffffffffff
    0x42f759: and      rsi, rcx
    0x42f75c: lea      rdx, [rsi + 1]
    0x42f760: mov      ecx, edx
    0x42f762: and      ecx, 3
    0x42f765: cmp      rsi, 3
    0x42f769: jae      0x42f780

; --- Block 0x42f76b [BODY] 3 insns, callees: (none)
    0x42f76b: xor      r14d, r14d
    0x42f76e: mov      rsi, rdi
    0x42f771: jmp      0x42f7e4

; --- Block 0x42f773 [BODY] 3 insns, callees: (none)
    0x42f773: mov      ebx, 1
    0x42f778: xor      r14d, r14d
    0x42f77b: jmp      0x42f8a1

; --- Block 0x42f780 [BODY] 28 insns, callees: (none)
    0x42f780: and      rdx, 0xfffffffffffffffc
    0x42f784: xor      r14d, r14d
    0x42f787: mov      r8, rdi
    0x42f78a: nop      word ptr [rax + rax]
    0x42f790: mov      rsi, qword ptr [r8]
    0x42f793: mov      r9, qword ptr [r8 + 8]
    0x42f797: inc      rsi
    0x42f79a: imul     rsi, qword ptr [r9]
    0x42f79e: mov      r9, qword ptr [r8 + 0x18]
    0x42f7a2: mov      r10, qword ptr [r8 + 0x10]
    0x42f7a6: inc      r10
    0x42f7a9: imul     r10, qword ptr [r9]
    ... +16 more instructions

; --- Block 0x42f790 [BODY] 24 insns, callees: (none)
    0x42f790: mov      rsi, qword ptr [r8]
    0x42f793: mov      r9, qword ptr [r8 + 8]
    0x42f797: inc      rsi
    0x42f79a: imul     rsi, qword ptr [r9]
    0x42f79e: mov      r9, qword ptr [r8 + 0x18]
    0x42f7a2: mov      r10, qword ptr [r8 + 0x10]
    0x42f7a6: inc      r10
    0x42f7a9: imul     r10, qword ptr [r9]
    0x42f7ad: mov      r9, qword ptr [r8 + 0x28]
    0x42f7b1: mov      r11, qword ptr [r8 + 0x20]
    0x42f7b5: inc      r11
    0x42f7b8: imul     r11, qword ptr [r9]
    ... +12 more instructions

; --- Block 0x42f7e4 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42f7e4: test     rcx, rcx
    0x42f7e7: je       0x42f80c

; --- Block 0x42f7e9 [BODY] 11 insns, callees: (none)
    0x42f7e9: shl      ecx, 4
    0x42f7ec: xor      edx, edx
    0x42f7ee: nop      
    0x42f7f0: mov      r8, qword ptr [rsi + rdx]
    0x42f7f4: mov      r9, qword ptr [rsi + rdx + 8]
    0x42f7f9: inc      r8
    0x42f7fc: imul     r8, qword ptr [r9]
    0x42f800: add      r14, r8
    0x42f803: add      rdx, 0x10
    0x42f807: cmp      rcx, rdx
    0x42f80a: jne      0x42f7f0

; --- Block 0x42f7f0 [BODY] 8 insns, callees: (none)
    0x42f7f0: mov      r8, qword ptr [rsi + rdx]
    0x42f7f4: mov      r9, qword ptr [rsi + rdx + 8]
    0x42f7f9: inc      r8
    0x42f7fc: imul     r8, qword ptr [r9]
    0x42f800: add      r14, r8
    0x42f803: add      rdx, 0x10
    0x42f807: cmp      rcx, rdx
    0x42f80a: jne      0x42f7f0

; --- Block 0x42f80c [BODY] 7 insns, callees: (none)
    0x42f80c: cmp      rax, 5
    0x42f810: mov      edx, 5
    0x42f815: cmovb    rdx, rax
    0x42f819: mov      ecx, edx
    0x42f81b: and      ecx, 3
    0x42f81e: cmp      rax, 4
    0x42f822: jae      0x42f82d

; --- Block 0x42f824 [BODY] 3 insns, callees: (none)
    0x42f824: mov      ebx, 1
    0x42f829: xor      eax, eax
    0x42f82b: jmp      0x42f86c

; --- Block 0x42f82d [BODY] 17 insns, callees: (none)
    0x42f82d: and      edx, 4
    0x42f830: lea      rsi, [rdi + 0x38]
    0x42f834: mov      ebx, 1
    0x42f839: xor      eax, eax
    0x42f83b: nop      dword ptr [rax + rax]
    0x42f840: mov      r8, qword ptr [rsi - 0x30]
    0x42f844: imul     rbx, qword ptr [r8]
    0x42f848: mov      r8, qword ptr [rsi - 0x20]
    0x42f84c: imul     rbx, qword ptr [r8]
    0x42f850: mov      r8, qword ptr [rsi - 0x10]
    0x42f854: imul     rbx, qword ptr [r8]
    0x42f858: add      rax, 4
    ... +5 more instructions

; --- Block 0x42f840 [BODY] 12 insns, callees: (none)
    0x42f840: mov      r8, qword ptr [rsi - 0x30]
    0x42f844: imul     rbx, qword ptr [r8]
    0x42f848: mov      r8, qword ptr [rsi - 0x20]
    0x42f84c: imul     rbx, qword ptr [r8]
    0x42f850: mov      r8, qword ptr [rsi - 0x10]
    0x42f854: imul     rbx, qword ptr [r8]
    0x42f858: add      rax, 4
    0x42f85c: mov      r8, qword ptr [rsi]
    0x42f85f: imul     rbx, qword ptr [r8]
    0x42f863: add      rsi, 0x40
    0x42f867: cmp      rdx, rax
    0x42f86a: jne      0x42f840

; --- Block 0x42f86c [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42f86c: test     rcx, rcx
    0x42f86f: je       0x42f8a1

; --- Block 0x42f871 [BODY] 11 insns, callees: (none)
    0x42f871: shl      rax, 4
    0x42f875: add      rax, rdi
    0x42f878: add      rax, 8
    0x42f87c: shl      ecx, 4
    0x42f87f: xor      edx, edx
    0x42f881: nop      word ptr cs:[rax + rax]
    0x42f890: mov      rsi, qword ptr [rax + rdx]
    0x42f894: imul     rbx, qword ptr [rsi]
    0x42f898: add      rdx, 0x10
    0x42f89c: cmp      rcx, rdx
    0x42f89f: jne      0x42f890

; --- Block 0x42f890 [ITERATOR_STATE] 5 insns, callees: (none)
    0x42f890: mov      rsi, qword ptr [rax + rdx]
    0x42f894: imul     rbx, qword ptr [rsi]
    0x42f898: add      rdx, 0x10
    0x42f89c: cmp      rcx, rdx
    0x42f89f: jne      0x42f890

; --- Block 0x42f8a1 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42f8a1: mov      rsi, qword ptr [rsp + 0x10]
    0x42f8a6: test     rsi, rsi
    0x42f8a9: je       0x42f8ba

; --- Block 0x42f8ab [BODY] 3 insns, callees: (none)
    0x42f8ab: shl      rsi, 4
    0x42f8af: mov      edx, 8
    0x42f8b4: call     qword ptr [rip + 0x55b6e]

; --- Block 0x42f8ba [BODY] 6 insns, callees: (none)
    0x42f8ba: add      rbx, r14
    0x42f8bd: mov      rax, rbx
    0x42f8c0: add      rsp, 0x48
    0x42f8c4: pop      rbx
    0x42f8c5: pop      r14
    0x42f8c7: ret      

```

**Hungarian matching result** (mean similarity: 0.566):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x45b445` | BODY | `0x42f76b` | BODY | 0.866 | GOOD |
| `0x45b53c` | BODY | `0x42f773` | BODY | 0.861 | GOOD |
| `0x45b557` | BODY | `0x42f824` | BODY | 0.846 | GOOD |
| `0x45b548` | BODY | `0x42f8a1` | BOUNDS_CHECK | 0.729 | GOOD |
| `0x45b3e4` | BODY | `0x42f73c` | BOUNDS_CHECK | 0.659 | PARTIAL |
| `0x45b4a6` | BODY | `0x42f7e4` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x45b5aa` | BODY | `0x42f86c` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x45b42f` | BODY | `0x42f8ab` | BODY | 0.642 | PARTIAL |
| `0x45b4d9` | BODY | `0x42f840` | BODY | 0.592 | PARTIAL |
| `0x45b4ad` | BODY | `0x42f871` | BODY | 0.519 | PARTIAL |
| `0x45b5eb` | EPILOGUE | `0x42f8ba` | BODY | 0.518 | PARTIAL |
| `0x45b5f8` | BODY | `0x42f7f0` | BODY | 0.499 | PARTIAL |
| `0x45b3c0` | BODY | `0x42f890` | ITERATOR_STATE | 0.489 | PARTIAL |
| `0x45b563` | BODY | `0x42f80c` | BODY | 0.480 | PARTIAL |
| `0x45b47c` | BODY | `0x42f700` | BODY | 0.476 | PARTIAL |
| `0x45b631` | BODY | `0x42f7e9` | BODY | 0.466 | PARTIAL |
| `0x45b3f9` | BODY | `0x42f74b` | BODY | 0.437 | PARTIAL |
| `0x45b5b1` | DROP_GLUE | `0x42f82d` | BODY | 0.393 | POOR |
| `0x45b418` | BODY | `0x42f790` | BODY | 0.302 | POOR |
| `0x45b598` | BODY | `0x42f780` | BODY | 0.251 | POOR |
| `0x45b499` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45b52a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45b52f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45b57f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45b581` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45b596` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45b61d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `iter_01` — O0: 17 blocks, O2: 18 blocks

**O0 blocks** (17 total):

```asm
; --- Block 0x40733d [BODY] 10 insns, callees: sub_4010f0
    0x40733d: push     rbp
    0x40733e: mov      rbp, rsp
    0x407341: sub      rsp, 0x60
    0x407345: mov      qword ptr [rbp - 0x48], rdi
    0x407349: mov      qword ptr [rbp - 0x50], rsi
    0x40734d: mov      qword ptr [rbp - 0x58], rdx
    0x407351: mov      rax, qword ptr [rbp - 0x50]
    0x407355: shl      rax, 3
    0x407359: mov      rdi, rax
    0x40735c: call     0x4010f0

; --- Block 0x407361 [BODY] 5 insns, callees: sub_4010f0
    0x407361: mov      qword ptr [rbp - 0x38], rax
    0x407365: mov      rax, qword ptr [rbp - 0x50]
    0x407369: shl      rax, 3
    0x40736d: mov      rdi, rax
    0x407370: call     0x4010f0

; --- Block 0x407375 [BODY] 4 insns, callees: (none)
    0x407375: mov      qword ptr [rbp - 0x40], rax
    0x407379: mov      qword ptr [rbp - 8], 0
    0x407381: mov      qword ptr [rbp - 0x10], 0
    0x407389: jmp      0x4073f7

; --- Block 0x40738b [LOOP_HEADER] 7 insns, callees: (none)
    0x40738b: mov      rax, qword ptr [rbp - 0x10]
    0x40738f: lea      rdx, [rax*8]
    0x407397: mov      rax, qword ptr [rbp - 0x48]
    0x40739b: add      rax, rdx
    0x40739e: mov      rax, qword ptr [rax]
    0x4073a1: cmp      qword ptr [rbp - 0x58], rax
    0x4073a5: jae      0x4073f2

; --- Block 0x4073a7 [BODY] 21 insns, callees: (none)
    0x4073a7: mov      rax, qword ptr [rbp - 8]
    0x4073ab: lea      rdx, [rax*8]
    0x4073b3: mov      rax, qword ptr [rbp - 0x38]
    0x4073b7: add      rdx, rax
    0x4073ba: mov      rax, qword ptr [rbp - 0x10]
    0x4073be: mov      qword ptr [rdx], rax
    0x4073c1: mov      rax, qword ptr [rbp - 0x10]
    0x4073c5: lea      rdx, [rax*8]
    0x4073cd: mov      rax, qword ptr [rbp - 0x48]
    0x4073d1: add      rax, rdx
    0x4073d4: mov      rdx, qword ptr [rbp - 8]
    0x4073d8: lea      rcx, [rdx*8]
    ... +9 more instructions

; --- Block 0x4073f2 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4073f2: add      qword ptr [rbp - 0x10], 1
    0x4073f7: mov      rax, qword ptr [rbp - 0x10]
    0x4073fb: cmp      rax, qword ptr [rbp - 0x50]
    0x4073ff: jb       0x40738b

; --- Block 0x4073f7 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4073f7: mov      rax, qword ptr [rbp - 0x10]
    0x4073fb: cmp      rax, qword ptr [rbp - 0x50]
    0x4073ff: jb       0x40738b

; --- Block 0x407401 [BODY] 3 insns, callees: (none)
    0x407401: mov      qword ptr [rbp - 0x18], 0
    0x407409: mov      qword ptr [rbp - 0x20], 0
    0x407411: jmp      0x407450

; --- Block 0x407413 [LOOP_HEADER] 17 insns, callees: (none)
    0x407413: mov      rax, qword ptr [rbp - 0x20]
    0x407417: lea      rdx, [rax*8]
    0x40741f: mov      rax, qword ptr [rbp - 0x40]
    0x407423: add      rax, rdx
    0x407426: mov      rax, qword ptr [rax]
    0x407429: mov      rdx, qword ptr [rbp - 0x20]
    0x40742d: lea      rcx, [rdx*8]
    0x407435: mov      rdx, qword ptr [rbp - 0x38]
    0x407439: add      rdx, rcx
    0x40743c: mov      rdx, qword ptr [rdx]
    0x40743f: add      rdx, 1
    0x407443: imul     rax, rdx
    ... +5 more instructions

; --- Block 0x407450 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407450: mov      rax, qword ptr [rbp - 0x20]
    0x407454: cmp      rax, qword ptr [rbp - 8]
    0x407458: jb       0x407413

; --- Block 0x40745a [BODY] 3 insns, callees: (none)
    0x40745a: mov      qword ptr [rbp - 0x28], 1
    0x407462: mov      qword ptr [rbp - 0x30], 0
    0x40746a: jmp      0x407493

; --- Block 0x40746c [LOOP_HEADER] 12 insns, callees: (none)
    0x40746c: mov      rax, qword ptr [rbp - 0x30]
    0x407470: lea      rdx, [rax*8]
    0x407478: mov      rax, qword ptr [rbp - 0x40]
    0x40747c: add      rax, rdx
    0x40747f: mov      rax, qword ptr [rax]
    0x407482: mov      rdx, qword ptr [rbp - 0x28]
    0x407486: imul     rax, rdx
    0x40748a: mov      qword ptr [rbp - 0x28], rax
    0x40748e: add      qword ptr [rbp - 0x30], 1
    0x407493: mov      rax, qword ptr [rbp - 0x30]
    0x407497: cmp      rax, qword ptr [rbp - 8]
    0x40749b: jae      0x4074a4

; --- Block 0x407493 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407493: mov      rax, qword ptr [rbp - 0x30]
    0x407497: cmp      rax, qword ptr [rbp - 8]
    0x40749b: jae      0x4074a4

; --- Block 0x40749d [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40749d: cmp      qword ptr [rbp - 0x30], 4
    0x4074a2: jbe      0x40746c

; --- Block 0x4074a4 [BODY] 3 insns, callees: sub_401030
    0x4074a4: mov      rax, qword ptr [rbp - 0x38]
    0x4074a8: mov      rdi, rax
    0x4074ab: call     0x401030

; --- Block 0x4074b0 [BODY] 3 insns, callees: sub_401030
    0x4074b0: mov      rax, qword ptr [rbp - 0x40]
    0x4074b4: mov      rdi, rax
    0x4074b7: call     0x401030

; --- Block 0x4074bc [BODY] 5 insns, callees: (none)
    0x4074bc: mov      rdx, qword ptr [rbp - 0x18]
    0x4074c0: mov      rax, qword ptr [rbp - 0x28]
    0x4074c4: add      rax, rdx
    0x4074c7: leave    
    0x4074c8: ret      

```

**O2 blocks** (18 total):

```asm
; --- Block 0x407560 [BODY] 11 insns, callees: sub_401100
    0x407560: push     r14
    0x407562: mov      r14, rdx
    0x407565: push     r13
    0x407567: push     r12
    0x407569: mov      r12, rsi
    0x40756c: push     rbp
    0x40756d: lea      rbp, [rsi*8]
    0x407575: push     rbx
    0x407576: mov      rbx, rdi
    0x407579: mov      rdi, rbp
    0x40757c: call     0x401100

; --- Block 0x407581 [BODY] 3 insns, callees: sub_401100
    0x407581: mov      rdi, rbp
    0x407584: mov      r13, rax
    0x407587: call     0x401100

; --- Block 0x40758c [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40758c: mov      rbp, rax
    0x40758f: test     r12, r12
    0x407592: je       0x407630

; --- Block 0x407598 [BODY] 6 insns, callees: (none)
    0x407598: xor      eax, eax
    0x40759a: xor      ecx, ecx
    0x40759c: nop      dword ptr [rax]
    0x4075a0: mov      rdi, qword ptr [rbx + rax*8]
    0x4075a4: cmp      rdi, r14
    0x4075a7: jbe      0x4075b7

; --- Block 0x4075a0 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4075a0: mov      rdi, qword ptr [rbx + rax*8]
    0x4075a4: cmp      rdi, r14
    0x4075a7: jbe      0x4075b7

; --- Block 0x4075a9 [ITERATOR_STATE] 6 insns, callees: (none)
    0x4075a9: mov      qword ptr [r13 + rcx*8], rax
    0x4075ae: mov      qword ptr [rbp + rcx*8], rdi
    0x4075b3: add      rcx, 1
    0x4075b7: add      rax, 1
    0x4075bb: cmp      r12, rax
    0x4075be: jne      0x4075a0

; --- Block 0x4075b7 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4075b7: add      rax, 1
    0x4075bb: cmp      r12, rax
    0x4075be: jne      0x4075a0

; --- Block 0x4075c0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4075c0: test     rcx, rcx
    0x4075c3: je       0x407630

; --- Block 0x4075c5 [BODY] 10 insns, callees: (none)
    0x4075c5: xor      edx, edx
    0x4075c7: xor      esi, esi
    0x4075c9: nop      dword ptr [rax]
    0x4075d0: mov      rax, qword ptr [r13 + rdx*8]
    0x4075d5: add      rax, 1
    0x4075d9: imul     rax, qword ptr [rbp + rdx*8]
    0x4075df: add      rdx, 1
    0x4075e3: add      rsi, rax
    0x4075e6: cmp      rcx, rdx
    0x4075e9: jne      0x4075d0

; --- Block 0x4075d0 [BODY] 7 insns, callees: (none)
    0x4075d0: mov      rax, qword ptr [r13 + rdx*8]
    0x4075d5: add      rax, 1
    0x4075d9: imul     rax, qword ptr [rbp + rdx*8]
    0x4075df: add      rdx, 1
    0x4075e3: add      rsi, rax
    0x4075e6: cmp      rcx, rdx
    0x4075e9: jne      0x4075d0

; --- Block 0x4075eb [BODY] 7 insns, callees: (none)
    0x4075eb: xor      ecx, ecx
    0x4075ed: mov      eax, 1
    0x4075f2: nop      word ptr [rax + rax]
    0x4075f8: imul     rax, qword ptr [rbp + rcx*8]
    0x4075fe: add      rcx, 1
    0x407602: cmp      rcx, rdx
    0x407605: jae      0x40760d

; --- Block 0x4075f8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4075f8: imul     rax, qword ptr [rbp + rcx*8]
    0x4075fe: add      rcx, 1
    0x407602: cmp      rcx, rdx
    0x407605: jae      0x40760d

; --- Block 0x407607 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407607: cmp      rcx, 4
    0x40760b: jbe      0x4075f8

; --- Block 0x40760d [BODY] 3 insns, callees: sub_401030
    0x40760d: lea      r12, [rax + rsi]
    0x407611: mov      rdi, r13
    0x407614: call     0x401030

; --- Block 0x407611 [LOOP_HEADER] 2 insns, callees: sub_401030
    0x407611: mov      rdi, r13
    0x407614: call     0x401030

; --- Block 0x407619 [BODY] 2 insns, callees: sub_401030
    0x407619: mov      rdi, rbp
    0x40761c: call     0x401030

; --- Block 0x407621 [BODY] 7 insns, callees: (none)
    0x407621: pop      rbx
    0x407622: mov      rax, r12
    0x407625: pop      rbp
    0x407626: pop      r12
    0x407628: pop      r13
    0x40762a: pop      r14
    0x40762c: ret      

; --- Block 0x407630 [BODY] 2 insns, callees: (none)
    0x407630: mov      r12d, 1
    0x407636: jmp      0x407611

```

**Hungarian matching result** (mean similarity: 0.763):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40749d` | BOUNDS_CHECK | `0x407607` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x4073f7` | BOUNDS_CHECK | `0x40758c` | BOUNDS_CHECK | 0.977 | GOOD |
| `0x407450` | BOUNDS_CHECK | `0x4075a0` | BOUNDS_CHECK | 0.973 | GOOD |
| `0x4074b0` | BODY | `0x407619` | BODY | 0.898 | GOOD |
| `0x4074a4` | BODY | `0x407611` | LOOP_HEADER | 0.887 | GOOD |
| `0x407401` | BODY | `0x407630` | BODY | 0.871 | GOOD |
| `0x40738b` | LOOP_HEADER | `0x4075eb` | BODY | 0.814 | GOOD |
| `0x4073f2` | BOUNDS_CHECK | `0x4075f8` | BOUNDS_CHECK | 0.812 | GOOD |
| `0x40746c` | LOOP_HEADER | `0x4075c5` | BODY | 0.774 | GOOD |
| `0x407493` | BOUNDS_CHECK | `0x4075c0` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x407413` | LOOP_HEADER | `0x4075d0` | BODY | 0.681 | PARTIAL |
| `0x4073a7` | BODY | `0x4075a9` | ITERATOR_STATE | 0.643 | PARTIAL |
| `0x40745a` | BODY | `0x4075b7` | BOUNDS_CHECK | 0.635 | PARTIAL |
| `0x4074bc` | BODY | `0x407621` | BODY | 0.631 | PARTIAL |
| `0x407375` | BODY | `0x407598` | BODY | 0.568 | PARTIAL |
| `0x40733d` | BODY | `0x407560` | BODY | 0.538 | PARTIAL |
| `0x407361` | BODY | `0x407581` | BODY | 0.523 | PARTIAL |
| — | — | `0x40760d` | BODY | 0.000 | UNMATCHED (O2 only) |

---

## Function `iter_16`

### Rust `iter_16` — O0: 41 blocks, O2: 59 blocks

**O0 blocks** (41 total):

```asm
; --- Block 0x45db20 [BODY] 9 insns, callees: (none)
    0x45db20: sub      rsp, 0x1d8
    0x45db27: mov      qword ptr [rsp + 0xc8], rdi
    0x45db2f: mov      qword ptr [rsp + 0xd0], rsi
    0x45db37: mov      qword ptr [rsp + 0xd8], rdx
    0x45db3f: mov      qword ptr [rsp + 0x1a8], rdi
    0x45db47: mov      qword ptr [rsp + 0x1b0], rsi
    0x45db4f: mov      qword ptr [rsp + 0x1b8], rdx
    0x45db57: cmp      rdx, 0
    0x45db5b: jne      0x45db6b

; --- Block 0x45db5d [BODY] 2 insns, callees: (none)
    0x45db5d: mov      qword ptr [rsp + 0xe0], 0
    0x45db69: jmp      0x45dbdb

; --- Block 0x45db6b [BODY] 7 insns, callees: core::slice::<impl [T]>::chunks
    0x45db6b: mov      rcx, qword ptr [rsp + 0xd8]
    0x45db73: mov      rdx, qword ptr [rsp + 0xd0]
    0x45db7b: mov      rsi, qword ptr [rsp + 0xc8]
    0x45db83: lea      r8, [rip + 0x93d3e]
    0x45db8a: lea      rdi, [rsp + 0x100]
    0x45db92: mov      qword ptr [rsp + 0xa8], rdi
    0x45db9a: call     0x4911d0

; --- Block 0x45db9f [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::collect
    0x45db9f: mov      rsi, qword ptr [rsp + 0xa8]
    0x45dba7: lea      rdi, [rsp + 0xe8]
    0x45dbaf: mov      qword ptr [rsp + 0xb0], rdi
    0x45dbb7: call     0x47ec80

; --- Block 0x45dbbc [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45dbbc: mov      rdi, qword ptr [rsp + 0xb0]
    0x45dbc4: call     0x4ab7b0

; --- Block 0x45dbc9 [BODY] 3 insns, callees: (none)
    0x45dbc9: mov      qword ptr [rsp + 0xb8], rdx
    0x45dbd1: mov      qword ptr [rsp + 0xc0], rax
    0x45dbd9: jmp      0x45dc13

; --- Block 0x45dbdb [EPILOGUE] 3 insns, callees: (none)
    0x45dbdb: mov      rax, qword ptr [rsp + 0xe0]
    0x45dbe3: add      rsp, 0x1d8
    0x45dbea: ret      

; --- Block 0x45dc13 [BODY] 3 insns, callees: core::slice::<impl [T]>::iter
    0x45dc13: mov      rsi, qword ptr [rsp + 0xb8]
    0x45dc1b: mov      rdi, qword ptr [rsp + 0xc0]
    0x45dc23: call     0x490fc0

; --- Block 0x45dc28 [BODY] 3 insns, callees: (none)
    0x45dc28: mov      qword ptr [rsp + 0x98], rdx
    0x45dc30: mov      qword ptr [rsp + 0xa0], rax
    0x45dc38: jmp      0x45dc3a

; --- Block 0x45dc3a [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::map
    0x45dc3a: mov      rsi, qword ptr [rsp + 0x98]
    0x45dc42: mov      rdi, qword ptr [rsp + 0xa0]
    0x45dc4a: call     0x47dbd0

; --- Block 0x45dc4f [BODY] 3 insns, callees: (none)
    0x45dc4f: mov      qword ptr [rsp + 0x88], rdx
    0x45dc57: mov      qword ptr [rsp + 0x90], rax
    0x45dc5f: jmp      0x45dc61

; --- Block 0x45dc61 [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::collect
    0x45dc61: mov      rdx, qword ptr [rsp + 0x88]
    0x45dc69: mov      rsi, qword ptr [rsp + 0x90]
    0x45dc71: lea      rdi, [rsp + 0x118]
    0x45dc79: call     0x487ba0

; --- Block 0x45dc7e [BODY] 1 insns, callees: (none)
    0x45dc7e: jmp      0x45dc80

; --- Block 0x45dc80 [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45dc80: lea      rdi, [rsp + 0xe8]
    0x45dc88: call     0x4ab7b0

; --- Block 0x45dc8d [BODY] 3 insns, callees: (none)
    0x45dc8d: mov      qword ptr [rsp + 0x78], rdx
    0x45dc92: mov      qword ptr [rsp + 0x80], rax
    0x45dc9a: jmp      0x45dcc4

; --- Block 0x45dcc4 [BODY] 3 insns, callees: core::slice::<impl [T]>::iter
    0x45dcc4: mov      rsi, qword ptr [rsp + 0x78]
    0x45dcc9: mov      rdi, qword ptr [rsp + 0x80]
    0x45dcd1: call     0x490fc0

; --- Block 0x45dcd6 [BODY] 3 insns, callees: (none)
    0x45dcd6: mov      qword ptr [rsp + 0x68], rdx
    0x45dcdb: mov      qword ptr [rsp + 0x70], rax
    0x45dce0: jmp      0x45dce2

; --- Block 0x45dce2 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::map
    0x45dce2: mov      rsi, qword ptr [rsp + 0x68]
    0x45dce7: mov      rdi, qword ptr [rsp + 0x70]
    0x45dcec: call     0x47dbb0

; --- Block 0x45dcf1 [BODY] 3 insns, callees: (none)
    0x45dcf1: mov      qword ptr [rsp + 0x58], rdx
    0x45dcf6: mov      qword ptr [rsp + 0x60], rax
    0x45dcfb: jmp      0x45dcfd

; --- Block 0x45dcfd [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::collect
    0x45dcfd: mov      rdx, qword ptr [rsp + 0x58]
    0x45dd02: mov      rsi, qword ptr [rsp + 0x60]
    0x45dd07: lea      rdi, [rsp + 0x130]
    0x45dd0f: call     0x4879f0

; --- Block 0x45dd14 [BODY] 1 insns, callees: (none)
    0x45dd14: jmp      0x45dd16

; --- Block 0x45dd16 [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45dd16: lea      rdi, [rsp + 0x118]
    0x45dd1e: call     0x4ab750

; --- Block 0x45dd23 [BODY] 3 insns, callees: (none)
    0x45dd23: mov      qword ptr [rsp + 0x48], rdx
    0x45dd28: mov      qword ptr [rsp + 0x50], rax
    0x45dd2d: jmp      0x45dd57

; --- Block 0x45dd57 [BODY] 3 insns, callees: core::slice::<impl [T]>::iter
    0x45dd57: mov      rsi, qword ptr [rsp + 0x48]
    0x45dd5c: mov      rdi, qword ptr [rsp + 0x50]
    0x45dd61: call     0x4910a0

; --- Block 0x45dd66 [BODY] 3 insns, callees: (none)
    0x45dd66: mov      qword ptr [rsp + 0x38], rdx
    0x45dd6b: mov      qword ptr [rsp + 0x40], rax
    0x45dd70: jmp      0x45dd72

; --- Block 0x45dd72 [BODY] 6 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45dd72: mov      rax, qword ptr [rsp + 0x38]
    0x45dd77: mov      rcx, qword ptr [rsp + 0x40]
    0x45dd7c: mov      qword ptr [rsp + 0x18], rcx
    0x45dd81: mov      qword ptr [rsp + 0x20], rax
    0x45dd86: lea      rdi, [rsp + 0x130]
    0x45dd8e: call     0x4ab750

; --- Block 0x45dd93 [BODY] 3 insns, callees: (none)
    0x45dd93: mov      qword ptr [rsp + 0x28], rdx
    0x45dd98: mov      qword ptr [rsp + 0x30], rax
    0x45dd9d: jmp      0x45dd9f

; --- Block 0x45dd9f [BODY] 3 insns, callees: core::slice::<impl [T]>::iter
    0x45dd9f: mov      rsi, qword ptr [rsp + 0x28]
    0x45dda4: mov      rdi, qword ptr [rsp + 0x30]
    0x45dda9: call     0x4910a0

; --- Block 0x45ddae [BODY] 3 insns, callees: (none)
    0x45ddae: mov      qword ptr [rsp + 8], rdx
    0x45ddb3: mov      qword ptr [rsp + 0x10], rax
    0x45ddb8: jmp      0x45ddba

; --- Block 0x45ddba [BODY] 6 insns, callees: core::iter::traits::iterator::Iterator::zip
    0x45ddba: mov      r8, qword ptr [rsp + 8]
    0x45ddbf: mov      rcx, qword ptr [rsp + 0x10]
    0x45ddc4: mov      rdx, qword ptr [rsp + 0x20]
    0x45ddc9: mov      rsi, qword ptr [rsp + 0x18]
    0x45ddce: lea      rdi, [rsp + 0x178]
    0x45ddd6: call     0x47e0c0

; --- Block 0x45dddb [BODY] 1 insns, callees: (none)
    0x45dddb: jmp      0x45dddd

; --- Block 0x45dddd [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::map
    0x45dddd: lea      rdi, [rsp + 0x148]
    0x45dde5: lea      rsi, [rsp + 0x178]
    0x45dded: call     0x49aac0

; --- Block 0x45ddf2 [BODY] 1 insns, callees: (none)
    0x45ddf2: jmp      0x45ddf4

; --- Block 0x45ddf4 [BODY] 2 insns, callees: core::iter::traits::iterator::Iterator::sum
    0x45ddf4: lea      rdi, [rsp + 0x148]
    0x45ddfc: call     0x487360

; --- Block 0x45de01 [BODY] 2 insns, callees: (none)
    0x45de01: mov      qword ptr [rsp], rax
    0x45de05: jmp      0x45de07

; --- Block 0x45de07 [DROP_GLUE] 5 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<u64>>
    0x45de07: mov      rax, qword ptr [rsp]
    0x45de0b: mov      qword ptr [rsp + 0x1d0], rax
    0x45de13: mov      qword ptr [rsp + 0xe0], rax
    0x45de1b: lea      rdi, [rsp + 0x130]
    0x45de23: call     0x496820

; --- Block 0x45de28 [BODY] 1 insns, callees: (none)
    0x45de28: jmp      0x45de2a

; --- Block 0x45de2a [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<u64>>
    0x45de2a: lea      rdi, [rsp + 0x118]
    0x45de32: call     0x496820

; --- Block 0x45de37 [BODY] 1 insns, callees: (none)
    0x45de37: jmp      0x45de39

; --- Block 0x45de39 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<&[u64]>>
    0x45de39: lea      rdi, [rsp + 0xe8]
    0x45de41: call     0x496ed0

; --- Block 0x45de46 [BODY] 1 insns, callees: (none)
    0x45de46: jmp      0x45dbdb

```

**O2 blocks** (59 total):

```asm
; --- Block 0x431b30 [BODY] 9 insns, callees: (none)
    0x431b30: push     rbp
    0x431b31: push     r15
    0x431b33: push     r14
    0x431b35: push     r13
    0x431b37: push     r12
    0x431b39: push     rbx
    0x431b3a: sub      rsp, 0x38
    0x431b3e: test     rdx, rdx
    0x431b41: je       0x431d8e

; --- Block 0x431b47 [BODY] 6 insns, callees: <alloc::vec::Vec<T> as alloc::vec::spec_from_iter_nested::SpecFromIterNested<T,I>>::from_iter
    0x431b47: mov      qword ptr [rsp + 0x20], rdi
    0x431b4c: mov      qword ptr [rsp + 0x28], rsi
    0x431b51: mov      qword ptr [rsp + 0x30], rdx
    0x431b56: lea      rdi, [rsp + 8]
    0x431b5b: lea      rsi, [rsp + 0x20]
    0x431b60: call     0x434e50

; --- Block 0x431b65 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431b65: mov      rbx, qword ptr [rsp + 0x10]
    0x431b6a: mov      r13, qword ptr [rsp + 0x18]
    0x431b6f: test     r13, r13
    0x431b72: je       0x431d96

; --- Block 0x431b78 [BODY] 2 insns, callees: (none)
    0x431b78: lea      r14, [r13*8]
    0x431b80: call     qword ptr [rip + 0x53862]

; --- Block 0x431b86 [BODY] 4 insns, callees: (none)
    0x431b86: mov      esi, 8
    0x431b8b: mov      qword ptr [rsp], r14
    0x431b8f: mov      rdi, r14
    0x431b92: call     qword ptr [rip + 0x53858]

; --- Block 0x431b98 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431b98: test     rax, rax
    0x431b9b: je       0x431df5

; --- Block 0x431ba1 [BODY] 3 insns, callees: (none)
    0x431ba1: mov      r15, rax
    0x431ba4: xor      eax, eax
    0x431ba6: jmp      0x431bc2

; --- Block 0x431bb0 [LOOP_HEADER] 5 insns, callees: (none)
    0x431bb0: xor      edi, edi
    0x431bb2: mov      qword ptr [r15 + rax*8], rdi
    0x431bb6: inc      rax
    0x431bb9: cmp      rax, r13
    0x431bbc: je       0x431c51

; --- Block 0x431bb2 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431bb2: mov      qword ptr [r15 + rax*8], rdi
    0x431bb6: inc      rax
    0x431bb9: cmp      rax, r13
    0x431bbc: je       0x431c51

; --- Block 0x431bc2 [BODY] 5 insns, callees: (none)
    0x431bc2: mov      rdx, rax
    0x431bc5: shl      rdx, 4
    0x431bc9: mov      rcx, qword ptr [rbx + rdx + 8]
    0x431bce: test     rcx, rcx
    0x431bd1: je       0x431bb0

; --- Block 0x431bd3 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431bd3: mov      rdx, qword ptr [rbx + rdx]
    0x431bd7: cmp      rcx, 4
    0x431bdb: jae      0x431bf0

; --- Block 0x431bdd [BODY] 3 insns, callees: (none)
    0x431bdd: xor      esi, esi
    0x431bdf: xor      edi, edi
    0x431be1: jmp      0x431c40

; --- Block 0x431bf0 [BODY] 13 insns, callees: (none)
    0x431bf0: mov      rsi, rcx
    0x431bf3: and      rsi, 0xfffffffffffffffc
    0x431bf7: pxor     xmm0, xmm0
    0x431bfb: xor      edi, edi
    0x431bfd: pxor     xmm1, xmm1
    0x431c01: nop      word ptr cs:[rax + rax]
    0x431c10: movdqu   xmm2, xmmword ptr [rdx + rdi*8]
    0x431c15: paddq    xmm0, xmm2
    0x431c19: movdqu   xmm2, xmmword ptr [rdx + rdi*8 + 0x10]
    0x431c1f: paddq    xmm1, xmm2
    0x431c23: add      rdi, 4
    0x431c27: cmp      rsi, rdi
    ... +1 more instructions

; --- Block 0x431c10 [BODY] 7 insns, callees: (none)
    0x431c10: movdqu   xmm2, xmmword ptr [rdx + rdi*8]
    0x431c15: paddq    xmm0, xmm2
    0x431c19: movdqu   xmm2, xmmword ptr [rdx + rdi*8 + 0x10]
    0x431c1f: paddq    xmm1, xmm2
    0x431c23: add      rdi, 4
    0x431c27: cmp      rsi, rdi
    0x431c2a: jne      0x431c10

; --- Block 0x431c2c [BODY] 5 insns, callees: (none)
    0x431c2c: paddq    xmm1, xmm0
    0x431c30: pshufd   xmm0, xmm1, 0xee
    0x431c35: paddq    xmm0, xmm1
    0x431c39: movq     rdi, xmm0
    0x431c3e: jmp      0x431c47

; --- Block 0x431c40 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431c40: add      rdi, qword ptr [rdx + rsi*8]
    0x431c44: inc      rsi
    0x431c47: cmp      rcx, rsi
    0x431c4a: jne      0x431c40

; --- Block 0x431c47 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431c47: cmp      rcx, rsi
    0x431c4a: jne      0x431c40

; --- Block 0x431c4c [BODY] 1 insns, callees: (none)
    0x431c4c: jmp      0x431bb2

; --- Block 0x431c51 [BODY] 1 insns, callees: (none)
    0x431c51: call     qword ptr [rip + 0x53791]

; --- Block 0x431c57 [BODY] 3 insns, callees: (none)
    0x431c57: mov      esi, 8
    0x431c5c: mov      rdi, qword ptr [rsp]
    0x431c60: call     qword ptr [rip + 0x5378a]

; --- Block 0x431c66 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431c66: test     rax, rax
    0x431c69: je       0x431e06

; --- Block 0x431c6f [BODY] 4 insns, callees: (none)
    0x431c6f: movabs   rcx, 0x1fffffffffffffff
    0x431c79: xor      edx, edx
    0x431c7b: lea      rsi, [rcx - 3]
    0x431c7f: jmp      0x431ca2

; --- Block 0x431c90 [LOOP_HEADER] 5 insns, callees: (none)
    0x431c90: xor      edi, edi
    0x431c92: mov      qword ptr [rax + rdx*8], rdi
    0x431c96: inc      rdx
    0x431c99: cmp      rdx, r13
    0x431c9c: je       0x431d7e

; --- Block 0x431c92 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431c92: mov      qword ptr [rax + rdx*8], rdi
    0x431c96: inc      rdx
    0x431c99: cmp      rdx, r13
    0x431c9c: je       0x431d7e

; --- Block 0x431ca2 [BODY] 5 insns, callees: (none)
    0x431ca2: mov      r8, rdx
    0x431ca5: shl      r8, 4
    0x431ca9: mov      rdi, qword ptr [rbx + r8 + 8]
    0x431cae: test     rdi, rdi
    0x431cb1: je       0x431c90

; --- Block 0x431cb3 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431cb3: mov      r9, qword ptr [rbx + r8]
    0x431cb7: cmp      rdi, 1
    0x431cbb: jne      0x431cd0

; --- Block 0x431cbd [BODY] 2 insns, callees: (none)
    0x431cbd: mov      r10, r9
    0x431cc0: jmp      0x431d17

; --- Block 0x431cd0 [BODY] 7 insns, callees: (none)
    0x431cd0: add      rdi, rcx
    0x431cd3: mov      r10, rdi
    0x431cd6: and      r10, rcx
    0x431cd9: mov      r8, qword ptr [r9]
    0x431cdc: dec      r10
    0x431cdf: cmp      r10, 3
    0x431ce3: jae      0x431d1f

; --- Block 0x431ce5 [BODY] 4 insns, callees: (none)
    0x431ce5: xor      r11d, r11d
    0x431ce8: mov      r10, r9
    0x431ceb: and      edi, 3
    0x431cee: je       0x431d17

; --- Block 0x431ceb [LOOP_HEADER] 2 insns, callees: (none)
    0x431ceb: and      edi, 3
    0x431cee: je       0x431d17

; --- Block 0x431cf0 [BODY] 10 insns, callees: (none)
    0x431cf0: lea      r9, [r9 + r11*8]
    0x431cf4: add      r9, 8
    0x431cf8: nop      dword ptr [rax + rax]
    0x431d00: mov      r11, qword ptr [r9]
    0x431d03: cmp      r8, r11
    0x431d06: cmovbe   r8, r11
    0x431d0a: cmovbe   r10, r9
    0x431d0e: add      r9, 8
    0x431d12: dec      rdi
    0x431d15: jne      0x431d00

; --- Block 0x431d00 [BODY] 7 insns, callees: (none)
    0x431d00: mov      r11, qword ptr [r9]
    0x431d03: cmp      r8, r11
    0x431d06: cmovbe   r8, r11
    0x431d0a: cmovbe   r10, r9
    0x431d0e: add      r9, 8
    0x431d12: dec      rdi
    0x431d15: jne      0x431d00

; --- Block 0x431d17 [BODY] 2 insns, callees: (none)
    0x431d17: mov      rdi, qword ptr [r10]
    0x431d1a: jmp      0x431c92

; --- Block 0x431d1f [BODY] 6 insns, callees: (none)
    0x431d1f: mov      r12, rdi
    0x431d22: and      r12, rsi
    0x431d25: mov      rbp, r9
    0x431d28: xor      r11d, r11d
    0x431d2b: mov      r10, r9
    0x431d2e: jmp      0x431d39

; --- Block 0x431d30 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431d30: add      r11, 4
    0x431d34: cmp      r12, r11
    0x431d37: je       0x431ceb

; --- Block 0x431d39 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431d39: mov      r14, qword ptr [rbp + 8]
    0x431d3d: cmp      r8, r14
    0x431d40: ja       0x431d49

; --- Block 0x431d42 [BODY] 5 insns, callees: (none)
    0x431d42: lea      r10, [rbp + 8]
    0x431d46: mov      r8, r14
    0x431d49: mov      r14, qword ptr [rbp + 0x10]
    0x431d4d: cmp      r8, r14
    0x431d50: ja       0x431d59

; --- Block 0x431d49 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431d49: mov      r14, qword ptr [rbp + 0x10]
    0x431d4d: cmp      r8, r14
    0x431d50: ja       0x431d59

; --- Block 0x431d52 [BODY] 5 insns, callees: (none)
    0x431d52: lea      r10, [rbp + 0x10]
    0x431d56: mov      r8, r14
    0x431d59: mov      r14, qword ptr [rbp + 0x18]
    0x431d5d: cmp      r8, r14
    0x431d60: ja       0x431d69

; --- Block 0x431d59 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431d59: mov      r14, qword ptr [rbp + 0x18]
    0x431d5d: cmp      r8, r14
    0x431d60: ja       0x431d69

; --- Block 0x431d62 [ITERATOR_STATE] 6 insns, callees: (none)
    0x431d62: lea      r10, [rbp + 0x18]
    0x431d66: mov      r8, r14
    0x431d69: mov      r14, qword ptr [rbp + 0x20]
    0x431d6d: add      rbp, 0x20
    0x431d71: cmp      r8, r14
    0x431d74: ja       0x431d30

; --- Block 0x431d69 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431d69: mov      r14, qword ptr [rbp + 0x20]
    0x431d6d: add      rbp, 0x20
    0x431d71: cmp      r8, r14
    0x431d74: ja       0x431d30

; --- Block 0x431d76 [BODY] 3 insns, callees: (none)
    0x431d76: mov      r8, r14
    0x431d79: mov      r10, rbp
    0x431d7c: jmp      0x431d30

; --- Block 0x431d7e [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431d7e: cmp      r13, 4
    0x431d82: jae      0x431d9e

; --- Block 0x431d84 [BODY] 3 insns, callees: (none)
    0x431d84: xor      r12d, r12d
    0x431d87: xor      ecx, ecx
    0x431d89: jmp      0x431e55

; --- Block 0x431d8e [BODY] 2 insns, callees: (none)
    0x431d8e: xor      r12d, r12d
    0x431d91: jmp      0x431ea8

; --- Block 0x431d96 [BODY] 2 insns, callees: (none)
    0x431d96: xor      r12d, r12d
    0x431d99: jmp      0x431e8c

; --- Block 0x431d9e [BODY] 17 insns, callees: (none)
    0x431d9e: mov      rcx, r13
    0x431da1: and      rcx, 0xfffffffffffffffc
    0x431da5: pxor     xmm0, xmm0
    0x431da9: xor      edx, edx
    0x431dab: pxor     xmm1, xmm1
    0x431daf: nop      
    0x431db0: movdqu   xmm2, xmmword ptr [r15 + rdx*8]
    0x431db6: paddq    xmm2, xmm0
    0x431dba: movdqu   xmm3, xmmword ptr [r15 + rdx*8 + 0x10]
    0x431dc1: paddq    xmm3, xmm1
    0x431dc5: movdqu   xmm0, xmmword ptr [rax + rdx*8]
    0x431dca: paddq    xmm0, xmm2
    ... +5 more instructions

; --- Block 0x431db0 [BODY] 11 insns, callees: (none)
    0x431db0: movdqu   xmm2, xmmword ptr [r15 + rdx*8]
    0x431db6: paddq    xmm2, xmm0
    0x431dba: movdqu   xmm3, xmmword ptr [r15 + rdx*8 + 0x10]
    0x431dc1: paddq    xmm3, xmm1
    0x431dc5: movdqu   xmm0, xmmword ptr [rax + rdx*8]
    0x431dca: paddq    xmm0, xmm2
    0x431dce: movdqu   xmm1, xmmword ptr [rax + rdx*8 + 0x10]
    0x431dd4: paddq    xmm1, xmm3
    0x431dd8: add      rdx, 4
    0x431ddc: cmp      rcx, rdx
    0x431ddf: jne      0x431db0

; --- Block 0x431de1 [BODY] 5 insns, callees: (none)
    0x431de1: paddq    xmm1, xmm0
    0x431de5: pshufd   xmm0, xmm1, 0xee
    0x431dea: paddq    xmm0, xmm1
    0x431dee: movq     r12, xmm0
    0x431df3: jmp      0x431e60

; --- Block 0x431df5 [BODY] 3 insns, callees: (none)
    0x431df5: mov      edi, 8
    0x431dfa: mov      rsi, qword ptr [rsp]
    0x431dfe: call     qword ptr [rip + 0x53614]

; --- Block 0x431e06 [BODY] 3 insns, callees: (none)
    0x431e06: mov      edi, 8
    0x431e0b: mov      rsi, qword ptr [rsp]
    0x431e0f: call     qword ptr [rip + 0x53603]

; --- Block 0x431e55 [LOOP_HEADER] 5 insns, callees: (none)
    0x431e55: add      r12, qword ptr [r15 + rcx*8]
    0x431e59: add      r12, qword ptr [rax + rcx*8]
    0x431e5d: inc      rcx
    0x431e60: cmp      r13, rcx
    0x431e63: jne      0x431e55

; --- Block 0x431e60 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431e60: cmp      r13, rcx
    0x431e63: jne      0x431e55

; --- Block 0x431e65 [BODY] 6 insns, callees: (none)
    0x431e65: mov      r14, qword ptr [rip + 0x535bc]
    0x431e6c: mov      edx, 8
    0x431e71: mov      rdi, rax
    0x431e74: mov      r13, qword ptr [rsp]
    0x431e78: mov      rsi, r13
    0x431e7b: call     r14

; --- Block 0x431e7e [BODY] 4 insns, callees: (none)
    0x431e7e: mov      edx, 8
    0x431e83: mov      rdi, r15
    0x431e86: mov      rsi, r13
    0x431e89: call     r14

; --- Block 0x431e8c [BOUNDS_CHECK] 3 insns, callees: (none)
    0x431e8c: mov      rsi, qword ptr [rsp + 8]
    0x431e91: test     rsi, rsi
    0x431e94: je       0x431ea8

; --- Block 0x431e96 [BODY] 4 insns, callees: (none)
    0x431e96: shl      rsi, 4
    0x431e9a: mov      edx, 8
    0x431e9f: mov      rdi, rbx
    0x431ea2: call     qword ptr [rip + 0x53580]

; --- Block 0x431ea8 [BODY] 9 insns, callees: (none)
    0x431ea8: mov      rax, r12
    0x431eab: add      rsp, 0x38
    0x431eaf: pop      rbx
    0x431eb0: pop      r12
    0x431eb2: pop      r13
    0x431eb4: pop      r14
    0x431eb6: pop      r15
    0x431eb8: pop      rbp
    0x431eb9: ret      

```

**Hungarian matching result** (mean similarity: 0.691):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x45de37` | BODY | `0x431c4c` | BODY | 1.000 | GOOD |
| `0x45de01` | BODY | `0x431d17` | BODY | 0.996 | GOOD |
| `0x45dc80` | BODY | `0x431b78` | BODY | 0.972 | GOOD |
| `0x45db5d` | BODY | `0x431cbd` | BODY | 0.971 | GOOD |
| `0x45dcd6` | BODY | `0x431d76` | BODY | 0.965 | GOOD |
| `0x45ddba` | BODY | `0x431b47` | BODY | 0.961 | GOOD |
| `0x45dc28` | BODY | `0x431ba1` | BODY | 0.831 | GOOD |
| `0x45dc13` | BODY | `0x431e06` | BODY | 0.734 | GOOD |
| `0x45dc3a` | BODY | `0x431df5` | BODY | 0.734 | GOOD |
| `0x45dcc4` | BODY | `0x431c57` | BODY | 0.734 | GOOD |
| `0x45dbc9` | BODY | `0x431cb3` | BOUNDS_CHECK | 0.733 | GOOD |
| `0x45dc4f` | BODY | `0x431e8c` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x45dcf1` | BODY | `0x431d59` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x45dd93` | BODY | `0x431d39` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x45ddae` | BODY | `0x431d49` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x45dc61` | BODY | `0x431b65` | BOUNDS_CHECK | 0.670 | PARTIAL |
| `0x45db9f` | BODY | `0x431bb2` | BOUNDS_CHECK | 0.668 | PARTIAL |
| `0x45dd57` | BODY | `0x431e7e` | BODY | 0.666 | PARTIAL |
| `0x45dd9f` | BODY | `0x431b86` | BODY | 0.664 | PARTIAL |
| `0x45dcfd` | BODY | `0x431c92` | BOUNDS_CHECK | 0.663 | PARTIAL |
| `0x45dddb` | BODY | `0x431c51` | BODY | 0.662 | PARTIAL |
| `0x45dd72` | BODY | `0x431d52` | BODY | 0.662 | PARTIAL |
| `0x45de07` | DROP_GLUE | `0x431bb0` | LOOP_HEADER | 0.652 | PARTIAL |
| `0x45dd14` | BODY | `0x431d96` | BODY | 0.651 | PARTIAL |
| `0x45de28` | BODY | `0x431d8e` | BODY | 0.651 | PARTIAL |
| `0x45dd16` | BODY | `0x431c47` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x45ddf4` | BODY | `0x431c66` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x45de2a` | DROP_GLUE | `0x431e60` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x45de39` | DROP_GLUE | `0x431b98` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x45db20` | BODY | `0x431b30` | BODY | 0.634 | PARTIAL |
| `0x45db6b` | BODY | `0x431d42` | BODY | 0.629 | PARTIAL |
| `0x45dd23` | BODY | `0x431d1f` | BODY | 0.601 | PARTIAL |
| `0x45ddf2` | BODY | `0x431bdd` | BODY | 0.594 | PARTIAL |
| `0x45dc7e` | BODY | `0x431d84` | BODY | 0.584 | PARTIAL |
| `0x45dce2` | BODY | `0x431e96` | BODY | 0.570 | PARTIAL |
| `0x45dc8d` | BODY | `0x431bd3` | BOUNDS_CHECK | 0.543 | PARTIAL |
| `0x45dbbc` | BODY | `0x431e65` | BODY | 0.541 | PARTIAL |
| `0x45dd66` | BODY | `0x431c90` | LOOP_HEADER | 0.540 | PARTIAL |
| `0x45dddd` | BODY | `0x431c40` | BOUNDS_CHECK | 0.515 | PARTIAL |
| `0x45dbdb` | EPILOGUE | `0x431d69` | BOUNDS_CHECK | 0.505 | PARTIAL |
| `0x45de46` | BODY | `0x431d7e` | BOUNDS_CHECK | 0.367 | POOR |
| — | — | `0x431bc2` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431bf0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431c10` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431c2c` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431c6f` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431ca2` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431cd0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431ce5` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431ceb` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431cf0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431d00` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431d30` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431d62` | ITERATOR_STATE | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431d9e` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431db0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431de1` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431e55` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431ea8` | BODY | 0.000 | UNMATCHED (O2 only) |

### C `iter_16` — O0: 14 blocks, O2: 10 blocks

**O0 blocks** (14 total):

```asm
; --- Block 0x4085c0 [BODY] 7 insns, callees: (none)
    0x4085c0: push     rbp
    0x4085c1: mov      rbp, rsp
    0x4085c4: mov      qword ptr [rbp - 0x38], rdi
    0x4085c8: mov      qword ptr [rbp - 0x40], rsi
    0x4085cc: mov      qword ptr [rbp - 0x48], rdx
    0x4085d0: cmp      qword ptr [rbp - 0x48], 0
    0x4085d5: jne      0x4085e1

; --- Block 0x4085d7 [BODY] 2 insns, callees: (none)
    0x4085d7: mov      eax, 0
    0x4085dc: jmp      0x4086cb

; --- Block 0x4085e1 [BODY] 3 insns, callees: (none)
    0x4085e1: mov      qword ptr [rbp - 8], 0
    0x4085e9: mov      qword ptr [rbp - 0x10], 0
    0x4085f1: jmp      0x4086b9

; --- Block 0x4085f6 [LOOP_HEADER] 7 insns, callees: (none)
    0x4085f6: mov      rdx, qword ptr [rbp - 0x10]
    0x4085fa: mov      rax, qword ptr [rbp - 0x48]
    0x4085fe: add      rax, rdx
    0x408601: mov      qword ptr [rbp - 0x18], rax
    0x408605: mov      rax, qword ptr [rbp - 0x18]
    0x408609: cmp      rax, qword ptr [rbp - 0x40]
    0x40860d: jbe      0x408617

; --- Block 0x40860f [BODY] 12 insns, callees: (none)
    0x40860f: mov      rax, qword ptr [rbp - 0x40]
    0x408613: mov      qword ptr [rbp - 0x18], rax
    0x408617: mov      qword ptr [rbp - 0x20], 0
    0x40861f: mov      rax, qword ptr [rbp - 0x10]
    0x408623: lea      rdx, [rax*8]
    0x40862b: mov      rax, qword ptr [rbp - 0x38]
    0x40862f: add      rax, rdx
    0x408632: mov      rax, qword ptr [rax]
    0x408635: mov      qword ptr [rbp - 0x28], rax
    0x408639: mov      rax, qword ptr [rbp - 0x10]
    0x40863d: mov      qword ptr [rbp - 0x30], rax
    0x408641: jmp      0x408698

; --- Block 0x408617 [BODY] 10 insns, callees: (none)
    0x408617: mov      qword ptr [rbp - 0x20], 0
    0x40861f: mov      rax, qword ptr [rbp - 0x10]
    0x408623: lea      rdx, [rax*8]
    0x40862b: mov      rax, qword ptr [rbp - 0x38]
    0x40862f: add      rax, rdx
    0x408632: mov      rax, qword ptr [rax]
    0x408635: mov      qword ptr [rbp - 0x28], rax
    0x408639: mov      rax, qword ptr [rbp - 0x10]
    0x40863d: mov      qword ptr [rbp - 0x30], rax
    0x408641: jmp      0x408698

; --- Block 0x408643 [LOOP_HEADER] 13 insns, callees: (none)
    0x408643: mov      rax, qword ptr [rbp - 0x30]
    0x408647: lea      rdx, [rax*8]
    0x40864f: mov      rax, qword ptr [rbp - 0x38]
    0x408653: add      rax, rdx
    0x408656: mov      rax, qword ptr [rax]
    0x408659: add      qword ptr [rbp - 0x20], rax
    0x40865d: mov      rax, qword ptr [rbp - 0x30]
    0x408661: lea      rdx, [rax*8]
    0x408669: mov      rax, qword ptr [rbp - 0x38]
    0x40866d: add      rax, rdx
    0x408670: mov      rax, qword ptr [rax]
    0x408673: cmp      qword ptr [rbp - 0x28], rax
    ... +1 more instructions

; --- Block 0x408679 [BODY] 10 insns, callees: (none)
    0x408679: mov      rax, qword ptr [rbp - 0x30]
    0x40867d: lea      rdx, [rax*8]
    0x408685: mov      rax, qword ptr [rbp - 0x38]
    0x408689: add      rax, rdx
    0x40868c: mov      rax, qword ptr [rax]
    0x40868f: mov      qword ptr [rbp - 0x28], rax
    0x408693: add      qword ptr [rbp - 0x30], 1
    0x408698: mov      rax, qword ptr [rbp - 0x30]
    0x40869c: cmp      rax, qword ptr [rbp - 0x18]
    0x4086a0: jb       0x408643

; --- Block 0x408693 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408693: add      qword ptr [rbp - 0x30], 1
    0x408698: mov      rax, qword ptr [rbp - 0x30]
    0x40869c: cmp      rax, qword ptr [rbp - 0x18]
    0x4086a0: jb       0x408643

; --- Block 0x408698 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x408698: mov      rax, qword ptr [rbp - 0x30]
    0x40869c: cmp      rax, qword ptr [rbp - 0x18]
    0x4086a0: jb       0x408643

; --- Block 0x4086a2 [BODY] 9 insns, callees: (none)
    0x4086a2: mov      rdx, qword ptr [rbp - 0x20]
    0x4086a6: mov      rax, qword ptr [rbp - 0x28]
    0x4086aa: add      rax, rdx
    0x4086ad: add      qword ptr [rbp - 8], rax
    0x4086b1: mov      rax, qword ptr [rbp - 0x48]
    0x4086b5: add      qword ptr [rbp - 0x10], rax
    0x4086b9: mov      rax, qword ptr [rbp - 0x10]
    0x4086bd: cmp      rax, qword ptr [rbp - 0x40]
    0x4086c1: jb       0x4085f6

; --- Block 0x4086b9 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4086b9: mov      rax, qword ptr [rbp - 0x10]
    0x4086bd: cmp      rax, qword ptr [rbp - 0x40]
    0x4086c1: jb       0x4085f6

; --- Block 0x4086c7 [EPILOGUE] 3 insns, callees: (none)
    0x4086c7: mov      rax, qword ptr [rbp - 8]
    0x4086cb: pop      rbp
    0x4086cc: ret      

; --- Block 0x4086cb [EPILOGUE] 2 insns, callees: (none)
    0x4086cb: pop      rbp
    0x4086cc: ret      

```

**O2 blocks** (10 total):

```asm
; --- Block 0x408010 [BODY] 6 insns, callees: (none)
    0x408010: push     r12
    0x408012: xor      r12d, r12d
    0x408015: push     rbp
    0x408016: push     rbx
    0x408017: test     rdx, rdx
    0x40801a: je       0x408094

; --- Block 0x40801c [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40801c: mov      r10, rsi
    0x40801f: test     rsi, rsi
    0x408022: je       0x408094

; --- Block 0x408024 [BODY] 13 insns, callees: (none)
    0x408024: mov      rbx, rdi
    0x408027: lea      rbp, [rdx*8]
    0x40802f: lea      r11, [rdi + 8]
    0x408033: xor      r9d, r9d
    0x408036: nop      word ptr cs:[rax + rax]
    0x408040: mov      rax, r9
    0x408043: add      r9, rdx
    0x408046: cmp      r10, r9
    0x408049: mov      rcx, r9
    0x40804c: mov      rsi, qword ptr [rbx + rax*8]
    0x408050: cmovbe   rcx, r10
    0x408054: cmp      rcx, rax
    ... +1 more instructions

; --- Block 0x408040 [LOOP_HEADER] 8 insns, callees: (none)
    0x408040: mov      rax, r9
    0x408043: add      r9, rdx
    0x408046: cmp      r10, r9
    0x408049: mov      rcx, r9
    0x40804c: mov      rsi, qword ptr [rbx + rax*8]
    0x408050: cmovbe   rcx, r10
    0x408054: cmp      rcx, rax
    0x408057: jbe      0x408089

; --- Block 0x408059 [BODY] 5 insns, callees: (none)
    0x408059: lea      r8, [rbx + rcx*8]
    0x40805d: mov      rax, rsi
    0x408060: mov      rcx, r11
    0x408063: xor      edi, edi
    0x408065: jmp      0x408077

; --- Block 0x408070 [LOOP_HEADER] 7 insns, callees: (none)
    0x408070: mov      rax, qword ptr [rcx]
    0x408073: add      rcx, 8
    0x408077: add      rdi, rax
    0x40807a: cmp      rsi, rax
    0x40807d: cmovb    rsi, rax
    0x408081: cmp      rcx, r8
    0x408084: jne      0x408070

; --- Block 0x408077 [ITERATOR_STATE] 5 insns, callees: (none)
    0x408077: add      rdi, rax
    0x40807a: cmp      rsi, rax
    0x40807d: cmovb    rsi, rax
    0x408081: cmp      rcx, r8
    0x408084: jne      0x408070

; --- Block 0x408086 [ITERATOR_STATE] 5 insns, callees: (none)
    0x408086: add      rsi, rdi
    0x408089: add      r12, rsi
    0x40808c: add      r11, rbp
    0x40808f: cmp      r10, r9
    0x408092: ja       0x408040

; --- Block 0x408089 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408089: add      r12, rsi
    0x40808c: add      r11, rbp
    0x40808f: cmp      r10, r9
    0x408092: ja       0x408040

; --- Block 0x408094 [EPILOGUE] 5 insns, callees: (none)
    0x408094: mov      rax, r12
    0x408097: pop      rbx
    0x408098: pop      rbp
    0x408099: pop      r12
    0x40809b: ret      

```

**Hungarian matching result** (mean similarity: 0.766):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x408698` | BOUNDS_CHECK | `0x40801c` | BOUNDS_CHECK | 0.955 | GOOD |
| `0x408693` | BOUNDS_CHECK | `0x408089` | BOUNDS_CHECK | 0.889 | GOOD |
| `0x4086a2` | BODY | `0x408040` | LOOP_HEADER | 0.829 | GOOD |
| `0x408643` | LOOP_HEADER | `0x408024` | BODY | 0.826 | GOOD |
| `0x4086c7` | EPILOGUE | `0x408094` | EPILOGUE | 0.825 | GOOD |
| `0x4085c0` | BODY | `0x408010` | BODY | 0.790 | GOOD |
| `0x4085f6` | LOOP_HEADER | `0x408070` | LOOP_HEADER | 0.671 | PARTIAL |
| `0x4086b9` | BOUNDS_CHECK | `0x408086` | ITERATOR_STATE | 0.640 | PARTIAL |
| `0x408617` | BODY | `0x408059` | BODY | 0.627 | PARTIAL |
| `0x408679` | BODY | `0x408077` | ITERATOR_STATE | 0.608 | PARTIAL |
| `0x4085d7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4085e1` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40860f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4086cb` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `iter_14`

### Rust `iter_14` — O0: 10 blocks, O2: 31 blocks

**O0 blocks** (10 total):

```asm
; --- Block 0x45d670 [BODY] 6 insns, callees: core::slice::<impl [T]>::iter
    0x45d670: sub      rsp, 0xa8
    0x45d677: mov      qword ptr [rsp], rdi
    0x45d67b: mov      qword ptr [rsp + 8], rsi
    0x45d680: mov      qword ptr [rsp + 0x78], rdi
    0x45d685: mov      qword ptr [rsp + 0x80], rsi
    0x45d68d: call     0x4910a0

; --- Block 0x45d692 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::enumerate
    0x45d692: mov      rsi, rax
    0x45d695: lea      rdi, [rsp + 0x30]
    0x45d69a: call     0x47f3d0

; --- Block 0x45d69f [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::filter_map
    0x45d69f: lea      rdi, [rsp + 0x18]
    0x45d6a4: lea      rsi, [rsp + 0x30]
    0x45d6a9: call     0x48dbc0

; --- Block 0x45d6ae [BODY] 4 insns, callees: <core::iter::adapters::filter_map::FilterMap<I,F> as core::iter::traits::iterator::Iterator>::fold
    0x45d6ae: lea      rdi, [rsp + 0x18]
    0x45d6b3: xor      eax, eax
    0x45d6b5: mov      esi, eax
    0x45d6b7: call     0x46d2f0

; --- Block 0x45d6bc [BODY] 5 insns, callees: core::slice::<impl [T]>::iter
    0x45d6bc: mov      rdi, qword ptr [rsp]
    0x45d6c0: mov      rsi, qword ptr [rsp + 8]
    0x45d6c5: mov      qword ptr [rsp + 0x10], rax
    0x45d6ca: mov      qword ptr [rsp + 0x88], rax
    0x45d6d2: call     0x4910a0

; --- Block 0x45d6d7 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::rev
    0x45d6d7: mov      rdi, rax
    0x45d6da: mov      rsi, rdx
    0x45d6dd: call     0x47dea0

; --- Block 0x45d6e2 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::enumerate
    0x45d6e2: mov      rsi, rax
    0x45d6e5: lea      rdi, [rsp + 0x60]
    0x45d6ea: call     0x48fc80

; --- Block 0x45d6ef [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::filter_map
    0x45d6ef: lea      rdi, [rsp + 0x48]
    0x45d6f4: lea      rsi, [rsp + 0x60]
    0x45d6f9: call     0x48dba0

; --- Block 0x45d6fe [BODY] 2 insns, callees: core::iter::traits::iterator::Iterator::sum
    0x45d6fe: lea      rdi, [rsp + 0x48]
    0x45d703: call     0x46d320

; --- Block 0x45d708 [BODY] 8 insns, callees: (none)
    0x45d708: mov      rcx, rax
    0x45d70b: mov      rax, qword ptr [rsp + 0x10]
    0x45d710: mov      qword ptr [rsp + 0x90], rcx
    0x45d718: mov      qword ptr [rsp + 0x98], rax
    0x45d720: mov      qword ptr [rsp + 0xa0], rcx
    0x45d728: add      rax, rcx
    0x45d72b: add      rsp, 0xa8
    0x45d732: ret      

```

**O2 blocks** (31 total):

```asm
; --- Block 0x4315e0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4315e0: test     rsi, rsi
    0x4315e3: je       0x4315f4

; --- Block 0x4315e5 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4315e5: push     r14
    0x4315e7: push     rbx
    0x4315e8: cmp      rsi, 1
    0x4315ec: jne      0x4315fe

; --- Block 0x4315ee [BODY] 3 insns, callees: (none)
    0x4315ee: xor      eax, eax
    0x4315f0: xor      ecx, ecx
    0x4315f2: jmp      0x431661

; --- Block 0x4315f4 [BODY] 3 insns, callees: (none)
    0x4315f4: xor      ecx, ecx
    0x4315f6: xor      r9d, r9d
    0x4315f9: jmp      0x43179c

; --- Block 0x4315fe [BODY] 25 insns, callees: (none)
    0x4315fe: mov      rdx, rsi
    0x431601: and      rdx, 0xfffffffffffffffe
    0x431605: mov      r8, 0xffffffffffffffff
    0x43160c: xor      r9d, r9d
    0x43160f: xor      eax, eax
    0x431611: xor      ecx, ecx
    0x431613: nop      word ptr cs:[rax + rax]
    0x431620: mov      r10, qword ptr [rdi + rax*8]
    0x431624: mov      r11, qword ptr [rdi + rax*8 + 8]
    0x431629: lea      rbx, [r8 + r10]
    0x43162d: inc      rbx
    0x431630: imul     rbx, rbx
    ... +13 more instructions

; --- Block 0x431620 [BODY] 18 insns, callees: (none)
    0x431620: mov      r10, qword ptr [rdi + rax*8]
    0x431624: mov      r11, qword ptr [rdi + rax*8 + 8]
    0x431629: lea      rbx, [r8 + r10]
    0x43162d: inc      rbx
    0x431630: imul     rbx, rbx
    0x431634: cmp      r10, rax
    0x431637: cmovbe   rbx, r9
    0x43163b: add      rbx, rcx
    0x43163e: lea      r10, [rax + 1]
    0x431642: lea      rcx, [r8 + r11]
    0x431646: imul     rcx, rcx
    0x43164a: cmp      r11, r10
    ... +6 more instructions

; --- Block 0x431661 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431661: test     sil, 1
    0x431665: je       0x431682

; --- Block 0x431667 [BODY] 10 insns, callees: (none)
    0x431667: mov      rdx, qword ptr [rdi + rax*8]
    0x43166b: mov      r8, rdx
    0x43166e: sub      r8, rax
    0x431671: imul     r8, r8
    0x431675: xor      r9d, r9d
    0x431678: cmp      rdx, rax
    0x43167b: cmova    r9, r8
    0x43167f: add      rcx, r9
    0x431682: cmp      rsi, 1
    0x431686: jne      0x431690

; --- Block 0x431682 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431682: cmp      rsi, 1
    0x431686: jne      0x431690

; --- Block 0x431688 [BODY] 2 insns, callees: (none)
    0x431688: xor      r9d, r9d
    0x43168b: jmp      0x431799

; --- Block 0x431690 [BODY] 4 insns, callees: (none)
    0x431690: lea      rax, [rsi*8]
    0x431698: mov      rbx, rax
    0x43169b: add      rbx, -0x10
    0x43169f: je       0x431755

; --- Block 0x4316a5 [BODY] 9 insns, callees: (none)
    0x4316a5: shr      rbx, 3
    0x4316a9: inc      rbx
    0x4316ac: lea      r11, [rax + rdi]
    0x4316b0: add      r11, -8
    0x4316b4: and      rbx, 0xfffffffffffffffe
    0x4316b8: neg      rbx
    0x4316bb: mov      r10d, 1
    0x4316c1: xor      r9d, r9d
    0x4316c4: jmp      0x4316ec

; --- Block 0x4316d0 [LOOP_HEADER] 8 insns, callees: (none)
    0x4316d0: add      r9, rdi
    0x4316d3: add      r9, r8
    0x4316d6: add      r11, -0x10
    0x4316da: lea      rax, [rbx + r10]
    0x4316de: add      rax, 2
    0x4316e2: add      r10, 2
    0x4316e6: cmp      rax, 1
    0x4316ea: je       0x431766

; --- Block 0x4316ec [BODY] 5 insns, callees: (none)
    0x4316ec: mov      rdi, qword ptr [r11 - 8]
    0x4316f0: mov      rax, rdi
    0x4316f3: or       rax, r10
    0x4316f6: shr      rax, 0x20
    0x4316fa: je       0x431730

; --- Block 0x4316fc [BODY] 5 insns, callees: (none)
    0x4316fc: mov      rax, rdi
    0x4316ff: xor      edx, edx
    0x431701: div      r10
    0x431704: test     rdx, rdx
    0x431707: je       0x43170b

; --- Block 0x431709 [LOOP_HEADER] 7 insns, callees: (none)
    0x431709: xor      edi, edi
    0x43170b: lea      r14, [r10 + 1]
    0x43170f: mov      r8, qword ptr [r11 - 0x10]
    0x431713: mov      rax, r8
    0x431716: or       rax, r14
    0x431719: shr      rax, 0x20
    0x43171d: je       0x431740

; --- Block 0x43170b [LOOP_HEADER] 6 insns, callees: (none)
    0x43170b: lea      r14, [r10 + 1]
    0x43170f: mov      r8, qword ptr [r11 - 0x10]
    0x431713: mov      rax, r8
    0x431716: or       rax, r14
    0x431719: shr      rax, 0x20
    0x43171d: je       0x431740

; --- Block 0x43171f [BODY] 5 insns, callees: (none)
    0x43171f: mov      rax, r8
    0x431722: xor      edx, edx
    0x431724: div      r14
    0x431727: test     rdx, rdx
    0x43172a: je       0x4316d0

; --- Block 0x43172c [BODY] 1 insns, callees: (none)
    0x43172c: jmp      0x43174d

; --- Block 0x431730 [BODY] 5 insns, callees: (none)
    0x431730: mov      eax, edi
    0x431732: xor      edx, edx
    0x431734: div      r10d
    0x431737: test     rdx, rdx
    0x43173a: jne      0x431709

; --- Block 0x43173c [BODY] 1 insns, callees: (none)
    0x43173c: jmp      0x43170b

; --- Block 0x431740 [BODY] 5 insns, callees: (none)
    0x431740: mov      eax, r8d
    0x431743: xor      edx, edx
    0x431745: div      r14d
    0x431748: test     rdx, rdx
    0x43174b: je       0x4316d0

; --- Block 0x43174d [BODY] 2 insns, callees: (none)
    0x43174d: xor      r8d, r8d
    0x431750: jmp      0x4316d0

; --- Block 0x431755 [ITERATOR_STATE] 6 insns, callees: (none)
    0x431755: lea      r11, [rdi + rsi*8]
    0x431759: add      r11, -8
    0x43175d: xor      r9d, r9d
    0x431760: mov      r10d, 1
    0x431766: test     sil, 1
    0x43176a: jne      0x431799

; --- Block 0x431766 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x431766: test     sil, 1
    0x43176a: jne      0x431799

; --- Block 0x43176c [BODY] 5 insns, callees: (none)
    0x43176c: mov      rsi, qword ptr [r11 - 8]
    0x431770: mov      rax, rsi
    0x431773: or       rax, r10
    0x431776: shr      rax, 0x20
    0x43177a: je       0x431786

; --- Block 0x43177c [BODY] 4 insns, callees: (none)
    0x43177c: mov      rax, rsi
    0x43177f: xor      edx, edx
    0x431781: div      r10
    0x431784: jmp      0x43178d

; --- Block 0x431786 [BODY] 12 insns, callees: (none)
    0x431786: mov      eax, esi
    0x431788: xor      edx, edx
    0x43178a: div      r10d
    0x43178d: xor      eax, eax
    0x43178f: test     rdx, rdx
    0x431792: cmove    rax, rsi
    0x431796: add      r9, rax
    0x431799: pop      rbx
    0x43179a: pop      r14
    0x43179c: add      rcx, r9
    0x43179f: mov      rax, rcx
    0x4317a2: ret      

; --- Block 0x43178d [BODY] 9 insns, callees: (none)
    0x43178d: xor      eax, eax
    0x43178f: test     rdx, rdx
    0x431792: cmove    rax, rsi
    0x431796: add      r9, rax
    0x431799: pop      rbx
    0x43179a: pop      r14
    0x43179c: add      rcx, r9
    0x43179f: mov      rax, rcx
    0x4317a2: ret      

; --- Block 0x431799 [EPILOGUE] 5 insns, callees: (none)
    0x431799: pop      rbx
    0x43179a: pop      r14
    0x43179c: add      rcx, r9
    0x43179f: mov      rax, rcx
    0x4317a2: ret      

; --- Block 0x43179c [EPILOGUE] 3 insns, callees: (none)
    0x43179c: add      rcx, r9
    0x43179f: mov      rax, rcx
    0x4317a2: ret      

```

**Hungarian matching result** (mean similarity: 0.598):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x45d6ae` | BODY | `0x43177c` | BODY | 0.724 | GOOD |
| `0x45d6d7` | BODY | `0x43179c` | EPILOGUE | 0.669 | PARTIAL |
| `0x45d6bc` | BODY | `0x4316fc` | BODY | 0.654 | PARTIAL |
| `0x45d6fe` | BODY | `0x4315e0` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x45d6e2` | BODY | `0x4315f4` | BODY | 0.606 | PARTIAL |
| `0x45d692` | BODY | `0x4315ee` | BODY | 0.587 | PARTIAL |
| `0x45d708` | BODY | `0x431799` | EPILOGUE | 0.543 | PARTIAL |
| `0x45d69f` | BODY | `0x4315e5` | BOUNDS_CHECK | 0.541 | PARTIAL |
| `0x45d6ef` | BODY | `0x431661` | BOUNDS_CHECK | 0.523 | PARTIAL |
| `0x45d670` | BODY | `0x431755` | ITERATOR_STATE | 0.496 | PARTIAL |
| — | — | `0x4315fe` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431620` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431667` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431682` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431688` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431690` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4316a5` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4316d0` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4316ec` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431709` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43170b` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43171f` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43172c` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431730` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43173c` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431740` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43174d` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431766` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43176c` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x431786` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x43178d` | BODY | 0.000 | UNMATCHED (O2 only) |

### C `iter_14` — O0: 12 blocks, O2: 11 blocks

**O0 blocks** (12 total):

```asm
; --- Block 0x40838a [BODY] 7 insns, callees: (none)
    0x40838a: push     rbp
    0x40838b: mov      rbp, rsp
    0x40838e: mov      qword ptr [rbp - 0x38], rdi
    0x408392: mov      qword ptr [rbp - 0x40], rsi
    0x408396: mov      qword ptr [rbp - 8], 0
    0x40839e: mov      qword ptr [rbp - 0x10], 0
    0x4083a6: jmp      0x4083f3

; --- Block 0x4083a8 [LOOP_HEADER] 7 insns, callees: (none)
    0x4083a8: mov      rax, qword ptr [rbp - 0x10]
    0x4083ac: lea      rdx, [rax*8]
    0x4083b4: mov      rax, qword ptr [rbp - 0x38]
    0x4083b8: add      rax, rdx
    0x4083bb: mov      rax, qword ptr [rax]
    0x4083be: cmp      qword ptr [rbp - 0x10], rax
    0x4083c2: jae      0x4083ee

; --- Block 0x4083c4 [BODY] 14 insns, callees: (none)
    0x4083c4: mov      rax, qword ptr [rbp - 0x10]
    0x4083c8: lea      rdx, [rax*8]
    0x4083d0: mov      rax, qword ptr [rbp - 0x38]
    0x4083d4: add      rax, rdx
    0x4083d7: mov      rax, qword ptr [rax]
    0x4083da: sub      rax, qword ptr [rbp - 0x10]
    0x4083de: mov      qword ptr [rbp - 0x30], rax
    0x4083e2: mov      rax, qword ptr [rbp - 0x30]
    0x4083e6: imul     rax, rax
    0x4083ea: add      qword ptr [rbp - 8], rax
    0x4083ee: add      qword ptr [rbp - 0x10], 1
    0x4083f3: mov      rax, qword ptr [rbp - 0x10]
    ... +2 more instructions

; --- Block 0x4083ee [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4083ee: add      qword ptr [rbp - 0x10], 1
    0x4083f3: mov      rax, qword ptr [rbp - 0x10]
    0x4083f7: cmp      rax, qword ptr [rbp - 0x40]
    0x4083fb: jb       0x4083a8

; --- Block 0x4083f3 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4083f3: mov      rax, qword ptr [rbp - 0x10]
    0x4083f7: cmp      rax, qword ptr [rbp - 0x40]
    0x4083fb: jb       0x4083a8

; --- Block 0x4083fd [BODY] 3 insns, callees: (none)
    0x4083fd: mov      qword ptr [rbp - 0x18], 0
    0x408405: mov      qword ptr [rbp - 0x20], 0
    0x40840d: jmp      0x40846c

; --- Block 0x40840f [LOOP_HEADER] 6 insns, callees: (none)
    0x40840f: mov      rax, qword ptr [rbp - 0x40]
    0x408413: sub      rax, qword ptr [rbp - 0x20]
    0x408417: sub      rax, 1
    0x40841b: mov      qword ptr [rbp - 0x28], rax
    0x40841f: cmp      qword ptr [rbp - 0x20], 0
    0x408424: je       0x408467

; --- Block 0x408426 [BODY] 10 insns, callees: (none)
    0x408426: mov      rax, qword ptr [rbp - 0x28]
    0x40842a: lea      rdx, [rax*8]
    0x408432: mov      rax, qword ptr [rbp - 0x38]
    0x408436: add      rax, rdx
    0x408439: mov      rax, qword ptr [rax]
    0x40843c: mov      edx, 0
    0x408441: div      qword ptr [rbp - 0x20]
    0x408445: mov      rax, rdx
    0x408448: test     rax, rax
    0x40844b: jne      0x408467

; --- Block 0x40844d [BODY] 10 insns, callees: (none)
    0x40844d: mov      rax, qword ptr [rbp - 0x28]
    0x408451: lea      rdx, [rax*8]
    0x408459: mov      rax, qword ptr [rbp - 0x38]
    0x40845d: add      rax, rdx
    0x408460: mov      rax, qword ptr [rax]
    0x408463: add      qword ptr [rbp - 0x18], rax
    0x408467: add      qword ptr [rbp - 0x20], 1
    0x40846c: mov      rax, qword ptr [rbp - 0x20]
    0x408470: cmp      rax, qword ptr [rbp - 0x40]
    0x408474: jb       0x40840f

; --- Block 0x408467 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x408467: add      qword ptr [rbp - 0x20], 1
    0x40846c: mov      rax, qword ptr [rbp - 0x20]
    0x408470: cmp      rax, qword ptr [rbp - 0x40]
    0x408474: jb       0x40840f

; --- Block 0x40846c [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40846c: mov      rax, qword ptr [rbp - 0x20]
    0x408470: cmp      rax, qword ptr [rbp - 0x40]
    0x408474: jb       0x40840f

; --- Block 0x408476 [EPILOGUE] 5 insns, callees: (none)
    0x408476: mov      rdx, qword ptr [rbp - 8]
    0x40847a: mov      rax, qword ptr [rbp - 0x18]
    0x40847e: add      rax, rdx
    0x408481: pop      rbp
    0x408482: ret      

```

**O2 blocks** (11 total):

```asm
; --- Block 0x407ea0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407ea0: test     rsi, rsi
    0x407ea3: je       0x407f10

; --- Block 0x407ea5 [BODY] 3 insns, callees: (none)
    0x407ea5: xor      ecx, ecx
    0x407ea7: xor      r10d, r10d
    0x407eaa: jmp      0x407eb3

; --- Block 0x407eb0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x407eb0: mov      rcx, rax
    0x407eb3: mov      rax, qword ptr [rdi + rcx*8]
    0x407eb7: cmp      rax, rcx
    0x407eba: jbe      0x407ec6

; --- Block 0x407eb3 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407eb3: mov      rax, qword ptr [rdi + rcx*8]
    0x407eb7: cmp      rax, rcx
    0x407eba: jbe      0x407ec6

; --- Block 0x407ebc [ITERATOR_STATE] 6 insns, callees: (none)
    0x407ebc: sub      rax, rcx
    0x407ebf: imul     rax, rax
    0x407ec3: add      r10, rax
    0x407ec6: lea      rax, [rcx + 1]
    0x407eca: cmp      rsi, rax
    0x407ecd: jne      0x407eb0

; --- Block 0x407ec6 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407ec6: lea      rax, [rcx + 1]
    0x407eca: cmp      rsi, rax
    0x407ecd: jne      0x407eb0

; --- Block 0x407ecf [BODY] 4 insns, callees: (none)
    0x407ecf: lea      r8, [rdi + rcx*8]
    0x407ed3: xor      eax, eax
    0x407ed5: xor      r9d, r9d
    0x407ed8: jmp      0x407ef8

; --- Block 0x407ee0 [LOOP_HEADER] 12 insns, callees: (none)
    0x407ee0: mov      rsi, qword ptr [r8]
    0x407ee3: xor      edx, edx
    0x407ee5: mov      rax, rsi
    0x407ee8: add      rsi, r9
    0x407eeb: div      rdi
    0x407eee: mov      rax, rdi
    0x407ef1: test     rdx, rdx
    0x407ef4: cmove    r9, rsi
    0x407ef8: lea      rdi, [rax + 1]
    0x407efc: sub      r8, 8
    0x407f00: cmp      rax, rcx
    0x407f03: jne      0x407ee0

; --- Block 0x407ef8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x407ef8: lea      rdi, [rax + 1]
    0x407efc: sub      r8, 8
    0x407f00: cmp      rax, rcx
    0x407f03: jne      0x407ee0

; --- Block 0x407f05 [BODY] 2 insns, callees: (none)
    0x407f05: lea      rax, [r10 + r9]
    0x407f09: ret      

; --- Block 0x407f10 [BODY] 2 insns, callees: (none)
    0x407f10: xor      eax, eax
    0x407f12: ret      

```

**Hungarian matching result** (mean similarity: 0.664):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40846c` | BOUNDS_CHECK | `0x407eb3` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x4083ee` | BOUNDS_CHECK | `0x407eb0` | BOUNDS_CHECK | 0.867 | GOOD |
| `0x4083f3` | BOUNDS_CHECK | `0x407ec6` | BOUNDS_CHECK | 0.803 | GOOD |
| `0x4083a8` | LOOP_HEADER | `0x407ebc` | ITERATOR_STATE | 0.745 | GOOD |
| `0x4083fd` | BODY | `0x407ea5` | BODY | 0.734 | GOOD |
| `0x408467` | BOUNDS_CHECK | `0x407ea0` | BOUNDS_CHECK | 0.656 | PARTIAL |
| `0x40838a` | BODY | `0x407ecf` | BODY | 0.541 | PARTIAL |
| `0x4083c4` | BODY | `0x407ee0` | LOOP_HEADER | 0.536 | PARTIAL |
| `0x40840f` | LOOP_HEADER | `0x407ef8` | BOUNDS_CHECK | 0.517 | PARTIAL |
| `0x408476` | EPILOGUE | `0x407f10` | BODY | 0.508 | PARTIAL |
| `0x40844d` | BODY | `0x407f05` | BODY | 0.403 | PARTIAL |
| `0x408426` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `iter_12`

### Rust `iter_12` — O0: 24 blocks, O2: 15 blocks

**O0 blocks** (24 total):

```asm
; --- Block 0x45d190 [BODY] 5 insns, callees: core::slice::<impl [T]>::iter
    0x45d190: sub      rsp, 0x118
    0x45d197: mov      qword ptr [rsp + 0x68], rdx
    0x45d19c: mov      qword ptr [rsp + 0xd8], rdi
    0x45d1a4: mov      qword ptr [rsp + 0xe0], rsi
    0x45d1ac: call     0x4910a0

; --- Block 0x45d1b1 [BODY] 6 insns, callees: core::iter::traits::iterator::Iterator::scan
    0x45d1b1: mov      rsi, rax
    0x45d1b4: xor      eax, eax
    0x45d1b6: mov      ecx, eax
    0x45d1b8: lea      rdi, [rsp + 0x88]
    0x45d1c0: mov      qword ptr [rsp + 0x48], rdi
    0x45d1c5: call     0x47e680

; --- Block 0x45d1ca [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::collect
    0x45d1ca: mov      rsi, qword ptr [rsp + 0x48]
    0x45d1cf: lea      rdi, [rsp + 0x70]
    0x45d1d4: mov      qword ptr [rsp + 0x50], rdi
    0x45d1d9: call     0x4954a0

; --- Block 0x45d1de [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45d1de: mov      rdi, qword ptr [rsp + 0x50]
    0x45d1e3: call     0x4ab750

; --- Block 0x45d1e8 [BODY] 3 insns, callees: (none)
    0x45d1e8: mov      qword ptr [rsp + 0x58], rdx
    0x45d1ed: mov      qword ptr [rsp + 0x60], rax
    0x45d1f2: jmp      0x45d219

; --- Block 0x45d219 [BODY] 6 insns, callees: core::slice::<impl [T]>::windows
    0x45d219: mov      rdx, qword ptr [rsp + 0x58]
    0x45d21e: mov      rsi, qword ptr [rsp + 0x60]
    0x45d223: lea      r8, [rip + 0x9466e]
    0x45d22a: lea      rdi, [rsp + 0xc0]
    0x45d232: mov      ecx, 2
    0x45d237: call     0x492640

; --- Block 0x45d23c [BODY] 1 insns, callees: (none)
    0x45d23c: jmp      0x45d23e

; --- Block 0x45d23e [BODY] 4 insns, callees: core::iter::traits::iterator::Iterator::filter
    0x45d23e: lea      rdi, [rsp + 0xa0]
    0x45d246: lea      rsi, [rsp + 0xc0]
    0x45d24e: lea      rdx, [rsp + 0x68]
    0x45d253: call     0x47e8f0

; --- Block 0x45d258 [BODY] 1 insns, callees: (none)
    0x45d258: jmp      0x45d25a

; --- Block 0x45d25a [BODY] 2 insns, callees: <core::iter::adapters::filter::Filter<I,P> as core::iter::traits::iterator::Iterator>::count
    0x45d25a: lea      rdi, [rsp + 0xa0]
    0x45d262: call     0x47c4b0

; --- Block 0x45d267 [BODY] 2 insns, callees: (none)
    0x45d267: mov      qword ptr [rsp + 0x40], rax
    0x45d26c: jmp      0x45d26e

; --- Block 0x45d26e [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x45d26e: mov      rax, qword ptr [rsp + 0x40]
    0x45d273: mov      qword ptr [rsp + 0xf8], rax
    0x45d27b: lea      rdi, [rsp + 0x70]
    0x45d280: call     0x4ab750

; --- Block 0x45d285 [BODY] 3 insns, callees: (none)
    0x45d285: mov      qword ptr [rsp + 0x30], rdx
    0x45d28a: mov      qword ptr [rsp + 0x38], rax
    0x45d28f: jmp      0x45d291

; --- Block 0x45d291 [BODY] 3 insns, callees: core::slice::<impl [T]>::last
    0x45d291: mov      rsi, qword ptr [rsp + 0x30]
    0x45d296: mov      rdi, qword ptr [rsp + 0x38]
    0x45d29b: call     0x4910c0

; --- Block 0x45d2a0 [BODY] 2 insns, callees: (none)
    0x45d2a0: mov      qword ptr [rsp + 0x28], rax
    0x45d2a5: jmp      0x45d2a7

; --- Block 0x45d2a7 [BODY] 2 insns, callees: core::option::Option<&T>::copied
    0x45d2a7: mov      rdi, qword ptr [rsp + 0x28]
    0x45d2ac: call     0x460d50

; --- Block 0x45d2b1 [BODY] 3 insns, callees: (none)
    0x45d2b1: mov      qword ptr [rsp + 0x18], rdx
    0x45d2b6: mov      qword ptr [rsp + 0x20], rax
    0x45d2bb: jmp      0x45d2bd

; --- Block 0x45d2bd [BODY] 5 insns, callees: core::option::Option<T>::unwrap_or
    0x45d2bd: mov      rsi, qword ptr [rsp + 0x18]
    0x45d2c2: mov      rdi, qword ptr [rsp + 0x20]
    0x45d2c7: xor      eax, eax
    0x45d2c9: mov      edx, eax
    0x45d2cb: call     0x460c50

; --- Block 0x45d2d0 [BODY] 2 insns, callees: (none)
    0x45d2d0: mov      qword ptr [rsp + 0x10], rax
    0x45d2d5: jmp      0x45d2d7

; --- Block 0x45d2d7 [BODY] 8 insns, callees: (none)
    0x45d2d7: mov      rax, qword ptr [rsp + 0x40]
    0x45d2dc: mov      rcx, qword ptr [rsp + 0x10]
    0x45d2e1: mov      qword ptr [rsp + 0x100], rcx
    0x45d2e9: mov      ecx, 0x64
    0x45d2ee: mul      rcx
    0x45d2f1: mov      qword ptr [rsp + 8], rax
    0x45d2f6: seto     al
    0x45d2f9: jo       0x45d31e

; --- Block 0x45d2fb [BODY] 7 insns, callees: (none)
    0x45d2fb: mov      rcx, qword ptr [rsp + 8]
    0x45d300: mov      rax, qword ptr [rsp + 0x10]
    0x45d305: mov      qword ptr [rsp + 0x108], rax
    0x45d30d: mov      qword ptr [rsp + 0x110], rcx
    0x45d315: add      rax, rcx
    0x45d318: mov      qword ptr [rsp], rax
    0x45d31c: jmp      0x45d332

; --- Block 0x45d31e [BODY] 3 insns, callees: (none)
    0x45d31e: lea      rdi, [rip + 0x9458b]
    0x45d325: mov      rax, qword ptr [rip + 0x97e0c]
    0x45d32c: call     rax

; --- Block 0x45d332 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<u64>>
    0x45d332: lea      rdi, [rsp + 0x70]
    0x45d337: call     0x496820

; --- Block 0x45d33c [EPILOGUE] 3 insns, callees: (none)
    0x45d33c: mov      rax, qword ptr [rsp]
    0x45d340: add      rsp, 0x118
    0x45d347: ret      

```

**O2 blocks** (15 total):

```asm
; --- Block 0x431220 [BODY] 11 insns, callees: <alloc::vec::Vec<T> as alloc::vec::spec_from_iter_nested::SpecFromIterNested<T,I>>::from_iter
    0x431220: push     r14
    0x431222: push     rbx
    0x431223: sub      rsp, 0x38
    0x431227: mov      rbx, rdx
    0x43122a: lea      rax, [rdi + rsi*8]
    0x43122e: mov      qword ptr [rsp + 0x20], rdi
    0x431233: mov      qword ptr [rsp + 0x28], rax
    0x431238: mov      qword ptr [rsp + 0x30], 0
    0x431241: lea      rdi, [rsp + 8]
    0x431246: lea      rsi, [rsp + 0x20]
    0x43124b: call     0x436410

; --- Block 0x431250 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431250: mov      rdi, qword ptr [rsp + 0x10]
    0x431255: mov      rax, qword ptr [rsp + 0x18]
    0x43125a: cmp      rax, 2
    0x43125e: jae      0x43126f

; --- Block 0x431260 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x431260: xor      r14d, r14d
    0x431263: mov      ebx, 0
    0x431268: test     rax, rax
    0x43126b: jne      0x4312e8

; --- Block 0x43126d [BODY] 1 insns, callees: (none)
    0x43126d: jmp      0x4312ed

; --- Block 0x43126f [BOUNDS_CHECK] 4 insns, callees: (none)
    0x43126f: mov      rdx, qword ptr [rdi]
    0x431272: lea      rsi, [rax - 1]
    0x431276: cmp      rax, 2
    0x43127a: jne      0x431283

; --- Block 0x43127c [BODY] 3 insns, callees: (none)
    0x43127c: xor      ecx, ecx
    0x43127e: mov      r8, rdi
    0x431281: jmp      0x4312c6

; --- Block 0x431283 [BODY] 21 insns, callees: (none)
    0x431283: mov      r9, rsi
    0x431286: and      r9, 0xfffffffffffffffe
    0x43128a: xor      ecx, ecx
    0x43128c: mov      r8, rdi
    0x43128f: nop      
    0x431290: cmp      rdx, rbx
    0x431293: setb     r10b
    0x431297: cmp      qword ptr [r8 + 8], rbx
    0x43129b: mov      rdx, qword ptr [r8 + 0x10]
    0x43129f: setb     r11b
    0x4312a3: xor      r10b, r11b
    0x4312a6: movzx    r10d, r10b
    ... +9 more instructions

; --- Block 0x431290 [BODY] 16 insns, callees: (none)
    0x431290: cmp      rdx, rbx
    0x431293: setb     r10b
    0x431297: cmp      qword ptr [r8 + 8], rbx
    0x43129b: mov      rdx, qword ptr [r8 + 0x10]
    0x43129f: setb     r11b
    0x4312a3: xor      r10b, r11b
    0x4312a6: movzx    r10d, r10b
    0x4312aa: add      r10, rcx
    0x4312ad: add      r8, 0x10
    0x4312b1: cmp      rdx, rbx
    0x4312b4: setb     cl
    0x4312b7: xor      cl, r11b
    ... +4 more instructions

; --- Block 0x4312c6 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4312c6: test     sil, 1
    0x4312ca: je       0x4312e4

; --- Block 0x4312cc [BODY] 12 insns, callees: (none)
    0x4312cc: cmp      rdx, rbx
    0x4312cf: setb     dl
    0x4312d2: cmp      qword ptr [r8 + 8], rbx
    0x4312d6: setb     sil
    0x4312da: xor      sil, dl
    0x4312dd: movzx    edx, sil
    0x4312e1: add      rcx, rdx
    0x4312e4: imul     r14, rcx, 0x64
    0x4312e8: mov      rbx, qword ptr [rdi + rax*8 - 8]
    0x4312ed: mov      rsi, qword ptr [rsp + 8]
    0x4312f2: test     rsi, rsi
    0x4312f5: je       0x431306

; --- Block 0x4312e4 [BODY] 5 insns, callees: (none)
    0x4312e4: imul     r14, rcx, 0x64
    0x4312e8: mov      rbx, qword ptr [rdi + rax*8 - 8]
    0x4312ed: mov      rsi, qword ptr [rsp + 8]
    0x4312f2: test     rsi, rsi
    0x4312f5: je       0x431306

; --- Block 0x4312e8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4312e8: mov      rbx, qword ptr [rdi + rax*8 - 8]
    0x4312ed: mov      rsi, qword ptr [rsp + 8]
    0x4312f2: test     rsi, rsi
    0x4312f5: je       0x431306

; --- Block 0x4312ed [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4312ed: mov      rsi, qword ptr [rsp + 8]
    0x4312f2: test     rsi, rsi
    0x4312f5: je       0x431306

; --- Block 0x4312f7 [BODY] 3 insns, callees: (none)
    0x4312f7: shl      rsi, 3
    0x4312fb: mov      edx, 8
    0x431300: call     qword ptr [rip + 0x54122]

; --- Block 0x431306 [BODY] 6 insns, callees: (none)
    0x431306: add      rbx, r14
    0x431309: mov      rax, rbx
    0x43130c: add      rsp, 0x38
    0x431310: pop      rbx
    0x431311: pop      r14
    0x431313: ret      

```

**Hungarian matching result** (mean similarity: 0.613):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x45d23c` | BODY | `0x43126d` | BODY | 1.000 | GOOD |
| `0x45d1e8` | BODY | `0x43127c` | BODY | 0.862 | GOOD |
| `0x45d219` | BODY | `0x43126f` | BOUNDS_CHECK | 0.733 | GOOD |
| `0x45d285` | BODY | `0x4312ed` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x45d1ca` | BODY | `0x4312e8` | BOUNDS_CHECK | 0.689 | PARTIAL |
| `0x45d2bd` | BODY | `0x431260` | BOUNDS_CHECK | 0.663 | PARTIAL |
| `0x45d267` | BODY | `0x4312c6` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x45d2d7` | BODY | `0x4312cc` | BODY | 0.650 | PARTIAL |
| `0x45d291` | BODY | `0x4312f7` | BODY | 0.644 | PARTIAL |
| `0x45d26e` | BODY | `0x431250` | BOUNDS_CHECK | 0.526 | PARTIAL |
| `0x45d33c` | EPILOGUE | `0x431306` | BODY | 0.518 | PARTIAL |
| `0x45d190` | BODY | `0x4312e4` | BODY | 0.503 | PARTIAL |
| `0x45d31e` | BODY | `0x431220` | BODY | 0.421 | PARTIAL |
| `0x45d2fb` | BODY | `0x431290` | BODY | 0.336 | POOR |
| `0x45d1b1` | BODY | `0x431283` | BODY | 0.265 | POOR |
| `0x45d1de` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d23e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d258` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d25a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d2a0` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d2a7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d2b1` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d2d0` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45d332` | DROP_GLUE | — | — | 0.000 | UNMATCHED (O0 only) |

### C `iter_12` — O0: 14 blocks, O2: 12 blocks

**O0 blocks** (14 total):

```asm
; --- Block 0x408152 [BODY] 10 insns, callees: sub_4010f0
    0x408152: push     rbp
    0x408153: mov      rbp, rsp
    0x408156: sub      rsp, 0x50
    0x40815a: mov      qword ptr [rbp - 0x38], rdi
    0x40815e: mov      qword ptr [rbp - 0x40], rsi
    0x408162: mov      qword ptr [rbp - 0x48], rdx
    0x408166: mov      rax, qword ptr [rbp - 0x40]
    0x40816a: shl      rax, 3
    0x40816e: mov      rdi, rax
    0x408171: call     0x4010f0

; --- Block 0x408176 [BODY] 4 insns, callees: (none)
    0x408176: mov      qword ptr [rbp - 0x28], rax
    0x40817a: mov      qword ptr [rbp - 8], 0
    0x408182: mov      qword ptr [rbp - 0x10], 0
    0x40818a: jmp      0x4081c5

; --- Block 0x40818c [LOOP_HEADER] 16 insns, callees: (none)
    0x40818c: mov      rax, qword ptr [rbp - 0x10]
    0x408190: lea      rdx, [rax*8]
    0x408198: mov      rax, qword ptr [rbp - 0x38]
    0x40819c: add      rax, rdx
    0x40819f: mov      rax, qword ptr [rax]
    0x4081a2: add      qword ptr [rbp - 8], rax
    0x4081a6: mov      rax, qword ptr [rbp - 0x10]
    0x4081aa: lea      rdx, [rax*8]
    0x4081b2: mov      rax, qword ptr [rbp - 0x28]
    0x4081b6: add      rdx, rax
    0x4081b9: mov      rax, qword ptr [rbp - 8]
    0x4081bd: mov      qword ptr [rdx], rax
    ... +4 more instructions

; --- Block 0x4081c5 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4081c5: mov      rax, qword ptr [rbp - 0x10]
    0x4081c9: cmp      rax, qword ptr [rbp - 0x40]
    0x4081cd: jb       0x40818c

; --- Block 0x4081cf [BODY] 3 insns, callees: (none)
    0x4081cf: mov      qword ptr [rbp - 0x18], 0
    0x4081d7: mov      qword ptr [rbp - 0x20], 0
    0x4081df: jmp      0x40822f

; --- Block 0x4081e1 [LOOP_HEADER] 18 insns, callees: (none)
    0x4081e1: mov      rax, qword ptr [rbp - 0x20]
    0x4081e5: lea      rdx, [rax*8]
    0x4081ed: mov      rax, qword ptr [rbp - 0x28]
    0x4081f1: add      rax, rdx
    0x4081f4: mov      rax, qword ptr [rax]
    0x4081f7: cmp      qword ptr [rbp - 0x48], rax
    0x4081fb: seta     dl
    0x4081fe: mov      rax, qword ptr [rbp - 0x20]
    0x408202: add      rax, 1
    0x408206: lea      rcx, [rax*8]
    0x40820e: mov      rax, qword ptr [rbp - 0x28]
    0x408212: add      rax, rcx
    ... +6 more instructions

; --- Block 0x408225 [ITERATOR_STATE] 6 insns, callees: (none)
    0x408225: add      qword ptr [rbp - 0x18], 1
    0x40822a: add      qword ptr [rbp - 0x20], 1
    0x40822f: mov      rax, qword ptr [rbp - 0x20]
    0x408233: add      rax, 1
    0x408237: cmp      qword ptr [rbp - 0x40], rax
    0x40823b: ja       0x4081e1

; --- Block 0x40822a [ITERATOR_STATE] 5 insns, callees: (none)
    0x40822a: add      qword ptr [rbp - 0x20], 1
    0x40822f: mov      rax, qword ptr [rbp - 0x20]
    0x408233: add      rax, 1
    0x408237: cmp      qword ptr [rbp - 0x40], rax
    0x40823b: ja       0x4081e1

; --- Block 0x40822f [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40822f: mov      rax, qword ptr [rbp - 0x20]
    0x408233: add      rax, 1
    0x408237: cmp      qword ptr [rbp - 0x40], rax
    0x40823b: ja       0x4081e1

; --- Block 0x40823d [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40823d: cmp      qword ptr [rbp - 0x40], 0
    0x408242: je       0x40825c

; --- Block 0x408244 [BODY] 7 insns, callees: (none)
    0x408244: mov      rax, qword ptr [rbp - 0x40]
    0x408248: shl      rax, 3
    0x40824c: lea      rdx, [rax - 8]
    0x408250: mov      rax, qword ptr [rbp - 0x28]
    0x408254: add      rax, rdx
    0x408257: mov      rax, qword ptr [rax]
    0x40825a: jmp      0x408261

; --- Block 0x40825c [BODY] 5 insns, callees: sub_401030
    0x40825c: mov      eax, 0
    0x408261: mov      qword ptr [rbp - 0x30], rax
    0x408265: mov      rax, qword ptr [rbp - 0x28]
    0x408269: mov      rdi, rax
    0x40826c: call     0x401030

; --- Block 0x408261 [BODY] 4 insns, callees: sub_401030
    0x408261: mov      qword ptr [rbp - 0x30], rax
    0x408265: mov      rax, qword ptr [rbp - 0x28]
    0x408269: mov      rdi, rax
    0x40826c: call     0x401030

; --- Block 0x408271 [BODY] 12 insns, callees: (none)
    0x408271: mov      rdx, qword ptr [rbp - 0x18]
    0x408275: mov      rax, rdx
    0x408278: shl      rax, 2
    0x40827c: add      rax, rdx
    0x40827f: lea      rdx, [rax*4]
    0x408287: add      rax, rdx
    0x40828a: shl      rax, 2
    0x40828e: mov      rdx, rax
    0x408291: mov      rax, qword ptr [rbp - 0x30]
    0x408295: add      rax, rdx
    0x408298: leave    
    0x408299: ret      

```

**O2 blocks** (12 total):

```asm
; --- Block 0x407d70 [BODY] 11 insns, callees: sub_401100
    0x407d70: push     r13
    0x407d72: lea      r13, [rsi*8]
    0x407d7a: push     r12
    0x407d7c: mov      r12, rdi
    0x407d7f: mov      rdi, r13
    0x407d82: push     rbp
    0x407d83: mov      rbp, rsi
    0x407d86: push     rbx
    0x407d87: mov      rbx, rdx
    0x407d8a: sub      rsp, 8
    0x407d8e: call     0x401100

; --- Block 0x407d93 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407d93: mov      r8, rax
    0x407d96: test     rbp, rbp
    0x407d99: je       0x407e20

; --- Block 0x407d9f [BODY] 8 insns, callees: (none)
    0x407d9f: xor      eax, eax
    0x407da1: xor      edx, edx
    0x407da3: nop      dword ptr [rax + rax]
    0x407da8: add      rdx, qword ptr [r12 + rax*8]
    0x407dac: mov      qword ptr [r8 + rax*8], rdx
    0x407db0: add      rax, 1
    0x407db4: cmp      rbp, rax
    0x407db7: jne      0x407da8

; --- Block 0x407da8 [ITERATOR_STATE] 5 insns, callees: (none)
    0x407da8: add      rdx, qword ptr [r12 + rax*8]
    0x407dac: mov      qword ptr [r8 + rax*8], rdx
    0x407db0: add      rax, 1
    0x407db4: cmp      rbp, rax
    0x407db7: jne      0x407da8

; --- Block 0x407db9 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407db9: cmp      rbp, 1
    0x407dbd: je       0x407e25

; --- Block 0x407dbf [BODY] 17 insns, callees: (none)
    0x407dbf: mov      rdx, qword ptr [r8]
    0x407dc2: lea      rax, [r8 + 8]
    0x407dc6: lea      r9, [r8 + r13]
    0x407dca: xor      ecx, ecx
    0x407dcc: nop      dword ptr [rax]
    0x407dd0: cmp      rbx, rdx
    0x407dd3: mov      rdx, qword ptr [rax]
    0x407dd6: seta     dil
    0x407dda: cmp      rdx, rbx
    0x407ddd: setb     sil
    0x407de1: cmp      dil, sil
    0x407de4: setne    sil
    ... +5 more instructions

; --- Block 0x407dd0 [BODY] 12 insns, callees: (none)
    0x407dd0: cmp      rbx, rdx
    0x407dd3: mov      rdx, qword ptr [rax]
    0x407dd6: seta     dil
    0x407dda: cmp      rdx, rbx
    0x407ddd: setb     sil
    0x407de1: cmp      dil, sil
    0x407de4: setne    sil
    0x407de8: add      rax, 8
    0x407dec: movzx    esi, sil
    0x407df0: add      rcx, rsi
    0x407df3: cmp      rax, r9
    0x407df6: jne      0x407dd0

; --- Block 0x407df8 [LOOP_HEADER] 6 insns, callees: sub_401030
    0x407df8: lea      rax, [rcx + rcx*4]
    0x407dfc: lea      rdx, [rax + rax*4]
    0x407e00: mov      rax, qword ptr [r8 + r13 - 8]
    0x407e05: lea      r12, [rax + rdx*4]
    0x407e09: mov      rdi, r8
    0x407e0c: call     0x401030

; --- Block 0x407e09 [LOOP_HEADER] 2 insns, callees: sub_401030
    0x407e09: mov      rdi, r8
    0x407e0c: call     0x401030

; --- Block 0x407e11 [BODY] 7 insns, callees: (none)
    0x407e11: add      rsp, 8
    0x407e15: mov      rax, r12
    0x407e18: pop      rbx
    0x407e19: pop      rbp
    0x407e1a: pop      r12
    0x407e1c: pop      r13
    0x407e1e: ret      

; --- Block 0x407e20 [BODY] 2 insns, callees: (none)
    0x407e20: xor      r12d, r12d
    0x407e23: jmp      0x407e09

; --- Block 0x407e25 [BODY] 2 insns, callees: (none)
    0x407e25: xor      ecx, ecx
    0x407e27: jmp      0x407df8

```

**Hungarian matching result** (mean similarity: 0.743):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40823d` | BOUNDS_CHECK | `0x407db9` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x40822a` | ITERATOR_STATE | `0x407da8` | ITERATOR_STATE | 0.994 | GOOD |
| `0x4081c5` | BOUNDS_CHECK | `0x407d93` | BOUNDS_CHECK | 0.949 | GOOD |
| `0x408261` | BODY | `0x407e09` | LOOP_HEADER | 0.850 | GOOD |
| `0x40825c` | BODY | `0x407df8` | LOOP_HEADER | 0.843 | GOOD |
| `0x408225` | ITERATOR_STATE | `0x407d9f` | BODY | 0.826 | GOOD |
| `0x4081cf` | BODY | `0x407e20` | BODY | 0.645 | PARTIAL |
| `0x4081e1` | LOOP_HEADER | `0x407dbf` | BODY | 0.613 | PARTIAL |
| `0x408176` | BODY | `0x407e25` | BODY | 0.590 | PARTIAL |
| `0x408152` | BODY | `0x407d70` | BODY | 0.581 | PARTIAL |
| `0x408244` | BODY | `0x407e11` | BODY | 0.515 | PARTIAL |
| `0x40818c` | LOOP_HEADER | `0x407dd0` | BODY | 0.507 | PARTIAL |
| `0x40822f` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x408271` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `opt_04`

### Rust `opt_04` — O0: 32 blocks, O2: 9 blocks

**O0 blocks** (32 total):

```asm
; --- Block 0x452b20 [BODY] 12 insns, callees: (none)
    0x452b20: sub      rsp, 0xe8
    0x452b27: mov      qword ptr [rsp + 0x28], rcx
    0x452b2c: mov      qword ptr [rsp + 0x30], rdx
    0x452b31: mov      qword ptr [rsp + 0x38], rsi
    0x452b36: mov      qword ptr [rsp + 0x40], rdi
    0x452b3b: mov      qword ptr [rsp + 0x48], rdi
    0x452b40: mov      qword ptr [rsp + 0xa8], rsi
    0x452b48: mov      qword ptr [rsp + 0xb0], rdx
    0x452b50: mov      qword ptr [rsp + 0xb8], rcx
    0x452b58: mov      qword ptr [rsp + 0xc8], 3
    0x452b64: cmp      rdx, 3
    0x452b68: jb       0x452b83

; --- Block 0x452b6a [ITERATOR_STATE] 6 insns, callees: (none)
    0x452b6a: mov      rax, qword ptr [rsp + 0x30]
    0x452b6f: mov      rcx, rax
    0x452b72: sub      rcx, 3
    0x452b76: mov      qword ptr [rsp + 0x20], rcx
    0x452b7b: cmp      rax, 3
    0x452b7f: jb       0x452bac

; --- Block 0x452b81 [BODY] 1 insns, callees: (none)
    0x452b81: jmp      0x452b94

; --- Block 0x452b83 [BODY] 3 insns, callees: (none)
    0x452b83: mov      rax, qword ptr [rsp + 0x40]
    0x452b88: mov      qword ptr [rax], 0
    0x452b8f: jmp      0x452c4b

; --- Block 0x452b94 [ITERATOR_STATE] 6 insns, callees: (none)
    0x452b94: mov      rcx, qword ptr [rsp + 0x20]
    0x452b99: mov      rax, rcx
    0x452b9c: add      rax, 1
    0x452ba0: mov      qword ptr [rsp + 0x18], rax
    0x452ba5: cmp      rax, rcx
    0x452ba8: jb       0x452bd3

; --- Block 0x452baa [BODY] 1 insns, callees: (none)
    0x452baa: jmp      0x452bb9

; --- Block 0x452bac [BODY] 2 insns, callees: (none)
    0x452bac: lea      rdi, [rip + 0x9df05]
    0x452bb3: call     qword ptr [rip + 0xa2597]

; --- Block 0x452bb9 [BODY] 4 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x452bb9: mov      rsi, qword ptr [rsp + 0x18]
    0x452bbe: xor      eax, eax
    0x452bc0: mov      edi, eax
    0x452bc2: call     0x49b480

; --- Block 0x452bc7 [BODY] 3 insns, callees: (none)
    0x452bc7: mov      qword ptr [rsp + 0x50], rax
    0x452bcc: mov      qword ptr [rsp + 0x58], rdx
    0x452bd1: jmp      0x452be0

; --- Block 0x452bd3 [BODY] 2 insns, callees: (none)
    0x452bd3: lea      rdi, [rip + 0x9dede]
    0x452bda: call     qword ptr [rip + 0xa2550]

; --- Block 0x452be0 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x452be0: lea      rdi, [rsp + 0x50]
    0x452be5: call     0x49ad10

; --- Block 0x452bea [BOUNDS_CHECK] 4 insns, callees: (none)
    0x452bea: mov      qword ptr [rsp + 0x60], rax
    0x452bef: mov      qword ptr [rsp + 0x68], rdx
    0x452bf4: test     qword ptr [rsp + 0x60], 1
    0x452bfd: je       0x452c3f

; --- Block 0x452bff [BODY] 9 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x452bff: mov      rax, qword ptr [rsp + 0x68]
    0x452c04: mov      qword ptr [rsp + 0x10], rax
    0x452c09: mov      qword ptr [rsp + 0xd0], rax
    0x452c11: mov      byte ptr [rsp + 0x77], 1
    0x452c16: mov      qword ptr [rsp + 0x78], 0
    0x452c1f: xor      eax, eax
    0x452c21: mov      edi, eax
    0x452c23: mov      esi, 3
    0x452c28: call     0x49b480

; --- Block 0x452c2d [BODY] 3 insns, callees: (none)
    0x452c2d: mov      qword ptr [rsp + 0x80], rax
    0x452c35: mov      qword ptr [rsp + 0x88], rdx
    0x452c3d: jmp      0x452c58

; --- Block 0x452c3f [EPILOGUE] 5 insns, callees: (none)
    0x452c3f: mov      rax, qword ptr [rsp + 0x40]
    0x452c44: mov      qword ptr [rax], 0
    0x452c4b: mov      rax, qword ptr [rsp + 0x48]
    0x452c50: add      rsp, 0xe8
    0x452c57: ret      

; --- Block 0x452c4b [EPILOGUE] 3 insns, callees: (none)
    0x452c4b: mov      rax, qword ptr [rsp + 0x48]
    0x452c50: add      rsp, 0xe8
    0x452c57: ret      

; --- Block 0x452c58 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x452c58: lea      rdi, [rsp + 0x80]
    0x452c60: call     0x49ad10

; --- Block 0x452c65 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x452c65: mov      qword ptr [rsp + 0x90], rax
    0x452c6d: mov      qword ptr [rsp + 0x98], rdx
    0x452c75: test     qword ptr [rsp + 0x90], 1
    0x452c81: je       0x452caa

; --- Block 0x452c83 [BODY] 8 insns, callees: (none)
    0x452c83: mov      rcx, qword ptr [rsp + 0x10]
    0x452c88: mov      rdx, qword ptr [rsp + 0x98]
    0x452c90: mov      qword ptr [rsp + 0xd8], rdx
    0x452c98: mov      rax, rcx
    0x452c9b: add      rax, rdx
    0x452c9e: mov      qword ptr [rsp + 8], rax
    0x452ca3: cmp      rax, rcx
    0x452ca6: jb       0x452d1d

; --- Block 0x452ca8 [BODY] 1 insns, callees: (none)
    0x452ca8: jmp      0x452cd8

; --- Block 0x452caa [BOUNDS_CHECK] 2 insns, callees: (none)
    0x452caa: test     byte ptr [rsp + 0x77], 1
    0x452caf: je       0x452be0

; --- Block 0x452cb5 [BODY] 7 insns, callees: (none)
    0x452cb5: mov      rax, qword ptr [rsp + 0x40]
    0x452cba: mov      rdx, qword ptr [rsp + 0x10]
    0x452cbf: mov      rcx, qword ptr [rsp + 0x78]
    0x452cc4: mov      qword ptr [rax + 8], rdx
    0x452cc8: mov      qword ptr [rax + 0x10], rcx
    0x452ccc: mov      qword ptr [rax], 1
    0x452cd3: jmp      0x452c4b

; --- Block 0x452cd8 [BODY] 4 insns, callees: core::slice::<impl [T]>::get
    0x452cd8: mov      rdx, qword ptr [rsp + 8]
    0x452cdd: mov      rsi, qword ptr [rsp + 0x30]
    0x452ce2: mov      rdi, qword ptr [rsp + 0x38]
    0x452ce7: call     0x490f30

; --- Block 0x452cec [BODY] 2 insns, callees: <core::option::Option<T> as core::ops::try_trait::Try>::branch
    0x452cec: mov      rdi, rax
    0x452cef: call     0x460e80

; --- Block 0x452cf4 [BODY] 8 insns, callees: (none)
    0x452cf4: mov      qword ptr [rsp + 0xa0], rax
    0x452cfc: mov      rdx, qword ptr [rsp + 0xa0]
    0x452d04: xor      eax, eax
    0x452d06: mov      ecx, 1
    0x452d0b: cmp      rdx, 0
    0x452d0f: cmove    rax, rcx
    0x452d13: test     rax, 1
    0x452d19: jne      0x452d2a

; --- Block 0x452d1b [BODY] 1 insns, callees: (none)
    0x452d1b: jmp      0x452d39

; --- Block 0x452d1d [BODY] 2 insns, callees: (none)
    0x452d1d: lea      rdi, [rip + 0x9ddac]
    0x452d24: call     qword ptr [rip + 0xa2406]

; --- Block 0x452d2a [BODY] 2 insns, callees: <core::option::Option<T> as core::ops::try_trait::FromResidual<core::option::Option<core::convert::Infallible>>>::from_residual
    0x452d2a: mov      rdi, qword ptr [rsp + 0x40]
    0x452d2f: call     0x45feb0

; --- Block 0x452d34 [BODY] 1 insns, callees: (none)
    0x452d34: jmp      0x452c4b

; --- Block 0x452d39 [BODY] 6 insns, callees: <u64 as core::ops::arith::AddAssign<&u64>>::add_assign
    0x452d39: mov      rsi, qword ptr [rsp + 0xa0]
    0x452d41: mov      qword ptr [rsp], rsi
    0x452d45: mov      qword ptr [rsp + 0xe0], rsi
    0x452d4d: lea      rdi, [rsp + 0x78]
    0x452d52: lea      rdx, [rip + 0x9dd8f]
    0x452d59: call     0x495700

; --- Block 0x452d5e [BOUNDS_CHECK] 4 insns, callees: (none)
    0x452d5e: mov      rcx, qword ptr [rsp + 0x28]
    0x452d63: mov      rax, qword ptr [rsp]
    0x452d67: cmp      qword ptr [rax], rcx
    0x452d6a: ja       0x452c58

; --- Block 0x452d70 [BODY] 2 insns, callees: (none)
    0x452d70: mov      byte ptr [rsp + 0x77], 0
    0x452d75: jmp      0x452c58

```

**O2 blocks** (9 total):

```asm
; --- Block 0x429390 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x429390: mov      rax, rdi
    0x429393: cmp      rdx, 3
    0x429397: jae      0x42939f

; --- Block 0x429399 [BODY] 3 insns, callees: (none)
    0x429399: xor      edx, edx
    0x42939b: mov      qword ptr [rax], rdx
    0x42939e: ret      

; --- Block 0x42939f [BODY] 8 insns, callees: (none)
    0x42939f: mov      edi, 2
    0x4293a4: sub      rdi, rdx
    0x4293a7: mov      r8, 0xffffffffffffffff
    0x4293ae: xor      edx, edx
    0x4293b0: mov      r10, r8
    0x4293b3: add      r8, rdi
    0x4293b6: cmp      r8, -1
    0x4293ba: je       0x4293f1

; --- Block 0x4293b0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4293b0: mov      r10, r8
    0x4293b3: add      r8, rdi
    0x4293b6: cmp      r8, -1
    0x4293ba: je       0x4293f1

; --- Block 0x4293bc [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4293bc: mov      r9, qword ptr [rsi + r10*8 + 0x18]
    0x4293c1: lea      r8, [r10 + 1]
    0x4293c5: cmp      r9, rcx
    0x4293c8: jbe      0x4293b0

; --- Block 0x4293ca [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4293ca: mov      r11, qword ptr [rsi + r10*8 + 8]
    0x4293cf: cmp      r11, rcx
    0x4293d2: jbe      0x4293b0

; --- Block 0x4293d4 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4293d4: mov      r10, qword ptr [rsi + r10*8 + 0x10]
    0x4293d9: cmp      r10, rcx
    0x4293dc: jbe      0x4293b0

; --- Block 0x4293de [BODY] 7 insns, callees: (none)
    0x4293de: add      r10, r11
    0x4293e1: add      r10, r9
    0x4293e4: mov      qword ptr [rax + 8], r8
    0x4293e8: mov      qword ptr [rax + 0x10], r10
    0x4293ec: mov      edx, 1
    0x4293f1: mov      qword ptr [rax], rdx
    0x4293f4: ret      

; --- Block 0x4293f1 [EPILOGUE] 2 insns, callees: (none)
    0x4293f1: mov      qword ptr [rax], rdx
    0x4293f4: ret      

```

**Hungarian matching result** (mean similarity: 0.780):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x452bea` | BOUNDS_CHECK | `0x4293ca` | BOUNDS_CHECK | 0.900 | GOOD |
| `0x452c65` | BOUNDS_CHECK | `0x4293d4` | BOUNDS_CHECK | 0.892 | GOOD |
| `0x452d5e` | BOUNDS_CHECK | `0x4293bc` | BOUNDS_CHECK | 0.852 | GOOD |
| `0x452b94` | ITERATOR_STATE | `0x4293b0` | BOUNDS_CHECK | 0.833 | GOOD |
| `0x452b6a` | ITERATOR_STATE | `0x429390` | BOUNDS_CHECK | 0.785 | GOOD |
| `0x452d70` | BODY | `0x4293f1` | EPILOGUE | 0.769 | GOOD |
| `0x452bc7` | BODY | `0x429399` | BODY | 0.726 | GOOD |
| `0x452cb5` | BODY | `0x4293de` | BODY | 0.673 | PARTIAL |
| `0x452c83` | BODY | `0x42939f` | BODY | 0.589 | PARTIAL |
| `0x452b20` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452b81` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452b83` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452baa` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452bac` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452bb9` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452bd3` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452be0` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452bff` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452c2d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452c3f` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452c4b` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452c58` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452ca8` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452caa` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452cd8` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452cec` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452cf4` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452d1b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452d1d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452d2a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452d34` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x452d39` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `opt_04` — O0: 14 blocks, O2: 10 blocks

**O0 blocks** (14 total):

```asm
; --- Block 0x405ce1 [BODY] 11 insns, callees: (none)
    0x405ce1: push     rbp
    0x405ce2: mov      rbp, rsp
    0x405ce5: mov      qword ptr [rbp - 0x38], rdi
    0x405ce9: mov      qword ptr [rbp - 0x40], rsi
    0x405ced: mov      qword ptr [rbp - 0x48], rdx
    0x405cf1: mov      qword ptr [rbp - 0x50], rcx
    0x405cf5: mov      qword ptr [rbp - 0x58], r8
    0x405cf9: mov      qword ptr [rbp - 0x28], 3
    0x405d01: mov      rax, qword ptr [rbp - 0x40]
    0x405d05: cmp      rax, qword ptr [rbp - 0x28]
    0x405d09: jae      0x405d15

; --- Block 0x405d0b [BODY] 2 insns, callees: (none)
    0x405d0b: mov      eax, 0
    0x405d10: jmp      0x405dd7

; --- Block 0x405d15 [BODY] 2 insns, callees: (none)
    0x405d15: mov      qword ptr [rbp - 8], 0
    0x405d1d: jmp      0x405dbd

; --- Block 0x405d22 [LOOP_HEADER] 4 insns, callees: (none)
    0x405d22: mov      dword ptr [rbp - 0xc], 1
    0x405d29: mov      qword ptr [rbp - 0x18], 0
    0x405d31: mov      qword ptr [rbp - 0x20], 0
    0x405d39: jmp      0x405d8b

; --- Block 0x405d3b [LOOP_HEADER] 17 insns, callees: (none)
    0x405d3b: mov      rdx, qword ptr [rbp - 8]
    0x405d3f: mov      rax, qword ptr [rbp - 0x20]
    0x405d43: add      rax, rdx
    0x405d46: lea      rdx, [rax*8]
    0x405d4e: mov      rax, qword ptr [rbp - 0x38]
    0x405d52: add      rax, rdx
    0x405d55: mov      rax, qword ptr [rax]
    0x405d58: add      qword ptr [rbp - 0x18], rax
    0x405d5c: mov      rdx, qword ptr [rbp - 8]
    0x405d60: mov      rax, qword ptr [rbp - 0x20]
    0x405d64: add      rax, rdx
    0x405d67: lea      rdx, [rax*8]
    ... +5 more instructions

; --- Block 0x405d7f [ITERATOR_STATE] 5 insns, callees: (none)
    0x405d7f: mov      dword ptr [rbp - 0xc], 0
    0x405d86: add      qword ptr [rbp - 0x20], 1
    0x405d8b: mov      rax, qword ptr [rbp - 0x20]
    0x405d8f: cmp      rax, qword ptr [rbp - 0x28]
    0x405d93: jb       0x405d3b

; --- Block 0x405d86 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x405d86: add      qword ptr [rbp - 0x20], 1
    0x405d8b: mov      rax, qword ptr [rbp - 0x20]
    0x405d8f: cmp      rax, qword ptr [rbp - 0x28]
    0x405d93: jb       0x405d3b

; --- Block 0x405d8b [BOUNDS_CHECK] 3 insns, callees: (none)
    0x405d8b: mov      rax, qword ptr [rbp - 0x20]
    0x405d8f: cmp      rax, qword ptr [rbp - 0x28]
    0x405d93: jb       0x405d3b

; --- Block 0x405d95 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x405d95: cmp      dword ptr [rbp - 0xc], 0
    0x405d99: je       0x405db8

; --- Block 0x405d9b [BODY] 8 insns, callees: (none)
    0x405d9b: mov      rax, qword ptr [rbp - 0x50]
    0x405d9f: mov      rdx, qword ptr [rbp - 8]
    0x405da3: mov      qword ptr [rax], rdx
    0x405da6: mov      rax, qword ptr [rbp - 0x58]
    0x405daa: mov      rdx, qword ptr [rbp - 0x18]
    0x405dae: mov      qword ptr [rax], rdx
    0x405db1: mov      eax, 1
    0x405db6: jmp      0x405dd7

; --- Block 0x405db8 [ITERATOR_STATE] 6 insns, callees: (none)
    0x405db8: add      qword ptr [rbp - 8], 1
    0x405dbd: mov      rdx, qword ptr [rbp - 8]
    0x405dc1: mov      rax, qword ptr [rbp - 0x28]
    0x405dc5: add      rax, rdx
    0x405dc8: cmp      qword ptr [rbp - 0x40], rax
    0x405dcc: jae      0x405d22

; --- Block 0x405dbd [ITERATOR_STATE] 5 insns, callees: (none)
    0x405dbd: mov      rdx, qword ptr [rbp - 8]
    0x405dc1: mov      rax, qword ptr [rbp - 0x28]
    0x405dc5: add      rax, rdx
    0x405dc8: cmp      qword ptr [rbp - 0x40], rax
    0x405dcc: jae      0x405d22

; --- Block 0x405dd2 [EPILOGUE] 3 insns, callees: (none)
    0x405dd2: mov      eax, 0
    0x405dd7: pop      rbp
    0x405dd8: ret      

; --- Block 0x405dd7 [EPILOGUE] 2 insns, callees: (none)
    0x405dd7: pop      rbp
    0x405dd8: ret      

```

**O2 blocks** (10 total):

```asm
; --- Block 0x406610 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406610: xor      r9d, r9d
    0x406613: cmp      rsi, 2
    0x406617: jbe      0x406680

; --- Block 0x406619 [BODY] 18 insns, callees: (none)
    0x406619: push     rbp
    0x40661a: mov      r10, rdx
    0x40661d: mov      rbp, rcx
    0x406620: xor      r11d, r11d
    0x406623: push     rbx
    0x406624: mov      rbx, rsi
    0x406627: xor      esi, esi
    0x406629: nop      dword ptr [rax]
    0x406630: xor      eax, eax
    0x406632: xor      ecx, ecx
    0x406634: mov      r9d, 1
    0x40663a: mov      rdx, qword ptr [rdi + rax*8]
    ... +6 more instructions

; --- Block 0x406630 [LOOP_HEADER] 10 insns, callees: (none)
    0x406630: xor      eax, eax
    0x406632: xor      ecx, ecx
    0x406634: mov      r9d, 1
    0x40663a: mov      rdx, qword ptr [rdi + rax*8]
    0x40663e: add      rcx, rdx
    0x406641: cmp      rdx, r10
    0x406644: cmovbe   r9d, r11d
    0x406648: add      rax, 1
    0x40664c: cmp      rax, 3
    0x406650: jne      0x40663a

; --- Block 0x40663a [BODY] 7 insns, callees: (none)
    0x40663a: mov      rdx, qword ptr [rdi + rax*8]
    0x40663e: add      rcx, rdx
    0x406641: cmp      rdx, r10
    0x406644: cmovbe   r9d, r11d
    0x406648: add      rax, 1
    0x40664c: cmp      rax, 3
    0x406650: jne      0x40663a

; --- Block 0x406652 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x406652: test     r9d, r9d
    0x406655: jne      0x406670

; --- Block 0x406657 [ITERATOR_STATE] 5 insns, callees: (none)
    0x406657: lea      rax, [rsi + 1]
    0x40665b: add      rsi, 4
    0x40665f: add      rdi, 8
    0x406663: cmp      rbx, rsi
    0x406666: jb       0x406677

; --- Block 0x406668 [BODY] 2 insns, callees: (none)
    0x406668: mov      rsi, rax
    0x40666b: jmp      0x406630

; --- Block 0x406670 [BODY] 6 insns, callees: (none)
    0x406670: mov      qword ptr [rbp], rsi
    0x406674: mov      qword ptr [r8], rcx
    0x406677: mov      eax, r9d
    0x40667a: pop      rbx
    0x40667b: pop      rbp
    0x40667c: ret      

; --- Block 0x406677 [EPILOGUE] 4 insns, callees: (none)
    0x406677: mov      eax, r9d
    0x40667a: pop      rbx
    0x40667b: pop      rbp
    0x40667c: ret      

; --- Block 0x406680 [EPILOGUE] 2 insns, callees: (none)
    0x406680: mov      eax, r9d
    0x406683: ret      

```

**Hungarian matching result** (mean similarity: 0.736):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x405d95` | BOUNDS_CHECK | `0x406652` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x405d15` | BODY | `0x406668` | BODY | 0.974 | GOOD |
| `0x405dd2` | EPILOGUE | `0x406677` | EPILOGUE | 0.891 | GOOD |
| `0x405ce1` | BODY | `0x406630` | LOOP_HEADER | 0.776 | GOOD |
| `0x405d0b` | BODY | `0x406680` | EPILOGUE | 0.759 | GOOD |
| `0x405db8` | ITERATOR_STATE | `0x406670` | BODY | 0.645 | PARTIAL |
| `0x405d8b` | BOUNDS_CHECK | `0x406610` | BOUNDS_CHECK | 0.599 | PARTIAL |
| `0x405d7f` | ITERATOR_STATE | `0x406657` | ITERATOR_STATE | 0.591 | PARTIAL |
| `0x405dbd` | ITERATOR_STATE | `0x40663a` | BODY | 0.589 | PARTIAL |
| `0x405d3b` | LOOP_HEADER | `0x406619` | BODY | 0.538 | PARTIAL |
| `0x405d22` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x405d86` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x405d9b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x405dd7` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `opt_09`

### Rust `opt_09` — O0: 32 blocks, O2: 9 blocks

**O0 blocks** (32 total):

```asm
; --- Block 0x453830 [BODY] 11 insns, callees: (none)
    0x453830: sub      rsp, 0xb8
    0x453837: mov      qword ptr [rsp + 0x28], rcx
    0x45383c: mov      qword ptr [rsp + 0x30], rdx
    0x453841: mov      qword ptr [rsp + 0x38], rsi
    0x453846: mov      qword ptr [rsp + 0x40], rdi
    0x45384b: mov      qword ptr [rsp + 0x48], rdi
    0x453850: mov      qword ptr [rsp + 0x70], rsi
    0x453855: mov      qword ptr [rsp + 0x78], rdx
    0x45385a: mov      qword ptr [rsp + 0x80], rcx
    0x453862: cmp      rdx, 2
    0x453866: jb       0x45388a

; --- Block 0x453868 [BODY] 7 insns, callees: (none)
    0x453868: mov      rax, qword ptr [rsp + 0x30]
    0x45386d: mov      qword ptr [rsp + 0x50], 0
    0x453876: mov      rcx, rax
    0x453879: sub      rcx, 1
    0x45387d: mov      qword ptr [rsp + 0x20], rcx
    0x453882: cmp      rax, 1
    0x453886: jb       0x4538a4

; --- Block 0x453888 [BODY] 1 insns, callees: (none)
    0x453888: jmp      0x453898

; --- Block 0x45388a [BODY] 3 insns, callees: (none)
    0x45388a: mov      rax, qword ptr [rsp + 0x40]
    0x45388f: mov      qword ptr [rax], 0
    0x453896: jmp      0x45390a

; --- Block 0x453898 [BODY] 3 insns, callees: (none)
    0x453898: mov      rax, qword ptr [rsp + 0x20]
    0x45389d: mov      qword ptr [rsp + 0x58], rax
    0x4538a2: jmp      0x4538b1

; --- Block 0x4538a4 [BODY] 2 insns, callees: (none)
    0x4538a4: lea      rdi, [rip + 0x9d2b5]
    0x4538ab: call     qword ptr [rip + 0xa189f]

; --- Block 0x4538b1 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4538b1: mov      rax, qword ptr [rsp + 0x50]
    0x4538b6: cmp      rax, qword ptr [rsp + 0x58]
    0x4538bb: jb       0x4538cb

; --- Block 0x4538bd [BODY] 3 insns, callees: (none)
    0x4538bd: mov      rax, qword ptr [rsp + 0x40]
    0x4538c2: mov      qword ptr [rax], 0
    0x4538c9: jmp      0x45390a

; --- Block 0x4538cb [BODY] 4 insns, callees: core::slice::<impl [T]>::get
    0x4538cb: mov      rsi, qword ptr [rsp + 0x30]
    0x4538d0: mov      rdi, qword ptr [rsp + 0x38]
    0x4538d5: mov      rdx, qword ptr [rsp + 0x50]
    0x4538da: call     0x490f30

; --- Block 0x4538df [BODY] 2 insns, callees: <core::option::Option<T> as core::ops::try_trait::Try>::branch
    0x4538df: mov      rdi, rax
    0x4538e2: call     0x460e80

; --- Block 0x4538e7 [BODY] 8 insns, callees: (none)
    0x4538e7: mov      qword ptr [rsp + 0x60], rax
    0x4538ec: mov      rdx, qword ptr [rsp + 0x60]
    0x4538f1: xor      eax, eax
    0x4538f3: mov      ecx, 1
    0x4538f8: cmp      rdx, 0
    0x4538fc: cmove    rax, rcx
    0x453900: test     rax, 1
    0x453906: jne      0x453917

; --- Block 0x453908 [BODY] 1 insns, callees: (none)
    0x453908: jmp      0x453923

; --- Block 0x45390a [EPILOGUE] 3 insns, callees: (none)
    0x45390a: mov      rax, qword ptr [rsp + 0x48]
    0x45390f: add      rsp, 0xb8
    0x453916: ret      

; --- Block 0x453917 [BODY] 2 insns, callees: <core::option::Option<T> as core::ops::try_trait::FromResidual<core::option::Option<core::convert::Infallible>>>::from_residual
    0x453917: mov      rdi, qword ptr [rsp + 0x40]
    0x45391c: call     0x45fe90

; --- Block 0x453921 [BODY] 1 insns, callees: (none)
    0x453921: jmp      0x45390a

; --- Block 0x453923 [BODY] 7 insns, callees: core::slice::<impl [T]>::get
    0x453923: mov      rsi, qword ptr [rsp + 0x30]
    0x453928: mov      rdi, qword ptr [rsp + 0x38]
    0x45392d: mov      rax, qword ptr [rsp + 0x60]
    0x453932: mov      qword ptr [rsp + 0x18], rax
    0x453937: mov      qword ptr [rsp + 0x90], rax
    0x45393f: mov      rdx, qword ptr [rsp + 0x58]
    0x453944: call     0x490f30

; --- Block 0x453949 [BODY] 2 insns, callees: <core::option::Option<T> as core::ops::try_trait::Try>::branch
    0x453949: mov      rdi, rax
    0x45394c: call     0x460e80

; --- Block 0x453951 [BODY] 8 insns, callees: (none)
    0x453951: mov      qword ptr [rsp + 0x68], rax
    0x453956: mov      rdx, qword ptr [rsp + 0x68]
    0x45395b: xor      eax, eax
    0x45395d: mov      ecx, 1
    0x453962: cmp      rdx, 0
    0x453966: cmove    rax, rcx
    0x45396a: test     rax, 1
    0x453970: je       0x45397e

; --- Block 0x453972 [BODY] 2 insns, callees: <core::option::Option<T> as core::ops::try_trait::FromResidual<core::option::Option<core::convert::Infallible>>>::from_residual
    0x453972: mov      rdi, qword ptr [rsp + 0x40]
    0x453977: call     0x45fe90

; --- Block 0x45397c [BODY] 1 insns, callees: (none)
    0x45397c: jmp      0x45390a

; --- Block 0x45397e [BODY] 13 insns, callees: (none)
    0x45397e: mov      rcx, qword ptr [rsp + 0x28]
    0x453983: mov      rax, qword ptr [rsp + 0x18]
    0x453988: mov      rdx, qword ptr [rsp + 0x68]
    0x45398d: mov      qword ptr [rsp + 0x98], rdx
    0x453995: mov      rax, qword ptr [rax]
    0x453998: mov      rdx, qword ptr [rdx]
    0x45399b: mov      qword ptr [rsp + 0xa8], rax
    0x4539a3: mov      qword ptr [rsp + 0xb0], rdx
    0x4539ab: add      rax, rdx
    0x4539ae: mov      qword ptr [rsp + 0x10], rax
    0x4539b3: mov      qword ptr [rsp + 0xa0], rax
    0x4539bb: cmp      rax, rcx
    ... +1 more instructions

; --- Block 0x4539c0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4539c0: mov      rax, qword ptr [rsp + 0x10]
    0x4539c5: mov      rcx, qword ptr [rsp + 0x28]
    0x4539ca: cmp      rax, rcx
    0x4539cd: jb       0x453a0d

; --- Block 0x4539cf [BODY] 1 insns, callees: (none)
    0x4539cf: jmp      0x4539f4

; --- Block 0x4539d1 [BODY] 7 insns, callees: (none)
    0x4539d1: mov      rax, qword ptr [rsp + 0x40]
    0x4539d6: mov      rdx, qword ptr [rsp + 0x50]
    0x4539db: mov      rcx, qword ptr [rsp + 0x58]
    0x4539e0: mov      qword ptr [rax + 8], rdx
    0x4539e4: mov      qword ptr [rax + 0x10], rcx
    0x4539e8: mov      qword ptr [rax], 1
    0x4539ef: jmp      0x45390a

; --- Block 0x4539f4 [ITERATOR_STATE] 6 insns, callees: (none)
    0x4539f4: mov      rax, qword ptr [rsp + 0x58]
    0x4539f9: mov      rcx, rax
    0x4539fc: sub      rcx, 1
    0x453a00: mov      qword ptr [rsp + 8], rcx
    0x453a05: cmp      rax, 1
    0x453a09: jb       0x453a33

; --- Block 0x453a0b [BODY] 1 insns, callees: (none)
    0x453a0b: jmp      0x453a24

; --- Block 0x453a0d [ITERATOR_STATE] 6 insns, callees: (none)
    0x453a0d: mov      rcx, qword ptr [rsp + 0x50]
    0x453a12: mov      rax, rcx
    0x453a15: add      rax, 1
    0x453a19: mov      qword ptr [rsp], rax
    0x453a1d: cmp      rax, rcx
    0x453a20: jb       0x453a4e

; --- Block 0x453a22 [BODY] 1 insns, callees: (none)
    0x453a22: jmp      0x453a40

; --- Block 0x453a24 [BODY] 3 insns, callees: (none)
    0x453a24: mov      rax, qword ptr [rsp + 8]
    0x453a29: mov      qword ptr [rsp + 0x58], rax
    0x453a2e: jmp      0x4538b1

; --- Block 0x453a33 [BODY] 2 insns, callees: (none)
    0x453a33: lea      rdi, [rip + 0x9d13e]
    0x453a3a: call     qword ptr [rip + 0xa1710]

; --- Block 0x453a40 [BODY] 3 insns, callees: (none)
    0x453a40: mov      rax, qword ptr [rsp]
    0x453a44: mov      qword ptr [rsp + 0x50], rax
    0x453a49: jmp      0x4538b1

; --- Block 0x453a4e [BODY] 2 insns, callees: (none)
    0x453a4e: lea      rdi, [rip + 0x9d13b]
    0x453a55: call     qword ptr [rip + 0xa16d5]

```

**O2 blocks** (9 total):

```asm
; --- Block 0x429ba0 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x429ba0: mov      rax, rdi
    0x429ba3: cmp      rdx, 2
    0x429ba7: jae      0x429baf

; --- Block 0x429ba9 [BODY] 3 insns, callees: (none)
    0x429ba9: xor      edi, edi
    0x429bab: mov      qword ptr [rax], rdi
    0x429bae: ret      

; --- Block 0x429baf [BODY] 6 insns, callees: (none)
    0x429baf: lea      r8, [rdx - 1]
    0x429bb3: xor      edi, edi
    0x429bb5: xor      r9d, r9d
    0x429bb8: nop      dword ptr [rax + rax]
    0x429bc0: cmp      r9, rdx
    0x429bc3: jae      0x429be7

; --- Block 0x429bc0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x429bc0: cmp      r9, rdx
    0x429bc3: jae      0x429be7

; --- Block 0x429bc5 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x429bc5: cmp      r8, rdx
    0x429bc8: jae      0x429be7

; --- Block 0x429bca [BOUNDS_CHECK] 4 insns, callees: (none)
    0x429bca: mov      r10, qword ptr [rsi + r8*8]
    0x429bce: add      r10, qword ptr [rsi + r9*8]
    0x429bd2: cmp      r10, rcx
    0x429bd5: je       0x429beb

; --- Block 0x429bd7 [ITERATOR_STATE] 5 insns, callees: (none)
    0x429bd7: adc      r8, -1
    0x429bdb: cmp      r10, rcx
    0x429bde: adc      r9, 0
    0x429be2: cmp      r9, r8
    0x429be5: jb       0x429bc0

; --- Block 0x429be7 [EPILOGUE] 2 insns, callees: (none)
    0x429be7: mov      qword ptr [rax], rdi
    0x429bea: ret      

; --- Block 0x429beb [EPILOGUE] 5 insns, callees: (none)
    0x429beb: mov      qword ptr [rax + 8], r9
    0x429bef: mov      qword ptr [rax + 0x10], r8
    0x429bf3: mov      edi, 1
    0x429bf8: mov      qword ptr [rax], rdi
    0x429bfb: ret      

```

**Hungarian matching result** (mean similarity: 0.723):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4539c0` | BOUNDS_CHECK | `0x429bca` | BOUNDS_CHECK | 0.857 | GOOD |
| `0x453a0d` | ITERATOR_STATE | `0x429bd7` | ITERATOR_STATE | 0.786 | GOOD |
| `0x453917` | BODY | `0x429be7` | EPILOGUE | 0.762 | GOOD |
| `0x4538b1` | BOUNDS_CHECK | `0x429ba0` | BOUNDS_CHECK | 0.739 | GOOD |
| `0x45388a` | BODY | `0x429ba9` | BODY | 0.710 | GOOD |
| `0x4539f4` | ITERATOR_STATE | `0x429baf` | BODY | 0.695 | PARTIAL |
| `0x4538cb` | BODY | `0x429beb` | EPILOGUE | 0.661 | PARTIAL |
| `0x453972` | BODY | `0x429bc0` | BOUNDS_CHECK | 0.647 | PARTIAL |
| `0x4538a4` | BODY | `0x429bc5` | BOUNDS_CHECK | 0.647 | PARTIAL |
| `0x453830` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453868` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453888` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453898` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4538bd` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4538df` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4538e7` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453908` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45390a` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453921` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453923` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453949` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453951` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45397c` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45397e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4539cf` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4539d1` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453a0b` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453a22` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453a24` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453a33` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453a40` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453a4e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `opt_09` — O0: 11 blocks, O2: 9 blocks

**O0 blocks** (11 total):

```asm
; --- Block 0x40649a [BODY] 9 insns, callees: (none)
    0x40649a: push     rbp
    0x40649b: mov      rbp, rsp
    0x40649e: mov      qword ptr [rbp - 0x28], rdi
    0x4064a2: mov      qword ptr [rbp - 0x30], rsi
    0x4064a6: mov      qword ptr [rbp - 0x38], rdx
    0x4064aa: mov      qword ptr [rbp - 0x40], rcx
    0x4064ae: mov      qword ptr [rbp - 0x48], r8
    0x4064b2: cmp      qword ptr [rbp - 0x30], 1
    0x4064b7: ja       0x4064c3

; --- Block 0x4064b9 [BODY] 2 insns, callees: (none)
    0x4064b9: mov      eax, 0
    0x4064be: jmp      0x406558

; --- Block 0x4064c3 [BODY] 5 insns, callees: (none)
    0x4064c3: mov      qword ptr [rbp - 8], 0
    0x4064cb: mov      rax, qword ptr [rbp - 0x30]
    0x4064cf: sub      rax, 1
    0x4064d3: mov      qword ptr [rbp - 0x10], rax
    0x4064d7: jmp      0x406549

; --- Block 0x4064d9 [LOOP_HEADER] 15 insns, callees: (none)
    0x4064d9: mov      rax, qword ptr [rbp - 8]
    0x4064dd: lea      rdx, [rax*8]
    0x4064e5: mov      rax, qword ptr [rbp - 0x28]
    0x4064e9: add      rax, rdx
    0x4064ec: mov      rdx, qword ptr [rax]
    0x4064ef: mov      rax, qword ptr [rbp - 0x10]
    0x4064f3: lea      rcx, [rax*8]
    0x4064fb: mov      rax, qword ptr [rbp - 0x28]
    0x4064ff: add      rax, rcx
    0x406502: mov      rax, qword ptr [rax]
    0x406505: add      rax, rdx
    0x406508: mov      qword ptr [rbp - 0x18], rax
    ... +3 more instructions

; --- Block 0x406516 [BODY] 8 insns, callees: (none)
    0x406516: mov      rax, qword ptr [rbp - 0x40]
    0x40651a: mov      rdx, qword ptr [rbp - 8]
    0x40651e: mov      qword ptr [rax], rdx
    0x406521: mov      rax, qword ptr [rbp - 0x48]
    0x406525: mov      rdx, qword ptr [rbp - 0x10]
    0x406529: mov      qword ptr [rax], rdx
    0x40652c: mov      eax, 1
    0x406531: jmp      0x406558

; --- Block 0x406533 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406533: mov      rax, qword ptr [rbp - 0x18]
    0x406537: cmp      rax, qword ptr [rbp - 0x38]
    0x40653b: jae      0x406544

; --- Block 0x40653d [BODY] 2 insns, callees: (none)
    0x40653d: add      qword ptr [rbp - 8], 1
    0x406542: jmp      0x406549

; --- Block 0x406544 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x406544: sub      qword ptr [rbp - 0x10], 1
    0x406549: mov      rax, qword ptr [rbp - 8]
    0x40654d: cmp      rax, qword ptr [rbp - 0x10]
    0x406551: jb       0x4064d9

; --- Block 0x406549 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406549: mov      rax, qword ptr [rbp - 8]
    0x40654d: cmp      rax, qword ptr [rbp - 0x10]
    0x406551: jb       0x4064d9

; --- Block 0x406553 [EPILOGUE] 3 insns, callees: (none)
    0x406553: mov      eax, 0
    0x406558: pop      rbp
    0x406559: ret      

; --- Block 0x406558 [EPILOGUE] 2 insns, callees: (none)
    0x406558: pop      rbp
    0x406559: ret      

```

**O2 blocks** (9 total):

```asm
; --- Block 0x406b60 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x406b60: mov      r9, rdi
    0x406b63: xor      eax, eax
    0x406b65: cmp      rsi, 1
    0x406b69: jbe      0x406b9b

; --- Block 0x406b6b [BODY] 3 insns, callees: (none)
    0x406b6b: sub      rsi, 1
    0x406b6f: xor      edi, edi
    0x406b71: jmp      0x406b81

; --- Block 0x406b78 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406b78: add      rdi, 1
    0x406b7c: cmp      rdi, rsi
    0x406b7f: jae      0x406b99

; --- Block 0x406b81 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x406b81: mov      rax, qword ptr [r9 + rsi*8]
    0x406b85: add      rax, qword ptr [r9 + rdi*8]
    0x406b89: cmp      rax, rdx
    0x406b8c: je       0x406ba0

; --- Block 0x406b8e [BODY] 1 insns, callees: (none)
    0x406b8e: jb       0x406b78

; --- Block 0x406b90 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406b90: sub      rsi, 1
    0x406b94: cmp      rdi, rsi
    0x406b97: jb       0x406b81

; --- Block 0x406b99 [BODY] 2 insns, callees: (none)
    0x406b99: xor      eax, eax
    0x406b9b: ret      

; --- Block 0x406b9b [EPILOGUE] 1 insns, callees: (none)
    0x406b9b: ret      

; --- Block 0x406ba0 [EPILOGUE] 4 insns, callees: (none)
    0x406ba0: mov      qword ptr [rcx], rdi
    0x406ba3: mov      eax, 1
    0x406ba8: mov      qword ptr [r8], rsi
    0x406bab: ret      

```

**Hungarian matching result** (mean similarity: 0.700):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x406544` | BOUNDS_CHECK | `0x406b60` | BOUNDS_CHECK | 0.845 | GOOD |
| `0x406549` | BOUNDS_CHECK | `0x406b90` | BOUNDS_CHECK | 0.787 | GOOD |
| `0x406533` | BOUNDS_CHECK | `0x406b78` | BOUNDS_CHECK | 0.777 | GOOD |
| `0x406553` | EPILOGUE | `0x406ba0` | EPILOGUE | 0.771 | GOOD |
| `0x406558` | EPILOGUE | `0x406b9b` | EPILOGUE | 0.662 | PARTIAL |
| `0x4064d9` | LOOP_HEADER | `0x406b81` | BOUNDS_CHECK | 0.659 | PARTIAL |
| `0x4064c3` | BODY | `0x406b6b` | BODY | 0.657 | PARTIAL |
| `0x4064b9` | BODY | `0x406b99` | BODY | 0.654 | PARTIAL |
| `0x40653d` | BODY | `0x406b8e` | BODY | 0.491 | PARTIAL |
| `0x40649a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406516` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `opt_06`

### Rust `opt_06` — O0: 12 blocks, O2: 10 blocks

**O0 blocks** (12 total):

```asm
; --- Block 0x4531d0 [BODY] 6 insns, callees: core::slice::<impl [T]>::iter
    0x4531d0: sub      rsp, 0xb8
    0x4531d7: mov      qword ptr [rsp], rdi
    0x4531db: mov      qword ptr [rsp + 8], rsi
    0x4531e0: mov      qword ptr [rsp + 0x38], rdi
    0x4531e5: mov      qword ptr [rsp + 0x40], rsi
    0x4531ea: call     0x4910a0

; --- Block 0x4531ef [BODY] 4 insns, callees: <core::slice::iter::Iter<T> as core::iter::traits::iterator::Iterator>::find
    0x4531ef: mov      qword ptr [rsp + 0x18], rax
    0x4531f4: mov      qword ptr [rsp + 0x20], rdx
    0x4531f9: lea      rdi, [rsp + 0x18]
    0x4531fe: call     0x480280

; --- Block 0x453203 [BODY] 3 insns, callees: core::option::Option<T>::map
    0x453203: mov      rdi, rax
    0x453206: mov      qword ptr [rsp + 0x48], rdi
    0x45320b: call     0x4604a0

; --- Block 0x453210 [BODY] 5 insns, callees: core::option::Option<T>::filter
    0x453210: mov      rdi, rax
    0x453213: mov      rsi, rdx
    0x453216: mov      qword ptr [rsp + 0x50], rdi
    0x45321b: mov      qword ptr [rsp + 0x58], rsi
    0x453220: call     0x460560

; --- Block 0x453225 [BODY] 6 insns, callees: core::option::Option<T>::unwrap_or
    0x453225: mov      rdi, rax
    0x453228: mov      rsi, rdx
    0x45322b: mov      qword ptr [rsp + 0x60], rdi
    0x453230: mov      qword ptr [rsp + 0x68], rsi
    0x453235: mov      edx, 0x2a
    0x45323a: call     0x460c50

; --- Block 0x45323f [BODY] 5 insns, callees: core::slice::<impl [T]>::iter
    0x45323f: mov      rdi, qword ptr [rsp]
    0x453243: mov      rsi, qword ptr [rsp + 8]
    0x453248: mov      qword ptr [rsp + 0x10], rax
    0x45324d: mov      qword ptr [rsp + 0x70], rax
    0x453252: call     0x4910a0

; --- Block 0x453257 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::rev
    0x453257: mov      rdi, rax
    0x45325a: mov      rsi, rdx
    0x45325d: call     0x47dea0

; --- Block 0x453262 [BODY] 4 insns, callees: <core::iter::adapters::rev::Rev<I> as core::iter::traits::iterator::Iterator>::find
    0x453262: mov      qword ptr [rsp + 0x28], rax
    0x453267: mov      qword ptr [rsp + 0x30], rdx
    0x45326c: lea      rdi, [rsp + 0x28]
    0x453271: call     0x48fda0

; --- Block 0x453276 [BODY] 3 insns, callees: core::option::Option<T>::map
    0x453276: mov      rdi, rax
    0x453279: mov      qword ptr [rsp + 0x78], rdi
    0x45327e: call     0x460230

; --- Block 0x453283 [BODY] 5 insns, callees: core::option::Option<T>::and_then
    0x453283: mov      rdi, rax
    0x453286: mov      rsi, rdx
    0x453289: mov      qword ptr [rsp + 0x80], rdi
    0x453291: mov      qword ptr [rsp + 0x88], rsi
    0x453299: call     0x460b00

; --- Block 0x45329e [BODY] 6 insns, callees: core::option::Option<T>::unwrap_or
    0x45329e: mov      rdi, rax
    0x4532a1: mov      rsi, rdx
    0x4532a4: mov      qword ptr [rsp + 0x90], rdi
    0x4532ac: mov      qword ptr [rsp + 0x98], rsi
    0x4532b4: mov      edx, 7
    0x4532b9: call     0x460c50

; --- Block 0x4532be [BODY] 8 insns, callees: (none)
    0x4532be: mov      rcx, rax
    0x4532c1: mov      rax, qword ptr [rsp + 0x10]
    0x4532c6: mov      qword ptr [rsp + 0xa0], rcx
    0x4532ce: mov      qword ptr [rsp + 0xa8], rax
    0x4532d6: mov      qword ptr [rsp + 0xb0], rcx
    0x4532de: add      rax, rcx
    0x4532e1: add      rsp, 0xb8
    0x4532e8: ret      

```

**O2 blocks** (10 total):

```asm
; --- Block 0x429750 [BODY] 6 insns, callees: (none)
    0x429750: shl      rsi, 3
    0x429754: xor      edx, edx
    0x429756: nop      word ptr cs:[rax + rax]
    0x429760: mov      rcx, rdx
    0x429763: cmp      rsi, rdx
    0x429766: je       0x429777

; --- Block 0x429760 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x429760: mov      rcx, rdx
    0x429763: cmp      rsi, rdx
    0x429766: je       0x429777

; --- Block 0x429768 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x429768: mov      rax, qword ptr [rdi + rcx]
    0x42976c: lea      rdx, [rcx + 8]
    0x429770: test     al, 1
    0x429772: jne      0x429760

; --- Block 0x429774 [ITERATOR_STATE] 5 insns, callees: (none)
    0x429774: add      rax, rax
    0x429777: mov      rdx, rsi
    0x42977a: nop      word ptr [rax + rax]
    0x429780: test     rdx, rdx
    0x429783: je       0x4297aa

; --- Block 0x429777 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x429777: mov      rdx, rsi
    0x42977a: nop      word ptr [rax + rax]
    0x429780: test     rdx, rdx
    0x429783: je       0x4297aa

; --- Block 0x429780 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x429780: test     rdx, rdx
    0x429783: je       0x4297aa

; --- Block 0x429785 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x429785: mov      r8, qword ptr [rdi + rdx - 8]
    0x42978a: add      rdx, -8
    0x42978e: test     r8b, 1
    0x429792: je       0x429780

; --- Block 0x429794 [BODY] 5 insns, callees: (none)
    0x429794: lea      rdi, [r8 + r8*2]
    0x429798: cmp      rdi, 0xc8
    0x42979f: mov      edx, 7
    0x4297a4: cmovb    rdx, rdi
    0x4297a8: jmp      0x4297af

; --- Block 0x4297aa [BODY] 8 insns, callees: (none)
    0x4297aa: mov      edx, 7
    0x4297af: cmp      rax, 0x64
    0x4297b3: mov      edi, 0x2a
    0x4297b8: cmovae   rax, rdi
    0x4297bc: cmp      rsi, rcx
    0x4297bf: cmove    rax, rdi
    0x4297c3: add      rax, rdx
    0x4297c6: ret      

; --- Block 0x4297af [BODY] 7 insns, callees: (none)
    0x4297af: cmp      rax, 0x64
    0x4297b3: mov      edi, 0x2a
    0x4297b8: cmovae   rax, rdi
    0x4297bc: cmp      rsi, rcx
    0x4297bf: cmove    rax, rdi
    0x4297c3: add      rax, rdx
    0x4297c6: ret      

```

**Hungarian matching result** (mean similarity: 0.593):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4531ef` | BODY | `0x429768` | BOUNDS_CHECK | 0.734 | GOOD |
| `0x453203` | BODY | `0x429760` | BOUNDS_CHECK | 0.689 | PARTIAL |
| `0x453262` | BODY | `0x429777` | BOUNDS_CHECK | 0.686 | PARTIAL |
| `0x45323f` | BODY | `0x429774` | ITERATOR_STATE | 0.676 | PARTIAL |
| `0x4532be` | BODY | `0x4297aa` | BODY | 0.575 | PARTIAL |
| `0x453225` | BODY | `0x4297af` | BODY | 0.567 | PARTIAL |
| `0x45329e` | BODY | `0x429794` | BODY | 0.558 | PARTIAL |
| `0x453276` | BODY | `0x429780` | BOUNDS_CHECK | 0.511 | PARTIAL |
| `0x4531d0` | BODY | `0x429750` | BODY | 0.492 | PARTIAL |
| `0x453210` | BODY | `0x429785` | BOUNDS_CHECK | 0.444 | PARTIAL |
| `0x453257` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x453283` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `opt_06` — O0: 29 blocks, O2: 13 blocks

**O0 blocks** (29 total):

```asm
; --- Block 0x405ff4 [BODY] 8 insns, callees: (none)
    0x405ff4: push     rbp
    0x405ff5: mov      rbp, rsp
    0x405ff8: mov      qword ptr [rbp - 0x68], rdi
    0x405ffc: mov      qword ptr [rbp - 0x70], rsi
    0x406000: mov      qword ptr [rbp - 8], 0
    0x406008: mov      dword ptr [rbp - 0xc], 0
    0x40600f: mov      qword ptr [rbp - 0x18], 0
    0x406017: jmp      0x40605f

; --- Block 0x406019 [LOOP_HEADER] 8 insns, callees: (none)
    0x406019: mov      rax, qword ptr [rbp - 0x18]
    0x40601d: lea      rdx, [rax*8]
    0x406025: mov      rax, qword ptr [rbp - 0x68]
    0x406029: add      rax, rdx
    0x40602c: mov      rax, qword ptr [rax]
    0x40602f: and      eax, 1
    0x406032: test     rax, rax
    0x406035: jne      0x40605a

; --- Block 0x406037 [BODY] 8 insns, callees: (none)
    0x406037: mov      rax, qword ptr [rbp - 0x18]
    0x40603b: lea      rdx, [rax*8]
    0x406043: mov      rax, qword ptr [rbp - 0x68]
    0x406047: add      rax, rdx
    0x40604a: mov      rax, qword ptr [rax]
    0x40604d: mov      qword ptr [rbp - 8], rax
    0x406051: mov      dword ptr [rbp - 0xc], 1
    0x406058: jmp      0x406069

; --- Block 0x40605a [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40605a: add      qword ptr [rbp - 0x18], 1
    0x40605f: mov      rax, qword ptr [rbp - 0x18]
    0x406063: cmp      rax, qword ptr [rbp - 0x70]
    0x406067: jb       0x406019

; --- Block 0x40605f [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40605f: mov      rax, qword ptr [rbp - 0x18]
    0x406063: cmp      rax, qword ptr [rbp - 0x70]
    0x406067: jb       0x406019

; --- Block 0x406069 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x406069: cmp      dword ptr [rbp - 0xc], 0
    0x40606d: je       0x406078

; --- Block 0x40606f [BODY] 3 insns, callees: (none)
    0x40606f: mov      rax, qword ptr [rbp - 8]
    0x406073: add      rax, rax
    0x406076: jmp      0x40607d

; --- Block 0x406078 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x406078: mov      eax, 0
    0x40607d: mov      qword ptr [rbp - 0x38], rax
    0x406081: cmp      dword ptr [rbp - 0xc], 0
    0x406085: je       0x406094

; --- Block 0x40607d [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40607d: mov      qword ptr [rbp - 0x38], rax
    0x406081: cmp      dword ptr [rbp - 0xc], 0
    0x406085: je       0x406094

; --- Block 0x406087 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x406087: cmp      qword ptr [rbp - 0x38], 0x63
    0x40608c: ja       0x406094

; --- Block 0x40608e [BODY] 2 insns, callees: (none)
    0x40608e: mov      rax, qword ptr [rbp - 0x38]
    0x406092: jmp      0x406099

; --- Block 0x406094 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x406094: mov      eax, 0
    0x406099: mov      qword ptr [rbp - 0x40], rax
    0x40609d: cmp      dword ptr [rbp - 0xc], 0
    0x4060a1: je       0x4060b0

; --- Block 0x406099 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406099: mov      qword ptr [rbp - 0x40], rax
    0x40609d: cmp      dword ptr [rbp - 0xc], 0
    0x4060a1: je       0x4060b0

; --- Block 0x4060a3 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4060a3: cmp      qword ptr [rbp - 0x38], 0x63
    0x4060a8: ja       0x4060b0

; --- Block 0x4060aa [BODY] 2 insns, callees: (none)
    0x4060aa: mov      rax, qword ptr [rbp - 0x40]
    0x4060ae: jmp      0x4060b5

; --- Block 0x4060b0 [BODY] 7 insns, callees: (none)
    0x4060b0: mov      eax, 0x2a
    0x4060b5: mov      qword ptr [rbp - 0x48], rax
    0x4060b9: mov      qword ptr [rbp - 0x20], 0
    0x4060c1: mov      dword ptr [rbp - 0x24], 0
    0x4060c8: mov      rax, qword ptr [rbp - 0x70]
    0x4060cc: mov      qword ptr [rbp - 0x30], rax
    0x4060d0: jmp      0x406118

; --- Block 0x4060b5 [BODY] 6 insns, callees: (none)
    0x4060b5: mov      qword ptr [rbp - 0x48], rax
    0x4060b9: mov      qword ptr [rbp - 0x20], 0
    0x4060c1: mov      dword ptr [rbp - 0x24], 0
    0x4060c8: mov      rax, qword ptr [rbp - 0x70]
    0x4060cc: mov      qword ptr [rbp - 0x30], rax
    0x4060d0: jmp      0x406118

; --- Block 0x4060d2 [LOOP_HEADER] 9 insns, callees: (none)
    0x4060d2: mov      rax, qword ptr [rbp - 0x30]
    0x4060d6: shl      rax, 3
    0x4060da: lea      rdx, [rax - 8]
    0x4060de: mov      rax, qword ptr [rbp - 0x68]
    0x4060e2: add      rax, rdx
    0x4060e5: mov      rax, qword ptr [rax]
    0x4060e8: and      eax, 1
    0x4060eb: test     rax, rax
    0x4060ee: je       0x406113

; --- Block 0x4060f0 [BODY] 9 insns, callees: (none)
    0x4060f0: mov      rax, qword ptr [rbp - 0x30]
    0x4060f4: shl      rax, 3
    0x4060f8: lea      rdx, [rax - 8]
    0x4060fc: mov      rax, qword ptr [rbp - 0x68]
    0x406100: add      rax, rdx
    0x406103: mov      rax, qword ptr [rax]
    0x406106: mov      qword ptr [rbp - 0x20], rax
    0x40610a: mov      dword ptr [rbp - 0x24], 1
    0x406111: jmp      0x40611f

; --- Block 0x406113 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406113: sub      qword ptr [rbp - 0x30], 1
    0x406118: cmp      qword ptr [rbp - 0x30], 0
    0x40611d: jne      0x4060d2

; --- Block 0x406118 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x406118: cmp      qword ptr [rbp - 0x30], 0
    0x40611d: jne      0x4060d2

; --- Block 0x40611f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40611f: cmp      dword ptr [rbp - 0x24], 0
    0x406123: je       0x406134

; --- Block 0x406125 [BODY] 5 insns, callees: (none)
    0x406125: mov      rdx, qword ptr [rbp - 0x20]
    0x406129: mov      rax, rdx
    0x40612c: add      rax, rax
    0x40612f: add      rax, rdx
    0x406132: jmp      0x406139

; --- Block 0x406134 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x406134: mov      eax, 0
    0x406139: mov      qword ptr [rbp - 0x50], rax
    0x40613d: cmp      dword ptr [rbp - 0x24], 0
    0x406141: je       0x406153

; --- Block 0x406139 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x406139: mov      qword ptr [rbp - 0x50], rax
    0x40613d: cmp      dword ptr [rbp - 0x24], 0
    0x406141: je       0x406153

; --- Block 0x406143 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x406143: cmp      qword ptr [rbp - 0x50], 0xc7
    0x40614b: ja       0x406153

; --- Block 0x40614d [BODY] 2 insns, callees: (none)
    0x40614d: mov      rax, qword ptr [rbp - 0x50]
    0x406151: jmp      0x406158

; --- Block 0x406153 [BODY] 7 insns, callees: (none)
    0x406153: mov      eax, 7
    0x406158: mov      qword ptr [rbp - 0x58], rax
    0x40615c: mov      rdx, qword ptr [rbp - 0x48]
    0x406160: mov      rax, qword ptr [rbp - 0x58]
    0x406164: add      rax, rdx
    0x406167: pop      rbp
    0x406168: ret      

; --- Block 0x406158 [BODY] 6 insns, callees: (none)
    0x406158: mov      qword ptr [rbp - 0x58], rax
    0x40615c: mov      rdx, qword ptr [rbp - 0x48]
    0x406160: mov      rax, qword ptr [rbp - 0x58]
    0x406164: add      rax, rdx
    0x406167: pop      rbp
    0x406168: ret      

```

**O2 blocks** (13 total):

```asm
; --- Block 0x4068a0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4068a0: test     rsi, rsi
    0x4068a3: je       0x406905

; --- Block 0x4068a5 [BODY] 2 insns, callees: (none)
    0x4068a5: xor      eax, eax
    0x4068a7: jmp      0x4068b9

; --- Block 0x4068b0 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4068b0: add      rax, 1
    0x4068b4: cmp      rsi, rax
    0x4068b7: je       0x4068f0

; --- Block 0x4068b9 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4068b9: mov      rdx, qword ptr [rdi + rax*8]
    0x4068bd: test     dl, 1
    0x4068c0: jne      0x4068b0

; --- Block 0x4068c2 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4068c2: add      rdx, rdx
    0x4068c5: cmp      rdx, 0x63
    0x4068c9: jbe      0x4068d6

; --- Block 0x4068cb [BODY] 1 insns, callees: (none)
    0x4068cb: jmp      0x4068f0

; --- Block 0x4068d0 [LOOP_HEADER] 2 insns, callees: (none)
    0x4068d0: sub      rsi, 1
    0x4068d4: je       0x406900

; --- Block 0x4068d6 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4068d6: mov      rax, qword ptr [rdi + rsi*8 - 8]
    0x4068db: test     al, 1
    0x4068dd: je       0x4068d0

; --- Block 0x4068df [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4068df: lea      rax, [rax + rax*2]
    0x4068e3: cmp      rax, 0xc7
    0x4068e9: ja       0x406900

; --- Block 0x4068eb [EPILOGUE] 2 insns, callees: (none)
    0x4068eb: add      rax, rdx
    0x4068ee: ret      

; --- Block 0x4068f0 [BODY] 2 insns, callees: (none)
    0x4068f0: mov      edx, 0x2a
    0x4068f5: jmp      0x4068d6

; --- Block 0x406900 [BODY] 2 insns, callees: (none)
    0x406900: lea      rax, [rdx + 7]
    0x406904: ret      

; --- Block 0x406905 [EPILOGUE] 2 insns, callees: (none)
    0x406905: mov      eax, 0x31
    0x40690a: ret      

```

**Hungarian matching result** (mean similarity: 0.786):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40605f` | BOUNDS_CHECK | `0x4068d6` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x406069` | BOUNDS_CHECK | `0x4068a0` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x406099` | BOUNDS_CHECK | `0x4068b9` | BOUNDS_CHECK | 0.991 | GOOD |
| `0x406087` | BOUNDS_CHECK | `0x4068c2` | BOUNDS_CHECK | 0.821 | GOOD |
| `0x406143` | BOUNDS_CHECK | `0x4068df` | BOUNDS_CHECK | 0.818 | GOOD |
| `0x40607d` | BOUNDS_CHECK | `0x4068b0` | BOUNDS_CHECK | 0.812 | GOOD |
| `0x4060b0` | BODY | `0x4068f0` | BODY | 0.790 | GOOD |
| `0x40608e` | BODY | `0x4068a5` | BODY | 0.769 | GOOD |
| `0x406113` | BOUNDS_CHECK | `0x4068d0` | LOOP_HEADER | 0.752 | GOOD |
| `0x4060aa` | BODY | `0x4068cb` | BODY | 0.639 | PARTIAL |
| `0x40611f` | BOUNDS_CHECK | `0x406900` | BODY | 0.637 | PARTIAL |
| `0x406118` | BOUNDS_CHECK | `0x4068eb` | EPILOGUE | 0.633 | PARTIAL |
| `0x40614d` | BODY | `0x406905` | EPILOGUE | 0.554 | PARTIAL |
| `0x405ff4` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406019` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406037` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40605a` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x40606f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406078` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406094` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4060a3` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4060b5` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4060d2` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4060f0` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406125` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406134` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406139` | BOUNDS_CHECK | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406153` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x406158` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `opt_20`

### Rust `opt_20` — O0: 21 blocks, O2: 28 blocks

**O0 blocks** (21 total):

```asm
; --- Block 0x455050 [BODY] 12 insns, callees: core::str::<impl str>::split
    0x455050: sub      rsp, 0x1d8
    0x455057: mov      rdx, rsi
    0x45505a: mov      rsi, rdi
    0x45505d: mov      qword ptr [rsp + 0x168], rsi
    0x455065: mov      qword ptr [rsp + 0x170], rdx
    0x45506d: mov      qword ptr [rsp + 0x10], 0
    0x455076: mov      qword ptr [rsp + 0x18], 0
    0x45507f: mov      qword ptr [rsp + 0x20], 0
    0x455088: mov      qword ptr [rsp + 0x30], 0
    0x455091: lea      rdi, [rsp + 0x88]
    0x455099: mov      ecx, 0x2c
    0x45509e: call     0x43e1b0

; --- Block 0x4550a3 [BODY] 3 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x4550a3: lea      rdi, [rsp + 0x40]
    0x4550a8: lea      rsi, [rsp + 0x88]
    0x4550b0: call     0x493fb0

; --- Block 0x4550b5 [BODY] 4 insns, callees: sub_ed310
    0x4550b5: lea      rdi, [rsp + 0xd0]
    0x4550bd: lea      rsi, [rsp + 0x40]
    0x4550c2: mov      edx, 0x48
    0x4550c7: call     0x4ed310

; --- Block 0x4550cc [LOOP_HEADER] 2 insns, callees: <core::str::iter::Split<P> as core::iter::traits::iterator::Iterator>::next
    0x4550cc: lea      rdi, [rsp + 0xd0]
    0x4550d4: call     0x4940a0

; --- Block 0x4550d9 [BODY] 9 insns, callees: (none)
    0x4550d9: mov      qword ptr [rsp + 0x118], rax
    0x4550e1: mov      qword ptr [rsp + 0x120], rdx
    0x4550e9: mov      rdx, qword ptr [rsp + 0x118]
    0x4550f1: mov      eax, 1
    0x4550f6: xor      ecx, ecx
    0x4550f8: cmp      rdx, 0
    0x4550fc: cmove    rax, rcx
    0x455100: test     rax, 1
    0x455106: je       0x45516a

; --- Block 0x455108 [BODY] 5 insns, callees: core::str::<impl str>::trim
    0x455108: mov      rdi, qword ptr [rsp + 0x118]
    0x455110: mov      rsi, qword ptr [rsp + 0x120]
    0x455118: mov      qword ptr [rsp + 0x188], rdi
    0x455120: mov      qword ptr [rsp + 0x190], rsi
    0x455128: call     0x4714e0

; --- Block 0x45512d [BODY] 5 insns, callees: core::str::<impl str>::parse
    0x45512d: mov      rsi, rax
    0x455130: mov      qword ptr [rsp + 0x198], rsi
    0x455138: mov      qword ptr [rsp + 0x1a0], rdx
    0x455140: lea      rdi, [rsp + 0x128]
    0x455148: call     0x43e150

; --- Block 0x45514d [BODY] 5 insns, callees: (none)
    0x45514d: mov      al, byte ptr [rsp + 0x128]
    0x455154: and      al, 1
    0x455156: movzx    eax, al
    0x455159: test     rax, 1
    0x45515f: jne      0x4550cc

; --- Block 0x455165 [BODY] 1 insns, callees: (none)
    0x455165: jmp      0x455254

; --- Block 0x45516a [BODY] 10 insns, callees: (none)
    0x45516a: mov      rsi, qword ptr [rsp + 0x20]
    0x45516f: mov      rdx, qword ptr [rsp + 0x28]
    0x455174: mov      rcx, qword ptr [rsp + 0x30]
    0x455179: mov      rax, qword ptr [rsp + 0x38]
    0x45517e: mov      qword ptr [rsp + 0x148], rsi
    0x455186: mov      qword ptr [rsp + 0x150], rdx
    0x45518e: mov      qword ptr [rsp + 0x158], rcx
    0x455196: mov      qword ptr [rsp + 0x160], rax
    0x45519e: test     qword ptr [rsp + 0x148], 1
    0x4551aa: je       0x4551ba

; --- Block 0x4551ac [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4551ac: test     qword ptr [rsp + 0x158], 1
    0x4551b8: jne      0x4551c8

; --- Block 0x4551ba [BODY] 2 insns, callees: (none)
    0x4551ba: mov      qword ptr [rsp + 0x140], 0
    0x4551c6: jmp      0x455214

; --- Block 0x4551c8 [BODY] 9 insns, callees: (none)
    0x4551c8: mov      rax, qword ptr [rsp + 0x150]
    0x4551d0: mov      qword ptr [rsp + 0x178], rax
    0x4551d8: mov      rcx, qword ptr [rsp + 0x160]
    0x4551e0: mov      qword ptr [rsp + 0x180], rcx
    0x4551e8: mov      rdx, rax
    0x4551eb: sub      rdx, rcx
    0x4551ee: mov      qword ptr [rsp + 8], rdx
    0x4551f3: cmp      rax, rcx
    0x4551f6: jb       0x455207

; --- Block 0x4551f8 [BODY] 3 insns, callees: (none)
    0x4551f8: mov      rax, qword ptr [rsp + 8]
    0x4551fd: mov      qword ptr [rsp + 0x140], rax
    0x455205: jmp      0x455214

; --- Block 0x455207 [BODY] 2 insns, callees: (none)
    0x455207: lea      rdi, [rip + 0x9bb32]
    0x45520e: call     qword ptr [rip + 0x9ff3c]

; --- Block 0x455214 [BODY] 11 insns, callees: (none)
    0x455214: mov      rax, qword ptr [rsp + 0x10]
    0x455219: mov      rcx, qword ptr [rsp + 0x140]
    0x455221: mov      qword ptr [rsp + 0x1c8], rax
    0x455229: mov      qword ptr [rsp + 0x1d0], rcx
    0x455231: add      rax, rcx
    0x455234: mov      rcx, qword ptr [rsp + 0x18]
    0x455239: mov      qword ptr [rsp + 0x1b8], rax
    0x455241: mov      qword ptr [rsp + 0x1c0], rcx
    0x455249: add      rax, rcx
    0x45524c: add      rsp, 0x1d8
    0x455253: ret      

; --- Block 0x455254 [BODY] 14 insns, callees: (none)
    0x455254: mov      rax, qword ptr [rsp + 0x130]
    0x45525c: mov      qword ptr [rsp + 0x138], rax
    0x455264: mov      rax, qword ptr [rsp + 0x10]
    0x455269: mov      rcx, qword ptr [rsp + 0x138]
    0x455271: mov      qword ptr [rsp + 0x1a8], rax
    0x455279: mov      qword ptr [rsp + 0x1b0], rcx
    0x455281: add      rax, rcx
    0x455284: mov      qword ptr [rsp + 0x10], rax
    0x455289: mov      rcx, qword ptr [rsp + 0x18]
    0x45528e: mov      rax, rcx
    0x455291: add      rax, 1
    0x455295: mov      qword ptr [rsp], rax
    ... +2 more instructions

; --- Block 0x45529e [BODY] 7 insns, callees: core::option::Option<T>::map_or
    0x45529e: mov      rax, qword ptr [rsp]
    0x4552a2: mov      qword ptr [rsp + 0x18], rax
    0x4552a7: mov      rdi, qword ptr [rsp + 0x20]
    0x4552ac: mov      rsi, qword ptr [rsp + 0x28]
    0x4552b1: mov      rdx, qword ptr [rsp + 0x138]
    0x4552b9: lea      rcx, [rsp + 0x138]
    0x4552c1: call     0x4606a0

; --- Block 0x4552c6 [BODY] 7 insns, callees: core::option::Option<T>::map_or
    0x4552c6: mov      qword ptr [rsp + 0x20], 1
    0x4552cf: mov      qword ptr [rsp + 0x28], rax
    0x4552d4: mov      rdi, qword ptr [rsp + 0x30]
    0x4552d9: mov      rsi, qword ptr [rsp + 0x38]
    0x4552de: mov      rdx, qword ptr [rsp + 0x138]
    0x4552e6: lea      rcx, [rsp + 0x138]
    0x4552ee: call     0x4607f0

; --- Block 0x4552f3 [BODY] 3 insns, callees: (none)
    0x4552f3: mov      qword ptr [rsp + 0x30], 1
    0x4552fc: mov      qword ptr [rsp + 0x38], rax
    0x455301: jmp      0x4550cc

; --- Block 0x455306 [BODY] 2 insns, callees: (none)
    0x455306: lea      rdi, [rip + 0x9ba4b]
    0x45530d: call     qword ptr [rip + 0x9fe1d]

```

**O2 blocks** (28 total):

```asm
; --- Block 0x42ad50 [BODY] 19 insns, callees: core::str::iter::SplitInternal<P>::next
    0x42ad50: push     rbp
    0x42ad51: push     r15
    0x42ad53: push     r14
    0x42ad55: push     r13
    0x42ad57: push     r12
    0x42ad59: push     rbx
    0x42ad5a: sub      rsp, 0x58
    0x42ad5e: mov      qword ptr [rsp + 0x10], 0
    0x42ad67: mov      qword ptr [rsp + 0x18], rsi
    0x42ad6c: mov      qword ptr [rsp + 0x20], rdi
    0x42ad71: mov      qword ptr [rsp + 0x28], rsi
    0x42ad76: mov      qword ptr [rsp + 0x30], 0
    ... +7 more instructions

; --- Block 0x42ada9 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42ada9: test     rax, rax
    0x42adac: je       0x42aef0

; --- Block 0x42adb2 [BODY] 6 insns, callees: (none)
    0x42adb2: mov      qword ptr [rsp + 8], 0
    0x42adbb: lea      r14, [rsp + 0x10]
    0x42adc0: mov      r15d, 0xa
    0x42adc6: xor      ebx, ebx
    0x42adc8: xor      ebp, ebp
    0x42adca: jmp      0x42ae11

; --- Block 0x42adcc [LOOP_HEADER] 14 insns, callees: core::str::iter::SplitInternal<P>::next
    0x42adcc: add      qword ptr [rsp + 8], rax
    0x42add1: inc      rbx
    0x42add4: cmp      rax, r12
    0x42add7: cmova    r12, rax
    0x42addb: test     bpl, 1
    0x42addf: cmove    r12, rax
    0x42ade3: cmp      rax, r13
    0x42ade6: cmovb    r13, rax
    0x42adea: test     bpl, 1
    0x42adee: cmove    r13, rax
    0x42adf2: mov      ebp, 1
    0x42adf7: nop      word ptr [rax + rax]
    ... +2 more instructions

; --- Block 0x42ae00 [LOOP_HEADER] 2 insns, callees: core::str::iter::SplitInternal<P>::next
    0x42ae00: mov      rdi, r14
    0x42ae03: call     0x433a30

; --- Block 0x42ae08 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42ae08: test     rax, rax
    0x42ae0b: je       0x42aed7

; --- Block 0x42ae11 [BODY] 3 insns, callees: core::str::<impl str>::trim_matches
    0x42ae11: mov      rdi, rax
    0x42ae14: mov      rsi, rdx
    0x42ae17: call     0x441280

; --- Block 0x42ae1c [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42ae1c: test     rdx, rdx
    0x42ae1f: je       0x42ae00

; --- Block 0x42ae21 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42ae21: mov      rcx, rax
    0x42ae24: cmp      rdx, 1
    0x42ae28: jne      0x42ae40

; --- Block 0x42ae2a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42ae2a: movzx    eax, byte ptr [rcx]
    0x42ae2d: cmp      eax, 0x2b
    0x42ae30: je       0x42ae00

; --- Block 0x42ae32 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42ae32: mov      esi, 1
    0x42ae37: cmp      eax, 0x2d
    0x42ae3a: je       0x42ae00

; --- Block 0x42ae3c [BODY] 1 insns, callees: (none)
    0x42ae3c: jmp      0x42aea9

; --- Block 0x42ae40 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42ae40: cmp      byte ptr [rcx], 0x2b
    0x42ae43: jne      0x42aea0

; --- Block 0x42ae45 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42ae45: inc      rcx
    0x42ae48: lea      rsi, [rdx - 1]
    0x42ae4c: cmp      rdx, 0x12
    0x42ae50: jb       0x42aea9

; --- Block 0x42ae52 [LOOP_HEADER] 5 insns, callees: (none)
    0x42ae52: xor      edi, edi
    0x42ae54: xor      eax, eax
    0x42ae56: nop      word ptr cs:[rax + rax]
    0x42ae60: cmp      rsi, rdi
    0x42ae63: je       0x42adcc

; --- Block 0x42ae60 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42ae60: cmp      rsi, rdi
    0x42ae63: je       0x42adcc

; --- Block 0x42ae69 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42ae69: movzx    r8d, byte ptr [rcx + rdi]
    0x42ae6e: add      r8d, -0x30
    0x42ae72: cmp      r8d, 9
    0x42ae76: ja       0x42ae00

; --- Block 0x42ae78 [BODY] 8 insns, callees: (none)
    0x42ae78: mul      r15
    0x42ae7b: mov      rdx, rax
    0x42ae7e: mov      eax, r8d
    0x42ae81: seto     r8b
    0x42ae85: add      rax, rdx
    0x42ae88: setb     dl
    0x42ae8b: test     r8b, r8b
    0x42ae8e: jne      0x42ae00

; --- Block 0x42ae94 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42ae94: inc      rdi
    0x42ae97: test     dl, dl
    0x42ae99: je       0x42ae60

; --- Block 0x42ae9b [BODY] 1 insns, callees: (none)
    0x42ae9b: jmp      0x42ae00

; --- Block 0x42aea0 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42aea0: mov      rsi, rdx
    0x42aea3: cmp      rdx, 0x11
    0x42aea7: jae      0x42ae52

; --- Block 0x42aea9 [BODY] 7 insns, callees: (none)
    0x42aea9: xor      edx, edx
    0x42aeab: xor      eax, eax
    0x42aead: nop      dword ptr [rax]
    0x42aeb0: movzx    edi, byte ptr [rcx + rdx]
    0x42aeb4: add      edi, -0x30
    0x42aeb7: cmp      edi, 9
    0x42aeba: ja       0x42ae00

; --- Block 0x42aeb0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42aeb0: movzx    edi, byte ptr [rcx + rdx]
    0x42aeb4: add      edi, -0x30
    0x42aeb7: cmp      edi, 9
    0x42aeba: ja       0x42ae00

; --- Block 0x42aec0 [ITERATOR_STATE] 6 insns, callees: (none)
    0x42aec0: lea      rax, [rax + rax*4]
    0x42aec4: mov      edi, edi
    0x42aec6: lea      rax, [rdi + rax*2]
    0x42aeca: inc      rdx
    0x42aecd: cmp      rsi, rdx
    0x42aed0: jne      0x42aeb0

; --- Block 0x42aed2 [BODY] 1 insns, callees: (none)
    0x42aed2: jmp      0x42adcc

; --- Block 0x42aed7 [BODY] 8 insns, callees: (none)
    0x42aed7: and      ebp, ebp
    0x42aed9: sub      r12, r13
    0x42aedc: xor      eax, eax
    0x42aede: test     bpl, 1
    0x42aee2: cmovne   rax, r12
    0x42aee6: add      rbx, qword ptr [rsp + 8]
    0x42aeeb: add      rbx, rax
    0x42aeee: jmp      0x42aef2

; --- Block 0x42aef0 [BODY] 10 insns, callees: (none)
    0x42aef0: xor      ebx, ebx
    0x42aef2: mov      rax, rbx
    0x42aef5: add      rsp, 0x58
    0x42aef9: pop      rbx
    0x42aefa: pop      r12
    0x42aefc: pop      r13
    0x42aefe: pop      r14
    0x42af00: pop      r15
    0x42af02: pop      rbp
    0x42af03: ret      

; --- Block 0x42aef2 [BODY] 9 insns, callees: (none)
    0x42aef2: mov      rax, rbx
    0x42aef5: add      rsp, 0x58
    0x42aef9: pop      rbx
    0x42aefa: pop      r12
    0x42aefc: pop      r13
    0x42aefe: pop      r14
    0x42af00: pop      r15
    0x42af02: pop      rbp
    0x42af03: ret      

```

**Hungarian matching result** (mean similarity: 0.676):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x455165` | BODY | `0x42ae3c` | BODY | 1.000 | GOOD |
| `0x4551ac` | BOUNDS_CHECK | `0x42ada9` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x45514d` | BODY | `0x42ae52` | LOOP_HEADER | 0.780 | GOOD |
| `0x455108` | BODY | `0x42ae00` | LOOP_HEADER | 0.773 | GOOD |
| `0x455254` | BODY | `0x42adcc` | LOOP_HEADER | 0.743 | GOOD |
| `0x4551c8` | BODY | `0x42ae78` | BODY | 0.704 | GOOD |
| `0x45516a` | BODY | `0x42ae21` | BOUNDS_CHECK | 0.703 | GOOD |
| `0x45512d` | BODY | `0x42ae11` | BODY | 0.693 | PARTIAL |
| `0x4551ba` | BODY | `0x42aed2` | BODY | 0.662 | PARTIAL |
| `0x45529e` | BODY | `0x42aec0` | ITERATOR_STATE | 0.655 | PARTIAL |
| `0x455207` | BODY | `0x42ae08` | BOUNDS_CHECK | 0.651 | PARTIAL |
| `0x4550d9` | BODY | `0x42aed7` | BODY | 0.648 | PARTIAL |
| `0x4550cc` | LOOP_HEADER | `0x42ae1c` | BOUNDS_CHECK | 0.647 | PARTIAL |
| `0x455306` | BODY | `0x42ae60` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x4550a3` | BODY | `0x42ae94` | BOUNDS_CHECK | 0.607 | PARTIAL |
| `0x4552f3` | BODY | `0x42ae9b` | BODY | 0.604 | PARTIAL |
| `0x455214` | BODY | `0x42aef2` | BODY | 0.583 | PARTIAL |
| `0x455050` | BODY | `0x42ad50` | BODY | 0.557 | PARTIAL |
| `0x4551f8` | BODY | `0x42ae2a` | BOUNDS_CHECK | 0.550 | PARTIAL |
| `0x4550b5` | BODY | `0x42aeb0` | BOUNDS_CHECK | 0.503 | PARTIAL |
| `0x4552c6` | BODY | `0x42adb2` | BODY | 0.502 | PARTIAL |
| — | — | `0x42ae32` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42ae40` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42ae45` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42ae69` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42aea0` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42aea9` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42aef0` | BODY | 0.000 | UNMATCHED (O2 only) |

### C `opt_20` — O0: 37 blocks, O2: 47 blocks

**O0 blocks** (37 total):

```asm
; --- Block 0x407159 [BODY] 13 insns, callees: (none)
    0x407159: push     rbp
    0x40715a: mov      rbp, rsp
    0x40715d: sub      rsp, 0xb0
    0x407164: mov      qword ptr [rbp - 0xa8], rdi
    0x40716b: mov      qword ptr [rbp - 8], 0
    0x407173: mov      qword ptr [rbp - 0x10], 0
    0x40717b: mov      qword ptr [rbp - 0x18], 0
    0x407183: mov      qword ptr [rbp - 0x20], 0
    0x40718b: mov      dword ptr [rbp - 0x24], 0
    0x407192: mov      dword ptr [rbp - 0x28], 0
    0x407199: mov      rax, qword ptr [rbp - 0xa8]
    0x4071a0: mov      qword ptr [rbp - 0x30], rax
    ... +1 more instructions

; --- Block 0x4071a9 [LOOP_HEADER] 5 insns, callees: (none)
    0x4071a9: add      qword ptr [rbp - 0x30], 1
    0x4071ae: mov      rax, qword ptr [rbp - 0x30]
    0x4071b2: movzx    eax, byte ptr [rax]
    0x4071b5: cmp      al, 0x2c
    0x4071b7: je       0x4071a9

; --- Block 0x4071ae [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4071ae: mov      rax, qword ptr [rbp - 0x30]
    0x4071b2: movzx    eax, byte ptr [rax]
    0x4071b5: cmp      al, 0x2c
    0x4071b7: je       0x4071a9

; --- Block 0x4071b9 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4071b9: mov      rax, qword ptr [rbp - 0x30]
    0x4071bd: movzx    eax, byte ptr [rax]
    0x4071c0: test     al, al
    0x4071c2: je       0x407309

; --- Block 0x4071c8 [BODY] 3 insns, callees: (none)
    0x4071c8: mov      rax, qword ptr [rbp - 0x30]
    0x4071cc: mov      qword ptr [rbp - 0x38], rax
    0x4071d0: jmp      0x4071d7

; --- Block 0x4071d2 [LOOP_HEADER] 5 insns, callees: (none)
    0x4071d2: add      qword ptr [rbp - 0x30], 1
    0x4071d7: mov      rax, qword ptr [rbp - 0x30]
    0x4071db: movzx    eax, byte ptr [rax]
    0x4071de: test     al, al
    0x4071e0: je       0x4071f4

; --- Block 0x4071d7 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4071d7: mov      rax, qword ptr [rbp - 0x30]
    0x4071db: movzx    eax, byte ptr [rax]
    0x4071de: test     al, al
    0x4071e0: je       0x4071f4

; --- Block 0x4071e2 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4071e2: mov      rax, qword ptr [rbp - 0x30]
    0x4071e6: movzx    eax, byte ptr [rax]
    0x4071e9: cmp      al, 0x2c
    0x4071eb: jne      0x4071d2

; --- Block 0x4071ed [BODY] 1 insns, callees: (none)
    0x4071ed: jmp      0x4071f4

; --- Block 0x4071ef [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4071ef: add      qword ptr [rbp - 0x38], 1
    0x4071f4: mov      rax, qword ptr [rbp - 0x38]
    0x4071f8: cmp      rax, qword ptr [rbp - 0x30]
    0x4071fc: jae      0x407209

; --- Block 0x4071f4 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4071f4: mov      rax, qword ptr [rbp - 0x38]
    0x4071f8: cmp      rax, qword ptr [rbp - 0x30]
    0x4071fc: jae      0x407209

; --- Block 0x4071fe [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4071fe: mov      rax, qword ptr [rbp - 0x38]
    0x407202: movzx    eax, byte ptr [rax]
    0x407205: cmp      al, 0x20
    0x407207: je       0x4071ef

; --- Block 0x407209 [BODY] 3 insns, callees: (none)
    0x407209: mov      rax, qword ptr [rbp - 0x30]
    0x40720d: mov      qword ptr [rbp - 0x40], rax
    0x407211: jmp      0x407218

; --- Block 0x407213 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x407213: sub      qword ptr [rbp - 0x40], 1
    0x407218: mov      rax, qword ptr [rbp - 0x40]
    0x40721c: cmp      rax, qword ptr [rbp - 0x38]
    0x407220: jbe      0x407231

; --- Block 0x407218 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407218: mov      rax, qword ptr [rbp - 0x40]
    0x40721c: cmp      rax, qword ptr [rbp - 0x38]
    0x407220: jbe      0x407231

; --- Block 0x407222 [ITERATOR_STATE] 5 insns, callees: (none)
    0x407222: mov      rax, qword ptr [rbp - 0x40]
    0x407226: sub      rax, 1
    0x40722a: movzx    eax, byte ptr [rax]
    0x40722d: cmp      al, 0x20
    0x40722f: je       0x407213

; --- Block 0x407231 [ITERATOR_STATE] 5 insns, callees: (none)
    0x407231: mov      rax, qword ptr [rbp - 0x40]
    0x407235: sub      rax, qword ptr [rbp - 0x38]
    0x407239: mov      qword ptr [rbp - 0x48], rax
    0x40723d: cmp      qword ptr [rbp - 0x48], 0
    0x407242: jne      0x407249

; --- Block 0x407244 [BODY] 1 insns, callees: (none)
    0x407244: jmp      0x4072f8

; --- Block 0x407249 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407249: cmp      qword ptr [rbp - 0x48], 0x3f
    0x40724e: jbe      0x407258

; --- Block 0x407250 [BODY] 7 insns, callees: sub_4010e0
    0x407250: mov      qword ptr [rbp - 0x48], 0x3f
    0x407258: mov      rdx, qword ptr [rbp - 0x48]
    0x40725c: mov      rcx, qword ptr [rbp - 0x38]
    0x407260: lea      rax, [rbp - 0xa0]
    0x407267: mov      rsi, rcx
    0x40726a: mov      rdi, rax
    0x40726d: call     0x4010e0

; --- Block 0x407258 [BODY] 6 insns, callees: sub_4010e0
    0x407258: mov      rdx, qword ptr [rbp - 0x48]
    0x40725c: mov      rcx, qword ptr [rbp - 0x38]
    0x407260: lea      rax, [rbp - 0xa0]
    0x407267: mov      rsi, rcx
    0x40726a: mov      rdi, rax
    0x40726d: call     0x4010e0

; --- Block 0x407272 [BODY] 10 insns, callees: sub_4010a0
    0x407272: lea      rdx, [rbp - 0xa0]
    0x407279: mov      rax, qword ptr [rbp - 0x48]
    0x40727d: add      rax, rdx
    0x407280: mov      byte ptr [rax], 0
    0x407283: lea      rcx, [rbp - 0x60]
    0x407287: lea      rax, [rbp - 0xa0]
    0x40728e: mov      edx, 0xa
    0x407293: mov      rsi, rcx
    0x407296: mov      rdi, rax
    0x407299: call     0x4010a0

; --- Block 0x40729e [BODY] 5 insns, callees: (none)
    0x40729e: mov      qword ptr [rbp - 0x50], rax
    0x4072a2: mov      rax, qword ptr [rbp - 0x60]
    0x4072a6: movzx    eax, byte ptr [rax]
    0x4072a9: test     al, al
    0x4072ab: jne      0x4072f8

; --- Block 0x4072ad [ITERATOR_STATE] 5 insns, callees: (none)
    0x4072ad: mov      rax, qword ptr [rbp - 0x50]
    0x4072b1: add      qword ptr [rbp - 8], rax
    0x4072b5: add      qword ptr [rbp - 0x10], 1
    0x4072ba: cmp      dword ptr [rbp - 0x24], 0
    0x4072be: je       0x4072ca

; --- Block 0x4072c0 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4072c0: mov      rax, qword ptr [rbp - 0x50]
    0x4072c4: cmp      rax, qword ptr [rbp - 0x18]
    0x4072c8: jbe      0x4072d9

; --- Block 0x4072ca [BODY] 5 insns, callees: (none)
    0x4072ca: mov      rax, qword ptr [rbp - 0x50]
    0x4072ce: mov      qword ptr [rbp - 0x18], rax
    0x4072d2: mov      dword ptr [rbp - 0x24], 1
    0x4072d9: cmp      dword ptr [rbp - 0x28], 0
    0x4072dd: je       0x4072e9

; --- Block 0x4072d9 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4072d9: cmp      dword ptr [rbp - 0x28], 0
    0x4072dd: je       0x4072e9

; --- Block 0x4072df [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4072df: mov      rax, qword ptr [rbp - 0x50]
    0x4072e3: cmp      rax, qword ptr [rbp - 0x20]
    0x4072e7: jae      0x4072f8

; --- Block 0x4072e9 [BODY] 7 insns, callees: (none)
    0x4072e9: mov      rax, qword ptr [rbp - 0x50]
    0x4072ed: mov      qword ptr [rbp - 0x20], rax
    0x4072f1: mov      dword ptr [rbp - 0x28], 1
    0x4072f8: mov      rax, qword ptr [rbp - 0x30]
    0x4072fc: movzx    eax, byte ptr [rax]
    0x4072ff: test     al, al
    0x407301: jne      0x4071ae

; --- Block 0x4072f8 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4072f8: mov      rax, qword ptr [rbp - 0x30]
    0x4072fc: movzx    eax, byte ptr [rax]
    0x4072ff: test     al, al
    0x407301: jne      0x4071ae

; --- Block 0x407307 [BODY] 1 insns, callees: (none)
    0x407307: jmp      0x40730a

; --- Block 0x407309 [PROLOGUE] 1 insns, callees: (none)
    0x407309: nop      

; --- Block 0x40730a [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40730a: cmp      dword ptr [rbp - 0x24], 0
    0x40730e: je       0x407320

; --- Block 0x407310 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407310: cmp      dword ptr [rbp - 0x28], 0
    0x407314: je       0x407320

; --- Block 0x407316 [BODY] 3 insns, callees: (none)
    0x407316: mov      rax, qword ptr [rbp - 0x18]
    0x40731a: sub      rax, qword ptr [rbp - 0x20]
    0x40731e: jmp      0x407325

; --- Block 0x407320 [BODY] 9 insns, callees: (none)
    0x407320: mov      eax, 0
    0x407325: mov      qword ptr [rbp - 0x58], rax
    0x407329: mov      rdx, qword ptr [rbp - 8]
    0x40732d: mov      rax, qword ptr [rbp - 0x58]
    0x407331: add      rdx, rax
    0x407334: mov      rax, qword ptr [rbp - 0x10]
    0x407338: add      rax, rdx
    0x40733b: leave    
    0x40733c: ret      

; --- Block 0x407325 [BODY] 8 insns, callees: (none)
    0x407325: mov      qword ptr [rbp - 0x58], rax
    0x407329: mov      rdx, qword ptr [rbp - 8]
    0x40732d: mov      rax, qword ptr [rbp - 0x58]
    0x407331: add      rdx, rax
    0x407334: mov      rax, qword ptr [rbp - 0x10]
    0x407338: add      rax, rdx
    0x40733b: leave    
    0x40733c: ret      

```

**O2 blocks** (47 total):

```asm
; --- Block 0x407350 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407350: movzx    edx, byte ptr [rdi]
    0x407353: test     dl, dl
    0x407355: je       0x407548

; --- Block 0x40735b [BODY] 16 insns, callees: (none)
    0x40735b: push     r15
    0x40735d: mov      rax, rdi
    0x407360: push     r14
    0x407362: xor      r14d, r14d
    0x407365: push     r13
    0x407367: xor      r13d, r13d
    0x40736a: push     r12
    0x40736c: xor      r12d, r12d
    0x40736f: push     rbp
    0x407370: xor      ebp, ebp
    0x407372: push     rbx
    0x407373: xor      ebx, ebx
    ... +4 more instructions

; --- Block 0x407380 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407380: cmp      dl, 0x2c
    0x407383: jne      0x40739d

; --- Block 0x407385 [PROLOGUE] 1 insns, callees: (none)
    0x407385: nop      dword ptr [rax]

; --- Block 0x407388 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x407388: movzx    edx, byte ptr [rax + 1]
    0x40738c: add      rax, 1
    0x407390: cmp      dl, 0x2c
    0x407393: je       0x407388

; --- Block 0x407395 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407395: test     dl, dl
    0x407397: je       0x4074ce

; --- Block 0x40739d [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40739d: movzx    esi, byte ptr [rax]
    0x4073a0: test     sil, sil
    0x4073a3: je       0x4074c3

; --- Block 0x4073a9 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4073a9: cmp      sil, 0x2c
    0x4073ad: je       0x4074c3

; --- Block 0x4073b3 [BODY] 7 insns, callees: (none)
    0x4073b3: mov      r15, rax
    0x4073b6: nop      word ptr cs:[rax + rax]
    0x4073c0: mov      rdx, r15
    0x4073c3: movzx    ecx, byte ptr [r15 + 1]
    0x4073c8: add      r15, 1
    0x4073cc: test     cl, cl
    0x4073ce: je       0x4073d5

; --- Block 0x4073c0 [LOOP_HEADER] 5 insns, callees: (none)
    0x4073c0: mov      rdx, r15
    0x4073c3: movzx    ecx, byte ptr [r15 + 1]
    0x4073c8: add      r15, 1
    0x4073cc: test     cl, cl
    0x4073ce: je       0x4073d5

; --- Block 0x4073d0 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4073d0: cmp      cl, 0x2c
    0x4073d3: jne      0x4073c0

; --- Block 0x4073d5 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4073d5: cmp      r15, rax
    0x4073d8: ja       0x4073f4

; --- Block 0x4073da [BODY] 1 insns, callees: (none)
    0x4073da: jmp      0x40754b

; --- Block 0x4073e0 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4073e0: lea      rcx, [rax + 1]
    0x4073e4: cmp      rcx, r15
    0x4073e7: je       0x4074f0

; --- Block 0x4073ed [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4073ed: movzx    esi, byte ptr [rax + 1]
    0x4073f1: mov      rax, rcx
    0x4073f4: cmp      sil, 0x20
    0x4073f8: je       0x4073e0

; --- Block 0x4073f4 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4073f4: cmp      sil, 0x20
    0x4073f8: je       0x4073e0

; --- Block 0x4073fa [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4073fa: mov      rdx, r15
    0x4073fd: cmp      r15, rax
    0x407400: ja       0x407415

; --- Block 0x407402 [BODY] 1 insns, callees: (none)
    0x407402: jmp      0x40741b

; --- Block 0x407408 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407408: sub      rdx, 1
    0x40740c: cmp      rdx, rax
    0x40740f: je       0x4074c0

; --- Block 0x407415 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407415: cmp      byte ptr [rdx - 1], 0x20
    0x407419: je       0x407408

; --- Block 0x40741b [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40741b: sub      rdx, rax
    0x40741e: test     rdx, rdx
    0x407421: je       0x4074c0

; --- Block 0x40741e [BOUNDS_CHECK] 2 insns, callees: (none)
    0x40741e: test     rdx, rdx
    0x407421: je       0x4074c0

; --- Block 0x407427 [BODY] 7 insns, callees: (none)
    0x407427: mov      ecx, 0x3f
    0x40742c: lea      rsi, [rsp + 0x10]
    0x407431: cmp      rdx, rcx
    0x407434: cmova    rdx, rcx
    0x407438: mov      rcx, rax
    0x40743b: cmp      edx, 8
    0x40743e: jae      0x407500

; --- Block 0x407444 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x407444: xor      eax, eax
    0x407446: test     dl, 4
    0x407449: je       0x407454

; --- Block 0x40744b [BODY] 5 insns, callees: (none)
    0x40744b: mov      eax, dword ptr [rcx]
    0x40744d: mov      dword ptr [rsi], eax
    0x40744f: mov      eax, 4
    0x407454: test     dl, 2
    0x407457: je       0x407465

; --- Block 0x407454 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407454: test     dl, 2
    0x407457: je       0x407465

; --- Block 0x407459 [ITERATOR_STATE] 5 insns, callees: (none)
    0x407459: movzx    edi, word ptr [rcx + rax]
    0x40745d: mov      word ptr [rsi + rax], di
    0x407461: add      rax, 2
    0x407465: test     dl, 1
    0x407468: je       0x407471

; --- Block 0x407465 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x407465: test     dl, 1
    0x407468: je       0x407471

; --- Block 0x40746a [BODY] 7 insns, callees: sub_4010b0
    0x40746a: movzx    ecx, byte ptr [rcx + rax]
    0x40746e: mov      byte ptr [rsi + rax], cl
    0x407471: mov      byte ptr [rsp + rdx + 0x10], 0
    0x407476: lea      rsi, [rsp + 8]
    0x40747b: mov      edx, 0xa
    0x407480: lea      rdi, [rsp + 0x10]
    0x407485: call     0x4010b0

; --- Block 0x407471 [BODY] 5 insns, callees: sub_4010b0
    0x407471: mov      byte ptr [rsp + rdx + 0x10], 0
    0x407476: lea      rsi, [rsp + 8]
    0x40747b: mov      edx, 0xa
    0x407480: lea      rdi, [rsp + 0x10]
    0x407485: call     0x4010b0

; --- Block 0x40748a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40748a: mov      rdx, qword ptr [rsp + 8]
    0x40748f: cmp      byte ptr [rdx], 0
    0x407492: jne      0x4074c0

; --- Block 0x407494 [ITERATOR_STATE] 6 insns, callees: (none)
    0x407494: mov      edx, ebp
    0x407496: add      r12, rax
    0x407499: add      rbx, 1
    0x40749d: xor      edx, 1
    0x4074a0: cmp      rax, r13
    0x4074a3: ja       0x407540

; --- Block 0x4074a9 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4074a9: test     dl, dl
    0x4074ab: jne      0x407540

; --- Block 0x4074b1 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4074b1: cmp      rax, r14
    0x4074b4: jb       0x407530

; --- Block 0x4074b6 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4074b6: mov      ebp, 1
    0x4074bb: test     dl, dl
    0x4074bd: jne      0x407530

; --- Block 0x4074bf [PROLOGUE] 1 insns, callees: (none)
    0x4074bf: nop      

; --- Block 0x4074c0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4074c0: mov      rax, r15
    0x4074c3: movzx    edx, byte ptr [rax]
    0x4074c6: test     dl, dl
    0x4074c8: jne      0x407380

; --- Block 0x4074c3 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4074c3: movzx    edx, byte ptr [rax]
    0x4074c6: test     dl, dl
    0x4074c8: jne      0x407380

; --- Block 0x4074ce [BODY] 14 insns, callees: (none)
    0x4074ce: lea      rax, [rbx + r12]
    0x4074d2: mov      rdx, rax
    0x4074d5: sub      rdx, r14
    0x4074d8: add      rdx, r13
    0x4074db: test     ebp, ebp
    0x4074dd: cmovne   rax, rdx
    0x4074e1: add      rsp, 0x58
    0x4074e5: pop      rbx
    0x4074e6: pop      rbp
    0x4074e7: pop      r12
    0x4074e9: pop      r13
    0x4074eb: pop      r14
    ... +2 more instructions

; --- Block 0x4074f0 [BODY] 3 insns, callees: (none)
    0x4074f0: sub      rdx, rax
    0x4074f3: mov      rax, r15
    0x4074f6: jmp      0x40741e

; --- Block 0x407500 [BODY] 9 insns, callees: (none)
    0x407500: mov      r8d, edx
    0x407503: xor      ecx, ecx
    0x407505: and      r8d, 0xfffffff8
    0x407509: mov      esi, ecx
    0x40750b: add      ecx, 8
    0x40750e: mov      rdi, qword ptr [rax + rsi]
    0x407512: mov      qword ptr [rsp + rsi + 0x10], rdi
    0x407517: cmp      ecx, r8d
    0x40751a: jb       0x407509

; --- Block 0x407509 [ITERATOR_STATE] 6 insns, callees: (none)
    0x407509: mov      esi, ecx
    0x40750b: add      ecx, 8
    0x40750e: mov      rdi, qword ptr [rax + rsi]
    0x407512: mov      qword ptr [rsp + rsi + 0x10], rdi
    0x407517: cmp      ecx, r8d
    0x40751a: jb       0x407509

; --- Block 0x40751c [BODY] 4 insns, callees: (none)
    0x40751c: lea      rdi, [rsp + 0x10]
    0x407521: lea      rsi, [rdi + rcx]
    0x407525: add      rcx, rax
    0x407528: jmp      0x407444

; --- Block 0x407530 [BODY] 3 insns, callees: (none)
    0x407530: mov      r14, rax
    0x407533: mov      ebp, 1
    0x407538: jmp      0x4074c0

; --- Block 0x407540 [BODY] 2 insns, callees: (none)
    0x407540: mov      r13, rax
    0x407543: jmp      0x4074b1

; --- Block 0x407548 [BODY] 2 insns, callees: (none)
    0x407548: xor      eax, eax
    0x40754a: ret      

; --- Block 0x40754b [BODY] 3 insns, callees: (none)
    0x40754b: mov      rdx, r15
    0x40754e: sub      rdx, rax
    0x407551: jmp      0x40741e

```

**Hungarian matching result** (mean similarity: 0.835):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4071ed` | BODY | `0x4073da` | BODY | 1.000 | GOOD |
| `0x4072d9` | BOUNDS_CHECK | `0x4073d5` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x407307` | BODY | `0x407402` | BODY | 1.000 | GOOD |
| `0x407309` | PROLOGUE | `0x4074bf` | PROLOGUE | 1.000 | GOOD |
| `0x40730a` | BOUNDS_CHECK | `0x40741e` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x407310` | BOUNDS_CHECK | `0x407465` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x407244` | BODY | `0x407385` | PROLOGUE | 0.997 | GOOD |
| `0x4071fe` | BOUNDS_CHECK | `0x4073ed` | BOUNDS_CHECK | 0.982 | GOOD |
| `0x4071b9` | BOUNDS_CHECK | `0x4074c0` | BOUNDS_CHECK | 0.980 | GOOD |
| `0x4072df` | BOUNDS_CHECK | `0x4074b6` | BOUNDS_CHECK | 0.977 | GOOD |
| `0x407218` | BOUNDS_CHECK | `0x40739d` | BOUNDS_CHECK | 0.971 | GOOD |
| `0x4071f4` | BOUNDS_CHECK | `0x407350` | BOUNDS_CHECK | 0.970 | GOOD |
| `0x4072c0` | BOUNDS_CHECK | `0x4074c3` | BOUNDS_CHECK | 0.970 | GOOD |
| `0x4071c8` | BODY | `0x407530` | BODY | 0.953 | GOOD |
| `0x407316` | BODY | `0x40754b` | BODY | 0.952 | GOOD |
| `0x4072ad` | ITERATOR_STATE | `0x4073c0` | LOOP_HEADER | 0.928 | GOOD |
| `0x4071a9` | LOOP_HEADER | `0x407388` | BOUNDS_CHECK | 0.918 | GOOD |
| `0x4071d7` | BOUNDS_CHECK | `0x40748a` | BOUNDS_CHECK | 0.884 | GOOD |
| `0x4072f8` | BOUNDS_CHECK | `0x4073fa` | BOUNDS_CHECK | 0.877 | GOOD |
| `0x407209` | BODY | `0x4074f0` | BODY | 0.850 | GOOD |
| `0x4072e9` | BODY | `0x4073b3` | BODY | 0.838 | GOOD |
| `0x407213` | BOUNDS_CHECK | `0x407408` | BOUNDS_CHECK | 0.804 | GOOD |
| `0x4071ae` | BOUNDS_CHECK | `0x407380` | BOUNDS_CHECK | 0.770 | GOOD |
| `0x4071e2` | BOUNDS_CHECK | `0x4073a9` | BOUNDS_CHECK | 0.770 | GOOD |
| `0x407249` | BOUNDS_CHECK | `0x407395` | BOUNDS_CHECK | 0.748 | GOOD |
| `0x4072ca` | BODY | `0x40744b` | BODY | 0.735 | GOOD |
| `0x407231` | ITERATOR_STATE | `0x40741b` | BOUNDS_CHECK | 0.730 | GOOD |
| `0x4071d2` | LOOP_HEADER | `0x407459` | ITERATOR_STATE | 0.724 | GOOD |
| `0x407222` | ITERATOR_STATE | `0x4073f4` | BOUNDS_CHECK | 0.701 | GOOD |
| `0x4071ef` | BOUNDS_CHECK | `0x4073e0` | BOUNDS_CHECK | 0.685 | PARTIAL |
| `0x40729e` | BODY | `0x4074a9` | BOUNDS_CHECK | 0.660 | PARTIAL |
| `0x407272` | BODY | `0x40746a` | BODY | 0.645 | PARTIAL |
| `0x407258` | BODY | `0x407471` | BODY | 0.642 | PARTIAL |
| `0x407325` | BODY | `0x407494` | ITERATOR_STATE | 0.624 | PARTIAL |
| `0x407250` | BODY | `0x407427` | BODY | 0.591 | PARTIAL |
| `0x407159` | BODY | `0x40735b` | BODY | 0.515 | PARTIAL |
| `0x407320` | BODY | `0x407500` | BODY | 0.501 | PARTIAL |
| — | — | `0x4073d0` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x407415` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x407444` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x407454` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4074b1` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x4074ce` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x407509` | ITERATOR_STATE | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x40751c` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x407540` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x407548` | BODY | 0.000 | UNMATCHED (O2 only) |

---

## Function `own_01`

### Rust `own_01` — O0: 52 blocks, O2: 42 blocks

**O0 blocks** (52 total):

```asm
; --- Block 0x455320 [BODY] 8 insns, callees: rust_bench::OwnedMatrix::new
    0x455320: sub      rsp, 0x218
    0x455327: mov      rdx, rdi
    0x45532a: mov      qword ptr [rsp + 0xe8], rdx
    0x455332: mov      qword ptr [rsp + 0x1b0], rdx
    0x45533a: mov      qword ptr [rsp + 0x1b8], rdx
    0x455342: lea      rdi, [rsp + 0x100]
    0x45534a: mov      rsi, rdx
    0x45534d: call     0x43fde0

; --- Block 0x455352 [BODY] 4 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x455352: mov      rsi, qword ptr [rsp + 0xe8]
    0x45535a: xor      eax, eax
    0x45535c: mov      edi, eax
    0x45535e: call     0x49b480

; --- Block 0x455363 [BODY] 3 insns, callees: (none)
    0x455363: mov      qword ptr [rsp + 0xf0], rdx
    0x45536b: mov      qword ptr [rsp + 0xf8], rax
    0x455373: jmp      0x45539d

; --- Block 0x45539d [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x45539d: mov      rax, qword ptr [rsp + 0xf0]
    0x4553a5: mov      rcx, qword ptr [rsp + 0xf8]
    0x4553ad: mov      qword ptr [rsp + 0x128], rcx
    0x4553b5: mov      qword ptr [rsp + 0x130], rax
    0x4553bd: lea      rdi, [rsp + 0x128]
    0x4553c5: call     0x49ad10

; --- Block 0x4553bd [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4553bd: lea      rdi, [rsp + 0x128]
    0x4553c5: call     0x49ad10

; --- Block 0x4553ca [BODY] 3 insns, callees: (none)
    0x4553ca: mov      qword ptr [rsp + 0xd8], rdx
    0x4553d2: mov      qword ptr [rsp + 0xe0], rax
    0x4553da: jmp      0x4553dc

; --- Block 0x4553dc [BODY] 6 insns, callees: (none)
    0x4553dc: mov      rax, qword ptr [rsp + 0xd8]
    0x4553e4: mov      rcx, qword ptr [rsp + 0xe0]
    0x4553ec: mov      qword ptr [rsp + 0x138], rcx
    0x4553f4: mov      qword ptr [rsp + 0x140], rax
    0x4553fc: test     qword ptr [rsp + 0x138], 1
    0x455408: je       0x45543f

; --- Block 0x45540a [BODY] 8 insns, callees: (none)
    0x45540a: mov      rcx, qword ptr [rsp + 0x140]
    0x455412: mov      qword ptr [rsp + 0xc8], rcx
    0x45541a: mov      qword ptr [rsp + 0x1e0], rcx
    0x455422: mov      rax, rcx
    0x455425: add      rax, 1
    0x455429: mov      qword ptr [rsp + 0xd0], rax
    0x455431: cmp      rax, rcx
    0x455434: jb       0x45563e

; --- Block 0x45543a [BODY] 1 insns, callees: (none)
    0x45543a: jmp      0x45561b

; --- Block 0x45543f [BODY] 5 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x45543f: mov      rsi, qword ptr [rsp + 0xe8]
    0x455447: mov      qword ptr [rsp + 0x168], 0
    0x455453: xor      eax, eax
    0x455455: mov      edi, eax
    0x455457: call     0x49b480

; --- Block 0x45545c [BODY] 3 insns, callees: (none)
    0x45545c: mov      qword ptr [rsp + 0xb8], rdx
    0x455464: mov      qword ptr [rsp + 0xc0], rax
    0x45546c: jmp      0x45546e

; --- Block 0x45546e [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x45546e: mov      rax, qword ptr [rsp + 0xb8]
    0x455476: mov      rcx, qword ptr [rsp + 0xc0]
    0x45547e: mov      qword ptr [rsp + 0x170], rcx
    0x455486: mov      qword ptr [rsp + 0x178], rax
    0x45548e: lea      rdi, [rsp + 0x170]
    0x455496: call     0x49ad10

; --- Block 0x45548e [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x45548e: lea      rdi, [rsp + 0x170]
    0x455496: call     0x49ad10

; --- Block 0x45549b [BODY] 3 insns, callees: (none)
    0x45549b: mov      qword ptr [rsp + 0xa8], rdx
    0x4554a3: mov      qword ptr [rsp + 0xb0], rax
    0x4554ab: jmp      0x4554ad

; --- Block 0x4554ad [BODY] 6 insns, callees: (none)
    0x4554ad: mov      rax, qword ptr [rsp + 0xa8]
    0x4554b5: mov      rcx, qword ptr [rsp + 0xb0]
    0x4554bd: mov      qword ptr [rsp + 0x180], rcx
    0x4554c5: mov      qword ptr [rsp + 0x188], rax
    0x4554cd: test     qword ptr [rsp + 0x180], 1
    0x4554d9: je       0x455516

; --- Block 0x4554db [BODY] 7 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x4554db: mov      rsi, qword ptr [rsp + 0xe8]
    0x4554e3: mov      rax, qword ptr [rsp + 0x188]
    0x4554eb: mov      qword ptr [rsp + 0x90], rax
    0x4554f3: mov      qword ptr [rsp + 0x1d0], rax
    0x4554fb: xor      eax, eax
    0x4554fd: mov      edi, eax
    0x4554ff: call     0x49b480

; --- Block 0x455504 [BODY] 3 insns, callees: (none)
    0x455504: mov      qword ptr [rsp + 0x98], rdx
    0x45550c: mov      qword ptr [rsp + 0xa0], rax
    0x455514: jmp      0x455543

; --- Block 0x455516 [DROP_GLUE] 4 insns, callees: core::ptr::drop_in_place<rust_bench::OwnedMatrix>
    0x455516: mov      rax, qword ptr [rsp + 0x168]
    0x45551e: mov      qword ptr [rsp + 0x88], rax
    0x455526: lea      rdi, [rsp + 0x100]
    0x45552e: call     0x496550

; --- Block 0x455533 [EPILOGUE] 3 insns, callees: (none)
    0x455533: mov      rax, qword ptr [rsp + 0x88]
    0x45553b: add      rsp, 0x218
    0x455542: ret      

; --- Block 0x455543 [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x455543: mov      rax, qword ptr [rsp + 0x98]
    0x45554b: mov      rcx, qword ptr [rsp + 0xa0]
    0x455553: mov      qword ptr [rsp + 0x190], rcx
    0x45555b: mov      qword ptr [rsp + 0x198], rax
    0x455563: lea      rdi, [rsp + 0x190]
    0x45556b: call     0x49ad10

; --- Block 0x455563 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x455563: lea      rdi, [rsp + 0x190]
    0x45556b: call     0x49ad10

; --- Block 0x455570 [BODY] 3 insns, callees: (none)
    0x455570: mov      qword ptr [rsp + 0x78], rdx
    0x455575: mov      qword ptr [rsp + 0x80], rax
    0x45557d: jmp      0x45557f

; --- Block 0x45557f [BODY] 6 insns, callees: (none)
    0x45557f: mov      rax, qword ptr [rsp + 0x78]
    0x455584: mov      rcx, qword ptr [rsp + 0x80]
    0x45558c: mov      qword ptr [rsp + 0x1a0], rcx
    0x455594: mov      qword ptr [rsp + 0x1a8], rax
    0x45559c: test     qword ptr [rsp + 0x1a0], 1
    0x4555a8: je       0x45548e

; --- Block 0x4555ae [BODY] 7 insns, callees: rust_bench::OwnedMatrix::get
    0x4555ae: mov      rsi, qword ptr [rsp + 0x90]
    0x4555b6: mov      rdx, qword ptr [rsp + 0x1a8]
    0x4555be: mov      qword ptr [rsp + 0x1d8], rdx
    0x4555c6: mov      rax, qword ptr [rsp + 0x168]
    0x4555ce: mov      qword ptr [rsp + 0x68], rax
    0x4555d3: lea      rdi, [rsp + 0x100]
    0x4555db: call     0x43fd60

; --- Block 0x4555e0 [BODY] 2 insns, callees: (none)
    0x4555e0: mov      qword ptr [rsp + 0x70], rax
    0x4555e5: jmp      0x4555e7

; --- Block 0x4555e7 [BODY] 9 insns, callees: (none)
    0x4555e7: mov      rcx, qword ptr [rsp + 0x70]
    0x4555ec: mov      rax, qword ptr [rsp + 0x68]
    0x4555f1: mov      qword ptr [rsp + 0x208], rax
    0x4555f9: mov      qword ptr [rsp + 0x210], rcx
    0x455601: add      rax, rcx
    0x455604: mov      qword ptr [rsp + 0x60], rax
    0x455609: mov      rax, qword ptr [rsp + 0x60]
    0x45560e: mov      qword ptr [rsp + 0x168], rax
    0x455616: jmp      0x455563

; --- Block 0x45561b [BODY] 6 insns, callees: rust_bench::OwnedMatrix::set
    0x45561b: mov      rcx, qword ptr [rsp + 0xd0]
    0x455623: mov      rsi, qword ptr [rsp + 0xc8]
    0x45562b: xor      eax, eax
    0x45562d: mov      edx, eax
    0x45562f: lea      rdi, [rsp + 0x100]
    0x455637: call     0x43fe70

; --- Block 0x45563c [BODY] 1 insns, callees: (none)
    0x45563c: jmp      0x455652

; --- Block 0x45563e [BODY] 3 insns, callees: (none)
    0x45563e: lea      rdi, [rip + 0x9b72b]
    0x455645: mov      rax, qword ptr [rip + 0x9fae4]
    0x45564c: call     rax

; --- Block 0x455652 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x455652: mov      rax, qword ptr [rsp + 0xe8]
    0x45565a: cmp      rax, 1
    0x45565e: ja       0x45567e

; --- Block 0x455660 [LOOP_HEADER] 3 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x455660: mov      rsi, qword ptr [rsp + 0xe8]
    0x455668: mov      edi, 2
    0x45566d: call     0x49b480

; --- Block 0x455672 [BODY] 3 insns, callees: (none)
    0x455672: mov      qword ptr [rsp + 0x50], rdx
    0x455677: mov      qword ptr [rsp + 0x58], rax
    0x45567c: jmp      0x4556cc

; --- Block 0x45567e [ITERATOR_STATE] 6 insns, callees: (none)
    0x45567e: mov      rcx, qword ptr [rsp + 0xc8]
    0x455686: mov      rax, rcx
    0x455689: add      rax, 2
    0x45568d: mov      qword ptr [rsp + 0x48], rax
    0x455692: cmp      rax, rcx
    0x455695: jb       0x4556b8

; --- Block 0x455697 [BODY] 5 insns, callees: rust_bench::OwnedMatrix::set
    0x455697: mov      rcx, qword ptr [rsp + 0x48]
    0x45569c: mov      rsi, qword ptr [rsp + 0xc8]
    0x4556a4: lea      rdi, [rsp + 0x100]
    0x4556ac: mov      edx, 1
    0x4556b1: call     0x43fe70

; --- Block 0x4556b6 [BODY] 1 insns, callees: (none)
    0x4556b6: jmp      0x4556ca

; --- Block 0x4556b8 [BODY] 3 insns, callees: (none)
    0x4556b8: lea      rdi, [rip + 0x9b6c9]
    0x4556bf: mov      rax, qword ptr [rip + 0x9fa6a]
    0x4556c6: call     rax

; --- Block 0x4556ca [BODY] 1 insns, callees: (none)
    0x4556ca: jmp      0x455660

; --- Block 0x4556cc [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4556cc: mov      rax, qword ptr [rsp + 0x50]
    0x4556d1: mov      rcx, qword ptr [rsp + 0x58]
    0x4556d6: mov      qword ptr [rsp + 0x148], rcx
    0x4556de: mov      qword ptr [rsp + 0x150], rax
    0x4556e6: lea      rdi, [rsp + 0x148]
    0x4556ee: call     0x49ad10

; --- Block 0x4556e6 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4556e6: lea      rdi, [rsp + 0x148]
    0x4556ee: call     0x49ad10

; --- Block 0x4556f3 [BODY] 3 insns, callees: (none)
    0x4556f3: mov      qword ptr [rsp + 0x38], rdx
    0x4556f8: mov      qword ptr [rsp + 0x40], rax
    0x4556fd: jmp      0x4556ff

; --- Block 0x4556ff [BODY] 6 insns, callees: (none)
    0x4556ff: mov      rax, qword ptr [rsp + 0x38]
    0x455704: mov      rcx, qword ptr [rsp + 0x40]
    0x455709: mov      qword ptr [rsp + 0x158], rcx
    0x455711: mov      qword ptr [rsp + 0x160], rax
    0x455719: test     qword ptr [rsp + 0x158], 1
    0x455725: je       0x4553bd

; --- Block 0x45572b [BODY] 8 insns, callees: (none)
    0x45572b: mov      rax, qword ptr [rsp + 0x160]
    0x455733: mov      qword ptr [rsp + 0x28], rax
    0x455738: mov      qword ptr [rsp + 0x1e8], rax
    0x455740: mov      rcx, rax
    0x455743: sub      rcx, 1
    0x455747: mov      qword ptr [rsp + 0x30], rcx
    0x45574c: cmp      rax, 1
    0x455750: jb       0x455773

; --- Block 0x455752 [BODY] 4 insns, callees: rust_bench::OwnedMatrix::get
    0x455752: mov      rdx, qword ptr [rsp + 0x30]
    0x455757: mov      rsi, qword ptr [rsp + 0xc8]
    0x45575f: lea      rdi, [rsp + 0x100]
    0x455767: call     0x43fd60

; --- Block 0x45576c [BODY] 2 insns, callees: (none)
    0x45576c: mov      qword ptr [rsp + 0x20], rax
    0x455771: jmp      0x455788

; --- Block 0x455773 [BODY] 3 insns, callees: (none)
    0x455773: lea      rdi, [rip + 0x9b626]
    0x45577a: mov      rax, qword ptr [rip + 0x9f9cf]
    0x455781: call     rax

; --- Block 0x455788 [ITERATOR_STATE] 6 insns, callees: (none)
    0x455788: mov      rax, qword ptr [rsp + 0x28]
    0x45578d: mov      rcx, rax
    0x455790: sub      rcx, 2
    0x455794: mov      qword ptr [rsp + 0x18], rcx
    0x455799: cmp      rax, 2
    0x45579d: jb       0x4557c0

; --- Block 0x45579f [BODY] 4 insns, callees: rust_bench::OwnedMatrix::get
    0x45579f: mov      rdx, qword ptr [rsp + 0x18]
    0x4557a4: mov      rsi, qword ptr [rsp + 0xc8]
    0x4557ac: lea      rdi, [rsp + 0x100]
    0x4557b4: call     0x43fd60

; --- Block 0x4557b9 [BODY] 2 insns, callees: (none)
    0x4557b9: mov      qword ptr [rsp + 0x10], rax
    0x4557be: jmp      0x4557d5

; --- Block 0x4557c0 [BODY] 3 insns, callees: (none)
    0x4557c0: lea      rdi, [rip + 0x9b5f1]
    0x4557c7: mov      rax, qword ptr [rip + 0x9f982]
    0x4557ce: call     rax

; --- Block 0x4557d5 [BODY] 12 insns, callees: rust_bench::OwnedMatrix::set
    0x4557d5: mov      rcx, qword ptr [rsp + 0x10]
    0x4557da: mov      rax, qword ptr [rsp + 0x20]
    0x4557df: mov      qword ptr [rsp + 0x1f8], rax
    0x4557e7: mov      qword ptr [rsp + 0x200], rcx
    0x4557ef: add      rax, rcx
    0x4557f2: mov      qword ptr [rsp + 8], rax
    0x4557f7: mov      rcx, qword ptr [rsp + 8]
    0x4557fc: mov      rdx, qword ptr [rsp + 0x28]
    0x455801: mov      rsi, qword ptr [rsp + 0xc8]
    0x455809: mov      qword ptr [rsp + 0x1f0], rcx
    0x455811: lea      rdi, [rsp + 0x100]
    0x455819: call     0x43fe70

; --- Block 0x45581e [BODY] 1 insns, callees: (none)
    0x45581e: jmp      0x455820

; --- Block 0x455820 [BODY] 1 insns, callees: (none)
    0x455820: jmp      0x4556e6

```

**O2 blocks** (42 total):

```asm
; --- Block 0x42af10 [BODY] 18 insns, callees: (none)
    0x42af10: push     rbp
    0x42af11: push     r15
    0x42af13: push     r14
    0x42af15: push     r13
    0x42af17: push     r12
    0x42af19: push     rbx
    0x42af1a: sub      rsp, 0x38
    0x42af1e: mov      r14, rdi
    0x42af21: imul     r14, rdi
    0x42af25: lea      r15, [r14*8]
    0x42af2d: mov      rax, r14
    0x42af30: shr      rax, 0x3d
    ... +6 more instructions

; --- Block 0x42af4b [BODY] 4 insns, callees: (none)
    0x42af4b: xor      r12d, r12d
    0x42af4e: mov      rdi, r12
    0x42af51: mov      rsi, r15
    0x42af54: call     qword ptr [rip + 0x5a4be]

; --- Block 0x42af4e [LOOP_HEADER] 3 insns, callees: (none)
    0x42af4e: mov      rdi, r12
    0x42af51: mov      rsi, r15
    0x42af54: call     qword ptr [rip + 0x5a4be]

; --- Block 0x42af5a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42af5a: mov      r10, rdi
    0x42af5d: test     r15, r15
    0x42af60: je       0x42af8c

; --- Block 0x42af62 [BODY] 2 insns, callees: (none)
    0x42af62: mov      rbx, r10
    0x42af65: call     qword ptr [rip + 0x5a47d]

; --- Block 0x42af6b [BODY] 4 insns, callees: (none)
    0x42af6b: mov      r12d, 8
    0x42af71: mov      esi, 8
    0x42af76: mov      rdi, r15
    0x42af79: call     qword ptr [rip + 0x5a4b9]

; --- Block 0x42af7f [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42af7f: test     rax, rax
    0x42af82: je       0x42af4e

; --- Block 0x42af84 [BODY] 3 insns, callees: (none)
    0x42af84: mov      r13, r14
    0x42af87: mov      r10, rbx
    0x42af8a: jmp      0x42af94

; --- Block 0x42af8c [BODY] 11 insns, callees: (none)
    0x42af8c: mov      eax, 8
    0x42af91: xor      r13d, r13d
    0x42af94: mov      qword ptr [rsp + 0x28], r10
    0x42af99: mov      qword ptr [rsp + 0x30], r10
    0x42af9e: mov      qword ptr [rsp + 0x10], r13
    0x42afa3: mov      qword ptr [rsp + 0x18], rax
    0x42afa8: mov      qword ptr [rsp + 0x20], r14
    0x42afad: test     r10, r10
    0x42afb0: mov      qword ptr [rsp], rax
    0x42afb4: mov      qword ptr [rsp + 8], r13
    0x42afb9: je       0x42b16c

; --- Block 0x42af94 [BODY] 9 insns, callees: (none)
    0x42af94: mov      qword ptr [rsp + 0x28], r10
    0x42af99: mov      qword ptr [rsp + 0x30], r10
    0x42af9e: mov      qword ptr [rsp + 0x10], r13
    0x42afa3: mov      qword ptr [rsp + 0x18], rax
    0x42afa8: mov      qword ptr [rsp + 0x20], r14
    0x42afad: test     r10, r10
    0x42afb0: mov      qword ptr [rsp], rax
    0x42afb4: mov      qword ptr [rsp + 8], r13
    0x42afb9: je       0x42b16c

; --- Block 0x42afbf [BODY] 8 insns, callees: (none)
    0x42afbf: lea      rcx, [r10*8]
    0x42afc7: xor      r8d, r8d
    0x42afca: lea      rsi, [rip + 0x575cf]
    0x42afd1: lea      rdx, [rip + 0x575b0]
    0x42afd8: mov      r9, rax
    0x42afdb: mov      r12, r14
    0x42afde: xor      r11d, r11d
    0x42afe1: jmp      0x42b002

; --- Block 0x42aff0 [LOOP_HEADER] 5 insns, callees: (none)
    0x42aff0: sub      r12, r10
    0x42aff3: add      r9, rcx
    0x42aff6: add      r8, r10
    0x42aff9: cmp      r11, r10
    0x42affc: je       0x42b080

; --- Block 0x42b002 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42b002: mov      rdi, r11
    0x42b005: imul     rdi, r10
    0x42b009: cmp      rdi, r14
    0x42b00c: jae      0x42b1b5

; --- Block 0x42b012 [ITERATOR_STATE] 5 insns, callees: (none)
    0x42b012: mov      rbx, r11
    0x42b015: inc      r11
    0x42b018: mov      qword ptr [rax + rdi*8], r11
    0x42b01c: cmp      r10, 1
    0x42b020: je       0x42aff0

; --- Block 0x42b022 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b022: lea      r15, [rdi + 1]
    0x42b026: cmp      r15, r14
    0x42b029: jae      0x42b1c3

; --- Block 0x42b02f [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42b02f: add      rbx, 2
    0x42b033: mov      qword ptr [rax + rdi*8 + 8], rbx
    0x42b038: cmp      r10, 3
    0x42b03c: jb       0x42aff0

; --- Block 0x42b03e [BODY] 5 insns, callees: (none)
    0x42b03e: mov      ebx, 2
    0x42b043: mov      rdi, r8
    0x42b046: nop      word ptr cs:[rax + rax]
    0x42b050: cmp      rdi, r14
    0x42b053: jae      0x42b1b8

; --- Block 0x42b050 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42b050: cmp      rdi, r14
    0x42b053: jae      0x42b1b8

; --- Block 0x42b059 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42b059: cmp      r12, rbx
    0x42b05c: je       0x42b1b1

; --- Block 0x42b062 [BODY] 7 insns, callees: (none)
    0x42b062: mov      r15, qword ptr [r9 + rbx*8 - 0x10]
    0x42b067: add      r15, qword ptr [r9 + rbx*8 - 8]
    0x42b06c: mov      qword ptr [r9 + rbx*8], r15
    0x42b070: inc      rbx
    0x42b073: inc      rdi
    0x42b076: cmp      r10, rbx
    0x42b079: jne      0x42b050

; --- Block 0x42b07b [BODY] 1 insns, callees: (none)
    0x42b07b: jmp      0x42aff0

; --- Block 0x42b080 [BODY] 26 insns, callees: (none)
    0x42b080: lea      rsi, [r10 - 1]
    0x42b084: lea      r8, [rax + 0x10]
    0x42b088: xor      r9d, r9d
    0x42b08b: mov      edx, 4
    0x42b090: mov      r11, rax
    0x42b093: xor      r13d, r13d
    0x42b096: xor      ebp, ebp
    0x42b098: xor      r12d, r12d
    0x42b09b: xor      r15d, r15d
    0x42b09e: nop      
    0x42b0a0: cmp      rbp, r14
    0x42b0a3: mov      rax, r14
    ... +14 more instructions

; --- Block 0x42b0a0 [LOOP_HEADER] 16 insns, callees: (none)
    0x42b0a0: cmp      rbp, r14
    0x42b0a3: mov      rax, r14
    0x42b0a6: cmova    rax, rbp
    0x42b0aa: add      rax, r13
    0x42b0ad: cmp      rax, rsi
    0x42b0b0: cmovae   rax, rsi
    0x42b0b4: mov      rdi, r10
    0x42b0b7: imul     rdi, r15
    0x42b0bb: mov      rbx, r14
    0x42b0be: sub      rbx, rdi
    0x42b0c1: cmovb    rbx, r9
    0x42b0c5: cmp      rbx, rsi
    ... +4 more instructions

; --- Block 0x42b0d5 [BODY] 2 insns, callees: (none)
    0x42b0d5: xor      ebx, ebx
    0x42b0d7: jmp      0x42b130

; --- Block 0x42b0e0 [BODY] 17 insns, callees: (none)
    0x42b0e0: mov      edi, ebx
    0x42b0e2: and      edi, 3
    0x42b0e5: cmove    rdi, rdx
    0x42b0e9: sub      rbx, rdi
    0x42b0ec: movq     xmm0, r12
    0x42b0f1: sub      rax, rdi
    0x42b0f4: inc      rax
    0x42b0f7: pxor     xmm1, xmm1
    0x42b0fb: xor      r12d, r12d
    0x42b0fe: nop      
    0x42b100: movdqu   xmm2, xmmword ptr [r8 + r12*8 - 0x10]
    0x42b107: paddq    xmm0, xmm2
    ... +5 more instructions

; --- Block 0x42b100 [BODY] 7 insns, callees: (none)
    0x42b100: movdqu   xmm2, xmmword ptr [r8 + r12*8 - 0x10]
    0x42b107: paddq    xmm0, xmm2
    0x42b10b: movdqu   xmm2, xmmword ptr [r8 + r12*8]
    0x42b111: paddq    xmm1, xmm2
    0x42b115: add      r12, 4
    0x42b119: cmp      rax, r12
    0x42b11c: jne      0x42b100

; --- Block 0x42b11e [BODY] 9 insns, callees: (none)
    0x42b11e: paddq    xmm1, xmm0
    0x42b122: pshufd   xmm0, xmm1, 0xee
    0x42b127: paddq    xmm0, xmm1
    0x42b12b: movq     r12, xmm0
    0x42b130: inc      r15
    0x42b133: nop      word ptr cs:[rax + rax]
    0x42b140: lea      rdi, [rbx + rbp]
    0x42b144: cmp      rdi, r14
    0x42b147: jae      0x42b1a8

; --- Block 0x42b130 [ITERATOR_STATE] 5 insns, callees: (none)
    0x42b130: inc      r15
    0x42b133: nop      word ptr cs:[rax + rax]
    0x42b140: lea      rdi, [rbx + rbp]
    0x42b144: cmp      rdi, r14
    0x42b147: jae      0x42b1a8

; --- Block 0x42b140 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b140: lea      rdi, [rbx + rbp]
    0x42b144: cmp      rdi, r14
    0x42b147: jae      0x42b1a8

; --- Block 0x42b149 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42b149: add      r12, qword ptr [r11 + rbx*8]
    0x42b14d: inc      rbx
    0x42b150: cmp      r10, rbx
    0x42b153: jne      0x42b140

; --- Block 0x42b155 [ITERATOR_STATE] 6 insns, callees: (none)
    0x42b155: add      r8, rcx
    0x42b158: add      rbp, r10
    0x42b15b: sub      r13, r10
    0x42b15e: add      r11, rcx
    0x42b161: cmp      r15, r10
    0x42b164: jne      0x42b0a0

; --- Block 0x42b16a [BODY] 1 insns, callees: (none)
    0x42b16a: jmp      0x42b16f

; --- Block 0x42b16c [BODY] 3 insns, callees: <rust_bench::OwnedMatrix as core::ops::drop::Drop>::drop
    0x42b16c: xor      r12d, r12d
    0x42b16f: lea      rdi, [rsp + 0x10]
    0x42b174: call     0x434350

; --- Block 0x42b16f [BODY] 2 insns, callees: <rust_bench::OwnedMatrix as core::ops::drop::Drop>::drop
    0x42b16f: lea      rdi, [rsp + 0x10]
    0x42b174: call     0x434350

; --- Block 0x42b179 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b179: mov      rsi, qword ptr [rsp + 8]
    0x42b17e: test     rsi, rsi
    0x42b181: je       0x42b196

; --- Block 0x42b183 [BODY] 4 insns, callees: (none)
    0x42b183: shl      rsi, 3
    0x42b187: mov      edx, 8
    0x42b18c: mov      rdi, qword ptr [rsp]
    0x42b190: call     qword ptr [rip + 0x5a292]

; --- Block 0x42b196 [BODY] 9 insns, callees: (none)
    0x42b196: mov      rax, r12
    0x42b199: add      rsp, 0x38
    0x42b19d: pop      rbx
    0x42b19e: pop      r12
    0x42b1a0: pop      r13
    0x42b1a2: pop      r14
    0x42b1a4: pop      r15
    0x42b1a6: pop      rbp
    0x42b1a7: ret      

; --- Block 0x42b1a8 [BODY] 2 insns, callees: (none)
    0x42b1a8: lea      rdx, [rip + 0x573d9]
    0x42b1af: jmp      0x42b1b8

; --- Block 0x42b1b1 [BODY] 4 insns, callees: (none)
    0x42b1b1: add      rdi, 2
    0x42b1b5: mov      rdx, rsi
    0x42b1b8: mov      rsi, r14
    0x42b1bb: call     qword ptr [rip + 0x5a26f]

; --- Block 0x42b1b5 [LOOP_HEADER] 3 insns, callees: (none)
    0x42b1b5: mov      rdx, rsi
    0x42b1b8: mov      rsi, r14
    0x42b1bb: call     qword ptr [rip + 0x5a26f]

; --- Block 0x42b1b8 [BODY] 2 insns, callees: (none)
    0x42b1b8: mov      rsi, r14
    0x42b1bb: call     qword ptr [rip + 0x5a26f]

; --- Block 0x42b1c3 [BODY] 2 insns, callees: (none)
    0x42b1c3: mov      rdi, r15
    0x42b1c6: jmp      0x42b1b5

```

**Hungarian matching result** (mean similarity: 0.704):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x45543a` | BODY | `0x42b07b` | BODY | 1.000 | GOOD |
| `0x45563c` | BODY | `0x42b16a` | BODY | 1.000 | GOOD |
| `0x45576c` | BODY | `0x42b1c3` | BODY | 1.000 | GOOD |
| `0x45548e` | LOOP_HEADER | `0x42b16f` | BODY | 0.989 | GOOD |
| `0x455363` | BODY | `0x42af84` | BODY | 0.969 | GOOD |
| `0x455652` | BOUNDS_CHECK | `0x42af5a` | BOUNDS_CHECK | 0.954 | GOOD |
| `0x455352` | BODY | `0x42af4b` | BODY | 0.953 | GOOD |
| `0x45540a` | BODY | `0x42b062` | BODY | 0.902 | GOOD |
| `0x455788` | ITERATOR_STATE | `0x42b03e` | BODY | 0.854 | GOOD |
| `0x4553dc` | BODY | `0x42af94` | BODY | 0.851 | GOOD |
| `0x45563e` | BODY | `0x42b1b5` | LOOP_HEADER | 0.841 | GOOD |
| `0x4556b8` | BODY | `0x42af4e` | LOOP_HEADER | 0.839 | GOOD |
| `0x455660` | LOOP_HEADER | `0x42b1b1` | BODY | 0.820 | GOOD |
| `0x4554ad` | BODY | `0x42b012` | ITERATOR_STATE | 0.815 | GOOD |
| `0x4557c0` | BODY | `0x42b16c` | BODY | 0.780 | GOOD |
| `0x4555e0` | BODY | `0x42b1b8` | BODY | 0.769 | GOOD |
| `0x45567e` | ITERATOR_STATE | `0x42b02f` | BOUNDS_CHECK | 0.767 | GOOD |
| `0x4557b9` | BODY | `0x42b0d5` | BODY | 0.754 | GOOD |
| `0x4556ff` | BODY | `0x42b002` | BOUNDS_CHECK | 0.746 | GOOD |
| `0x455773` | BODY | `0x42af62` | BODY | 0.731 | GOOD |
| `0x4553ca` | BODY | `0x42b179` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x45557f` | BODY | `0x42b155` | ITERATOR_STATE | 0.701 | GOOD |
| `0x45561b` | BODY | `0x42afbf` | BODY | 0.669 | PARTIAL |
| `0x4556b6` | BODY | `0x42b1a8` | BODY | 0.653 | PARTIAL |
| `0x455563` | LOOP_HEADER | `0x42b050` | BOUNDS_CHECK | 0.643 | PARTIAL |
| `0x4553bd` | LOOP_HEADER | `0x42b059` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x4556e6` | LOOP_HEADER | `0x42af7f` | BOUNDS_CHECK | 0.638 | PARTIAL |
| `0x45549b` | BODY | `0x42b140` | BOUNDS_CHECK | 0.628 | PARTIAL |
| `0x455516` | DROP_GLUE | `0x42af6b` | BODY | 0.627 | PARTIAL |
| `0x455697` | BODY | `0x42b130` | ITERATOR_STATE | 0.623 | PARTIAL |
| `0x45545c` | BODY | `0x42b022` | BOUNDS_CHECK | 0.620 | PARTIAL |
| `0x45579f` | BODY | `0x42b149` | BOUNDS_CHECK | 0.616 | PARTIAL |
| `0x455752` | BODY | `0x42b183` | BODY | 0.593 | PARTIAL |
| `0x45543f` | BODY | `0x42aff0` | LOOP_HEADER | 0.560 | PARTIAL |
| `0x4555e7` | BODY | `0x42b196` | BODY | 0.543 | PARTIAL |
| `0x4554db` | BODY | `0x42af8c` | BODY | 0.476 | PARTIAL |
| `0x45572b` | BODY | `0x42b0a0` | LOOP_HEADER | 0.451 | PARTIAL |
| `0x4555ae` | BODY | `0x42b100` | BODY | 0.439 | PARTIAL |
| `0x455320` | BODY | `0x42b11e` | BODY | 0.419 | PARTIAL |
| `0x4557d5` | BODY | `0x42b0e0` | BODY | 0.382 | POOR |
| `0x455543` | BODY | `0x42af10` | BODY | 0.318 | POOR |
| `0x45546e` | BODY | `0x42b080` | BODY | 0.251 | POOR |
| `0x45539d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x455504` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x455533` | EPILOGUE | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x455570` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x455672` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4556ca` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4556cc` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4556f3` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45581e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x455820` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `own_01` — O0: 17 blocks, O2: 15 blocks

**O0 blocks** (17 total):

```asm
; --- Block 0x40332f [BODY] 12 insns, callees: cmatrix_new
    0x40332f: push     rbp
    0x403330: mov      rbp, rsp
    0x403333: sub      rsp, 0x60
    0x403337: mov      qword ptr [rbp - 0x58], rdi
    0x40333b: mov      rax, qword ptr [rbp - 0x58]
    0x40333f: mov      qword ptr [rbp - 0x30], rax
    0x403343: lea      rax, [rbp - 0x50]
    0x403347: mov      rdx, qword ptr [rbp - 0x30]
    0x40334b: mov      rcx, qword ptr [rbp - 0x30]
    0x40334f: mov      rsi, rcx
    0x403352: mov      rdi, rax
    0x403355: call     0x403263

; --- Block 0x40335a [BODY] 2 insns, callees: (none)
    0x40335a: mov      qword ptr [rbp - 8], 0
    0x403362: jmp      0x40343c

; --- Block 0x403367 [LOOP_HEADER] 10 insns, callees: (none)
    0x403367: mov      rdx, qword ptr [rbp - 0x40]
    0x40336b: mov      rax, qword ptr [rbp - 8]
    0x40336f: imul     rax, qword ptr [rbp - 0x30]
    0x403374: shl      rax, 3
    0x403378: add      rax, rdx
    0x40337b: mov      rdx, qword ptr [rbp - 8]
    0x40337f: add      rdx, 1
    0x403383: mov      qword ptr [rax], rdx
    0x403386: cmp      qword ptr [rbp - 0x30], 1
    0x40338b: jbe      0x4033b0

; --- Block 0x40338d [BODY] 11 insns, callees: (none)
    0x40338d: mov      rdx, qword ptr [rbp - 0x40]
    0x403391: mov      rax, qword ptr [rbp - 8]
    0x403395: imul     rax, qword ptr [rbp - 0x30]
    0x40339a: add      rax, 1
    0x40339e: shl      rax, 3
    0x4033a2: add      rax, rdx
    0x4033a5: mov      rdx, qword ptr [rbp - 8]
    0x4033a9: add      rdx, 2
    0x4033ad: mov      qword ptr [rax], rdx
    0x4033b0: mov      qword ptr [rbp - 0x10], 2
    0x4033b8: jmp      0x40342d

; --- Block 0x4033b0 [BODY] 2 insns, callees: (none)
    0x4033b0: mov      qword ptr [rbp - 0x10], 2
    0x4033b8: jmp      0x40342d

; --- Block 0x4033ba [LOOP_HEADER] 34 insns, callees: (none)
    0x4033ba: mov      rdx, qword ptr [rbp - 0x40]
    0x4033be: mov      rax, qword ptr [rbp - 8]
    0x4033c2: imul     rax, qword ptr [rbp - 0x30]
    0x4033c7: mov      rcx, rax
    0x4033ca: mov      rax, qword ptr [rbp - 0x10]
    0x4033ce: add      rax, rcx
    0x4033d1: shl      rax, 3
    0x4033d5: sub      rax, 8
    0x4033d9: add      rax, rdx
    0x4033dc: mov      rcx, qword ptr [rax]
    0x4033df: mov      rdx, qword ptr [rbp - 0x40]
    0x4033e3: mov      rax, qword ptr [rbp - 8]
    ... +22 more instructions

; --- Block 0x40342d [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40342d: mov      rax, qword ptr [rbp - 0x10]
    0x403431: cmp      rax, qword ptr [rbp - 0x30]
    0x403435: jb       0x4033ba

; --- Block 0x403437 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x403437: add      qword ptr [rbp - 8], 1
    0x40343c: mov      rax, qword ptr [rbp - 8]
    0x403440: cmp      rax, qword ptr [rbp - 0x30]
    0x403444: jb       0x403367

; --- Block 0x40343c [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40343c: mov      rax, qword ptr [rbp - 8]
    0x403440: cmp      rax, qword ptr [rbp - 0x30]
    0x403444: jb       0x403367

; --- Block 0x40344a [BODY] 3 insns, callees: (none)
    0x40344a: mov      qword ptr [rbp - 0x18], 0
    0x403452: mov      qword ptr [rbp - 0x20], 0
    0x40345a: jmp      0x40349f

; --- Block 0x40345c [LOOP_HEADER] 2 insns, callees: (none)
    0x40345c: mov      qword ptr [rbp - 0x28], 0
    0x403464: jmp      0x403490

; --- Block 0x403466 [LOOP_HEADER] 14 insns, callees: (none)
    0x403466: mov      rdx, qword ptr [rbp - 0x40]
    0x40346a: mov      rax, qword ptr [rbp - 0x20]
    0x40346e: imul     rax, qword ptr [rbp - 0x30]
    0x403473: mov      rcx, rax
    0x403476: mov      rax, qword ptr [rbp - 0x28]
    0x40347a: add      rax, rcx
    0x40347d: shl      rax, 3
    0x403481: add      rax, rdx
    0x403484: mov      rax, qword ptr [rax]
    0x403487: add      qword ptr [rbp - 0x18], rax
    0x40348b: add      qword ptr [rbp - 0x28], 1
    0x403490: mov      rax, qword ptr [rbp - 0x28]
    ... +2 more instructions

; --- Block 0x403490 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403490: mov      rax, qword ptr [rbp - 0x28]
    0x403494: cmp      rax, qword ptr [rbp - 0x30]
    0x403498: jb       0x403466

; --- Block 0x40349a [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40349a: add      qword ptr [rbp - 0x20], 1
    0x40349f: mov      rax, qword ptr [rbp - 0x20]
    0x4034a3: cmp      rax, qword ptr [rbp - 0x30]
    0x4034a7: jb       0x40345c

; --- Block 0x40349f [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40349f: mov      rax, qword ptr [rbp - 0x20]
    0x4034a3: cmp      rax, qword ptr [rbp - 0x30]
    0x4034a7: jb       0x40345c

; --- Block 0x4034a9 [BODY] 3 insns, callees: cmatrix_free
    0x4034a9: lea      rax, [rbp - 0x50]
    0x4034ad: mov      rdi, rax
    0x4034b0: call     0x4032c2

; --- Block 0x4034b5 [BODY] 3 insns, callees: (none)
    0x4034b5: mov      rax, qword ptr [rbp - 0x18]
    0x4034b9: leave    
    0x4034ba: ret      

```

**O2 blocks** (15 total):

```asm
; --- Block 0x404820 [BODY] 7 insns, callees: sub_4010c0
    0x404820: push     r12
    0x404822: mov      esi, 8
    0x404827: push     rbx
    0x404828: mov      rbx, rdi
    0x40482b: imul     rdi, rdi
    0x40482f: sub      rsp, 8
    0x404833: call     0x4010c0

; --- Block 0x404838 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x404838: mov      r10, rax
    0x40483b: test     rbx, rbx
    0x40483e: je       0x4048eb

; --- Block 0x404844 [BODY] 10 insns, callees: (none)
    0x404844: lea      r9, [rbx*8]
    0x40484c: mov      r8, rax
    0x40484f: xor      edi, edi
    0x404851: lea      rsi, [rax + r9 - 0x10]
    0x404856: nop      word ptr cs:[rax + rax]
    0x404860: mov      rdx, rdi
    0x404863: add      rdi, 1
    0x404867: mov      qword ptr [r8], rdi
    0x40486a: cmp      rbx, 1
    0x40486e: je       0x40489c

; --- Block 0x404860 [LOOP_HEADER] 5 insns, callees: (none)
    0x404860: mov      rdx, rdi
    0x404863: add      rdi, 1
    0x404867: mov      qword ptr [r8], rdi
    0x40486a: cmp      rbx, 1
    0x40486e: je       0x40489c

; --- Block 0x404870 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x404870: add      rdx, 2
    0x404874: mov      qword ptr [r8 + 8], rdx
    0x404878: cmp      rbx, 2
    0x40487c: je       0x40489c

; --- Block 0x40487e [BODY] 8 insns, callees: (none)
    0x40487e: mov      rdx, r8
    0x404881: nop      dword ptr [rax]
    0x404888: mov      rcx, qword ptr [rdx]
    0x40488b: add      rcx, qword ptr [rdx + 8]
    0x40488f: add      rdx, 8
    0x404893: mov      qword ptr [rdx + 8], rcx
    0x404897: cmp      rdx, rsi
    0x40489a: jne      0x404888

; --- Block 0x404888 [ITERATOR_STATE] 6 insns, callees: (none)
    0x404888: mov      rcx, qword ptr [rdx]
    0x40488b: add      rcx, qword ptr [rdx + 8]
    0x40488f: add      rdx, 8
    0x404893: mov      qword ptr [rdx + 8], rcx
    0x404897: cmp      rdx, rsi
    0x40489a: jne      0x404888

; --- Block 0x40489c [BOUNDS_CHECK] 4 insns, callees: (none)
    0x40489c: add      r8, r9
    0x40489f: add      rsi, r9
    0x4048a2: cmp      rdi, rbx
    0x4048a5: jne      0x404860

; --- Block 0x4048a7 [BODY] 10 insns, callees: (none)
    0x4048a7: lea      rcx, [r10 + r9]
    0x4048ab: xor      esi, esi
    0x4048ad: xor      r12d, r12d
    0x4048b0: mov      rdx, rcx
    0x4048b3: sub      rdx, r9
    0x4048b6: nop      word ptr cs:[rax + rax]
    0x4048c0: add      r12, qword ptr [rdx]
    0x4048c3: add      rdx, 8
    0x4048c7: cmp      rcx, rdx
    0x4048ca: jne      0x4048c0

; --- Block 0x4048b0 [LOOP_HEADER] 7 insns, callees: (none)
    0x4048b0: mov      rdx, rcx
    0x4048b3: sub      rdx, r9
    0x4048b6: nop      word ptr cs:[rax + rax]
    0x4048c0: add      r12, qword ptr [rdx]
    0x4048c3: add      rdx, 8
    0x4048c7: cmp      rcx, rdx
    0x4048ca: jne      0x4048c0

; --- Block 0x4048c0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4048c0: add      r12, qword ptr [rdx]
    0x4048c3: add      rdx, 8
    0x4048c7: cmp      rcx, rdx
    0x4048ca: jne      0x4048c0

; --- Block 0x4048cc [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4048cc: add      rsi, 1
    0x4048d0: add      rcx, r9
    0x4048d3: cmp      rbx, rsi
    0x4048d6: jne      0x4048b0

; --- Block 0x4048d8 [LOOP_HEADER] 2 insns, callees: sub_401030
    0x4048d8: mov      rdi, r10
    0x4048db: call     0x401030

; --- Block 0x4048e0 [EPILOGUE] 5 insns, callees: (none)
    0x4048e0: add      rsp, 8
    0x4048e4: mov      rax, r12
    0x4048e7: pop      rbx
    0x4048e8: pop      r12
    0x4048ea: ret      

; --- Block 0x4048eb [BODY] 2 insns, callees: (none)
    0x4048eb: xor      r12d, r12d
    0x4048ee: jmp      0x4048d8

```

**Hungarian matching result** (mean similarity: 0.627):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x40342d` | BOUNDS_CHECK | `0x404838` | BOUNDS_CHECK | 0.977 | GOOD |
| `0x40349a` | BOUNDS_CHECK | `0x40489c` | BOUNDS_CHECK | 0.882 | GOOD |
| `0x403437` | BOUNDS_CHECK | `0x4048cc` | BOUNDS_CHECK | 0.866 | GOOD |
| `0x40345c` | LOOP_HEADER | `0x4048eb` | BODY | 0.758 | GOOD |
| `0x403490` | BOUNDS_CHECK | `0x404860` | LOOP_HEADER | 0.717 | GOOD |
| `0x4033b0` | BODY | `0x404870` | BOUNDS_CHECK | 0.644 | PARTIAL |
| `0x40335a` | BODY | `0x4048d8` | LOOP_HEADER | 0.553 | PARTIAL |
| `0x403466` | LOOP_HEADER | `0x40487e` | BODY | 0.531 | PARTIAL |
| `0x40349f` | BOUNDS_CHECK | `0x4048c0` | BOUNDS_CHECK | 0.527 | PARTIAL |
| `0x403367` | LOOP_HEADER | `0x404844` | BODY | 0.527 | PARTIAL |
| `0x40343c` | BOUNDS_CHECK | `0x404888` | ITERATOR_STATE | 0.523 | PARTIAL |
| `0x4033ba` | LOOP_HEADER | `0x4048b0` | LOOP_HEADER | 0.511 | PARTIAL |
| `0x40332f` | BODY | `0x404820` | BODY | 0.484 | PARTIAL |
| `0x4034b5` | BODY | `0x4048e0` | EPILOGUE | 0.458 | PARTIAL |
| `0x40338d` | BODY | `0x4048a7` | BODY | 0.444 | PARTIAL |
| `0x40344a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4034a9` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

---

## Function `own_05`

### Rust `own_05` — O0: 75 blocks, O2: 46 blocks

**O0 blocks** (75 total):

```asm
; --- Block 0x4564f0 [BODY] 8 insns, callees: alloc::vec::Vec<T,A>::len
    0x4564f0: sub      rsp, 0x188
    0x4564f7: mov      qword ptr [rsp + 0xf8], rdx
    0x4564ff: mov      qword ptr [rsp + 0x100], rsi
    0x456507: mov      rax, rdi
    0x45650a: mov      rdi, qword ptr [rsp + 0x100]
    0x456512: mov      qword ptr [rsp + 0x108], rax
    0x45651a: mov      qword ptr [rsp + 0x110], rax
    0x456522: call     0x4a8ea0

; --- Block 0x456527 [BODY] 2 insns, callees: (none)
    0x456527: mov      qword ptr [rsp + 0x118], rax
    0x45652f: jmp      0x456559

; --- Block 0x456559 [BODY] 2 insns, callees: alloc::vec::Vec<T,A>::len
    0x456559: mov      rdi, qword ptr [rsp + 0xf8]
    0x456561: call     0x4a8ea0

; --- Block 0x456566 [BODY] 2 insns, callees: (none)
    0x456566: mov      qword ptr [rsp + 0xf0], rax
    0x45656e: jmp      0x456570

; --- Block 0x456570 [BODY] 7 insns, callees: (none)
    0x456570: mov      rcx, qword ptr [rsp + 0x118]
    0x456578: mov      rdx, qword ptr [rsp + 0xf0]
    0x456580: mov      rax, rcx
    0x456583: add      rax, rdx
    0x456586: mov      qword ptr [rsp + 0xe8], rax
    0x45658e: cmp      rax, rcx
    0x456591: jb       0x4565aa

; --- Block 0x456593 [BODY] 3 insns, callees: alloc::vec::Vec<T>::with_capacity
    0x456593: mov      rsi, qword ptr [rsp + 0xe8]
    0x45659b: lea      rdi, [rsp + 0x120]
    0x4565a3: call     0x4a5020

; --- Block 0x4565a8 [BODY] 1 insns, callees: (none)
    0x4565a8: jmp      0x4565be

; --- Block 0x4565aa [BODY] 3 insns, callees: (none)
    0x4565aa: lea      rdi, [rip + 0x9a90f]
    0x4565b1: mov      rax, qword ptr [rip + 0x9eb78]
    0x4565b8: call     rax

; --- Block 0x4565be [BODY] 6 insns, callees: alloc::vec::Vec<T,A>::len
    0x4565be: mov      qword ptr [rsp + 0x138], 0
    0x4565ca: mov      qword ptr [rsp + 0x140], 0
    0x4565d6: mov      rdi, qword ptr [rsp + 0x100]
    0x4565de: mov      rax, qword ptr [rsp + 0x138]
    0x4565e6: mov      qword ptr [rsp + 0xd8], rax
    0x4565ee: call     0x4a8ea0

; --- Block 0x4565d6 [LOOP_HEADER] 4 insns, callees: alloc::vec::Vec<T,A>::len
    0x4565d6: mov      rdi, qword ptr [rsp + 0x100]
    0x4565de: mov      rax, qword ptr [rsp + 0x138]
    0x4565e6: mov      qword ptr [rsp + 0xd8], rax
    0x4565ee: call     0x4a8ea0

; --- Block 0x4565f3 [BODY] 2 insns, callees: (none)
    0x4565f3: mov      qword ptr [rsp + 0xe0], rax
    0x4565fb: jmp      0x456625

; --- Block 0x456625 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x456625: mov      rax, qword ptr [rsp + 0xd8]
    0x45662d: mov      rcx, qword ptr [rsp + 0xe0]
    0x456635: cmp      rax, rcx
    0x456638: jb       0x456661

; --- Block 0x45663a [LOOP_HEADER] 4 insns, callees: alloc::vec::Vec<T,A>::len
    0x45663a: mov      rdi, qword ptr [rsp + 0x100]
    0x456642: mov      rax, qword ptr [rsp + 0x138]
    0x45664a: mov      qword ptr [rsp + 0xc8], rax
    0x456652: call     0x4a8ea0

; --- Block 0x456657 [BODY] 2 insns, callees: (none)
    0x456657: mov      qword ptr [rsp + 0xd0], rax
    0x45665f: jmp      0x4566c6

; --- Block 0x456661 [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::len
    0x456661: mov      rdi, qword ptr [rsp + 0xf8]
    0x456669: mov      rax, qword ptr [rsp + 0x140]
    0x456671: mov      qword ptr [rsp + 0xb8], rax
    0x456679: call     0x4a8ea0

; --- Block 0x45667e [BODY] 2 insns, callees: (none)
    0x45667e: mov      qword ptr [rsp + 0xc0], rax
    0x456686: jmp      0x456688

; --- Block 0x456688 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x456688: mov      rax, qword ptr [rsp + 0xb8]
    0x456690: mov      rcx, qword ptr [rsp + 0xc0]
    0x456698: cmp      rax, rcx
    0x45669b: jae      0x45663a

; --- Block 0x45669d [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x45669d: mov      rdi, qword ptr [rsp + 0x100]
    0x4566a5: mov      rsi, qword ptr [rsp + 0x138]
    0x4566ad: lea      rdx, [rip + 0x9a8cc]
    0x4566b4: call     0x4abb40

; --- Block 0x4566b9 [BODY] 2 insns, callees: (none)
    0x4566b9: mov      qword ptr [rsp + 0xb0], rax
    0x4566c1: jmp      0x4569e4

; --- Block 0x4566c6 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4566c6: mov      rax, qword ptr [rsp + 0xc8]
    0x4566ce: mov      rcx, qword ptr [rsp + 0xd0]
    0x4566d6: cmp      rax, rcx
    0x4566d9: jb       0x456702

; --- Block 0x4566db [LOOP_HEADER] 4 insns, callees: alloc::vec::Vec<T,A>::len
    0x4566db: mov      rdi, qword ptr [rsp + 0xf8]
    0x4566e3: mov      rax, qword ptr [rsp + 0x140]
    0x4566eb: mov      qword ptr [rsp + 0xa0], rax
    0x4566f3: call     0x4a8ea0

; --- Block 0x4566f8 [BODY] 2 insns, callees: (none)
    0x4566f8: mov      qword ptr [rsp + 0xa8], rax
    0x456700: jmp      0x45672b

; --- Block 0x456702 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x456702: mov      rdi, qword ptr [rsp + 0x100]
    0x45670a: mov      rsi, qword ptr [rsp + 0x138]
    0x456712: lea      rdx, [rip + 0x9a837]
    0x456719: call     0x4abb40

; --- Block 0x45671e [BODY] 2 insns, callees: (none)
    0x45671e: mov      qword ptr [rsp + 0x98], rax
    0x456726: jmp      0x45698a

; --- Block 0x45672b [BOUNDS_CHECK] 4 insns, callees: (none)
    0x45672b: mov      rax, qword ptr [rsp + 0xa0]
    0x456733: mov      rcx, qword ptr [rsp + 0xa8]
    0x45673b: cmp      rax, rcx
    0x45673e: jb       0x456763

; --- Block 0x456740 [BODY] 3 insns, callees: alloc::vec::Vec<T,A>::len
    0x456740: mov      qword ptr [rsp + 0x148], 0
    0x45674c: lea      rdi, [rsp + 0x120]
    0x456754: call     0x4a8ea0

; --- Block 0x456759 [BODY] 2 insns, callees: (none)
    0x456759: mov      qword ptr [rsp + 0x90], rax
    0x456761: jmp      0x45678c

; --- Block 0x456763 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x456763: mov      rdi, qword ptr [rsp + 0xf8]
    0x45676b: mov      rsi, qword ptr [rsp + 0x140]
    0x456773: lea      rdx, [rip + 0x9a7a6]
    0x45677a: call     0x4abb40

; --- Block 0x45677f [BODY] 2 insns, callees: (none)
    0x45677f: mov      qword ptr [rsp + 0x88], rax
    0x456787: jmp      0x456930

; --- Block 0x45678c [BODY] 4 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x45678c: mov      rsi, qword ptr [rsp + 0x90]
    0x456794: xor      eax, eax
    0x456796: mov      edi, eax
    0x456798: call     0x49b480

; --- Block 0x45679d [BODY] 3 insns, callees: (none)
    0x45679d: mov      qword ptr [rsp + 0x78], rdx
    0x4567a2: mov      qword ptr [rsp + 0x80], rax
    0x4567aa: jmp      0x4567ac

; --- Block 0x4567ac [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4567ac: mov      rax, qword ptr [rsp + 0x78]
    0x4567b1: mov      rcx, qword ptr [rsp + 0x80]
    0x4567b9: mov      qword ptr [rsp + 0x150], rcx
    0x4567c1: mov      qword ptr [rsp + 0x158], rax
    0x4567c9: lea      rdi, [rsp + 0x150]
    0x4567d1: call     0x49ad10

; --- Block 0x4567c9 [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x4567c9: lea      rdi, [rsp + 0x150]
    0x4567d1: call     0x49ad10

; --- Block 0x4567d6 [BODY] 3 insns, callees: (none)
    0x4567d6: mov      qword ptr [rsp + 0x68], rdx
    0x4567db: mov      qword ptr [rsp + 0x70], rax
    0x4567e0: jmp      0x4567e2

; --- Block 0x4567e2 [BODY] 6 insns, callees: (none)
    0x4567e2: mov      rax, qword ptr [rsp + 0x68]
    0x4567e7: mov      rcx, qword ptr [rsp + 0x70]
    0x4567ec: mov      qword ptr [rsp + 0x160], rcx
    0x4567f4: mov      qword ptr [rsp + 0x168], rax
    0x4567fc: test     qword ptr [rsp + 0x160], 1
    0x456808: je       0x45683a

; --- Block 0x45680a [BODY] 6 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x45680a: mov      rsi, qword ptr [rsp + 0x168]
    0x456812: mov      qword ptr [rsp + 0x58], rsi
    0x456817: mov      qword ptr [rsp + 0x180], rsi
    0x45681f: lea      rdx, [rip + 0x9a6b2]
    0x456826: lea      rdi, [rsp + 0x120]
    0x45682e: call     0x4abb40

; --- Block 0x456833 [BODY] 2 insns, callees: (none)
    0x456833: mov      qword ptr [rsp + 0x60], rax
    0x456838: jmp      0x4568ad

; --- Block 0x45683a [DROP_GLUE] 7 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<u64>>
    0x45683a: mov      rdi, qword ptr [rsp + 0xf8]
    0x456842: mov      rax, qword ptr [rsp + 0x108]
    0x45684a: mov      rcx, qword ptr [rsp + 0x130]
    0x456852: mov      qword ptr [rax + 0x10], rcx
    0x456856: movups   xmm0, xmmword ptr [rsp + 0x120]
    0x45685e: movups   xmmword ptr [rax], xmm0
    0x456861: call     0x496820

; --- Block 0x456866 [BODY] 1 insns, callees: (none)
    0x456866: jmp      0x456890

; --- Block 0x456890 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<u64>>
    0x456890: mov      rdi, qword ptr [rsp + 0x100]
    0x456898: call     0x496820

; --- Block 0x45689d [EPILOGUE] 3 insns, callees: (none)
    0x45689d: mov      rax, qword ptr [rsp + 0x110]
    0x4568a5: add      rsp, 0x188
    0x4568ac: ret      

; --- Block 0x4568ad [BOUNDS_CHECK] 4 insns, callees: (none)
    0x4568ad: mov      rax, qword ptr [rsp + 0x60]
    0x4568b2: mov      rax, qword ptr [rax]
    0x4568b5: cmp      rax, qword ptr [rsp + 0x148]
    0x4568bd: ja       0x4568ec

; --- Block 0x4568bf [LOOP_HEADER] 6 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::IndexMut<I>>::index_mut
    0x4568bf: mov      rsi, qword ptr [rsp + 0x58]
    0x4568c4: mov      rax, qword ptr [rsp + 0x148]
    0x4568cc: mov      qword ptr [rsp + 0x48], rax
    0x4568d1: lea      rdx, [rip + 0x9a630]
    0x4568d8: lea      rdi, [rsp + 0x120]
    0x4568e0: call     0x4abdc0

; --- Block 0x4568e5 [BODY] 2 insns, callees: (none)
    0x4568e5: mov      qword ptr [rsp + 0x50], rax
    0x4568ea: jmp      0x45691e

; --- Block 0x4568ec [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x4568ec: mov      rsi, qword ptr [rsp + 0x58]
    0x4568f1: lea      rdx, [rip + 0x9a5f8]
    0x4568f8: lea      rdi, [rsp + 0x120]
    0x456900: call     0x4abb40

; --- Block 0x456905 [BODY] 2 insns, callees: (none)
    0x456905: mov      qword ptr [rsp + 0x40], rax
    0x45690a: jmp      0x45690c

; --- Block 0x45690c [BODY] 4 insns, callees: (none)
    0x45690c: mov      rax, qword ptr [rsp + 0x40]
    0x456911: mov      rax, qword ptr [rax]
    0x456914: mov      qword ptr [rsp + 0x148], rax
    0x45691c: jmp      0x4568bf

; --- Block 0x45691e [BODY] 4 insns, callees: (none)
    0x45691e: mov      rax, qword ptr [rsp + 0x50]
    0x456923: mov      rcx, qword ptr [rsp + 0x48]
    0x456928: mov      qword ptr [rax], rcx
    0x45692b: jmp      0x4567c9

; --- Block 0x456930 [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x456930: mov      rax, qword ptr [rsp + 0x88]
    0x456938: mov      rsi, qword ptr [rax]
    0x45693b: lea      rdi, [rsp + 0x120]
    0x456943: call     0x4a9070

; --- Block 0x456948 [BODY] 1 insns, callees: (none)
    0x456948: jmp      0x45694a

; --- Block 0x45694a [ITERATOR_STATE] 6 insns, callees: (none)
    0x45694a: mov      rcx, qword ptr [rsp + 0x140]
    0x456952: mov      rax, rcx
    0x456955: add      rax, 1
    0x456959: mov      qword ptr [rsp + 0x38], rax
    0x45695e: cmp      rax, rcx
    0x456961: jb       0x456975

; --- Block 0x456963 [BODY] 3 insns, callees: (none)
    0x456963: mov      rax, qword ptr [rsp + 0x38]
    0x456968: mov      qword ptr [rsp + 0x140], rax
    0x456970: jmp      0x4566db

; --- Block 0x456975 [BODY] 3 insns, callees: (none)
    0x456975: lea      rdi, [rip + 0x9a5bc]
    0x45697c: mov      rax, qword ptr [rip + 0x9e7ad]
    0x456983: call     rax

; --- Block 0x45698a [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x45698a: mov      rax, qword ptr [rsp + 0x98]
    0x456992: mov      rsi, qword ptr [rax]
    0x456995: lea      rdi, [rsp + 0x120]
    0x45699d: call     0x4a9070

; --- Block 0x4569a2 [BODY] 1 insns, callees: (none)
    0x4569a2: jmp      0x4569a4

; --- Block 0x4569a4 [ITERATOR_STATE] 6 insns, callees: (none)
    0x4569a4: mov      rcx, qword ptr [rsp + 0x138]
    0x4569ac: mov      rax, rcx
    0x4569af: add      rax, 1
    0x4569b3: mov      qword ptr [rsp + 0x30], rax
    0x4569b8: cmp      rax, rcx
    0x4569bb: jb       0x4569cf

; --- Block 0x4569bd [BODY] 3 insns, callees: (none)
    0x4569bd: mov      rax, qword ptr [rsp + 0x30]
    0x4569c2: mov      qword ptr [rsp + 0x138], rax
    0x4569ca: jmp      0x45663a

; --- Block 0x4569cf [BODY] 3 insns, callees: (none)
    0x4569cf: lea      rdi, [rip + 0x9a592]
    0x4569d6: mov      rax, qword ptr [rip + 0x9e753]
    0x4569dd: call     rax

; --- Block 0x4569e4 [BODY] 7 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x4569e4: mov      rdi, qword ptr [rsp + 0xf8]
    0x4569ec: mov      rax, qword ptr [rsp + 0xb0]
    0x4569f4: mov      rax, qword ptr [rax]
    0x4569f7: mov      qword ptr [rsp + 0x20], rax
    0x4569fc: mov      rsi, qword ptr [rsp + 0x140]
    0x456a04: lea      rdx, [rip + 0x9a58d]
    0x456a0b: call     0x4abb40

; --- Block 0x456a10 [BODY] 2 insns, callees: (none)
    0x456a10: mov      qword ptr [rsp + 0x28], rax
    0x456a15: jmp      0x456a17

; --- Block 0x456a17 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x456a17: mov      rax, qword ptr [rsp + 0x20]
    0x456a1c: mov      rcx, qword ptr [rsp + 0x28]
    0x456a21: cmp      rax, qword ptr [rcx]
    0x456a24: jbe      0x456a49

; --- Block 0x456a26 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x456a26: mov      rdi, qword ptr [rsp + 0xf8]
    0x456a2e: mov      rsi, qword ptr [rsp + 0x140]
    0x456a36: lea      rdx, [rip + 0x9a573]
    0x456a3d: call     0x4abb40

; --- Block 0x456a42 [BODY] 2 insns, callees: (none)
    0x456a42: mov      qword ptr [rsp + 0x18], rax
    0x456a47: jmp      0x456a6c

; --- Block 0x456a49 [BODY] 4 insns, callees: <alloc::vec::Vec<T,A> as core::ops::index::Index<I>>::index
    0x456a49: mov      rdi, qword ptr [rsp + 0x100]
    0x456a51: mov      rsi, qword ptr [rsp + 0x138]
    0x456a59: lea      rdx, [rip + 0x9a580]
    0x456a60: call     0x4abb40

; --- Block 0x456a65 [BODY] 2 insns, callees: (none)
    0x456a65: mov      qword ptr [rsp + 0x10], rax
    0x456a6a: jmp      0x456ac3

; --- Block 0x456a6c [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x456a6c: mov      rax, qword ptr [rsp + 0x18]
    0x456a71: mov      rsi, qword ptr [rax]
    0x456a74: lea      rdi, [rsp + 0x120]
    0x456a7c: call     0x4a9070

; --- Block 0x456a81 [BODY] 1 insns, callees: (none)
    0x456a81: jmp      0x456a83

; --- Block 0x456a83 [ITERATOR_STATE] 6 insns, callees: (none)
    0x456a83: mov      rcx, qword ptr [rsp + 0x140]
    0x456a8b: mov      rax, rcx
    0x456a8e: add      rax, 1
    0x456a92: mov      qword ptr [rsp + 8], rax
    0x456a97: cmp      rax, rcx
    0x456a9a: jb       0x456aae

; --- Block 0x456a9c [BODY] 3 insns, callees: (none)
    0x456a9c: mov      rax, qword ptr [rsp + 8]
    0x456aa1: mov      qword ptr [rsp + 0x140], rax
    0x456aa9: jmp      0x4565d6

; --- Block 0x456aae [BODY] 3 insns, callees: (none)
    0x456aae: lea      rdi, [rip + 0x9a513]
    0x456ab5: mov      rax, qword ptr [rip + 0x9e674]
    0x456abc: call     rax

; --- Block 0x456ac3 [BODY] 4 insns, callees: alloc::vec::Vec<T,A>::push
    0x456ac3: mov      rax, qword ptr [rsp + 0x10]
    0x456ac8: mov      rsi, qword ptr [rax]
    0x456acb: lea      rdi, [rsp + 0x120]
    0x456ad3: call     0x4a9070

; --- Block 0x456ad8 [BODY] 1 insns, callees: (none)
    0x456ad8: jmp      0x456ada

; --- Block 0x456ada [ITERATOR_STATE] 6 insns, callees: (none)
    0x456ada: mov      rcx, qword ptr [rsp + 0x138]
    0x456ae2: mov      rax, rcx
    0x456ae5: add      rax, 1
    0x456ae9: mov      qword ptr [rsp], rax
    0x456aed: cmp      rax, rcx
    0x456af0: jb       0x456b03

; --- Block 0x456af2 [BODY] 3 insns, callees: (none)
    0x456af2: mov      rax, qword ptr [rsp]
    0x456af6: mov      qword ptr [rsp + 0x138], rax
    0x456afe: jmp      0x4565d6

; --- Block 0x456b03 [BODY] 3 insns, callees: (none)
    0x456b03: lea      rdi, [rip + 0x9a4ee]
    0x456b0a: mov      rax, qword ptr [rip + 0x9e61f]
    0x456b11: call     rax

```

**O2 blocks** (46 total):

```asm
; --- Block 0x42bbf0 [BODY] 16 insns, callees: (none)
    0x42bbf0: push     rbp
    0x42bbf1: push     r15
    0x42bbf3: push     r14
    0x42bbf5: push     r13
    0x42bbf7: push     r12
    0x42bbf9: push     rbx
    0x42bbfa: sub      rsp, 0x48
    0x42bbfe: mov      qword ptr [rsp], rsi
    0x42bc02: mov      rbx, qword ptr [rsi + 0x10]
    0x42bc06: mov      qword ptr [rsp + 0x20], rdx
    0x42bc0b: mov      rbp, qword ptr [rdx + 0x10]
    0x42bc0f: lea      r14, [rbx + rbp]
    ... +4 more instructions

; --- Block 0x42bc25 [BODY] 4 insns, callees: (none)
    0x42bc25: xor      r13d, r13d
    0x42bc28: mov      rdi, r13
    0x42bc2b: mov      rsi, r12
    0x42bc2e: call     qword ptr [rip + 0x597e4]

; --- Block 0x42bc28 [LOOP_HEADER] 3 insns, callees: (none)
    0x42bc28: mov      rdi, r13
    0x42bc2b: mov      rsi, r12
    0x42bc2e: call     qword ptr [rip + 0x597e4]

; --- Block 0x42bc39 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42bc39: mov      qword ptr [rsp + 0x40], rdi
    0x42bc3e: test     r14, r14
    0x42bc41: je       0x42bc6c

; --- Block 0x42bc43 [BODY] 2 insns, callees: (none)
    0x42bc43: lea      r12, [r14*8]
    0x42bc4b: call     qword ptr [rip + 0x59797]

; --- Block 0x42bc51 [BODY] 4 insns, callees: (none)
    0x42bc51: mov      r13d, 8
    0x42bc57: mov      esi, 8
    0x42bc5c: mov      rdi, r12
    0x42bc5f: call     qword ptr [rip + 0x5978b]

; --- Block 0x42bc65 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42bc65: test     rax, rax
    0x42bc68: jne      0x42bc71

; --- Block 0x42bc6a [BODY] 1 insns, callees: (none)
    0x42bc6a: jmp      0x42bc28

; --- Block 0x42bc6c [BODY] 7 insns, callees: (none)
    0x42bc6c: mov      eax, 8
    0x42bc71: mov      qword ptr [rsp + 8], r14
    0x42bc76: mov      qword ptr [rsp + 0x10], rax
    0x42bc7b: mov      qword ptr [rsp + 0x18], 0
    0x42bc84: test     rbx, rbx
    0x42bc87: mov      qword ptr [rsp + 0x30], rbp
    0x42bc8c: je       0x42bd95

; --- Block 0x42bc71 [BODY] 6 insns, callees: (none)
    0x42bc71: mov      qword ptr [rsp + 8], r14
    0x42bc76: mov      qword ptr [rsp + 0x10], rax
    0x42bc7b: mov      qword ptr [rsp + 0x18], 0
    0x42bc84: test     rbx, rbx
    0x42bc87: mov      qword ptr [rsp + 0x30], rbp
    0x42bc8c: je       0x42bd95

; --- Block 0x42bc92 [BODY] 11 insns, callees: (none)
    0x42bc92: mov      rax, qword ptr [rsp]
    0x42bc96: mov      rax, qword ptr [rax + 8]
    0x42bc9a: mov      qword ptr [rsp + 0x38], rax
    0x42bc9f: mov      rax, qword ptr [rsp + 0x20]
    0x42bca4: mov      rax, qword ptr [rax + 8]
    0x42bca8: mov      qword ptr [rsp + 0x28], rax
    0x42bcad: xor      r13d, r13d
    0x42bcb0: xor      r12d, r12d
    0x42bcb3: xor      r15d, r15d
    0x42bcb6: mov      r14, rbx
    0x42bcb9: jmp      0x42bce5

; --- Block 0x42bcc0 [LOOP_HEADER] 10 insns, callees: (none)
    0x42bcc0: mov      rax, qword ptr [rsp + 0x10]
    0x42bcc5: mov      qword ptr [rax + r13*8], rbx
    0x42bcc9: lea      rax, [r13 + 1]
    0x42bccd: mov      qword ptr [rsp + 0x18], rax
    0x42bcd2: inc      r15
    0x42bcd5: mov      rbp, qword ptr [rsp + 0x30]
    0x42bcda: inc      r13
    0x42bcdd: mov      rbx, r14
    0x42bce0: cmp      r12, r14
    0x42bce3: jae      0x42bd46

; --- Block 0x42bcd5 [LOOP_HEADER] 5 insns, callees: (none)
    0x42bcd5: mov      rbp, qword ptr [rsp + 0x30]
    0x42bcda: inc      r13
    0x42bcdd: mov      rbx, r14
    0x42bce0: cmp      r12, r14
    0x42bce3: jae      0x42bd46

; --- Block 0x42bce5 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42bce5: cmp      r15, rbp
    0x42bce8: jae      0x42bd46

; --- Block 0x42bcea [BODY] 7 insns, callees: (none)
    0x42bcea: mov      rax, qword ptr [rsp + 0x38]
    0x42bcef: mov      rbp, qword ptr [rax + r12*8]
    0x42bcf3: mov      rax, qword ptr [rsp + 0x28]
    0x42bcf8: mov      rbx, qword ptr [rax + r15*8]
    0x42bcfc: mov      rax, qword ptr [rsp + 8]
    0x42bd01: cmp      rbp, rbx
    0x42bd04: jbe      0x42bd20

; --- Block 0x42bd06 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42bd06: cmp      r13, rax
    0x42bd09: jne      0x42bcc0

; --- Block 0x42bd0b [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x42bd0b: lea      rdi, [rsp + 8]
    0x42bd10: call     0x43fe40

; --- Block 0x42bd15 [BODY] 1 insns, callees: (none)
    0x42bd15: jmp      0x42bcc0

; --- Block 0x42bd20 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42bd20: cmp      r13, rax
    0x42bd23: jne      0x42bd2f

; --- Block 0x42bd25 [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x42bd25: lea      rdi, [rsp + 8]
    0x42bd2a: call     0x43fe40

; --- Block 0x42bd2f [BODY] 6 insns, callees: (none)
    0x42bd2f: mov      rax, qword ptr [rsp + 0x10]
    0x42bd34: mov      qword ptr [rax + r13*8], rbp
    0x42bd38: lea      rax, [r13 + 1]
    0x42bd3c: mov      qword ptr [rsp + 0x18], rax
    0x42bd41: inc      r12
    0x42bd44: jmp      0x42bcd5

; --- Block 0x42bd46 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42bd46: cmp      r12, rbx
    0x42bd49: jae      0x42bda2

; --- Block 0x42bd4b [BODY] 4 insns, callees: (none)
    0x42bd4b: lea      rax, [rbx + r13]
    0x42bd4f: sub      rax, r12
    0x42bd52: mov      qword ptr [rsp + 0x28], rax
    0x42bd57: jmp      0x42bd79

; --- Block 0x42bd60 [LOOP_HEADER] 7 insns, callees: (none)
    0x42bd60: mov      rax, qword ptr [rsp + 0x10]
    0x42bd65: mov      qword ptr [rax + r13*8], rbx
    0x42bd69: inc      r13
    0x42bd6c: mov      qword ptr [rsp + 0x18], r13
    0x42bd71: inc      r12
    0x42bd74: cmp      r14, r12
    0x42bd77: je       0x42bd9d

; --- Block 0x42bd79 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42bd79: mov      rax, qword ptr [rsp + 0x38]
    0x42bd7e: mov      rbx, qword ptr [rax + r12*8]
    0x42bd82: cmp      r13, qword ptr [rsp + 8]
    0x42bd87: jne      0x42bd60

; --- Block 0x42bd89 [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x42bd89: lea      rdi, [rsp + 8]
    0x42bd8e: call     0x43fe40

; --- Block 0x42bd93 [BODY] 1 insns, callees: (none)
    0x42bd93: jmp      0x42bd60

; --- Block 0x42bd95 [BODY] 3 insns, callees: (none)
    0x42bd95: xor      r15d, r15d
    0x42bd98: xor      r13d, r13d
    0x42bd9b: jmp      0x42bda2

; --- Block 0x42bd9d [BODY] 5 insns, callees: (none)
    0x42bd9d: mov      r13, qword ptr [rsp + 0x28]
    0x42bda2: mov      rbx, qword ptr [rsp]
    0x42bda6: cmp      r15, rbp
    0x42bda9: mov      r8, qword ptr [rsp + 0x20]
    0x42bdae: jae      0x42be0c

; --- Block 0x42bda2 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42bda2: mov      rbx, qword ptr [rsp]
    0x42bda6: cmp      r15, rbp
    0x42bda9: mov      r8, qword ptr [rsp + 0x20]
    0x42bdae: jae      0x42be0c

; --- Block 0x42bdb0 [BODY] 6 insns, callees: (none)
    0x42bdb0: mov      r14, qword ptr [r8 + 8]
    0x42bdb4: mov      rbx, r13
    0x42bdb7: add      rbx, rbp
    0x42bdba: sub      rbx, r15
    0x42bdbd: lea      r12, [rsp + 8]
    0x42bdc2: jmp      0x42bdeb

; --- Block 0x42bdd0 [LOOP_HEADER] 7 insns, callees: (none)
    0x42bdd0: mov      rax, qword ptr [rsp + 0x10]
    0x42bdd5: mov      qword ptr [rax + r13*8], rbp
    0x42bdd9: inc      r13
    0x42bddc: mov      qword ptr [rsp + 0x18], r13
    0x42bde1: inc      r15
    0x42bde4: cmp      qword ptr [rsp + 0x30], r15
    0x42bde9: je       0x42be00

; --- Block 0x42bdeb [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42bdeb: mov      rbp, qword ptr [r14 + r15*8]
    0x42bdef: cmp      r13, qword ptr [rsp + 8]
    0x42bdf4: jne      0x42bdd0

; --- Block 0x42bdf6 [BODY] 2 insns, callees: alloc::raw_vec::RawVec<T,A>::grow_one
    0x42bdf6: mov      rdi, r12
    0x42bdf9: call     0x43fe40

; --- Block 0x42bdfe [BODY] 1 insns, callees: (none)
    0x42bdfe: jmp      0x42bdd0

; --- Block 0x42be00 [BODY] 5 insns, callees: (none)
    0x42be00: mov      r13, rbx
    0x42be03: mov      rbx, qword ptr [rsp]
    0x42be07: mov      r8, qword ptr [rsp + 0x20]
    0x42be0c: test     r13, r13
    0x42be0f: je       0x42be46

; --- Block 0x42be0c [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42be0c: test     r13, r13
    0x42be0f: je       0x42be46

; --- Block 0x42be11 [BODY] 6 insns, callees: (none)
    0x42be11: xor      edi, edi
    0x42be13: xor      eax, eax
    0x42be15: nop      word ptr cs:[rax + rax]
    0x42be20: mov      rsi, qword ptr [rsp + 0x18]
    0x42be25: cmp      rdi, rsi
    0x42be28: jae      0x42bea5

; --- Block 0x42be20 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42be20: mov      rsi, qword ptr [rsp + 0x18]
    0x42be25: cmp      rdi, rsi
    0x42be28: jae      0x42bea5

; --- Block 0x42be2a [BODY] 8 insns, callees: (none)
    0x42be2a: mov      rcx, qword ptr [rsp + 0x10]
    0x42be2f: mov      rdx, qword ptr [rcx + rdi*8]
    0x42be33: cmp      rdx, rax
    0x42be36: cmova    rax, rdx
    0x42be3a: mov      qword ptr [rcx + rdi*8], rax
    0x42be3e: inc      rdi
    0x42be41: cmp      r13, rdi
    0x42be44: jne      0x42be20

; --- Block 0x42be46 [BODY] 8 insns, callees: (none)
    0x42be46: mov      rax, qword ptr [rsp + 0x18]
    0x42be4b: mov      r14, qword ptr [rsp + 0x40]
    0x42be50: mov      qword ptr [r14 + 0x10], rax
    0x42be54: movups   xmm0, xmmword ptr [rsp + 8]
    0x42be59: movups   xmmword ptr [r14], xmm0
    0x42be5d: mov      rsi, qword ptr [r8]
    0x42be60: test     rsi, rsi
    0x42be63: je       0x42be78

; --- Block 0x42be65 [BODY] 4 insns, callees: (none)
    0x42be65: shl      rsi, 3
    0x42be69: mov      rdi, qword ptr [r8 + 8]
    0x42be6d: mov      edx, 8
    0x42be72: call     qword ptr [rip + 0x595b0]

; --- Block 0x42be78 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42be78: mov      rsi, qword ptr [rbx]
    0x42be7b: test     rsi, rsi
    0x42be7e: je       0x42be93

; --- Block 0x42be80 [BODY] 4 insns, callees: (none)
    0x42be80: shl      rsi, 3
    0x42be84: mov      rdi, qword ptr [rbx + 8]
    0x42be88: mov      edx, 8
    0x42be8d: call     qword ptr [rip + 0x59595]

; --- Block 0x42be93 [BODY] 9 insns, callees: (none)
    0x42be93: mov      rax, r14
    0x42be96: add      rsp, 0x48
    0x42be9a: pop      rbx
    0x42be9b: pop      r12
    0x42be9d: pop      r13
    0x42be9f: pop      r14
    0x42bea1: pop      r15
    0x42bea3: pop      rbp
    0x42bea4: ret      

; --- Block 0x42bea5 [BODY] 2 insns, callees: (none)
    0x42bea5: lea      rdx, [rip + 0x56cdc]
    0x42beac: call     qword ptr [rip + 0x5957e]

```

**Hungarian matching result** (mean similarity: 0.780):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4565a8` | BODY | `0x42bc6a` | BODY | 1.000 | GOOD |
| `0x456866` | BODY | `0x42bd15` | BODY | 1.000 | GOOD |
| `0x456948` | BODY | `0x42bd93` | BODY | 1.000 | GOOD |
| `0x4569a2` | BODY | `0x42bdfe` | BODY | 1.000 | GOOD |
| `0x4567c9` | LOOP_HEADER | `0x42bd0b` | BODY | 0.986 | GOOD |
| `0x4568ad` | BOUNDS_CHECK | `0x42bd79` | BOUNDS_CHECK | 0.986 | GOOD |
| `0x456890` | DROP_GLUE | `0x42bdf6` | BODY | 0.976 | GOOD |
| `0x45678c` | BODY | `0x42bc25` | BODY | 0.949 | GOOD |
| `0x4566c6` | BOUNDS_CHECK | `0x42bda2` | BOUNDS_CHECK | 0.947 | GOOD |
| `0x456570` | BODY | `0x42bdd0` | LOOP_HEADER | 0.937 | GOOD |
| `0x4567e2` | BODY | `0x42bcea` | BODY | 0.929 | GOOD |
| `0x45694a` | ITERATOR_STATE | `0x42bcd5` | LOOP_HEADER | 0.894 | GOOD |
| `0x456ada` | ITERATOR_STATE | `0x42bc71` | BODY | 0.892 | GOOD |
| `0x456a83` | ITERATOR_STATE | `0x42bd60` | LOOP_HEADER | 0.880 | GOOD |
| `0x456625` | BOUNDS_CHECK | `0x42be78` | BOUNDS_CHECK | 0.877 | GOOD |
| `0x45672b` | BOUNDS_CHECK | `0x42be20` | BOUNDS_CHECK | 0.877 | GOOD |
| `0x456688` | BOUNDS_CHECK | `0x42bd9d` | BODY | 0.876 | GOOD |
| `0x456a17` | BOUNDS_CHECK | `0x42be00` | BODY | 0.875 | GOOD |
| `0x4565d6` | LOOP_HEADER | `0x42bc28` | LOOP_HEADER | 0.866 | GOOD |
| `0x4569a4` | ITERATOR_STATE | `0x42be2a` | BODY | 0.805 | GOOD |
| `0x45690c` | BODY | `0x42bd4b` | BODY | 0.805 | GOOD |
| `0x456740` | BODY | `0x42bd25` | BODY | 0.756 | GOOD |
| `0x456559` | BODY | `0x42bea5` | BODY | 0.752 | GOOD |
| `0x456593` | BODY | `0x42bc43` | BODY | 0.745 | GOOD |
| `0x456975` | BODY | `0x42bd89` | BODY | 0.742 | GOOD |
| `0x45679d` | BODY | `0x42bdeb` | BOUNDS_CHECK | 0.735 | GOOD |
| `0x4567d6` | BODY | `0x42bc39` | BOUNDS_CHECK | 0.735 | GOOD |
| `0x456963` | BODY | `0x42bd95` | BODY | 0.732 | GOOD |
| `0x4567ac` | BODY | `0x42bd2f` | BODY | 0.731 | GOOD |
| `0x45683a` | DROP_GLUE | `0x42be46` | BODY | 0.720 | GOOD |
| `0x45680a` | BODY | `0x42bdb0` | BODY | 0.716 | GOOD |
| `0x45663a` | LOOP_HEADER | `0x42bc51` | BODY | 0.710 | GOOD |
| `0x4565be` | BODY | `0x42be11` | BODY | 0.706 | GOOD |
| `0x456527` | BODY | `0x42be0c` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x456566` | BODY | `0x42bd20` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x4565f3` | BODY | `0x42bd46` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x456657` | BODY | `0x42bd06` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x45667e` | BODY | `0x42bce5` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x4566b9` | BODY | `0x42bc65` | BOUNDS_CHECK | 0.653 | PARTIAL |
| `0x456661` | BODY | `0x42be65` | BODY | 0.632 | PARTIAL |
| `0x4566db` | LOOP_HEADER | `0x42be80` | BODY | 0.632 | PARTIAL |
| `0x45691e` | BODY | `0x42bc92` | BODY | 0.626 | PARTIAL |
| `0x4568bf` | LOOP_HEADER | `0x42bcc0` | LOOP_HEADER | 0.539 | PARTIAL |
| `0x4569e4` | BODY | `0x42bc6c` | BODY | 0.514 | PARTIAL |
| `0x45689d` | EPILOGUE | `0x42be93` | BODY | 0.475 | PARTIAL |
| `0x4564f0` | BODY | `0x42bbf0` | BODY | 0.384 | POOR |
| `0x4565aa` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45669d` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4566f8` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456702` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45671e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456759` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456763` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45677f` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456833` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4568e5` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4568ec` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456905` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456930` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45698a` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4569bd` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4569cf` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a10` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a26` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a42` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a49` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a65` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a6c` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a81` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456a9c` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456aae` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456ac3` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456ad8` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456af2` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456b03` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `own_05` — O0: 21 blocks, O2: 25 blocks

**O0 blocks** (21 total):

```asm
; --- Block 0x403925 [BODY] 14 insns, callees: sub_4010f0
    0x403925: push     rbp
    0x403926: mov      rbp, rsp
    0x403929: sub      rsp, 0x60
    0x40392d: mov      qword ptr [rbp - 0x38], rdi
    0x403931: mov      qword ptr [rbp - 0x40], rsi
    0x403935: mov      qword ptr [rbp - 0x48], rdx
    0x403939: mov      qword ptr [rbp - 0x50], rcx
    0x40393d: mov      qword ptr [rbp - 0x58], r8
    0x403941: mov      rdx, qword ptr [rbp - 0x40]
    0x403945: mov      rax, qword ptr [rbp - 0x50]
    0x403949: add      rax, rdx
    0x40394c: shl      rax, 3
    ... +2 more instructions

; --- Block 0x403958 [BODY] 5 insns, callees: (none)
    0x403958: mov      qword ptr [rbp - 0x30], rax
    0x40395c: mov      qword ptr [rbp - 8], 0
    0x403964: mov      qword ptr [rbp - 0x10], 0
    0x40396c: mov      qword ptr [rbp - 0x18], 0
    0x403974: jmp      0x403a26

; --- Block 0x403979 [LOOP_HEADER] 12 insns, callees: (none)
    0x403979: mov      rax, qword ptr [rbp - 8]
    0x40397d: lea      rdx, [rax*8]
    0x403985: mov      rax, qword ptr [rbp - 0x38]
    0x403989: add      rax, rdx
    0x40398c: mov      rdx, qword ptr [rax]
    0x40398f: mov      rax, qword ptr [rbp - 0x10]
    0x403993: lea      rcx, [rax*8]
    0x40399b: mov      rax, qword ptr [rbp - 0x48]
    0x40399f: add      rax, rcx
    0x4039a2: mov      rax, qword ptr [rax]
    0x4039a5: cmp      rdx, rax
    0x4039a8: ja       0x4039e9

; --- Block 0x4039aa [BODY] 15 insns, callees: (none)
    0x4039aa: mov      rax, qword ptr [rbp - 8]
    0x4039ae: lea      rdx, [rax + 1]
    0x4039b2: mov      qword ptr [rbp - 8], rdx
    0x4039b6: lea      rdx, [rax*8]
    0x4039be: mov      rax, qword ptr [rbp - 0x38]
    0x4039c2: lea      rcx, [rdx + rax]
    0x4039c6: mov      rax, qword ptr [rbp - 0x18]
    0x4039ca: lea      rdx, [rax + 1]
    0x4039ce: mov      qword ptr [rbp - 0x18], rdx
    0x4039d2: lea      rdx, [rax*8]
    0x4039da: mov      rax, qword ptr [rbp - 0x30]
    0x4039de: add      rdx, rax
    ... +3 more instructions

; --- Block 0x4039e9 [BODY] 17 insns, callees: (none)
    0x4039e9: mov      rax, qword ptr [rbp - 0x10]
    0x4039ed: lea      rdx, [rax + 1]
    0x4039f1: mov      qword ptr [rbp - 0x10], rdx
    0x4039f5: lea      rdx, [rax*8]
    0x4039fd: mov      rax, qword ptr [rbp - 0x48]
    0x403a01: lea      rcx, [rdx + rax]
    0x403a05: mov      rax, qword ptr [rbp - 0x18]
    0x403a09: lea      rdx, [rax + 1]
    0x403a0d: mov      qword ptr [rbp - 0x18], rdx
    0x403a11: lea      rdx, [rax*8]
    0x403a19: mov      rax, qword ptr [rbp - 0x30]
    0x403a1d: add      rdx, rax
    ... +5 more instructions

; --- Block 0x403a26 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403a26: mov      rax, qword ptr [rbp - 8]
    0x403a2a: cmp      rax, qword ptr [rbp - 0x40]
    0x403a2e: jae      0x403a7d

; --- Block 0x403a30 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403a30: mov      rax, qword ptr [rbp - 0x10]
    0x403a34: cmp      rax, qword ptr [rbp - 0x50]
    0x403a38: jb       0x403979

; --- Block 0x403a3e [BODY] 1 insns, callees: (none)
    0x403a3e: jmp      0x403a7d

; --- Block 0x403a40 [LOOP_HEADER] 17 insns, callees: (none)
    0x403a40: mov      rax, qword ptr [rbp - 8]
    0x403a44: lea      rdx, [rax + 1]
    0x403a48: mov      qword ptr [rbp - 8], rdx
    0x403a4c: lea      rdx, [rax*8]
    0x403a54: mov      rax, qword ptr [rbp - 0x38]
    0x403a58: lea      rcx, [rdx + rax]
    0x403a5c: mov      rax, qword ptr [rbp - 0x18]
    0x403a60: lea      rdx, [rax + 1]
    0x403a64: mov      qword ptr [rbp - 0x18], rdx
    0x403a68: lea      rdx, [rax*8]
    0x403a70: mov      rax, qword ptr [rbp - 0x30]
    0x403a74: add      rdx, rax
    ... +5 more instructions

; --- Block 0x403a7d [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403a7d: mov      rax, qword ptr [rbp - 8]
    0x403a81: cmp      rax, qword ptr [rbp - 0x40]
    0x403a85: jb       0x403a40

; --- Block 0x403a87 [BODY] 1 insns, callees: (none)
    0x403a87: jmp      0x403ac6

; --- Block 0x403a89 [LOOP_HEADER] 17 insns, callees: (none)
    0x403a89: mov      rax, qword ptr [rbp - 0x10]
    0x403a8d: lea      rdx, [rax + 1]
    0x403a91: mov      qword ptr [rbp - 0x10], rdx
    0x403a95: lea      rdx, [rax*8]
    0x403a9d: mov      rax, qword ptr [rbp - 0x48]
    0x403aa1: lea      rcx, [rdx + rax]
    0x403aa5: mov      rax, qword ptr [rbp - 0x18]
    0x403aa9: lea      rdx, [rax + 1]
    0x403aad: mov      qword ptr [rbp - 0x18], rdx
    0x403ab1: lea      rdx, [rax*8]
    0x403ab9: mov      rax, qword ptr [rbp - 0x30]
    0x403abd: add      rdx, rax
    ... +5 more instructions

; --- Block 0x403ac6 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403ac6: mov      rax, qword ptr [rbp - 0x10]
    0x403aca: cmp      rax, qword ptr [rbp - 0x50]
    0x403ace: jb       0x403a89

; --- Block 0x403ad0 [BODY] 3 insns, callees: (none)
    0x403ad0: mov      qword ptr [rbp - 0x20], 0
    0x403ad8: mov      qword ptr [rbp - 0x28], 0
    0x403ae0: jmp      0x403b37

; --- Block 0x403ae2 [LOOP_HEADER] 7 insns, callees: (none)
    0x403ae2: mov      rax, qword ptr [rbp - 0x28]
    0x403ae6: lea      rdx, [rax*8]
    0x403aee: mov      rax, qword ptr [rbp - 0x30]
    0x403af2: add      rax, rdx
    0x403af5: mov      rax, qword ptr [rax]
    0x403af8: cmp      qword ptr [rbp - 0x20], rax
    0x403afc: jae      0x403b18

; --- Block 0x403afe [BODY] 16 insns, callees: (none)
    0x403afe: mov      rax, qword ptr [rbp - 0x28]
    0x403b02: lea      rdx, [rax*8]
    0x403b0a: mov      rax, qword ptr [rbp - 0x30]
    0x403b0e: add      rax, rdx
    0x403b11: mov      rax, qword ptr [rax]
    0x403b14: mov      qword ptr [rbp - 0x20], rax
    0x403b18: mov      rax, qword ptr [rbp - 0x28]
    0x403b1c: lea      rdx, [rax*8]
    0x403b24: mov      rax, qword ptr [rbp - 0x30]
    0x403b28: add      rdx, rax
    0x403b2b: mov      rax, qword ptr [rbp - 0x20]
    0x403b2f: mov      qword ptr [rdx], rax
    ... +4 more instructions

; --- Block 0x403b18 [BODY] 10 insns, callees: (none)
    0x403b18: mov      rax, qword ptr [rbp - 0x28]
    0x403b1c: lea      rdx, [rax*8]
    0x403b24: mov      rax, qword ptr [rbp - 0x30]
    0x403b28: add      rdx, rax
    0x403b2b: mov      rax, qword ptr [rbp - 0x20]
    0x403b2f: mov      qword ptr [rdx], rax
    0x403b32: add      qword ptr [rbp - 0x28], 1
    0x403b37: mov      rax, qword ptr [rbp - 0x28]
    0x403b3b: cmp      rax, qword ptr [rbp - 0x18]
    0x403b3f: jb       0x403ae2

; --- Block 0x403b37 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x403b37: mov      rax, qword ptr [rbp - 0x28]
    0x403b3b: cmp      rax, qword ptr [rbp - 0x18]
    0x403b3f: jb       0x403ae2

; --- Block 0x403b41 [BODY] 3 insns, callees: sub_401030
    0x403b41: mov      rax, qword ptr [rbp - 0x38]
    0x403b45: mov      rdi, rax
    0x403b48: call     0x401030

; --- Block 0x403b4d [BODY] 3 insns, callees: sub_401030
    0x403b4d: mov      rax, qword ptr [rbp - 0x48]
    0x403b51: mov      rdi, rax
    0x403b54: call     0x401030

; --- Block 0x403b59 [BODY] 6 insns, callees: (none)
    0x403b59: mov      rax, qword ptr [rbp - 0x58]
    0x403b5d: mov      rdx, qword ptr [rbp - 0x18]
    0x403b61: mov      qword ptr [rax], rdx
    0x403b64: mov      rax, qword ptr [rbp - 0x30]
    0x403b68: leave    
    0x403b69: ret      

```

**O2 blocks** (25 total):

```asm
; --- Block 0x404bf0 [BODY] 18 insns, callees: sub_401100
    0x404bf0: push     r15
    0x404bf2: mov      r15, rdx
    0x404bf5: push     r14
    0x404bf7: mov      r14, rdi
    0x404bfa: lea      rdi, [rsi + rcx]
    0x404bfe: push     r13
    0x404c00: shl      rdi, 3
    0x404c04: push     r12
    0x404c06: xor      r12d, r12d
    0x404c09: push     rbp
    0x404c0a: xor      ebp, ebp
    0x404c0c: push     rbx
    ... +6 more instructions

; --- Block 0x404c26 [BODY] 5 insns, callees: (none)
    0x404c26: mov      r9, qword ptr [rsp + 8]
    0x404c2b: mov      rcx, qword ptr [rsp + 0x10]
    0x404c30: mov      r13, rax
    0x404c33: test     r9, r9
    0x404c36: je       0x404d90

; --- Block 0x404c3c [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404c3c: test     rcx, rcx
    0x404c3f: jne      0x404c63

; --- Block 0x404c41 [BODY] 1 insns, callees: (none)
    0x404c41: jmp      0x404d90

; --- Block 0x404c50 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x404c50: add      r12, 1
    0x404c54: mov      qword ptr [r13 + rbx*8 - 8], rax
    0x404c59: cmp      r12, r9
    0x404c5c: jae      0x404c85

; --- Block 0x404c5e [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404c5e: cmp      rcx, rbp
    0x404c61: jbe      0x404c90

; --- Block 0x404c63 [ITERATOR_STATE] 5 insns, callees: (none)
    0x404c63: mov      rax, qword ptr [r14 + r12*8]
    0x404c67: mov      rdx, qword ptr [r15 + rbp*8]
    0x404c6b: add      rbx, 1
    0x404c6f: cmp      rax, rdx
    0x404c72: jbe      0x404c50

; --- Block 0x404c74 [ITERATOR_STATE] 5 insns, callees: (none)
    0x404c74: mov      rax, rdx
    0x404c77: add      rbp, 1
    0x404c7b: mov      qword ptr [r13 + rbx*8 - 8], rax
    0x404c80: cmp      r12, r9
    0x404c83: jb       0x404c5e

; --- Block 0x404c85 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404c85: cmp      rcx, rbp
    0x404c88: ja       0x404cf6

; --- Block 0x404c8a [BODY] 1 insns, callees: (none)
    0x404c8a: jmp      0x404d42

; --- Block 0x404c90 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404c90: cmp      r12, r9
    0x404c93: jae      0x404c85

; --- Block 0x404c95 [LOOP_HEADER] 13 insns, callees: sub_4010f0
    0x404c95: mov      rdx, r9
    0x404c98: lea      r10, [r12 + 1]
    0x404c9d: mov      eax, 8
    0x404ca2: mov      qword ptr [rsp + 0x18], rcx
    0x404ca7: sub      rdx, r12
    0x404caa: lea      rdi, [r13 + rbx*8]
    0x404caf: lea      rsi, [r14 + r12*8]
    0x404cb3: mov      qword ptr [rsp + 0x10], r10
    0x404cb8: shl      rdx, 3
    0x404cbc: cmp      r9, r10
    0x404cbf: mov      qword ptr [rsp + 8], r9
    0x404cc4: cmovb    rdx, rax
    ... +1 more instructions

; --- Block 0x404ccd [BODY] 11 insns, callees: (none)
    0x404ccd: mov      r9, qword ptr [rsp + 8]
    0x404cd2: mov      r10, qword ptr [rsp + 0x10]
    0x404cd7: xor      edx, edx
    0x404cd9: mov      rcx, qword ptr [rsp + 0x18]
    0x404cde: lea      rax, [r9 - 1]
    0x404ce2: sub      rax, r12
    0x404ce5: cmp      r9, r10
    0x404ce8: cmovb    rax, rdx
    0x404cec: lea      rbx, [rbx + rax + 1]
    0x404cf1: cmp      rbp, rcx
    0x404cf4: jae      0x404d3d

; --- Block 0x404cf6 [LOOP_HEADER] 11 insns, callees: sub_4010f0
    0x404cf6: mov      rdx, rcx
    0x404cf9: lea      r12, [rbp + 1]
    0x404cfd: lea      rsi, [r15 + rbp*8]
    0x404d01: mov      eax, 8
    0x404d06: sub      rdx, rbp
    0x404d09: lea      rdi, [r13 + rbx*8]
    0x404d0e: mov      qword ptr [rsp + 8], rcx
    0x404d13: shl      rdx, 3
    0x404d17: cmp      r12, rcx
    0x404d1a: cmova    rdx, rax
    0x404d1e: call     0x4010f0

; --- Block 0x404d23 [BODY] 9 insns, callees: (none)
    0x404d23: mov      rcx, qword ptr [rsp + 8]
    0x404d28: xor      edx, edx
    0x404d2a: lea      rax, [rcx - 1]
    0x404d2e: sub      rax, rbp
    0x404d31: cmp      r12, rcx
    0x404d34: cmova    rax, rdx
    0x404d38: lea      rbx, [rbx + rax + 1]
    0x404d3d: test     rbx, rbx
    0x404d40: je       0x404da8

; --- Block 0x404d3d [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404d3d: test     rbx, rbx
    0x404d40: je       0x404da8

; --- Block 0x404d42 [BODY] 11 insns, callees: (none)
    0x404d42: mov      rax, r13
    0x404d45: lea      rsi, [r13 + rbx*8]
    0x404d4a: xor      edx, edx
    0x404d4c: nop      dword ptr [rax]
    0x404d50: mov      rcx, qword ptr [rax]
    0x404d53: cmp      rdx, rcx
    0x404d56: cmovb    rdx, rcx
    0x404d5a: add      rax, 8
    0x404d5e: mov      qword ptr [rax - 8], rdx
    0x404d62: cmp      rsi, rax
    0x404d65: jne      0x404d50

; --- Block 0x404d50 [BODY] 7 insns, callees: (none)
    0x404d50: mov      rcx, qword ptr [rax]
    0x404d53: cmp      rdx, rcx
    0x404d56: cmovb    rdx, rcx
    0x404d5a: add      rax, 8
    0x404d5e: mov      qword ptr [rax - 8], rdx
    0x404d62: cmp      rsi, rax
    0x404d65: jne      0x404d50

; --- Block 0x404d67 [LOOP_HEADER] 2 insns, callees: sub_401030
    0x404d67: mov      rdi, r14
    0x404d6a: call     0x401030

; --- Block 0x404d6f [BODY] 2 insns, callees: sub_401030
    0x404d6f: mov      rdi, r15
    0x404d72: call     0x401030

; --- Block 0x404d77 [BODY] 11 insns, callees: (none)
    0x404d77: mov      rax, qword ptr [rsp]
    0x404d7b: mov      qword ptr [rax], rbx
    0x404d7e: add      rsp, 0x28
    0x404d82: mov      rax, r13
    0x404d85: pop      rbx
    0x404d86: pop      rbp
    0x404d87: pop      r12
    0x404d89: pop      r13
    0x404d8b: pop      r14
    0x404d8d: pop      r15
    0x404d8f: ret      

; --- Block 0x404d90 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404d90: test     r9, r9
    0x404d93: jne      0x404c95

; --- Block 0x404d99 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404d99: test     rcx, rcx
    0x404d9c: jne      0x404cf6

; --- Block 0x404da2 [PROLOGUE] 1 insns, callees: (none)
    0x404da2: nop      word ptr [rax + rax]

; --- Block 0x404da8 [BODY] 2 insns, callees: (none)
    0x404da8: xor      ebx, ebx
    0x404daa: jmp      0x404d67

```

**Hungarian matching result** (mean similarity: 0.720):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x403a3e` | BODY | `0x404c41` | BODY | 1.000 | GOOD |
| `0x403a87` | BODY | `0x404c8a` | BODY | 1.000 | GOOD |
| `0x403b41` | BODY | `0x404d6f` | BODY | 0.895 | GOOD |
| `0x403b4d` | BODY | `0x404d67` | LOOP_HEADER | 0.888 | GOOD |
| `0x403ae2` | LOOP_HEADER | `0x404c74` | ITERATOR_STATE | 0.809 | GOOD |
| `0x403a26` | BOUNDS_CHECK | `0x404c85` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x403a30` | BOUNDS_CHECK | `0x404c5e` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x403a7d` | BOUNDS_CHECK | `0x404c3c` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x403ac6` | BOUNDS_CHECK | `0x404c90` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x403b37` | BOUNDS_CHECK | `0x404d3d` | BOUNDS_CHECK | 0.751 | GOOD |
| `0x403b18` | BODY | `0x404d23` | BODY | 0.734 | GOOD |
| `0x403979` | LOOP_HEADER | `0x404ccd` | BODY | 0.722 | GOOD |
| `0x403958` | BODY | `0x404c26` | BODY | 0.703 | GOOD |
| `0x4039e9` | BODY | `0x404c63` | ITERATOR_STATE | 0.670 | PARTIAL |
| `0x403afe` | BODY | `0x404c50` | BOUNDS_CHECK | 0.643 | PARTIAL |
| `0x403925` | BODY | `0x404c95` | LOOP_HEADER | 0.641 | PARTIAL |
| `0x403ad0` | BODY | `0x404da8` | BODY | 0.641 | PARTIAL |
| `0x403a89` | LOOP_HEADER | `0x404d42` | BODY | 0.552 | PARTIAL |
| `0x403b59` | BODY | `0x404da2` | PROLOGUE | 0.520 | PARTIAL |
| `0x403a40` | LOOP_HEADER | `0x404d50` | BODY | 0.487 | PARTIAL |
| `0x4039aa` | BODY | `0x404d77` | BODY | 0.457 | PARTIAL |
| — | — | `0x404bf0` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x404cf6` | LOOP_HEADER | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x404d90` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x404d99` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |

---

## Function `own_03`

### Rust `own_03` — O0: 53 blocks, O2: 55 blocks

**O0 blocks** (53 total):

```asm
; --- Block 0x455cb0 [BODY] 10 insns, callees: <alloc::string::String as core::ops::deref::Deref>::deref
    0x455cb0: sub      rsp, 0x218
    0x455cb7: mov      qword ptr [rsp + 0x80], rdx
    0x455cbf: mov      qword ptr [rsp + 0x88], rsi
    0x455cc7: mov      rax, rdi
    0x455cca: mov      rdi, qword ptr [rsp + 0x88]
    0x455cd2: mov      qword ptr [rsp + 0x90], rax
    0x455cda: mov      qword ptr [rsp + 0x98], rax
    0x455ce2: mov      qword ptr [rsp + 0x1d8], rdx
    0x455cea: mov      byte ptr [rsp + 0x1d7], 0
    0x455cf2: call     0x470690

; --- Block 0x455cf7 [BODY] 3 insns, callees: (none)
    0x455cf7: mov      qword ptr [rsp + 0xa0], rdx
    0x455cff: mov      qword ptr [rsp + 0xa8], rax
    0x455d07: jmp      0x455d31

; --- Block 0x455d31 [BODY] 4 insns, callees: core::str::<impl str>::split_whitespace
    0x455d31: mov      rdx, qword ptr [rsp + 0xa0]
    0x455d39: mov      rsi, qword ptr [rsp + 0xa8]
    0x455d41: lea      rdi, [rsp + 0x108]
    0x455d49: call     0x4713f0

; --- Block 0x455d4e [BODY] 1 insns, callees: (none)
    0x455d4e: jmp      0x455d50

; --- Block 0x455d50 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::map
    0x455d50: lea      rdi, [rsp + 0xc8]
    0x455d58: lea      rsi, [rsp + 0x108]
    0x455d60: call     0x4936b0

; --- Block 0x455d65 [BODY] 1 insns, callees: (none)
    0x455d65: jmp      0x455d67

; --- Block 0x455d67 [BODY] 3 insns, callees: core::iter::traits::iterator::Iterator::collect
    0x455d67: lea      rdi, [rsp + 0xb0]
    0x455d6f: lea      rsi, [rsp + 0xc8]
    0x455d77: call     0x487a70

; --- Block 0x455d7c [BODY] 1 insns, callees: (none)
    0x455d7c: jmp      0x455d7e

; --- Block 0x455d7e [BODY] 2 insns, callees: alloc::vec::Vec<T,A>::len
    0x455d7e: lea      rdi, [rsp + 0xb0]
    0x455d86: call     0x4a8e80

; --- Block 0x455d8b [BODY] 2 insns, callees: (none)
    0x455d8b: mov      qword ptr [rsp + 0x78], rax
    0x455d90: jmp      0x455dba

; --- Block 0x455dba [BODY] 3 insns, callees: alloc::vec::Vec<T>::with_capacity
    0x455dba: mov      rsi, qword ptr [rsp + 0x78]
    0x455dbf: lea      rdi, [rsp + 0x148]
    0x455dc7: call     0x4a5070

; --- Block 0x455dcc [BODY] 1 insns, callees: (none)
    0x455dcc: jmp      0x455dce

; --- Block 0x455dce [BODY] 2 insns, callees: <&alloc::vec::Vec<T,A> as core::iter::traits::collect::IntoIterator>::into_iter
    0x455dce: lea      rdi, [rsp + 0xb0]
    0x455dd6: call     0x4ac120

; --- Block 0x455ddb [BODY] 3 insns, callees: (none)
    0x455ddb: mov      qword ptr [rsp + 0x68], rdx
    0x455de0: mov      qword ptr [rsp + 0x70], rax
    0x455de5: jmp      0x455e0c

; --- Block 0x455e0c [BODY] 6 insns, callees: <core::slice::iter::Iter<T> as core::iter::traits::iterator::Iterator>::next
    0x455e0c: mov      rax, qword ptr [rsp + 0x68]
    0x455e11: mov      rcx, qword ptr [rsp + 0x70]
    0x455e16: mov      qword ptr [rsp + 0x160], rcx
    0x455e1e: mov      qword ptr [rsp + 0x168], rax
    0x455e26: lea      rdi, [rsp + 0x160]
    0x455e2e: call     0x484710

; --- Block 0x455e26 [LOOP_HEADER] 2 insns, callees: <core::slice::iter::Iter<T> as core::iter::traits::iterator::Iterator>::next
    0x455e26: lea      rdi, [rsp + 0x160]
    0x455e2e: call     0x484710

; --- Block 0x455e33 [BODY] 2 insns, callees: (none)
    0x455e33: mov      qword ptr [rsp + 0x60], rax
    0x455e38: jmp      0x455e3a

; --- Block 0x455e3a [BODY] 9 insns, callees: (none)
    0x455e3a: mov      rax, qword ptr [rsp + 0x60]
    0x455e3f: mov      qword ptr [rsp + 0x170], rax
    0x455e47: mov      rdx, qword ptr [rsp + 0x170]
    0x455e4f: mov      eax, 1
    0x455e54: xor      ecx, ecx
    0x455e56: cmp      rdx, 0
    0x455e5a: cmove    rax, rcx
    0x455e5e: test     rax, 1
    0x455e64: je       0x455e87

; --- Block 0x455e66 [BODY] 3 insns, callees: alloc::string::String::as_bytes
    0x455e66: mov      rdi, qword ptr [rsp + 0x170]
    0x455e6e: mov      qword ptr [rsp + 0x1f0], rdi
    0x455e76: call     0x470570

; --- Block 0x455e7b [BODY] 3 insns, callees: (none)
    0x455e7b: mov      qword ptr [rsp + 0x50], rdx
    0x455e80: mov      qword ptr [rsp + 0x58], rax
    0x455e85: jmp      0x455f01

; --- Block 0x455e87 [BODY] 2 insns, callees: <alloc::vec::Vec<T,A> as core::ops::deref::Deref>::deref
    0x455e87: lea      rdi, [rsp + 0x148]
    0x455e8f: call     0x4ab7e0

; --- Block 0x455e94 [BODY] 3 insns, callees: (none)
    0x455e94: mov      qword ptr [rsp + 0x40], rdx
    0x455e99: mov      qword ptr [rsp + 0x48], rax
    0x455e9e: jmp      0x455ea0

; --- Block 0x455ea0 [BODY] 6 insns, callees: alloc::slice::<impl [T]>::join
    0x455ea0: mov      rdx, qword ptr [rsp + 0x40]
    0x455ea5: mov      rsi, qword ptr [rsp + 0x48]
    0x455eaa: mov      rdi, qword ptr [rsp + 0x90]
    0x455eb2: lea      rcx, [rip - 0x4910b]
    0x455eb9: mov      r8d, 1
    0x455ebf: call     0x485d00

; --- Block 0x455ec4 [BODY] 1 insns, callees: (none)
    0x455ec4: jmp      0x455ec6

; --- Block 0x455ec6 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<alloc::string::String>>
    0x455ec6: lea      rdi, [rsp + 0x148]
    0x455ece: call     0x497130

; --- Block 0x455ed3 [BODY] 1 insns, callees: (none)
    0x455ed3: jmp      0x455ed5

; --- Block 0x455ed5 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::vec::Vec<alloc::string::String>>
    0x455ed5: lea      rdi, [rsp + 0xb0]
    0x455edd: call     0x497130

; --- Block 0x455ee2 [BODY] 1 insns, callees: (none)
    0x455ee2: jmp      0x455ee4

; --- Block 0x455ee4 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<alloc::string::String>
    0x455ee4: mov      rdi, qword ptr [rsp + 0x88]
    0x455eec: call     0x496520

; --- Block 0x455ef1 [EPILOGUE] 3 insns, callees: (none)
    0x455ef1: mov      rax, qword ptr [rsp + 0x98]
    0x455ef9: add      rsp, 0x218
    0x455f00: ret      

; --- Block 0x455f01 [BODY] 10 insns, callees: alloc::string::String::with_capacity
    0x455f01: mov      rsi, qword ptr [rsp + 0x50]
    0x455f06: mov      rax, qword ptr [rsp + 0x58]
    0x455f0b: mov      rcx, rax
    0x455f0e: mov      qword ptr [rsp + 0x30], rcx
    0x455f13: mov      rcx, rsi
    0x455f16: mov      qword ptr [rsp + 0x38], rcx
    0x455f1b: mov      qword ptr [rsp + 0x1f8], rax
    0x455f23: mov      qword ptr [rsp + 0x200], rsi
    0x455f2b: lea      rdi, [rsp + 0x178]
    0x455f33: call     0x470350

; --- Block 0x455f38 [BODY] 1 insns, callees: (none)
    0x455f38: jmp      0x455f3a

; --- Block 0x455f3a [BODY] 5 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x455f3a: mov      rsi, qword ptr [rsp + 0x38]
    0x455f3f: mov      byte ptr [rsp + 0x1d7], 1
    0x455f47: xor      eax, eax
    0x455f49: mov      edi, eax
    0x455f4b: call     0x49b480

; --- Block 0x455f50 [BODY] 3 insns, callees: (none)
    0x455f50: mov      qword ptr [rsp + 0x20], rdx
    0x455f55: mov      qword ptr [rsp + 0x28], rax
    0x455f5a: jmp      0x455f85

; --- Block 0x455f85 [BODY] 6 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x455f85: mov      rax, qword ptr [rsp + 0x20]
    0x455f8a: mov      rcx, qword ptr [rsp + 0x28]
    0x455f8f: mov      qword ptr [rsp + 0x190], rcx
    0x455f97: mov      qword ptr [rsp + 0x198], rax
    0x455f9f: lea      rdi, [rsp + 0x190]
    0x455fa7: call     0x49ad10

; --- Block 0x455f9f [LOOP_HEADER] 2 insns, callees: core::iter::range::<impl core::iter::traits::iterator::Iterator for core::ops::range::Range<A>>::next
    0x455f9f: lea      rdi, [rsp + 0x190]
    0x455fa7: call     0x49ad10

; --- Block 0x455fac [BODY] 3 insns, callees: (none)
    0x455fac: mov      qword ptr [rsp + 0x10], rdx
    0x455fb1: mov      qword ptr [rsp + 0x18], rax
    0x455fb6: jmp      0x455fb8

; --- Block 0x455fb8 [BODY] 6 insns, callees: (none)
    0x455fb8: mov      rax, qword ptr [rsp + 0x10]
    0x455fbd: mov      rcx, qword ptr [rsp + 0x18]
    0x455fc2: mov      qword ptr [rsp + 0x1a0], rcx
    0x455fca: mov      qword ptr [rsp + 0x1a8], rax
    0x455fd2: test     qword ptr [rsp + 0x1a0], 1
    0x455fde: je       0x45600a

; --- Block 0x455fe0 [BODY] 8 insns, callees: (none)
    0x455fe0: mov      rdx, qword ptr [rsp + 0x80]
    0x455fe8: mov      rcx, qword ptr [rsp + 0x1a8]
    0x455ff0: mov      qword ptr [rsp + 0x208], rcx
    0x455ff8: mov      rax, rcx
    0x455ffb: add      rax, rdx
    0x455ffe: mov      qword ptr [rsp + 8], rax
    0x456003: cmp      rax, rcx
    0x456006: jb       0x456063

; --- Block 0x456008 [BODY] 1 insns, callees: (none)
    0x456008: jmp      0x456056

; --- Block 0x45600a [BODY] 8 insns, callees: alloc::vec::Vec<T,A>::push
    0x45600a: mov      byte ptr [rsp + 0x1d7], 0
    0x456012: mov      rax, qword ptr [rsp + 0x188]
    0x45601a: mov      qword ptr [rsp + 0x1c0], rax
    0x456022: movups   xmm0, xmmword ptr [rsp + 0x178]
    0x45602a: movaps   xmmword ptr [rsp + 0x1b0], xmm0
    0x456032: lea      rdi, [rsp + 0x148]
    0x45603a: lea      rsi, [rsp + 0x1b0]
    0x456042: call     0x4a91a0

; --- Block 0x456047 [BODY] 1 insns, callees: (none)
    0x456047: jmp      0x456049

; --- Block 0x456049 [BODY] 2 insns, callees: (none)
    0x456049: mov      byte ptr [rsp + 0x1d7], 0
    0x456051: jmp      0x455e26

; --- Block 0x456056 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x456056: mov      rax, qword ptr [rsp + 0x38]
    0x45605b: cmp      rax, 0
    0x45605f: je       0x45609e

; --- Block 0x456061 [BODY] 1 insns, callees: (none)
    0x456061: jmp      0x456077

; --- Block 0x456063 [BODY] 3 insns, callees: (none)
    0x456063: lea      rdi, [rip + 0x9adf6]
    0x45606a: mov      rax, qword ptr [rip + 0x9f0bf]
    0x456071: call     rax

; --- Block 0x456077 [BODY] 9 insns, callees: (none)
    0x456077: mov      rcx, qword ptr [rsp + 0x38]
    0x45607c: mov      rax, qword ptr [rsp + 8]
    0x456081: xor      edx, edx
    0x456083: div      rcx
    0x456086: mov      rax, qword ptr [rsp + 0x38]
    0x45608b: mov      qword ptr [rsp], rdx
    0x45608f: mov      qword ptr [rsp + 0x210], rdx
    0x456097: cmp      rdx, rax
    0x45609a: jb       0x4560b0

; --- Block 0x45609c [BODY] 1 insns, callees: (none)
    0x45609c: jmp      0x4560cc

; --- Block 0x45609e [BODY] 3 insns, callees: (none)
    0x45609e: lea      rdi, [rip + 0x9adbb]
    0x4560a5: mov      rax, qword ptr [rip + 0x9f024]
    0x4560ac: call     rax

; --- Block 0x4560b0 [BODY] 5 insns, callees: alloc::string::String::push
    0x4560b0: mov      rax, qword ptr [rsp + 0x30]
    0x4560b5: mov      rcx, qword ptr [rsp]
    0x4560b9: movzx    esi, byte ptr [rax + rcx]
    0x4560bd: lea      rdi, [rsp + 0x178]
    0x4560c5: call     0x470410

; --- Block 0x4560ca [BODY] 1 insns, callees: (none)
    0x4560ca: jmp      0x4560e7

; --- Block 0x4560cc [BODY] 5 insns, callees: (none)
    0x4560cc: mov      rsi, qword ptr [rsp + 0x38]
    0x4560d1: mov      rdi, qword ptr [rsp]
    0x4560d5: lea      rdx, [rip + 0x9ad9c]
    0x4560dc: mov      rax, qword ptr [rip + 0x9efb5]
    0x4560e3: call     rax

; --- Block 0x4560e7 [BODY] 1 insns, callees: (none)
    0x4560e7: jmp      0x455f9f

```

**O2 blocks** (55 total):

```asm
; --- Block 0x42b630 [BODY] 24 insns, callees: <alloc::vec::Vec<T> as alloc::vec::spec_from_iter_nested::SpecFromIterNested<T,I>>::from_iter
    0x42b630: push     rbp
    0x42b631: push     r15
    0x42b633: push     r14
    0x42b635: push     r13
    0x42b637: push     r12
    0x42b639: push     rbx
    0x42b63a: sub      rsp, 0xd8
    0x42b641: mov      rbx, rdx
    0x42b644: mov      qword ptr [rsp + 0x40], rdi
    0x42b649: mov      r12, qword ptr [rsi + 8]
    0x42b64d: mov      qword ptr [rsp + 0x48], rsi
    0x42b652: mov      rax, qword ptr [rsi + 0x10]
    ... +12 more instructions

; --- Block 0x42b6b9 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b6b9: mov      r13, qword ptr [rsp + 0x90]
    0x42b6c1: test     r13, r13
    0x42b6c4: je       0x42b8ec

; --- Block 0x42b6ca [BODY] 3 insns, callees: (none)
    0x42b6ca: lea      rax, [r13*8]
    0x42b6d2: lea      r14, [rax + rax*2]
    0x42b6d6: call     qword ptr [rip + 0x59d0c]

; --- Block 0x42b6dc [BODY] 3 insns, callees: (none)
    0x42b6dc: mov      esi, 8
    0x42b6e1: mov      rdi, r14
    0x42b6e4: call     qword ptr [rip + 0x59d06]

; --- Block 0x42b6ea [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42b6ea: test     rax, rax
    0x42b6ed: je       0x42ba5e

; --- Block 0x42b6f3 [BODY] 8 insns, callees: (none)
    0x42b6f3: mov      qword ptr [rsp + 0x78], r13
    0x42b6f8: mov      qword ptr [rsp + 8], r13
    0x42b6fd: mov      qword ptr [rsp + 0x10], rax
    0x42b702: mov      qword ptr [rsp + 0x18], 0
    0x42b70b: mov      rax, qword ptr [rsp + 0x88]
    0x42b713: mov      r13, qword ptr [rax + 0x10]
    0x42b717: test     r13, r13
    0x42b71a: js       0x42ba57

; --- Block 0x42b720 [BODY] 11 insns, callees: (none)
    0x42b720: add      r14, rax
    0x42b723: mov      rcx, qword ptr [rax + 8]
    0x42b727: mov      qword ptr [rsp + 0x50], rcx
    0x42b72c: mov      rcx, rax
    0x42b72f: mov      qword ptr [rsp], r12
    0x42b733: mov      qword ptr [rsp + 0x58], rax
    0x42b738: mov      qword ptr [rsp + 0x60], rbx
    0x42b73d: mov      qword ptr [rsp + 0x70], r14
    0x42b742: test     r13, r13
    0x42b745: mov      qword ptr [rsp + 0x68], rcx
    0x42b74a: je       0x42b850

; --- Block 0x42b742 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b742: test     r13, r13
    0x42b745: mov      qword ptr [rsp + 0x68], rcx
    0x42b74a: je       0x42b850

; --- Block 0x42b750 [BODY] 1 insns, callees: (none)
    0x42b750: call     qword ptr [rip + 0x59c92]

; --- Block 0x42b756 [BODY] 3 insns, callees: (none)
    0x42b756: mov      esi, 1
    0x42b75b: mov      rdi, r13
    0x42b75e: call     qword ptr [rip + 0x59c8c]

; --- Block 0x42b764 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42b764: test     rax, rax
    0x42b767: je       0x42ba6e

; --- Block 0x42b76d [BODY] 8 insns, callees: (none)
    0x42b76d: mov      qword ptr [rsp + 0x20], r13
    0x42b772: mov      qword ptr [rsp + 0x28], rax
    0x42b777: mov      qword ptr [rsp + 0x30], 0
    0x42b780: mov      r15, r13
    0x42b783: mov      qword ptr [rsp + 0x38], rax
    0x42b788: mov      rcx, rax
    0x42b78b: xor      r14d, r14d
    0x42b78e: jmp      0x42b7a8

; --- Block 0x42b790 [LOOP_HEADER] 6 insns, callees: (none)
    0x42b790: mov      byte ptr [rcx + rax], bpl
    0x42b794: add      r14, r12
    0x42b797: mov      qword ptr [rsp + 0x30], r14
    0x42b79c: inc      rbx
    0x42b79f: dec      r15
    0x42b7a2: je       0x42b840

; --- Block 0x42b7a8 [BODY] 4 insns, callees: (none)
    0x42b7a8: mov      rax, rbx
    0x42b7ab: or       rax, r13
    0x42b7ae: shr      rax, 0x20
    0x42b7b2: je       0x42b7c0

; --- Block 0x42b7b4 [BODY] 4 insns, callees: (none)
    0x42b7b4: mov      rax, rbx
    0x42b7b7: xor      edx, edx
    0x42b7b9: div      r13
    0x42b7bc: jmp      0x42b7c7

; --- Block 0x42b7c0 [BODY] 14 insns, callees: (none)
    0x42b7c0: mov      eax, ebx
    0x42b7c2: xor      edx, edx
    0x42b7c4: div      r13d
    0x42b7c7: mov      rax, qword ptr [rsp + 0x50]
    0x42b7cc: movzx    ebp, byte ptr [rax + rdx]
    0x42b7d0: xor      r12d, r12d
    0x42b7d3: test     bpl, bpl
    0x42b7d6: sets     r12b
    0x42b7da: inc      r12
    0x42b7dd: mov      rdx, qword ptr [rsp + 0x20]
    0x42b7e2: sub      rdx, r14
    0x42b7e5: mov      rax, r14
    ... +2 more instructions

; --- Block 0x42b7c7 [BODY] 11 insns, callees: (none)
    0x42b7c7: mov      rax, qword ptr [rsp + 0x50]
    0x42b7cc: movzx    ebp, byte ptr [rax + rdx]
    0x42b7d0: xor      r12d, r12d
    0x42b7d3: test     bpl, bpl
    0x42b7d6: sets     r12b
    0x42b7da: inc      r12
    0x42b7dd: mov      rdx, qword ptr [rsp + 0x20]
    0x42b7e2: sub      rdx, r14
    0x42b7e5: mov      rax, r14
    0x42b7e8: cmp      r12, rdx
    0x42b7eb: ja       0x42b805

; --- Block 0x42b7ed [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42b7ed: test     bpl, bpl
    0x42b7f0: jns      0x42b790

; --- Block 0x42b7f2 [LOOP_HEADER] 6 insns, callees: (none)
    0x42b7f2: mov      edx, ebp
    0x42b7f4: and      dl, 0xbf
    0x42b7f7: shr      bpl, 6
    0x42b7fb: or       bpl, 0xc0
    0x42b7ff: mov      byte ptr [rcx + rax + 1], dl
    0x42b803: jmp      0x42b790

; --- Block 0x42b805 [BODY] 6 insns, callees: alloc::raw_vec::RawVecInner<A>::reserve::do_reserve_and_handle
    0x42b805: mov      ecx, 1
    0x42b80a: mov      r8d, 1
    0x42b810: lea      rdi, [rsp + 0x20]
    0x42b815: mov      rsi, r14
    0x42b818: mov      rdx, r12
    0x42b81b: call     0x440130

; --- Block 0x42b820 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42b820: mov      rcx, qword ptr [rsp + 0x28]
    0x42b825: mov      rax, qword ptr [rsp + 0x30]
    0x42b82a: test     bpl, bpl
    0x42b82d: jns      0x42b790

; --- Block 0x42b833 [BODY] 1 insns, callees: (none)
    0x42b833: jmp      0x42b7f2

; --- Block 0x42b840 [BODY] 3 insns, callees: (none)
    0x42b840: mov      r12, qword ptr [rsp + 0x20]
    0x42b845: mov      r15, qword ptr [rsp + 0x28]
    0x42b84a: jmp      0x42b866

; --- Block 0x42b850 [BODY] 9 insns, callees: (none)
    0x42b850: mov      eax, 1
    0x42b855: mov      qword ptr [rsp + 0x38], rax
    0x42b85a: xor      r14d, r14d
    0x42b85d: mov      r15d, 1
    0x42b863: xor      r12d, r12d
    0x42b866: mov      rbx, qword ptr [rsp + 0x18]
    0x42b86b: cmp      rbx, qword ptr [rsp + 8]
    0x42b870: mov      r13, qword ptr [rsp + 0x78]
    0x42b875: jne      0x42b882

; --- Block 0x42b866 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42b866: mov      rbx, qword ptr [rsp + 0x18]
    0x42b86b: cmp      rbx, qword ptr [rsp + 8]
    0x42b870: mov      r13, qword ptr [rsp + 0x78]
    0x42b875: jne      0x42b882

; --- Block 0x42b877 [BODY] 2 insns, callees: (none)
    0x42b877: lea      rdi, [rsp + 8]
    0x42b87c: call     qword ptr [rip + 0x59be6]

; --- Block 0x42b882 [BODY] 12 insns, callees: (none)
    0x42b882: mov      rsi, qword ptr [rsp + 0x68]
    0x42b887: lea      rax, [rsi + 0x18]
    0x42b88b: mov      rcx, qword ptr [rsp + 0x10]
    0x42b890: lea      rdx, [rbx + rbx*2]
    0x42b894: mov      qword ptr [rcx + rdx*8], r12
    0x42b898: mov      qword ptr [rcx + rdx*8 + 8], r15
    0x42b89d: mov      qword ptr [rcx + rdx*8 + 0x10], r14
    0x42b8a2: inc      rbx
    0x42b8a5: mov      qword ptr [rsp + 0x18], rbx
    0x42b8aa: mov      r14, qword ptr [rsp + 0x70]
    0x42b8af: cmp      rax, r14
    0x42b8b2: je       0x42ba44

; --- Block 0x42b8b8 [BODY] 8 insns, callees: (none)
    0x42b8b8: mov      rcx, qword ptr [rsi + 0x20]
    0x42b8bc: mov      qword ptr [rsp + 0x50], rcx
    0x42b8c1: mov      r13, qword ptr [rsi + 0x28]
    0x42b8c5: mov      rcx, rax
    0x42b8c8: test     r13, r13
    0x42b8cb: mov      r12, qword ptr [rsp]
    0x42b8cf: mov      rbx, qword ptr [rsp + 0x60]
    0x42b8d4: jns      0x42b742

; --- Block 0x42b8da [BODY] 3 insns, callees: (none)
    0x42b8da: xor      edi, edi
    0x42b8dc: mov      rsi, qword ptr [rsp + 0x38]
    0x42b8e1: call     qword ptr [rip + 0x59b31]

; --- Block 0x42b8e1 [LOOP_HEADER] 1 insns, callees: (none)
    0x42b8e1: call     qword ptr [rip + 0x59b31]

; --- Block 0x42b8ec [BODY] 11 insns, callees: alloc::str::join_generic_copy
    0x42b8ec: mov      qword ptr [rsp + 8], 0
    0x42b8f5: mov      qword ptr [rsp + 0x10], 8
    0x42b8fe: mov      qword ptr [rsp + 0x18], 0
    0x42b907: mov      esi, 8
    0x42b90c: mov      rbp, qword ptr [rsp + 0x88]
    0x42b914: xor      ebx, ebx
    0x42b916: lea      rcx, [rip - 0x240e0]
    0x42b91d: lea      rdi, [rsp + 0x20]
    0x42b922: mov      r8d, 1
    0x42b928: mov      rdx, rbx
    0x42b92b: call     0x43f970

; --- Block 0x42b916 [LOOP_HEADER] 5 insns, callees: alloc::str::join_generic_copy
    0x42b916: lea      rcx, [rip - 0x240e0]
    0x42b91d: lea      rdi, [rsp + 0x20]
    0x42b922: mov      r8d, 1
    0x42b928: mov      rdx, rbx
    0x42b92b: call     0x43f970

; --- Block 0x42b930 [BODY] 8 insns, callees: (none)
    0x42b930: mov      rax, qword ptr [rsp + 0x30]
    0x42b935: mov      rcx, qword ptr [rsp + 0x40]
    0x42b93a: mov      qword ptr [rcx + 0x10], rax
    0x42b93e: movups   xmm0, xmmword ptr [rsp + 0x20]
    0x42b943: movups   xmmword ptr [rcx], xmm0
    0x42b946: mov      rbx, qword ptr [rsp + 0x18]
    0x42b94b: test     rbx, rbx
    0x42b94e: je       0x42b98f

; --- Block 0x42b950 [BODY] 4 insns, callees: (none)
    0x42b950: mov      r14, qword ptr [rsp + 0x10]
    0x42b955: add      r14, 8
    0x42b959: mov      r15, qword ptr [rip + 0x59ac8]
    0x42b960: jmp      0x42b979

; --- Block 0x42b970 [LOOP_HEADER] 3 insns, callees: (none)
    0x42b970: add      r14, 0x18
    0x42b974: dec      rbx
    0x42b977: je       0x42b98f

; --- Block 0x42b979 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b979: mov      rsi, qword ptr [r14 - 8]
    0x42b97d: test     rsi, rsi
    0x42b980: je       0x42b970

; --- Block 0x42b982 [BODY] 3 insns, callees: (none)
    0x42b982: mov      rdi, qword ptr [r14]
    0x42b985: mov      edx, 1
    0x42b98a: call     r15

; --- Block 0x42b98d [BODY] 1 insns, callees: (none)
    0x42b98d: jmp      0x42b970

; --- Block 0x42b98f [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b98f: mov      rax, qword ptr [rsp + 8]
    0x42b994: test     rax, rax
    0x42b997: je       0x42b9b1

; --- Block 0x42b999 [BODY] 5 insns, callees: (none)
    0x42b999: shl      rax, 3
    0x42b99d: lea      rsi, [rax + rax*2]
    0x42b9a1: mov      rdi, qword ptr [rsp + 0x10]
    0x42b9a6: mov      edx, 8
    0x42b9ab: call     qword ptr [rip + 0x59a77]

; --- Block 0x42b9b1 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b9b1: test     r13, r13
    0x42b9b4: mov      r15, rbp
    0x42b9b7: je       0x42b9ef

; --- Block 0x42b9b9 [BODY] 3 insns, callees: (none)
    0x42b9b9: lea      rbx, [r15 + 8]
    0x42b9bd: mov      r14, qword ptr [rip + 0x59a64]
    0x42b9c4: jmp      0x42b9d9

; --- Block 0x42b9d0 [LOOP_HEADER] 3 insns, callees: (none)
    0x42b9d0: add      rbx, 0x18
    0x42b9d4: dec      r13
    0x42b9d7: je       0x42b9ef

; --- Block 0x42b9d9 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b9d9: mov      rsi, qword ptr [rbx - 8]
    0x42b9dd: test     rsi, rsi
    0x42b9e0: je       0x42b9d0

; --- Block 0x42b9e2 [BODY] 3 insns, callees: (none)
    0x42b9e2: mov      rdi, qword ptr [rbx]
    0x42b9e5: mov      edx, 1
    0x42b9ea: call     r14

; --- Block 0x42b9ed [BODY] 1 insns, callees: (none)
    0x42b9ed: jmp      0x42b9d0

; --- Block 0x42b9ef [BOUNDS_CHECK] 3 insns, callees: (none)
    0x42b9ef: mov      rax, qword ptr [rsp + 0x80]
    0x42b9f7: test     rax, rax
    0x42b9fa: je       0x42ba12

; --- Block 0x42b9fc [BODY] 5 insns, callees: (none)
    0x42b9fc: shl      rax, 3
    0x42ba00: lea      rsi, [rax + rax*2]
    0x42ba04: mov      edx, 8
    0x42ba09: mov      rdi, r15
    0x42ba0c: call     qword ptr [rip + 0x59a16]

; --- Block 0x42ba12 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x42ba12: mov      rax, qword ptr [rsp + 0x48]
    0x42ba17: mov      rsi, qword ptr [rax]
    0x42ba1a: test     rsi, rsi
    0x42ba1d: je       0x42ba2d

; --- Block 0x42ba1f [BODY] 3 insns, callees: (none)
    0x42ba1f: mov      edx, 1
    0x42ba24: mov      rdi, r12
    0x42ba27: call     qword ptr [rip + 0x599fb]

; --- Block 0x42ba2d [BODY] 9 insns, callees: (none)
    0x42ba2d: mov      rax, qword ptr [rsp + 0x40]
    0x42ba32: add      rsp, 0xd8
    0x42ba39: pop      rbx
    0x42ba3a: pop      r12
    0x42ba3c: pop      r13
    0x42ba3e: pop      r14
    0x42ba40: pop      r15
    0x42ba42: pop      rbp
    0x42ba43: ret      

; --- Block 0x42ba44 [BODY] 4 insns, callees: (none)
    0x42ba44: mov      rsi, qword ptr [rsp + 0x10]
    0x42ba49: mov      r12, qword ptr [rsp]
    0x42ba4d: mov      rbp, qword ptr [rsp + 0x58]
    0x42ba52: jmp      0x42b916

; --- Block 0x42ba57 [BODY] 2 insns, callees: (none)
    0x42ba57: xor      edi, edi
    0x42ba59: jmp      0x42b8e1

; --- Block 0x42ba5e [BODY] 3 insns, callees: (none)
    0x42ba5e: mov      edi, 8
    0x42ba63: mov      rsi, r14
    0x42ba66: call     qword ptr [rip + 0x599ac]

; --- Block 0x42ba6e [BODY] 3 insns, callees: (none)
    0x42ba6e: mov      rsi, r13
    0x42ba71: mov      edi, 1
    0x42ba76: jmp      0x42b8e1

```

**Hungarian matching result** (mean similarity: 0.689):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x455d7c` | BODY | `0x42b9ed` | BODY | 1.000 | GOOD |
| `0x456056` | BOUNDS_CHECK | `0x42b98f` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x45609c` | BODY | `0x42b98d` | BODY | 1.000 | GOOD |
| `0x4560ca` | BODY | `0x42b833` | BODY | 1.000 | GOOD |
| `0x455ec6` | DROP_GLUE | `0x42b877` | BODY | 0.993 | GOOD |
| `0x455cf7` | BODY | `0x42b840` | BODY | 0.985 | GOOD |
| `0x455e66` | BODY | `0x42b982` | BODY | 0.980 | GOOD |
| `0x455e94` | BODY | `0x42ba6e` | BODY | 0.963 | GOOD |
| `0x455ea0` | BODY | `0x42b805` | BODY | 0.955 | GOOD |
| `0x455d50` | BODY | `0x42b6ca` | BODY | 0.940 | GOOD |
| `0x4560cc` | BODY | `0x42b916` | LOOP_HEADER | 0.924 | GOOD |
| `0x455fb8` | BODY | `0x42b6f3` | BODY | 0.899 | GOOD |
| `0x455fac` | BODY | `0x42b9b9` | BODY | 0.872 | GOOD |
| `0x455ee4` | DROP_GLUE | `0x42b9e2` | BODY | 0.867 | GOOD |
| `0x455f3a` | BODY | `0x42b8da` | BODY | 0.839 | GOOD |
| `0x455dba` | BODY | `0x42ba1f` | BODY | 0.838 | GOOD |
| `0x455fe0` | BODY | `0x42b720` | BODY | 0.836 | GOOD |
| `0x456063` | BODY | `0x42b756` | BODY | 0.829 | GOOD |
| `0x455e33` | BODY | `0x42ba44` | BODY | 0.814 | GOOD |
| `0x455e3a` | BODY | `0x42b8b8` | BODY | 0.735 | GOOD |
| `0x455f50` | BODY | `0x42b9b1` | BOUNDS_CHECK | 0.731 | GOOD |
| `0x455e7b` | BODY | `0x42b979` | BOUNDS_CHECK | 0.728 | GOOD |
| `0x455ddb` | BODY | `0x42b6b9` | BOUNDS_CHECK | 0.726 | GOOD |
| `0x45609e` | BODY | `0x42b9ef` | BOUNDS_CHECK | 0.709 | GOOD |
| `0x45600a` | BODY | `0x42b930` | BODY | 0.700 | PARTIAL |
| `0x455d31` | BODY | `0x42ba12` | BOUNDS_CHECK | 0.676 | PARTIAL |
| `0x455ec4` | BODY | `0x42b750` | BODY | 0.662 | PARTIAL |
| `0x455ed3` | BODY | `0x42b8e1` | LOOP_HEADER | 0.662 | PARTIAL |
| `0x455dcc` | BODY | `0x42ba57` | BODY | 0.658 | PARTIAL |
| `0x455f01` | BODY | `0x42b882` | BODY | 0.648 | PARTIAL |
| `0x455e26` | LOOP_HEADER | `0x42b6ea` | BOUNDS_CHECK | 0.647 | PARTIAL |
| `0x455dce` | BODY | `0x42b764` | BOUNDS_CHECK | 0.643 | PARTIAL |
| `0x455f9f` | LOOP_HEADER | `0x42b7ed` | BOUNDS_CHECK | 0.643 | PARTIAL |
| `0x4560b0` | BODY | `0x42b999` | BODY | 0.634 | PARTIAL |
| `0x455e0c` | BODY | `0x42b790` | LOOP_HEADER | 0.628 | PARTIAL |
| `0x455d67` | BODY | `0x42b9d9` | BOUNDS_CHECK | 0.627 | PARTIAL |
| `0x456049` | BODY | `0x42b742` | BOUNDS_CHECK | 0.626 | PARTIAL |
| `0x455d8b` | BODY | `0x42b7b4` | BODY | 0.617 | PARTIAL |
| `0x456077` | BODY | `0x42b850` | BODY | 0.614 | PARTIAL |
| `0x455f85` | BODY | `0x42b9fc` | BODY | 0.598 | PARTIAL |
| `0x455cb0` | BODY | `0x42b8ec` | BODY | 0.493 | PARTIAL |
| `0x455d7e` | BODY | `0x42ba5e` | BODY | 0.485 | PARTIAL |
| `0x455ef1` | EPILOGUE | `0x42ba2d` | BODY | 0.483 | PARTIAL |
| `0x455ed5` | DROP_GLUE | `0x42b6dc` | BODY | 0.473 | PARTIAL |
| `0x455f38` | BODY | `0x42b76d` | BODY | 0.433 | PARTIAL |
| `0x456008` | BODY | `0x42b866` | BOUNDS_CHECK | 0.380 | POOR |
| `0x456047` | BODY | `0x42b950` | BODY | 0.378 | POOR |
| `0x455ee2` | BODY | `0x42b820` | BOUNDS_CHECK | 0.371 | POOR |
| `0x455e87` | BODY | `0x42b970` | LOOP_HEADER | 0.368 | POOR |
| `0x455d65` | BODY | `0x42b7f2` | LOOP_HEADER | 0.317 | POOR |
| `0x456061` | BODY | `0x42b9d0` | LOOP_HEADER | 0.299 | POOR |
| `0x455d4e` | BODY | `0x42b7c7` | BODY | 0.285 | POOR |
| `0x4560e7` | BODY | `0x42b7a8` | BODY | 0.282 | POOR |
| — | — | `0x42b630` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x42b7c0` | BODY | 0.000 | UNMATCHED (O2 only) |

### C `own_03` — O0: 24 blocks, O2: 26 blocks

**O0 blocks** (24 total):

```asm
; --- Block 0x403689 [BODY] 8 insns, callees: sub_401070
    0x403689: push     rbp
    0x40368a: mov      rbp, rsp
    0x40368d: sub      rsp, 0x950
    0x403694: mov      qword ptr [rbp - 0x948], rdi
    0x40369b: mov      qword ptr [rbp - 0x950], rsi
    0x4036a2: mov      rax, qword ptr [rbp - 0x948]
    0x4036a9: mov      rdi, rax
    0x4036ac: call     0x401070

; --- Block 0x4036b1 [BODY] 4 insns, callees: sub_401130
    0x4036b1: mov      qword ptr [rbp - 0x28], rax
    0x4036b5: mov      rax, qword ptr [rbp - 0x948]
    0x4036bc: mov      rdi, rax
    0x4036bf: call     0x401130

; --- Block 0x4036c4 [BODY] 6 insns, callees: sub_401110
    0x4036c4: mov      qword ptr [rbp - 0x30], rax
    0x4036c8: mov      qword ptr [rbp - 8], 0
    0x4036d0: mov      rax, qword ptr [rbp - 0x30]
    0x4036d4: mov      esi, 0x40f010
    0x4036d9: mov      rdi, rax
    0x4036dc: call     0x401110

; --- Block 0x4036e1 [BODY] 2 insns, callees: (none)
    0x4036e1: mov      qword ptr [rbp - 0x10], rax
    0x4036e5: jmp      0x403712

; --- Block 0x4036e7 [LOOP_HEADER] 8 insns, callees: sub_401110
    0x4036e7: mov      rax, qword ptr [rbp - 8]
    0x4036eb: lea      rdx, [rax + 1]
    0x4036ef: mov      qword ptr [rbp - 8], rdx
    0x4036f3: mov      rdx, qword ptr [rbp - 0x10]
    0x4036f7: mov      qword ptr [rbp + rax*8 - 0x840], rdx
    0x4036ff: mov      esi, 0x40f010
    0x403704: mov      edi, 0
    0x403709: call     0x401110

; --- Block 0x40370e [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40370e: mov      qword ptr [rbp - 0x10], rax
    0x403712: cmp      qword ptr [rbp - 0x10], 0
    0x403717: je       0x403723

; --- Block 0x403712 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x403712: cmp      qword ptr [rbp - 0x10], 0
    0x403717: je       0x403723

; --- Block 0x403719 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x403719: cmp      qword ptr [rbp - 8], 0xff
    0x403721: jbe      0x4036e7

; --- Block 0x403723 [BODY] 5 insns, callees: sub_4010f0
    0x403723: mov      rax, qword ptr [rbp - 0x28]
    0x403727: add      rax, rax
    0x40372a: add      rax, 1
    0x40372e: mov      rdi, rax
    0x403731: call     0x4010f0

; --- Block 0x403736 [BODY] 5 insns, callees: (none)
    0x403736: mov      qword ptr [rbp - 0x38], rax
    0x40373a: mov      rax, qword ptr [rbp - 0x38]
    0x40373e: mov      byte ptr [rax], 0
    0x403741: mov      qword ptr [rbp - 0x18], 0
    0x403749: jmp      0x40381a

; --- Block 0x40374e [LOOP_HEADER] 4 insns, callees: sub_401070
    0x40374e: mov      rax, qword ptr [rbp - 0x18]
    0x403752: mov      rax, qword ptr [rbp + rax*8 - 0x840]
    0x40375a: mov      rdi, rax
    0x40375d: call     0x401070

; --- Block 0x403762 [BODY] 3 insns, callees: (none)
    0x403762: mov      qword ptr [rbp - 0x40], rax
    0x403766: mov      qword ptr [rbp - 0x20], 0
    0x40376e: jmp      0x4037b1

; --- Block 0x403770 [LOOP_HEADER] 18 insns, callees: (none)
    0x403770: mov      rax, qword ptr [rbp - 0x18]
    0x403774: mov      rcx, qword ptr [rbp + rax*8 - 0x840]
    0x40377c: mov      rdx, qword ptr [rbp - 0x20]
    0x403780: mov      rax, qword ptr [rbp - 0x950]
    0x403787: add      rax, rdx
    0x40378a: mov      edx, 0
    0x40378f: div      qword ptr [rbp - 0x40]
    0x403793: mov      rax, rdx
    0x403796: add      rax, rcx
    0x403799: movzx    eax, byte ptr [rax]
    0x40379c: lea      rcx, [rbp - 0x940]
    0x4037a3: mov      rdx, qword ptr [rbp - 0x20]
    ... +6 more instructions

; --- Block 0x4037b1 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x4037b1: mov      rax, qword ptr [rbp - 0x20]
    0x4037b5: cmp      rax, qword ptr [rbp - 0x40]
    0x4037b9: jae      0x4037c5

; --- Block 0x4037bb [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4037bb: cmp      qword ptr [rbp - 0x20], 0xfe
    0x4037c3: jbe      0x403770

; --- Block 0x4037c5 [BODY] 7 insns, callees: (none)
    0x4037c5: mov      rax, qword ptr [rbp - 0x40]
    0x4037c9: mov      edx, 0xff
    0x4037ce: cmp      rax, rdx
    0x4037d1: cmova    rax, rdx
    0x4037d5: mov      byte ptr [rbp + rax - 0x940], 0
    0x4037dd: cmp      qword ptr [rbp - 0x18], 0
    0x4037e2: je       0x4037ff

; --- Block 0x4037e4 [BODY] 3 insns, callees: sub_401070
    0x4037e4: mov      rax, qword ptr [rbp - 0x38]
    0x4037e8: mov      rdi, rax
    0x4037eb: call     0x401070

; --- Block 0x4037f0 [BODY] 9 insns, callees: sub_401120
    0x4037f0: mov      rdx, rax
    0x4037f3: mov      rax, qword ptr [rbp - 0x38]
    0x4037f7: add      rax, rdx
    0x4037fa: mov      word ptr [rax], 0x20
    0x4037ff: lea      rdx, [rbp - 0x940]
    0x403806: mov      rax, qword ptr [rbp - 0x38]
    0x40380a: mov      rsi, rdx
    0x40380d: mov      rdi, rax
    0x403810: call     0x401120

; --- Block 0x4037ff [BODY] 5 insns, callees: sub_401120
    0x4037ff: lea      rdx, [rbp - 0x940]
    0x403806: mov      rax, qword ptr [rbp - 0x38]
    0x40380a: mov      rsi, rdx
    0x40380d: mov      rdi, rax
    0x403810: call     0x401120

; --- Block 0x403815 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x403815: add      qword ptr [rbp - 0x18], 1
    0x40381a: mov      rax, qword ptr [rbp - 0x18]
    0x40381e: cmp      rax, qword ptr [rbp - 8]
    0x403822: jb       0x40374e

; --- Block 0x40381a [BOUNDS_CHECK] 3 insns, callees: (none)
    0x40381a: mov      rax, qword ptr [rbp - 0x18]
    0x40381e: cmp      rax, qword ptr [rbp - 8]
    0x403822: jb       0x40374e

; --- Block 0x403828 [BODY] 3 insns, callees: sub_401030
    0x403828: mov      rax, qword ptr [rbp - 0x30]
    0x40382c: mov      rdi, rax
    0x40382f: call     0x401030

; --- Block 0x403834 [BODY] 3 insns, callees: sub_401030
    0x403834: mov      rax, qword ptr [rbp - 0x948]
    0x40383b: mov      rdi, rax
    0x40383e: call     0x401030

; --- Block 0x403843 [BODY] 3 insns, callees: (none)
    0x403843: mov      rax, qword ptr [rbp - 0x38]
    0x403847: leave    
    0x403848: ret      

```

**O2 blocks** (26 total):

```asm
; --- Block 0x404a00 [BODY] 10 insns, callees: sub_401080
    0x404a00: push     r15
    0x404a02: mov      r15, rsi
    0x404a05: push     r14
    0x404a07: push     r13
    0x404a09: mov      r13, rdi
    0x404a0c: push     r12
    0x404a0e: push     rbp
    0x404a0f: push     rbx
    0x404a10: sub      rsp, 0x918
    0x404a17: call     0x401080

; --- Block 0x404a1c [BODY] 3 insns, callees: sub_401140
    0x404a1c: mov      rdi, r13
    0x404a1f: mov      rbx, rax
    0x404a22: call     0x401140

; --- Block 0x404a27 [BODY] 5 insns, callees: sub_401120
    0x404a27: mov      esi, 0x40b02b
    0x404a2c: lea      r12, [rbx + rbx + 1]
    0x404a31: mov      rdi, rax
    0x404a34: mov      qword ptr [rsp + 8], rax
    0x404a39: call     0x401120

; --- Block 0x404a3e [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404a3e: test     rax, rax
    0x404a41: je       0x404b1a

; --- Block 0x404a47 [BODY] 2 insns, callees: (none)
    0x404a47: xor      ebx, ebx
    0x404a49: jmp      0x404a59

; --- Block 0x404a50 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404a50: cmp      rbx, 0xff
    0x404a57: ja       0x404a79

; --- Block 0x404a59 [BODY] 6 insns, callees: sub_401120
    0x404a59: mov      rbp, rbx
    0x404a5c: xor      edi, edi
    0x404a5e: add      rbx, 1
    0x404a62: mov      esi, 0x40b02b
    0x404a67: mov      qword ptr [rsp + rbx*8 + 0x108], rax
    0x404a6f: call     0x401120

; --- Block 0x404a74 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404a74: test     rax, rax
    0x404a77: jne      0x404a50

; --- Block 0x404a79 [BODY] 3 insns, callees: sub_401100
    0x404a79: mov      rdi, r12
    0x404a7c: xor      ebx, ebx
    0x404a7e: call     0x401100

; --- Block 0x404a83 [BODY] 6 insns, callees: sub_401080
    0x404a83: mov      byte ptr [rax], 0
    0x404a86: mov      r12, rax
    0x404a89: nop      dword ptr [rax]
    0x404a90: mov      r14, qword ptr [rsp + rbx*8 + 0x110]
    0x404a98: mov      rdi, r14
    0x404a9b: call     0x401080

; --- Block 0x404a90 [LOOP_HEADER] 3 insns, callees: sub_401080
    0x404a90: mov      r14, qword ptr [rsp + rbx*8 + 0x110]
    0x404a98: mov      rdi, r14
    0x404a9b: call     0x401080

; --- Block 0x404aa0 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x404aa0: xor      ecx, ecx
    0x404aa2: mov      rsi, rax
    0x404aa5: test     rax, rax
    0x404aa8: je       0x404ad4

; --- Block 0x404aaa [PROLOGUE] 1 insns, callees: (none)
    0x404aaa: nop      word ptr [rax + rax]

; --- Block 0x404ab0 [LOOP_HEADER] 8 insns, callees: (none)
    0x404ab0: lea      rax, [r15 + rcx]
    0x404ab4: xor      edx, edx
    0x404ab6: div      rsi
    0x404ab9: movzx    eax, byte ptr [r14 + rdx]
    0x404abe: mov      byte ptr [rsp + rcx + 0x10], al
    0x404ac2: add      rcx, 1
    0x404ac6: cmp      rsi, rcx
    0x404ac9: jbe      0x404ad4

; --- Block 0x404acb [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404acb: cmp      rcx, 0xfe
    0x404ad2: jbe      0x404ab0

; --- Block 0x404ad4 [BODY] 6 insns, callees: (none)
    0x404ad4: mov      eax, 0xff
    0x404ad9: cmp      rsi, rax
    0x404adc: cmovbe   rax, rsi
    0x404ae0: mov      byte ptr [rsp + rax + 0x10], 0
    0x404ae5: test     rbx, rbx
    0x404ae8: je       0x404afc

; --- Block 0x404aea [BODY] 2 insns, callees: sub_401080
    0x404aea: mov      rdi, r12
    0x404aed: call     0x401080

; --- Block 0x404af2 [BODY] 5 insns, callees: sub_401130
    0x404af2: mov      edx, 0x20
    0x404af7: mov      word ptr [r12 + rax], dx
    0x404afc: lea      rsi, [rsp + 0x10]
    0x404b01: mov      rdi, r12
    0x404b04: call     0x401130

; --- Block 0x404afc [BODY] 3 insns, callees: sub_401130
    0x404afc: lea      rsi, [rsp + 0x10]
    0x404b01: mov      rdi, r12
    0x404b04: call     0x401130

; --- Block 0x404b09 [BOUNDS_CHECK] 3 insns, callees: (none)
    0x404b09: lea      rax, [rbx + 1]
    0x404b0d: cmp      rbp, rbx
    0x404b10: je       0x404b28

; --- Block 0x404b12 [BODY] 2 insns, callees: (none)
    0x404b12: mov      rbx, rax
    0x404b15: jmp      0x404a90

; --- Block 0x404b1a [BODY] 2 insns, callees: sub_401100
    0x404b1a: mov      rdi, r12
    0x404b1d: call     0x401100

; --- Block 0x404b22 [BODY] 4 insns, callees: sub_401030
    0x404b22: mov      byte ptr [rax], 0
    0x404b25: mov      r12, rax
    0x404b28: mov      rdi, qword ptr [rsp + 8]
    0x404b2d: call     0x401030

; --- Block 0x404b28 [BODY] 2 insns, callees: sub_401030
    0x404b28: mov      rdi, qword ptr [rsp + 8]
    0x404b2d: call     0x401030

; --- Block 0x404b32 [BODY] 2 insns, callees: sub_401030
    0x404b32: mov      rdi, r13
    0x404b35: call     0x401030

; --- Block 0x404b3a [BODY] 9 insns, callees: (none)
    0x404b3a: add      rsp, 0x918
    0x404b41: mov      rax, r12
    0x404b44: pop      rbx
    0x404b45: pop      rbp
    0x404b46: pop      r12
    0x404b48: pop      r13
    0x404b4a: pop      r14
    0x404b4c: pop      r15
    0x404b4e: ret      

```

**Hungarian matching result** (mean similarity: 0.752):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x403712` | BOUNDS_CHECK | `0x404a3e` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x403719` | BOUNDS_CHECK | `0x404a50` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x4037bb` | BOUNDS_CHECK | `0x404acb` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x4036e1` | BODY | `0x404b12` | BODY | 0.982 | GOOD |
| `0x4037c5` | BODY | `0x404ad4` | BODY | 0.939 | GOOD |
| `0x4037ff` | BODY | `0x404a27` | BODY | 0.927 | GOOD |
| `0x403834` | BODY | `0x404b28` | BODY | 0.898 | GOOD |
| `0x403828` | BODY | `0x404b32` | BODY | 0.887 | GOOD |
| `0x403815` | BOUNDS_CHECK | `0x404aa0` | BOUNDS_CHECK | 0.822 | GOOD |
| `0x4036b1` | BODY | `0x404afc` | BODY | 0.815 | GOOD |
| `0x40381a` | BOUNDS_CHECK | `0x404b09` | BOUNDS_CHECK | 0.803 | GOOD |
| `0x40370e` | BOUNDS_CHECK | `0x404a74` | BOUNDS_CHECK | 0.773 | GOOD |
| `0x4037e4` | BODY | `0x404a90` | LOOP_HEADER | 0.723 | GOOD |
| `0x40374e` | LOOP_HEADER | `0x404b22` | BODY | 0.713 | GOOD |
| `0x4036c4` | BODY | `0x404a83` | BODY | 0.697 | PARTIAL |
| `0x403689` | BODY | `0x404a00` | BODY | 0.647 | PARTIAL |
| `0x403762` | BODY | `0x404a47` | BODY | 0.641 | PARTIAL |
| `0x4037f0` | BODY | `0x404a59` | BODY | 0.636 | PARTIAL |
| `0x4036e7` | LOOP_HEADER | `0x404af2` | BODY | 0.613 | PARTIAL |
| `0x403736` | BODY | `0x404aaa` | PROLOGUE | 0.586 | PARTIAL |
| `0x403843` | BODY | `0x404a1c` | BODY | 0.511 | PARTIAL |
| `0x4037b1` | BOUNDS_CHECK | `0x404a79` | BODY | 0.501 | PARTIAL |
| `0x403723` | BODY | `0x404b1a` | BODY | 0.485 | PARTIAL |
| `0x403770` | LOOP_HEADER | `0x404ab0` | LOOP_HEADER | 0.453 | PARTIAL |
| — | — | `0x404aea` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x404b3a` | BODY | 0.000 | UNMATCHED (O2 only) |

---

## Function `own_04`

### Rust `own_04` — O0: 26 blocks, O2: 13 blocks

**O0 blocks** (26 total):

```asm
; --- Block 0x456120 [BODY] 9 insns, callees: core::iter::traits::iterator::Iterator::rev
    0x456120: sub      rsp, 0x168
    0x456127: mov      rsi, rdi
    0x45612a: mov      qword ptr [rsp + 0xd0], rsi
    0x456132: mov      byte ptr [rsp + 0xcf], 0
    0x45613a: mov      byte ptr [rsp + 0xcf], 1
    0x456142: mov      qword ptr [rsp + 0x80], 0
    0x45614e: xor      eax, eax
    0x456150: mov      edi, eax
    0x456152: call     0x49af60

; --- Block 0x456157 [BODY] 3 insns, callees: (none)
    0x456157: mov      qword ptr [rsp + 0x70], rdx
    0x45615c: mov      qword ptr [rsp + 0x78], rax
    0x456161: jmp      0x4561a0

; --- Block 0x4561a0 [BODY] 3 insns, callees: <I as core::iter::traits::collect::IntoIterator>::into_iter
    0x4561a0: mov      rsi, qword ptr [rsp + 0x70]
    0x4561a5: mov      rdi, qword ptr [rsp + 0x78]
    0x4561aa: call     0x48fd00

; --- Block 0x4561af [BODY] 3 insns, callees: (none)
    0x4561af: mov      qword ptr [rsp + 0x50], rdx
    0x4561b4: mov      qword ptr [rsp + 0x58], rax
    0x4561b9: jmp      0x4561bb

; --- Block 0x4561bb [BODY] 6 insns, callees: <core::iter::adapters::rev::Rev<I> as core::iter::traits::iterator::Iterator>::next
    0x4561bb: mov      rax, qword ptr [rsp + 0x50]
    0x4561c0: mov      rcx, qword ptr [rsp + 0x58]
    0x4561c5: mov      qword ptr [rsp + 0x90], rcx
    0x4561cd: mov      qword ptr [rsp + 0x98], rax
    0x4561d5: lea      rdi, [rsp + 0x90]
    0x4561dd: call     0x48fe10

; --- Block 0x4561d5 [LOOP_HEADER] 2 insns, callees: <core::iter::adapters::rev::Rev<I> as core::iter::traits::iterator::Iterator>::next
    0x4561d5: lea      rdi, [rsp + 0x90]
    0x4561dd: call     0x48fe10

; --- Block 0x4561e2 [BODY] 3 insns, callees: (none)
    0x4561e2: mov      qword ptr [rsp + 0x40], rdx
    0x4561e7: mov      qword ptr [rsp + 0x48], rax
    0x4561ec: jmp      0x4561ee

; --- Block 0x4561ee [BODY] 6 insns, callees: (none)
    0x4561ee: mov      rax, qword ptr [rsp + 0x40]
    0x4561f3: mov      rcx, qword ptr [rsp + 0x48]
    0x4561f8: mov      qword ptr [rsp + 0xa0], rcx
    0x456200: mov      qword ptr [rsp + 0xa8], rax
    0x456208: test     qword ptr [rsp + 0xa0], 1
    0x456214: je       0x456244

; --- Block 0x456216 [BODY] 7 insns, callees: (none)
    0x456216: mov      rax, qword ptr [rsp + 0xa8]
    0x45621e: mov      qword ptr [rsp + 0xf8], rax
    0x456226: mov      qword ptr [rsp + 0x128], rax
    0x45622e: mov      qword ptr [rsp + 0x130], rax
    0x456236: imul     rax, rax
    0x45623a: mov      qword ptr [rsp + 0x38], rax
    0x45623f: jmp      0x4563da

; --- Block 0x456244 [BODY] 12 insns, callees: (none)
    0x456244: mov      qword ptr [rsp + 0xb0], 0
    0x456250: lea      rax, [rsp + 0x80]
    0x456258: mov      qword ptr [rsp + 0xb8], rax
    0x456260: mov      qword ptr [rsp + 0xc0], 0
    0x45626c: mov      rax, qword ptr [rsp + 0xb8]
    0x456274: mov      rdx, qword ptr [rax]
    0x456277: xor      eax, eax
    0x456279: mov      ecx, 1
    0x45627e: cmp      rdx, 0
    0x456282: cmove    rax, rcx
    0x456286: test     rax, 1
    0x45628c: je       0x4562bc

; --- Block 0x45626c [LOOP_HEADER] 8 insns, callees: (none)
    0x45626c: mov      rax, qword ptr [rsp + 0xb8]
    0x456274: mov      rdx, qword ptr [rax]
    0x456277: xor      eax, eax
    0x456279: mov      ecx, 1
    0x45627e: cmp      rdx, 0
    0x456282: cmove    rax, rcx
    0x456286: test     rax, 1
    0x45628c: je       0x4562bc

; --- Block 0x45628e [BODY] 7 insns, callees: (none)
    0x45628e: mov      rax, qword ptr [rsp + 0xb0]
    0x456296: mov      rcx, qword ptr [rsp + 0xc0]
    0x45629e: mov      qword ptr [rsp + 0x138], rax
    0x4562a6: mov      qword ptr [rsp + 0x140], rcx
    0x4562ae: imul     rax, rcx
    0x4562b2: mov      qword ptr [rsp + 0x30], rax
    0x4562b7: jmp      0x4563b8

; --- Block 0x4562bc [BODY] 21 insns, callees: (none)
    0x4562bc: mov      rcx, qword ptr [rsp + 0xb8]
    0x4562c4: mov      rax, rcx
    0x4562c7: add      rax, 8
    0x4562cb: mov      qword ptr [rsp + 0xe8], rax
    0x4562d3: mov      rax, qword ptr [rsp + 0xb8]
    0x4562db: mov      qword ptr [rsp + 0x20], rax
    0x4562e0: mov      qword ptr [rsp + 0xf0], rax
    0x4562e8: mov      rax, qword ptr [rsp + 0xb0]
    0x4562f0: mov      rcx, qword ptr [rcx + 8]
    0x4562f4: mov      qword ptr [rsp + 0x118], rax
    0x4562fc: mov      qword ptr [rsp + 0x120], rcx
    0x456304: add      rax, rcx
    ... +9 more instructions

; --- Block 0x456332 [BODY] 8 insns, callees: (none)
    0x456332: mov      rax, qword ptr [rsp + 0x20]
    0x456337: mov      rcx, qword ptr [rsp + 0x18]
    0x45633c: mov      qword ptr [rsp + 0xc0], rcx
    0x456344: mov      rax, qword ptr [rax]
    0x456347: mov      qword ptr [rsp + 0x10], rax
    0x45634c: and      rax, 7
    0x456350: cmp      rax, 0
    0x456354: je       0x45636c

; --- Block 0x456356 [BODY] 1 insns, callees: (none)
    0x456356: jmp      0x456382

; --- Block 0x456358 [BODY] 3 insns, callees: (none)
    0x456358: lea      rdi, [rip + 0x9ab31]
    0x45635f: mov      rax, qword ptr [rip + 0x9edca]
    0x456366: call     rax

; --- Block 0x45636c [BODY] 7 insns, callees: (none)
    0x45636c: mov      rax, qword ptr [rsp + 0x10]
    0x456371: cmp      rax, 0
    0x456375: sete     al
    0x456378: and      al, 0xff
    0x45637a: xor      al, 0xff
    0x45637c: test     al, 1
    0x45637e: jne      0x456399

; --- Block 0x456380 [BODY] 1 insns, callees: (none)
    0x456380: jmp      0x4563ab

; --- Block 0x456382 [BODY] 4 insns, callees: (none)
    0x456382: mov      rsi, qword ptr [rsp + 0x10]
    0x456387: mov      edi, 8
    0x45638c: lea      rdx, [rip + 0x9ab15]
    0x456393: call     qword ptr [rip + 0x9eda7]

; --- Block 0x456399 [BODY] 3 insns, callees: (none)
    0x456399: mov      rax, qword ptr [rsp + 0x10]
    0x45639e: mov      qword ptr [rsp + 0xb8], rax
    0x4563a6: jmp      0x45626c

; --- Block 0x4563ab [BODY] 2 insns, callees: (none)
    0x4563ab: lea      rdi, [rip + 0x9aaf6]
    0x4563b2: call     qword ptr [rip + 0x9ed90]

; --- Block 0x4563b8 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<rust_bench::own_04::List>
    0x4563b8: lea      rdi, [rsp + 0x80]
    0x4563c0: call     0x4965a0

; --- Block 0x4563c5 [EPILOGUE] 4 insns, callees: (none)
    0x4563c5: mov      rax, qword ptr [rsp + 0x30]
    0x4563ca: mov      byte ptr [rsp + 0xcf], 0
    0x4563d2: add      rsp, 0x168
    0x4563d9: ret      

; --- Block 0x4563da [BODY] 15 insns, callees: alloc::alloc::exchange_malloc
    0x4563da: mov      rax, qword ptr [rsp + 0x38]
    0x4563df: mov      qword ptr [rsp + 0x108], rax
    0x4563e7: mov      qword ptr [rsp + 0x110], 1
    0x4563f3: add      rax, 1
    0x4563f7: mov      qword ptr [rsp + 8], rax
    0x4563fc: mov      rax, qword ptr [rsp + 8]
    0x456401: mov      qword ptr [rsp + 0x100], rax
    0x456409: mov      byte ptr [rsp + 0xcf], 0
    0x456411: mov      rcx, qword ptr [rsp + 0x80]
    0x456419: mov      rax, qword ptr [rsp + 0x88]
    0x456421: mov      qword ptr [rsp + 0x148], rcx
    0x456429: mov      qword ptr [rsp + 0x150], rax
    ... +3 more instructions

; --- Block 0x456440 [BODY] 2 insns, callees: (none)
    0x456440: mov      qword ptr [rsp], rax
    0x456444: jmp      0x45648c

; --- Block 0x45648c [BODY] 11 insns, callees: (none)
    0x45648c: mov      rax, qword ptr [rsp]
    0x456490: mov      rdx, qword ptr [rsp + 0x148]
    0x456498: mov      rcx, qword ptr [rsp + 0x150]
    0x4564a0: mov      qword ptr [rax], rdx
    0x4564a3: mov      qword ptr [rax + 8], rcx
    0x4564a7: mov      rax, qword ptr [rsp + 8]
    0x4564ac: mov      rcx, qword ptr [rsp]
    0x4564b0: mov      byte ptr [rsp + 0xcf], 1
    0x4564b8: mov      qword ptr [rsp + 0x80], rcx
    0x4564c0: mov      qword ptr [rsp + 0x88], rax
    0x4564c8: jmp      0x4561d5

```

**O2 blocks** (13 total):

```asm
; --- Block 0x42bb00 [BODY] 8 insns, callees: (none)
    0x42bb00: push     r15
    0x42bb02: push     r14
    0x42bb04: push     r13
    0x42bb06: push     r12
    0x42bb08: push     rbx
    0x42bb09: sub      rsp, 0x10
    0x42bb0d: test     rdi, rdi
    0x42bb10: je       0x42bb98

; --- Block 0x42bb16 [BODY] 9 insns, callees: (none)
    0x42bb16: mov      rbx, rdi
    0x42bb19: dec      rbx
    0x42bb1c: xor      r12d, r12d
    0x42bb1f: mov      r14, qword ptr [rip + 0x598c2]
    0x42bb26: mov      r15, qword ptr [rip + 0x598c3]
    0x42bb2d: nop      dword ptr [rax]
    0x42bb30: mov      qword ptr [rsp], r12
    0x42bb34: mov      qword ptr [rsp + 8], r13
    0x42bb39: call     r14

; --- Block 0x42bb30 [LOOP_HEADER] 3 insns, callees: (none)
    0x42bb30: mov      qword ptr [rsp], r12
    0x42bb34: mov      qword ptr [rsp + 8], r13
    0x42bb39: call     r14

; --- Block 0x42bb3c [BODY] 3 insns, callees: (none)
    0x42bb3c: mov      edi, 0x10
    0x42bb41: mov      esi, 8
    0x42bb46: call     r15

; --- Block 0x42bb49 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x42bb49: test     rax, rax
    0x42bb4c: je       0x42bbbb

; --- Block 0x42bb4e [BODY] 9 insns, callees: (none)
    0x42bb4e: mov      rcx, rbx
    0x42bb51: imul     rcx, rbx
    0x42bb55: inc      rcx
    0x42bb58: mov      qword ptr [rax], r12
    0x42bb5b: mov      qword ptr [rax + 8], r13
    0x42bb5f: mov      r12, rax
    0x42bb62: mov      r13, rcx
    0x42bb65: add      rbx, -1
    0x42bb69: jb       0x42bb30

; --- Block 0x42bb6b [BODY] 12 insns, callees: (none)
    0x42bb6b: mov      qword ptr [rsp], rax
    0x42bb6f: mov      qword ptr [rsp + 8], rcx
    0x42bb74: mov      rdx, rsp
    0x42bb77: xor      ecx, ecx
    0x42bb79: xor      ebx, ebx
    0x42bb7b: nop      dword ptr [rax + rax]
    0x42bb80: add      rbx, qword ptr [rdx + 8]
    0x42bb84: inc      rcx
    0x42bb87: mov      rdx, rax
    0x42bb8a: mov      rax, qword ptr [rax]
    0x42bb8d: test     rax, rax
    0x42bb90: jne      0x42bb80

; --- Block 0x42bb80 [ITERATOR_STATE] 6 insns, callees: (none)
    0x42bb80: add      rbx, qword ptr [rdx + 8]
    0x42bb84: inc      rcx
    0x42bb87: mov      rdx, rax
    0x42bb8a: mov      rax, qword ptr [rax]
    0x42bb8d: test     rax, rax
    0x42bb90: jne      0x42bb80

; --- Block 0x42bb92 [BODY] 2 insns, callees: (none)
    0x42bb92: imul     rbx, rcx
    0x42bb96: jmp      0x42bba2

; --- Block 0x42bb98 [DROP_GLUE] 4 insns, callees: core::ptr::drop_in_place<rust_bench::own_04::List>
    0x42bb98: mov      qword ptr [rsp], 0
    0x42bba0: xor      ebx, ebx
    0x42bba2: mov      rdi, rsp
    0x42bba5: call     0x433580

; --- Block 0x42bba2 [DROP_GLUE] 2 insns, callees: core::ptr::drop_in_place<rust_bench::own_04::List>
    0x42bba2: mov      rdi, rsp
    0x42bba5: call     0x433580

; --- Block 0x42bbaa [BODY] 8 insns, callees: (none)
    0x42bbaa: mov      rax, rbx
    0x42bbad: add      rsp, 0x10
    0x42bbb1: pop      rbx
    0x42bbb2: pop      r12
    0x42bbb4: pop      r13
    0x42bbb6: pop      r14
    0x42bbb8: pop      r15
    0x42bbba: ret      

; --- Block 0x42bbbb [BODY] 3 insns, callees: (none)
    0x42bbbb: mov      edi, 8
    0x42bbc0: mov      esi, 0x10
    0x42bbc5: call     qword ptr [rip + 0x59835]

```

**Hungarian matching result** (mean similarity: 0.711):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4561a0` | BODY | `0x42bb30` | LOOP_HEADER | 0.987 | GOOD |
| `0x4561ee` | BODY | `0x42bb80` | ITERATOR_STATE | 0.870 | GOOD |
| `0x456244` | BODY | `0x42bb6b` | BODY | 0.776 | GOOD |
| `0x4563b8` | DROP_GLUE | `0x42bba2` | DROP_GLUE | 0.765 | GOOD |
| `0x456440` | BODY | `0x42bb92` | BODY | 0.750 | GOOD |
| `0x456382` | BODY | `0x42bbbb` | BODY | 0.708 | GOOD |
| `0x456358` | BODY | `0x42bb98` | DROP_GLUE | 0.694 | PARTIAL |
| `0x456120` | BODY | `0x42bb16` | BODY | 0.690 | PARTIAL |
| `0x4563da` | BODY | `0x42bb3c` | BODY | 0.687 | PARTIAL |
| `0x4561d5` | LOOP_HEADER | `0x42bb49` | BOUNDS_CHECK | 0.643 | PARTIAL |
| `0x456216` | BODY | `0x42bb4e` | BODY | 0.619 | PARTIAL |
| `0x456332` | BODY | `0x42bb00` | BODY | 0.543 | PARTIAL |
| `0x4563c5` | EPILOGUE | `0x42bbaa` | BODY | 0.510 | PARTIAL |
| `0x456157` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4561af` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4561bb` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4561e2` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45626c` | LOOP_HEADER | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45628e` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4562bc` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456356` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45636c` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456380` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x456399` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x4563ab` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |
| `0x45648c` | BODY | — | — | 0.000 | UNMATCHED (O0 only) |

### C `own_04` — O0: 11 blocks, O2: 14 blocks

**O0 blocks** (11 total):

```asm
; --- Block 0x403849 [BODY] 8 insns, callees: (none)
    0x403849: push     rbp
    0x40384a: mov      rbp, rsp
    0x40384d: sub      rsp, 0x50
    0x403851: mov      qword ptr [rbp - 0x48], rdi
    0x403855: mov      qword ptr [rbp - 8], 0
    0x40385d: mov      rax, qword ptr [rbp - 0x48]
    0x403861: mov      qword ptr [rbp - 0x10], rax
    0x403865: jmp      0x4038ad

; --- Block 0x403867 [LOOP_HEADER] 2 insns, callees: sub_4010f0
    0x403867: mov      edi, 0x10
    0x40386c: call     0x4010f0

; --- Block 0x403871 [BODY] 17 insns, callees: (none)
    0x403871: mov      qword ptr [rbp - 0x38], rax
    0x403875: mov      rax, qword ptr [rbp - 0x10]
    0x403879: lea      rdx, [rax - 1]
    0x40387d: mov      rax, qword ptr [rbp - 0x10]
    0x403881: sub      rax, 1
    0x403885: imul     rax, rdx
    0x403889: lea      rdx, [rax + 1]
    0x40388d: mov      rax, qword ptr [rbp - 0x38]
    0x403891: mov      qword ptr [rax], rdx
    0x403894: mov      rax, qword ptr [rbp - 0x38]
    0x403898: mov      rdx, qword ptr [rbp - 8]
    0x40389c: mov      qword ptr [rax + 8], rdx
    ... +5 more instructions

; --- Block 0x4038ad [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4038ad: cmp      qword ptr [rbp - 0x10], 0
    0x4038b2: jne      0x403867

; --- Block 0x4038b4 [BODY] 5 insns, callees: (none)
    0x4038b4: mov      qword ptr [rbp - 0x18], 0
    0x4038bc: mov      qword ptr [rbp - 0x20], 0
    0x4038c4: mov      rax, qword ptr [rbp - 8]
    0x4038c8: mov      qword ptr [rbp - 0x28], rax
    0x4038cc: jmp      0x4038ea

; --- Block 0x4038ce [LOOP_HEADER] 9 insns, callees: (none)
    0x4038ce: mov      rax, qword ptr [rbp - 0x28]
    0x4038d2: mov      rax, qword ptr [rax]
    0x4038d5: add      qword ptr [rbp - 0x18], rax
    0x4038d9: add      qword ptr [rbp - 0x20], 1
    0x4038de: mov      rax, qword ptr [rbp - 0x28]
    0x4038e2: mov      rax, qword ptr [rax + 8]
    0x4038e6: mov      qword ptr [rbp - 0x28], rax
    0x4038ea: cmp      qword ptr [rbp - 0x28], 0
    0x4038ef: jne      0x4038ce

; --- Block 0x4038ea [BOUNDS_CHECK] 2 insns, callees: (none)
    0x4038ea: cmp      qword ptr [rbp - 0x28], 0
    0x4038ef: jne      0x4038ce

; --- Block 0x4038f1 [BODY] 1 insns, callees: (none)
    0x4038f1: jmp      0x403913

; --- Block 0x4038f3 [LOOP_HEADER] 8 insns, callees: sub_401030
    0x4038f3: mov      rax, qword ptr [rbp - 8]
    0x4038f7: mov      qword ptr [rbp - 0x30], rax
    0x4038fb: mov      rax, qword ptr [rbp - 8]
    0x4038ff: mov      rax, qword ptr [rax + 8]
    0x403903: mov      qword ptr [rbp - 8], rax
    0x403907: mov      rax, qword ptr [rbp - 0x30]
    0x40390b: mov      rdi, rax
    0x40390e: call     0x401030

; --- Block 0x403913 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x403913: cmp      qword ptr [rbp - 8], 0
    0x403918: jne      0x4038f3

; --- Block 0x40391a [BODY] 4 insns, callees: (none)
    0x40391a: mov      rax, qword ptr [rbp - 0x18]
    0x40391e: imul     rax, qword ptr [rbp - 0x20]
    0x403923: leave    
    0x403924: ret      

```

**O2 blocks** (14 total):

```asm
; --- Block 0x404b50 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404b50: test     rdi, rdi
    0x404b53: je       0x404be0

; --- Block 0x404b59 [BODY] 10 insns, callees: sub_401100
    0x404b59: push     r12
    0x404b5b: push     rbp
    0x404b5c: push     rbx
    0x404b5d: mov      rbx, rdi
    0x404b60: xor      edi, edi
    0x404b62: nop      word ptr [rax + rax]
    0x404b68: mov      rbp, rdi
    0x404b6b: mov      edi, 0x10
    0x404b70: sub      rbx, 1
    0x404b74: call     0x401100

; --- Block 0x404b68 [LOOP_HEADER] 4 insns, callees: sub_401100
    0x404b68: mov      rbp, rdi
    0x404b6b: mov      edi, 0x10
    0x404b70: sub      rbx, 1
    0x404b74: call     0x401100

; --- Block 0x404b79 [BODY] 8 insns, callees: (none)
    0x404b79: mov      rdi, rax
    0x404b7c: mov      rax, rbx
    0x404b7f: imul     rax, rbx
    0x404b83: mov      qword ptr [rdi + 8], rbp
    0x404b87: add      rax, 1
    0x404b8b: mov      qword ptr [rdi], rax
    0x404b8e: test     rbx, rbx
    0x404b91: jne      0x404b68

; --- Block 0x404b93 [BODY] 3 insns, callees: (none)
    0x404b93: mov      rdx, rbp
    0x404b96: xor      r12d, r12d
    0x404b99: jmp      0x404ba7

; --- Block 0x404ba0 [LOOP_HEADER] 6 insns, callees: (none)
    0x404ba0: mov      rax, qword ptr [rdx]
    0x404ba3: mov      rdx, qword ptr [rdx + 8]
    0x404ba7: add      rbx, rax
    0x404baa: add      r12, 1
    0x404bae: test     rdx, rdx
    0x404bb1: jne      0x404ba0

; --- Block 0x404ba7 [BOUNDS_CHECK] 4 insns, callees: (none)
    0x404ba7: add      rbx, rax
    0x404baa: add      r12, 1
    0x404bae: test     rdx, rdx
    0x404bb1: jne      0x404ba0

; --- Block 0x404bb3 [BODY] 1 insns, callees: sub_401030
    0x404bb3: call     0x401030

; --- Block 0x404bb8 [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404bb8: test     rbp, rbp
    0x404bbb: je       0x404bd1

; --- Block 0x404bbd [PROLOGUE] 1 insns, callees: (none)
    0x404bbd: nop      dword ptr [rax]

; --- Block 0x404bc0 [LOOP_HEADER] 3 insns, callees: sub_401030
    0x404bc0: mov      rdi, rbp
    0x404bc3: mov      rbp, qword ptr [rbp + 8]
    0x404bc7: call     0x401030

; --- Block 0x404bcc [BOUNDS_CHECK] 2 insns, callees: (none)
    0x404bcc: test     rbp, rbp
    0x404bcf: jne      0x404bc0

; --- Block 0x404bd1 [BODY] 6 insns, callees: (none)
    0x404bd1: mov      rax, rbx
    0x404bd4: pop      rbx
    0x404bd5: pop      rbp
    0x404bd6: imul     rax, r12
    0x404bda: pop      r12
    0x404bdc: ret      

; --- Block 0x404be0 [BODY] 2 insns, callees: (none)
    0x404be0: xor      eax, eax
    0x404be2: ret      

```

**Hungarian matching result** (mean similarity: 0.802):

| O0 Block | Type | O2 Block | Type | Similarity | Verdict |
|----------|------|----------|------|------------|---------|
| `0x4038ad` | BOUNDS_CHECK | `0x404b50` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x4038ea` | BOUNDS_CHECK | `0x404bb8` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x403913` | BOUNDS_CHECK | `0x404bcc` | BOUNDS_CHECK | 1.000 | GOOD |
| `0x4038f1` | BODY | `0x404bbd` | PROLOGUE | 0.997 | GOOD |
| `0x4038ce` | LOOP_HEADER | `0x404ba0` | LOOP_HEADER | 0.857 | GOOD |
| `0x4038f3` | LOOP_HEADER | `0x404bc0` | LOOP_HEADER | 0.827 | GOOD |
| `0x4038b4` | BODY | `0x404b93` | BODY | 0.707 | GOOD |
| `0x40391a` | BODY | `0x404bd1` | BODY | 0.705 | GOOD |
| `0x403871` | BODY | `0x404b79` | BODY | 0.608 | PARTIAL |
| `0x403867` | LOOP_HEADER | `0x404b68` | LOOP_HEADER | 0.598 | PARTIAL |
| `0x403849` | BODY | `0x404b59` | BODY | 0.521 | PARTIAL |
| — | — | `0x404ba7` | BOUNDS_CHECK | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x404bb3` | BODY | 0.000 | UNMATCHED (O2 only) |
| — | — | `0x404be0` | BODY | 0.000 | UNMATCHED (O2 only) |

---
