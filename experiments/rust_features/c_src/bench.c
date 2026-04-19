#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <ctype.h>

#define NOINLINE __attribute__((noinline))

static void black_box_u64(uint64_t v) { asm volatile("" : : "r"(v)); }
static void black_box_ptr(void *p) { asm volatile("" : : "r"(p)); }

/* =========================================================================
   OWNERSHIP & MOVE (om_01 .. om_20)
   C has no ownership — caller manages memory, callee may free/realloc.
   These are semantically equivalent but without compiler-enforced ownership.
   ========================================================================= */

/* Merge two sorted arrays, caller frees a and b */
NOINLINE uint64_t *om_01(uint64_t *a, size_t alen, uint64_t *b, size_t blen, size_t *out_len) {
    /* sort a and b first */
    for (size_t i = 0; i < alen; i++)
        for (size_t j = i+1; j < alen; j++)
            if (a[i] > a[j]) { uint64_t t = a[i]; a[i] = a[j]; a[j] = t; }
    for (size_t i = 0; i < blen; i++)
        for (size_t j = i+1; j < blen; j++)
            if (b[i] > b[j]) { uint64_t t = b[i]; b[i] = b[j]; b[j] = t; }
    uint64_t *result = malloc((alen + blen) * 8);
    size_t i = 0, j = 0, k = 0;
    while (i < alen && j < blen) {
        if (a[i] <= b[j]) result[k++] = a[i++];
        else result[k++] = b[j++];
    }
    while (i < alen) result[k++] = a[i++];
    while (j < blen) result[k++] = b[j++];
    *out_len = k;
    free(a); free(b);
    return result;
}

/* Concatenate two strings with transform, caller frees both */
NOINLINE char *om_02(char *a, char *b) {
    size_t alen = strlen(a), blen = strlen(b);
    char *result = malloc(alen + blen + 2);
    size_t k = 0;
    for (size_t i = 0; i < alen; i++) result[k++] = toupper(a[i]);
    result[k++] = '-';
    for (size_t i = blen; i > 0; i--) result[k++] = b[i-1];
    result[k] = '\0';
    free(a); free(b);
    return result;
}

/* Partition into evens and odds */
NOINLINE void om_03(uint64_t *data, size_t n,
                    uint64_t **evens, size_t *ne, uint64_t **odds, size_t *no) {
    *evens = malloc(n * 8); *odds = malloc(n * 8);
    *ne = 0; *no = 0;
    for (size_t i = 0; i < n; i++) {
        if (data[i] % 2 == 0) (*evens)[(*ne)++] = data[i];
        else (*odds)[(*no)++] = data[i];
    }
    free(data);
}

/* Split string into words, rotate, rejoin */
NOINLINE char *om_04(char *s, size_t rot) {
    char *words[256]; size_t nw = 0;
    char *tok = strtok(s, " \t\n");
    while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " \t\n"); }
    if (nw == 0) return s;
    rot = rot % nw;
    size_t total = 0;
    for (size_t i = 0; i < nw; i++) total += strlen(words[i]);
    char *result = malloc(total + nw + 1);
    result[0] = '\0';
    for (size_t i = 0; i < nw; i++) {
        size_t idx = (i + rot) % nw;
        if (i > 0) strcat(result, " ");
        strcat(result, words[idx]);
    }
    free(s);
    return result;
}

/* Merge 3 arrays, sort, dedup */
NOINLINE uint64_t *om_05(uint64_t *a, size_t an, uint64_t *b, size_t bn,
                          uint64_t *c, size_t cn, size_t *out_len) {
    size_t total = an + bn + cn;
    uint64_t *combined = malloc(total * 8);
    memcpy(combined, a, an * 8);
    memcpy(combined + an, b, bn * 8);
    memcpy(combined + an + bn, c, cn * 8);
    /* sort */
    for (size_t i = 0; i < total; i++)
        for (size_t j = i+1; j < total; j++)
            if (combined[i] > combined[j]) { uint64_t t = combined[i]; combined[i] = combined[j]; combined[j] = t; }
    /* dedup */
    size_t k = 0;
    for (size_t i = 0; i < total; i++)
        if (i == 0 || combined[i] != combined[i-1]) combined[k++] = combined[i];
    *out_len = k;
    free(a); free(b); free(c);
    return combined;
}

/* Reverse string */
NOINLINE char *om_06(char *s) {
    size_t n = strlen(s);
    char *result = malloc(n + 1);
    for (size_t i = 0; i < n; i++) result[i] = s[n - 1 - i];
    result[n] = '\0';
    free(s);
    return result;
}

/* Running difference */
NOINLINE int64_t *om_07(uint64_t *data, size_t n, size_t *out_len) {
    int64_t *result = malloc(n * 8);
    if (n == 0) { *out_len = 0; free(data); return result; }
    result[0] = (int64_t)data[0];
    for (size_t i = 1; i < n; i++)
        result[i] = (int64_t)data[i] - (int64_t)data[i-1];
    *out_len = n;
    free(data);
    return result;
}

/* Extract every nth char */
NOINLINE char *om_08(char *s, size_t n) {
    size_t slen = strlen(s);
    char *result = malloc(slen + 1);
    size_t k = 0, i = 0;
    while (i < slen) { result[k++] = s[i]; i += n; }
    result[k] = '\0';
    free(s);
    return result;
}

/* Split at pivot, sort halves, merge */
NOINLINE uint64_t *om_09(uint64_t *data, size_t n, size_t *out_len) {
    if (n < 2) { *out_len = n; return data; }
    size_t mid = n / 2;
    /* sort left */
    for (size_t i = 0; i < mid; i++)
        for (size_t j = i+1; j < mid; j++)
            if (data[i] > data[j]) { uint64_t t = data[i]; data[i] = data[j]; data[j] = t; }
    /* sort right */
    for (size_t i = mid; i < n; i++)
        for (size_t j = i+1; j < n; j++)
            if (data[i] > data[j]) { uint64_t t = data[i]; data[i] = data[j]; data[j] = t; }
    uint64_t *merged = malloc(n * 8);
    size_t i = 0, j = mid, k = 0;
    while (i < mid && j < n) {
        if (data[i] <= data[j]) merged[k++] = data[i++];
        else merged[k++] = data[j++];
    }
    while (i < mid) merged[k++] = data[i++];
    while (j < n) merged[k++] = data[j++];
    *out_len = n;
    free(data);
    return merged;
}

/* Interleave 3 strings */
NOINLINE char *om_10(char *a, char *b, char *c) {
    size_t al = strlen(a), bl = strlen(b), cl = strlen(c);
    size_t maxl = al > bl ? (al > cl ? al : cl) : (bl > cl ? bl : cl);
    char *result = malloc(al + bl + cl + 1);
    size_t k = 0;
    for (size_t i = 0; i < maxl; i++) {
        if (i < al) result[k++] = a[i];
        if (i < bl) result[k++] = b[i];
        if (i < cl) result[k++] = c[i];
    }
    result[k] = '\0';
    free(a); free(b); free(c);
    return result;
}

/* Remove duplicates */
NOINLINE uint64_t *om_11(uint64_t *data, size_t n, size_t *out_len) {
    /* sort first */
    for (size_t i = 0; i < n; i++)
        for (size_t j = i+1; j < n; j++)
            if (data[i] > data[j]) { uint64_t t = data[i]; data[i] = data[j]; data[j] = t; }
    uint64_t *result = malloc(n * 8);
    size_t k = 0;
    for (size_t i = 0; i < n; i++)
        if (i == 0 || data[i] != data[i-1]) result[k++] = data[i];
    *out_len = k;
    free(data);
    return result;
}

