# Original-Field Product Normal Form

A geometrically integral plane conic in odd characteristic is nonsingular:
a singular ternary quadratic has rank at most2 and factors over the algebraic
closure. A rational point gives a nonzero isotropic vector e. For the polar
form B choose f with B(e,f)=1 and replace f by f-Q(f)*e after fixing the
convention B(x,y)=Q(x+y)-Q(x)-Q(y). This makes Q(f)=0.
The orthogonal complement of span(e,f) is one-dimensional and nondegenerate.
In that basis Q=ab+c*z^2 with c nonzero. Rescaling a coordinate, not taking
a square root, identifies the conic over F with Y0*Y2=Y1^2.

After the corresponding F-basis change of U, u0*u2=u1^2 and the polynomial
gcd remains1. For each irreducible factor, its valuations in u0,u1,u2 obey
v0+v2=2v1 with minimum0. Thus v0,v2 are even and at most one is positive.
It follows that u0=a*P^2,u1=b*PQ,u2=c*Q^2 for nonzero F constants, with
P,Q coprime. Constants do not affect their F-span. Linear independence
excludes constant P/Q. The actual maximum degree is D=2nu.

Homogenize P,Q to degree nu. Coprimality excludes affine basepoints and
the actual maximum degree excludes a common zero at infinity. The map
[P:Q]:P1->P1 has degree nu, including inseparability; every geometric
fibre has length nu. Composing with the conic parametrization proves the
finite fibre bound. This is also the smooth-conic case of the required
branch/genus normalization theorem.

## Height Of An Actual Collision Line

Express y and Ty as binary quadratics in P,Q. If y is not an F-eigenvector,
these quadratics are independent. A joint zero at an actual F-coordinate
gives a common F-linear homogeneous factor L in the parameter variables.
Their homogeneous gcd has degree exactly1; degree2 would make them
proportional. Thus y=L(P,Q)*A(P,Q), Ty=L(P,Q)*B(P,Q), where A,B are
independent linear forms over F. These residual polynomials are coprime:
their common divisor would divide both P and Q by invertibility of A,B.
Their maximum degree is exactly nu for the same reason.

This is the primitive rational pair height. Scalar multiplication cancels
in the pair gcd; an invertible F pair change preserves both the generated
ideal and actual maximum degree. Thus returning through the original
anchor/gcd multiplier and pair chart does not alter the height.

The kernel geometry and rank-one restrictions are proved in kernel_map.md.
