# Proof By Refinement Of Fibers And One Jensen Step

## 1. Split The Actual Fiber Moment

Every original projective fiber is either wholly inside A or wholly outside:
membership of its evaluation line in span(A) does not depend on its coordinate.
Inside fibers have size<=h, so their square sum is at most a*h.

The polynomial annihilator of span(A) has rank ell. Division by the FULL
locator P_A gives a degree<k=K-a polynomial space on the N-a outside
coordinates, with actual rank ell and nonzero evaluations. Root capacity
gives k>=ell. Completeness is necessary for the nonzero assertion.

Its projective fibers COARSEN the original outside fibers. Merging
nonnegative fiber sizes increases their square sum. The full-fiber
contraction supplier bounds that quotient moment by Q(N-a,k,ell) when
ell>=2; for ell=1 it is exactly (N-a)^2. Independently the ORIGINAL
outside fibers still have size<=h, giving the other bound (N-a)*h.
This proves SPLIT. The argument does not assume quotient fibers have
size<=h; only original fibers obey that cap.

For original fiber sizes c_i, S2=N+sum_i c_i*(c_i-1), proving the
collision-cap alternative. Restriction of a larger SAME-carrier domain
can only decrease the ordered equal-fiber pair count.

## 2. Retain The Original Descendant Profile

The required rank-profile theorem gives a positive increasing convex
polynomial F_(s-1)(D,x) for EVERY first full-fiber contraction of this
source. Its coefficients are those calibrated for the ORIGINAL rank s
and degree box, not a freshly optimized profile on a fictional child.

Exact contraction and Jensen therefore give

    B_s >= sum_i c_i*F_(s-1)(D,K-c_i)
        >= N*F_(s-1)(D,K-S2/N)
        >= N*F_(s-1)(D,K-q).

The actual child degrees K-c_i are integers >=s-1. Only their weighted
mean and its lower relaxation are real. The product is increasing and
convex on x>=1, which is the explicit guard on K-q. This proves ROOT.
There is no need for the old uniform root coefficient mu_s if a smaller
valid root moment is known; every remaining descendant coefficient stays.

## 3. Whole Boxes

Q(D+k,k,ell) is increasing for k>=ell: both of its branches are
increasing, and the ell=1 expression is increasing too. The inside bound
a*h is at most a1*h1; the outside point count is at most D+k1. Divide
their combined upper bound by N>=N0. The old profile gives
S2/N<=mu_s*(K-1)<=mu_s*(K1-1); the simple fiber bound gives <=h1.
A uniform collision cap gives <=1+C/N0. Every entry in q0 is thus a
valid upper bound, so their minimum remains valid.

Finally K-q0>=K0-q0, N>=N0, and the same frozen product is positive
and increasing. This proves the box statement. If the relaxed argument
is below one, use the trivial zero bound rather than evaluating an
unproved extension of the product.

The quotient moment and hereditary convex product are credited suppliers.
The new step is feeding the complete-flat split of the ORIGINAL root
moment into that product, retaining rather than replacing the old profile.
