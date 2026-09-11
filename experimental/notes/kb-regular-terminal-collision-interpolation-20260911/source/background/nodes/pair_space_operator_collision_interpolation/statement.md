# Actual Collision Fibres Supply A Multiplicity Interpolant

Status: PROVED locally; independent mathematical review remains due.

Let U be a dimension3 F-polynomial carrier of degree<=D with no common
evaluation zero on an n-point domain. Let T:U->U have at most one-dimensional
F-eigenspaces. For exactly M actual pairs f_*+(y,T(y)), each complete joint
core has size>=A. Remove the F-eigenpolynomial root set E as in the required
incidence theorem, with an aggregate core-incidence bound B on E.

On Omega outside E, group coordinates by their nonzero projective evaluation
p=[ev_x|U]. Let r_p be the maximum number of these M pairs jointly agreeing
at ONE actual coordinate in that fibre. Retain p only when r_p>=2 and put
w_p=r_p-1, C=sum_p binom(r_p,2). Then

    C<=binom(M,2).                                      (PAIR OWNERSHIP)

Let H_U(ell) be the dimension over F of the space spanned by all degree-ell
products of a basis of U. If H_U(ell)>C, then

    sum_(x in Omega) max(c_x-1,0)<=D*ell,
    M*A<=B+n+D*ell.                                    (INCIDENCE)

Here c_x counts ACTUAL agreeing pairs. In particular H_U(ell)>binom(M,2)
and M*A>B+n+D*ell rule out an M-element actual subset. A family with fewer
pairs is not artificially padded with formal points.

If eta is the degree of the primitive homogeneous equation of the plane
image [u0:u1:u2], then eta>=2 and

    H_U(ell)=binom(ell+2,2)-binom(ell-eta+2,2),

where the second term is zero when ell<eta. Thus the interpolation rank
is explicit. This eta is NOT the degree or maximum fibre size of the
parameter map, nor the original polynomial degree D.

All singularities, ramification and finite repeated fibres are retained by
pullback multiplicities. No generic-fibre replacement, full-hull source
census, characteristic-dependent differentiation or MCA row closure is used.
