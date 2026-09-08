# One geometrically integral quartic is the next obstruction

HISTORICAL DICHOTOMY: `quartic_strip_payment.md` now closes the whole
8764..9526 residual. Sections 1--5 below remain an independent proof
of the original <=64-off-pair factor dichotomy, and supply that closure.
They do not use the new multiplicity theorem or the closure in reverse.
The remaining normalized interval now starts at 9527. The scope notes
and residual descriptions below record the preceding stages.

Current scope note: `low_cutoff_strip.md` now pays every source through
8763 using a different cutoff. This older LOW_500 dichotomy remains true
on 8656..9526, but only 8764..9526 is still an unpaid interval portion.

Status: PROVED. On the EXACT canonical normalized source with
8656<=J<=9526, at least one of the following holds:

1. N=|Gamma|+134944<=274979661975561635<B=274980728111395087,
   with reserve at least 1066135833452.
2. All but at most four represented LOW pairs lie on ONE geometrically
   integral quartic over F(X), a primitive factor of the full interpolation
   kernel's gcd and of weighted degree <J+66972 for weights (1,J-1,J-1).
   It is not of the form x*y^3=R!=0 after an invertible constant F-matrix
   on the pair variables and fixed rational X offsets.

On the currently unpaid 8764..9526 portion, the stronger multiplier
conclusion in section 7 gives off-pair limits 0/1/2/3/4, the precise
leading-height envelope and the additional projection-graph exclusions.
On the already paid 8656..8763 portion, alternative 1 holds by the
LOW-101 theorem, so no extra quartic assertion is needed there.

Thus a source exceeding the budget must have the second description.
This is a proved necessary restriction, not a proof that such quartics
are affordable or do not occur. No new speculative conditional node is
introduced. The entire interval through 8655 remains paid; the new 871
J-values have a sharply smaller residual, not whole-interval closure.

## 1. The full kernel forces degree at most four

Put A=J+66972, w=J-1, n=1048576+J. Use the ENTIRE interpolation
kernel E in W8 on the complete LOW joint-core union, as in the earlier
cubic proof. Every Q in E vanishes identically on every represented
LOW pair, and

    dim E>=D8-n, D8=sum_(i=0)^8 (i+1)*(A-i*w).

All summands are positive through J=9526, since A-8w>=298. Let G
be the primitive gcd over F(X)[Y,Z], g its pair-degree. If g>=5,
Gauss division and additive weighted degree give

    dim E<=D_mult5=sum_(i=0)^3 (i+1)*(A-(i+5)*w).

But direct subtraction gives

    D8-n-D_mult5=1295614-136J>=78>0.                  (K4)

Hence E is nonzero and g<=4. After dividing by G, two coprime
combinations of residual relations leave at most (8-g)^2<=64
off-G pairs. The old bound g<=3 is NOT asserted here. At J=9527
the surplus (K4) is -58, so this argument stops at 9526.

## 2. Every populated line is small unless the source already pays

Apply `height_aware_line_split.md`. Its large-line alternative pays the
ENTIRE source at 255637083438792239, below the theorem's bound.
Otherwise every populated F(X)-line has at most 696 LOW pairs,
regardless of direction height. In particular every linear factor of G
has this cap. Empty factors are ignored and repeated factors count once.

Use the completed-HIGH resource base

    base=C//5500+134944=4194116990084347,
    C=23067643444721720934,
    labels_per_pair=981604.

All subsequent prices are bounds on actual pair or LOW-label counts,
NOT /501-discounted gains combined incorrectly with a /5500 resource.
Only the separately completed large-line alternative used its own
coupled /501 expression. No two resource budgets are added.

## 3. Every irreducible cubic factor is affordable

Here is a uniform cubic total, INCLUDING up to 64 off-curve pairs and
the one resource/near base:

    C3=274979661292365251.                            (C3)

We verify all cubic types without assuming one of them is the whole G.

- A smooth cubic or a rational-normalization cubic with at least two
  boundary points has coefficient dimension <=1 by the existing suppliers.
  Its direct JOINT pair cap at LOW agreement is
  floor(3^21*1048577/66973)=163774741769. This gives whole total
  164956058672324479, below C3. We use a direct count, not the
  earlier discounted group gain.
- A geometrically integral one-boundary cubic singular at infinity is
  a polynomial cubic in its primitive linear input, by the earlier
  classification. As a primitive factor of G it has weighted degree <A,
  so its input height is at most floor((66974-2J)/3)<=17580.
  The existing coupled projection proof gives at most 73222472421
  pairs, hence a total below C3. Its characteristic and input-degree
  conditions remain valid on this interval; its ratio is independent of J.
- For an affine-singular one-boundary cubic, let d be projection-kernel
  dimension. d=0 has at most 3^22 coefficient points directly. For
  1<=d<11, h<=9525/floor(10/(11-d)); for d=11, h=0. The required
  weighted pair formula applies, with r=ceil(d/3). Among d outside
  {7,10}, all totals are <=268384711268522187, below C3.
