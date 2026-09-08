# Proof By Rank-Specific Hereditary Moments

Use the complete-flat contraction and capped-moment argument of the
quantitative-density supplier. For a rank-r descendant with degree <k,
length n=D+k and largest projective fiber <=A,

    S2 <= (k-1)*max(n/(r-1), A).                    (1)

## 1. A Uniform Coefficient For Each Rank

A descendant of rank r is obtained by contracting an actual complete
original rank-j flat, j=s-r, of size b>=j. Its degree k=K-b and length
n=N-b; its fibers lift to rank-(j+1) original flats. Hence

    A <= (j+1)*h-b,  A <= k-r+1.

Since k<=K1-j, and the ratio (k-r+1)/(D+k) is nondecreasing in k,

    A/n <= (K1-s+1)/(D+K1-s+r).                  (2)

Write c=(j+1)*h. If c<N, the function (c-b)/(N-b) is nonincreasing
in b. Thus b>=j and K>=K0 imply

    A/n <= (c-j)/(N-j) <= (c-j)/(D+K0-j).

The last numerator is positive because h>=1. Together with (1) this
gives the density entry in the minimum defining mu_r.
If c>=N, that entry is at least one, whereas (2) is strictly below one,
so (2) alone gives the same minimum. Substituting the resulting fiber
bound into (1), in ALL cases and at EVERY actual descendant,

    S2/n <= mu_r*(k-1).                            (3)

The outer maximum is at least 1/(r-1). Its root-density entry is strictly
less than one, as is 1/(r-1). Thus 0<1-mu_r<=1.
No common worst-case lambda is carried through all ranks.

## 2. Product Induction With A Frozen Profile

Fix the entire profile above. Define F1(D,x)=D+x,
F2(D,x)=(D+x)*(D+1), and for r>=3 define

    Fr(D,x)=(D+x)*F_(r-1)(D,1+(1-mu_r)*(x-1)).

Each Fr is a positive polynomial in x-1 with nonnegative coefficients,
so is nondecreasing and convex on x>=1. At rank two, root capacity gives
the separate bound B2>=n*(D+1); rank one has exactly n bases.

For each rank-r actual descendant, exact full-fiber contraction and Jensen
give, using the SAME remaining rank profile for all its actual children,

    Br >= sum_i a_i*F_(r-1)(D,k-a_i)
       >= n*F_(r-1)(D,k-S2/n)
       >= n*F_(r-1)(D,1+(1-mu_r)*(k-1))
        = Fr(D,k).

Actual child degrees are >=r-1. The final relaxed argument is >=1,
within the convex domain, without asserting a fractional-degree source.
At the root Fs(D,K)>=Fs(D,K0). Unrolling proves (PROFILE).

## 3. Comparison With The Earlier Quantitative Product

Take K0=K1=K and a valid old lambda in [1,2]. For r>=3,
(r-1)*(j+1)<=floor(s*s/4), so c/N<=lambda/(r-1)<=1.
If c<N, subtracting j lowers its ratio, giving
(c-j)/(N-j)<=c/N. The same holds at c=N by equality.
Consequently mu_r<=lambda/(r-1), since lambda>=1.
Each contraction coefficient in the new product is therefore at least
the old coefficient. Product monotonicity proves the comparison.

All quotient geometry and (1) are credited inputs. The refinement is
the separate hereditary coefficient at each rank and its uniform degree
box, not a new root theorem or an assumed shape of an optimized envelope.
