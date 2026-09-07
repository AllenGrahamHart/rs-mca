# Maximum-margin selection and complete-core compatibility

Status: PROVED. Fix n distinct field points, degree bound K, m=K+d,
an affine explanation carrier h_*+V, and a finite set Gamma of labels
each admitting an exact size-m full-code-bad support with explanation
in that carrier. Here h_* has degree <K, V is a subspace of the
degree-<K polynomials, and an allowed pair means a in h_*+V and b in V.
Raw means the untruncated minimum mismatch of the
second receiver to b in V on that support.

For each label maximize raw over ALL such supports and ALL explanations
in the fixed carrier, and choose one maximizer. The attained raw values
are nonempty and contained in the finite integer set {1,...,m};
no efficient computation is asserted. For 1<=T with 2T<d, call a label
low if its maximal raw r_gamma<=T. Let

    A_gamma={x:u(x)+gamma v(x)=h_gamma(x)}.

Then there is a UNIQUE b_gamma in V with at most T mismatches on
A_gamma. For f_gamma=(h_gamma-gamma b_gamma,b_gamma), its COMPLETE
pair core H_gamma satisfies

    A_gamma=H_gamma disjoint_union D_gamma,
    |D_gamma|=r_gamma,
    D_gamma subset S_gamma.

Every set D_gamma plus m-r_gamma points of H_gamma is a maximizing
full-code-bad support for this explanation.

More generally let f=(a,b), f'=(a',b') be ANY allowed polynomial pairs
with complete cores of size >=m-T. If

    f'-f=(alpha P,beta P), P!=0, beta!=0,

then gamma=-alpha/beta cannot be a canonically low label. Consequently,
at a low cross-core incidence x in H_f' minus H_f, the two difference
polynomials a'-a and b'-b are F-linearly independent (rank TWO).

The guard 2T<d and maximizing the support are essential. Small exact
controls show both failures when omitted, and also actual zero/cyclic
full row spaces with canonical low rank-two cross incidences surviving.
