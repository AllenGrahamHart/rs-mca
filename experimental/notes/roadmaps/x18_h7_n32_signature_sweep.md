# X18-H7: n=32 top-six signature sweep

- **DAG node:** `active_core_count_bound`.
- **Status:** exact finite evidence; no h=7 active partners before stripping in
  all checked n=32 rows.
- **Verifier:** `experimental/scripts/verify_x18_h7_n32_sweep.py`.
- **Certificate:**
  `experimental/data/certificates/x18-h7-n32-sweep/x18_h7_n32_sweep.json`.

## Scope

This packet tests the next minimal-signature row:

```text
h = 7,        t = h - 1 = 6.
```

For

```text
n = 32,  alpha in {2, 9/4, 5/2, 11/4, 3},
```

the verifier takes the first prime

```text
p == 1 mod n,        p > floor(n^alpha),
```

and enumerates all 7-subsets of `mu_n`, grouping by the top-six elementary
symmetric signature

```text
(e_1, e_2, e_3, e_4, e_5, e_6).
```

If this signature is injective on 7-subsets, then no h=7 active partner exists,
anchored or otherwise.  This is stronger than a post-strip statement.

As with the h=6 packet, this is not a fixed-`t=3` band-trade census.  The
tested condition is the minimal terminal condition `t=h-1=6`.

## Result

All checked h=7 signatures are injective.

```text
row                  p          7-subsets    signature collisions
---------------------------------------------------------------
n32, alpha=2         1153       3365856      0
n32, alpha=9/4       2593       3365856      0
n32, alpha=5/2       5857       3365856      0
n32, alpha=11/4      13921      3365856      0
n32, alpha=3         32801      3365856      0
```

Therefore:

```text
raw active h=7 partners = 0
post-strip h=7 non-toral residue = 0
```

in every checked row.

## Encoding

The verifier stores the top-six signature as

```text
(e_1 + p e_2,  e_3 + p e_4,  e_5 + p e_6),
```

and sorts the three `uint64` words lexicographically.  The largest row sorts
`C(32,7)=3365856` subsets.

## Interpretation

The raw-injectivity pattern now extends one more step at n=32:

```text
h=5: no top-four signature collisions through n=64, alpha=3
h=7: no top-six signature collisions through n=32, alpha=3
```

The pending h=6 packet tests the intervening size.  Together these scans
support the proposed closure route that, above the small-h artifacts, the
top-`h-1` elementary-symmetric signature is injective on h-subsets of `mu_n`.
That would make the raw active-core residue empty before the paid strip.  The
statement remains finite evidence, not a proof.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x18_h7_n32_sweep.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x18_h7_n32_sweep.py --write-certificate
```

Current replay: **30 PASS, 0 FAIL**.
