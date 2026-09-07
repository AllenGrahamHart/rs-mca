# Proof

The weighted affine-singular cubic extension is proved in
`weighted_singular_cubic_payment.md`, using new supplier 14. Its nonpure
degree budget avoids extra constant-projection components. The full-kernel
child provides the curve coverage and <=64 exceptional pairs; no reverse
dependency from the supplier to that child is used.

The coupled moving-projection continuation of `jet_graph_payment.md`
uses the existing jet supplier's new companion. It accounts jointly
for input rank, kernel dimension and the actual input degree J+h.
Its weighted-height consequence removes infinity-singular cubics from
the full-kernel child's residual case. No additional requirement is added.

The normalization-unit extension of the same factor companion uses
supplier 13's monic-equation/divisor proof. The finite degree-three gain
is unchanged; the class of recognized singular cubics is larger.

The smooth-cubic and nonconstant-j extension is proved in
`smooth_cubic_factor_payment.md`, using the new section-dimension and
joint-count supplier chain. It retains original coefficient degree and
adds only one resource/near allowance after partitioning curve groups.

The projective-jet graph extension is bound in `jet_graph_payment.md`.
Its new required supplier proves the dimension theorem and its finite
resource/cap arithmetic without depending on this consumer. Earlier
companions remain valid at their historical scopes.

The exhaustive nonsingular-conic assembly and the moving-plus-five-
degree mixed cover are proved in `all_conic_payment.md`, using the
existing graph and affine-product suppliers. General factor mixtures
are not inferred from the individual-conic theorem.

The distinct nongraph continuation is proved in
`homogeneous_level_factor_payment.md`, using the complete coefficient-
dimension, joint LIST and group-gain proof in the new required supplier
`mca_low_core_homogeneous_level_payment`. Earlier companions keep their
own scopes; no assertion below is extrapolated to arbitrary plane curves.

All counts are original finite slope labels. The child field is the
unchanged KoalaBear sextic field, not a smaller coefficient field.

## 1. Empty universal core improves the global resource

The support-margin proof, before maximizing its common-zero parameters,
gives

    sum theta <= (n-z)_falling_(s+1)
                 / ((m-g_0)*(d+1)_rising_(s-1)),

