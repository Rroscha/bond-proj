/*
 * 100 C functions equivalent to the Rust benchmark.
 * Same algorithms, but:
 *   - No bounds checking (raw pointer arithmetic)
 *   - No Option/Result (use return codes, sentinel values)
 *   - No Drop/RAII (manual free)
 *   - No iterators (explicit loops)
 *   - No rich enums (tagged unions with manual dispatch)
 *
 * Compiled with: gcc -O0/-O2 -g -o c_bench bench.c -lm
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <ctype.h>

#define NOINLINE __attribute__((noinline))
#define USED     __attribute__((used))

static volatile uint64_t sink;
static void black_box_u64(uint64_t v) { sink = v; }
static void black_box_i64(int64_t v)  { sink = (uint64_t)v; }
static void black_box_ptr(const void *p) { sink = (uint64_t)(uintptr_t)p; }

static int cmp_u64(const void *a, const void *b) {
    uint64_t va = *(const uint64_t *)a, vb = *(const uint64_t *)b;
    return (va > vb) - (va < vb);
}

static int cmp_i64(const void *a, const void *b) {
    int64_t va = *(const int64_t *)a, vb = *(const int64_t *)b;
    return (va > vb) - (va < vb);
}

/* ========================================================================== */
/* Category 1: Array operations (no bounds checking in C)                     */
/* bc_01 .. bc_20                                                             */
/* ========================================================================== */

/* Insertion sort on first `limit` elements, return inversions counted */
NOINLINE uint64_t bc_01(const uint64_t *data, size_t len, size_t limit) {
    size_t n = len < limit ? len : limit;
    uint64_t *buf = (uint64_t *)malloc(n * sizeof(uint64_t));
    memcpy(buf, data, n * sizeof(uint64_t));
    uint64_t inversions = 0;
    for (size_t i = 1; i < n; i++) {
        uint64_t key = buf[i];
        size_t j = i;
        while (j > 0 && buf[j - 1] > key) {
            buf[j] = buf[j - 1];
            j--;
            inversions++;
        }
        buf[j] = key;
    }
    free(buf);
    return inversions;
}

/* Partition around pivot (quicksort partition) */
NOINLINE size_t bc_02(uint64_t *data, size_t n) {
    if (n <= 1) return 0;
    size_t pivot_idx = n / 2;
    uint64_t tmp = data[pivot_idx]; data[pivot_idx] = data[n-1]; data[n-1] = tmp;
    uint64_t pivot = data[n - 1];
    size_t store = 0;
    for (size_t i = 0; i < n - 1; i++) {
        if (data[i] < pivot) {
            tmp = data[i]; data[i] = data[store]; data[store] = tmp;
            store++;
        }
    }
    tmp = data[store]; data[store] = data[n-1]; data[n-1] = tmp;
    return store;
}

/* Compute histogram with `bins` buckets */
NOINLINE uint64_t *bc_03(const uint64_t *data, size_t len, size_t bins, size_t *out_len) {
    *out_len = 0;
    if (len == 0 || bins == 0) return NULL;
    uint64_t min_val = data[0];
    uint64_t max_val = data[0];
    for (size_t i = 1; i < len; i++) {
        if (data[i] > max_val) max_val = data[i];
    }
    uint64_t range = max_val - min_val + 1;
    uint64_t bin_size = (range + (uint64_t)bins - 1) / (uint64_t)bins;
    uint64_t *hist = (uint64_t *)calloc(bins, sizeof(uint64_t));
    for (size_t i = 0; i < len; i++) {
        size_t bin = (size_t)((data[i] - min_val) / bin_size);
        if (bin < bins) hist[bin]++;
    }
    *out_len = bins;
    return hist;
}

/* Merge two sorted arrays */
NOINLINE uint64_t *bc_04(const uint64_t *a, size_t alen, const uint64_t *b, size_t blen, size_t *out_len) {
    uint64_t *result = (uint64_t *)malloc((alen + blen) * sizeof(uint64_t));
    size_t i = 0, j = 0, k = 0;
    while (i < alen && j < blen) {
        if (a[i] <= b[j]) { result[k++] = a[i++]; }
        else { result[k++] = b[j++]; }
    }
    while (i < alen) result[k++] = a[i++];
    while (j < blen) result[k++] = b[j++];
    *out_len = k;
    return result;
}

/* Longest increasing subsequence length via patience sorting */
NOINLINE uint64_t bc_05(const uint64_t *data, size_t len) {
    uint64_t *tails = (uint64_t *)malloc(len * sizeof(uint64_t));
    size_t tails_len = 0;
    for (size_t i = 0; i < len; i++) {
        uint64_t val = data[i];
        size_t lo = 0, hi = tails_len;
        while (lo < hi) {
            size_t mid = lo + (hi - lo) / 2;
            if (tails[mid] < val) lo = mid + 1; else hi = mid;
        }
        if (lo == tails_len) {
            tails[tails_len++] = val;
        } else {
            tails[lo] = val;
        }
    }
    uint64_t result = (uint64_t)tails_len;
    free(tails);
    return result;
}

/* Shell sort with given gap */
NOINLINE uint64_t bc_06(uint64_t *data, size_t n, size_t initial_gap) {
    uint64_t swaps = 0;
    size_t gap = initial_gap;
    while (gap > 0) {
        for (size_t i = gap; i < n; i++) {
            uint64_t temp = data[i];
            size_t j = i;
            while (j >= gap && data[j - gap] > temp) {
                data[j] = data[j - gap];
                j -= gap;
                swaps++;
            }
            data[j] = temp;
        }
        gap /= 2;
    }
    return swaps;
}

/* Convolution with kernel [-1, 2, -1], then smooth */
NOINLINE int64_t *bc_07(const uint64_t *data, size_t n, size_t *out_len) {
    *out_len = 0;
    if (n < 3) return NULL;
    size_t rlen = n - 2;
    int64_t *result = (int64_t *)malloc(rlen * sizeof(int64_t));
    for (size_t i = 1; i < n - 1; i++) {
        result[i - 1] = -(int64_t)data[i - 1] + 2 * (int64_t)data[i] - (int64_t)data[i + 1];
    }
    int64_t *smoothed = (int64_t *)malloc(rlen * sizeof(int64_t));
    for (size_t i = 0; i < rlen; i++) {
        int64_t left = (i > 0) ? result[i - 1] : result[i];
        int64_t right = (i + 1 < rlen) ? result[i + 1] : result[i];
        smoothed[i] = (left + result[i] + right) / 3;
    }
    free(result);
    *out_len = rlen;
    return smoothed;
}

/* Find local maxima with prominence check */
NOINLINE size_t bc_08(const uint64_t *data, size_t n, uint64_t min_prominence,
                      size_t *peak_idx, uint64_t *peak_val, size_t max_peaks) {
    size_t count = 0;
    if (n < 3) return 0;
    for (size_t i = 1; i < n - 1; i++) {
        if (data[i] > data[i - 1] && data[i] > data[i + 1]) {
            uint64_t left_min = data[i];
            for (size_t j = i; j > 0; j--) {
                if (data[j - 1] < left_min) left_min = data[j - 1];
                if (data[j - 1] > data[i]) break;
            }
            uint64_t prominence = data[i] - left_min;
            if (prominence >= min_prominence && count < max_peaks) {
                peak_idx[count] = i;
                peak_val[count] = data[i];
                count++;
            }
        }
    }
    return count;
}

/* Bubble sort with early termination */
NOINLINE uint64_t bc_09(uint64_t *data, size_t n) {
    uint64_t passes = 0;
    while (1) {
        int swapped = 0;
        for (size_t i = 1; i < n; i++) {
            if (data[i - 1] > data[i]) {
                uint64_t tmp = data[i - 1]; data[i - 1] = data[i]; data[i] = tmp;
                swapped = 1;
            }
        }
        passes++;
        if (!swapped) break;
    }
    return passes;
}

/* Rotate array left by k positions using reversal algorithm */
NOINLINE uint64_t *bc_10(const uint64_t *data, size_t n, size_t k, size_t *out_len) {
    *out_len = n;
    if (n == 0) return NULL;
    k = k % n;
    uint64_t *result = (uint64_t *)malloc(n * sizeof(uint64_t));
    memcpy(result, data, n * sizeof(uint64_t));
    /* Reverse first k */
    size_t lo = 0, hi = (k > 0) ? k - 1 : 0;
    while (lo < hi) { uint64_t t = result[lo]; result[lo] = result[hi]; result[hi] = t; lo++; hi--; }
    /* Reverse rest */
    lo = k; hi = n - 1;
    while (lo < hi) { uint64_t t = result[lo]; result[lo] = result[hi]; result[hi] = t; lo++; hi--; }
    /* Reverse all */
    lo = 0; hi = n - 1;
    while (lo < hi) { uint64_t t = result[lo]; result[lo] = result[hi]; result[hi] = t; lo++; hi--; }
    return result;
}

/* Selection sort */
NOINLINE uint64_t bc_11(uint64_t *data, size_t n) {
    uint64_t comparisons = 0;
    for (size_t i = 0; i < n; i++) {
        size_t min_idx = i;
        for (size_t j = i + 1; j < n; j++) {
            comparisons++;
            if (data[j] < data[min_idx]) min_idx = j;
        }
        if (min_idx != i) {
            uint64_t tmp = data[i]; data[i] = data[min_idx]; data[min_idx] = tmp;
        }
    }
    return comparisons;
}

/* Running median using sorted window */
NOINLINE uint64_t *bc_12(const uint64_t *data, size_t n, size_t window, size_t *out_len) {
    *out_len = 0;
    if (window == 0 || window > n) return NULL;
    size_t rlen = n - window + 1;
    uint64_t *result = (uint64_t *)malloc(rlen * sizeof(uint64_t));
    uint64_t *win = (uint64_t *)malloc(window * sizeof(uint64_t));
    memcpy(win, data, window * sizeof(uint64_t));
    qsort(win, window, sizeof(uint64_t), cmp_u64);
    result[0] = win[window / 2];
    for (size_t i = window; i < n; i++) {
        uint64_t old = data[i - window];
        uint64_t new_val = data[i];
        /* Remove old: find via binary search */
        size_t pos = 0;
        { size_t lo = 0, hi = window; while (lo < hi) { size_t mid = lo+(hi-lo)/2; if (win[mid] < old) lo = mid+1; else hi = mid; } pos = lo; }
        if (pos < window && win[pos] == old) {
            memmove(&win[pos], &win[pos + 1], (window - 1 - pos) * sizeof(uint64_t));
        }
        /* Insert new in sorted position */
        size_t wlen = window - 1;
        size_t ins = 0;
        { size_t lo = 0, hi = wlen; while (lo < hi) { size_t mid = lo+(hi-lo)/2; if (win[mid] < new_val) lo = mid+1; else hi = mid; } ins = lo; }
        memmove(&win[ins + 1], &win[ins], (wlen - ins) * sizeof(uint64_t));
        win[ins] = new_val;
        result[i - window + 1] = win[window / 2];
    }
    free(win);
    *out_len = rlen;
    return result;
}

/* Count inversions (O(n^2)) */
NOINLINE uint64_t bc_13(const uint64_t *data, size_t n) {
    uint64_t inv = 0;
    for (size_t i = 0; i < n; i++) {
        for (size_t j = i + 1; j < n; j++) {
            if (data[i] > data[j]) inv++;
        }
    }
    return inv;
}

/* Three-way partition (Dutch National Flag) */
NOINLINE void bc_14(uint64_t *data, size_t n, uint64_t pivot, size_t *out_lo, size_t *out_hi) {
    size_t lo = 0, mid = 0, hi = n;
    while (mid < hi) {
        if (data[mid] < pivot) {
            uint64_t tmp = data[lo]; data[lo] = data[mid]; data[mid] = tmp;
            lo++; mid++;
        } else if (data[mid] > pivot) {
            hi--;
            uint64_t tmp = data[mid]; data[mid] = data[hi]; data[hi] = tmp;
        } else {
            mid++;
        }
    }
    *out_lo = lo;
    *out_hi = hi;
}

/* Prefix sum + range query simulation */
NOINLINE uint64_t bc_15(const uint64_t *data, size_t n) {
    if (n == 0) return 0;
    uint64_t *prefix = (uint64_t *)calloc(n + 1, sizeof(uint64_t));
    for (size_t i = 0; i < n; i++) {
        prefix[i + 1] = prefix[i] + data[i]; /* wrapping in C is UB for signed, ok for unsigned */
    }
    uint64_t total = 0;
    size_t max_len = n < 10 ? n : 10;
    for (size_t len = 1; len <= max_len; len++) {
        for (size_t start = 0; start + len <= n; start++) {
            uint64_t range_sum = prefix[start + len] - prefix[start];
            if (range_sum > total) total = range_sum;
        }
    }
    free(prefix);
    return total;
}

/* Interleave two halves of array with checksum */
NOINLINE uint64_t *bc_16(const uint64_t *data, size_t n, size_t split, size_t *out_len) {
    if (split > n) split = n;
    uint64_t *result = (uint64_t *)malloc((n + 1) * sizeof(uint64_t));
    size_t k = 0;
    size_t i = 0, j = split;
    while (i < split || j < n) {
        if (i < split) result[k++] = data[i++];
        if (j < n) result[k++] = data[j++];
    }
    uint64_t check = 0;
    for (size_t m = 0; m < k; m++) {
        check += result[m] * ((uint64_t)m + 1);
    }
    result[k++] = check;
    *out_len = k;
    return result;
}

/* Heap sift-down: build max-heap */
NOINLINE uint64_t bc_17(uint64_t *data, size_t n) {
    uint64_t sifts = 0;
    for (size_t ii = n / 2; ii > 0; ii--) {
        size_t parent = ii - 1;
        while (1) {
            size_t left = 2 * parent + 1;
            size_t right = 2 * parent + 2;
            size_t largest = parent;
            if (left < n && data[left] > data[largest]) largest = left;
            if (right < n && data[right] > data[largest]) largest = right;
            if (largest == parent) break;
            uint64_t tmp = data[parent]; data[parent] = data[largest]; data[largest] = tmp;
            parent = largest;
            sifts++;
        }
    }
    return sifts;
}

