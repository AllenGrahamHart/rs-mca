# Nonuniform support-margin resource

Status: PROVED. This is a summed weighted bound, not a prize-row payment.

Let F be a finite field, D a set of n distinct elements, and
`1<=s<=K<m=K+d<=n`, with `d>=1`. Let C' be an s-dimensional subspace of
degree-`<K` polynomials and h_* another degree-`<K` polynomial. Fix arbitrary
received functions r_0,r_1 on D. For each distinct slope gamma in a finite
set Z, select h_gamma in h_*+C' and a size-m set S_gamma on which
`r_0+gamma*r_1=h_gamma`. Require that no degree-`<K` pair explains
`(r_0,r_1)` on that SAME S_gamma.

Define

```text
raw_gamma = min_(b in C') #{x in S_gamma: r_1(x)!=b(x)},
theta_gamma = min(d+1,raw_gamma),
C_s = floor(max(
  n_falling_(s+1)/(m*(d+1)_rising_(s-1)),
  (n-K+s)_falling_(s+1)/(d+1)_rising_s
)).
```

Here falling and rising products have unit steps; a length-zero product is
one. Then

```text
theta_gamma>=1,             sum_(gamma in Z) theta_gamma<=C_s.
```

The dimension is that of the actual chosen subspace C', not a substituted
upper bound. Supports need not be complete agreement sets, nor disjoint
across slopes. There is one record per slope. The theorem uses neither a
post-near restriction nor any computed constants.
