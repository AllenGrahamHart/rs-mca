# Proof

For every low record, scalar agreement on its selected size-m support
means that v=b_gamma implies u=a_gamma. Hence the intersection of
that support with its joint core is exactly {v=b_gamma} on the support,
including at gamma=0. Its complete core has at least m-raw_gamma>=m-T points.
For two low records, both cores lie in U_T, so

    |H_gamma intersect H_eta|
      >= 2(m-T)-|U_T| >= K.

Both degree-<K components of the two polynomial pairs agree on this
intersection. Polynomial uniqueness identifies the pairs. Hence all
low records use one pair (a,b), whose COMPLETE core H has size >=m-T.

Every selected support for that pair has a point outside H, by its
same-support pair noncontainment. Such a point satisfies

    (u-a)+gamma(v-b)=0.

Here v-b cannot vanish, since then u-a vanishes too and the point is
in H. It determines gamma uniquely. Distinct selected labels therefore
own disjoint nonempty outside sets, so the low count L is at most
n-|H|<=n-m+T. This reasoning uses complete cores, not selected support
subsets, and also covers H of size >=m.

Each low record contributes theta>=1 to the margin resource; every
high record contributes theta>=T+1. Consequently

    L+(T+1)(|Gamma|-L)<=C,
    |Gamma|<=L+floor((C-L)/(T+1)).

Also L<=C. The last integer expression is nondecreasing in L, so use
L<=M=min(C,n-m+T). If the low family is empty, the direct bound
floor(C/(T+1)) is covered by the same monotone expression at M.
This proves the full selected-family bound.

## Sharp pair-overlap control

Over F_7 on D={0,1,2,3}, put K=2, d=T=1, m=3,
C'=span{1,X}, h_*=0, and

    u=(0,0,0,3), v=(0,0,2,0).

For gamma=0 choose h=0, support {0,1,2}, minimizing b=0.
For gamma=1 choose h=X, support {0,2,3}, minimizing b=X.
Both raw margins are one: no affine polynomial fits v on the selected
three points, but each chosen b fits two. Thus both supports are
pair-noncontained. The minimizing pairs are (0,0) and (0,X), with
complete cores {0,1} and {0,2}. Their union has size three, exactly
2(m-T)-K+1, and their intersection has size K-1. The pairs differ.
The displayed overlap threshold, not the entire numerical payment,
is sharp under these hypotheses.