/* Edit distance between two regions of the same array */
NOINLINE uint64_t bc_18(const uint64_t *data, size_t n, size_t split) {
    if (split > n) split = n;
    const uint64_t *a = data;
    size_t m = split;
    const uint64_t *b = data + split;
    size_t k = n - split;
    if (m == 0 || k == 0) return (uint64_t)(m + k);
    uint64_t *prev = (uint64_t *)malloc((k + 1) * sizeof(uint64_t));
    uint64_t *curr = (uint64_t *)malloc((k + 1) * sizeof(uint64_t));
    for (size_t j = 0; j <= k; j++) prev[j] = (uint64_t)j;
    for (size_t i = 1; i <= m; i++) {
        curr[0] = (uint64_t)i;
        for (size_t j = 1; j <= k; j++) {
            uint64_t cost = (a[i - 1] == b[j - 1]) ? 0 : 1;
            uint64_t del = prev[j] + 1;
            uint64_t ins = curr[j - 1] + 1;
            uint64_t sub = prev[j - 1] + cost;
            uint64_t min_val = del;
            if (ins < min_val) min_val = ins;
            if (sub < min_val) min_val = sub;
            curr[j] = min_val;
        }
        uint64_t *tmp = prev; prev = curr; curr = tmp;
    }
    uint64_t result = prev[k];
    free(prev); free(curr);
    return result;
}

/* Find longest plateau */
NOINLINE uint64_t bc_19(const uint64_t *data, size_t n, uint64_t *out_val) {
    if (n == 0) { *out_val = 0; return 0; }
    size_t best_len = 1;
    uint64_t best_val = data[0];
    size_t cur_len = 1;
    for (size_t i = 1; i < n; i++) {
        if (data[i] == data[i - 1]) {
            cur_len++;
        } else {
            if (cur_len > best_len) { best_len = cur_len; best_val = data[i - 1]; }
            cur_len = 1;
        }
    }
    if (cur_len > best_len) { best_len = cur_len; best_val = data[n - 1]; }
    *out_val = best_val;
    return (uint64_t)best_len;
}

/* Counting sort on values mod radix */
NOINLINE uint64_t *bc_20(uint64_t *data, size_t n, size_t radix, size_t *out_len) {
    *out_len = n;
    if (radix == 0) {
        uint64_t *copy = (uint64_t *)malloc(n * sizeof(uint64_t));
        memcpy(copy, data, n * sizeof(uint64_t));
        return copy;
    }
    size_t *count = (size_t *)calloc(radix, sizeof(size_t));
    for (size_t i = 0; i < n; i++) count[data[i] % radix]++;
    for (size_t i = 1; i < radix; i++) count[i] += count[i - 1];
    uint64_t *output = (uint64_t *)malloc(n * sizeof(uint64_t));
    for (size_t i = n; i > 0; i--) {
        size_t bucket = data[i - 1] % radix;
        count[bucket]--;
        output[count[bucket]] = data[i - 1];
    }
    free(count);
    return output;
}

/* ========================================================================== */
/* Category 2: Manual memory management (C equivalent of ownership/Drop)      */
/* own_01 .. own_20: no destructors, explicit free()                          */
/* ========================================================================== */

typedef struct {
    size_t rows, cols;
    uint64_t *data;
} CMatrix;

static CMatrix cmatrix_new(size_t rows, size_t cols) {
    CMatrix m;
    m.rows = rows; m.cols = cols;
    m.data = (uint64_t *)calloc(rows * cols, sizeof(uint64_t));
    return m;
}
static void cmatrix_free(CMatrix *m) {
    /* Manual zeroing (like Rust Drop impl) */
    for (size_t i = 0; i < m->rows * m->cols; i++) m->data[i] = 0;
    free(m->data);
    m->data = NULL;
}

/* Build matrix, fill Fibonacci-like, compute row sums */
NOINLINE uint64_t own_01(uint64_t n_param) {
    size_t n = (size_t)n_param;
    CMatrix mat = cmatrix_new(n, n);
    for (size_t r = 0; r < n; r++) {
        mat.data[r * n + 0] = (uint64_t)(r + 1);
        if (n > 1) mat.data[r * n + 1] = (uint64_t)(r + 2);
        for (size_t c = 2; c < n; c++) {
            mat.data[r * n + c] = mat.data[r * n + c - 1] + mat.data[r * n + c - 2];
        }
    }
    uint64_t total = 0;
    for (size_t r = 0; r < n; r++)
        for (size_t c = 0; c < n; c++)
            total += mat.data[r * n + c];
    cmatrix_free(&mat);
    return total;
}

/* Sort vec, optionally reverse, split, interleave */
NOINLINE uint64_t *own_02(uint64_t *data, size_t len, int ascending, size_t *out_len) {
    qsort(data, len, sizeof(uint64_t), cmp_u64);
    if (!ascending) {
        for (size_t i = 0; i < len / 2; i++) {
            uint64_t t = data[i]; data[i] = data[len - 1 - i]; data[len - 1 - i] = t;
        }
    }
    size_t mid = len / 2;
    uint64_t *result = (uint64_t *)malloc(len * sizeof(uint64_t));
    size_t i = 0, j = mid, k = 0;
    while (i < mid || j < len) {
        if (i < mid) result[k++] = data[i++];
        if (j < len) result[k++] = data[j++];
    }
    free(data);
    *out_len = k;
    return result;
}

/* Split string into words, rotate each, rejoin */
NOINLINE char *own_03(char *s, size_t rot) {
    size_t slen = strlen(s);
    /* Count words */
    char *copy = strdup(s);
    size_t word_count = 0;
    char *words[256]; /* max 256 words */
    char *tok = strtok(copy, " \t\n");
    while (tok && word_count < 256) { words[word_count++] = tok; tok = strtok(NULL, " \t\n"); }

    char *result = (char *)malloc(slen * 2 + 1);
    result[0] = '\0';
    for (size_t w = 0; w < word_count; w++) {
        size_t wlen = strlen(words[w]);
        char rotated[256];
        for (size_t k = 0; k < wlen && k < 255; k++) {
            rotated[k] = words[w][(k + rot) % wlen];
        }
        rotated[wlen < 255 ? wlen : 255] = '\0';
        if (w > 0) strcat(result, " ");
        strcat(result, rotated);
    }
    free(copy);
    free(s);
    return result;
}

/* Build linked list, traverse and sum */
typedef struct LNode { uint64_t val; struct LNode *next; } LNode;

NOINLINE uint64_t own_04(uint64_t n) {
    LNode *head = NULL;
    for (uint64_t i = n; i > 0; i--) {
        LNode *node = (LNode *)malloc(sizeof(LNode));
        node->val = (i - 1) * (i - 1) + 1;
        node->next = head;
        head = node;
    }
    uint64_t sum = 0, count = 0;
    LNode *cur = head;
    while (cur) { sum += cur->val; count++; cur = cur->next; }
    /* Manual free */
    while (head) { LNode *tmp = head; head = head->next; free(tmp); }
    return sum * count;
}

/* Merge two owned sorted arrays, compute running max */
NOINLINE uint64_t *own_05(uint64_t *a, size_t alen, uint64_t *b, size_t blen, size_t *out_len) {
    uint64_t *result = (uint64_t *)malloc((alen + blen) * sizeof(uint64_t));
    size_t i = 0, j = 0, k = 0;
    while (i < alen && j < blen) {
        if (a[i] <= b[j]) result[k++] = a[i++]; else result[k++] = b[j++];
    }
    while (i < alen) result[k++] = a[i++];
    while (j < blen) result[k++] = b[j++];
    uint64_t max_so_far = 0;
    for (size_t m = 0; m < k; m++) {
        if (result[m] > max_so_far) max_so_far = result[m];
        result[m] = max_so_far;
    }
    free(a); free(b);
    *out_len = k;
    return result;
}

/* Build string by interleaving chars with ASCII codes */
NOINLINE char *own_06(char *s) {
    size_t slen = strlen(s);
    char *result = (char *)malloc(slen * 5 + 1);
    size_t pos = 0;
    for (size_t i = 0; i < slen; i++) {
        result[pos++] = s[i];
        if (isalpha((unsigned char)s[i])) {
            char code[16];
            snprintf(code, sizeof(code), "%u", (unsigned int)(unsigned char)s[i]);
            size_t clen = strlen(code);
            memcpy(&result[pos], code, clen);
            pos += clen;
        }
    }
    result[pos] = '\0';
    free(s);
    return result;
}

/* Build binary tree, compute depth-weighted sum */
typedef struct TNode { uint64_t val; struct TNode *left; struct TNode *right; } TNode;

static TNode *build_tree(uint64_t d, uint64_t val) {
    if (d == 0) return NULL;
    TNode *n = (TNode *)malloc(sizeof(TNode));
    n->val = val;
    n->left = build_tree(d - 1, val * 2 + 1);
    n->right = build_tree(d - 1, val * 2 + 2);
    return n;
}
static uint64_t sum_tree_weighted(TNode *n, uint64_t depth) {
    if (!n) return 0;
    return n->val * depth + sum_tree_weighted(n->left, depth + 1) + sum_tree_weighted(n->right, depth + 1);
}
static void free_tree(TNode *n) {
    if (!n) return;
    free_tree(n->left); free_tree(n->right); free(n);
}

NOINLINE uint64_t own_07(uint64_t depth) {
    TNode *tree = build_tree(depth, 1);
    uint64_t result = sum_tree_weighted(tree, 1);
    free_tree(tree);
    return result;
}

/* Partition vec, sort both halves, compute weighted sum */
NOINLINE uint64_t own_08(uint64_t *data, size_t len, uint64_t threshold) {
    uint64_t *below = (uint64_t *)malloc(len * sizeof(uint64_t));
    uint64_t *above = (uint64_t *)malloc(len * sizeof(uint64_t));
    size_t blen = 0, alen = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i] < threshold) below[blen++] = data[i];
        else above[alen++] = data[i];
    }
    free(data);
    qsort(below, blen, sizeof(uint64_t), cmp_u64);
    qsort(above, alen, sizeof(uint64_t), cmp_u64);
    uint64_t sum = 0;
    for (size_t i = 0; i < blen; i++) sum += below[i] * ((uint64_t)i + 1);
    for (size_t i = 0; i < alen; i++) sum += above[i] * ((uint64_t)i + 10);
    free(below); free(above);
    return sum;
}

/* Build char frequency histogram, format top-N */
NOINLINE char *own_09(char *s, size_t top_n) {
    uint32_t freq[256] = {0};
    for (size_t i = 0; s[i]; i++) freq[(unsigned char)s[i]]++;
    /* Sort by frequency (insertion sort on pairs) */
    typedef struct { uint8_t ch; uint32_t cnt; } Pair;
    Pair pairs[256];
    size_t plen = 0;
    for (int i = 0; i < 256; i++) {
        if (freq[i] > 0) { pairs[plen].ch = (uint8_t)i; pairs[plen].cnt = freq[i]; plen++; }
    }
    for (size_t i = 1; i < plen; i++) {
        Pair key = pairs[i]; size_t j = i;
        while (j > 0 && pairs[j-1].cnt < key.cnt) { pairs[j] = pairs[j-1]; j--; }
        pairs[j] = key;
    }
    char *result = (char *)malloc(plen * 16 + 1);
    result[0] = '\0';
    for (size_t i = 0; i < plen && i < top_n; i++) {
        char tmp[32];
        snprintf(tmp, sizeof(tmp), "%c:%u ", pairs[i].ch, pairs[i].cnt);
        strcat(result, tmp);
    }
    free(s);
    return result;
}

/* Build array of strings, sort by length then alphabetically */
NOINLINE char **own_10(uint64_t n, size_t *out_len) {
    char **strings = (char **)malloc(n * sizeof(char *));
    for (uint64_t i = 0; i < n; i++) {
        size_t slen = (size_t)(i % 5 + 3);
        strings[i] = (char *)malloc(slen + 1);
        for (size_t j = 0; j < slen; j++) {
            strings[i][j] = (char)('a' + ((i + j) % 26));
        }
        strings[i][slen] = '\0';
    }
    /* Sort by length, then alphabetically */
    for (size_t i = 1; i < n; i++) {
        char *key = strings[i]; size_t j = i;
        while (j > 0) {
            int cmp;
            size_t la = strlen(strings[j-1]), lb = strlen(key);
            if (la != lb) cmp = (la > lb) - (la < lb);
            else cmp = strcmp(strings[j-1], key);
            if (cmp <= 0) break;
            strings[j] = strings[j-1]; j--;
        }
        strings[j] = key;
    }
    *out_len = (size_t)n;
    return strings;
}

/* Reverse, deduplicate adjacent, return both versions */
NOINLINE void own_11(uint64_t *data, size_t len, int do_reverse,
                     uint64_t **orig_out, size_t *orig_len,
                     uint64_t **dedup_out, size_t *dedup_len) {
    *orig_out = (uint64_t *)malloc(len * sizeof(uint64_t));
    memcpy(*orig_out, data, len * sizeof(uint64_t));
    *orig_len = len;
    if (do_reverse) {
        for (size_t i = 0; i < len / 2; i++) {
            uint64_t t = data[i]; data[i] = data[len-1-i]; data[len-1-i] = t;
        }
    }
    uint64_t *deduped = (uint64_t *)malloc(len * sizeof(uint64_t));
    size_t dlen = 0;
    for (size_t i = 0; i < len; i++) {
        if (i == 0 || data[i] != data[i-1]) deduped[dlen++] = data[i];
    }
    *dedup_out = deduped;
    *dedup_len = dlen;
    free(data);
}

/* Split on spaces, reverse each word, capitalize first char, rejoin */
NOINLINE char *own_12(char *s) {
    size_t slen = strlen(s);
    char *copy = strdup(s);
    char *words[256];
    size_t wcount = 0;
    char *tok = strtok(copy, " \t\n");
    while (tok && wcount < 256) { words[wcount++] = tok; tok = strtok(NULL, " \t\n"); }

    char *result = (char *)malloc(slen * 2 + 1);
    result[0] = '\0';
    for (size_t w = 0; w < wcount; w++) {
        size_t wlen = strlen(words[w]);
        char rev[256];
        for (size_t i = 0; i < wlen && i < 255; i++) rev[i] = words[w][wlen - 1 - i];
        rev[wlen < 255 ? wlen : 255] = '\0';
        if (rev[0] >= 'a' && rev[0] <= 'z') rev[0] -= 32;
        if (w > 0) strcat(result, " ");
        strcat(result, rev);
    }
    free(copy); free(s);
    return result;
}