/* Sort words in string */
NOINLINE char *om_12(char *s) {
    char *words[256]; size_t nw = 0;
    char *copy = strdup(s);
    char *tok = strtok(copy, " \t\n");
    while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " \t\n"); }
    /* sort words */
    for (size_t i = 0; i < nw; i++)
        for (size_t j = i+1; j < nw; j++)
            if (strcmp(words[i], words[j]) > 0) { char *t = words[i]; words[i] = words[j]; words[j] = t; }
    char *result = malloc(strlen(s) + 1);
    result[0] = '\0';
    for (size_t i = 0; i < nw; i++) {
        if (i > 0) strcat(result, " ");
        strcat(result, words[i]);
    }
    free(copy); free(s);
    return result;
}

/* Zip two arrays */
NOINLINE void om_13(uint64_t *a, size_t an, uint64_t *b, size_t bn,
                    uint64_t *out_a, uint64_t *out_b, size_t *out_len) {
    size_t n = an < bn ? an : bn;
    for (size_t i = 0; i < n; i++) { out_a[i] = a[i]; out_b[i] = b[i]; }
    *out_len = n;
    free(a); free(b);
}

/* Rotate bytes */
NOINLINE char *om_14(char *s, size_t offset) {
    size_t n = strlen(s);
    if (n == 0) { return s; }
    offset = offset % n;
    char *result = malloc(n + 1);
    for (size_t i = 0; i < n; i++) result[i] = s[(i + offset) % n];
    result[n] = '\0';
    free(s);
    return result;
}

/* Selection sort */
NOINLINE uint64_t *om_15(uint64_t *data, size_t n) {
    for (size_t i = 0; i < n; i++) {
        size_t min_idx = i;
        for (size_t j = i + 1; j < n; j++)
            if (data[j] < data[min_idx]) min_idx = j;
        uint64_t t = data[i]; data[i] = data[min_idx]; data[min_idx] = t;
    }
    return data;
}

/* Char frequency */
NOINLINE char *om_16(char *s) {
    int freq[26] = {0};
    for (size_t i = 0; s[i]; i++)
        if (isalpha(s[i])) freq[tolower(s[i]) - 'a']++;
    char *result = malloc(256);
    result[0] = '\0';
    for (int i = 0; i < 26; i++) {
        if (freq[i] > 0) {
            char buf[16]; snprintf(buf, 16, "%c%d", 'a'+i, freq[i]);
            strcat(result, buf);
        }
    }
    free(s);
    return result;
}

/* Cumulative sums */
NOINLINE uint64_t *om_17(uint64_t *data, size_t n, size_t *out_len) {
    uint64_t *result = malloc(n * 8);
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) { sum += data[i]; result[i] = sum; }
    *out_len = n;
    free(data);
    return result;
}

/* Interleave two strings */
NOINLINE char *om_18(char *a, char *b) {
    size_t al = strlen(a), bl = strlen(b);
    char *result = malloc(al + bl + 1);
    size_t k = 0, maxl = al > bl ? al : bl;
    for (size_t i = 0; i < maxl; i++) {
        if (i < al) result[k++] = a[i];
        if (i < bl) result[k++] = b[i];
    }
    result[k] = '\0';
    free(a); free(b);
    return result;
}

/* Chunk sums */
NOINLINE uint64_t *om_19(uint64_t *data, size_t n, size_t *out_len) {
    size_t chunk = 3;
    size_t nchunks = (n + chunk - 1) / chunk;
    uint64_t *result = malloc(nchunks * 8);
    size_t k = 0, i = 0;
    while (i < n) {
        size_t end = i + chunk; if (end > n) end = n;
        uint64_t sum = 0;
        for (size_t j = i; j < end; j++) sum += data[j];
        result[k++] = sum;
        i = end;
    }
    *out_len = k;
    free(data);
    return result;
}

/* Caesar cipher */
NOINLINE char *om_20(char *s, uint8_t shift) {
    size_t n = strlen(s);
    char *result = malloc(n + 1);
    for (size_t i = 0; i < n; i++) {
        if (s[i] >= 'a' && s[i] <= 'z')
            result[i] = (s[i] - 'a' + shift) % 26 + 'a';
        else if (s[i] >= 'A' && s[i] <= 'Z')
            result[i] = (s[i] - 'A' + shift) % 26 + 'A';
        else result[i] = s[i];
    }
    result[n] = '\0';
    free(s);
    return result;
}

/* =========================================================================
   DROP GLUE (dg_01 .. dg_20)
   C equivalents: manual free() calls. No compiler-generated cleanup.
   ========================================================================= */

/* Matrix trace + off-diagonal sum */
NOINLINE uint64_t dg_01(size_t n) {
    uint64_t **matrix = malloc(n * sizeof(uint64_t*));
    for (size_t i = 0; i < n; i++) {
        matrix[i] = malloc(n * 8);
        for (size_t j = 0; j < n; j++) matrix[i][j] = i * j + 1;
    }
    uint64_t trace = 0, off = 0;
    for (size_t i = 0; i < n; i++) trace += matrix[i][i];
    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < n; j++)
            if (i != j) off += matrix[i][j];
    for (size_t i = 0; i < n; i++) free(matrix[i]);
    free(matrix);
    return trace * off;
}

/* Filter words by length */
NOINLINE uint64_t dg_02(char *s, size_t min_len) {
    char *words[256]; size_t nw = 0;
    char *copy = strdup(s);
    char *tok = strtok(copy, " ");
    while (tok && nw < 256) { words[nw++] = strdup(tok); tok = strtok(NULL, " "); }
    uint64_t total = 0;
    for (size_t i = 0; i < nw; i++) {
        if (strlen(words[i]) >= min_len) {
            total += strlen(words[i]);
            for (size_t j = 0; words[i][j]; j++) total += words[i][j];
        }
        free(words[i]);
    }
    free(copy); free(s);
    return total;
}

typedef struct CTree { int is_leaf; uint64_t val; struct CTree *left, *right; } CTree;
static CTree *build_tree(uint32_t d, uint64_t val) {
    CTree *n = calloc(1, sizeof(CTree));
    if (d == 0) { n->is_leaf = 1; n->val = val; return n; }
    n->val = val;
    n->left = build_tree(d-1, val*2);
    n->right = build_tree(d-1, val*2+1);
    return n;
}
static uint64_t sum_tree(const CTree *t) {
    if (!t) return 0;
    if (t->is_leaf) return t->val;
    return sum_tree(t->left) + t->val + sum_tree(t->right);
}
static void free_tree(CTree *t) {
    if (!t) return;
    free_tree(t->left); free_tree(t->right); free(t);
}

/* Binary tree build, sum, free */
NOINLINE uint64_t dg_03(uint32_t depth) {
    CTree *tree = build_tree(depth, 1);
    uint64_t r = sum_tree(tree);
    free_tree(tree);
    return r;
}

/* Histogram */
NOINLINE uint64_t dg_04(uint64_t *data, size_t n) {
    uint64_t keys[256]; uint64_t counts[256]; size_t nk = 0;
    for (size_t i = 0; i < n; i++) {
        int found = 0;
        for (size_t j = 0; j < nk; j++) {
            if (keys[j] == data[i]) { counts[j]++; found = 1; break; }
        }
        if (!found && nk < 256) { keys[nk] = data[i]; counts[nk] = 1; nk++; }
    }
    uint64_t total = 0;
    for (size_t i = 0; i < nk; i++) total += keys[i] * counts[i];
    free(data);
    return total;
}

typedef struct CList { uint64_t val; struct CList *next; } CList;

/* Linked list build, traverse, free */
NOINLINE uint64_t dg_05(uint64_t n) {
    CList *head = NULL;
    for (uint64_t i = n; i > 0; i--) {
        CList *node = malloc(sizeof(CList));
        node->val = (i-1)*(i-1) + 1; node->next = head; head = node;
    }
    uint64_t sum = 0, count = 0;
    for (CList *c = head; c; c = c->next) { sum += c->val; count++; }
    while (head) { CList *t = head; head = head->next; free(t); }
    return sum * count;
}

