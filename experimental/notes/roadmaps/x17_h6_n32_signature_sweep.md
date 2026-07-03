# X17-H6: n=32 top-five signature sweep

- **DAG node:** `active_core_count_bound`.
- **Status:** exact finite evidence; no h=6 active partners before stripping in
  all checked n=32 rows.
- **Verifier:** `experimental/scripts/verify_x17_h6_n32_sweep.py`.
- **Certificate:**
  `experimental/data/certificates/x17-h6-n32-sweep/x17_h6_n32_sweep.json`.

## Scope

This packet tests the next minimal-signature row after X15:

```text
h = 6,        t = h - 1 = 5.
```

For

```text
n = 32,  alpha in {2, 9/4, 5/2, 11/4, 3},
```

the verifier takes the first prime

```text
p == 1 mod n,        p > floor(n^alpha),
```

and enumerates all 6-subsets of `mu_n`, grouping by the top-five elementary
symmetric signature

```text
(e_1, e_2, e_3, e_4, e_5).
```

If this signature is injective on 6-subsets, then no h=6 active partner exists,
anchored or otherwise.  This is stronger than a post-strip statement.

This is not the SP-CENSUS-2 fixed-`t=3` h=6 band census.  Here the tested
minimal terminal condition is `t=h-1=5`.

## Result

All checked h=6 signatures are injective.

```text
row                  p          6-subsets    signature collisions
---------------------------------------------------------------
n32, alpha=2         1153       906192       0
n32, alpha=9/4       2593       906192       0
n32, alpha=5/2       5857       906192       0
n32, alpha=11/4      13921      906192       0
n32, alpha=3         32801      906192       0
```

Therefore:

```text
raw active h=6 partners = 0
post-strip h=6 non-toral residue = 0
```

in every checked row.

## Encoding

The verifier stores the top-five signature as

```text
(e_1 + p e_2,  e_3 + p e_4,  e_5),
```

and sorts the three `uint64` words lexicographically.  This keeps the exact
scan small: the largest row sorts `C(32,6)=906192` subsets.  The analogous
`n=64,h=6` row would sort `C(64,6)=74974368` subsets and is intentionally not
part of this low-memory packet.

## Interpretation

Together with X15, this extends the raw-injectivity pattern:

```text
h=5: no top-four signature collisions through n=64, alpha=3
h=6: no top-five signature collisions through n=32, alpha=3
```

The evidence strengthens the proposed closure route that for sufficiently large
minimal terminal size, the top-`h-1` elementary-symmetric signature is
injective on h-subsets of `mu_n`, so the raw active-core residue is empty before
the paid strip.  The h=3 counterexamples and the h=4 cyclic-paid row still show
that the threshold and mechanism need proof rather than extrapolation.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x17_h6_n32_sweep.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x17_h6_n32_sweep.py --write-certificate
```

Current replay: **30 PASS, 0 FAIL**.