/* Sieve of Eratosthenes */
NOINLINE uint64_t *own_13(uint64_t limit, size_t *out_len) {
    size_t n = (size_t)limit;
    *out_len = 0;
    if (n < 2) return NULL;
    char *is_prime = (char *)malloc(n + 1);
    memset(is_prime, 1, n + 1);
    is_prime[0] = 0; is_prime[1] = 0;
    for (size_t i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (size_t j = i * i; j <= n; j += i) is_prime[j] = 0;
        }
    }
    size_t count = 0;
    for (size_t i = 2; i <= n; i++) if (is_prime[i]) count++;
    uint64_t *primes = (uint64_t *)malloc(count * sizeof(uint64_t));
    size_t idx = 0;
    for (size_t i = 2; i <= n; i++) if (is_prime[i]) primes[idx++] = (uint64_t)i;
    free(is_prime);
    *out_len = count;
    return primes;
}

/* Run-length encode */
typedef struct { uint64_t val; size_t count; } RLEPair;

NOINLINE RLEPair *own_14(uint64_t *data, size_t len, size_t min_run, size_t *out_len) {
    RLEPair *runs = (RLEPair *)malloc(len * sizeof(RLEPair));
    size_t rlen = 0;
    size_t i = 0;
    while (i < len) {
        uint64_t val = data[i];
        size_t count = 1;
        while (i + count < len && data[i + count] == val) count++;
        if (count >= min_run) { runs[rlen].val = val; runs[rlen].count = count; rlen++; }
        i += count;
    }
    free(data);
    *out_len = rlen;
    return runs;
}

/* Build frequency map of chars, filter, format by frequency */
NOINLINE char *own_15(char *s, char filter_char) {
    size_t slen = strlen(s);
    /* Filter */
    char *filtered = (char *)malloc(slen + 1);
    size_t flen = 0;
    for (size_t i = 0; i < slen; i++) {
        if (s[i] != filter_char) filtered[flen++] = s[i];
    }
    filtered[flen] = '\0';
    free(s);
    /* Count frequencies */
    typedef struct { char ch; size_t cnt; } CF;
    CF freq[256]; size_t fcount = 0;
    for (size_t i = 0; i < flen; i++) {
        int found = 0;
        for (size_t j = 0; j < fcount; j++) {
            if (freq[j].ch == filtered[i]) { freq[j].cnt++; found = 1; break; }
        }
        if (!found) { freq[fcount].ch = filtered[i]; freq[fcount].cnt = 1; fcount++; }
    }
    /* Sort by frequency descending */
    for (size_t i = 1; i < fcount; i++) {
        CF key = freq[i]; size_t j = i;
        while (j > 0 && freq[j-1].cnt < key.cnt) { freq[j] = freq[j-1]; j--; }
        freq[j] = key;
    }
    char *result = (char *)malloc(flen + 1);
    size_t pos = 0;
    for (size_t i = 0; i < fcount; i++) {
        for (size_t c = 0; c < freq[i].cnt; c++) result[pos++] = freq[i].ch;
    }
    result[pos] = '\0';
    free(filtered);
    return result;
}

/* Build binary heap in array, extract top k */
NOINLINE uint64_t *own_16(uint64_t k, size_t *out_len) {
    uint64_t n = 4 * k;
    uint64_t *heap = (uint64_t *)malloc(n * sizeof(uint64_t));
    size_t hlen = 0;
    for (uint64_t i = 0; i < n; i++) {
        uint64_t val = (i * 7 + 13) % (n * 2);
        heap[hlen++] = val;
        /* Sift up */
        size_t idx = hlen - 1;
        while (idx > 0) {
            size_t parent = (idx - 1) / 2;
            if (heap[idx] > heap[parent]) {
                uint64_t t = heap[idx]; heap[idx] = heap[parent]; heap[parent] = t;
                idx = parent;
            } else break;
        }
    }
    uint64_t *result = (uint64_t *)malloc(k * sizeof(uint64_t));
    size_t rlen = 0;
    for (uint64_t i = 0; i < k && i < n; i++) {
        if (hlen == 0) break;
        uint64_t top = heap[0];
        hlen--;
        heap[0] = heap[hlen];
        result[rlen++] = top;
        /* Sift down */
        size_t idx = 0;
        while (1) {
            size_t left = 2 * idx + 1, right = 2 * idx + 2, largest = idx;
            if (left < hlen && heap[left] > heap[largest]) largest = left;
            if (right < hlen && heap[right] > heap[largest]) largest = right;
            if (largest == idx) break;
            uint64_t t = heap[idx]; heap[idx] = heap[largest]; heap[largest] = t;
            idx = largest;
        }
    }
    free(heap);
    *out_len = rlen;
    return result;
}

/* Chunk, sort each chunk descending, flatten */
NOINLINE uint64_t *own_17(uint64_t *data, size_t len, size_t chunk_size, size_t *out_len) {
    if (chunk_size == 0) { *out_len = len; return data; }
    uint64_t *result = (uint64_t *)malloc(len * sizeof(uint64_t));
    size_t pos = 0;
    for (size_t i = 0; i < len; i += chunk_size) {
        size_t clen = (i + chunk_size <= len) ? chunk_size : (len - i);
        /* Copy chunk, sort, reverse */
        uint64_t *chunk = (uint64_t *)malloc(clen * sizeof(uint64_t));
        memcpy(chunk, &data[i], clen * sizeof(uint64_t));
        qsort(chunk, clen, sizeof(uint64_t), cmp_u64);
        for (size_t j = 0; j < clen / 2; j++) {
            uint64_t t = chunk[j]; chunk[j] = chunk[clen-1-j]; chunk[clen-1-j] = t;
        }
        memcpy(&result[pos], chunk, clen * sizeof(uint64_t));
        pos += clen;
        free(chunk);
    }
    free(data);
    *out_len = pos;
    return result;
}

/* Interleave two strings char-by-char */
NOINLINE char *own_18(char *a, char *b) {
    size_t alen = strlen(a), blen = strlen(b);
    size_t max_len = alen > blen ? alen : blen;
    char *result = (char *)malloc(max_len * 2 + 1);
    size_t pos = 0;
    for (size_t i = 0; i < max_len; i++) {
        if (i < alen) result[pos++] = a[i];
        if (i < blen) result[pos++] = b[i];
    }
    result[pos] = '\0';
    /* Compute reverse */
    char *rev = (char *)malloc(pos + 1);
    for (size_t i = 0; i < pos; i++) rev[i] = result[pos - 1 - i];
    rev[pos] = '\0';
    free(a); free(b);
    char *ret = (strlen(rev) > strlen(result)) ? rev : result;
    if (ret == rev) free(result); else free(rev);
    return ret;
}

/* Build adjacency matrix, compute reachability (Floyd-Warshall) */
NOINLINE uint64_t own_19(uint64_t n_param) {
    size_t n = (size_t)n_param;
    char *adj = (char *)calloc(n * n, 1);
    for (size_t i = 0; i < n; i++) {
        if (i + 1 < n) adj[i * n + i + 1] = 1;
        if (i + 2 < n) adj[i * n + i + 2] = 1;
    }
    char *reach = (char *)malloc(n * n);
    memcpy(reach, adj, n * n);
    for (size_t k = 0; k < n; k++)
        for (size_t i = 0; i < n; i++)
            for (size_t j = 0; j < n; j++)
                if (reach[i * n + k] && reach[k * n + j])
                    reach[i * n + j] = 1;
    uint64_t count = 0;
    for (size_t i = 0; i < n * n; i++) if (reach[i]) count++;
    free(adj); free(reach);
    return count;
}

/* Sort, dedup, cumulative product */
NOINLINE uint64_t *own_20(uint64_t *data, size_t len, int do_sort, size_t *out_len) {
    if (do_sort) qsort(data, len, sizeof(uint64_t), cmp_u64);
    /* Dedup in place */
    size_t dlen = 0;
    for (size_t i = 0; i < len; i++) {
        if (dlen == 0 || data[i] != data[dlen - 1]) data[dlen++] = data[i];
    }
    uint64_t *cum = (uint64_t *)malloc(dlen * sizeof(uint64_t));
    uint64_t prod = 1;
    for (size_t i = 0; i < dlen; i++) {
        prod *= (data[i] + 1);
        cum[i] = prod;
    }
    free(data);
    *out_len = dlen;
    return cum;
}

/* ========================================================================== */
/* Category 3: Return-code style (C equivalent of Option/Result)              */
/* opt_01 .. opt_20: sentinel values, error codes, no discriminant tags       */
/* ========================================================================== */

#define NOT_FOUND UINT64_MAX

/* Binary search, probe neighbors */
NOINLINE uint64_t opt_01(const uint64_t *data, size_t len, uint64_t target) {
    size_t lo = 0, hi = len;
    size_t found = NOT_FOUND;
    while (lo < hi) {
        size_t mid = lo + (hi - lo) / 2;
        if (data[mid] == target) { found = mid; break; }
        else if (data[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    if (found != NOT_FOUND) {
        uint64_t left = (found > 0) ? data[found - 1] : 0;
        uint64_t right = (found + 1 < len) ? data[found + 1] : 0;
        return left + data[found] + right;
    }
    /* Return nearest */
    if (lo < len) return data[lo];
    if (len > 0) return data[len - 1];
    return 0;
}

/* Split on delimiter, parse segments */
NOINLINE uint64_t opt_02(const char *s, char delim) {
    uint64_t count = 0, total = 0;
    uint64_t max_val = 0;
    int has_max = 0;
    const char *p = s;
    while (*p) {
        /* Skip delimiters */
        while (*p == delim) p++;
        if (!*p) break;
        /* Find end of token */
        const char *start = p;
        while (*p && *p != delim) p++;
        /* Skip leading/trailing spaces */
        while (start < p && (*start == ' ' || *start == '\t')) start++;
        const char *end = p;
        while (end > start && (*(end-1) == ' ' || *(end-1) == '\t')) end--;
        if (start == end) continue;
        /* Try parse as number */
        char buf[64];
        size_t tlen = (size_t)(end - start);
        if (tlen >= 64) tlen = 63;
        memcpy(buf, start, tlen);
        buf[tlen] = '\0';
        char *endptr;
        unsigned long long val = strtoull(buf, &endptr, 10);
        if (*endptr == '\0' && tlen > 0) {
            count++;
            total += val;
            if (!has_max || val > max_val) { max_val = val; has_max = 1; }
        } else {
            count += tlen;
        }
    }
    return total + (has_max ? max_val : 0) + count;
}

/* Process array of optional u64 (has_value + value), running sum */
typedef struct { int has_value; uint64_t value; } OptU64;

NOINLINE uint64_t opt_03(const OptU64 *data, size_t len) {
    uint64_t sum = 0;
    int has_prev = 0;
    uint64_t prev_val = 0;
    uint64_t transitions = 0;
    for (size_t i = 0; i < len; i++) {
        if (has_prev && data[i].has_value) {
            sum += data[i].value;
            if (data[i].value > prev_val) transitions++;
            prev_val = data[i].value;
        } else if (!has_prev && data[i].has_value) {
            sum += data[i].value;
            transitions++;
            prev_val = data[i].value;
            has_prev = 1;
        } else if (has_prev && !data[i].has_value) {
            transitions++;
            has_prev = 0;
        }
    }
    return sum * (transitions + 1);
}

/* Sliding window search: find first window where all > target */
NOINLINE int opt_04(const uint64_t *data, size_t len, uint64_t target,
                    size_t *out_start, uint64_t *out_sum) {
    size_t win_size = 3;
    if (len < win_size) return 0;
    for (size_t start = 0; start + win_size <= len; start++) {
        int all_above = 1;
        uint64_t win_sum = 0;
        for (size_t j = 0; j < win_size; j++) {
            win_sum += data[start + j];
            if (data[start + j] <= target) all_above = 0;
        }
        if (all_above) {
            *out_start = start;
            *out_sum = win_sum;
            return 1;
        }
    }
    return 0;
}

/* Parse tokens: numbers ok, words error, compute stats */
NOINLINE uint64_t opt_05(const char *s, size_t limit) {
    uint64_t *numbers = (uint64_t *)malloc(limit * sizeof(uint64_t));
    size_t ncount = 0;
    uint64_t errors = 0;
    size_t count = 0;
    const char *p = s;
    while (*p && count < limit) {
        while (*p == ' ') p++;
        if (!*p) break;
        const char *start = p;
        while (*p && *p != ' ') p++;
        char buf[64];
        size_t tlen = (size_t)(p - start);
        if (tlen >= 64) tlen = 63;
        memcpy(buf, start, tlen); buf[tlen] = '\0';
        char *endptr;
        unsigned long long val = strtoull(buf, &endptr, 10);
        if (*endptr == '\0' && tlen > 0) {
            if (ncount < limit) numbers[ncount++] = (uint64_t)val;
        } else {
            errors++;
        }
        count++;
    }
    if (ncount == 0) { free(numbers); return errors; }
    qsort(numbers, ncount, sizeof(uint64_t), cmp_u64);
    uint64_t median = numbers[ncount / 2];
    uint64_t sum = 0;
    for (size_t i = 0; i < ncount; i++) sum += numbers[i];
    free(numbers);
    return sum + median + errors;
}

/* Chain of transformations: find even, double, clamp, fallback */
NOINLINE uint64_t opt_06(const uint64_t *data, size_t len) {
    /* Find first even */
    uint64_t first_even = 0; int found_even = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i] % 2 == 0) { first_even = data[i]; found_even = 1; break; }
    }
    uint64_t doubled = found_even ? first_even * 2 : 0;
    uint64_t clamped = (found_even && doubled < 100) ? doubled : 0;
    uint64_t base = (found_even && doubled < 100) ? clamped : 42;

    /* Find last odd */
    uint64_t last_odd = 0; int found_odd = 0;
    for (size_t i = len; i > 0; i--) {
        if (data[i-1] % 2 == 1) { last_odd = data[i-1]; found_odd = 1; break; }
    }
    uint64_t tripled = found_odd ? last_odd * 3 : 0;
    uint64_t extra = (found_odd && tripled < 200) ? tripled : 7;

    return base + extra;
}