/* Process words with temp strings */
NOINLINE uint64_t dg_06(char *s) {
    uint64_t total = 0;
    char *copy = strdup(s);
    char *tok = strtok(copy, " ");
    while (tok) {
        size_t len = strlen(tok);
        char *upper = malloc(len + 1);
        for (size_t i = 0; i < len; i++) upper[i] = toupper(tok[i]);
        upper[len] = '\0';
        char *rev = malloc(len + 1);
        for (size_t i = 0; i < len; i++) rev[i] = upper[len - 1 - i];
        rev[len] = '\0';
        total += len;
        for (size_t i = 0; i < len; i++) total += rev[i];
        free(upper); free(rev);
        tok = strtok(NULL, " ");
    }
    free(copy); free(s);
    return total;
}

/* 3D array */
NOINLINE uint64_t dg_07(size_t n) {
    uint64_t ***cube = malloc(n * sizeof(uint64_t**));
    for (size_t i = 0; i < n; i++) {
        cube[i] = malloc(n * sizeof(uint64_t*));
        for (size_t j = 0; j < n; j++) {
            cube[i][j] = malloc(n * 8);
            for (size_t k = 0; k < n; k++) cube[i][j][k] = (i+j+k) * 7 + 1;
        }
    }
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++)
        for (size_t j = 0; j < n; j++)
            for (size_t k = 0; k < n; k++) sum += cube[i][j][k];
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < n; j++) free(cube[i][j]);
        free(cube[i]);
    }
    free(cube);
    return sum;
}

/* Format numbers as padded strings */
NOINLINE char *dg_08(uint64_t *data, size_t n) {
    char *result = malloc(n * 8);
    result[0] = '\0';
    for (size_t i = 0; i < n; i++) {
        char buf[32]; snprintf(buf, 32, "%5lu", (unsigned long)data[i]);
        if (i > 0) strcat(result, ",");
        strcat(result, buf);
    }
    free(data);
    return result;
}

/* Array of heap-allocated values */
NOINLINE uint64_t dg_09(uint64_t n) {
    uint64_t **boxes = malloc(n * sizeof(uint64_t*));
    for (uint64_t i = 0; i < n; i++) { boxes[i] = malloc(8); *boxes[i] = i * i; }
    uint64_t sum = 0, product = 1;
    for (uint64_t i = 0; i < n; i++) sum += *boxes[i];
    for (uint64_t i = 0; i < n; i++) if (*boxes[i] > 0) product *= (*boxes[i] % 100 + 1);
    for (uint64_t i = 0; i < n; i++) free(boxes[i]);
    free(boxes);
    return sum + product;
}

/* Split string by delimiter */
NOINLINE uint64_t dg_10(char *s, char target) {
    char *segs[256]; size_t ns = 0;
    char *current = malloc(strlen(s) + 1);
    size_t ck = 0;
    for (size_t i = 0; s[i]; i++) {
        if (s[i] == target) {
            if (ck > 0) { current[ck] = '\0'; segs[ns++] = strdup(current); ck = 0; }
        } else { current[ck++] = s[i]; }
    }
    if (ck > 0) { current[ck] = '\0'; segs[ns++] = strdup(current); }
    free(current);
    uint64_t total = 0;
    for (size_t i = 0; i < ns; i++) {
        total += strlen(segs[i]) * (i + 1);
        free(segs[i]);
    }
    free(s);
    return total;
}

/* Map of string to values */
NOINLINE uint64_t dg_11(size_t n) {
    char *keys[256]; uint64_t *vals[256]; size_t vlens[256] = {0};
    size_t nk = 0;
    for (size_t i = 0; i < 5 && nk < 256; i++) {
        char buf[32]; snprintf(buf, 32, "key_%zu", i);
        keys[nk] = strdup(buf); vals[nk] = malloc(n * 8); vlens[nk] = 0; nk++;
    }
    for (size_t i = 0; i < n; i++) {
        size_t bucket = i % 5;
        vals[bucket][vlens[bucket]++] = i;
    }
    uint64_t total = 0;
    for (size_t i = 0; i < nk; i++) {
        total += strlen(keys[i]);
        for (size_t j = 0; j < vlens[i]; j++) total += vals[i][j];
        free(keys[i]); free(vals[i]);
    }
    return total;
}

/* Run-length encoding */
NOINLINE uint64_t dg_12(uint64_t *data, size_t n) {
    /* sort */
    for (size_t i = 0; i < n; i++)
        for (size_t j = i+1; j < n; j++)
            if (data[i] > data[j]) { uint64_t t = data[i]; data[i] = data[j]; data[j] = t; }
    uint64_t total = 0;
    size_t i = 0;
    while (i < n) {
        uint64_t val = data[i], count = 0;
        while (i < n && data[i] == val) { count++; i++; }
        total += val * count;
    }
    free(data);
    return total;
}

/* Build label-value pairs */
NOINLINE uint64_t dg_13(size_t n) {
    char **labels = malloc(n * sizeof(char*));
    uint64_t *values = malloc(n * 8);
    for (size_t i = 0; i < n; i++) {
        labels[i] = malloc(32);
        snprintf(labels[i], 32, "item_%zu", i);
        values[i] = i * 17 + 3;
    }
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) {
        sum += strlen(labels[i]) + values[i];
        free(labels[i]);
    }
    free(labels); free(values);
    return sum;
}

/* Char manipulation with temp strings */
NOINLINE char *dg_14(char *s, size_t shift) {
    size_t n = strlen(s);
    char *line1 = malloc(n + 1), *line2 = malloc(n + 1);
    for (size_t i = 0; i < n; i++) { line1[i] = s[i]; line2[i] = s[(i + shift) % n]; }
    line1[n] = '\0'; line2[n] = '\0';
    char *result = malloc(2 * n + 2);
    snprintf(result, 2*n+2, "%s|%s", line1, line2);
    free(line1); free(line2); free(s);
    return result;
}

/* Array of array pointers */
NOINLINE uint64_t dg_15(size_t n) {
    uint64_t **outer = malloc(n * sizeof(uint64_t*));
    size_t *sizes = malloc(n * sizeof(size_t));
    for (size_t i = 0; i < n; i++) {
        sizes[i] = i + 1;
        outer[i] = malloc(sizes[i] * 8);
        for (size_t j = 0; j <= i; j++) outer[i][j] = i + j;
    }
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) {
        for (size_t j = 0; j < sizes[i]; j++) sum += outer[i][j];
        free(outer[i]);
    }
    free(outer); free(sizes);
    return sum;
}

/* Partition with temp arrays */
NOINLINE uint64_t dg_16(uint64_t *data, size_t n) {
    uint64_t total = 0;
    for (size_t p = 0; p < n; p++) {
        uint64_t *less = malloc(n * 8), *greater = malloc(n * 8);
        size_t nl = 0, ng = 0;
        for (size_t i = 0; i < n; i++) {
            if (data[i] < data[p]) less[nl++] = data[i];
            else if (data[i] > data[p]) greater[ng++] = data[i];
        }
        total += nl + ng;
        free(less); free(greater);
    }
    free(data);
    return total;
}

/* Adjacency list */
NOINLINE uint64_t dg_17(size_t n) {
    size_t *adj_lens = calloc(n, sizeof(size_t));
    size_t **adj = malloc(n * sizeof(size_t*));
    for (size_t i = 0; i < n; i++) adj[i] = malloc(n * sizeof(size_t));
    for (size_t i = 0; i < n; i++)
        for (size_t j = i+1; j < n; j++)
            if ((i+j) % 3 != 0) {
                adj[i][adj_lens[i]++] = j;
                adj[j][adj_lens[j]++] = i;
            }
    uint64_t total = 0;
    for (size_t i = 0; i < n; i++) {
        total += i * adj_lens[i];
        free(adj[i]);
    }
    free(adj); free(adj_lens);
    return total;
}

