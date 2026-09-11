# Count Projected Polynomials, Then Original Owners

The original same-pair owner lemma gives disjoint selected defect sets
for distinct finite labels assigned to one pair. Indeed, at a defect
(u-a,v-b) is nonzero, and scalar agreement determines a unique gamma.
Thus one pair's original raw weight is at most n-|H_f|<=n-A.

## Singleton Fibres

Every represented projected polynomial q agrees with the projected
receiver on H_f for any pair in its fibre, hence on at least A points.
The total number of occupied projections is at most Q(n-A).
Consequently all singleton fibres have total raw weight at most
(n-A)*Q(n-A). Including rich projections in this count is harmless.
This is a count of projected polynomials, not arbitrary formal hull points.

## Two Pairs Force A Larger Union

In one fibre, two distinct pairs differ by delta*h for a nonzero
polynomial h of degree<K. Delta is a nonzero constant vector.
At every coordinate shared by their complete joint cores, h vanishes.
Their core intersection has at most K-1 points. Hence

    |C_q| >= |H_f union H_f'| >= 2*A-(K-1),
    e_q <= n-2*A+K-1 = E.

This uses actual represented pairs. A formal affine dimension alone does
not assert that two actual pairs occupy the fibre.

## Scalar Count Within A Rich Fibre

Choose one actual base pair f_q. Every pair in that fibre is uniquely
f_q+delta*h, with h in an affine scalar space of dimension at most s.
On C_q the received pair has the same constant projection as f_q.
Using a nonzero component of delta defines a scalar receiver there.
Joint agreement with f_q+delta*h is exactly scalar agreement with h.
Every actual parameter therefore has at least A scalar agreements.

If l<=e_q<=u, the actual scalar domain has n-e_q<=n-l points.
Pad it to n-l distinct original field points and assign arbitrary received
values at added points. The original parameters retain their A agreements.
The uniform ordinary LIST cap P(l) bounds the actual number of pairs.
Only a scalar list is counted; the original source and labels are unchanged.

For every fibre in this bin, q agrees with the projected receiver on
C_q, which has at least n-u points. There are at most Q(u) distinct
such fibres. The number of rich pairs in this bin is thus at most P(l)*Q(u).
Using the same projected tail cap in several bins is deliberate overpayment,
not a disjointness assertion or a separate conserved resource for each bin.

## Original Weight Outside And Inside Its OWN Union

For a fixed pair in a rich fibre, its selected defects outside C_q are
disjoint over its assigned labels. Their total is at most e_q<=u.
This prices all outside weight in that bin by u*P(l)*Q(u).

For an inside defect x of a pair in its OWN C_q, compatibility forces

    (u(x)-a(x),v(x)-b(x)) = c*delta, c!=0.

Scalar agreement at that defect requires lambda1-gamma*lambda0=0.
If lambda0=0 this has no finite solution. Otherwise gamma=lambda1/lambda0
is ONE constant label for ALL fibres. That label has only one original
owner/support and its raw value is at most t. Therefore inside weight
across all rich fibres is at most t, even when their unions overlap.

Adding singleton weight and these rich inside/outside weights proves CENSUS.
No codimension-one quotient, anchor history, fibre disjointness or shared
packing budget enters this argument. The generic projection dimension
may exceed one.
