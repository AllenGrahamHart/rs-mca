# Proof

The later moving-projection theorem is proved in `moving_projection_graphs.md`.
It reuses the pure-power argument below with the exact projection kernel,
and applies scalar LIST to the input at its actual degree K+h.

All geometric arguments are over the algebraically closed constant field
k. Finite-field applications extend constants only to bound coefficient
dimensions; their actual slopes and denominators stay over the original F.

## 1. Generic multiplicity conditions are independent on V

Let W be any q-dimensional subspace of degree-<K polynomials. Choose a
basis f_1,...,f_q with distinct leading degrees d_1<...<d_q<K. The
determinant of their derivatives of orders 0,...,q-1 has leading
coefficient, up to the nonzero basis leading coefficients,

    product_(i<j)(d_j-d_i).

It is nonzero in characteristic zero or p>=K. The leading exponent is
sum d_i-q*(q-1)/2>=0. Dividing rows by factorials converts to Hasse
derivatives, also invertible since q<=K<=p. Thus q independent
polynomials have full jet rank q at a generic point. Applied to a subset
of min(e,q) basis vectors, this says that imposing vanishing of order e
at one generic point drops dimension by min(e,q).

Repeat on the surviving polynomial subspace after each chosen point.
It still has degree <K and inherits the characteristic guard. Given any
d>=0, there are d distinct points x_1,...,x_d, avoiding ANY prescribed
finite exceptional set, such that the only f in V vanishing to order e
at all x_i form a subspace of dimension

    max(s-e*d,0).                                       (1)

These are auxiliary points over k, NOT a genericity assumption on the
Reed--Solomon evaluation domain. If the surviving space is zero, choose
the remaining points arbitrarily outside the finite exclusions.

## 2. A projective pure-power family has dimension <=floor((s-1)/e)

For a fixed nonzero rational alpha(X), let P be the closed projective
locus of nonzero polynomial parameters [h] in P(H) such that
alpha*h^e belongs to V. The condition is homogeneous and closed after
clearing the fixed denominator and imposing coefficient membership in V.
No nonzero h maps to zero.

Suppose a nonempty component has dimension d. Choose d auxiliary points
as in (1), avoiding zeros and poles of alpha. The d linear conditions
h(x_i)=0 are hyperplanes (or identically zero conditions) on P(H).
A projective variety of dimension d intersects any d hyperplanes.
Hence there is a nonzero h on that component satisfying all conditions.
The nonzero polynomial alpha*h^e in V then vanishes to order at least e
at each x_i. By (1), this is impossible if e*d>=s. Therefore

    dim P <= floor((s-1)/e).                            (2)

