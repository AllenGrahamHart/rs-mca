# A Branch-Weighted Budget For Nonbirational Inner Centres

Let C subset P^r be a geometrically integral rational curve of degree d,
nondegenerate, with r>=3. Work in characteristic0 or characteristic p>d.
Projection from a general smooth point of C is birational onto its image.

For any geometric inner centre P whose projection has degree mu_P>=2,
let b_P be its geometric branch count. The set of such centres is finite,
and

    sum_P binom(b_P+mu_P-1,2) <= G=binom(d-r+1,2).       (SEGRE BUDGET)

For any h>=2, their mu_P>=h subfamily has at most floor(G/binom(h,2))
centres and total branch count at most floor(G/(2h-3)). If C is covered
by the primitive original polynomial map of normalization degree nu, its
ACTUAL evaluation coordinates over those centres number at most

    nu*floor(G/(2h-3)).

This is a branch-weighted coordinate bound, NOT nu times the centre count.
A sharper bound uses B=d-h*(r-1). If B<1 there are no such centres.
Otherwise put b0=min(B,max(1,h-2)); the coordinate bound improves to

    nu*floor(G*b0/binom(b0+h-1,2)).                     (BRANCH CAP)

These bounds may be too large to fit a particular anchor budget. No
uniform affordability, free anchor selection or MCA row payment is asserted.
Characteristic and singular-branch guards are essential.