/* Parse key=value pairs */
NOINLINE uint64_t opt_07(const char *s) {
    uint64_t total = 0, count = 0;
    const char *p = s;
    while (*p) {
        while (*p == ' ' || *p == '\t') p++;
        if (!*p) break;
        const char *start = p;
        while (*p && *p != ' ' && *p != '\t') p++;
        size_t tlen = (size_t)(p - start);
        /* Look for '=' */
        const char *eq = NULL;
        for (size_t i = 0; i < tlen; i++) {
            if (start[i] == '=') { eq = start + i; break; }
        }
        if (eq) {
            const char *val_start = eq + 1;
            size_t vlen = tlen - (size_t)(val_start - start);
            char buf[64];
            if (vlen >= 64) vlen = 63;
            memcpy(buf, val_start, vlen); buf[vlen] = '\0';
            char *endptr;
            unsigned long long v = strtoull(buf, &endptr, 10);
            if (*endptr == '\0' && vlen > 0) {
                total += v; count++;
            } else {
                total += (size_t)(eq - start);
            }
        } else {
            if (tlen > 0) total += (unsigned char)start[0];
        }
    }
    return total * (count + 1);
}

/* Process array of results (is_ok, value/error_len), accumulate with streaks */
typedef struct { int is_ok; uint64_t value; size_t err_len; } ResU64;

NOINLINE uint64_t opt_08(const ResU64 *data, size_t len) {
    uint64_t sum = 0;
    uint64_t err_streak = 0, max_streak = 0;
    int has_last_ok = 0;
    uint64_t last_ok = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i].is_ok) {
            if (err_streak > max_streak) max_streak = err_streak;
            err_streak = 0;
            sum += data[i].value;
            last_ok = has_last_ok ? (last_ok + data[i].value) : data[i].value;
            has_last_ok = 1;
        } else {
            err_streak++;
            sum += (uint64_t)data[i].err_len;
        }
    }
    if (err_streak > max_streak) max_streak = err_streak;
    return sum + max_streak + (has_last_ok ? last_ok : 0);
}

/* Two-pointer search */
NOINLINE int opt_09(const uint64_t *data, size_t len, uint64_t target_sum,
                    size_t *out_lo, size_t *out_hi) {
    if (len < 2) return 0;
    size_t lo = 0, hi = len - 1;
    while (lo < hi) {
        uint64_t sum = data[lo] + data[hi];
        if (sum == target_sum) { *out_lo = lo; *out_hi = hi; return 1; }
        else if (sum < target_sum) lo++;
        else hi--;
    }
    return 0;
}

/* Extract nth word, then nth char */
NOINLINE uint64_t opt_10(const char *s, size_t n) {
    /* Forward: nth word */
    const char *p = s;
    size_t word_idx = 0;
    uint64_t code = 0;
    while (*p) {
        while (*p == ' ') p++;
        if (!*p) break;
        const char *wstart = p;
        while (*p && *p != ' ') p++;
        if (word_idx == n) {
            size_t wlen = (size_t)(p - wstart);
            if (wlen > 0) {
                size_t ci = n % wlen;
                code = (uint64_t)(unsigned char)wstart[ci];
            }
            break;
        }
        word_idx++;
    }
    /* Backward: collect words then pick nth from end */
    const char *words[256];
    size_t wlens[256], wcount = 0;
    p = s;
    while (*p && wcount < 256) {
        while (*p == ' ') p++;
        if (!*p) break;
        words[wcount] = p;
        while (*p && *p != ' ') p++;
        wlens[wcount] = (size_t)(p - words[wcount]);
        wcount++;
    }
    uint64_t rcode = 0;
    if (n < wcount) {
        size_t ri = wcount - 1 - n;
        size_t wlen = wlens[ri];
        if (wlen > 0) {
            size_t ci = n % wlen;
            rcode = (uint64_t)(unsigned char)words[ri][wlen - 1 - ci];
        }
    }
    return code + rcode;
}

/* Find adjacent pair with gap > 5 */
NOINLINE uint64_t opt_11(const uint64_t *data, size_t n) {
    uint64_t asc_sum = 0, desc_sum = 0;
    for (size_t i = 0; i + 1 < n; i++) {
        if (data[i + 1] > data[i] + 5) { asc_sum = data[i] + data[i + 1]; break; }
    }
    for (size_t i = 0; i + 1 < n; i++) {
        if (data[i] > data[i + 1] + 5) { desc_sum = data[i] + data[i + 1]; break; }
    }
    return asc_sum + desc_sum;
}

/* Threshold filtering on optional values */
NOINLINE uint64_t opt_12(const OptU64 *data, size_t len, uint64_t threshold) {
    uint64_t above = 0, below = 0, none_count = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i].has_value) {
            if (data[i].value > threshold) above += data[i].value;
            else below += data[i].value;
        } else {
            none_count++;
        }
    }
    return above * 2 + below + none_count * 100;
}

/* Chained access with step, cascading fallback */
NOINLINE uint64_t opt_13(const uint64_t *data, size_t len, size_t step) {
    size_t idx = 0;
    uint64_t acc = 0, hops = 0;
    while (idx < len) {
        acc += data[idx];
        hops++;
        size_t next = idx + step;
        if (next >= len || (next <= idx && step == 0)) break;
        idx = next;
    }
    return acc * hops;
}

/* Parse multiple number formats */
NOINLINE uint64_t opt_14(const char *s) {
    uint64_t total = 0, parsed = 0, failed = 0;
    const char *p = s;
    while (*p) {
        while (*p == ' ') p++;
        if (!*p) break;
        const char *start = p;
        while (*p && *p != ' ') p++;
        char buf[64];
        size_t tlen = (size_t)(p - start);
        if (tlen >= 64) tlen = 63;
        memcpy(buf, start, tlen); buf[tlen] = '\0';

        char *endptr;
        unsigned long long val;
        if (tlen > 2 && buf[0] == '0' && buf[1] == 'x') {
            val = strtoull(buf + 2, &endptr, 16);
        } else if (tlen > 2 && buf[0] == '0' && buf[1] == 'b') {
            val = strtoull(buf + 2, &endptr, 2);
        } else {
            val = strtoull(buf, &endptr, 10);
        }
        if (*endptr == '\0' && ((tlen > 2 && (buf[1] == 'x' || buf[1] == 'b')) || tlen > 0)) {
            /* Check that we actually parsed something */
            if (endptr != buf && !(tlen > 2 && endptr == buf + 2)) {
                total += val; parsed++;
            } else {
                failed++;
            }
        } else {
            failed++;
        }
    }
    return total + parsed * 10 + failed;
}

/* Sliding window with boundary handling */
NOINLINE uint64_t opt_15(const uint64_t *data, size_t len, size_t window) {
    uint64_t best_sum = 0;
    size_t best_start = NOT_FOUND;
    if (window == 0 || window > len) return 0;
    for (size_t start = 0; start + window <= len; start++) {
        uint64_t win_sum = 0;
        for (size_t j = 0; j < window; j++) win_sum += data[start + j];
        if (win_sum > best_sum) { best_sum = win_sum; best_start = start; }
    }
    return best_sum + (best_start != NOT_FOUND ? (uint64_t)best_start : 0);
}

/* Running positive/negative balance */
NOINLINE int64_t opt_16(const int64_t *ok_vals, const int *is_ok, size_t len) {
    int64_t balance = 0, max_balance = 0, min_balance = 0;
    int has_last = 0; int64_t last_valid = 0;
    for (size_t i = 0; i < len; i++) {
        if (is_ok[i]) {
            balance += ok_vals[i];
            if (balance > max_balance) max_balance = balance;
            if (balance < min_balance) min_balance = balance;
            last_valid = balance; has_last = 1;
        } else {
            balance = has_last ? last_valid : 0;
        }
    }
    return max_balance - min_balance + (has_last ? last_valid : 0);
}

/* Find k-th element */
NOINLINE uint64_t opt_17(const uint64_t *data, size_t len, size_t k) {
    uint64_t *sorted = (uint64_t *)malloc(len * sizeof(uint64_t));
    memcpy(sorted, data, len * sizeof(uint64_t));
    qsort(sorted, len, sizeof(uint64_t), cmp_u64);
    uint64_t kth = (k < len) ? sorted[k] : 0;
    size_t rev_idx = (len > k + 1) ? (len - k - 1) : 0;
    uint64_t rev_kth = (rev_idx < len) ? sorted[rev_idx] : 0;
    uint64_t median = (len > 0) ? sorted[len / 2] : 0;
    free(sorted);
    return kth + rev_kth + median;
}

/* Longest and shortest word */
NOINLINE uint64_t opt_18(const char *s) {
    const char *words[256]; size_t wlens[256]; size_t wcount = 0;
    const char *p = s;
    while (*p && wcount < 256) {
        while (*p == ' ') p++;
        if (!*p) break;
        words[wcount] = p;
        while (*p && *p != ' ') p++;
        wlens[wcount] = (size_t)(p - words[wcount]);
        wcount++;
    }
    size_t longest = 0, shortest = (size_t)-1, mid_len = 0;
    for (size_t i = 0; i < wcount; i++) {
        if (wlens[i] > longest) longest = wlens[i];
        if (wlens[i] < shortest) shortest = wlens[i];
    }
    if (wcount == 0) shortest = 0;
    if (wcount > 0) mid_len = wlens[wcount / 2];
    return (uint64_t)longest * 100 + (uint64_t)shortest + (uint64_t)mid_len;
}

/* Binary search returning index or insertion point */
NOINLINE uint64_t opt_19(const uint64_t *data, size_t len, uint64_t target) {
    size_t lo = 0, hi = len;
    int found = 0;
    size_t result_idx = lo;
    while (lo < hi) {
        size_t mid = lo + (hi - lo) / 2;
        if (data[mid] == target) { found = 1; result_idx = mid; break; }
        else if (data[mid] < target) { lo = mid + 1; result_idx = lo; }
        else { hi = mid; result_idx = hi; }
    }
    if (found) return (uint64_t)result_idx * 1000;
    return (uint64_t)result_idx;
}

/* Parse CSV-like string */
NOINLINE uint64_t opt_20(const char *s) {
    uint64_t sum = 0, count = 0;
    uint64_t max_val = 0, min_val = 0;
    int has_max = 0, has_min = 0;
    const char *p = s;
    while (*p) {
        while (*p == ',') p++;
        if (!*p) break;
        const char *start = p;
        while (*p && *p != ',') p++;
        /* Trim spaces */
        while (start < p && *start == ' ') start++;
        const char *end = p;
        while (end > start && *(end-1) == ' ') end--;
        size_t tlen = (size_t)(end - start);
        if (tlen == 0) continue;
        char buf[64];
        if (tlen >= 64) tlen = 63;
        memcpy(buf, start, tlen); buf[tlen] = '\0';
        char *endptr;
        unsigned long long val = strtoull(buf, &endptr, 10);
        if (*endptr == '\0') {
            sum += val; count++;
            if (!has_max || val > max_val) { max_val = val; has_max = 1; }
            if (!has_min || val < min_val) { min_val = val; has_min = 1; }
        }
    }
    uint64_t range = (has_max && has_min) ? max_val - min_val : 0;
    return sum + range + count;
}

/* ========================================================================== */
/* Category 4: Explicit loops (C equivalent of iterator chains)               */
/* iter_01 .. iter_20: hand-written loops, no state machine lowering          */
/* ========================================================================== */

/* Filter, enumerate, weighted sum + product of first 5 */
NOINLINE uint64_t iter_01(const uint64_t *data, size_t len, uint64_t threshold) {
    size_t *indices = (size_t *)malloc(len * sizeof(size_t));
    uint64_t *values = (uint64_t *)malloc(len * sizeof(uint64_t));
    size_t acount = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i] > threshold) { indices[acount] = i; values[acount] = data[i]; acount++; }
    }
    uint64_t sum = 0;
    for (size_t i = 0; i < acount; i++) sum += values[i] * ((uint64_t)indices[i] + 1);
    uint64_t prod = 1;
    for (size_t i = 0; i < acount && i < 5; i++) prod *= values[i];
    free(indices); free(values);
    return sum + prod;
}

/* Zip, weighted dot product with running max */
NOINLINE uint64_t iter_02(const uint64_t *a, size_t alen, const uint64_t *b, size_t blen) {
    size_t len = alen < blen ? alen : blen;
    uint64_t dot = 0, max_product = 0, count = 0;
    for (size_t i = 0; i < len; i++) {
        uint64_t weight = ((uint64_t)i + 1);
        if (weight > 10) weight = 10;
        uint64_t product = a[i] * b[i];
        dot += product * weight;
        if (product > max_product) max_product = product;
        count++;
    }
    return dot + max_product + count;
}

/* Windows + map + filter: window sums, count above average */
NOINLINE uint64_t iter_03(const uint64_t *data, size_t len, size_t window) {
    if (window == 0 || window > len) return 0;
    size_t wcount = len - window + 1;
    uint64_t *wsums = (uint64_t *)malloc(wcount * sizeof(uint64_t));
    for (size_t i = 0; i < wcount; i++) {
        uint64_t s = 0;
        for (size_t j = 0; j < window; j++) s += data[i + j];
        wsums[i] = s;
    }
    uint64_t total = 0;
    for (size_t i = 0; i < wcount; i++) total += wsums[i];
    uint64_t avg = wcount > 0 ? total / wcount : 0;
    uint64_t above_avg = 0;
    for (size_t i = 0; i < wcount; i++) if (wsums[i] > avg) above_avg++;
    free(wsums);
    return total + above_avg;
}

/* Character frequency analysis */
NOINLINE uint64_t iter_04(const char *s) {
    uint64_t freq[256] = {0};
    for (size_t i = 0; s[i]; i++) freq[(unsigned char)s[i]]++;
    uint64_t max_freq = 0, unique = 0, total = 0, entropy_sum = 0;
    for (int i = 0; i < 256; i++) {
        if (freq[i] > max_freq) max_freq = freq[i];
        if (freq[i] > 0) unique++;
        total += freq[i];
        if (freq[i] > 0) entropy_sum += freq[i] * freq[i];
    }
    return max_freq + unique + total + entropy_sum;
}

/* Chunk, compute sum+range per chunk, running peak */
NOINLINE uint64_t iter_05(const uint64_t *data, size_t len) {
    uint64_t running = 0, peak = 0;
    for (size_t i = 0; i < len; i += 4) {
        size_t end = i + 4;
        if (end > len) end = len;
        uint64_t sum = 0, mx = data[i], mn = data[i];
        for (size_t j = i; j < end; j++) {
            sum += data[j];
            if (data[j] > mx) mx = data[j];
            if (data[j] < mn) mn = data[j];
        }
        running += sum + (mx - mn);
        if (running > peak) peak = running;
    }
    return peak;
}

