# Interpret Vanishing At An Actual Anchor As Inner Projection

Homogenize the full-gcd1 carrier to its ACTUAL maximum degree D. There
are no common affine zeros, and a maximum-degree section excludes a base
point at infinity. Thus V gives a basepoint-free P1 morphism, whose pullback
of O_C(1) has degree D. The normalization factor is finite flat of degree nu,
so D=nu*eta, by the same divisor-length calculation as the required supplier.
This argument does not depend on the target being a plane.

On the normalization, the hyperplane line bundle has degree eta and at
least s independent sections. A line bundle of degree eta on a smooth
proper integral curve has at most eta+1 independent sections: a nonzero
section identifies it with an effective divisor, and adding its geometric
points one at a time increases h0 by at most1. Hence eta>=s-1.

The regular anchor theorem gives V_x=ker(ell_x), of dimension s-1. Since
ell_x is nonzero, these are precisely the hyperplanes through p=[ell_x].
Dividing their full fixed divisor does not change any ratio of sections.
Their function field is consequently the field of the actual inner image,
a subfield of F(C). The tower law gives nu_child=nu*mu.

On the normalization of C let B_p be the fixed divisor of those hyperplane
sections, of degree m. It is supported on the branches above p, and each
branch has positive order, so m>=b(p). Remove B_p. The resulting free linear
system is the inner projection, and its line bundle has degree eta-m.
Finite-map degree multiplication gives eta-m=mu*eta_child.

Pulling B_p back to P1 has degree nu*m, including ramification and points
at infinity. Removal of this FULL homogeneous factor leaves child degree
D-nu*m. Dehomogenizing the basepoint-free child gives exactly its actual
polynomial maximum degree; it does not silently saturate the original bound.
This proves all three identities and their telescope along the actual path.

For s_0=11 and D_0<=J-1, nu_0<=floor((J-1)/10). Each mu_j is a positive
integer. If all are1, the final normalization degree is nu_0; its strict
increase therefore forces at least one genuine nonbirational anchor.

No auxiliary geometric projection selects or reassigns an original label.
The use of geometric divisors is only for these degree identities; actual
domain roots need not exhaust them and original raw weights are unchanged.
