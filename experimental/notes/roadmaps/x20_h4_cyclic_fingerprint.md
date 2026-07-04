# X20: h=4 cyclic fingerprint

- **DAG node:** `x20_h4_cyclic_fingerprint`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved fingerprint identities plus exact finite evidence.
- **Verifier:** `experimental/scripts/verify_x20_h4_cyclic_fingerprint.py`.
- **Certificate:**
  `experimental/data/certificates/x20-h4-cyclic-fingerprint/x20_h4_cyclic_fingerprint.json`.

## Statement

X14 showed that every checked `h=4`, `t=3` active partner is cyclic-paid.
This packet refines the observed cyclic charge into two explicit
fingerprints:

```text
1. mu_4 full fibers:                 P and Q are single fibers of X^4;
2. antipodal h=2 quotient lifts:      P and Q are unions of two antipodal
                                      pairs and descend through X^2.
```

The second family is the `cyclic:m=6` component seen only at the boundary row
`n=128, alpha=2`; since `gcd(128,6)=2`, the degree-window partition for `X^6`
is the same antipodal partition as `X^2`, but now lies in the allowed
`t < m` window for `t=3`.

## Algebraic Identities

Let `H = mu_n` with `4 | n`.

For a full `mu_4` fiber

```text
P = {a, ia, -a, -ia},
```

where `i^2 = -1` in `H`, the locator is

```text
L_P(X) = X^4 - a^4.
```

Thus its top-three elementary coefficients vanish.  Any two such fibers have
the same `h=4`, `t=3` signature and differ only in the constant coefficient.
This is the persistent `cyclic:m=4` family.

For an antipodal pair union

```text
P = {a, -a, b, -b},
```

the locator is

```text
L_P(X) = (X^2 - a^2)(X^2 - b^2)
       = X^4 - (a^2 + b^2)X^2 + a^2 b^2.
```

Hence `e_1(P)=e_3(P)=0`, and two such supports `P,Q` have the same
top-three signature exactly when their quotient pairs have the same sum in
`mu_{n/2}`:

```text
a^2 + b^2 = c^2 + d^2.
```

So the family is not new primitive `h=4` structure.  It is an `h=2`,
`t=1` quotient trade lifted through `X^2`, and therefore cyclic-pullback paid.

## Finite Fingerprint

The verifier reruns the X14 rows:

```text
n in {32,64,128},      alpha in {2,9/4,5/2,3},
p = first prime == 1 mod n above floor(n^alpha).
```

Every anchored active pair lands in one of the two fingerprints:

```text
row                  active pairs   mu4 full fiber   antipodal quotient lift   other
------------------------------------------------------------------------------------
n32, alpha=2              7               7                    0                 0
n32, alpha=9/4            7               7                    0                 0
n32, alpha=5/2            7               7                    0                 0
n32, alpha=3              7               7                    0                 0

n64, alpha=2             15              15                    0                 0
n64, alpha=9/4           15              15                    0                 0
n64, alpha=5/2           15              15                    0                 0
n64, alpha=3             15              15                    0                 0

n128, alpha=2            43              31                   12                 0
n128, alpha=9/4          31              31                    0                 0
n128, alpha=5/2          31              31                    0                 0
n128, alpha=3            31              31                    0                 0
```

## Interpretation

The first campaign trade size has no observed primitive residue after
fingerprinting:

```text
h=4 active pairs = persistent mu_4 fibers + one boundary antipodal quotient lift.
```

This does not prove the uniform `h=4` theorem.  It does sharpen the proof
target: a future `h=4` classification can aim to show that every top-three
four-trade is either a full `mu_4` fiber trade or a lower-rank antipodal
quotient lift, both already paid by the cyclic pullback ledger.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x20_h4_cyclic_fingerprint.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x20_h4_cyclic_fingerprint.py --write-certificate
```

Current replay: **70 PASS, 0 FAIL**.
