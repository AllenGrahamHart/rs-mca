# f_dim2_skeleton proof

Let `P` be a gcd-trivial two-dimensional flat. For each domain point `x`, the
condition that a locator in `P` vanish at `x` is a trace line `L_x` in the
projective plane `P`.

If `L_x = P`, then every member has root `x`, contradicting gcd-triviality.
Thus each trace is a genuine line. If two distinct traces `L_x` and `L_y` are
not equal, they meet in exactly one point of the projective plane. Counting
pairs of roots through members gives

```text
sum_{ell in P cap D_j} binom(mult(ell), 2) <= binom(n, 2)
```

for the twin-free part, where no two domain points have the same trace line.
Every `D_j` member contributes at least `binom(j, 2)` to the left-hand side, so

```text
#(P cap D_j) <= binom(n, 2) / binom(j, 2)
```

on the twin-free stratum.

If `L_x = L_y` for a twin pair `x != y`, then every member through `x` is also
through `y`. The sub-pencil supported on that line has the shared divisor
`(X - x)(X - y)`, so `f_gcd_reduction` moves it into the paid tangent/common-gcd
branch. Accounting for the `T` twin traces gives the stated correction term

```text
(binom(n, 2) + (q + 1) T) / binom(j, 2).
```

Thus dimension two is controlled by the elementary pair count plus the paid
twin reduction.