/* Step_by + enumerate + stateful accumulation */
NOINLINE uint64_t iter_06(const uint64_t *data, size_t len, size_t step) {
    if (step == 0) return 0;
    uint64_t state = 0, result = 0;
    size_t idx = 0;
    for (size_t i = 0; i < len; i += step) {
        state += data[i];
        if (state > (uint64_t)idx * 10) result += state;
        idx++;
    }
    return result;
}

/* Split string, map to lengths, filter long, fold */
NOINLINE uint64_t iter_07(const char *s, char delim) {
    size_t lengths[256]; size_t pcount = 0;
    const char *p = s;
    while (*p && pcount < 256) {
        const char *start = p;
        while (*p && *p != delim) p++;
        /* Trim */
        const char *ts = start;
        while (ts < p && (*ts == ' ' || *ts == '\t')) ts++;
        const char *te = p;
        while (te > ts && (*(te-1) == ' ' || *(te-1) == '\t')) te--;
        lengths[pcount++] = (size_t)(te - ts);
        if (*p) p++;
    }
    uint64_t long_count = 0, total_len = 0, max_len = 0;
    for (size_t i = 0; i < pcount; i++) {
        if (lengths[i] > 3) long_count++;
        total_len += lengths[i];
        if (lengths[i] > max_len) max_len = lengths[i];
    }
    return long_count * max_len + total_len;
}

/* Chain, skip, take_while, weighted sum */
NOINLINE uint64_t iter_08(const uint64_t *data, size_t len, size_t split) {
    if (split > len) split = len;
    /* Chain is just the whole array in order; skip 2, take_while < 50 */
    size_t start = 2;
    uint64_t weighted_sum = 0;
    size_t count = 0;
    for (size_t i = start; i < len; i++) {
        if (data[i] >= 50) break;
        weighted_sum += data[i] * ((uint64_t)count + 1);
        count++;
    }
    return weighted_sum + (uint64_t)count;
}

/* Peekable: detect ascending runs */
NOINLINE uint64_t iter_09(const uint64_t *data, size_t len) {
    uint64_t ascending_runs = 0, current_run = 1, max_run = 0;
    for (size_t i = 0; i + 1 < len; i++) {
        if (data[i + 1] > data[i]) {
            current_run++;
        } else {
            if (current_run > max_run) max_run = current_run;
            if (current_run > 1) ascending_runs++;
            current_run = 1;
        }
    }
    if (current_run > max_run) max_run = current_run;
    if (current_run > 1) ascending_runs++;
    return max_run * ascending_runs;
}

/* Flat_map with conditional expansion */
NOINLINE uint64_t iter_10(const uint64_t *data, size_t len, uint64_t factor) {
    uint64_t *expanded = (uint64_t *)malloc(len * 2 * sizeof(uint64_t));
    size_t elen = 0;
    for (size_t i = 0; i < len; i++) {
        expanded[elen++] = data[i];
        if (data[i] % 2 == 0) expanded[elen++] = data[i] * factor;
    }
    uint64_t sum = 0, prev = 0;
    for (size_t i = 0; i < elen; i++) {
        sum += expanded[i] - prev;
        prev = expanded[i];
    }
    free(expanded);
    return sum + (uint64_t)elen;
}

/* Multi-pass string analysis */
NOINLINE uint64_t iter_11(const char *s) {
    const char *words[256]; size_t wlens[256]; size_t wcount = 0;
    const char *p = s;
    while (*p && wcount < 256) {
        while (*p == ' ') p++;
        if (!*p) break;
        words[wcount] = p;
        while (*p && *p != ' ') p++;
        wlens[wcount] = (size_t)(p - words[wcount]);
        wcount++;
    }
    uint64_t total_chars = 0;
    for (size_t i = 0; i < wcount; i++) total_chars += wlens[i];
    uint64_t vowel_words = 0;
    for (size_t i = 0; i < wcount; i++) {
        for (size_t j = 0; j < wlens[i]; j++) {
            char c = words[i][j];
            if (c=='a'||c=='e'||c=='i'||c=='o'||c=='u'||
                c=='A'||c=='E'||c=='I'||c=='O'||c=='U') { vowel_words++; break; }
        }
    }
    uint64_t longest = 0;
    for (size_t i = 0; i < wcount; i++) if (wlens[i] > longest) longest = wlens[i];
    uint64_t cap_count = 0;
    for (size_t i = 0; i < wcount; i++)
        for (size_t j = 0; j < wlens[i]; j++)
            if (words[i][j] >= 'A' && words[i][j] <= 'Z') cap_count++;
    return total_chars + vowel_words * 10 + longest + cap_count;
}

/* Scan (running sum) with threshold crossing detection */
NOINLINE uint64_t iter_12(const uint64_t *data, size_t len, uint64_t threshold) {
    uint64_t *running = (uint64_t *)malloc(len * sizeof(uint64_t));
    uint64_t state = 0;
    for (size_t i = 0; i < len; i++) { state += data[i]; running[i] = state; }
    uint64_t crossings = 0;
    for (size_t i = 0; i + 1 < len; i++) {
        if ((running[i] < threshold) != (running[i + 1] < threshold)) crossings++;
    }
    uint64_t final_val = (len > 0) ? running[len - 1] : 0;
    free(running);
    return final_val + crossings * 100;
}

/* Zip, diff, statistics */
NOINLINE uint64_t iter_13(const uint64_t *a, size_t alen, const uint64_t *b, size_t blen) {
    size_t len = alen < blen ? alen : blen;
    uint64_t positive = 0, negative = 0, abs_sum = 0;
    for (size_t i = 0; i < len; i++) {
        int64_t d = (int64_t)a[i] - (int64_t)b[i];
        if (d > 0) positive++;
        else if (d < 0) negative++;
        abs_sum += (uint64_t)(d < 0 ? -d : d);
    }
    return positive * 100 + negative + abs_sum;
}

/* Enumerate + filter_map + fold */
NOINLINE uint64_t iter_14(const uint64_t *data, size_t len) {
    uint64_t result = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i] > (uint64_t)i) {
            uint64_t v = data[i] - (uint64_t)i;
            result += v * v;
        }
    }
    uint64_t rev_result = 0;
    for (size_t i = 0; i < len; i++) {
        size_t ri = len - 1 - i;
        if (i > 0 && data[ri] % (uint64_t)i == 0) rev_result += data[ri];
    }
    return result + rev_result;
}

/* Split, rotate lengths, pair-multiply, sum */
NOINLINE uint64_t iter_15(const char *s, size_t n) {
    size_t lengths[256]; size_t wcount = 0;
    const char *p = s;
    while (*p && wcount < 256) {
        while (*p == ' ') p++;
        if (!*p) break;
        const char *start = p;
        while (*p && *p != ' ') p++;
        lengths[wcount++] = (size_t)(p - start);
    }
    /* Shifted = skip n, then take n from start */
    size_t shifted[256];
    for (size_t i = 0; i < wcount; i++) {
        shifted[i] = lengths[(i + n) % wcount];
    }
    uint64_t paired = 0;
    for (size_t i = 0; i < wcount; i++) {
        paired += (uint64_t)lengths[i] * (uint64_t)shifted[i];
    }
    return paired + (uint64_t)wcount;
}

/* Group consecutive, sum + max per group */
NOINLINE uint64_t iter_16(const uint64_t *data, size_t len, size_t group_size) {
    if (group_size == 0) return 0;
    uint64_t total = 0;
    for (size_t i = 0; i < len; i += group_size) {
        size_t end = i + group_size;
        if (end > len) end = len;
        uint64_t sum = 0, mx = data[i];
        for (size_t j = i; j < end; j++) {
            sum += data[j];
            if (data[j] > mx) mx = data[j];
        }
        total += sum + mx;
    }
    return total;
}

/* Dedup with counting */
NOINLINE uint64_t iter_17(const uint64_t *data, size_t len) {
    uint64_t *sorted = (uint64_t *)malloc(len * sizeof(uint64_t));
    memcpy(sorted, data, len * sizeof(uint64_t));
    qsort(sorted, len, sizeof(uint64_t), cmp_u64);
    uint64_t result = 0;
    size_t i = 0;
    while (i < len) {
        uint64_t val = sorted[i];
        uint64_t count = 0;
        while (i < len && sorted[i] == val) { count++; i++; }
        if (count > 1) result += val * count;
    }
    free(sorted);
    return result;
}

/* Rev + skip + take + enumerate + fold */
NOINLINE uint64_t iter_18(const uint64_t *data, size_t len, size_t k) {
    /* Reverse, skip k, take 2*k */
    uint64_t weighted = 0, max_val = 0;
    size_t count = 0;
    if (k >= len) { return 0; }
    size_t start = len - 1 - k;  /* after skipping k from reversed */
    size_t take = k * 2;
    for (size_t i = 0; i < take && start >= i; i++) {
        size_t idx = start - i;
        weighted += data[idx] * ((uint64_t)count + 1);
        if (data[idx] > max_val) max_val = data[idx];
        count++;
        if (idx == 0) break;
    }
    return weighted + max_val;
}

/* Multi-pass byte analysis */
NOINLINE uint64_t iter_19(const char *s) {
    uint64_t alpha = 0, digit = 0, space = 0, xor_sum = 0, byte_sum = 0;
    for (size_t i = 0; s[i]; i++) {
        unsigned char b = (unsigned char)s[i];
        if (isalpha(b)) alpha++;
        if (isdigit(b)) digit++;
        if (isspace(b)) space++;
        xor_sum ^= (uint64_t)b;
        byte_sum += (uint64_t)b;
    }
    return alpha * 100 + digit * 10 + space + xor_sum + byte_sum;
}

/* Partition by modulus, weighted sums */
NOINLINE uint64_t iter_20(const uint64_t *data, size_t len, uint64_t modulus) {
    if (modulus == 0) return 0;
    uint64_t even_sum = 0, odd_sum = 0;
    size_t ei = 0, oi = 0;
    for (size_t i = 0; i < len; i++) {
        if (data[i] % modulus == 0) {
            even_sum += data[i] * ((uint64_t)ei + 1);
            ei++;
        } else {
            odd_sum += data[i] + (uint64_t)oi;
            oi++;
        }
    }
    return even_sum + odd_sum;
}

/* ========================================================================== */
/* Category 5: Tagged unions (C equivalent of Rust enums)                     */
/* em_01 .. em_20: manual tag + union, switch dispatch                        */
/* ========================================================================== */

enum TokenTag { TOK_NUM, TOK_IDENT, TOK_PLUS, TOK_MINUS, TOK_STAR, TOK_SLASH, TOK_LPAREN, TOK_RPAREN, TOK_EOF };
typedef struct {
    enum TokenTag tag;
    union {
        int64_t number;
        char ident[64];
    };
} CToken;

enum ExprTag { EXPR_LIT, EXPR_VAR, EXPR_BINOP, EXPR_UNARY_MINUS, EXPR_CALL };
enum OpTag { OP_ADD, OP_SUB, OP_MUL, OP_DIV };
typedef struct CExpr {
    enum ExprTag tag;
    union {
        int64_t lit;
        char var[64];
        struct { struct CExpr *left; enum OpTag op; struct CExpr *right; } binop;
        struct CExpr *inner;
        struct { char name[64]; struct CExpr **args; size_t nargs; } call;
    };
} CExpr;

enum CmdTag { CMD_SET, CMD_ADD, CMD_PRINT, CMD_IF };
enum CValTag { CVAL_INT, CVAL_STR, CVAL_LIST };
typedef struct {
    enum CValTag tag;
    union {
        int64_t int_val;
        char str_val[128];
        struct { int64_t *items; size_t len; } list;
    };
} CCVal;

typedef struct CCmd {
    enum CmdTag tag;
    union {
        struct { char name[64]; CCVal val; } set;
        struct { char a[64]; char b[64]; char dst[64]; } add;
        char print_name[64];
        struct { char cond[64]; struct CCmd *then_cmds; size_t then_len; struct CCmd *else_cmds; size_t else_len; } if_cmd;
    };
} CCmd;

/* Lexer */
NOINLINE CToken *c_lex(const char *input, size_t *out_len) {
    CToken *tokens = (CToken *)malloc(256 * sizeof(CToken));
    size_t count = 0;
    size_t i = 0, slen = strlen(input);
    while (i < slen && count < 255) {
        if (input[i] == ' ' || input[i] == '\t') { i++; continue; }
        switch (input[i]) {
            case '+': tokens[count].tag = TOK_PLUS; count++; i++; break;
            case '-': tokens[count].tag = TOK_MINUS; count++; i++; break;
            case '*': tokens[count].tag = TOK_STAR; count++; i++; break;
            case '/': tokens[count].tag = TOK_SLASH; count++; i++; break;
            case '(': tokens[count].tag = TOK_LPAREN; count++; i++; break;
            case ')': tokens[count].tag = TOK_RPAREN; count++; i++; break;
            default:
                if (input[i] >= '0' && input[i] <= '9') {
                    size_t start = i;
                    while (i < slen && input[i] >= '0' && input[i] <= '9') i++;
                    char buf[32]; size_t bl = i - start;
                    if (bl >= 32) bl = 31;
                    memcpy(buf, &input[start], bl); buf[bl] = '\0';
                    tokens[count].tag = TOK_NUM;
                    tokens[count].number = atoll(buf);
                    count++;
                } else if (isalpha((unsigned char)input[i]) || input[i] == '_') {
                    size_t start = i;
                    while (i < slen && (isalnum((unsigned char)input[i]) || input[i] == '_')) i++;
                    size_t bl = i - start;
                    if (bl >= 64) bl = 63;
                    memcpy(tokens[count].ident, &input[start], bl);
                    tokens[count].ident[bl] = '\0';
                    tokens[count].tag = TOK_IDENT;
                    count++;
                } else { i++; }
        }
    }
    tokens[count].tag = TOK_EOF;
    count++;
    *out_len = count;
    return tokens;
}

/* Parser helpers */
static CExpr *c_parse_add(const CToken *tokens, size_t len, size_t *pos);
static CExpr *c_parse_mul(const CToken *tokens, size_t len, size_t *pos);
static CExpr *c_parse_atom(const CToken *tokens, size_t len, size_t *pos);

