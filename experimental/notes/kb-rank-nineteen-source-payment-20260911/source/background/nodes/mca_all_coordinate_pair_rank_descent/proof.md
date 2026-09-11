# Retain Each Coordinate At Its Actual Rank

## Unrestricted Sections

Primitive V has no common finite root, so V_x has dimension s-1 at every
coordinate. A joint-rank-q section is an affine translate of W_x of
dimension r-q, contained in V_x squared. Thus its codimension is c+q-2.
A negative codimension is impossible.

The shared-carrier anchor supplier bounds the span of rank-at-most-one
evaluation functionals by c. The annihilator inside V therefore has
dimension at least s-c and vanishes on every such coordinate. Polynomial
degree D gives their cardinality at most D+1-(s-c)=kappa+c.

Let H be the sum of the component images of W. Then r<=2 dim H, so
dim H>=s-floor(c/2). At a rank-zero coordinate every member of H
vanishes. Hence their number is at most D+1-dim H<=kappa+floor(c/2).
This includes proper component spans inside the declared carrier.
For c0, W=V squared and every coordinate has rank two.

Every section's component differences lie in V_x, so its full shared gcd
contains X-x. Division preserves enclosure dimension and gives degree
at most D-1. Consequently the new kappa is at most the old kappa.
The original field, anchor count, weights and complete cores are retained.
If the full new shared gcd has degree e and z remaining domain roots,
then D-D_child>=e>=z. The new unused slack is
v_child=v+D-D_child-z>=0. Deleting those z coordinates loses at most z
joint agreements, giving exactly the child's printed N,A corridor.

Every pair has at least A remaining joint agreements. Sum its same
nonnegative weight over all of them. Raise the rank-one price to
max(C2,C1), and the rank-zero price to max(C2,C1,C0). The rank-zero
set is a subset of the rank-at-most-one set; charging these two nested
increments gives exactly (U), without overlapping source resources.

## Full Generic Projection

Let K_z be the kernel of pi_z on W over F(z); its dimension is r-s=s-c.
Its b-component is injective, because a=-z*b on this kernel.
The common finite zero set of K_z has size at most
D+1-(s-c)=kappa+c, by the same polynomial dimension count over F(z).

Outside that set, the regular-projection supplier proves joint rank two
and full generic projection of the child. No original slope is treated
as the transcendental symbol z or changed by this argument.

Generic fullness also makes the sum of the component images equal V,
so joint rank zero is impossible. At a rank-one coordinate, the evaluated
image of W is a fixed nonzero F-line in F squared. The functional
(a,b)->a+z*b is nonzero on that line over F(z). Thus
W_x is exactly the kernel of evaluation after pi_z. Surjectivity of pi_z
then gives pi_z(W_x)=V_x: the rank-one child is full generic.

At a joint-rank-two point where K_z evaluates to zero, all of K_z stays
inside W_x. Its image has dimension(r-2)-(r-s)=s-2, not s-1.
The child is NOT regular. It must be charged by an unrestricted bound.

A codimension-zero pair space is the full square. A codimension-one pair
space also has full generic projection: its one-dimensional annihilator
has a fixed F-generator(A,B), which cannot be proportional to
(ell(z),z*ell(z)) with ell nonzero, since that would force B=z*A.
Thus a rank-two nonregular child cannot occur at c0 or c1.

All exceptional coordinates are in the same K_z zero set. Charge the
largest of the possible child-price excesses there, once. This proves (G).
