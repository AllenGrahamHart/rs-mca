# A Split Three-Cycle Gives A Multiple Fibre In The Surviving Geometry

The polynomials1,v,w have distinct degrees0,3,4, so they are independent.
The first component identifies W with U and makes pi_0 invertible.
For ell=(1,v,w), the joint evaluation rows are ell and ell*T=(v,w,1).

If they are dependent at a finite geometric coordinate x, there is
lambda with v=lambda,w=lambda^2 and lambda^3=1. In particular v!=0.
Since w=x*v, x=lambda. But v=x^3-x=1-lambda=lambda, so2*lambda=1.
Together with lambda^3=1 this forces8=1, impossible in characteristic
zero or greater than7. Thus joint evaluation has rank two everywhere
finite; W also has function-field rank two.

Their cross product is the stated kernel d, with components

    -X^8+2X^6-X^4+X^3-X,
     X^7-2X^5+X^3-1,
    -X^6+3X^4-2X^2.

Their distinct degrees make them linearly independent over F.
If a two-dimensional constant coefficient plane H in W had function-field
rank one, its scalar extension would contain the one-dimensional kernel
of W_(F(X))->F(X)^2. A nonzero constant functional annihilating H would
therefore annihilate d(X) identically, contradicting that independence.
Hence W is pencil-free in the required sense.

## A Rational Inverse Exists Generically

The coefficient action of T is (a,b,c)->(c,a,b). By definition,
ell*d=ell*T*d=0. Wherever d and T*d are independent, their cross
product therefore recovers ell projectively. This open set is nonempty:
at x=0, d=(0,-1,0) and T*d=(0,0,-1) are independent.
On the further open set v!=0, the recovered ratio w/v recovers x.
Thus the kernel map has a rational inverse and generic fibre size one.

## The Exceptional Fibre Has Three Points

At x=-1,0,1 we have v=w=0 and d=(0,-1,0).
Conversely a finite x in this projective fibre satisfies v=w^2 and
w=v^2. If v!=0 these imply v^3=1 and x=w/v=v, whence
v=x^3-x=1-v. Again2*v=1 and v^3=1 would force8=1.
Therefore v=0, giving exactly the three printed coordinates; they are
distinct under the characteristic guard. The degree-eight homogeneous
kernel map takes infinity to[-1:0:0], not the specified fibre, so there
is no additional point at infinity. Its common-zero exclusion was
already proved by joint rank two, with the leading term excluding infinity.

The pair(v,w) differs from(0,0) in two polynomials whose common zeros
are exactly those of v, since w=X*v. This realizes the multiple fibre
as candidate-pair joint intersections, without asserting the large
agreement, raw minimization or full-code badness of an official source.
