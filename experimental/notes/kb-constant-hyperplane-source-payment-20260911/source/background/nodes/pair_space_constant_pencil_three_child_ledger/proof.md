# Maximality Fixes The Exceptional Scalar Carrier

Apply an invertible constant change of the two pair components to put
u=(1,0). The joint zero condition, generic fullness, actual weights and
all shared-carrier dimensions are unchanged. This is a coordinate change
for the proof, not a reassignment of any original slope labels.

Distinct constant directions have zero intersection in W. Hence there
cannot be two three-dimensional constant-direction subspaces in W5.
The absence of a four-dimensional one makes S the entire constant pencil
of its direction.

At a regular anchor, W_x has dimension3 and V_x has dimension3.
If evaluation on T is nonzero, S intersect W_x has dimension2. A
function-field-rank-one W_x would have the same constant direction as
that plane. Maximality would then give W_x=S, contradicting nonzero
evaluation on S. Thus W_x has rank2 and contains the constant plane.

If evaluation on T is zero, S subset W_x, so equal dimensions give W_x=S.
Its scalar carrier is the SAME T at every such anchor. Dividing by the
chosen anchor and then the full gcd gives primitive degree E. Prior
anchor/gcd divisions affect both scalar directions and shared coordinates,
not the original affine weights.

Write T=G*T0, gcd(T0)=1. Then deg G+E=max degree(T)<=D.
Every exceptional finite coordinate is a root of G, so their number
is at most deg G<=D-E. Repeated roots reduce the distinct count.
Any degree difference D-max degree(T) is slack at infinity, never extra
finite coordinates. This proof is valid in every characteristic.

## Weighted Incidence

The regular-anchor supplier has excluded count b<=D, including zero
evaluations. Count good agreements with the original fixed weights:

    (A-b)*Omega <= sum_good Omega_x
               <= (N-b)*C+(D-E)*max(U(E)-C,0).

The ratio on the right increases with b<A because N>=A and all
costs are nonnegative. Replacing b by D proves the stated bound.
The exceptional root set may overlap the excluded set; charging the
full root bound remains conservative. No actual agreeing family is
assumed to span its enclosure.

## Contrast With A Full Constant Four-Pencil

If W contains a constant4 subspace, put that direction at (1,0).
Then W=(V,0)+span((0,b)) for a nonzero b in V. Every regular anchor
has b(x)!=0, since otherwise joint evaluation would have rank at most1.
Consequently W_x=(V_x,0): EVERY regular child is whole constant3.
The three-pencil root-exception argument does not apply to this case.
