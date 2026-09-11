# Couple Actual Pair Ownership To The Finite Domain

The required actual-collision theorem proves C<=P. At each p with r_p>=2,
choose one coordinate attaining r_p and its actual agreeing pairs. A pair
difference is not an F-eigenvector outside E, so y,T(y) are independent
and determine p uniquely. Distinct chosen groups therefore own disjoint
unordered pairs. The cases r_p=0,1 use no pair budget.

The geometric claims l_p<=nu*b_p and sum binom(b_p,2)<=g are proved in
normalization.md and branch_budget.md. These count ALL geometric branches,
including branches not rational over F; restricting to actual F-coordinates
can only decrease l_p. Put n'=sum l_p<=n. The actual incidence obeys
S<=sum l_p*r_p, even when different coordinates in one fibre have different
received values or different agreeing groups.

Write r_p=1/2+(r_p-1/2). Weighted Cauchy--Schwarz gives

    (sum l_p*(r_p-1/2))^2
      <= (sum l_p*b_p)*(sum (l_p/b_p)*(r_p-1/2)^2).

The first factor is at most

    n'+sum nu*b_p*(b_p-1)<=n'+2*nu*g.

For the second, use (r-1/2)^2=r*(r-1)+1/4 and l_p/b_p<=nu:

    sum (l_p/b_p)*(r_p-1/2)^2 <=2*nu*C+n'/4.

Taking the positive square root bounds sum l_p*r_p from above by
n'/2+sqrt((n'+2*nu*g)*(n'/4+2*nu*C)). This expression increases with
n'>=0 and C>=0. Padding from n' to n and then C to P proves BRANCH ENERGY.

The original cores give S>=M*A-B. If Z>0, squaring this positive lower
bound against BRANCH ENERGY yields Z^2<=(n+2*nu*g)*(n+8*nu*P).
The strict reverse is impossible. The positive-Z guard is indispensable.

Unlike interpolation with only a condition-count budget, this argument
also uses sum l_p<=n. Many fibres cannot simultaneously fill a large
polynomial degree allowance when there are too few domain coordinates.
It retains original assignments, actual pair membership and all finite
exceptional fibres. It neither fills formal hulls nor changes source degrees.