/* Multiple string transforms */
NOINLINE uint64_t dg_18(char *s) {
    char *words[256]; size_t nw = 0;
    char *copy = strdup(s);
    char *tok = strtok(copy, " ");
    while (tok && nw < 256) { words[nw++] = strdup(tok); tok = strtok(NULL, " "); }
    char *rev_words[256];
    for (size_t i = 0; i < nw; i++) {
        size_t len = strlen(words[i]);
        rev_words[i] = malloc(len + 1);
        for (size_t j = 0; j < len; j++) rev_words[i][j] = words[i][len-1-j];
        rev_words[i][len] = '\0';
    }
    uint64_t total = 0;
    for (size_t i = 0; i < nw; i++) {
        for (size_t j = 0; rev_words[i][j]; j++) total += toupper(rev_words[i][j]);
        free(words[i]); free(rev_words[i]);
    }
    free(copy); free(s);
    return total;
}

/* Array of optional boxed values */
NOINLINE uint64_t dg_19(uint64_t n) {
    uint64_t **items = malloc(n * sizeof(uint64_t*));
    for (uint64_t i = 0; i < n; i++) {
        if (i % 3 == 0) { items[i] = malloc(8); *items[i] = i * i; }
        else items[i] = NULL;
    }
    uint64_t sum = 0;
    for (uint64_t i = 0; i < n; i++) {
        if (items[i]) { sum += *items[i]; free(items[i]); }
    }
    free(items);
    return sum;
}

/* Prefix + suffix sums */
NOINLINE uint64_t dg_20(uint64_t *data, size_t n) {
    uint64_t *prefix = malloc(n * 8), *suffix = malloc(n * 8);
    uint64_t acc = 0;
    for (size_t i = 0; i < n; i++) { acc += data[i]; prefix[i] = acc; }
    acc = 0;
    for (size_t i = n; i > 0; i--) { acc += data[i-1]; suffix[i-1] = acc; }
    uint64_t max_diff = 0;
    for (size_t i = 0; i < n; i++) {
        uint64_t d = prefix[i] > suffix[i] ? prefix[i] - suffix[i] : suffix[i] - prefix[i];
        if (d > max_diff) max_diff = d;
    }
    free(prefix); free(suffix); free(data);
    return max_diff;
}

/* =========================================================================
   BOUNDS CHECKING (bc_01 .. bc_20)
   C: raw pointer arithmetic, no checks.
   ========================================================================= */

NOINLINE int bc_01(const uint64_t *data, size_t n, uint64_t target, size_t *out_idx) {
    size_t lo = 0, hi = n;
    while (lo < hi) {
        size_t mid = lo + (hi - lo) / 2;
        if (data[mid] == target) { *out_idx = mid; return 1; }
        else if (data[mid] < target) lo = mid + 1;
        else hi = mid;
    }
    return 0;
}

NOINLINE uint64_t bc_02(uint64_t *data, size_t n) {
    uint64_t swaps = 0;
    for (size_t i = 1; i < n; i++) {
        uint64_t key = data[i]; size_t j = i;
        while (j > 0 && data[j-1] > key) { data[j] = data[j-1]; j--; swaps++; }
        data[j] = key;
    }
    return swaps;
}

NOINLINE uint64_t *bc_03(const uint64_t *data, size_t n, size_t window, size_t *out_len) {
    if (window == 0 || window > n) { *out_len = 0; return NULL; }
    *out_len = n - window + 1;
    uint64_t *result = malloc(*out_len * 8);
    for (size_t i = 0; i <= n - window; i++) {
        uint64_t mx = data[i];
        for (size_t j = 1; j < window; j++) if (data[i+j] > mx) mx = data[i+j];
        result[i] = mx;
    }
    return result;
}

NOINLINE uint64_t bc_04(const uint64_t *a, const uint64_t *b, size_t na, size_t nb) {
    size_t n = na < nb ? na : nb;
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) sum += a[i] * b[i];
    return sum;
}

NOINLINE uint64_t bc_05(const uint64_t *data, size_t n) {
    uint64_t inv = 0;
    for (size_t i = 0; i < n; i++)
        for (size_t j = i+1; j < n; j++)
            if (data[i] > data[j]) inv++;
    return inv;
}

NOINLINE uint64_t bc_06(uint64_t *data, size_t n, size_t gap) {
    uint64_t moves = 0;
    while (gap > 0) {
        for (size_t i = gap; i < n; i++) {
            uint64_t temp = data[i]; size_t j = i;
            while (j >= gap && data[j-gap] > temp) { data[j] = data[j-gap]; j -= gap; moves++; }
            data[j] = temp;
        }
        gap /= 2;
    }
    return moves;
}

NOINLINE int64_t *bc_07(const uint64_t *data, size_t n, size_t *out_len) {
    if (n < 3) { *out_len = 0; return NULL; }
    size_t rlen = n - 2;
    int64_t *result = malloc(rlen * 8);
    for (size_t i = 1; i < n-1; i++)
        result[i-1] = -(int64_t)data[i-1] + 2*(int64_t)data[i] - (int64_t)data[i+1];
    int64_t *smoothed = malloc(rlen * 8);
    for (size_t i = 0; i < rlen; i++) {
        int64_t l = (i > 0) ? result[i-1] : result[i];
        int64_t r = (i+1 < rlen) ? result[i+1] : result[i];
        smoothed[i] = (l + result[i] + r) / 3;
    }
    free(result); *out_len = rlen;
    return smoothed;
}

NOINLINE uint64_t bc_08(const uint64_t *data, size_t n, uint64_t min_prom) {
    uint64_t count = 0;
    for (size_t i = 1; i+1 < n; i++) {
        if (data[i] > data[i-1] && data[i] > data[i+1]) {
            uint64_t lmin = data[i];
            for (size_t j = i; j > 0; j--) {
                if (data[j-1] < lmin) lmin = data[j-1];
                if (data[j-1] > data[i]) break;
            }
            if (data[i] - lmin >= min_prom) count++;
        }
    }
    return count;
}

NOINLINE uint64_t bc_09(uint64_t *data, size_t n) {
    uint64_t passes = 0;
    while (1) {
        int swapped = 0;
        for (size_t i = 1; i < n; i++)
            if (data[i-1] > data[i]) { uint64_t t = data[i-1]; data[i-1] = data[i]; data[i] = t; swapped = 1; }
        passes++;
        if (!swapped) break;
    }
    return passes;
}

NOINLINE uint64_t bc_10(const uint64_t *data, size_t n, size_t dim) {
    size_t d = dim < n ? dim : n;
    uint64_t sum = 0;
    for (size_t i = 0; i < d; i++)
        for (size_t j = 0; j < d; j++) {
            uint64_t cell = 0;
            for (size_t k = 0; k < d; k++) {
                size_t ai = i*d+k, bi = k*d+j;
                if (ai < n && bi < n) cell += data[ai] * data[bi];
            }
            sum += cell;
        }
    return sum;
}

NOINLINE void bc_11(uint64_t *data, size_t n, size_t *lo_out, size_t *hi_out) {
    if (n == 0) { *lo_out = 0; *hi_out = 0; return; }
    uint64_t pivot = data[n/2];
    size_t lo = 0, mid = 0, hi = n;
    while (mid < hi) {
        if (data[mid] < pivot) { uint64_t t = data[lo]; data[lo] = data[mid]; data[mid] = t; lo++; mid++; }
        else if (data[mid] > pivot) { hi--; uint64_t t = data[mid]; data[mid] = data[hi]; data[hi] = t; }
        else mid++;
    }
    *lo_out = lo; *hi_out = hi;
}

