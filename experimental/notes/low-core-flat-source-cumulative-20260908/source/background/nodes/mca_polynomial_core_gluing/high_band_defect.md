# High-band gluing has an exact zero-or-two dichotomy

Hand proof, 2026-09-06. This is a continuation of the gluing theorem,
not a population bound or an import of the upstream finite-row payment.

## Hypotheses and assertion

Let D be n distinct points of a field F, let k>=1, h>=2 and A=k+h,
and suppose the received functions u,v satisfy the ALL-projective ceiling

```text
agr_D(alpha*u+beta*v,c) <= A
for every [alpha:beta] in P^1(F) and every deg(c)<k.       (G)
```

Take a family of DISTINCT polynomial pairs P=(f_P,g_P), of degrees <k,
whose COMPLETE joint cores Z_P have sizes k+d_P, with 1<=d_P<=h-1.
On their union U use the gluing quotient and received-pair defect c_glue
defined in proof.md. The subscript distinguishes this dimension from a
scalar codeword. The empty family has defect zero by convention.

1. If two pairs have d_P+d_Q>=h, their two-core received-pair defect is
   exactly two. The defect of every larger family containing them is two.
2. Their core intersection has size at most k-2. Their two polynomial
   differences f_Q-f_P and g_Q-g_P are linearly independent over F.
3. If every depth is at least ceil(h/2), then

```text
c_glue=0  iff the family has at most one pair;
c_glue=2  iff the family has at least two pairs.
c_glue=1  never occurs.                                (DICH)
```

More generally, a family of defect at most one has d_P+d_Q<=h-1 for
each pair of distinct members. In particular, a cascade core cannot share
such a family with ANY other positive-depth band core.

These conclusions do not require a window-rank assumption, smoothness,
strip survival or selected liveness. They therefore apply to the actual
filtered families without removing any of those filters.

## 1. A nontrivial scalar kernel cannot cover more than A points

If c_glue<=1, rank-nullity gives a nonzero (alpha,beta) and a polynomial
c_0 of degree <k agreeing with alpha*u+beta*v on U. Hypothesis (G) gives
|U|<=A. This uses the projective ceiling, including infinity; a finite-chart
ceiling alone does not justify the step.

Two distinct polynomial pairs can have at most k-1 common core points:
at least one of their component differences is a nonzero polynomial of
degree <k, vanishing at every common point. Therefore

```text
|Z_P union Z_Q| >= (k+d_P)+(k+d_Q)-(k-1)
                = k+d_P+d_Q+1.
```

If d_P+d_Q>=h this exceeds A. No nonzero scalar combination can be
globally polynomial on that union, so its defect is two. Such a combination
cannot become polynomial on a larger union either. This proves assertion 1
and the general depth-sum restriction.

One core has L=C_k(U), so its quotient is zero. The empty case is separate.
Any two depths at least ceil(h/2) have sum at least h, proving (DICH).
Defect zero also permits only one distinct pair in ANY family of cores of
size at least k: global component polynomials are identified with every
local pair by interpolation on its core.

## 2. Exact two-core quotient and the sharper intersection bound

Write I=Z_P intersection Z_Q and j=|I|. Both cores have at least k
points, so local degree-<k representatives are unique. A local section is
a pair of polynomials (a,b) with a|I=b|I. The map

```text
L/C_k(U) -> {t in F[X]: deg(t)<k and t|I=0},
[(a,b)] -> b-a                                           (Q2)
```

is an isomorphism. Its kernel is exactly a common global polynomial;
surjectivity follows by using (0,t). Since j<=k-1, its dimension is k-j.
The received classes map to f_Q-f_P and g_Q-g_P. Their span has dimension
two by assertion 1, so these polynomials are independent and k-j>=2.
This proves assertion 2. If k=1, the dimension contradiction says that no
such pair of high-depth cores exists; it is not a negative-size convention.

There is also a direct check at the excluded boundary j=k-1: both
differences are constant multiples of the same degree-(k-1) root
polynomial. A nonzero scalar combination kills both differences, hence
glues the corresponding scalar explanation on the two cores. Their union
exceeds A, contradicting (G).

## 3. Selected-slope payment and the exact critical route boundary

For a pair at depth d<h, each selected exact-A scalar support containing
its complete core uses h-d outside points. The selected scalar polynomial
equals alpha*f_P+beta*g_P by uniqueness on at least k core points.
Outside the core its error
vector is nonzero and has exactly one projective annihilator. Hence the
outside portions belonging to different slopes are disjoint, and

```text
L_P <= floor((n-k-d)/(h-d)).                            (CAP)
```

Consequently a high-depth family with c_glue<=1 has at most one pair and
its selected slope union has size at most n. At any fixed depth its pair
count is at most one, satisfying 25*N_d<=17*n^2 whenever n>=2.
For a single cascade pair the sharper slope cap is n-A+1.

Thus on the prize rows the full-rank SL-2 target is equivalent to its
restriction to c_glue=2: the omitted zero-defect branch is already paid
and the one-defect branch is empty. But (DICH) also says that defect two
here means exactly "at least two pairs". It is NOT a smaller structural
classification of the potentially large family. A cover by defect-at-most-
one containers uses at least as many nonempty containers as high-band pairs.
The gluing trichotomy alone therefore supplies no aggregate count.

This does not identify c_glue with rank J_d, the dimension of the whole
gluing quotient, affine explanation rank, or the degree of a window syzygy.
In particular it does not delete the already useful deficient-window
branch: that branch may have received-pair gluing defect two.

## 4. The depth-sum boundary cannot be silently relaxed

In F_7 take D={0,1,2,3,4,5}, k=2, h=3 and A=5. Put

```text
(u,v)=(0,0) at 0,1,2;
(u,v)=(0,x) at 3,4;
(u,v)=(1,1) at 5.
```

The pairs (0,0) and (0,X) have complete cores {0,1,2} and {0,3,4}.
Both have depth one, their depth sum is h-1, and their union has size A.
On the union, u is globally zero and v is not globally affine, so the
received-pair defect is one. To verify (G), agreement on all six points
would force the scalar polynomial to be zero from 0,1,2, then beta=0
from 3, and finally alpha=0 from 5. This excludes every nonzero projective
combination. Since n=6, the ceiling is indeed five.

This is a sharpness control for the general algebraic depth-sum theorem.
It is not a smooth prize-row fixture, a selected productive family, or
a counterexample to a critical population bound.
