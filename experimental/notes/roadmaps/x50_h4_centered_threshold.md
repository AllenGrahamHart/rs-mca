# X50: h=4 centered threshold

- **DAG node:** `x50_h4_centered_threshold`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved exact threshold consequence of X49.
- **Verifier:** `experimental/scripts/verify_x50_h4_centered_threshold.py`.
- **Certificate:**
  `experimental/data/certificates/x50-h4-centered-threshold/x50_h4_centered_threshold.json`.

## Statement

Let `M` be the maximum quotient-coset shell size from X49:

```text
M = max_C m_C,
```

where

```text
m_C = (1/2) #{ r in H \ {1} : 1+r in C }.
```

X49 proves

```text
R_centered <= (C(M,4)/M) * n(n-2)/2.
```

For `M >= 4`, this bound is at most `n^3` exactly when

```text
(M-1)(M-2)(M-3)(n-2) <= 48 n^2.
```

Thus the centered h=4 branch is inside the rewired terminal `n^3` column
whenever `M <= T(n)`, where `T(n)` is the largest integer satisfying the
displayed inequality.  A simpler sufficient condition is

```text
M^3 <= 48 n.
```

## Proof

For `M < 4`, the centered bound is zero.

For `M >= 4`,

```text
C(M,4)/M = (M-1)(M-2)(M-3)/24.
```

Substituting this into X49 gives

```text
R_centered
  <= ((M-1)(M-2)(M-3)/24) * n(n-2)/2.
```

Therefore `R_centered <= n^3` is equivalent to

```text
(M-1)(M-2)(M-3) n(n-2) <= 48 n^3,
```

and, since `n > 0`, to

```text
(M-1)(M-2)(M-3)(n-2) <= 48 n^2.
```

The cubic factor is increasing for `M >= 4`, so this defines an exact largest
admissible shell size `T(n)`.

For the closed-form sufficient threshold, use

```text
(M-1)(M-2)(M-3) <= M^3.
```

If `M^3 <= 48n`, then

```text
R_centered <= M^3 n(n-2)/48 <= n^2(n-2) <= n^3.
```

## Thresholds

The exact threshold is slightly larger than the simple cube-root sufficient
threshold:

```text
n              T(n)       floor((48n)^(1/3))
16             11         9
32             13         11
64             16         14
128            20         18
256            25         23
1024           38         36
2^20           371        369
2^41           47261      47259
```

## Consequence

After X48-X50, the nonzero-centered affine h=4 branch has been reduced to one
row-local shifted-subgroup concentration target:

```text
max_C #{ r in H \ {1} : 1+r in C } <= 2 T(n).
```

This is a substantially smaller object than h=4 support sorting.  It is a
cyclotomic-number / shifted-subgroup-intersection bound over `F_p^*/H`.

## Replay

The verifier reads the X49 certificate and checks:

- the exact integer threshold boundary for every replay row;
- the replay rows' measured `M` values all satisfy `M <= T(n)`;
- the exact Fraction form of X49's bound crosses `n^3` at `T(n)+1`;
- the simple `M^3 <= 48n` threshold is safe;
- an official-scale `n=2^41` threshold row is included.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x50_h4_centered_threshold.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x50_h4_centered_threshold.py --write-certificate
```
