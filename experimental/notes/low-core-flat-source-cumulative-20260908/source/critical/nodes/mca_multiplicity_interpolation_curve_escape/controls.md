# Algebraic controls

These are small proof-interface examples, not canonical KoalaBear sources.

## The X condition cannot be omitted

At P=(0,0,0), Q=X satisfies Q(P)=Q_Y(P)=Q_Z(P)=0. Along the
polynomial pair a=b=0, its substitution is X, with only a simple root.
The omitted Q_X(P)=1 is precisely why the proposed double-root claim
would be false. Full double-point interpolation uses four constraints.

## A concrete escaping relation

Over F7 use D={0,1,2,3,4}, w=1, A=3, r=2, G=Z-Y^4.
Let the received pair be (0,0) at the first three coordinates and (1,1)
at the other two. The polynomial

    Q=Y^2*(Y-1)^2

has weighted degree 4<6 and a double zero at every received triple.
It is not divisible by G, since it is nonzero and independent of Z.
The only affine-linear polynomial pairs on G are constant pairs (c,c^4),
since a nonconstant a has fourth power of degree four, not <=1. Exactly
one, (0,0), has three joint agreements. The bound permits <=20 pairs.
Here Phi_1(6)=56, Phi_1(2)=4 and the escape surplus is 32>0.

## Strictness and degree conventions

At n=A=r=w=g=1 with receiver (0,0) at X=0, W(r*A) consists
only of constants. The interpolation kernel is zero. The gap in (ESC)
is exactly zero, so replacing > by >= would incorrectly assert an escape.
Taking G=Y makes the failed escape statement literal.

The upper pair degree is floor((r*A-1)/w), not floor(r*A/w).
No result is inferred just beyond a positive dimension interval. In the
finite quartic application, the gap is 80 at J=9821 and -284 at 9822.
This is failure of the sufficient recipe, not an unsafe MCA witness.
