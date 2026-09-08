# Proof By A Quantitative Hereditary Moment

## 1. The Capped Moment Without An Exact Balance Assumption

For a rank-r polynomial space of degree <k and length n>k, order its
nonzero projective fiber sizes a_i decreasingly. Write m=r-1 and
x=a_m. Polynomial roots give sum_(i=1)^m a_i<=k-1. There are at least
r fibers, since the evaluations span the dual. If every fiber is <=A,
then the same nonnegative excess calculation as in the balanced supplier
gives

    S_2=sum_i a_i^2 <= n*x+A*(k-1-m*x).

When n-m*A>=0, use x<=(k-1)/m. Otherwise use x>=0. In both cases,

    S_2 <= (k-1)*max(n/m,A).

In particular, m*A<=lambda*n and lambda>=1 imply
S_2<=lambda*n*(k-1)/(r-1). No independent maxima of all fiber sizes
or omission of the joint top-fiber constraint is used.

## 2. The Same Loss Factor At Every Actual Descendant

Contract any complete original rank-j flat of size b, where r=s-j>=3.
Full-locator division of its annihilator gives actual rank r, degree
k=K-b, length n=N-b and unchanged gap D. Every child fiber lifts to
an original rank-(j+1) flat containing ALL b removed coordinates, so

    (r-1)*fiber_size
       <=(s-j-1)*(j+1)*h-(r-1)*b
       <=lambda*N-(r-1)*b
       <=lambda*(N-b).

The last step uses r-1>=2>=lambda. The original zero flat j=b=0
is included. Further full-fiber contractions remain complete original
flats, so the SAME lambda works throughout the actual contraction tree.
Section 1 proves its quantitative moment at every rank >=3.

Rank two is handled separately: every fiber has size <=k-1, so its
ordered basis count is n^2-S_2>=n*(D+1). Rank one has exactly n bases.
There is no need to impose the rank>=3 moment argument at rank two.

## 3. Convex Product Induction

The displayed product has factors D+1+alpha*(x-1), with alpha in [0,1]
because lambda<=2 and every denominator j>=2. Its polynomial in x-1
has nonnegative coefficients. It is positive, nondecreasing and convex
for x>=1. Each alpha is nonincreasing in lambda, proving that monotonicity.

Induct on rank in the actual descendants. Exact fiber contraction gives

    B_r >= sum_i a_i F_(r-1)(D,k-a_i;lambda)
        >= n F_(r-1)(D,k-S_2/n;lambda)
        >= n F_(r-1)(D,1+(1-lambda/(r-1))*(k-1);lambda)
         = F_r(D,k;lambda).

The first average is over actual integer child degrees >=r-1. Jensen
therefore uses arguments in the proved convex domain. The final relaxed
argument is >=1, even when it is below the actual child rank; no polynomial
source at that fractional or smaller degree is asserted. Rank two uses
its separate seed, avoiding a negative contraction coefficient.

Unrolling the affine contractions gives the printed product. At lambda=1,
the internal product telescopes to (a-1)/(s-1), exactly recovering the
balanced product. The proof imports the existing exact full-fiber geometry
and root constraints, not an assumed curvature of an optimized envelope.
