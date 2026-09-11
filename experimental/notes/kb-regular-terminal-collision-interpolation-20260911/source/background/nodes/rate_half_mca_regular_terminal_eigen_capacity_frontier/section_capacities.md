# Prove Hereditary Pair Counts For Lines And Planes

Let g_J be the parent profile's original constant P43 pencil-union gate.
After its paid whole-source alternatives are removed, every actual constant
pencil subfamily has union complement at least g_J+1. This hereditary fact
is proved in the parent's pencil_gates.md, not assumed for a formal hull.

## Eigenvector Lines

An affine line parallel to an F-eigenvector of the primitive T is a
constant-direction pencil of ORIGINAL pairs: its direction is
H_a*G*u*(1-alpha*lambda,lambda). Its nonzero scalar polynomial has degree<J.
At coordinates off its at most J-1 zeros, different pairs cannot jointly
agree with the same receiver. If b of these zeros lie in the actual union,
counting core incidences gives

    M_line <= (n-e_union-b)/(d+J-t-b)
            <= (n-e_union-J+1)/(d+1-t)
            <= (R-g_J)/(d+1-t).

Here the ratio increases with b because the union contains each core,
and d+1-t>0. Thus the actual eigenline capacity is

    q1=floor((R-g_J)/(d+1-t)).

An empty subfamily needs no division. This is a PAIR count, not an owner
weight. It holds for every subset and every primitive degree kappa.

## Arbitrary Affine Planes

Every F-plane of directions in the primitive pair carrier has nonzero
polynomial determinant: otherwise it would be a forbidden rank-one pair
plane. Its degree is at most2*kappa-2. Outside its zeros, joint evaluation
on that affine plane is injective; at most one represented pair agrees.
For M_plane actual pairs and b determinant zeros on the remaining domain,

    M_plane <= (N_v-b)/(A_v-b)
             <= (R-kappa+2+v)/(d-kappa+2-t+v)
             <= (R-kappa+2)/(d-kappa+2-t).

The denominator is positive throughout kappa<=21491. The first ratio
increases with b<=2*kappa-2, and the second decreases with v>=0.
Consequently q2=floor((R-kappa+2)/(d-kappa+2-t)) is hereditary.

The finite certificate checks2*q1<=q2 everywhere. These two capacities
therefore discharge all hypotheses of the generic eigen-root incidence
theorem without requiring the actual family to fill any line or plane.
