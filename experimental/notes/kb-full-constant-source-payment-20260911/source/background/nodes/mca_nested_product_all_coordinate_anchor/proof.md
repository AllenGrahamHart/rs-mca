# Include Rank-One Evaluations Instead Of Discarding Them

## Geometry

The gcd1 assumption on V makes evaluation on V nonzero at every finite
coordinate. Evaluation on the nested product W has rank two exactly when
evaluation on B is nonzero. A nonempty actual affine agreement section
is a translate of the product of the two evaluation kernels.
The second kernel is B_x of dimension b-1 in the first case, and all of
B in the second. Because B subset V, both lie inside V_x, of dimension
s-1. These are enclosures only; no actual family has to span them.

If b>0, write B=G*B0 with primitive scalar degree E. Dimension b gives
E>=b-1, while deg G+E<=D. The distinct finite common roots therefore
number at most D-b+1. If c=0 then B=V has gcd1, so there are none.

All component differences in V_x are divisible by X-x. Divide by the
FULL shared gcd, including this anchor factor, and remove its domain
roots only as a change of coordinates. The new shared degree is at
most D-1; its dimension is s-1. Thus
D_child-((s-1)-1)<=D-(s-1). The same nonnegative original unused degree
calculation applies: actual gcd roots removed never exceed its degree.
The branch codimension changes but the anchor count a still increases
by exactly one. No original degree, raw label or owner is reset.

For an original full constant subspace of W, choose its direction as
the first F-basis vector. Subtract that full first component from every
remaining pair direction. This gives precisely the nested product form;
B is contained in the original shared carrier. No extension of F is used.

## Weighted Incidence

Let z be the number of remaining B-root coordinates. Every pair still
has at least A joint agreements, and its SAME nonnegative owner weight
is charged at each of them. Therefore

    A*Omega <= sum_x Omega_x
             <= (N-z)*C+z*F
             <= N*C+(D-b+1)*max(F-C,0).

The estimate uses all remaining coordinates, including the rank-one
ones. Empty sections cost zero. For c=0 there are no rank-one sections.

Substitute D=s-1+kappa. For fixed kappa the right side is a ratio
of affine functions of v>=0, with limit C at infinity; its maximum
is bounded by the value at v0 or that limit. At v0 it is a ratio
of affine functions of kappa with positive denominator, hence monotone
or constant. The two endpoints of[lo,hi] suffice. This proves the
printed three-value envelope, even when F<C.

For each shared stage, prices for all smaller degree bands must be
maximized before being used for a child. This retains any extra degree
drop caused by full gcds. The codimension-zero branch uses only C.

## Whole-Constant Terminal And Original Resource

For b0, all actual pairs lie in one original constant-direction pencil.
Its complete-core union has original complement e. The preferred finite
slope, if it exists, costs at most t globally. All other original raw
defects lie outside that union, with at most e disjoint selected defects
per represented pair. Hence an actual scalar LIST cap L gives t+e*L.

Let the full divided scalar carrier have primitive degree D. Let z_C count
the additional full-gcd roots in this terminal's ORIGINAL core union,
outside the a anchors; it is bounded by the remaining gcd degree.
Then v_C=J-a-1-D-z_C>=0. The scalar length is
R-e+D+1+v_C and agreement is at least d+D+1-t+v_C.
Delete any v_C additional coordinates from that scalar instance.
This loses at most v_C agreements and leaves length at least
D+1, hence an injective restriction on degree-at-most-D polynomials.
The same-field uniform-in-degree LIST parameters are

    (r,w,Kmax,dimension)=(R-e,d-t,D+1,c).

An upper degree band endpoint gives Kmax=c+hi. For e in[u,v_e], padding
to r=R-u and using weight t+v_e*L gives a certified whole box bound.
All padding must fit the original field; the finite consumer checks it.

For s0 the enclosure contains at most one original pair. Same-pair
ownership bounds its raw weight by R-d+t. This base case is distinct
from a positive-dimensional scalar pencil. These costs and the generic
incidence inequality do not themselves claim an all-source row payment.
