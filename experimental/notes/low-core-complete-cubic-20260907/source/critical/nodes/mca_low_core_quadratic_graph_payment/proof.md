# Proof

The common matrix and polynomial offset send the pair family into
(a_0+V) x (b_0+V). Both component degrees remain <K. Complete pair
cores are unchanged because the matrix is invertible at every point.
Let w be the first transformed received coordinate. Each transformed
first polynomial agrees with w at every point of its complete pair core.
The identity b=a^2 makes projection onto the first polynomial injective
on the represented pairs.

## 1. The quadratic locus has dimension at most half the carrier

Extend scalars to an algebraic closure k. In the affine s-space a_0+V
consider

    X={a: a^2 belongs to b_0+V}.

Membership in b_0+V is a system of linear coefficient equations on a^2,
so X is defined by finitely many quadrics in the s coefficients of a.
There may be many coefficient equations; their number is not used.

Let Y be a positive-dimensional irreducible component of the REDUCED
locus X, and let D be the largest polynomial degree attained on Y.
Choose a point a of Y of degree D. Every polynomial in Y has degree
<=D, so its tangent vectors at a are polynomials w satisfying

    w in V, deg w<=D, a*w in V.                          (1)

The last inclusion follows by differentiating a^2-b_0 in V and using
char F!=2. The tangent dimension is at least dim Y; smoothness or a
separable projection of Y is not needed for this inequality.

Let W be the vector space in (1), of dimension t. If D=0, then t<=1.
If D>0, row reduction by polynomial degree gives t distinct leading
degrees S in [0,D] for W. Since W and aW are both subspaces of V,
the leading-degree set of V contains both S and D+S. These two sets
intersect in at most the single degree D. Hence

    s >= |S union (D+S)| >= 2t-1,
    dim Y <=t<=floor((s+1)/2)=r.                         (2)

Leading-degree sets of the fixed polynomial space V are unchanged by
scalar extension. A component consisting of the zero polynomial or any
other isolated point has dimension zero and also satisfies the bound.
This proves dim X<=r for every component, not merely for a sampled
generic polynomial. Using unrelated component spaces would invalidate
the common leading-degree count.

## 2. Count pairs, then original slopes

The proved companion `algebraic_list_bound.md` covers X by a reduced
pure r-dimensional coefficient variety of degree <=2^(s-r). Its LIST
incidence bound at agreement A=m-T therefore gives

    M <= floor(2^(s-r)*((n-K+1)/(m-T-K+1))^r).

Every represented LOW pair has complete core size >=m-T, so its first
polynomial is in this scalar list. Injectivity of projection proves (QG).
No scalar-image family is substituted for joint pairs without this
injectivity and the quadratic-locus restriction.

Return to ORIGINAL pair coordinates. For a fixed pair f=(a,b), every
assigned selected scalar support contains at least one point outside
H_f, since the full support is pair-bad. At any such point, scalar
agreement is (u-a)+gamma*(v-b)=0 and holds for at most one finite
gamma. Thus the assigned labels consume disjoint noncore coordinates:

    number of LOW labels assigned to f <=n-|H_f|<=n-m+T.

Summing gives L_LOW<=(n-m+T)*M. The original truncated-margin resource
has theta=raw on LOW and theta>=T+1 elsewhere. Consequently

    |Gamma| <=C_s/(T+1)
                 +sum_LOW(1-raw/(T+1))
             <=C_s/(T+1)+L_LOW.

This proves (PAY), including all high labels. In particular, coordinates
inside other pair cores are counted; replacing n-|H_f| by n-|U| would
be false. No nonlinear map is applied to the MCA challenge itself.
