# Proof

The original quadratic-strip proof is below. The later, separately
proved residual restriction on 7117..8655 is in `cubic_obstruction.md`;
it uses the same kernel/divisibility mechanism with degree eight and a
new asymmetric collective constant-line count. It does not claim interval closure.

The source hypotheses and all inherited prices are those in statement.md.
Set R=1048576, d=67472, T=500, ell=d-T=66972,
A=J+ell, w=J-1, n=R+J, and Kappa=F(X). Let U be the union of
the COMPLETE joint cores of all represented LOW pairs. Each such core
has at least A points. All polynomial components have degree <J.

## 1. Use the whole interpolation kernel

Let W_10 be the F-vector space of Q(X,Y,Z) of total (Y,Z)-degree
at most ten and weighted degree <A for weights (1,w,w). Its dimension is

    D_10 = sum_(i=0)^10 (i+1)*(A-i*w).

All summands are positive on the asserted interval. Impose the linear
conditions Q(x,u(x),v(x))=0 at every x in U, and call the kernel E.
No interpolation matrix needs to be constructed. Since |U|<=n,

    dim_F E >= D_10-n.

For every Q in E and every represented pair (a,b), Q(X,a,b) has
degree <A and vanishes on that pair's complete core. Root counting
therefore gives Q(X,a,b)=0 identically. This uses all of U, not a
selected subset, and involves no assumption that a coefficient is nonzero.

Take the gcd G of an F-basis of E in Kappa[Y,Z], normalized to a
primitive polynomial in F[X,Y,Z]. Write g=deg_(Y,Z) G. If E is
nonzero, every Q in E is divisible by G already in F[X,Y,Z].
Indeed, Gauss's lemma applies over the UFD F[X]: a primitive G has
content valuation zero at every prime of F[X], so negative valuation
in a coefficient of Q/G would persist in the product, impossible for Q.

Weighted degree is additive for products of nonzero polynomials: their
highest weighted parts have nonzero product in a polynomial domain.
Consequently, if g>=3, every Q/G has pair-degree <=10-g<=7 and
weighted degree <A-g*w<=A-3*w. Multiplication by fixed G is injective,
so

    dim_F E <= D_mult3
      := sum_(i=0)^7 (i+1)*(A-(i+3)*w).

But exact subtraction gives

    D_10-n-D_mult3 = 960748-135*J >=88>0

on 4801<=J<=7116. In particular E is nonzero and g<=2. At
J=7117 the difference is -47; this proof makes no claim there.

## 2. At most 100 pairs lie off the common curve

Write a finite basis Q_i=G*R_i over Kappa[Y,Z]. The R_i have no
common factor and pair-degree <=10-g. At a represented pair off G=0,
all R_i vanish. If one R_i is a nonzero constant there are no such
pairs. Otherwise fix a nonconstant R_0 and choose a Kappa-linear
combination R_1 of the other R_i avoiding every irreducible factor of
R_0. Each avoidance condition is proper, since the R_i have gcd one;
the field Kappa is infinite. Thus R_0,R_1 are coprime.

The affine plane Bezout bound gives at most (10-g)^2<=100 common
geometric points. This also bounds the distinct Kappa-points and hence
the original polynomial pairs. The hypersurface/degree proof is in
`mca_low_core_quadratic_graph_payment/algebraic_list_bound.md`.
Auxiliary algebraic closures count points only; they do not change the
challenge field or slope denominator.

Assign each LOW pair to exactly one factor of G, or to the off-curve
exception set, and keep all its labels with it. Canonical cores make
the nonempty mismatch sets for different labels of a fixed pair disjoint
outside that pair's own core. Each pair thus carries at most

    n-A = 981604

labels. The at most 100 exceptional pairs contribute gain at most
98160400 to the original partitioned margin ledger.

## 3. Price two nonparallel constant-direction lines

The inherited conic/pencil results already pay a single irreducible
quadratic, any single line, two nonconstant-direction lines, one constant
and one nonconstant line, and parallel constant-direction lines. The only
new quadratic pattern is two nonparallel constant-direction lines.

Discard empty groups. Write their independent constant linear forms as
L_1(f)=c_1(X), L_2(f)=c_2(X). Each group contains an actual pair in
the affine common carrier (a_*+V,b_*+V), so c_i-L_i(a_*,b_*) lies
in V. Solving the invertible constant two-by-two system gives an
intersection f_0 in the same affine pair carrier, with degree <J.

For geometry only, subtract f_0 and apply a fixed GL_2(F) change.
The two pair groups become (g,0) and (0,h), with g,h in V. This
does NOT replace or reparameterize the original finite slope labels.
Let the transformed received pair be (u',v'), and put

    S  = {x: u'(x)=v'(x)=0},
    D_1= {x: v'(x)=0, u'(x)!=0},
    D_2= {x: u'(x)=0, v'(x)!=0}.

The sets D_1,D_2 are disjoint, so one has size at most floor(n/2).
For a nonzero pair (g,0), at most J-1 of its >=A joint agreements
can lie in S, since those are roots of g. Thus g agrees with u' at
at least A-(J-1)=66973 points of D_1. The same assertion holds
for h on D_2. Charge the intersection pair separately, at most once.

On the smaller D_i use N_0=floor((R+7116)/2)=527846,
K_0=7116 and A_0=66973. Distinct degree-<J scalar polynomials
agree with each other at at most K_0-1 points. For M listed
polynomials choose A_0 agreements each, and use Cauchy--Schwarz
on the coordinate incidence counts, padded with zeros up to N_0:

    M*(A_0^2-N_0*(K_0-1)) <= N_0*(A_0-K_0+1).

The denominator is 729758439>0 and the numerator 31595805868.
Their ratio lies between 43 and 44, so this group has at most 43
nonzero polynomial pairs. If its domain has fewer than A_0 points,
it is empty instead. This is an ordinary elementary Johnson bound,
not a conjectural MCA conversion.

The other constant group, together with the ONE original resource and
near add-back, has the inherited coupled expression bound
255637082864553899. This bound permits other LOW groups to remain;
it does not reclassify them as HIGH. The smaller group, intersection
pair, and off-G pairs therefore give whole original total at most

    255637082864553899 + (43+1+100)*981604
      = 255637083005904875.

## 4. Exhaust the factor patterns and retain a single resource

Here are conservative whole-source bounds BEFORE the off-G exceptions,
except where the preceding argument has already included them:

- g=0: original resource and near alone, <=46043200488601452.
- g=1: one line, <=255637082864553899.
- g=2 irreducible nonsingular: any one conic, <=170738199574037868.
- g=2 irreducible geometrically singular: at most one rational pair,
  so resource, near and one-pair gain suffice.
- g=2 reducible, two nonconstant lines: <=80443200488601452.
- g=2 reducible, one constant and one nonconstant line:
  <=272837082864553899.
- g=2 reducible, parallel constant lines: the stronger seven-parallel-
  fiber result gives <=261008568111878723.
- g=2 reducible, nonparallel constant lines: section 3 gives
  <=255637083005904875 INCLUDING the off-G exceptions.

A repeated linear factor is just one line; no double charge is needed.
Irreducible geometrically singular quadratics have at most one rational
point in odd characteristic, as proved in all_conic_payment.md.
Each inherited group bound uses the original label partition and counts
the global margin resource and near contribution once. Add 98160400
for the off-G exceptions when not already included. The largest bound is

    272837082864553899+98160400=272837082962714299,

strictly below the budget by 2143645148680788. The proof covers every
source with the printed contract on the entire interval; no arbitrary
curve-existence or per-factor affordability premise remains on this strip.
