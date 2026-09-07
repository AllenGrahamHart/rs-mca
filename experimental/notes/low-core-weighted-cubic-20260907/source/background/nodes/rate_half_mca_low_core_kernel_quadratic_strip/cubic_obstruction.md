# A one-place-at-infinity cubic is the remaining lower-strip obstruction

Status: PROVED, 2026-09-07. This is a necessary condition for an
unpaid source, NOT closure of the interval below.

Use exactly this node's canonical normalized source contract. Put

    B=274980728111395087, N=|Gamma|+134944,
    R=1048576, A=J+66972, w=J-1, n=R+J, Kappa=F(X).

For 7117<=J<=8655, at least one of the following holds:

1. N<=255637082913634099<B, with reserve 19343645197760988.
2. There is a geometrically integral singular cubic G over Kappa,
   with its unique singular point in the AFFINE plane,
   whose geometric projective normalization is P^1 and has exactly
   ONE point above the line at infinity, containing all but at most
   64 represented LOW polynomial pairs.

Consequently N>B forces the second alternative. It also forces every
populated constant-direction line to carry at most 132 LOW pairs.
The two alternatives need not be disjoint; the second is not an unsafe
witness. It includes both nodal and cuspidal cubics.

The affine-singularity refinement in section 5 additionally gives the
explicit parametrization in `affine_singular_normal_form.md` for all
but <=65 pairs. The first four sections establish the earlier one-place
reduction without yet excluding a singularity at infinity.

## 1. The whole degree-eight kernel forces pair-degree at most three

Use the proof in `proof.md`, now with W_8, the full space of
weighted-degree-<A, pair-degree-<=8 polynomials. On the complete
LOW core union, let E be its entire interpolation kernel. Then

    dim E >= D_8-n,
    D_8 = sum_(i=0)^8 (i+1)*(A-i*w).

Each Q in E vanishes identically on every LOW pair by the same
strict-degree root argument. Normalize the gcd of a basis to a
primitive G in F[X,Y,Z]. If its pair-degree g>=4, Gauss division
and additive weighted degree give

    dim E <= D_mult4 = sum_(i=0)^4 (i+1)*(A-(i+4)*w).

But

    D_8-n-D_mult4 = 960724-111J >0

through J=8655, and in particular on the present interval. Every
summand here is positive. Thus E is nonzero and g<=3. Two coprime
linear combinations of the residual basis after dividing by G leave
at most (8-g)^2<=64 geometric points off G. This is exactly the
Bezout step in the original proof, with eight in place of ten.
Each exceptional polynomial pair carries at most n-A=981604 labels.
No interpolation matrix is constructed or assumed generic.

## 2. A constant-direction line is small, or the whole source pays

Let ell be any constant-direction affine Kappa-line containing an
actual LOW pair. Write ell as L(a,b)=c(X), where L is a nonzero
F-linear form. The represented pair shows c is a polynomial of
degree <J. Define

    S={x: L(u(x),v(x))=c(x)}.

Every LOW pair on ell has all its joint agreements inside S.
For a pair f off ell, the nonzero polynomial L(f)-c has degree <J.
At most J-1 of its >=A agreements can therefore lie in S. At least

    A-(J-1)=66973

lie in S-complement.

Split at |S|=600000 rather than dividing the domain equally. Use
K_0=8655 and the following two uniform Johnson rows:

    on the line:  N_1=600000, A_1=7117+66972=74089;
    off the line: N_2=(R+8655)-600001=457230, A_2=66973.

The ordinary Johnson incidence argument applies to JOINT pairs too:
two distinct pairs agree jointly in at most K_0-1 places. Selecting
A_i agreements per pair and applying Cauchy--Schwarz gives

    M*(A_i^2-N_i*(K_0-1)) <= N_i*(A_i-K_0+1).

For i=1 the denominator/numerator are 296779921 and 39261000000,
giving M<=132. For i=2 they are 528514309 and 26665196370,
giving M<=50. If the chosen domain has fewer than A_i coordinates,
the list is empty. The on-line bound uses A>=A_1; the off-line bound
uses the different agreement A_2, not the stronger on-line agreement.

If |S|<=600000, this bounds all LOW pairs on ell by 132.
If |S|>600000, it
bounds ALL LOW pairs off ell, not just those on a chosen second
curve, by 50. The inherited constant-line group bound includes the single
resource and near allowance and is <=255637082864553899. Hence
in the latter case

    N <=255637082864553899+50*981604
       =255637082913634099.                           (1)

