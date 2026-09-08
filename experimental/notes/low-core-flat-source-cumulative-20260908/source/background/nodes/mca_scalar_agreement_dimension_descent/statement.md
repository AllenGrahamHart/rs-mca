# Scalar-agreement dimension descent

The [two-anchor companion](two_anchor_fiber_bound.md), proved
2026-09-07, additionally couples the projective evaluation fibers of
a zero-free direction space. With a uniform second-child cap U it gives
|Z|<=floor(U*max(F_bal,F_spike)) at the formulas printed there.
It retains both branches and the jointly realizable fiber-size condition.

Status: PROVED. Work over any finite field on n distinct evaluation
points, with 1<=s<=K<m=K+d<=n, d>=1, R=n-K. Fix an
s-dimensional F-linear polynomial space C' of degree <K and an affine translate
h_*+C'. Select one explanation h_gamma in that translate and one exact
size-m SAME-support pair-noncontained scalar agreement set S_gamma for
each distinct finite slope gamma in Z.

Let T be the common evaluation zero set of C', z=|T|, and

```text
g = #{x in T: r_1(x)=0 and r_0(x)=h_*(x)},
tau = #{x in T: r_1(x)!=0}.
```

Then z<=K-s, g+tau<=z. At each x outside T, the selected records
with x in S_gamma descend, with their original slopes, to the row
(n-1,K-1,m-1), in explanation dimension at most s-1. Their EXACT
supports are S_gamma minus {x} and remain pair-noncontained in the
full shortened code. No core or minimizing direction is required.

If U_x bounds that child family at x, then

```text
(m-g)|Z| <= sum_(x outside T) U_x + tau.
```

In particular, if an integer U>=1 uniformly bounds all such children,

```text
|Z| <= floor(((n-z)U+tau)/(m-g))
     <= floor((R+s)U/(d+s)).
```

The rank-zero base, meaning all selected explanations are the same
polynomial, has the exact uniform cap n-m+1=R-d+1. This includes
the zero code when it occurs as a child. The theorem does not claim
that arbitrary sources have bounded explanation dimension or that a
post-near condition survives shortening.