where z counts zero lifted normals (v,-C') and g_0 counts their
universally satisfied equations u=h_*. Here g_0=0. Dropping z
only increases the numerator, so the resource is bounded by

    F(J)=prod_(j=0)^11(R+J-j)
         / ((d+J)*prod_(j=1)^10(d+j)).                    (1)

This uses no whole-line farness. It counts all low and high labels
together, with theta=min(d+1,raw). It is not the old resource with
an independently maximized common-zero denominator.

## 2. Constant and nonconstant primitive rows

First suppose |U|>=m, so e=n-|U| lies in [0,R-d]. Put ell=d-500
and A=J+ell. Every low pair agrees at at least A>=J points.
The polynomial-relation supplier's root argument therefore applies.
Its covered-core gcd argument has no incompatible gcd roots on U.

For a nonconstant primitive row, the same-carrier argument puts all
low pairs in an affine scalar family of dimension at most ten.
The preferred rational-direction labels cost at most n. For any
rank-ten ordinary LIST caps V_t on (|U|,J,m-t), its weighted proof,
using (1) instead of the coarser global resource, gives

    |Gamma| <= n+F(J)/501
                     + e sum_(t=1)^500 V_t/(t(t+1)).      (2)

For a constant primitive row, use the weighted gluing proof. In its
finite chart u+gamma_0 v=c on U with c in h_*+C'. A universally
agreeing scalar-list common zero would satisfy C'=0,v=0 and hence
u=c=h_*, contrary to the empty universal core. In its infinite
chart v=c in C', and the analogous condition is C'=0,u=h_*;
it again forces v=0 and is impossible. Thus the scalar-list common
zero count is ZERO in both charts.

The scalar incidence step is consequently

    M_t <= (n-e)V_t/(m-t),

where now V_t is the rank-ten child cap on
(|U|-1,J-1,m-t-1). This cap is supplied by the same uniform padded
LIST compiler with r=R-e, w=d-t, degree range up to 254999.
Removing common-zero nonagreements can only improve this incidence
bound. Grouping identical complete pairs, charging the optional
finite kernel label, and the same summation by parts give

    |Gamma| <= 1+F(J)/501
                  + e sum_(t=1)^500
                        (R+J-e)V_t/((d+J-t)*t*(t+1)).    (3)

In both formulas every high label remains in (1); no relation is
assumed outside U. The exceptional n in (2) and one in (3) are
retained. The actual-field counterexamples in the earlier supplier
explain why the n charge cannot simply be omitted.

## 3. A finite, exact envelope covers every row

Divide e=0,...,981104 into 99 consecutive intervals [a,b] of width
10000 (the last is truncated). Divide t=1,...,500 using endpoints

    1,...,20,50,100,200,300,400,500.

On an interval ending in depth v, use the printed compiler cap for
r=R-a, w=d-v, k_max=254999 and rank ten. It covers the actual
smaller domain by padding it with arbitrary distinct coordinates and
received values, and the actual higher agreement by forgetting excess
agreements. The field-size gate is more than satisfied. This covers
both the direct scalar list in (2) and the one-anchor child in (3).

Replace e by b in the outside multiplier, by a in R+J-e, and t
by v in its decreasing denominator. The exact weight for a block
of depths u+1,...,v is

    sum 1/(t*(t+1)) = (v-u)/((u+1)*(v+1)).

It remains to cover all 250199 integer values of J without a scan.
Put y=d+J and c=R-d. Up to a positive constant,

    F(J)=prod_(j=0)^11(y+c-j)/y.

As c>11, this is a polynomial in y with nonnegative coefficients
plus a positive multiple of 1/y, hence convex for y>0.
Each incidence factor is 1+(R-a-d+v)/(d+J-v), also convex because
its fixed numerator is nonnegative. The entire upper envelope in
(3) is therefore convex in J. In (2), use n<=R+254999; only the
convex F(J) remains variable. Both maxima occur at J=4801 or 254999.

`verify.py` uses exact fractions and 25740 integer LIST transitions.
`verify_audit.py` checks every transition independently by integer
division, recomputes (1) by binomial coefficients, and uses upward
Decimal rounding for a separate envelope check. No numerical search
or optimality claim is a premise. The near-inclusive ceilings are

    constant:    255637082864553899 at J=4801, e in [80000,89999],
    nonconstant:  93265404076279452 at J=254999, e in [90000,99999].

Both are strictly below B, with the advertised slacks.

## 4. Small and empty low unions

If |U|<m, then |U|<=2(m-500)-J because d>=1000. The complete-core
overlap supplier makes all low minimizing pairs coincide, and its
outside injection bounds the number of low labels by R-d+500.
Combining this with (1), and maximizing F at the two endpoints,
gives the near-inclusive bound

    (R-d+500) + (max F-(R-d+500))/501 + 134944,

whose ceiling is 76153884700948142. An empty low family is bounded
by max F/501 alone. No relation hypothesis is needed in this branch.
Since label counts are integral, subtracting 134944 from the largest
stated near-inclusive ceiling gives the selected bound in the claim.

## 5. Return to the original row

The required common-core forcing theorem has already paid original
error rank <=11 and the two rank-twelve common-core extremes. Every
remaining rank-twelve case has J=1048576-|G| in [4801,254999].
Its intrinsic error-rank gauge identifies G exactly with the universal
carrier core. The new transport theorem supplies saturated bad supports
and then preserves all labels, raw minima and relation rows under
whole-core cancellation. The child's universal core is empty.

Thus (2)-(4) apply without a new exceptional-label charge, and only
the ORIGINAL near add-back 134944 is used. Every unpaid selection
is relation-free on the nonempty U'_500. A row space with
2*(ell+1) unknowns and |U'|-(J+ell) constraints can be zero only if

    |U'|>=J+3*ell+2=J+200918.

Transport gives |U_500|=|U'_500|+|G|>=1048576+200918=1249494.
This bound concerns the newly saturated supports, not any old arbitrary
selection. No upper bound on the resulting relation-free family is proved.
