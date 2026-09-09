# Two-Constraint Incidence Or Charged Rational-Pencil Ownership

Write R=1048576,d=67472,J_max=21499,n_max=1070075,
W=624373932788019251 and near=134944. The required rank-filtration
theorem proves on the entire stated interval, for ANY valid selection,

    sum_gamma min(raw_gamma,4)<=W.                    (MASS)

The original-source assembly owns the normalization and one-time near
allowance. No original rank or shared-core condition is retested after
reselection inside its fixed actual carrier. Choose any minimizers; all
arguments below hold uniformly for that assignment.

## 1. The Same-Source Truncated-Three Identity

Let N=|Gamma| and S_t=sum_(raw<=t) raw for t=1,2. Since every
full-code-bad record has raw>=1, termwise telescoping gives exactly

    N = (sum min(raw,3))/3 + S_1/2 + S_2/6
      <= W/3 + S_1/2 + S_2/6.                        (CUM)

Thus raw>=3 labels have not been discarded or left to an older cutoff.
Equivalently N<=W/3+G for G=sum_(raw<=2)(1-raw/3).

For a pair f let H_f be its COMPLETE joint agreement set on the original
normalized domain. A raw<=t owner has |H_f|>=m-t. At a coordinate outside
H_f, the nontrivial equation (u-a)+gamma*(v-b)=0 has at most one finite
slope solution. Hence all selected defect sets belonging to the SAME pair
are disjoint. If M_t counts pairs of P_2 with |H_f|>=m-t, then

    S_t <= (n-m+t) M_t = (981104+t) M_t.               (OWN)

Pairs represented only at raw two may also be counted in M_1 if their
complete core is large enough; this only enlarges the upper bound.
Different pairs may reuse coordinates. No outside-of-union factor is
valid in this unrestricted branch.

## 2. Function-Field Rank Two

Let f_*+W_pair=aff(P_2), actual F-dimension r<=10. Assume W_pair has
rank two over F(X); necessarily r>=2. Apply the required determinant
incidence theorem at agreement A_t=m-t. Its degree guard is positive:

    A_t-2K+2=d-J+2-t>=45973>0.

The affine-incidence quotient does not depend on J:

    Q_t=(n-K+1)/(A_t-K+1)=(R+1)/(d+1-t)>1.

The theorem therefore gives

    M_t <= (R-J+2)/(d-J+2-t) * Q_t^(r-2)
        <= (R-J_max+2)/(d-J_max+2-t) * Q_t^8.          (PAIR)

The first ratio increases with J, with derivative
(R-d+t)/(d-J+2-t)^2>0. The denominator is positive throughout the
whole interval. Replacing the exponent by eight uses Q_t>1 and r<=10.
No condition is imposed on the function-field rank of child sections.

Substitute (PAIR) and (OWN) into (CUM), retain rational values until the
final floor, and add original near once:

    N+near <= floor(W/3 + sum_(t=1)^2
       (981104+t)/(t*(t+1))
       * (R-J_max+2)/(d-J_max+2-t)
       * ((R+1)/(d+1-t))^8) + near
      =257846243054097181.                            (TWO-PRICE)

The separate integer pair caps are 76016086692 and76026754036, but the
printed total conservatively uses the unfloored fractions. The exact
reserve is17134485057297906.

## 3. Function-Field Rank One: Keep Preferred Labels

Now W_pair has function-field rank one and P_2 contains at least two
pairs. The required rational_line_cores.md proof supplies a primitive
coprime row A0*a+A1*b=Q and parameterization

    (a,b)=(a_*,b_*)+(A1,-A0)H, deg H<K-h<=K,
    h=max(deg A0,deg A1)<K.

Here each H is a POLYNOMIAL, by Bezout for the coprime row. This affine
parameterization is injective and F-linear on differences, so the ACTUAL
represented H-family has affine dimension r<=10, even for a constant
direction row. We do not substitute the full ambient pencil dimension.

Let U be the union of the COMPLETE cores of every pair in P_2, e=n-|U|.
Coverage gives A0*u+A1*v=Q on U and a unique scalar receiver w there
with (u-a_*,v-b_*)=(A1,-A0)w. No gcd-root coordinate is removed.
Joint agreement for each represented pair is exactly H=w on its core.

