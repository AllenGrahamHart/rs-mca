# Full Projection Multiplicities Consume The Genus Budget

Let C subset P^r be geometrically integral, rational and nondegenerate,
of degree d, with r>=3, in characteristic0 or characteristic p>d.
For an inner centre P let mu_P be its inner-projection degree and m_P
the degree of the FULL fixed divisor on the normalization. Then

    sum_(mu_P>=2) binom(m_P+mu_P-1,2)<=G=binom(d-r+1,2).

This strengthens the branch-count budget: m_P>=b_P includes singular
branch multiplicity, not only the number of branches. The actual
normalization-cover degree nu still bounds coordinates by nu*b_P<=nu*m_P.
No actual coordinate is counted m_P times by equality.

For a curve in P3, write d=m+mu*eta at such a centre; eta>=2 is its
plane inner-image degree. The exact universal pricing inequality is

    nu*m*binom(d-2,2)/binom(m+mu-1,2) <= (eta-1)*nu*d.

Thus a degree-dependent extra cost can be summed against one shared
genus budget. Generic projections used in the proof are geometric
counting devices, not substitutes for original-domain anchors.