NOINLINE uint64_t *bc_12(const uint64_t *data, size_t n, size_t window, size_t *out_len) {
    if (window == 0 || window > n) { *out_len = 0; return NULL; }
    *out_len = n - window + 1;
    uint64_t *result = malloc(*out_len * 8);
    uint64_t *win = malloc(window * 8);
    memcpy(win, data, window * 8);
    /* sort window */
    for (size_t i = 0; i < window; i++)
        for (size_t j = i+1; j < window; j++)
            if (win[i] > win[j]) { uint64_t t = win[i]; win[i] = win[j]; win[j] = t; }
    result[0] = win[window/2];
    for (size_t i = window; i < n; i++) {
        uint64_t old = data[i-window], nv = data[i];
        /* remove old */
        for (size_t j = 0; j < window; j++) {
            if (win[j] == old) {
                memmove(win+j, win+j+1, (window-1-j)*8);
                break;
            }
        }
        /* insert nv in sorted position */
        size_t pos = 0;
        while (pos < window-1 && win[pos] < nv) pos++;
        memmove(win+pos+1, win+pos, (window-1-pos)*8);
        win[pos] = nv;
        result[i-window+1] = win[window/2];
    }
    free(win);
    return result;
}

NOINLINE uint64_t bc_13(const uint64_t *data, size_t n) {
    uint64_t *prefix = malloc((n+1) * 8);
    prefix[0] = 0;
    for (size_t i = 0; i < n; i++) prefix[i+1] = prefix[i] + data[i];
    uint64_t total = 0;
    for (size_t i = 0; i < n; i++)
        for (size_t j = i+1; j <= n; j++)
            total += prefix[j] - prefix[i];
    free(prefix);
    return total;
}

NOINLINE uint64_t bc_14(uint64_t *data, size_t n, uint64_t shrink) {
    size_t gap = n; uint64_t swaps = 0; int sorted = 0;
    while (!sorted) {
        gap = (size_t)((double)gap / shrink); if (gap < 1) gap = 1;
        sorted = (gap == 1);
        for (size_t i = 0; i + gap < n; i++)
            if (data[i] > data[i+gap]) {
                uint64_t t = data[i]; data[i] = data[i+gap]; data[i+gap] = t;
                sorted = 0; swaps++;
            }
    }
    return swaps;
}

NOINLINE uint64_t *bc_15(const uint64_t *data, size_t n, size_t *out_len) {
    uint64_t *result = malloc(n * 8);
    for (size_t i = 0; i < n; i++) {
        uint64_t l = (i > 0) ? data[i-1] : data[i];
        uint64_t r = (i+1 < n) ? data[i+1] : data[i];
        result[i] = (l + data[i] + r) / 3;
    }
    *out_len = n;
    return result;
}

NOINLINE uint64_t bc_16(const uint64_t *data, size_t n, size_t stride) {
    if (stride == 0) return 0;
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i += stride) {
        sum += data[i];
        if (i + stride < n) sum += data[i] * data[i + stride];
    }
    return sum;
}

NOINLINE uint64_t bc_17(uint64_t *data, size_t n) {
    int sorted = 0; uint64_t passes = 0;
    while (!sorted) {
        sorted = 1;
        for (size_t i = 1; i < n-1; i += 2)
            if (data[i] > data[i+1]) { uint64_t t = data[i]; data[i] = data[i+1]; data[i+1] = t; sorted = 0; }
        for (size_t i = 0; i < n-1; i += 2)
            if (data[i] > data[i+1]) { uint64_t t = data[i]; data[i] = data[i+1]; data[i+1] = t; sorted = 0; }
        passes++;
    }
    return passes;
}

NOINLINE uint64_t bc_18(const uint64_t *data, size_t n, size_t width) {
    if (width == 0) return 0;
    size_t rows = (n + width - 1) / width;
    uint64_t sum = 0;
    for (size_t r = 0; r < rows; r++) {
        if (r % 2 == 0) {
            for (size_t c = 0; c < width; c++) {
                size_t idx = r * width + c; if (idx < n) sum += data[idx];
            }
        } else {
            for (size_t c = width; c > 0; c--) {
                size_t idx = r * width + c - 1; if (idx < n) sum += data[idx] * 2;
            }
        }
    }
    return sum;
}

NOINLINE uint64_t bc_19(const uint64_t *data, size_t n) {
    uint64_t count = 0;
    for (size_t i = 0; i < n; i++)
        for (size_t j = i+1; j < n; j++)
            if (data[i] > 2 * data[j]) count++;
    return count;
}

NOINLINE uint64_t bc_20(uint64_t *data, size_t n, size_t k) {
    if (n == 0) return 0;
    k = k % n;
    /* reverse all */
    for (size_t i = 0; i < n/2; i++) { uint64_t t = data[i]; data[i] = data[n-1-i]; data[n-1-i] = t; }
    /* reverse first k */
    for (size_t i = 0; i < k/2; i++) { uint64_t t = data[i]; data[i] = data[k-1-i]; data[k-1-i] = t; }
    /* reverse rest */
    for (size_t i = 0; i < (n-k)/2; i++) { uint64_t t = data[k+i]; data[k+i] = data[n-1-i]; data[n-1-i] = t; }
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) sum += data[i] * i;
    return sum;
}

/* =========================================================================
   ? OPERATOR (qm_01 .. qm_20)
   C: if-null/if-error checks with early return. No Option/Result types.
   ========================================================================= */

NOINLINE int qm_01(const uint64_t *data, size_t n, uint64_t target, size_t *out) {
    if (n == 0) return 0;
    size_t lo = 0, hi = n - 1;
    while (lo <= hi) {
        size_t mid = lo + (hi - lo) / 2;
        if (mid >= n) return 0;
        if (data[mid] == target) { *out = mid; return 1; }
        else if (data[mid] < target) lo = mid + 1;
        else { if (mid == 0) return 0; hi = mid - 1; }
    }
    return 0;
}

NOINLINE int qm_02(const char *s, uint64_t *out) {
    uint64_t total = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " \t\n");
    while (tok) {
        char *eq = strchr(tok, '=');
        if (!eq) { *out = 0; return 0; }
        *eq = '\0';
        char *endp; uint64_t val = strtoull(eq+1, &endp, 10);
        if (*endp != '\0') { *out = 0; return 0; }
        total += strlen(tok) + val;
        tok = strtok(NULL, " \t\n");
    }
    *out = total; return 1;
}

NOINLINE int qm_03(const uint64_t *data, const int *valid, size_t n, uint64_t *out) {
    uint64_t sum = 0, count = 0;
    for (size_t i = 0; i < n; i++) {
        if (!valid[i]) { *out = 0; return 0; }
        sum += data[i]; count++;
    }
    *out = sum * count; return 1;
}

NOINLINE int qm_04(const uint64_t *data, size_t n, uint64_t target, size_t *out_start, uint64_t *out_sum) {
    size_t win = 3;
    if (n < win) return 0;
    for (size_t s = 0; s + win <= n; s++) {
        int all = 1; uint64_t wsum = 0;
        for (size_t j = 0; j < win; j++) {
            if (s + j >= n) return 0;
            wsum += data[s+j];
            if (data[s+j] <= target) all = 0;
        }
        if (all) { *out_start = s; *out_sum = wsum; return 1; }
    }
    return 0;
}

