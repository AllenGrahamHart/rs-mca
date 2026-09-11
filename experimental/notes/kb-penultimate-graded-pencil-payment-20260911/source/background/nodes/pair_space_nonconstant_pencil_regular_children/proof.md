# Product Growth And The Exclusion Of Whole Rank-One Children

Write a function-field-rank-one subspace with nonconstant direction as
S=T*(P,Q), where P,Q are a primitive coprime polynomial pair. Every
scalar multiplier lies in F[X]: a Bezout identity for P,Q recovers it
as an F[X]-combination of the two polynomial components.

Multiplication by P and Q is injective. For nonzero finite-dimensional T,

    dim(P*T+Q*T)>=dim T+1.

Otherwise P*T=Q*T and multiplication by Q/P preserves T. A nonzero
polynomial over F annihilates this finite-dimensional operator, making
Q/P algebraic over F, impossible for a nonconstant element of F(X).
This also proves the bound dim T<=s-1. When equality holds,
V=P*T+Q*T, and polynomial coprimality gives gcd(V)=gcd(T).

At a regular anchor the evaluation of V is nonzero. For maximal T this
implies the evaluation of T is nonzero; since P,Q do not vanish together,
the evaluation of S has rank one. Its kernel S_x therefore has
dimension s-2. The same product-growth bound now gives

    V_x=P*T_x+Q*T_x, dim V_x=s-1.

This identity proves the maximal-pencil property for the next carrier.
It does not require the original carrier to be full-gcd1. Dividing the
anchor locator, or a full common factor G of V_x, divides every scalar
in T_x, because gcd(P,Q)=1. The direction P/Q stays nonconstant and
the dimensions are unchanged.

Now take s4,dim W5 and any nonconstant pencil plane S. Its evaluation
has rank at most one, so dim(S intersect W_x)>=1. If the three-dimensional
regular child W_x had function-field rank one, its rational direction
would equal the nonconstant direction of S. The full subspace
W intersect F(X)*(P,Q) would then have dimension at least3, and product
growth bounds it by3. Hence it equals W_x and its component span is V.
But W_x vanishes at x, forcing all of V to vanish at x, contrary to
regularity. Thus EVERY regular child has function-field rank two.

This argument uses a plane, not a single nonconstant pair direction.
The constant-direction analogue is false; controls.md exhibits a regular
whole constant child. The quadric and actual degree conclusions are
proved in quadric_projection.md.
