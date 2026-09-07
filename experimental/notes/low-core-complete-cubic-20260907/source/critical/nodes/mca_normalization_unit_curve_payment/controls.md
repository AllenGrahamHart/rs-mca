# Controls and a singular cubic beyond the previous curve classes

## A three-boundary nodal cubic

In characteristic >3, consider

    Q(U,V)=UV(U+V)-U^2-V^2.

Its quadratic and cubic homogeneous parts are coprime. It is absolutely
irreducible: any factorization of a cubic has a line factor. A line
through the double point (0,0) would divide both homogeneous parts;
a line not through (0,0) would leave a homogeneous quadratic factor
there, again dividing both. Neither is possible.

Projection from (0,0) gives the birational parameter

    U=(1+t^2)/(t*(1+t)),  V=(1+t^2)/(1+t),  t=V/U.

Its normalization has three boundary points t=0,-1,infinity.
Both t and w=1/t are integral over the affine curve ring:

    t^2-V*t+1-V=0,
    w^2-U*w+1-U=0.

This also proves directly that every polynomial pair on this CONSTANT
curve, other than the node, is constant: t and t^(-1) are integral
over k[X], thus both polynomial, hence constant. The constant pairs
form a dimension-one curve. The unit may distinguish the two branches
of the node, so demanding a unit in the unnormalized ring is too strong.

The cubic is not smooth, and it is not a polynomial graph after an
invertible affine component change: its highest homogeneous part has
three distinct directions, whereas a degree-three graph has one.
Nor is it a fixed nonzero affine-product level. Its top directions
would force a product (U+c)(V+d)(U+V+e). Matching the quadratic
part gives c=d=-1,e=2, whose linear part is -U-V, not zero. Subtracting
a constant level cannot fix that mismatch. These properties are invariant
under invertible affine changes. This shows a genuine additional
geometric class, not an unsafe MCA source.

## Guards that cannot be removed

- One place at infinity is different. On b^2=a^3, the family
  (a,b)=(h^2,h^3), deg h<=3, has dimension four.
- The residual class is not only cuspidal: on b^2=a^2(a+1), use
  (a,b)=(h^2-1,h*(h^2-1)). This nodal cubic also has just one
  point above infinity and a dimension-four family. In both examples
  the parameter is recovered rationally away from finitely many points.
- Integrality without an inverse is insufficient. On the affine line
  b=0, take a arbitrary of degree <K. The coordinate a is integral,
  but the coefficient dimension is K. The same example rejects using
  the constant unit 1 instead of a nonconstant unit.
- Finitely many divisor patterns does not mean one. On ab=X(X-1),
  the four choices a=lambda*d(X), d a monic divisor of X(X-1), give
  different projective classes. The degree cover retains all components.

The verifier checks the displayed rational identities and a nodal
one-place polynomial witness. Universal dimensions and normalization
statements are hand proofs, not conclusions from point samples.
