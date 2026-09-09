# Induction On The Ambient Affine Dimension

Write Z=f_*+W and r=dim_F W. For direction rank zero or one, (AFF)
is exactly (PC), including the dimension-zero case. For direction rank
two, r>=2. Choose two directions with nonzero polynomial determinant.
By the required joint-incidence proof, its roots E_bad have size
e<=2K-2<A, and evaluation W -> F^2 has rank two elsewhere.

At each good coordinate x, the joint agreement section Z_x is empty or
an affine space of dimension r-2. By induction, |S intersect Z_x| is at
most P^(r-2). The section condition (PC) is inherited because any affine
pencil subspace inside a child is also one of the original allowed Z.

Every member of S intersect Z has at least A-e good agreements. Counting
pair/good-coordinate incidences gives

    (A-e)*|S intersect Z| <= (n-e)*P^(r-2).

The ratio (n-e)/(A-e) is nondecreasing in e, so replacing e by
2K-2 proves (TWO). Since H<=P^2, (TWO) implies (AFF) and completes
the induction. No rank-two hypothesis on any child was used.

All agreement counts remain on the original domain. Restricting which
coordinates may anchor the count does not puncture polynomials or change
their original degree, agreement threshold, receiver or MCA labels.