NOINLINE int qm_05(const char *s, uint64_t *out) {
    uint64_t sum = 0, count = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " \t\n");
    while (tok) {
        char *endp; uint64_t val = strtoull(tok, &endp, 10);
        if (*endp != '\0') { *out = 0; return 0; }
        sum += val; count++;
        tok = strtok(NULL, " \t\n");
    }
    if (count == 0) return 0;
    *out = sum / count; return 1;
}

NOINLINE int qm_06(const uint64_t *data, size_t n, uint64_t *out) {
    if (n < 3) return 0;
    uint64_t first = data[0], last = data[n-1], mid = data[n/2];
    if (last < first) return 0;
    uint64_t range = last - first;
    uint64_t center = first + range / 2;
    uint64_t dev = mid > center ? mid - center : center - mid;
    *out = range + dev; return 1;
}

NOINLINE int qm_07(const char *s, uint64_t *out) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " \t\n");
    while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " \t\n"); }
    if (nw == 0) return 0;
    char fc = words[0][0], lc = words[nw-1][strlen(words[nw-1])-1];
    char *mid_word = words[nw/2];
    if (!mid_word[0]) return 0;
    *out = ((uint64_t)fc + lc) * strlen(mid_word); return 1;
}

NOINLINE int qm_08(const int64_t *data, const int *valid, size_t n, int64_t *out) {
    int64_t sum = 0, max = 0;
    for (size_t i = 0; i < n; i++) {
        if (!valid[i]) return 0;
        sum += data[i];
        if (data[i] > max) max = data[i];
    }
    *out = sum + max; return 1;
}

NOINLINE int qm_09(const uint64_t *data, size_t n, uint64_t target, size_t *lo_out, size_t *hi_out) {
    if (n < 2) return 0;
    size_t lo = 0, hi = n - 1;
    while (lo < hi) {
        if (lo >= n || hi >= n) return 0;
        uint64_t sum = data[lo] + data[hi];
        if (sum == target) { *lo_out = lo; *hi_out = hi; return 1; }
        else if (sum < target) lo++;
        else hi--;
    }
    return 0;
}

NOINLINE int qm_10(const char *s, size_t n, uint64_t *out) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " \t\n");
    while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " \t\n"); }
    if (n >= nw) return 0;
    char *word = words[n];
    size_t wlen = strlen(word);
    if (wlen == 0) return 0;
    char ch = word[n % wlen];
    char *rword = words[nw - 1 - n];
    size_t rwlen = strlen(rword);
    if (rwlen == 0) return 0;
    char rch = rword[rwlen - 1 - (n % rwlen)];
    *out = (uint64_t)ch + rch; return 1;
}

NOINLINE int qm_11(const uint64_t *data, size_t n, size_t *out_idx, uint64_t *out_val) {
    if (n < 2) return 0;
    for (size_t i = 0; i < n - 1; i++) {
        if (i >= n || i+1 >= n) return 0;
        uint64_t a = data[i], b = data[i+1];
        if (a > 0 && b > 0) {
            uint64_t sum = a + b;
            if (sum > 0 && (sum & (sum - 1)) == 0) { *out_idx = i; *out_val = sum; return 1; }
        }
    }
    return 0;
}

NOINLINE int qm_12(const uint64_t *data, const int *valid, size_t n, uint64_t threshold, uint64_t *out) {
    uint64_t sum = 0, count = 0;
    for (size_t i = 0; i < n; i++) {
        if (!valid[i]) return 0;
        if (data[i] > threshold) { sum += data[i]; count++; }
    }
    if (count == 0) return 0;
    *out = sum / count; return 1;
}

NOINLINE int qm_13(const uint64_t *data, size_t n, uint64_t divisor, uint64_t *out) {
    if (divisor == 0) return 0;
    uint64_t acc = 0;
    for (size_t i = 0; i < n; i++) {
        if (i >= n) return 0;
        if (acc + data[i] < acc) return 0; /* overflow */
        acc += data[i];
        if ((i + 1) % (size_t)divisor == 0) {
            if (divisor == 0) return 0;
            acc /= divisor;
        }
    }
    *out = acc; return 1;
}

NOINLINE int qm_14(const char *s, uint64_t *out) {
    uint64_t nums[256]; size_t nn = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " \t\n");
    while (tok) {
        char *endp; uint64_t val = strtoull(tok, &endp, 10);
        if (*endp != '\0') return 0;
        nums[nn++] = val;
        tok = strtok(NULL, " \t\n");
    }
    if (nn == 0) return 0;
    *out = nums[0] + nums[nn-1] + nums[nn/2]; return 1;
}

NOINLINE int qm_15(const uint64_t *data, size_t n, size_t stride, uint64_t *out) {
    if (stride == 0) return 0;
    size_t rows = n / stride;
    uint64_t sum = 0;
    for (size_t r = 0; r < rows; r++)
        for (size_t c = 0; c < stride; c++) {
            size_t idx = r * stride + c;
            if (idx >= n) return 0;
            sum += data[idx];
        }
    *out = sum; return 1;
}

NOINLINE int qm_16(const int64_t *data, const int *valid, size_t n, int64_t *out) {
    int64_t sum = 0, pos = 0, neg = 0;
    for (size_t i = 0; i < n; i++) {
        if (!valid[i]) return 0;
        sum += data[i];
        if (data[i] > 0) pos++;
        else if (data[i] < 0) neg++;
    }
    *out = sum * (pos - neg); return 1;
}

NOINLINE int qm_17(const uint64_t *data, size_t n, size_t window, uint64_t *out) {
    if (window == 0 || n == 0) return 0;
    uint64_t threshold = data[0], crossings = 0;
    for (size_t i = 0; i + 1 < n; i++) {
        if (i >= n || i + 1 >= n) return 0;
        if ((data[i] < threshold) != (data[i+1] < threshold)) crossings++;
    }
    *out = crossings; return 1;
}

NOINLINE int qm_18(const char *s, uint64_t *out) {
    const char *first = strchr(s, ' ');
    if (!first) return 0;
    const char *last = strrchr(s, ' ');
    if (!last || first >= last) return 0;
    /* find first word in middle */
    const char *mid_start = first + 1;
    while (*mid_start == ' ') mid_start++;
    const char *mid_end = mid_start;
    while (*mid_end && *mid_end != ' ') mid_end++;
    if (mid_start == mid_end) return 0;
    *out = (uint64_t)(*mid_start) * (size_t)(mid_end - mid_start); return 1;
}

NOINLINE int qm_19(const uint64_t *data, size_t n, size_t chunk_size, uint64_t *out) {
    if (chunk_size == 0) return 0;
    uint64_t first_sum = 0, last_sum = 0;
    /* first chunk */
    size_t end = chunk_size < n ? chunk_size : n;
    for (size_t i = 0; i < end; i++) {
        if (i >= n) return 0;
        if (first_sum + data[i] < first_sum) return 0;
        first_sum += data[i];
    }
    /* last chunk */
    size_t last_start = (n / chunk_size) * chunk_size;
    if (last_start >= n) last_start = n > chunk_size ? n - chunk_size : 0;
    for (size_t i = last_start; i < n; i++) {
        if (i >= n) return 0;
        last_sum += data[i];
    }
    *out = first_sum + last_sum; return 1;
}

NOINLINE int qm_20(const char *s, uint64_t *out) {
    uint64_t sum = 0, count = 0, max = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, ",");
    while (tok) {
        while (*tok == ' ') tok++;
        char *endp; uint64_t val = strtoull(tok, &endp, 10);
        if (*endp != '\0' && *endp != ' ' && *endp != '\n') return 0;
        sum += val; if (val > max) max = val; count++;
        tok = strtok(NULL, ",");
    }
    if (count == 0) return 0;
    *out = sum + max + count; return 1;
}

/* =========================================================================
   PANIC / UNWIND (pu_01 .. pu_20)
   C: no panics, just proceeds (or returns error). Equivalent logic.
   ========================================================================= */