static CExpr *c_parse_atom(const CToken *tokens, size_t len, size_t *pos) {
    if (*pos >= len) { CExpr *e = (CExpr*)calloc(1,sizeof(CExpr)); e->tag = EXPR_LIT; return e; }
    CExpr *e = (CExpr *)calloc(1, sizeof(CExpr));
    switch (tokens[*pos].tag) {
        case TOK_NUM:
            e->tag = EXPR_LIT; e->lit = tokens[*pos].number; (*pos)++;
            return e;
        case TOK_IDENT:
            e->tag = EXPR_VAR; strcpy(e->var, tokens[*pos].ident); (*pos)++;
            return e;
        case TOK_MINUS:
            (*pos)++;
            e->tag = EXPR_UNARY_MINUS; e->inner = c_parse_atom(tokens, len, pos);
            return e;
        case TOK_LPAREN:
            (*pos)++;
            free(e);
            e = c_parse_add(tokens, len, pos);
            if (*pos < len && tokens[*pos].tag == TOK_RPAREN) (*pos)++;
            return e;
        default:
            e->tag = EXPR_LIT;
            return e;
    }
}

static CExpr *c_parse_mul(const CToken *tokens, size_t len, size_t *pos) {
    CExpr *left = c_parse_atom(tokens, len, pos);
    while (*pos < len) {
        if (tokens[*pos].tag == TOK_STAR || tokens[*pos].tag == TOK_SLASH) {
            enum OpTag op = (tokens[*pos].tag == TOK_STAR) ? OP_MUL : OP_DIV;
            (*pos)++;
            CExpr *right = c_parse_atom(tokens, len, pos);
            CExpr *node = (CExpr *)calloc(1, sizeof(CExpr));
            node->tag = EXPR_BINOP; node->binop.left = left; node->binop.op = op; node->binop.right = right;
            left = node;
        } else break;
    }
    return left;
}

static CExpr *c_parse_add(const CToken *tokens, size_t len, size_t *pos) {
    CExpr *left = c_parse_mul(tokens, len, pos);
    while (*pos < len) {
        if (tokens[*pos].tag == TOK_PLUS || tokens[*pos].tag == TOK_MINUS) {
            enum OpTag op = (tokens[*pos].tag == TOK_PLUS) ? OP_ADD : OP_SUB;
            (*pos)++;
            CExpr *right = c_parse_mul(tokens, len, pos);
            CExpr *node = (CExpr *)calloc(1, sizeof(CExpr));
            node->tag = EXPR_BINOP; node->binop.left = left; node->binop.op = op; node->binop.right = right;
            left = node;
        } else break;
    }
    return left;
}

static CExpr *c_parse_expr(const char *input) {
    size_t tlen;
    CToken *tokens = c_lex(input, &tlen);
    size_t pos = 0;
    CExpr *e = c_parse_add(tokens, tlen, &pos);
    free(tokens);
    return e;
}

static void c_free_expr(CExpr *e) {
    if (!e) return;
    switch (e->tag) {
        case EXPR_BINOP: c_free_expr(e->binop.left); c_free_expr(e->binop.right); break;
        case EXPR_UNARY_MINUS: c_free_expr(e->inner); break;
        case EXPR_CALL:
            for (size_t i = 0; i < e->call.nargs; i++) c_free_expr(e->call.args[i]);
            free(e->call.args);
            break;
        default: break;
    }
    free(e);
}

/* em_01: Token stream analysis */
NOINLINE int64_t em_01(const CToken *tokens, size_t len) {
    int64_t sum = 0, depth = 0, max_depth = 0, num_count = 0;
    for (size_t i = 0; i < len; i++) {
        switch (tokens[i].tag) {
            case TOK_NUM: sum += tokens[i].number; num_count++; break;
            case TOK_LPAREN: depth++; if (depth > max_depth) max_depth = depth; break;
            case TOK_RPAREN: depth--; break;
            case TOK_PLUS: case TOK_STAR: sum++; break;
            case TOK_MINUS: case TOK_SLASH: sum--; break;
            case TOK_IDENT: sum += (int64_t)strlen(tokens[i].ident); break;
            default: break;
        }
    }
    return sum * (max_depth + 1) + num_count;
}

/* em_02: Evaluate expression tree */
NOINLINE int64_t em_02(const CExpr *e) {
    if (!e) return 0;
    switch (e->tag) {
        case EXPR_LIT: return e->lit;
        case EXPR_VAR: return (int64_t)strlen(e->var);
        case EXPR_BINOP: {
            int64_t lv = em_02(e->binop.left);
            int64_t rv = em_02(e->binop.right);
            switch (e->binop.op) {
                case OP_ADD: return lv + rv;
                case OP_SUB: return lv - rv;
                case OP_MUL: return lv * rv;
                case OP_DIV: return rv != 0 ? lv / rv : 0;
            }
            return 0;
        }
        case EXPR_UNARY_MINUS: return -em_02(e->inner);
        case EXPR_CALL: {
            int64_t sum = (int64_t)strlen(e->call.name);
            for (size_t i = 0; i < e->call.nargs; i++) sum += em_02(e->call.args[i]);
            return sum;
        }
        default: return 0;
    }
}

/* em_03: Count token types */
NOINLINE uint64_t em_03(const CToken *tokens, size_t len) {
    uint64_t nums = 0, idents = 0, ops = 0, parens = 0;
    for (size_t i = 0; i < len; i++) {
        switch (tokens[i].tag) {
            case TOK_NUM: nums++; break;
            case TOK_IDENT: idents++; break;
            case TOK_PLUS: case TOK_MINUS: case TOK_STAR: case TOK_SLASH: ops++; break;
            case TOK_LPAREN: case TOK_RPAREN: parens++; break;
            default: break;
        }
    }
    return nums * 1000 + idents * 100 + ops * 10 + parens;
}

/* em_04: Expression depth and node count */
static uint64_t expr_depth(const CExpr *e) {
    if (!e) return 0;
    switch (e->tag) {
        case EXPR_LIT: case EXPR_VAR: return 1;
        case EXPR_BINOP: { uint64_t ld = expr_depth(e->binop.left), rd = expr_depth(e->binop.right); return 1 + (ld > rd ? ld : rd); }
        case EXPR_UNARY_MINUS: return 1 + expr_depth(e->inner);
        case EXPR_CALL: { uint64_t mx = 0; for (size_t i = 0; i < e->call.nargs; i++) { uint64_t d = expr_depth(e->call.args[i]); if (d > mx) mx = d; } return 1 + mx; }
        default: return 0;
    }
}
static uint64_t expr_count(const CExpr *e) {
    if (!e) return 0;
    switch (e->tag) {
        case EXPR_LIT: case EXPR_VAR: return 1;
        case EXPR_BINOP: return 1 + expr_count(e->binop.left) + expr_count(e->binop.right);
        case EXPR_UNARY_MINUS: return 1 + expr_count(e->inner);
        case EXPR_CALL: { uint64_t s = 1; for (size_t i = 0; i < e->call.nargs; i++) s += expr_count(e->call.args[i]); return s; }
        default: return 0;
    }
}
NOINLINE uint64_t em_04(const CExpr *e) {
    return expr_depth(e) * 100 + expr_count(e);
}

/* em_05: Extract numbers, compute stats */
NOINLINE int64_t em_05(const CToken *tokens, size_t len, size_t top_n) {
    int64_t *nums = (int64_t *)malloc(len * sizeof(int64_t));
    size_t ncount = 0;
    for (size_t i = 0; i < len; i++) {
        if (tokens[i].tag == TOK_NUM) nums[ncount++] = tokens[i].number;
    }
    qsort(nums, ncount, sizeof(int64_t), cmp_i64);
    int64_t sum = 0;
    for (size_t i = 0; i < ncount; i++) sum += nums[i];
    int64_t top_sum = 0;
    for (size_t i = 0; i < top_n && i < ncount; i++) top_sum += nums[ncount - 1 - i];
    int64_t median = (ncount > 0) ? nums[ncount / 2] : 0;
    free(nums);
    return sum + top_sum * 10 + median;
}

/* em_06: Constant fold */
NOINLINE CExpr *em_06(const CExpr *e) {
    if (!e) return NULL;
    CExpr *r = (CExpr *)calloc(1, sizeof(CExpr));
    switch (e->tag) {
        case EXPR_LIT: r->tag = EXPR_LIT; r->lit = e->lit; return r;
        case EXPR_VAR: r->tag = EXPR_VAR; strcpy(r->var, e->var); return r;
        case EXPR_BINOP: {
            CExpr *lf = em_06(e->binop.left);
            CExpr *rf = em_06(e->binop.right);
            if (lf->tag == EXPR_LIT && rf->tag == EXPR_LIT) {
                int64_t a = lf->lit, b = rf->lit;
                switch (e->binop.op) {
                    case OP_ADD: r->tag = EXPR_LIT; r->lit = a + b; c_free_expr(lf); c_free_expr(rf); return r;
                    case OP_SUB: r->tag = EXPR_LIT; r->lit = a - b; c_free_expr(lf); c_free_expr(rf); return r;
                    case OP_MUL: r->tag = EXPR_LIT; r->lit = a * b; c_free_expr(lf); c_free_expr(rf); return r;
                    case OP_DIV: if (b != 0) { r->tag = EXPR_LIT; r->lit = a / b; c_free_expr(lf); c_free_expr(rf); return r; } break;
                }
            }
            if (lf->tag == EXPR_LIT && lf->lit == 0 && e->binop.op == OP_ADD) { free(r); c_free_expr(lf); return rf; }
            if (rf->tag == EXPR_LIT && rf->lit == 0 && e->binop.op == OP_ADD) { free(r); c_free_expr(rf); return lf; }
            if (lf->tag == EXPR_LIT && lf->lit == 0 && e->binop.op == OP_MUL) { r->tag = EXPR_LIT; r->lit = 0; c_free_expr(lf); c_free_expr(rf); return r; }
            if (rf->tag == EXPR_LIT && rf->lit == 0 && e->binop.op == OP_MUL) { r->tag = EXPR_LIT; r->lit = 0; c_free_expr(lf); c_free_expr(rf); return r; }
            if (lf->tag == EXPR_LIT && lf->lit == 1 && e->binop.op == OP_MUL) { free(r); c_free_expr(lf); return rf; }
            if (rf->tag == EXPR_LIT && rf->lit == 1 && e->binop.op == OP_MUL) { free(r); c_free_expr(rf); return lf; }
            r->tag = EXPR_BINOP; r->binop.left = lf; r->binop.op = e->binop.op; r->binop.right = rf;
            return r;
        }
        case EXPR_UNARY_MINUS: {
            CExpr *f = em_06(e->inner);
            if (f->tag == EXPR_LIT) { r->tag = EXPR_LIT; r->lit = -f->lit; c_free_expr(f); return r; }
            r->tag = EXPR_UNARY_MINUS; r->inner = f; return r;
        }
        default: r->tag = EXPR_LIT; return r;
    }
}

/* em_07: Pretty-print tokens */
NOINLINE char *em_07(const CToken *tokens, size_t len) {
    char *result = (char *)malloc(len * 64 + 1);
    result[0] = '\0';
    int prev_was_num = 0;
    for (size_t i = 0; i < len; i++) {
        switch (tokens[i].tag) {
            case TOK_NUM: {
                if (prev_was_num) strcat(result, " ");
                char buf[32]; snprintf(buf, 32, "%lld", (long long)tokens[i].number);
                strcat(result, buf); prev_was_num = 1; break;
            }
            case TOK_IDENT:
                if (prev_was_num) strcat(result, " ");
                strcat(result, tokens[i].ident); prev_was_num = 1; break;
            case TOK_PLUS: strcat(result, " + "); prev_was_num = 0; break;
            case TOK_MINUS: strcat(result, " - "); prev_was_num = 0; break;
            case TOK_STAR: strcat(result, " * "); prev_was_num = 0; break;
            case TOK_SLASH: strcat(result, " / "); prev_was_num = 0; break;
            case TOK_LPAREN: strcat(result, "("); prev_was_num = 0; break;
            case TOK_RPAREN: strcat(result, ")"); prev_was_num = 0; break;
            default: break;
        }
    }
    return result;
}

/* em_08: Serialize expression */
static void expr_to_str(const CExpr *e, char *buf, size_t bufsz) {
    if (!e) { buf[0] = '\0'; return; }
    switch (e->tag) {
        case EXPR_LIT: snprintf(buf, bufsz, "%lld", (long long)e->lit); break;
        case EXPR_VAR: snprintf(buf, bufsz, "%s", e->var); break;
        case EXPR_BINOP: {
            char lb[512], rb[512];
            expr_to_str(e->binop.left, lb, 512);
            expr_to_str(e->binop.right, rb, 512);
            const char *op = "+";
            switch (e->binop.op) { case OP_ADD: op="+"; break; case OP_SUB: op="-"; break; case OP_MUL: op="*"; break; case OP_DIV: op="/"; break; }
            snprintf(buf, bufsz, "(%s %s %s)", lb, op, rb);
            break;
        }
        case EXPR_UNARY_MINUS: { char ib[512]; expr_to_str(e->inner, ib, 512); snprintf(buf, bufsz, "(-%s)", ib); break; }
        default: buf[0] = '\0'; break;
    }
}
NOINLINE char *em_08(const CExpr *e) {
    char *buf = (char *)malloc(1024);
    expr_to_str(e, buf, 1024);
    return buf;
}

/* em_09: Validate token stream */
NOINLINE uint64_t em_09(const CToken *tokens, size_t len) {
    int64_t depth = 0, max_depth = 0;
    uint64_t errors = 0;
    int prev_was_op = 1;
    for (size_t i = 0; i < len; i++) {
        switch (tokens[i].tag) {
            case TOK_NUM: case TOK_IDENT:
                if (!prev_was_op) errors++;
                prev_was_op = 0; break;
            case TOK_PLUS: case TOK_MINUS: case TOK_STAR: case TOK_SLASH:
                if (prev_was_op) errors++;
                prev_was_op = 1; break;
            case TOK_LPAREN: depth++; if (depth > max_depth) max_depth = depth; prev_was_op = 1; break;
            case TOK_RPAREN: depth--; if (depth < 0) errors++; prev_was_op = 0; break;
            default: break;
        }
    }
    if (depth != 0) errors += (uint64_t)(depth < 0 ? -depth : depth);
    return errors * 100 + (uint64_t)max_depth;
}

