# X33: h=4 common-gcd gate

- **DAG node:** `x33_h4_common_gcd_gate`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved checker plus finite evidence.  This is not yet the
  official-row h=4 exclusion theorem.
- **Verifier:** `experimental/scripts/verify_x33_h4_common_gcd_gate.py`.
- **Certificate:**
  `experimental/data/certificates/x33-h4-common-gcd-gate/x33_h4_common_gcd_gate.json`.

## Statement

Let `n = 2^s`, let `p == 1 mod n`, and fix two disjoint 4-subsets of
exponents

```text
P,Q subset Z/nZ.
```

For `r=1,2,3`, define the elementary-difference polynomial

```text
E_r(X) =
  sum_{I subset P, |I|=r} X^{sum I}
  -
  sum_{J subset Q, |J|=r} X^{sum J},
```

with exponents reduced modulo `n`.  Then some Galois scaling of the pattern
is an h=4 top-three trade in `mu_n(F_p)` if and only if

```text
gcd(Phi_n, E_1, E_2, E_3) in F_p[X]
```

has positive degree.

Equivalently, degree zero certifies that the pattern and all of its Galois
scalings are not h=4 trades at that row.

## Proof

Because `p == 1 mod n`, all primitive `n`-th roots in `F_p` are Galois
scalings of a chosen generator:

```text
zeta^u,       u in (Z/nZ)^*.
```

For a fixed `u`, the scaled pattern is a top-three h=4 trade exactly when

```text
E_1(zeta^u)=E_2(zeta^u)=E_3(zeta^u)=0.
```

The primitive roots are precisely the roots of `Phi_n`.  Therefore such a
unit `u` exists if and only if `Phi_n` and all three `E_r` have a common root
over `F_p`, which is equivalent to the displayed gcd having positive degree.

For `n=2^s`,

```text
Phi_n(X)=X^(n/2)+1,
```

so the verifier computes the gcd with elementary modular polynomial arithmetic,
without factoring `Phi_n`.

## Relation to X32

X32 proves the h=4 branch split:

```text
h=4 trade = paid antipodal quotient branch
          or top-level 8-sparse norm-gate branch.
```

X33 gives the exact row-local checker for the second branch.  The first-sum
norm gate alone is too weak: it only tests `gcd(Phi_n,E_1)`.  The real h=4
obstruction is the full common gcd:

```text
gcd(Phi_n,E_1,E_2,E_3).
```

## Finite Evidence

The verifier checks two small boundary rows.  In both, non-antipodal
first-sum norm gates are abundant, but the full h=4 common-gcd survivor count
is zero:

```text
row             top-level E1 pairs     top-level common-gcd survivors   top-three pairs
---------------------------------------------------------------------------------------
F257 / mu16              712                         0                         3
F4993 / mu32           19860                         0                         7
```

All top-three pairs in these rows are the paid `mu_4` baseline:

```text
F257 / mu16:     3 = n/4 - 1
F4993 / mu32:    7 = n/4 - 1
```

Thus the extra h=4 equations are doing real work: they annihilate thousands
of first-sum top-level norm gates in the representative rows.

## What Remains

The official h=4 closure now has a precise certifier shape:

```text
For every non-antipodal h=4 pattern relevant to the row,
prove gcd(Phi_n,E_1,E_2,E_3)=1 in F_p[X],
or count the positive-degree survivors as a top-level norm-gate column.
```

This packet proves the checker and demonstrates the expected empty outcome at
small rows.  It does not supply the compressed official-row pattern list.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x33_h4_common_gcd_gate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x33_h4_common_gcd_gate.py --write-certificate
```
