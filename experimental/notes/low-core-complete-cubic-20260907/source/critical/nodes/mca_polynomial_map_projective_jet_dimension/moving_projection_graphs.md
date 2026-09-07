# Couple a moving projection to its kernel dimension

Status: PROVED, 2026-09-07. This extends the same projective-jet
mechanism; it does not assume the projection preserves polynomial degree.

## 1. Exact statement

Let V be an s-dimensional subspace of degree-<K polynomials over F,
s>=1, in characteristic zero or p>=K. Fix affine pair offsets
(a_0,b_0) with both degrees <K. Let A,B in F[X] be coprime and
not both zero, and put h=max(deg A,deg B). Suppose Phi,Psi in
F(X)[Z] have maximum Z-degree e>=2 and satisfy the EXACT identity

    A*Phi(Z)+B*Psi(Z)=Z.                              (1)

Consider the polynomial pairs (a,b)=(Phi(z),Psi(z)) in
(a_0+V) x (b_0+V). Define the F-linear map

    L: V x V -> F[X], (v,w) |-> A*v+B*w,
    d=dim ker L, N=dim im L=2s-d, r=ceil(d/e).

At least one multiplier is injective on V, so 0<=d<=s.
The input z=A*a+B*b lies in the affine N-dimensional space
A*a_0+B*b_0+im L and has degree <K+h. Every reduced coefficient
component of admissible inputs has dimension <=r. This includes d=0,
when every component is zero-dimensional.

If m-t>=K+h, then on n distinct evaluation points the number M_t of
represented pairs having >=m-t joint agreements satisfies

    M_t <= e^(N-r)*((n-K-h+1)/(m-t-K-h+1))^r.          (2)

The inverse from pairs to inputs and the polynomial maps Phi,Psi are
over the original function field. No normalization extension, evaluation
pole deletion, or nonlinear change of the original slope labels occurs.

## 2. The SAME d controls dimension and coefficient cost

The nonzero leading vector (alpha,beta) of (Phi,Psi) satisfies
A*alpha+B*beta=0, because e>=2 in (1). Over an algebraic closure
of the constant field, take an irreducible positive-dimensional input
component Y of dimension q. Its projective infinity has dimension >=q-1.
At every point [z] there, the original output-membership equations give

    (alpha*z^e,beta*z^e) in ker(L:V x V -> F[X]).        (3)

If alpha!=0, then B!=0, so first-coordinate projection is injective
on ker L. Its image W is a d-dimensional subspace of V. Equation
(3) implies alpha*z^e in W. If alpha=0, use the second coordinate,
which is injective since A!=0. In either case W has degree bound <K,
even though the INPUT parameter degree may be larger.

The pure-power jet lemma in this node's main proof gives

    q-1 <= floor((d-1)/e), hence q<=ceil(d/e).

For d=0, (3) is impossible for a nonzero z, so no positive-dimensional
component exists. Affine offsets disappear at projective infinity and
do not alter the leading vector. The characteristic guard concerns
the output space W, not a falsely preserved input degree.

Meanwhile, the input ambient dimension is N=2s-d by rank-nullity.
Clearing fixed X-denominators in output membership gives equations
of degree <=e in THESE N affine coordinates. The existing proper-section
lemma covers the input locus by a reduced pure r-dimensional variety
of degree <=e^(N-r). All components are retained.

## 3. Count the larger-degree scalar input honestly

Every original joint agreement at x implies

    z(x)=A(x)*u(x)+B(x)*v(x).

The right side defines a scalar received word on ALL original domain
points. It is polynomial evaluation of A,B, with no denominator to
delete. Even poles in the displayed output formulas Phi,Psi do not
remove this implication: those formulas are used as rational identities,
not evaluated at their poles.

Distinct represented pairs have distinct z by their given Phi,Psi
description. Apply the scalar algebraic LIST lemma to the input
coefficient cover at degree bound K+h and agreement m-t. This proves
(2). There is no factor e^r from mapping the cover into pair space:
LIST is applied to the scalar INPUT in its actual, larger degree bound.
Nor is a multiplicity factor silently discarded: (1) and Phi,Psi make
the pair-to-input map a bijection on the represented solution set.

