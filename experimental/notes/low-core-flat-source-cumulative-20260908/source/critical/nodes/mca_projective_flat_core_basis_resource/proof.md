# Proof by core bases outside occupied subspaces

## 1. Identify usable core evaluations

Fix one chosen support S, its minimizing b in V and raw mismatch r.
The polynomial pair (h_gamma-gamma*b,b) matches (u,v) on the in-support
core H of size m-r. If ell_x=0 at a point of H, then b(x)=0 and the
pair's first value is h_*(x). Such a point is a universally satisfied
zero incidence normal. At most g points of H have this property.

Consequently H contains at least m-r-g nonzero evaluation vectors.
After choosing j independent evaluations, their span is a j-dimensional
subspace containing evaluations from at most j*h original nonzero
coordinates. Any evaluation outside that span extends the independent
set. For j=0 there are no nonzero evaluations in the zero subspace.
Thus the number of ORDERED evaluation bases from H is at least

    prod_(j=0)^(s-1)(m-r-g-j*h),                       (1)

whenever the last factor is positive. Repeated points in one projective
fiber are not independent choices. No coordinate is removed from S.

To check the sufficient arc condition, a j-dimensional subspace can meet
at most j projective classes: j+1 classes there would be dependent, and
j+1<=s. Each class contributes at most h coordinates. Full arc independence
is sufficient but not necessary for this weaker occupancy bound.

## 2. Insert one actual defect

The incidence normals on H lie in the hyperplane annihilated by (1,b),
where b is written in the fixed carrier basis. Projection onto the V
coordinates identifies that hyperplane with the s-dimensional dual
carrier, so every basis in (1) gives an incidence-hyperplane basis.

Each of the r actual defect coordinates lies outside that hyperplane,
since v(x)!=b(x). Choose one and insert it at any of the s+1 ordered
positions. This produces beta(r) independent ordered (s+1)-tuples.

There is no multiplicity loss: the tuple has exactly one point outside
THIS record's H, which identifies both the inserted point and its
position; the remaining ordered basis is recovered uniquely. If the
product's positivity condition fails, use the valid bound zero instead.

## 3. The SAME global budget and all HIGH records

An independent incidence tuple determines at most one parameter vector
(gamma,lambda_1,...,lambda_s) solving the selected scalar agreement
equations. The affine offset h_* and received pair are fixed.
Tuples belonging to distinct selected labels are therefore disjoint.
Every independent tuple avoids the z zero normals, so at most
(n-z)_falling_(s+1) tuples are available in total.

The required completed-basis supplier already gives
(m-g)*P*w_s(r;g) tuples on this SAME record. Those two within-record
constructions need not be disjoint. Their MAXIMUM is bounded by the
actual number of independent tuples on the record. Summing proves (FLAT).
Adding the two counts would be unjustified.

For positive real r<=T the logarithmic derivative of beta is at least

    1/r - s/(m-r-g-(s-1)h)>0,

because (s+1)r<m-g-(s-1)h. All factors are positive. Thus every LOW
record has at least beta(1) tuples. Every HIGH record has at least
(m-g)*P*L tuples by its original completed weight. Assign the smaller
of those two lower bounds to every record and divide the ONE global
budget. This proves (MIN). Equivalently the count is the maximum of
the two corresponding resource quotients, not their sum.

This proof does not merge projective fibers, descend the receiver, change
the field, puncture defects, or assume an algebraic pair-curve cover.
