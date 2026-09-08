# Sharpness and required guards

## Sharp upward rounding

Let e>=2 and r>=1, work in characteristic zero or p>e(r-1), and
take V to be all polynomials of degree <=e(r-1). Then s=e(r-1)+1.
The graph (h,h^e), with h any polynomial of degree <=r-1, has an
r-dimensional coefficient family in V x V. Hence ceil(s/e)=r is
attained. Replacing it by floor(s/e) would be false when e>1.
For e=3,r=4 this is s=10 and a genuine four-parameter family.

## Characteristic is load-bearing

In characteristic three, h=c+dX gives h^3=c^3+d^3 X^3. With
V=span{1,X,X^3}, s=3, the graph family has dimension TWO (its first
component gives independent c,d), although ceil(3/3)=1. Here K=4>p=3.
The output Wronskian vanishes. This is an algebraic counterfamily over the
algebraic closure, not an inference of dimension from nine finite points.

## Generic auxiliary points are not arbitrary domain points

For V=span{1,X^2} in characteristic 101, evaluation at 1 and -1 has
rank one, not two. There is no assertion that arbitrary domain points
impose independent jets. The proof chooses auxiliary points in k away
from successive Wronskian zero sets; they need not be code coordinates.

For V=span{1,X,X^3,X^4}, two double-root conditions at 1 and 2
DO have full rank four in characteristic 101. A degree-four polynomial
with those double roots is proportional to (X-1)^2(X-2)^2, whose
X^2 coefficient is 13, so it is not in V unless it is zero.

## Affine offsets must survive until homogenization

For h=c+dX, h^2 in X+span{1,X^2} is the affine hyperbola 2cd=1.
Its projective closure is 2cd=z^2. Its two infinity points satisfy cd=0,
the pure-square condition for V=span{1,X^2}. Dropping the offset in
the original affine equation would give a different locus; only the
homogeneous highest-degree equations are used at infinity.

## Rational leading coefficients and high parameter degree

Let h=(X+1)(c+dX), Phi(X,h)=h^3/(X+1)^3, V=P_<=3.
This is a two-parameter family, attaining ceil(4/3)=2. The parameter
has degree two while the output has degree three. A naive assertion
degree(output)=3*degree(parameter) would be wrong. The fixed pole at -1
is avoided by the auxiliary-jet argument, not deleted from a code domain.

The finite consequence continues to require an actual graph identity on
the represented pairs. Merely fitting received values at some coordinates
does not provide one; the earlier pole-safe root-degree gate is unchanged.
This proof does not supply affordable bounds for arbitrary nongraph cubics.