/* em_10: Execute commands with environment */
static int64_t c_lookup(const char names[][64], const CCVal *vals, size_t count, const char *name) {
    for (size_t i = count; i > 0; i--) {
        if (strcmp(names[i-1], name) == 0) {
            switch (vals[i-1].tag) {
                case CVAL_INT: return vals[i-1].int_val;
                case CVAL_STR: return (int64_t)strlen(vals[i-1].str_val);
                case CVAL_LIST: { int64_t s = 0; for (size_t j = 0; j < vals[i-1].list.len; j++) s += vals[i-1].list.items[j]; return s; }
            }
        }
    }
    return -99999; /* not found sentinel */
}

NOINLINE int64_t em_10(const CCmd *cmds, size_t len) {
    char names[64][64];
    CCVal vals[64];
    size_t env_count = 0;
    int64_t output = 0;
    for (size_t i = 0; i < len; i++) {
        switch (cmds[i].tag) {
            case CMD_SET:
                if (env_count < 64) {
                    strcpy(names[env_count], cmds[i].set.name);
                    vals[env_count] = cmds[i].set.val;
                    env_count++;
                }
                break;
            case CMD_ADD: {
                int64_t va = c_lookup(names, vals, env_count, cmds[i].add.a);
                int64_t vb = c_lookup(names, vals, env_count, cmds[i].add.b);
                if (va == -99999) va = 0;
                if (vb == -99999) vb = 0;
                if (env_count < 64) {
                    strcpy(names[env_count], cmds[i].add.dst);
                    vals[env_count].tag = CVAL_INT; vals[env_count].int_val = va + vb;
                    env_count++;
                }
                break;
            }
            case CMD_PRINT: {
                int64_t v = c_lookup(names, vals, env_count, cmds[i].print_name);
                output += (v == -99999) ? -1 : v;
                break;
            }
            case CMD_IF: {
                int64_t v = c_lookup(names, vals, env_count, cmds[i].if_cmd.cond);
                if (v == -99999) v = 0;
                if (v > 0) output += em_10(cmds[i].if_cmd.then_cmds, cmds[i].if_cmd.then_len);
                else output += em_10(cmds[i].if_cmd.else_cmds, cmds[i].if_cmd.else_len);
                break;
            }
        }
    }
    return output;
}

/* em_11: Extract unique identifiers, hash */
NOINLINE uint64_t em_11(const CToken *tokens, size_t len) {
    char names[64][64]; size_t ncount = 0;
    for (size_t i = 0; i < len; i++) {
        if (tokens[i].tag == TOK_IDENT) {
            int found = 0;
            for (size_t j = 0; j < ncount; j++) {
                if (strcmp(names[j], tokens[i].ident) == 0) { found = 1; break; }
            }
            if (!found && ncount < 64) { strcpy(names[ncount], tokens[i].ident); ncount++; }
        }
    }
    /* Sort */
    for (size_t i = 1; i < ncount; i++) {
        char tmp[64]; strcpy(tmp, names[i]);
        size_t j = i;
        while (j > 0 && strcmp(names[j-1], tmp) > 0) { strcpy(names[j], names[j-1]); j--; }
        strcpy(names[j], tmp);
    }
    uint64_t hash = 0;
    for (size_t i = 0; i < ncount; i++) {
        for (size_t j = 0; names[i][j]; j++) hash = hash * 31 + (unsigned char)names[i][j];
    }
    return hash + (uint64_t)ncount;
}

/* em_12: Collect variables from expression */
static void collect_vars(const CExpr *e, char vars[][64], size_t *count) {
    if (!e) return;
    switch (e->tag) {
        case EXPR_LIT: break;
        case EXPR_VAR: {
            int found = 0;
            for (size_t i = 0; i < *count; i++) { if (strcmp(vars[i], e->var) == 0) { found = 1; break; } }
            if (!found && *count < 64) { strcpy(vars[*count], e->var); (*count)++; }
            break;
        }
        case EXPR_BINOP: collect_vars(e->binop.left, vars, count); collect_vars(e->binop.right, vars, count); break;
        case EXPR_UNARY_MINUS: collect_vars(e->inner, vars, count); break;
        case EXPR_CALL: for (size_t i = 0; i < e->call.nargs; i++) collect_vars(e->call.args[i], vars, count); break;
    }
}
NOINLINE size_t em_12(const CExpr *e, char out[][64]) {
    size_t count = 0;
    collect_vars(e, out, &count);
    /* Sort */
    for (size_t i = 1; i < count; i++) {
        char tmp[64]; strcpy(tmp, out[i]);
        size_t j = i;
        while (j > 0 && strcmp(out[j-1], tmp) > 0) { strcpy(out[j], out[j-1]); j--; }
        strcpy(out[j], tmp);
    }
    return count;
}

/* em_13: Complexity score */
NOINLINE uint64_t em_13(const CToken *tokens, size_t len) {
    uint64_t score = 0, nesting = 0;
    for (size_t i = 0; i < len; i++) {
        switch (tokens[i].tag) {
            case TOK_NUM: score += 1 + ((uint64_t)(tokens[i].number < 0 ? -tokens[i].number : tokens[i].number) / 10); break;
            case TOK_IDENT: score += strlen(tokens[i].ident) * 2; break;
            case TOK_PLUS: case TOK_MINUS: score += 1 + nesting; break;
            case TOK_STAR: case TOK_SLASH: score += 2 + nesting * 2; break;
            case TOK_LPAREN: nesting++; score += nesting; break;
            case TOK_RPAREN: if (nesting > 0) nesting--; break;
            default: break;
        }
    }
    return score;
}

/* em_14: Variable substitution */
NOINLINE CExpr *em_14(const CExpr *e) {
    if (!e) return NULL;
    CExpr *r = (CExpr *)calloc(1, sizeof(CExpr));
    switch (e->tag) {
        case EXPR_LIT: r->tag = EXPR_LIT; r->lit = e->lit; return r;
        case EXPR_VAR:
            if (strcmp(e->var, "x") == 0) { r->tag = EXPR_LIT; r->lit = 10; }
            else if (strcmp(e->var, "y") == 0) { r->tag = EXPR_LIT; r->lit = 20; }
            else if (strcmp(e->var, "z") == 0) { r->tag = EXPR_LIT; r->lit = 30; }
            else { r->tag = EXPR_VAR; strcpy(r->var, e->var); }
            return r;
        case EXPR_BINOP:
            r->tag = EXPR_BINOP; r->binop.left = em_14(e->binop.left); r->binop.op = e->binop.op; r->binop.right = em_14(e->binop.right);
            return r;
        case EXPR_UNARY_MINUS:
            r->tag = EXPR_UNARY_MINUS; r->inner = em_14(e->inner); return r;
        default: r->tag = EXPR_LIT; return r;
    }
}

/* em_15: Validate commands (check defined vars) */
NOINLINE uint64_t em_15(const CCmd *cmds, size_t len) {
    char defined[64][64]; size_t dcount = 0;
    uint64_t errors = 0;
    for (size_t i = 0; i < len; i++) {
        switch (cmds[i].tag) {
            case CMD_SET: {
                int found = 0;
                for (size_t j = 0; j < dcount; j++) if (strcmp(defined[j], cmds[i].set.name) == 0) { found = 1; break; }
                if (!found && dcount < 64) { strcpy(defined[dcount], cmds[i].set.name); dcount++; }
                break;
            }
            case CMD_ADD: {
                int fa = 0, fb = 0;
                for (size_t j = 0; j < dcount; j++) {
                    if (strcmp(defined[j], cmds[i].add.a) == 0) fa = 1;
                    if (strcmp(defined[j], cmds[i].add.b) == 0) fb = 1;
                }
                if (!fa) errors++;
                if (!fb) errors++;
                int fd = 0;
                for (size_t j = 0; j < dcount; j++) if (strcmp(defined[j], cmds[i].add.dst) == 0) { fd = 1; break; }
                if (!fd && dcount < 64) { strcpy(defined[dcount], cmds[i].add.dst); dcount++; }
                break;
            }
            case CMD_PRINT: {
                int found = 0;
                for (size_t j = 0; j < dcount; j++) if (strcmp(defined[j], cmds[i].print_name) == 0) { found = 1; break; }
                if (!found) errors++;
                break;
            }
            case CMD_IF: {
                int found = 0;
                for (size_t j = 0; j < dcount; j++) if (strcmp(defined[j], cmds[i].if_cmd.cond) == 0) { found = 1; break; }
                if (!found) errors++;
                errors += em_15(cmds[i].if_cmd.then_cmds, cmds[i].if_cmd.then_len);
                errors += em_15(cmds[i].if_cmd.else_cmds, cmds[i].if_cmd.else_len);
                break;
            }
        }
    }
    return errors;
}

/* em_16: RPN conversion */
NOINLINE size_t em_16(const CToken *tokens, size_t len, char out[][16], size_t max_out) {
    size_t ocount = 0;
    const CToken *op_stack[64]; size_t sp = 0;
    for (size_t i = 0; i < len && ocount < max_out; i++) {
        switch (tokens[i].tag) {
            case TOK_NUM: snprintf(out[ocount++], 16, "%lld", (long long)tokens[i].number); break;
            case TOK_IDENT: strncpy(out[ocount++], tokens[i].ident, 15); out[ocount-1][15] = '\0'; break;
            case TOK_PLUS: case TOK_MINUS: case TOK_STAR: case TOK_SLASH: {
                int prec = (tokens[i].tag == TOK_STAR || tokens[i].tag == TOK_SLASH) ? 2 : 1;
                while (sp > 0) {
                    const CToken *top = op_stack[sp - 1];
                    if (top->tag == TOK_LPAREN) break;
                    int tp = (top->tag == TOK_STAR || top->tag == TOK_SLASH) ? 2 : 1;
                    if (tp >= prec && ocount < max_out) {
                        sp--;
                        switch (top->tag) {
                            case TOK_PLUS: strcpy(out[ocount++], "+"); break;
                            case TOK_MINUS: strcpy(out[ocount++], "-"); break;
                            case TOK_STAR: strcpy(out[ocount++], "*"); break;
                            case TOK_SLASH: strcpy(out[ocount++], "/"); break;
                            default: strcpy(out[ocount++], "?"); break;
                        }
                    } else break;
                }
                if (sp < 64) op_stack[sp++] = &tokens[i];
                break;
            }
            case TOK_LPAREN: if (sp < 64) op_stack[sp++] = &tokens[i]; break;
            case TOK_RPAREN:
                while (sp > 0 && ocount < max_out) {
                    const CToken *top = op_stack[--sp];
                    if (top->tag == TOK_LPAREN) break;
                    switch (top->tag) {
                        case TOK_PLUS: strcpy(out[ocount++], "+"); break;
                        case TOK_MINUS: strcpy(out[ocount++], "-"); break;
                        case TOK_STAR: strcpy(out[ocount++], "*"); break;
                        case TOK_SLASH: strcpy(out[ocount++], "/"); break;
                        default: strcpy(out[ocount++], "?"); break;
                    }
                }
                break;
            default: break;
        }
    }
    while (sp > 0 && ocount < max_out) {
        const CToken *top = op_stack[--sp];
        switch (top->tag) {
            case TOK_PLUS: strcpy(out[ocount++], "+"); break;
            case TOK_MINUS: strcpy(out[ocount++], "-"); break;
            case TOK_STAR: strcpy(out[ocount++], "*"); break;
            case TOK_SLASH: strcpy(out[ocount++], "/"); break;
            default: strcpy(out[ocount++], "?"); break;
        }
    }
    return ocount;
}

/* em_17: Check linearity */
static int is_linear(const CExpr *e) {
    if (!e) return 1;
    switch (e->tag) {
        case EXPR_LIT: case EXPR_VAR: return 1;
        case EXPR_BINOP:
            if (e->binop.op == OP_MUL || e->binop.op == OP_DIV) return 0;
            return is_linear(e->binop.left) && is_linear(e->binop.right);
        case EXPR_UNARY_MINUS: return is_linear(e->inner);
        case EXPR_CALL: {
            for (size_t i = 0; i < e->call.nargs; i++) if (!is_linear(e->call.args[i])) return 0;
            return 1;
        }
        default: return 1;
    }
}
NOINLINE int em_17(const CExpr *e) { return is_linear(e); }

/* em_18: Nesting histogram */
NOINLINE uint64_t *em_18(const CToken *tokens, size_t len, size_t max_depth, size_t *out_len) {
    uint64_t *histogram = (uint64_t *)calloc(max_depth + 1, sizeof(uint64_t));
    size_t depth = 0;
    for (size_t i = 0; i < len; i++) {
        switch (tokens[i].tag) {
            case TOK_LPAREN:
                if (depth <= max_depth) histogram[depth]++;
                depth++;
                break;
            case TOK_RPAREN:
                if (depth > 0) depth--;
                break;
            default:
                if (depth <= max_depth) histogram[depth < max_depth ? depth : max_depth]++;
                break;
        }
    }
    *out_len = max_depth + 1;
    return histogram;
}

/* em_19: Type-check commands */
static const char *c_get_type(const char names[][64], const char types[][16], size_t count, const char *name) {
    for (size_t i = count; i > 0; i--) {
        if (strcmp(names[i-1], name) == 0) return types[i-1];
    }
    return NULL;
}

