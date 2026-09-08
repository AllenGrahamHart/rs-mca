# Proof By One Weighted Resource And Exact First-Coordinate Counting

## 1. Pay The Existing Exceptional Set Once

Use the required secant theorem's explicit E, including nonuniversal
carrier-zero agreeing labels. Every independent agreeing tuple outside E
has distinct nonzero source fibers. Tuples owned by different labels are
disjoint. Nonnegative weighting preserves this disjoint-resource argument.

The number of such ordered tuples is bounded by the proved Bonferroni
polynomial U(n,r,A,T). The sum of sum_(x in tuple) w_x over ALL ordered
distinct-coordinate r-tuples is exactly

    r*T*(n-1)_(r-1):

choose a marked position, its coordinate x and its weight, then the other
coordinates. Restricting to independent, distinct-fiber or agreeing tuples
can only decrease this nonnegative sum. Thus the augmented resource is
at most U+lambda*r*T*(n-1)_(r-1).

Subtract(n)_r, factor T*(n-4)_(r-4), and the remaining coefficient is

    -binom(r,2)(n-2)(n-3)
    +3binom(r,3)(A-2)(n-3)+3binom(r,4)T
    +lambda*r*(n-1)(n-2)(n-3).

It is<=0 by CREDIT and T<=Tstar. The T=0 case is equality. This proves
the resource bound without requiring the augmented polynomial to decrease
everywhere: the displayed bound relative to its T=0 value suffices.
The discount from forbidden same-fiber tuples pays the coordinate weight.
It is not an independent additional budget available for other records.

## 2. Bound The Full Source Collision Statistic

All carrier-zero points are roots of every polynomial in V. Dividing V
by their full locator gives dimension s, degree<K-z and n-z nonzero
evaluations, with positive gap n-K. This is ONLY an auxiliary polynomial
moment calculation, not receiver descent or removal of exceptional labels.
Apply the full-fiber contraction supplier's second-moment inequality and
subtract n-z. Monotonicity in n-z and K-z gives

    T<=max(n*(K-s)/(s-1),(K-s+1)(K-s)).

T is an integer, so take its floor. If K=s both branches vanish. Otherwise
the stated n gate makes the first branch at least the second. Source
weights are defined before any core, explanation reselection or exceptions.

## 3. Collision Mass Forces Marked Core Bases

Every core fiber is contained in a single complete source fiber. Hence
w_x>=c_j-1 on a core fiber of size c_j and sum_(x in core)w_x>=C.
Fix a first coordinate x in that fiber. Exact full-fiber contraction
counts its ordered basis completions by B_(s-1) on the quotient of that
entire CORE fiber. Its degree is K-c_j, gap D, and original-rank profile
is inherited. Since c_j<=h, its count is at least F(K-c_j)>=F(K-h)=G.

The sum of the first-coordinate weights over all ordered core bases is
therefore at least G*sum_(x in core)w_x>=C*G. Ordered-basis symmetry
gives exactly s times this sum for the sum of weights in every position,
proving MARKED. This does not suppose that fiber sizes are equal or that
the larger SOURCE fibers fit inside the core.

The existing first-step Jensen argument gives the unweighted count
M*F(K-S2/M)=M*F(K-1-C/M), using the SAME frozen remaining profile.
For a LOW full-code-bad record select one actual defect from its witness.
Inserting it in r recoverable positions gives r distinct copies of each
ordered core basis. The added coordinate's weight is nonnegative, so
the resulting tuple weight is at least r times the weighted core-basis
count. All points still agree with the SAME selected explanation; core
points outside the old witness are allowed by the completed-basis supplier.
This proves COST and the alternative using any other unweighted bound.
No step in this core-counting argument uses CREDIT; these lower bounds
and their tangents hold for every lambda>=0. Only section1 used that
sufficient resource guard, which an independently proved resource bound
for the same weights may replace.

## 4. Tangents And Whole Boxes

The inherited product F is increasing and convex on x>=1. Its tangent
at x0=K-1-C0/M gives

    M*F(K-1-C/M)>=M*F(x0)+F'(x0)(C0-C).

Add lambda*s*C*G and use the correct endpoint for its linear coefficient.
This is TANGENT. In particular a negative coefficient cannot be multiplied
by a lower C. The argument does not assume an optimized basis-envelope
curvature: it uses the explicitly proved fixed polynomial F.

On K0<=K<=K1, M=D+K>=M0 and C>=0 imply
K-1-C/M>=K0-1-C/M0. Where the latter is>=1, positivity and monotonicity
give M*F(K-1-C/M)>=M0*F(K0-1-C/M0). Also K-c_j>=K0-h1, giving
the uniform G=F(K0-h1). The profile is calibrated once for the original
rank and degree/density box, not recalibrated at a real argument.

For a source box n0<=n<=n1, a uniform maximum fiber A1 and uniform
collision cap T1, one may take the nonnegative rational

    lambda=[binom(r,2)(n0-2)(n0-3)
       -3binom(r,3)(A1-2)(n1-3)-3binom(r,4)T1]
       /[r(n1-1)(n1-2)(n1-3)],                       (BOX-CREDIT)

when its numerator is nonnegative. The positive term is bounded below
at n0, all subtracted terms above at n1,T1; the denominator is bounded
above at n1. Therefore it satisfies CREDIT for every actual source in
the box. A source T1 from SOURCE is monotone in its nonnegative n,K
arguments; the rank and branch guards must still be checked.

One lambda is fixed for ALL labels on that source. Tangent calibration
may vary between record types, because each gives a lower cost in the
same weighted resource. HIGH record costs remain valid without a bonus.
The finite total divides the shared resource by the smallest applicable
record cost and adds the single exception allowance and original near once.
No full row, endpoint or unrestricted rank theorem follows from the
symbolic weighted lemma alone.
