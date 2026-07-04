# X53: h=4 centered line-bound gap

- **DAG node:** `x53_h4_centered_line_bound_gap`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved comparison / route obstruction.
- **Verifier:** `experimental/scripts/verify_x53_h4_centered_line_bound_gap.py`.
- **Certificate:**
  `experimental/data/certificates/x53-h4-centered-line-bound-gap/x53_h4_centered_line_bound_gap.json`.

## Statement

The existing h=2 subgroup-point input controls a fixed additive line at
exponent `2/3`.  In the notation of X48-X52, it gives the centered shell
maximum bounds

```text
M <= 6 n^(2/3)       general finite-field CZ/MV line bound,
M <= 2 n^(2/3)       prime-field Garcia-Voloch variant recorded in pte_h2_rung.
```

X50 closes the centered h=4 branch only under

```text
M <= T(n) ~ (48n)^(1/3).
```

Therefore the standard fixed-line input is one full `n^(1/3)` too weak for the
centered h=4 energy budget.  Exact arithmetic shows even the optimistic
prime-field constant fails from `n=16` onward.

## Proof

X50 defines `T(n)` as the largest integer satisfying

```text
(T-1)(T-2)(T-3)(n-2) <= 48 n^2.
```

Substituting a line-bound shell estimate

```text
M <= C n^(2/3)
```

can imply X50 only if

```text
C n^(2/3) <= T(n).
```

The verifier checks this without floating point by cubing:

```text
C^3 n^2 <= T(n)^3.
```

For `C=6` and `C=2`, this inequality fails for every recorded `n >= 16`,
including the official-scale row `n=2^41`.

Equivalently, inserting `M <= C n^(2/3)` directly into the X49 max-shell bound
gives

```text
R_centered <= (C^3 n^2 / 48) * n(n-2),
```

which is of order `n^4`, not `n^3`.

## Threshold Table

```text
n        T(n)    gap bits for 6n^(2/3)    gap bits for 2n^(2/3)
16       11      1.792                    0.207
32       13      2.218                    0.633
64       16      2.585                    1.000
128      20      2.930                    1.345
256      25      3.274                    1.689
512      31      3.631                    2.046
1024     38      4.004                    2.419
2^20     371     7.383                    5.798
2^41     47261   14.390                   12.805
```

Here "gap bits" means

```text
log2(C n^(2/3) / T(n)).
```

## Consequence

The centered h=4 branch cannot be closed by simply importing the h=2
fixed-line subgroup-point bound.  The remaining shifted-subgroup theorem must
use more structure, such as:

- dyadic / characteristic-zero rigidity plus sparse norm-gate exclusion;
- a fourth-moment or distribution theorem for the quotient-shell histogram;
- a genuinely stronger shifted-subgroup intersection bound at exponent
  `<= 1/3`.

This explains why X51 sees `M <= 6` in complete boundary windows while the
available general line theorem only proves `M = O(n^(2/3))`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x53_h4_centered_line_bound_gap.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x53_h4_centered_line_bound_gap.py --write-certificate
```
