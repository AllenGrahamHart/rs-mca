# Preserve Orders As Well As Branches Under The Generic Counting Projection

On a normalization branch above P, let e be the minimum vanishing order
of the affine coordinate differences from P. The pulled-back ideal of
hyperplanes through P has order e. Thus the full fixed-divisor degree
is m_P=sum e over its branches, whereas b_P counts those branches once.

A linear projection with centre different from P does not decrease these
orders: after choosing a target affine chart, its coordinate differences
are linear combinations of the old differences divided by a unit.
If the projection is birational, normalization points are retained, so
each resulting branch contributes at least its old order.

Take any finite set of nonbirational centres P_i. The required branch-budget
theorem supplies a generic smooth q whose inner projection is birational,
whose fibres for all P_i are unramified and disjoint from their base branches,
and whose lines qP_i are distinct. After projection from q, the image of
P_i contains its original branches with total order at least m_i, plus
mu_i-1 other normalization points, each of order at least1.

Continue generic inner projections to P2, preserving these distinct marked
points. The final plane curve has degree q_final=d-(r-2). At each marked
point its multiplicity is at least m_i+mu_i-1.

For completeness, plane multiplicity equals the sum of these branch
orders: intersect with a general line through the point. In the local
equation this length is the lowest total degree; on the normalization
it is the sum of valuations. Passing from the local ring to its finite
normalization preserves this intersection length, since multiplication
by the line on their finite quotient has kernel and cokernel of equal
length. No branch is presumed smooth or transverse.

The all-characteristic plane calculation in plane_multiplicities.md gives

    sum_i binom(m_i+mu_i-1,2)<=binom(d-r+1,2).

The old theorem already proves that nonbirational centres are finite;
equivalently this bound for every finite set proves finiteness again.
The coordinate bound nu*b_i<=nu*m_i follows from finite flat normalization.
The exact source-cost ratio is proved in price_ratio.md.
