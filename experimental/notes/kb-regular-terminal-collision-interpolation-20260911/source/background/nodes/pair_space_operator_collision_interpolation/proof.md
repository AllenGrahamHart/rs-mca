# Charge Interpolation Conditions To Disjoint Actual Pairs

For each retained evaluation point p choose a coordinate attaining r_p and
its r_p agreeing actual pairs. For any two of these pairs, the nonzero
parameter difference y has y(x)=T(y)(x)=0. It is not an F-eigenvector,
since eigenpolynomial roots were removed. Thus y,T(y) are F-independent.
Their common annihilator in U* is one-dimensional, uniquely identifying p.

The same unordered pair cannot therefore occur in the chosen sets for two
different p. Their binom(r_p,2) pairs are disjoint subsets of the binom(M,2)
available pairs. This proves PAIR OWNERSHIP even when joint evaluation has
rank one, when several coordinates have the same p, or when the actual
family does not fill its affine enclosure.

## Interpolate With Multiplicity, Then Pull Back

In the vector space of homogeneous degree-ell ternary forms, impose
vanishing to order w_p at each retained p. In a projective affine chart
this asks that all Taylor coefficients of total degree<w_p vanish, at
most binom(w_p+1,2)=binom(r_p,2) linear conditions over F. Use coefficient
conditions, not ordinary derivatives, so no characteristic restriction arises.

The substitution map P->P(u0,u1,u2) has rank H_U(ell). Since this exceeds
the total number C of conditions, their common solution space cannot be
contained in its kernel. There is a form P satisfying all conditions whose
univariate pullback Q is NONZERO, of degree<=D*ell.

For x mapping to p, choose a basis polynomial uj with uj(x)!=0. The
affine coordinate differences ui/uj-ui(x)/uj(x) vanish at x. The Taylor
conditions imply Q=P(u)=uj^ell*P(u/uj) has a zero of order at least w_p
there. This remains true at singular image points and ramified parameter
values. Summing multiplicities over distinct domain coordinates gives

    sum_x max(c_x-1,0)<=sum_(p,x over p) w_p<=deg Q<=D*ell.

Coordinates with c_x<=1 need no condition. Since c_x<=1+max(c_x-1,0),
the total remaining core incidence is<=n+D*ell, even if E is padded back
by zeros. Restoring its incidence B gives M*A<=B+n+D*ell.

The product-rank formula is proved in product_rank.md. Replacing this rank
by the dimension binom(ell+2,2) of all ternary forms would be invalid:
the interpolant could vanish IDENTICALLY on the image. The conic control
demonstrates exactly that failure. Original owner weights are not changed.
