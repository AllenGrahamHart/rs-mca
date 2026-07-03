# X15-H5: empty sweep for the next campaign trade size

- **DAG node:** `active_core_count_bound`.
- **Status:** exact finite evidence; no h=5 active partners before stripping in
  all checked rows.
- **Verifier:** `experimental/scripts/verify_x15_h5_empty_sweep.py`.
- **Certificate:**
  `experimental/data/certificates/x15-h5-empty-sweep/x15_h5_empty_sweep.json`.

## Scope

This packet scans the next terminal trade size after X14:

```text
h = 5,        t = 4.
```

For

```text
n = 32,  alpha in {2, 9/4, 5/2, 3}
n = 64,  alpha in {2, 9/4, 5/2, 11/4, 3},
```

the verifier takes the first prime

```text
p == 1 mod n,        p > floor(n^alpha),
```

and enumerates all 5-subsets of `mu_n`, grouping by the top-four elementary
symmetric signature

```text
(e_1, e_2, e_3, e_4).
```

If this signature is injective on 5-subsets, then no h=5 active partner can
exist, anchored or otherwise.  This is stronger than a post-strip statement.

## Result

All checked h=5 signatures are injective.

```text
row                  p          5-subsets    signature collisions
---------------------------------------------------------------
n32, alpha=2         1153       201376       0
n32, alpha=9/4       2593       201376       0
n32, alpha=5/2       5857       201376       0
n32, alpha=3         32801      201376       0

n64, alpha=2         4289       7624512      0
n64, alpha=9/4       11777      7624512      0
n64, alpha=5/2       32833      7624512      0
n64, alpha=11/4      92737      7624512      0
n64, alpha=3         262337     7624512      0
```

Therefore:

```text
raw active h=5 partners = 0
post-strip h=5 non-toral residue = 0
```

in every checked row.

## Two-Word Signature

The verifier stores the top-four signature as

```text
(e_1 + p e_2,  e_3 + p e_4),
```

and sorts the two `uint64` words lexicographically.  This keeps the exact
low-memory sweep but removes the old `p^4 < 2^64` cap; the checked `n=64`
range now reaches `alpha=3`.

## Interpretation

X14 showed that h=4 active partners exist but are cyclic-paid in all checked
rows.  X15 shows the next size, h=5, is even cleaner at the checked scales:
there are no top-four signature collisions at all.

This is finite evidence, not a uniform proof.  It suggests that the h=5 proof
route may be ordinary injectivity/high-q exclusion rather than a paid-structure
classification.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x15_h5_empty_sweep.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x15_h5_empty_sweep.py --write-certificate
```

Current replay: **50 PASS, 0 FAIL**.
