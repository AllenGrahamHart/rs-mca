# X12-H3: active-core census replication

- **DAG node:** `active_core_count_bound`.
- **Task:** replicate the X-12 h=3 active-core counts in-repo.
- **Status:** evidence for the high-`q` route; exact verifier green.
- **Verifier:** `experimental/scripts/verify_x12_h3_active_core_census.py`.
- **Certificate:**
  `experimental/data/certificates/x12-h3-active-core-census/x12_h3_active_core_census.json`.

## Scope

For `h=3`, a locator has a second completely split `H`-fiber exactly when two
disjoint triples have the same first two elementary symmetric sums:

```text
e1(P) = e1(Q),      e2(P) = e2(Q).
```

The verifier enumerates all triples in `mu_n`, groups them by `(e1,e2)`, and
then counts anchored cores `P` with `1 in P` that have a disjoint partner `Q`
in the same group.  The cyclic/dihedral SP-CENSUS strip is applied to every
active partner.

The scan is exact for these rows:

```text
q ~ n^2:  first prime p > n^2, p = 1 mod n, n = 32,64,128,256
q ~ n^3:  first prime p > n^3, p = 1 mod n, n = 32,64,128,256
```

## Results

```text
row                 p          collision groups   C_3^nt   partner pairs
----------------------------------------------------------------------------
n32 q~n^2           1153       0                  0        0
n64 q~n^2           4289       0                  0        0
n128 q~n^2          17921      384                18       18
n256 q~n^2          65537      5504               129      129
n32 q~n^3           32801      0                  0        0
n64 q~n^3           262337     0                  0        0
n128 q~n^3          2100097    0                  0        0
n256 q~n^3          16777729   0                  0        0
```

The `q ~ n^2` active cores at `n=128` and `n=256` reproduce the X-12
boundary counts `18` and `129`.  They are not removed by the cyclic/dihedral
strip used by SP-CENSUS.

At the first `q > n^3` rows, the h=3 active-core count vanishes through
`n=256`.  This verifies the high-`q` signal in-repo for the first nontrivial
terminal-node rung.

## Interpretation

This does not prove high-`q` vanishing.  It does remove one integration gap:
the X-12 h=3 numbers are now replayable in the repository, and the boundary
mass is separated from the high-`q` rows by a clean exact census.

The next proof target can use this as the falsifier-backed statement:

```text
for h >= 3, after the full strip, C_h^nt vanishes once q >= n^c
```

with the empirical threshold currently compatible with `c = 3`, while the
official rows can afford any `c <= 6`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x12_h3_active_core_census.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x12_h3_active_core_census.py --write-certificate
```

Current replay: **38 PASS, 0 FAIL**.