NOINLINE uint64_t em_19(const CCmd *cmds, size_t len) {
    char names[64][64]; char types[64][16]; size_t tcount = 0;
    uint64_t errors = 0;
    for (size_t i = 0; i < len; i++) {
        switch (cmds[i].tag) {
            case CMD_SET: {
                const char *t;
                switch (cmds[i].set.val.tag) {
                    case CVAL_INT: t = "int"; break;
                    case CVAL_STR: t = "str"; break;
                    case CVAL_LIST: t = "list"; break;
                    default: t = "int"; break;
                }
                if (tcount < 64) { strcpy(names[tcount], cmds[i].set.name); strcpy(types[tcount], t); tcount++; }
                break;
            }
            case CMD_ADD: {
                const char *ta = c_get_type(names, types, tcount, cmds[i].add.a);
                const char *tb = c_get_type(names, types, tcount, cmds[i].add.b);
                if (ta && tb && strcmp(ta, "int") == 0 && strcmp(tb, "int") == 0) {
                    if (tcount < 64) { strcpy(names[tcount], cmds[i].add.dst); strcpy(types[tcount], "int"); tcount++; }
                } else if (ta && tb && strcmp(ta, tb) == 0) {
                    if (tcount < 64) { strcpy(names[tcount], cmds[i].add.dst); strcpy(types[tcount], ta); tcount++; }
                } else {
                    errors++;
                    if (tcount < 64) { strcpy(names[tcount], cmds[i].add.dst); strcpy(types[tcount], "int"); tcount++; }
                }
                break;
            }
            case CMD_PRINT: {
                if (!c_get_type(names, types, tcount, cmds[i].print_name)) errors++;
                break;
            }
            case CMD_IF: {
                const char *t = c_get_type(names, types, tcount, cmds[i].if_cmd.cond);
                if (!t || strcmp(t, "int") != 0) errors++;
                errors += em_19(cmds[i].if_cmd.then_cmds, cmds[i].if_cmd.then_len);
                errors += em_19(cmds[i].if_cmd.else_cmds, cmds[i].if_cmd.else_len);
                break;
            }
        }
    }
    return errors;
}

/* em_20: Distribute multiplication over addition */
static CExpr *c_clone_expr(const CExpr *e);
static CExpr *c_clone_expr(const CExpr *e) {
    if (!e) return NULL;
    CExpr *r = (CExpr *)calloc(1, sizeof(CExpr));
    *r = *e;
    switch (e->tag) {
        case EXPR_BINOP: r->binop.left = c_clone_expr(e->binop.left); r->binop.right = c_clone_expr(e->binop.right); break;
        case EXPR_UNARY_MINUS: r->inner = c_clone_expr(e->inner); break;
        default: break;
    }
    return r;
}

NOINLINE CExpr *em_20(const CExpr *e) {
    if (!e) return NULL;
    CExpr *r = (CExpr *)calloc(1, sizeof(CExpr));
    switch (e->tag) {
        case EXPR_LIT: r->tag = EXPR_LIT; r->lit = e->lit; return r;
        case EXPR_VAR: r->tag = EXPR_VAR; strcpy(r->var, e->var); return r;
        case EXPR_BINOP: {
            CExpr *lf = em_20(e->binop.left);
            CExpr *rf = em_20(e->binop.right);
            if (e->binop.op == OP_MUL && rf->tag == EXPR_BINOP && rf->binop.op == OP_ADD) {
                /* a * (b + c) => a*b + a*c */
                CExpr *ab = (CExpr *)calloc(1, sizeof(CExpr));
                ab->tag = EXPR_BINOP; ab->binop.left = c_clone_expr(lf); ab->binop.op = OP_MUL; ab->binop.right = c_clone_expr(rf->binop.left);
                CExpr *ac = (CExpr *)calloc(1, sizeof(CExpr));
                ac->tag = EXPR_BINOP; ac->binop.left = lf; ac->binop.op = OP_MUL; ac->binop.right = c_clone_expr(rf->binop.right);
                c_free_expr(rf);
                r->tag = EXPR_BINOP; r->binop.left = ab; r->binop.op = OP_ADD; r->binop.right = ac;
                return r;
            }
            r->tag = EXPR_BINOP; r->binop.left = lf; r->binop.op = e->binop.op; r->binop.right = rf;
            return r;
        }
        case EXPR_UNARY_MINUS: r->tag = EXPR_UNARY_MINUS; r->inner = em_20(e->inner); return r;
        default: r->tag = EXPR_LIT; return r;
    }
}

/* ========================================================================== */
/* main: call all 100 functions                                               */
/* ========================================================================== */

int main(void) {
    uint64_t data[64], data2[100];
    for (int i = 0; i < 64; i++) data[i] = (uint64_t)i;
    for (int i = 0; i < 100; i++) data2[i] = (uint64_t)(i + 100);
    const char *test_str = "hello world foo bar baz 123 testing";

    /* bc_01 .. bc_20 */
    black_box_u64(bc_01(data, 64, 10));
    { uint64_t tmp[64]; memcpy(tmp, data, 512); black_box_u64((uint64_t)bc_02(tmp, 64)); }
    { size_t olen; uint64_t *h = bc_03(data, 64, 3, &olen); black_box_ptr(h); free(h); }
    { size_t olen; uint64_t *m = bc_04(data, 32, data+32, 32, &olen); black_box_ptr(m); free(m); }
    black_box_u64(bc_05(data, 64));
    { uint64_t tmp[64]; memcpy(tmp, data, 512); black_box_u64(bc_06(tmp, 64, 5)); }
    { size_t olen; int64_t *c = bc_07(data, 64, &olen); black_box_ptr(c); free(c); }
    { size_t pi[64]; uint64_t pv[64]; black_box_u64((uint64_t)bc_08(data, 64, 30, pi, pv, 64)); }
    { uint64_t tmp[64]; memcpy(tmp, data, 512); black_box_u64(bc_09(tmp, 64)); }
    { size_t olen; uint64_t *r = bc_10(data, 64, 4, &olen); black_box_ptr(r); free(r); }
    { uint64_t tmp[64]; memcpy(tmp, data, 512); black_box_u64(bc_11(tmp, 64)); }
    { size_t olen; uint64_t *r = bc_12(data, 64, 7, &olen); black_box_ptr(r); free(r); }
    black_box_u64(bc_13(data, 64));
    { uint64_t tmp[64]; memcpy(tmp, data, 512); size_t lo, hi; bc_14(tmp, 64, 3, &lo, &hi); black_box_u64(lo + hi); }
    black_box_u64(bc_15(data, 64));
    { size_t olen; uint64_t *r = bc_16(data, 64, 8, &olen); black_box_ptr(r); free(r); }
    { uint64_t tmp[64]; memcpy(tmp, data, 512); black_box_u64(bc_17(tmp, 64)); }
    black_box_u64(bc_18(data, 64, 5));
    { uint64_t val; black_box_u64(bc_19(data, 64, &val)); }
    { uint64_t tmp[64]; memcpy(tmp, data, 512); size_t olen; uint64_t *r = bc_20(tmp, 64, 10, &olen); black_box_ptr(r); free(r); }

    /* own_01 .. own_20 */
    black_box_u64(own_01(20));
    { uint64_t *v = malloc(9*8); uint64_t d[] = {5,3,8,1,7,2,9,4,6}; memcpy(v,d,9*8); size_t ol; uint64_t *r = own_02(v,9,1,&ol); black_box_ptr(r); free(r); }
    { char *s = strdup("hello world foo bar baz 123 testing"); char *r = own_03(s, 3); black_box_ptr(r); free(r); }
    black_box_u64(own_04(15));
    { uint64_t *a = malloc(5*8); uint64_t *b = malloc(5*8); uint64_t ad[]={10,20,30,40,50}, bd[]={5,15,25,35,45}; memcpy(a,ad,40); memcpy(b,bd,40); size_t ol; uint64_t *r=own_05(a,5,b,5,&ol); black_box_ptr(r); free(r); }
    { char *s = strdup("hello world test"); char *r = own_06(s); black_box_ptr(r); free(r); }
    black_box_u64(own_07(8));
    { uint64_t *v = malloc(8*8); uint64_t d[]={1,5,3,8,2,7,4,6}; memcpy(v,d,64); black_box_u64(own_08(v, 8, 4)); }
    { char *s = strdup("abcdefghij"); char *r = own_09(s, 3); black_box_ptr(r); free(r); }
    { size_t ol; char **r = own_10(12, &ol); for(size_t i=0;i<ol;i++) free(r[i]); free(r); }
    { uint64_t *v = malloc(9*8); uint64_t d[]={9,1,5,3,7,2,8,4,6}; memcpy(v,d,72); uint64_t *o,*dd; size_t ol,dl; own_11(v,9,1,&o,&ol,&dd,&dl); free(o); free(dd); }
    { char *s = strdup("the quick brown fox"); char *r = own_12(s); black_box_ptr(r); free(r); }
    { size_t ol; uint64_t *r = own_13(10, &ol); black_box_ptr(r); free(r); }
    { uint64_t *v = malloc(11*8); uint64_t d[]={3,1,4,1,5,9,2,6,5,3,5}; memcpy(v,d,88); size_t ol; RLEPair *r = own_14(v,11,3,&ol); free(r); }
    { char *s = strdup("rust lang is great"); char *r = own_15(s, 'a'); black_box_ptr(r); free(r); }
    { size_t ol; uint64_t *r = own_16(6, &ol); black_box_ptr(r); free(r); }
    { uint64_t *v = malloc(5*8); uint64_t d[]={100,200,50,300,150}; memcpy(v,d,40); size_t ol; uint64_t *r = own_17(v,5,2,&ol); black_box_ptr(r); free(r); }
    { char *a = strdup("hello"); char *b = strdup("world"); char *r = own_18(a, b); black_box_ptr(r); free(r); }
    black_box_u64(own_19(8));
    { uint64_t *v = malloc(8*8); uint64_t d[]={7,2,5,1,8,3,6,4}; memcpy(v,d,64); size_t ol; uint64_t *r = own_20(v,8,1,&ol); black_box_ptr(r); free(r); }

    /* opt_01 .. opt_20 */
    black_box_u64(opt_01(data, 64, 30));
    black_box_u64(opt_02(test_str, ' '));
    { OptU64 od[] = {{1,1},{0,0},{1,3},{1,4},{0,0},{1,6}}; black_box_u64(opt_03(od, 6)); }
    { size_t os; uint64_t osum; black_box_u64((uint64_t)opt_04(data, 64, 50, &os, &osum)); }
    black_box_u64(opt_05("123 456 abc 789", 10));
    black_box_u64(opt_06(data, 64));
    black_box_u64(opt_07(test_str));
    { ResU64 rd[] = {{1,1,0},{0,0,3},{1,3,0},{1,4,0},{0,0,4},{1,6,0}}; black_box_u64(opt_08(rd, 6)); }
    { size_t lo, hi; black_box_u64((uint64_t)opt_09(data, 64, 5, &lo, &hi)); }
    black_box_u64(opt_10(test_str, 3));
    black_box_u64(opt_11(data, 64));
    { OptU64 od[] = {{1,10},{1,20},{0,0},{1,40}}; black_box_u64(opt_12(od, 4, 25)); }
    black_box_u64(opt_13(data, 64, 7));
    black_box_u64(opt_14("10 20 abc 30 40 xyz 50"));
    black_box_u64(opt_15(data, 64, 3));
    { int64_t vals[] = {5,-3,0,7,0,-1}; int ok[] = {1,1,0,1,0,1}; black_box_i64(opt_16(vals, ok, 6)); }
    black_box_u64(opt_17(data, 64, 10));
    black_box_u64(opt_18(test_str));
    black_box_u64(opt_19(data, 64, 8));
    black_box_u64(opt_20("3,1,4,1,5,9,2,6"));

    /* iter_01 .. iter_20 */
    black_box_u64(iter_01(data, 64, 10));
    black_box_u64(iter_02(data, 64, data2, 100));
    black_box_u64(iter_03(data, 64, 5));
    black_box_u64(iter_04(test_str));
    black_box_u64(iter_05(data, 64));
    black_box_u64(iter_06(data, 64, 3));
    black_box_u64(iter_07(test_str, ' '));
    black_box_u64(iter_08(data, 64, 4));
    black_box_u64(iter_09(data, 64));
    black_box_u64(iter_10(data, 64, 10));
    black_box_u64(iter_11(test_str));
    black_box_u64(iter_12(data, 64, 8));
    black_box_u64(iter_13(data, 64, data2, 100));
    black_box_u64(iter_14(data, 64));
    black_box_u64(iter_15(test_str, 3));
    black_box_u64(iter_16(data, 64, 5));
    black_box_u64(iter_17(data, 64));
    black_box_u64(iter_18(data, 64, 7));
    black_box_u64(iter_19(test_str));
    black_box_u64(iter_20(data, 64, 3));

    /* em_01 .. em_20 */
    size_t tlen;
    CToken *tokens = c_lex("42 + foo * (bar - 3)", &tlen);
    black_box_i64(em_01(tokens, tlen));

    CExpr *expr = c_parse_expr("1 + 2 * 3");
    black_box_i64(em_02(expr));
    black_box_u64(em_03(tokens, tlen));
    black_box_u64(em_04(expr));
    black_box_i64(em_05(tokens, tlen, 3));

    CExpr *folded = em_06(expr);
    black_box_ptr(folded);
    c_free_expr(folded);

    { char *s = em_07(tokens, tlen); black_box_ptr(s); free(s); }
    { char *s = em_08(expr); black_box_ptr(s); free(s); }
    black_box_u64(em_09(tokens, tlen));

    /* em_10: commands */
    {
        CCmd cmds[4];
        cmds[0].tag = CMD_SET; strcpy(cmds[0].set.name, "x"); cmds[0].set.val.tag = CVAL_INT; cmds[0].set.val.int_val = 10;
        cmds[1].tag = CMD_SET; strcpy(cmds[1].set.name, "y"); cmds[1].set.val.tag = CVAL_INT; cmds[1].set.val.int_val = 20;
        cmds[2].tag = CMD_ADD; strcpy(cmds[2].add.a, "x"); strcpy(cmds[2].add.b, "y"); strcpy(cmds[2].add.dst, "z");
        cmds[3].tag = CMD_PRINT; strcpy(cmds[3].print_name, "z");
        black_box_i64(em_10(cmds, 4));

        black_box_u64(em_11(tokens, tlen));
        { char vars[64][64]; black_box_u64((uint64_t)em_12(expr, vars)); }
        black_box_u64(em_13(tokens, tlen));
        { CExpr *s = em_14(expr); black_box_ptr(s); c_free_expr(s); }
        black_box_u64(em_15(cmds, 4));
        { char rpn[64][16]; black_box_u64((uint64_t)em_16(tokens, tlen, rpn, 64)); }
        black_box_u64((uint64_t)em_17(expr));
        { size_t hlen; uint64_t *h = em_18(tokens, tlen, 5, &hlen); black_box_ptr(h); free(h); }
        black_box_u64(em_19(cmds, 4));
        { CExpr *d = em_20(expr); black_box_ptr(d); c_free_expr(d); }
    }

    c_free_expr(expr);
    free(tokens);

    return 0;
}