- For d=7 and h<=1300 the same weighted formula gives (C3) exactly;
  its fixed-gap ratio does not depend on J. At h>=1301 the component
  supplier's `next_interval.md` gives 241058823023306107, counting
  all top components and their entire lower-dimensional complement.
- For d=10, `single_fiber_payment.md` in the GP supplier gives
  83243563858163463 for ALL coefficient dimensions on this interval.
  It keeps original receiver variation, bad fibers and infinity.
- A cubic irreducible over F(X) but not geometrically integral has at
  most six F(X)-points by the derivative/Bezout argument already proved.

These exhaust the cubic types: a geometrically integral singular cubic
has rational normalization and nonempty boundary; if there is one
boundary point its singularity is either affine or at infinity. The
point and component classifications are not inferred from finite samples.

## 4. Count every quadratic and every reducible quartic pattern

Every irreducible quadratic has at most M2=127031877504 LOW pairs.
For a moving-axis nonsingular conic this is the proved pair cap
2^17*(63/4)^5. For a constant-axis conic, the rational-graph theorem
gives floor(2^5*(1048577/66973)^6)=471360758. Rank-two conics use
the dimension-one bound floor(2^21*1048577/66973)=32834505. The
geometrically singular irreducible case has at most one rational pair.
All these are direct pair counts, and are <=M2.

Assign LOW pairs and all their labels to one factor or the off-G set.
Factor patterns of total degree <=4, with their worst whole-source totals,
are then covered as follows:

    up to four lines: base+981604*(4*696+64)
                     =4194119785692539;
    one conic and up to two lines:
                     base+981604*(M2+2*696+64)
                     =128889117504736187;
    up to two conics: base+981604*(2*M2+64)
                     =253584115223779835;
    one cubic and at most one line:
                     C3+696*981604=274979661975561635.

The last expression retains the cubic proof's 64-pair off-G allowance
and adds the extra line group; it does not replace 760 exceptions by 64
or assume the whole source lies on the cubic. Underlying pair bounds are
groupwise and the HIGH resource/near charge remains single. The case
g=0 and all lower-degree or repeated-factor patterns are included.

## 5. A remaining irreducible quartic is geometrically integral

An irreducible quartic over F(X) is geometrically reduced in our
characteristic p>4: an inseparable geometric multiplicity would be at
least p, exceeding its total degree. If it is not geometrically integral,
the separable Galois group acts transitively on its geometric components.
A smooth rational point would pick out one invariant component, impossible.
Thus all its rational points are geometrically singular.

Choose a nonzero partial derivative, of degree at most three. It is
coprime to the irreducible quartic over F(X), and remains coprime over
an algebraic closure by the same component-orbit argument. Bezout gives
at most 12 rational points. Their pairs plus the 64 off-G pairs are
affordable with the single base. Hence only a geometrically integral
quartic can escape the first alternative. Its primitive equation inherits
the strict weighted-degree bound from G and Gauss division.

## 6. Remove the constant-direction split-product family

The finite consumer's `quartic_split_product_payment.md`, using its
new required projective split-product supplier, pays every source whose
quartic has the excluded exact form by N<=164828561948185643.
This includes all projective factor classes, affine scale choices and
the same <=64 off-curve pairs, with one HIGH/near allowance. Its bound
is below alternative 1, so a source not satisfying alternative 1 cannot
have this quartic form. No normal-form existence is asserted for other
quartics, even rational ones or those with the same infinity multiplicities.

## 7. Use the multiplier space, not just the gcd degree

For a source escaping alternative 1 on 8764..9526, the preceding
sections give an exact degree-four gcd. The companion
`quartic_multiplier_geometry.md` uses this fact and the unchanged
kernel definition to prove its two-piece bound on weighted excess H,
the 0/1/2/3/4 off-pair staircase, and |U|>=2009300-110J. It does
not assume the new refined conclusion to prove those properties.

For a polynomial projection graph, the same companion gives h<=2379,
h<=1532 through 9294, and >=28881 coordinates with no on-graph
agreement if even one off-pair exists. The finite consumer's
`quartic_projection_graph_payment.md` consequently pays all such
graphs except possibly d<=2, d=3 with coefficient dimension one, or
d=4 with dimension one / d=5 with dimension two where J>=9295,
h>=1533 and every LOW pair lies on the quartic. Its uniform total
274015369961868939 is below alternative 1. All original labels,
off-pairs, HIGH resource and near are retained, without a graph cover
being assumed for arbitrary quartics.

This completes the refined exhaustive residual restriction. General
non-projection quartics, the printed low-kernel graph cases, larger-J
coverage, higher ranks, original transport and unrestricted prize endpoints
remain open. Neither prize nor an original red closes.