The only general intersection fact used is the projective dimension
theorem, [Stacks Project, Lemma 33.34.3](https://stacks.math.columbia.edu/tag/0B2R).
Apply it to the intersection of the hyperplanes, whose codimension is at
most d. The same theorem handles components or redundant hyperplanes.

## 3. Pass to infinity in an arbitrary affine family

The condition Phi(X,h)-b_0 in V is finitely many coefficient equations
of degree at most e in the coordinates of H, after clearing one fixed
X denominator. Let Y be a positive-dimensional irreducible component,
of dimension r, and take its projective closure with homogenizing
coordinate z. It is not contained in z=0. The projective dimension
theorem gives a nonempty intersection Y_infinity with dimension at least
r-1.

For each linear coefficient functional annihilating V, homogenize its
output equation to degree e. Setting z=0 kills all lower powers of h
and the affine offset b_0; the surviving equation is the functional
applied to alpha*h^e. The full projective closure satisfies these
homogenized equations, whether or not they alone define that closure.
Consequently Y_infinity lies in the pure-power locus of section 2.
It follows that

    r-1 <= floor((s-1)/e),
    r <= ceil(s/e).

An isolated component has dimension zero and needs no argument at
infinity. This proves (JD). The proof does not differentiate Phi in h;
the characteristic hypothesis enters ONLY the output-space jet ranks.
Large rational coefficient heights and large parameter degree do not
invalidate the argument, since zeros/poles of alpha are fixed exclusions.

## 4. Two same-degree outputs with a moving leading ratio

Let their leading coefficients be alpha,beta, with beta/alpha
nonconstant. At infinity both alpha*h^e and beta*h^e belong to V.
Thus alpha*h^e belongs to

    W=V intersect (alpha/beta)*V.

If dim W=s, multiplication by beta/alpha preserves V. Cayley--Hamilton
on the nonzero finite-dimensional k-space V would make this rational
function algebraic over k, hence constant, a contradiction. Therefore
dim W<=s-1. If W=0 there is no positive-dimensional component. Otherwise
apply sections 2--3 with W in place of V; it is still a polynomial
subspace of degree <K. This proves (J2).

For e=2 this recovers the moving-parabola dimension floor(s/2) on the
large-characteristic finite rows. The older tangent-equality proof remains
stronger in characteristic scope: it requires only characteristic !=2.
It is not replaced or retracted here. Two outputs of DIFFERENT degrees
are not combined by section 4's shared-power argument.

## 5. Original graph coefficients retain their degree and slope units

For an actual graph, parameterize a=a_0+v in the s-dimensional affine
input carrier. Clearing fixed X denominators makes the output-membership
locus a zero set of equations of degree <=e in those s coordinates.
Its dimension is <=r=ceil(s/e), by section 3. The required generic
supplier's proper-section lemma covers it by a pure r-dimensional variety
of degree <=e^(s-r). Its scalar LIST incidence bound counts the first
polynomial at >=m-T agreements, giving (JL). Projection onto a is
injective on graph pairs, and every complete joint core supplies that many
first-coordinate agreements. No uncontrolled parameter degree is used for
this LIST application; it uses the actual first polynomial, degree <K.

Each original LOW pair carries at most n-m+T finite labels by the disjoint
outside-core argument. Thus the unchanged source resource gives

    |Gamma| <= C/(T+1)+(n-m+T)*floor(e^(s-r)*Q^r).       (3)

HIGH labels stay in the resource. A fixed constant GL_2(F) component
change and a polynomial pair offset may identify the graph; no nonlinear
change is made to the original challenge labels.

## 6. Finite consequence without a degree-by-degree search

On the normalized KoalaBear source s=11, K=J<=169999<p=2130706433,
T=500, n-m+T=981604, Q=1048577/66973<63/4, and
C<=23067643444721720934. The exponent r=ceil(11/e) is constant on
each of the degree ranges {2}, {3}, {4,5}, {6,7,8,9}. Within a range
e^(11-r)*(63/4)^r increases with e. Only endpoints 2,3,5,9 need checking:

    e     r     floor(e^(11-r)*(63/4)^r)
    2     6                    488464861
    3     4                    134577053
    5     3                   1526165771
    9     2                  96104495052

The largest gives, after adding original near once,

    floor(C/501)+981604*96104495052+134944
       =140379757249624860,
    floor(2130706433^6/2^128)-total=134600970861770227.

For completeness this resource bound does not require the finite consumer
as a reverse dependency. The already required nonuniform margin theorem,
with empty universal carrier core, gives

    F(J)=prod_(i=0)^11(R+J-i)/((d+J)*prod_(i=1)^10(d+i)).

Write y=d+J and c=R-d>11. Apart from a positive constant,
F(J)=prod_(i=0)^11(y+c-i)/y. Its expansion is a polynomial with
nonnegative coefficients plus a positive multiple of 1/y; it is convex
for y>0. Thus its maximum on 4801..169999 is at an endpoint.
The primary exact-fraction checker verifies both endpoint values <=C;
the independent checker below also checks them by binomial products.
This reproduces the needed part of the existing resource proof without
making that consumer a dependency of its new supplier.

This is one consequence of the general dimension theorem, not a family
of new per-degree targets.
It invalidates the earlier *recipe limitation* at graph degrees eight and
nine, not an earlier counterexample or unrestricted source obstruction.