NOINLINE uint64_t pu_01(const uint64_t *data, size_t n) {
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) sum += data[i];
    return sum / n + data[0] + data[n-1];
}

NOINLINE uint64_t pu_02(const char *s) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " "); while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " "); }
    char fc = words[0][0], lc = words[nw-1][strlen(words[nw-1])-1];
    return ((uint64_t)fc + lc) * (strlen(words[0]) + strlen(words[nw-1]));
}

NOINLINE uint64_t pu_03(const uint64_t *data, size_t n, size_t window) {
    uint64_t sum = 0;
    for (size_t i = 0; i + window <= n; i++) {
        uint64_t ws = 0;
        for (size_t j = 0; j < window; j++) ws += data[i+j];
        sum += ws;
    }
    return sum;
}

NOINLINE uint64_t pu_04(const char *s) {
    uint64_t sum = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " ");
    while (tok) { sum += strtoull(tok, NULL, 10); tok = strtok(NULL, " "); }
    return sum;
}

NOINLINE uint64_t pu_05(const uint64_t *data, size_t n) {
    return data[0] + data[n-1] + data[n/2] + data[n/4] + data[3*n/4];
}

NOINLINE uint64_t pu_06(const char *s, size_t n_char) {
    uint64_t total = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " ");
    while (tok) { size_t len = strlen(tok); total += tok[n_char % len]; tok = strtok(NULL, " "); }
    return total;
}

NOINLINE uint64_t pu_07(const uint64_t *data, size_t n, size_t stride) {
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i += stride) {
        sum += data[i];
        if (i + stride < n) sum += data[i] * data[i+stride];
    }
    return sum;
}

NOINLINE uint64_t pu_08(const char *s) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " "); while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " "); }
    uint64_t sum = 0;
    for (size_t i = 0; words[0][i]; i++) sum += words[0][i];
    for (size_t i = 0; words[nw/2][i]; i++) sum += words[nw/2][i];
    for (size_t i = 0; words[nw-1][i]; i++) sum += words[nw-1][i];
    return sum;
}

NOINLINE uint64_t pu_09(const uint64_t *data, size_t n) {
    uint64_t result = 0;
    for (size_t i = 0; i < n; i++) result += data[data[i] % n];
    return result;
}

NOINLINE uint64_t pu_10(const char *s) {
    char upper[1024]; size_t i = 0;
    for (; s[i] && i < 1023; i++) upper[i] = toupper(s[i]);
    upper[i] = '\0';
    char *words[256]; size_t nw = 0;
    char *tok = strtok(upper, " "); while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " "); }
    return (uint64_t)words[0][0] + words[1][0] + words[nw-1][strlen(words[nw-1])-1];
}

NOINLINE uint64_t pu_11(const uint64_t *data, size_t n, size_t window) {
    uint64_t *result = malloc(n * 8);
    for (size_t i = 0; i < n; i++) {
        size_t start = (i >= window) ? i - window : 0;
        uint64_t sum = 0;
        for (size_t j = start; j <= i; j++) sum += data[j];
        result[i] = sum;
    }
    uint64_t total = 0;
    for (size_t i = 0; i < n; i++) total += result[i];
    free(result);
    return total;
}

NOINLINE uint64_t pu_12(const char *s) {
    size_t n = strlen(s); uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) {
        if (isalpha(s[i])) sum += s[i] + s[(i+1) % n];
    }
    return sum;
}

NOINLINE uint64_t pu_13(const uint64_t *data, size_t n) {
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) sum += data[i] * data[(n-1-i) % n];
    return sum + data[n/2];
}

NOINLINE uint64_t pu_14(const char *s, size_t count) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " "); while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " "); }
    uint64_t sum = 0;
    for (size_t i = 0; i < count && i < nw; i++) {
        size_t wl = strlen(words[i]);
        sum += words[i][0] + words[i][wl-1];
    }
    return sum;
}

NOINLINE uint64_t pu_15(const uint64_t *data, size_t n) {
    uint64_t *running = malloc(n * 8); uint64_t acc = 0;
    for (size_t i = 0; i < n; i++) { acc += data[i]; running[i] = acc; }
    uint64_t r = running[n-1] - running[0] + running[n/2];
    free(running);
    return r;
}

NOINLINE uint64_t pu_16(const char *s) {
    uint64_t sum = 0, count = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, ",");
    while (tok) { while (*tok == ' ') tok++; sum += strtoull(tok, NULL, 10); count++; tok = strtok(NULL, ","); }
    return sum * count;
}

NOINLINE uint64_t pu_17(const uint64_t *data, size_t n, size_t chunk) {
    uint64_t sum = 0; size_t i = 0;
    while (i + chunk <= n) {
        uint64_t cs = 0;
        for (size_t j = 0; j < chunk; j++) cs += data[i+j];
        sum += cs * data[i];
        i += chunk;
    }
    return sum;
}

NOINLINE uint64_t pu_18(const char *s) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " "); while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " "); }
    uint64_t total = 0;
    for (size_t i = 0; i < nw; i++) {
        size_t wl = strlen(words[i]);
        total += wl * ((uint64_t)words[i][0] + words[i][wl-1]);
    }
    return total;
}

NOINLINE uint64_t pu_19(const uint64_t *data, size_t n) {
    uint64_t sum = 0;
    for (size_t i = 0; i < n; i++) sum += data[i] * data[n-1-i];
    return sum;
}

NOINLINE uint64_t pu_20(const char *s) {
    char *words[256]; size_t nw = 0;
    char copy[1024]; strncpy(copy, s, 1023); copy[1023] = '\0';
    char *tok = strtok(copy, " "); while (tok && nw < 256) { words[nw++] = tok; tok = strtok(NULL, " "); }
    uint64_t result = 0;
    for (size_t i = 0; i < nw; i++) {
        size_t ni = (i+1) % nw;
        result += (uint64_t)words[i][0] ^ words[ni][strlen(words[ni])-1];
    }
    return result;
}

