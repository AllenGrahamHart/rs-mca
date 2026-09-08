# Coordinate-Weighted Collision Credit On The Same Tuple Resource

Status: PROVED by the hand argument; external independent review remains due.

Use the selected full-code-bad polynomial source of the projective-fiber
secant theorem, with actual carrier dimension s>=3, r=s+1, n>=r,
empty universal carrier core and z carrier-zero coordinates. Nonzero
source fibers have sizes a_i<=A, A>=2. Set

    T=sum_i a_i(a_i-1), 0<=T<=Tstar,
    w_x=a_i-1 on the i-th nonzero fiber, w_x=0 on carrier zeros.

Thus sum_x w_x=T. An ordered coordinate tuple receives weight
1+lambda*sum_(x in tuple) w_x, where lambda>=0. If

    lambda*r*(n-1)(n-2)(n-3)
      <=binom(r,2)(n-2)(n-3)
         -3binom(r,3)(A-2)(n-3)-3binom(r,4)Tstar,       (CREDIT)

then, outside the SAME secant/zero-label exceptional set of size<=z+T/2,
the TOTAL weighted independent-tuple resource is at most(n)_r. No second
tuple budget, independent per-core resource or extra near event is added.

For polynomial degree<K and n>K>=s, one may always take

    Tstar=floor(max(n*(K-s)/(s-1),(K-s+1)(K-s))).       (SOURCE)

In particular the first branch suffices when n>=(s-1)(K-s+1).
This is a source theorem; it does not assume favorable receiver colors.

## A Collision-Rich Core Pays More In This Resource

Consider one M=D+K point nonzero joint core, D>=1, K>=s, actual rank s,
with proper-flat density<=h, h>=1 and K-h>=1.
Let C=sum_j c_j(c_j-1) be its OWN ordered same-fiber
pair count, where c_j are restricted core fiber sizes. Freeze the original
rank-s hereditary profile. Write F(x)=F_(s-1)(D,x) for the corresponding
positive convex polynomial. For G=F(K-h), the sum over ordered core bases
of their coordinate weights is at least

    s*C*G.                                           (MARKED)

Each LOW record therefore owns weighted r-tuples of total weight at least

    r*[M*F(K-1-C/M)+lambda*s*C*G].                    (COST)

MARKED, COST and TANGENT hold for every lambda>=0. CREDIT is only the
preceding sufficient condition for the resource upper bound, not a
hypothesis of these core-counting inequalities. A separate proved bound
on the SAME weighted source resource may replace that sufficient condition.

Any other proved unweighted core-basis lower bound B may replace the first
term. If C>=Cmin, it also gives r*(B+lambda*s*Cmin*G).
The r positions of one actual witness defect remain recoverable; its
nonnegative weight is not needed for these lower bounds.

For Cmin<=C<=Cmax and any C0 such that x0=K-1-C0/M>=1, a uniform lower
bound for COST/r is

    M*F(x0)+C0*F'(x0)
      +(lambda*s*G-F'(x0))*C_endpoint,                (TANGENT)

where C_endpoint=Cmin for a nonnegative coefficient and Cmax otherwise.
The actual and relaxed arguments must remain in x>=1. Multiple proved
tangents and other lower counts combine by maximum for the SAME record.

For whole boxes, use the fixed original profile, M0=D+K0, K0 and
G=F(K0-h1). A valid Cmax and K0-1-Cmax/M0>=1 make the same formula
uniform. SOURCE and CREDIT also admit endpoint bounds as proved below.

This lemma supplies a weighted resource and record costs, not a numerical
row payment. A finite consumer must cover all cores, HIGH records, source
alternatives and the original near/source transport. The weights and lambda
are fixed for a source, never selected independently by each label or core.
