# Rational X-coefficients: two coprime tangent images

Status: PROVED, 2026-09-07. The polynomial-graph theorem extends to

    b=Psi(X,a), Psi in F(X)[Y], deg_Y Psi=e>=2,
    e nonzero in F.                                      (RG)

The denominator may depend on X but NOT on Y. Keep actual carrier
dimension s>=1 and all the original support and label hypotheses.
The same bounds hold:

    r=floor((s+1)/2) if e=2; r=max(1,floor(s/2)) if e>=3,
    M<=floor(e^(s-r)*Q^r), Q=(n-K+1)/(m-T-K+1),
    |Gamma|<=C_s/(T+1)+(n-m+T)*floor(e^(s-r)*Q^r).       (1)

Fixed constant GL_2(F) changes and degree-<K polynomial pair offsets
are allowed only as in the earlier theorem. No nonlinear change of
MCA labels is made. This proof replaces the earlier leading-degree
argument, which by itself does NOT work with rational coefficients.

## 1. Normalize the variation and the derivative

Work over an algebraic closure k. Clearing the fixed X denominator
makes the coefficient locus

    Z={a in a_0+V: Psi(X,a) belongs to b_0+V}

an affine algebraic set cut out by equations of degree at most e in
s input coefficients. Take a positive-dimensional reduced irreducible
component Y and a k-point a_* in Y. Let P be the monic gcd of all
polynomials a-a_* as a ranges over Y. One can take the gcd of a finite
basis of their linear span. P is nonzero. The normalized family

    H={(a-a_*)/P: a in Y}

is isomorphic to Y, contains zero, and has gcd one. At every x in k,
evaluation h -> h(x) is NONCONSTANT on H: if constant, it is zero
because 0 belongs to H, contradicting the gcd-one property.

Let D be the maximum polynomial degree in H. If D=0, dim Y<=1,
which is enough since s>=1. Otherwise D>0 and the coefficient lambda
of X^D is a nonconstant function on H. Tangents w to H have degree
at most D. Set

    Phi(X,H)=Psi(X,a_*+P*H),
    Phi_H(X,H)=c(X)*R(X,H),

where c is a nonzero rational function and R in k[X,H] is primitive
in its polynomial X-coefficients: gcd_j R_j(X)=1. This comes from
clearing denominators and dividing out their common content. Because
e is nonzero in k, deg_H R=e-1.

## 2. Two derivative values can be chosen coprime

The polynomials R(X,h(X)), as h ranges over H, have no common root.
Indeed, at any x the polynomial R(x,H) is nonzero by primitivity,
and h(x) is nonconstant on the irreducible variety H. A nonconstant
function over the algebraically closed field k is transcendental over
k, so R(x,h(x)) cannot vanish identically.

Their generic degree is

    E=max_(R_j!=0)(deg R_j+j*D)>=(e-1)*D.               (2)

At degree E the coefficient is the nonzero polynomial
sum_(deg R_j+jD=E) lc(R_j)*lambda^j. Distinct j give distinct
powers and lambda is nonconstant, so this coefficient does not vanish
identically. Choose h_1 of full degree E for its derivative value R_1.
For each of the finitely many roots x of R_1, the condition
R(x,h(x))=0 is a proper closed condition on H. Choose h_2 outside
their union and outside the degree-drop locus. Thus

    deg R_1=deg R_2=E, gcd(R_1,R_2)=1.                   (3)

These auxiliary choices are over k; they assert no generic-point
existence over the original finite field. Both normalization steps
above are essential to (3).

## 3. Pay the component dimension using a common output space

Differentiate the defining output-membership equations at h_i. For
every w in the tangent space T_i of H,

    c*R_i*w belongs to V_k.

Multiplication by nonzero R_i is injective. Therefore the two spaces
R_i*T_i each have dimension at least dim Y and both lie in the SAME
s-dimensional rational-function space c^(-1)*V_k.

If R_1*w_1=R_2*w_2, coprimality implies R_2 divides w_1 and
R_1 divides w_2. Since deg w_i<=D, for e=2 the intersection has
dimension at most one: E>=D, and equality permits only constant
multiples of R_1*R_2. For e>=3, E>=2D>D and the intersection is
zero. Consequently s>=2 dim Y-1 or s>=2 dim Y, respectively.
The D=0 and zero-dimensional cases finish dim Y<=r. Smoothness is
not assumed: the tangent dimension is at least the component dimension.

Apply the existing degree-e proper-section cover and algebraic LIST
incidence lemma in `algebraic_list_bound.md`. Their degree cost is
e^(s-r), unchanged by a fixed X denominator. Graph projection to a
is injective as a polynomial-pair map even if the rational expression
has poles. Complete cores give at least m-T first-coordinate agreements.
The original-label argument in `proof.md` now proves (1).

## 4. A pole-safe received-data certificate

Write Psi=N(X,Y)/B(X), with B nonzero and N polynomial. On the
COMPLETE transformed LOW core union U require

    B(x)*v_*(x)=N(x,u_*(x)) for EVERY x in U,
    max(deg B+K-1, max_i(deg N_i+i*(K-1))) < m-T.      (4)

Include roots of B in this condition; do not delete those coordinates.
For each pair, B*b-N(X,a) has degree <m-T and vanishes on its
complete core of size at least m-T. It is zero, proving (RG).
No monic B, nonvanishing B on the domain, or bounded pole count is
needed. At a pole, first-coordinate agreement need not imply joint
agreement. Only the reverse inclusion was used in the LIST bound.

An arbitrary high-degree received fit remains insufficient. A rational
denominator depending on Y, a general plane curve, and a universal
graph description are outside this theorem.