int main() {
    uint64_t data[64]; for (int i = 0; i < 64; i++) data[i] = i;
    uint64_t data2[100]; for (int i = 0; i < 100; i++) data2[i] = 100 + i;
    const char *s = "hello world foo bar baz 123 testing seven";

    /* om */
    { uint64_t *a = malloc(40), *b = malloc(40); memcpy(a,(uint64_t[]){5,3,8,1,7},40); memcpy(b,(uint64_t[]){2,9,4,6,0},40); size_t ol; uint64_t *r = om_01(a,5,b,5,&ol); black_box_ptr(r); free(r); }
    { char *a = strdup("hello world"), *b = strdup("foo bar"); char *r = om_02(a,b); black_box_ptr(r); free(r); }
    { uint64_t *d = malloc(40); memcpy(d,(uint64_t[]){10,20,30,40,50},40); uint64_t *e,*o; size_t ne,no; om_03(d,5,&e,&ne,&o,&no); free(e); free(o); }
    { char *d = strdup("the quick brown fox"); char *r = om_04(d,3); black_box_ptr(r); free(r); }
    { uint64_t *a=malloc(40),*b=malloc(40),*c=malloc(40); for(int i=0;i<5;i++){a[i]=i+1;b[i]=i+6;c[i]=i+11;} size_t ol; uint64_t *r=om_05(a,5,b,5,c,5,&ol); free(r); }
    { char *d = strdup("abcdef"); char *r = om_06(d); free(r); }
    { uint64_t *d=malloc(40); memcpy(d,(uint64_t[]){100,50,200,25,75},40); size_t ol; int64_t *r=om_07(d,5,&ol); free(r); }
    { char *d=strdup("rust is great"); char *r=om_08(d,4); free(r); }
    { uint64_t *d=malloc(64); memcpy(d,(uint64_t[]){3,1,4,1,5,9,2,6},64); size_t ol; uint64_t *r=om_09(d,8,&ol); free(r); }
    { char *a=strdup("hello"),*b=strdup("world"),*c=strdup("!"); char *r=om_10(a,b,c); free(r); }
    { uint64_t *d=malloc(48); memcpy(d,(uint64_t[]){7,2,5,1,8,3},48); size_t ol; uint64_t *r=om_11(d,6,&ol); free(r); }
    { char *d=strdup("testing one two three"); char *r=om_12(d); free(r); }
    { uint64_t *a=malloc(24),*b=malloc(24); memcpy(a,(uint64_t[]){10,20,30},24); memcpy(b,(uint64_t[]){40,50,60},24); uint64_t oa[3],ob[3]; size_t ol; om_13(a,3,b,3,oa,ob,&ol); }
    { char *d=strdup("abcdefghij"); char *r=om_14(d,3); free(r); }
    { uint64_t *d=malloc(72); memcpy(d,(uint64_t[]){9,1,5,3,7,2,8,4,6},72); uint64_t *r=om_15(d,9); free(r); }
    { char *d=strdup("hello world test"); char *r=om_16(d); free(r); }
    { uint64_t *d=malloc(64); for(int i=0;i<8;i++)d[i]=i+1; size_t ol; uint64_t *r=om_17(d,8,&ol); free(r); }
    { char *a=strdup("the quick brown"),*b=strdup("fox jumps over"); char *r=om_18(a,b); free(r); }
    { uint64_t *d=malloc(48); memcpy(d,(uint64_t[]){5,10,15,20,25,30},48); size_t ol; uint64_t *r=om_19(d,6,&ol); free(r); }
    { char *d=strdup("abcdefghijklmnop"); char *r=om_20(d,5); free(r); }

    /* dg */
    black_box_u64(dg_01(8));
    { char *d=strdup("hello world foo"); black_box_u64(dg_02(d,3)); }
    black_box_u64(dg_03(10));
    { uint64_t *d=malloc(80); memcpy(d,(uint64_t[]){3,1,4,1,5,9,2,6,5,3},80); black_box_u64(dg_04(d,10)); }
    black_box_u64(dg_05(12));
    { char *d=strdup("the quick brown fox jumps"); black_box_u64(dg_06(d)); }
    black_box_u64(dg_07(6));
    { uint64_t *d=malloc(64); for(int i=0;i<8;i++)d[i]=(i+1)*10; char *r=dg_08(d,8); free(r); }
    black_box_u64(dg_09(15));
    { char *d=strdup("rust lang is great for systems"); black_box_u64(dg_10(d,'a')); }
    black_box_u64(dg_11(20));
    { uint64_t *d=malloc(72); memcpy(d,(uint64_t[]){7,2,5,1,8,3,6,4,9},72); black_box_u64(dg_12(d,9)); }
    black_box_u64(dg_13(8));
    { char *d=strdup("abcdefghij"); char *r=dg_14(d,2); free(r); }
    black_box_u64(dg_15(10));
    { uint64_t *d=malloc(48); memcpy(d,(uint64_t[]){100,50,200,25,75,150},48); black_box_u64(dg_16(d,6)); }
    black_box_u64(dg_17(7));
    { char *d=strdup("hello world test data"); black_box_u64(dg_18(d)); }
    black_box_u64(dg_19(16));
    { uint64_t *d=malloc(80); memcpy(d,(uint64_t[]){1,3,5,7,9,2,4,6,8,10},80); black_box_u64(dg_20(d,10)); }

    /* bc */
    { size_t idx; bc_01(data,64,10,&idx); }
    { uint64_t d[64]; memcpy(d,data,512); black_box_u64(bc_02(d,64)); }
    { size_t ol; uint64_t *r=bc_03(data,64,3,&ol); free(r); }
    black_box_u64(bc_04(data,data2,64,100));
    black_box_u64(bc_05(data,64));
    { uint64_t d[64]; memcpy(d,data,512); black_box_u64(bc_06(d,64,5)); }
    { size_t ol; int64_t *r=bc_07(data,64,&ol); free(r); }
    black_box_u64(bc_08(data,64,30));
    { uint64_t d[64]; memcpy(d,data,512); black_box_u64(bc_09(d,64)); }
    black_box_u64(bc_10(data,64,4));
    { uint64_t d[64]; memcpy(d,data,512); size_t lo,hi; bc_11(d,64,&lo,&hi); }
    { size_t ol; uint64_t *r=bc_12(data,64,7,&ol); free(r); }
    black_box_u64(bc_13(data,64));
    { uint64_t d[64]; memcpy(d,data,512); black_box_u64(bc_14(d,64,3)); }
    { size_t ol; uint64_t *r=bc_15(data,64,&ol); free(r); }
    black_box_u64(bc_16(data,64,8));
    { uint64_t d[64]; memcpy(d,data,512); black_box_u64(bc_17(d,64)); }
    black_box_u64(bc_18(data,64,5));
    black_box_u64(bc_19(data,64));
    { uint64_t d[64]; memcpy(d,data,512); black_box_u64(bc_20(d,64,10)); }

    /* qm */
    { size_t idx; qm_01(data,64,50,&idx); }
    { uint64_t out; qm_02(s,&out); }
    { uint64_t d[]={1,3,4}; int v[]={1,0,1}; uint64_t out; qm_03(d,v,3,&out); }
    { size_t os; uint64_t osum; qm_04(data,64,5,&os,&osum); }
    { uint64_t out; qm_05("123 456 abc 789",&out); }
    { uint64_t out; qm_06(data,64,&out); }
    { uint64_t out; qm_07(s,&out); }
    { int64_t d[]={1,-1,3}; int v[]={1,0,1}; int64_t out; qm_08(d,v,3,&out); }
    { size_t lo,hi; qm_09(data,64,5,&lo,&hi); }
    { uint64_t out; qm_10(s,3,&out); }
    { size_t idx; uint64_t val; qm_11(data,64,&idx,&val); }
    { uint64_t d[]={10,20,40}; int v[]={1,1,1}; uint64_t out; qm_12(d,v,3,25,&out); }
    { uint64_t out; qm_13(data,64,7,&out); }
    { uint64_t out; qm_14("10 20 30 40",&out); }
    { uint64_t out; qm_15(data,64,3,&out); }
    { int64_t d[]={5,-3,7}; int v[]={1,1,1}; int64_t out; qm_16(d,v,3,&out); }
    { uint64_t out; qm_17(data,64,10,&out); }
    { uint64_t out; qm_18(s,&out); }
    { uint64_t out; qm_19(data,64,8,&out); }
    { uint64_t out; qm_20("3,1,4,1,5,9,2,6",&out); }

    /* pu */
    black_box_u64(pu_01(data,64));
    black_box_u64(pu_02(s));
    black_box_u64(pu_03(data,64,10));
    black_box_u64(pu_04("123 456 789"));
    black_box_u64(pu_05(data,64));
    black_box_u64(pu_06(s,3));
    black_box_u64(pu_07(data,64,5));
    black_box_u64(pu_08("hello world"));
    black_box_u64(pu_09(data,64));
    black_box_u64(pu_10(s));
    { uint64_t *r = malloc(512); memcpy(r,pu_11(data,64,8),512); free(r); }
    black_box_u64(pu_12("test data string"));
    black_box_u64(pu_13(data,64));
    black_box_u64(pu_14(s,4));
    black_box_u64(pu_15(data,64));
    black_box_u64(pu_16("1,2,3,4,5"));
    black_box_u64(pu_17(data,64,3));
    black_box_u64(pu_18(s));
    black_box_u64(pu_19(data,64));
    black_box_u64(pu_20("the quick brown fox"));

    return 0;
}
