# Bounded polynomial points on smooth cubics

Status: PROVED, 2026-09-07. Classical surface inputs are identified in
`audit.md`; the coefficient-family application is proved here.

Let k be an algebraically closed field of characteristic zero or p>3,
and let Q in k(X)[U,V] have total degree three. Suppose its projective
homogenization defines a geometrically smooth plane cubic C over k(X).
For any finite bounds on deg(a),deg(b), every irreducible component of
the REDUCED coefficient locus

    Y_Q = {(a,b) in k[X]^2: Q(a,b)=0}

has dimension at most one. Intersecting with fixed affine polynomial
coefficient subspaces preserves the bound. No coefficient-height bound
on Q, and no common-carrier assumption, is required.

If C has nonconstant j-invariant, every such component has dimension
zero. More generally, this holds whenever the relatively minimal
elliptic surface associated to C has a singular fiber. If the locus
is nonempty, one polynomial point supplies the origin needed for this
surface; no rational flex in the original plane embedding is assumed.

Smoothness is over the FUNCTION FIELD, not smoothness of every
specialized X-fiber. Singular specialized fibers are allowed, and
are useful for the stronger conclusion. Singular generic cubics are
excluded. A constant smooth cubic can have a dimension-one locus.

This is a dimension theorem, not a point-counting theorem or an MCA
source classification. Fixed rational coordinate changes in its proof
are used ONLY for dimension, not to transfer polynomial degree bounds.