For canonical LOW pairs, a fixed pair carries at most n-m+T labels.
Thus a uniform pair cap M gives group gain <=(n-m+T)*M, before the
one global margin resource and original near allowance are added.

## 4. Cubic payment with a printed projection-height cap

On the usual normalized source s=11, (n,K,m)=(1048576+J,J,67472+J),
T=500, 4801<=J<=169999, set e=3. If h<=51391, then

    Q_h=(1048577-h)/(66973-h) <64.

Here 0<=d<=11, N=22-d and r=ceil(d/3). For each fixed r>=1,
the largest e^(N-r)*64^r occurs at d=3r-2, and the successive
block maxima have ratio 64/81<1. The r=0 value is 3^22,
less than the first block maximum. Hence

    M_LOW <=3^20*64=223154201664,
    |Gamma|+134944 <=265092257458790508,
    reserve =9888470652604579.                         (4)

The source resource bound is the same C=23067643444721720934
proved in this node's main proof. Original labels, HIGH, complete own
cores and the single near charge are unchanged. This is a restricted
graph theorem, not a classification of every curve.

## 5. Primitive weighted equations bound projection height

Suppose a primitive polynomial curve equation G(X,Y,Z) has total
pair degree e and top homogeneous pair part c(X)*(A Y+B Z)^e,
with the same coprime A,B. Then c is in F[X]: the coefficients
c*A^e and c*B^e are polynomial and gcd(A^e,B^e)=1. Consequently

    weighted_degree_(1,w,w)(G) >= e*w+e*h.             (5)

If this degree is <A_core=J+66972 and w=J-1, then

    h <= floor((A_core-1-e*w)/e).                      (6)

For e=3 and 7117<=J<=8655, (6) gives h<=17580 and Q_h<21.
The same block argument now gives

    M_LOW <=3^20*21=73222472421,
    group gain <=71875471818343284,
    whole selected source plus near <=117918672306944736.  (7)

A primitive factor of the full interpolation-kernel gcd inherits the
strict weighted bound, by Gauss division and additive weighted degree.
No matrix needs to be constructed to apply this statement.

## 6. Quadratic version pays weighted moving conics ordinarily

For e=2, (6) gives h<=31086 whenever J>=4801. Thus Q_h<29.
With N=22-d,r=ceil(d/2), the fixed-r maxima occur at d=2r-1;
their ratio is 29/8>1. Including d=0, the largest is d=11,r=6:

    M_LOW <=2^5*29^6=19034346272,
    group gain <=18684190437980288 <2W,
    W=17200000000000000.                              (8)

This gives an ordinary degree-two price for any quadratic PROJECTION
GRAPH with the printed height or weighted-equation condition. It does
not replace the older unrestricted moving-conic bound at arbitrary height.

## 7. Geometric recognition at infinity

For a conic or cubic with just one geometric point on the line at
infinity, its highest binary form is a power of one linear form. In
characteristic different from two or three respectively, that linear
direction is defined over F(X): a coefficient ratio recovers it, with
the pure-coordinate case immediate. Choose the primitive input
x=A Y+B Z and a complementary F(X)-linear coordinate y.

A geometrically integral conic in these coordinates is
c*x^2+l*x+d*y+b=0. Irreducibility forces d!=0, so y is a polynomial
of degree two in x. Transforming back gives (1) with e=2. This covers
the unique-infinity nonsingular conics, including moving parabolas.

For a one-place-at-infinity geometrically integral cubic, write its
equation as c*x^3+q20*x^2+q11*x*y+q02*y^2+q10*x+q01*y+q00=0.
Its unique point at infinity is [0:1:0]. If that point is singular,
q02=0 by the W-derivative of the homogenization. If q11!=0, solving
for y gives a cubic numerator over a linear denominator. They cannot
share a factor by geometric integrality. Its normalization then has
two boundary points: the finite denominator root and x=infinity,
contrary to the one-place hypothesis. Hence q11=0 and q01!=0,
and y is a polynomial cubic in x. This proves (1) with e=3 and
allows the weighted height/payment (7).

The remaining one-place singular cubics must therefore have their
singular point in the AFFINE plane. No polynomial-in-linear-projection
description is claimed for them; their normalization has quadratic and
cubic coordinates, not a linear coordinate.