Let E be the finite slopes gamma with A1(x)-gamma*A0(x)=0 for some
x in U. Because A0,A1 have no common zero, |E|<=|U|<=n_max. For
nonpreferred assigned labels, scalar agreement inside U implies joint
agreement, so ALL their selected defects lie outside U. Preferred labels
are charged separately by at most one unit of G each.

For a fixed pair write c_f=max(1,m-|H_f|), necessarily1 or2 here.
All nonpreferred owners have raw>=c_f and total raw at most e. Their
contribution to G is at most e*(1/c_f-1/3). Thus the exact same-pair
telescoping in the credited pencil proof gives

    G <= n_max + e*(M_1/2+M_2/6).                    (PENCIL-GAIN)

This group argument uses actual counts, not the older cutoff-500 resource.
Its resource term is (MASS) through (CUM), on the SAME original source.
All other raw labels are still paid there.

Apply the scalar specialization of the required affine incidence lemma on
U. If |U|>=m-t, its ratio is at least one and r<=10 gives

    M_t <= ((|U|-K+1)/(m-t-K+1))^10
         =((R+1-e)/(d+1-t))^10.                       (U-LIST)

If |U|<m-t then M_t=0, so the displayed upper bound still holds. Its
numerator remains positive: P_2 is nonempty, hence |U|>=m-2>=K and
0<=e<=981106<R+1. In particular there is no unjustified |U|>=m gate.

Put Z=R+1. On0<=e<=Z, the derivative of e*(Z-e)^10 is
(Z-e)^9*(Z-11e). Therefore the continuous maximum is

    e*(Z-e)^10 <= Z^11*10^10/11^11.                  (PEAK)

This is a universal analytic inequality, not an enumeration of possible
core unions. Combining (CUM), (PENCIL-GAIN), (U-LIST) and (PEAK) gives

    N+near <= floor(W/3+n_max + (Z^11*10^10/11^11)
                   *(1/(2*d^10)+1/(6*(d-1)^10)))+near
      =228260637755610995.                            (PENCIL-PRICE)

The preferred-slope charge n_max is essential to the argument, even though
it is numerically small. The existing F17 ownership control has U=D and
all twelve low labels preferred; dropping them would give G<=0 falsely.

## 4. Empty Or Singleton Family And The Original Source

If P_2 is empty, (CUM) gives N<=W/3. If it is a singleton, each low
label has a defect, and the same-pair disjointness in section1 bounds all
low labels by n-|H_f|<=n_max. Hence N<=W/3+n_max. Including near,
this gives208124644263878102, smaller than both branch prices.

The direction space has function-field rank zero only in this singleton
case, rank one in section3, or rank two in section2. Taking the maximum
of exhaustive WHOLE-source alternatives proves (PAY), not their sum.

The original assembly preserves every finite label and includes near at
most once. Therefore an over-budget original line cannot admit any valid
selection/minimizer assignment with pair affine dimension<=10. Every such
assignment on every rank-twelve normalization in the remaining interval
must have dimension>=11. No canonical-maximization premise was needed.

This narrows actual low-defect source geometry, not the list of possible
J-values. It neither bounds the full-dimensional pair census nor asserts
that all original error ranks are at most twelve. The router stays TARGET;
the two Prize problems remain open.

## 5. Every Nonconstant Low-Pair Pencil Is Already Paid

In section3 all pair differences lie in V x V. The parameter direction
space is therefore contained in

    W_H={H: A0*H in V and A1*H in V}.

The required pencil theorem proves dim W_H<=dim V-1=10 when the
primitive direction is nonconstant (h>=1). Both row entries are then
nonzero. If dim W_H=11, their multiplication maps would be isomorphisms
onto V and multiplication by the nonconstant rational ratio A1/A0 would
preserve V. Repeated multiplication forces unbounded denominator divisibility
or polynomial degree in a fixed nonzero finite-dimensional polynomial
space, impossible. Thus (PAY) applies without an extra affine-rank premise
for every nonconstant-direction P_2 pencil.

For a constant direction, one row entry is a nonzero scalar, so parameter
dimension is at most dim V=11. The rank<=10 alternative is paid; only
actual rank11 remains. Function-field rank zero was already paid, leaving
exactly the two necessary over-budget alternatives stated in statement.md.
This does not assert that a full-rank constant-direction pencil is affordable
or that its relevant complete-core union is small.
