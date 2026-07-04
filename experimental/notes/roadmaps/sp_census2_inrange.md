# SP-CENSUS-2: In-Range Anchored Split-Pair Census

- **DAG node:** `anchored_nontoral_pte_bound`.
- **Task:** SP-CENSUS-2.
- **Status:** falsifier for the strict `A_h^nt <= h n` target under the
  SP-CENSUS toral classifier.
- **Verifier:** `experimental/scripts/verify_sp_census2_inrange.py`.
- **Certificate:**
  `experimental/data/certificates/sp-census2-inrange/sp_census2_inrange.json`.

## Scope

The verifier enumerates anchored split pairs

```text
1 in P,  P cap Q = empty,  |P| = |Q| = h,
e_i(P) = e_i(Q), 1 <= i <= t,
```

and then removes the same toral charged classes used by SP-CENSUS:

```text
cyclic:    psi = F(x^m)
dihedral:  psi = F(x^m + alpha x^-m)
```

The remaining count is the measured `A_h^nt`.

Coverage is exact over the full disjoint `h` range for `n=16` and `n=24`.
For `n=32`, the low-memory default scan stops at `h=8`: the requested disjoint
ceiling is `h=16`, but `h=9` already requires sorting `C(32,9)=28048800`
masks per prime.  The later `n=32` primes are skipped in the default run after
the first falsifier is reproduced.

## Results

```text
row                       h scanned    A_nt total   max A_h^nt/(h n)   verdict
--------------------------------------------------------------------------------
F641 / mu16               4..8         0            0.0000             clear
F1153 / mu16              4..8         0            0.0000             clear
F4289 / mu16              4..8         0            0.0000             clear
F601 / mu24               4..12        32           0.1667             clear
F1201 / mu24              4..12        16           0.0833             clear
F1801 / mu24              4..12        0            0.0000             clear
F1153 / mu32              4..8         1236         3.8125             FALSIFIES
```

The violating row is already in range:

```text
n = 32, p = q = 1153, q > n^2 = 1024.
```

The violation occurs at `h=8`:

```text
A_8^nt = 976,     h n = 8 * 32 = 256,     ratio = 3.8125.
```

The same row has smaller non-toral counts before the violation:

```text
h=6: A_h^nt = 36
h=7: A_h^nt = 224
h=8: A_h^nt = 976
```

Every non-toral pair in the certificate includes full anatomy:

```text
Q/P exponent sets, locator coefficients, derivative coefficients,
derivative-zero exponents, route code, and defect degree.
```

All `1236` non-toral pairs in the falsifier row are primitive moment/PTE route
`3`.  Defect degrees are exactly at the expected bound:

```text
h=6: degree 2
h=7: degree 3
h=8: degree 4
```

The derivative-zero profile is mostly clean:

```text
0,0: 1158 pairs
0,1:   39 pairs
1,0:   39 pairs
```

## Interpretation

The strict X-10 target

```text
A_h^nt <= h n
```

is false as stated under the frozen SP-CENSUS toral classifier.  There are two
possible exits:

1. The `F_1153 / mu32` survivors are actually chargeable by a toral clause not
   implemented by the fiber-union classifier.
2. The target must be weakened, at least by a constant exceeding `3.8125` at
   this toy row, and the downstream tolerance ladder must absorb that loss.

This is not the old below-threshold low-q warning.  The falsifier sits above
the advertised `q >= n^2` line.

Follow-up `spc2_dihedral_g1_reclass.md` tested the cheapest missing paid
clause: adding all coprime dihedral pair-fiber partitions
`X^m + alpha X^-m` with `gcd(n,m)=1`.  It charges none of the h=8 survivors:

```text
old non-toral = 976
new non-toral = 976
```

So the boundary mass is not an omitted coprime-dihedral artifact.

## Verification

Run:

```bash
python3 experimental/scripts/verify_sp_census2_inrange.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_sp_census2_inrange.py --write-certificate
```

Current replay: **54 PASS, 0 FAIL**.
