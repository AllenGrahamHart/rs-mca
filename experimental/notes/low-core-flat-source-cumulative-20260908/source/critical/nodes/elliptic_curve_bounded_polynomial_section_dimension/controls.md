# Algebraic controls and scope boundaries

These are hand proofs, not dimension estimates from finite samples.

1. Smooth generic cubic is necessary. On b^2=a^3, put
   (a,b)=(h^2,h^3) with h arbitrary of degree <=3. Both coordinates
   have degree <=9, but this is a dimension-four family: away from
   h=0, h=b/a recovers the parameter. It contradicts a dimension-one
   statement without the smoothness guard.
2. Universal rigidity is false. On the constant smooth cubic
   b^2=a^3-a in characteristic >3, the constant polynomial pairs
   contain a dimension-one affine elliptic curve. Thus one cannot
   replace <=1 by zero merely because the generic cubic is smooth.
3. A nonconstant-j example has a complete small-degree classification.
   Take b^2=a^3+X*a+1. Its discriminant is -16(4X^3+27), nonzero
   in k(X); j=6912X^3/(4X^3+27) is nonconstant for p>3.
   For a=alpha*X+beta, b=gamma*X+delta, comparison in degrees
   3,2,1,0 successively gives alpha=0, gamma=0, beta=0,
   delta^2=1. Exactly (0,1) and (0,-1) remain. Some specialized
   fibers are singular: that does not violate generic smoothness.
4. The result goes beyond the preceding affine-product-level class.
   The homogeneous degree-three part of b^2-a^3+a is -a^3,
   with just one direction. A degree-three affine product with at
   least two nonparallel directions has at least two directions in
   its top homogeneous part. Invertible affine changes over k(X)
   preserve that distinction. A polynomial graph is rational, whereas
   this smooth projective cubic has genus one. This is a distinction
   between geometric classes, not an original-row unsafe witness.
5. The theorem concerns reduced components. Nonreduced coefficient
   schemes may have larger tangent spaces at singular points. The
   proof takes a smooth point of a reduced component after spreading;
   it does not assert a bound on every ambient Zariski tangent space.
6. All-smooth implies the product here only because the base is P^1
   and the fibration has a section. Neither condition is dropped.
7. A nonminimal discriminant zero does not certify rigidity. The cubic
   b^2=a^3-X^4*a has discriminant 64X^12 in these coordinates and
   constant j=1728. But (a,b)=(X^2*c,X^3*d), for constants satisfying
   d^2=c^3-c, is a dimension-one bounded polynomial family. Scaling
   over k(X) identifies the curve with a constant elliptic curve;
   its relatively minimal surface is the product, with no singular
   fiber. Always use the relatively minimal surface, not the zeros
   of a discriminant before minimizing. The nonconstant-j test avoids
   this particular recognition problem.

The critical counting consumer checks the elementary coefficient
identities in items 1 and 3. Those checks do not certify the surface
theorems or the family-spreading argument.