This already includes off-G pairs. There is no extra near/resource
charge and no deletion of other LOW labels. An empty line group is
ignored. The equal-half argument with agreement 66973 on BOTH sides
would fail at J=8488, but it throws away the stronger on-line agreement.
The asymmetric cutoff proves the whole asserted interval. Its endpoint
8655 comes from the kernel test, which fails at 8656.

## 3. Exhaust every affordable factor pattern of degree at most three

If (1) does not already hold, every populated constant-direction
line has at most 132 pairs, hence gain <=129571728<W,
where W=17200000000000000. Every nonconstant-direction line also
has gain <W by the existing pencil bound. Thus ALL line factors in
the remaining case cost at most W each, regardless of their directions.

Every irreducible quadratic has the inherited group gain at most
124694999085436416 (including moving conics); a geometrically
singular irreducible quadratic instead has at most one rational pair.
An irreducible cubic of either of these two classes has group gain
at most G_3=159185671413625180:

- its projective completion is geometrically smooth;
- its geometric normalization is rational with at least two points
  above infinity, by the normalization-unit supplier.

An irreducible cubic which is not geometrically integral has at most
six Kappa-points; justification is in section 4. Its gain is negligible
compared with G_3. Repeated factors do not incur repeated charges.
For all other factor patterns, the largest group-gain upper bound is
G_3: three lines cost <=3W, and a line plus a conic costs at most
W+124694999085436416<G_3. Lower-degree cases are included.

Assign pairs, together with all their labels, to one factor or the
off-G set. The inherited global resource satisfies
F(J)<=23067643444721720934 throughout this interval. All affordable
patterns therefore give

    N <=46043200488601452+G_3+64*981604
       =205228871965049288,                            (2)

less than the bound in (1). A source escaping both (1) and (2)
must have G irreducible of degree three, geometrically integral,
singular, and with fewer than two normalization points at infinity.
Section 4 shows its normalization is P^1 and the boundary is nonempty,
leaving exactly one point. All but at most 64 LOW pairs lie on it.

## 4. Cubic classification details used above

The field has characteristic p>3. An irreducible polynomial of total
degree three is geometrically reduced: after choosing a variable in
which its derivative is nonzero, the coprimality with that derivative
persists over an algebraic extension. Primitive coefficient content
does not acquire a common factor under extension. The case of a
univariate polynomial follows from separability at degree <p.

If such a curve has several geometric components, the absolute Galois
group permutes them transitively. Purely inseparable extension creates
no new components; reducedness excludes an inseparable multiplicity.
A smooth Kappa-point would lie on one unique component fixed by this
action, impossible. All its Kappa-points are therefore geometrically
singular. Choose a nonzero partial derivative of the cubic. It has
degree <=2 and is coprime to the cubic over Kappa; the coprimality
persists on extension. Plane Bezout bounds their common points by six.

For a geometrically integral singular cubic, projection from a singular
point parametrizes the curve over a finite extension. In affine
coordinates centered there its equation is Q_2+Q_3=0, with nonzero
quadratic and cubic homogeneous parts. A general line through the
double point meets just one further point; explicitly its nonzero
coordinate is -q_2(t)/q_3(t). A triple point would make the cubic
homogeneous and geometrically reducible. Thus the geometric projective
normalization is P^1. Its boundary above infinity is nonempty, since
a positive-dimensional proper curve cannot be contained in affine space.

The remaining one-boundary class includes b^2=a^3 and b^2=a^2(a+1).
Their dimension-four bounded polynomial families show why the proved
dimension-one arguments cannot simply be extended to this last class.
No assertion of its impossibility or payment is made.

## 5. Exclude a singularity at infinity and retain a rational normal form

The existing jet supplier now proves a coupled moving-projection bound.
If the remaining one-place cubic has its singular point at infinity,
its direct coefficient test shows that it is a polynomial cubic graph
in a primitive linear input x=A*a+B*b over Kappa. Its highest binary
form is c*(A Y+B Z)^3. The primitive weighted-degree bound inherited
from the kernel forces h=max(deg A,deg B)<=17580 on this interval.

That supplier gives group gain <=71875471818343284, hence whole
resource/near plus <=64 off-curve pairs costs <=117918672369767392.
This is below the paid alternative, so any source escaping that alternative
cannot have an infinity singularity; in particular N>B excludes it.
The unique singular point must therefore be affine. Completing the square
and removing the repeated root, as proved in
`affine_singular_normal_form.md`, gives the exact original-function-field
description

    f=f_s+(tau^2-lambda)*(P+tau*Q),

where P,Q are Kappa-linearly independent. Aside from the <=64 off-curve
pairs, only the singular pair f_s may lack a nonsingular rational parameter.
Thus all but <=65 LOW pairs have this form with tau^2!=lambda.
This last (2,3) family is not paid by a polynomial-in-linear-input theorem.
