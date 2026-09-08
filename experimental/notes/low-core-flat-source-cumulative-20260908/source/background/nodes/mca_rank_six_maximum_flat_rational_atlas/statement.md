# A Small Rational Atlas For Maximum-Density Rank-Six Flats

Status: PROVED by the self-contained hand argument; external review remains due.

Let V<=F[X]_(<K) have actual dimension11, K>=26, and let H be M>K
distinct field points with every V-evaluation nonzero. Let h be the
maximum coordinate density over proper evaluation flats, and assume

    h>(K-4)/7.

Let A be the family of COMPLETE rank-six H-flats attaining that maximum.
All members have the same integer cardinality a=6h. The family may be empty.

1. Distinct members span V*. Their evaluation-subspace intersection has
   dimension one and their coordinate intersection has size<=h. Their
   annihilator spaces W_A={v in V:v|_A=0} have dimension5 and intersect
   pairwise only in zero.
2. If 36h>M, the number L of members satisfies

       L <= 5M/(36h-M).                                (PACK)

3. Fix any two members A,B and write P_A,P_B for their full monic locators,
   U_A=W_A/P_A, U_B=W_B/P_B, k=K-a. Put U=W_A+W_B, of dimension10.
   For every other member C, d_C=dim(W_C intersect U) belongs to{4,5}.
   There is a coprime pair of nonzero polynomials (f_C,g_C), unique up to
   a common nonzero field scalar, and a d_C-dimensional polynomial space T_C,
   such that

       W_C intersect U=(P_A*f_C+P_B*g_C)*T_C,
       f_C*T_C<=U_A, g_C*T_C<=U_B,
       deg f_C, deg g_C <= k-d_C.                      (RATIONAL)

   Different C give different projective rational directions [f_C:g_C].
   No denominator-root deletion is involved. In particular, if G_C is the
   monic gcd of T_C, then

       P_C divides (P_A*f_C+P_B*g_C)*G_C,
       deg G_C <= min(k-deg f_C,k-deg g_C)-d_C.         (LOCATOR)

The proof also establishes a more general three-flat lemma: for complete
rank-six flats A,B,C whose subspaces span V* pairwise, put a=|A|, b=|B|,
c=|C|, k_A=K-a, k_B=K-b. If

    |C outside (A union B)| > k_A+k_B-2,

then the same rational conclusion holds with component degree bounds
k_A-d_C and k_B-d_C. Here K>=11 suffices; this version requires neither
maximal density nor the K>=26 guard used to deduce its root inequality.

## A Quantified Near-Maximum Band

More generally, fix an integer b with6<=b<=6h and

    2b-5h>K-4.

Then ALL complete rank-six H-flats of size at least b have pairwise full
joins and the same two-anchor rational conclusion. For anchors A,B the
component bounds are K-|A|-d_C and K-|B|-d_C, hence at most K-b-4.
If b^2>Mh, their number is at most M(b-h)/(b^2-Mh).
The finite caps25/17 above are for the EXACT maximizing family; they must
not be assigned automatically to this larger band.

## The Current LOW-Core Specialization

For one fixed empty-universal-core normalized KoalaBear source, take the
actual M=J+67466 nonzero joint-core coordinates used by the raw<=6
basis count, with K=J. Density is measured on THIS core, not the whole
domain of size1048576+J. If h>(J-4)/7, every maximizing proper flat has
rank<=6. The rank-six subfamily above has at most25 members on
20481<=J<=22999, and at most17 on22500<=J<=22999.
Every rational direction in its two-anchor atlas has component degrees
at most3284 throughout the former interval.

This is a per-core structural theorem, not a selected-label count.
Different labels can have different cores and different anchors. No factor25
or17 may multiply a source or child payment without a new same-source
ownership/counting theorem. Ranks1..5, flats outside the explicit band,
the remaining J interval, unrestricted MCA/LIST and both Prizes remain open.
