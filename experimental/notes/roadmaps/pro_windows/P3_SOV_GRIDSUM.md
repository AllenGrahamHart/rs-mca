# PRO WINDOW P3 — "SOV-GRIDSUM"

*Self-contained character-sum problem. The affine-piece proof route was REFUTED
(no nonconstant affine line of actual mu_n-locators exists when q>n); this is the
correct replacement. Scan evidence is UNIFORM_CONSISTENT.*

## Setting
RS over mu_n, n | q-1 (so q > n). Official-shape rows; anchored-core locators L
(monic, k-1 near-core roots fixed). For h in (20, A], the first obstruction is
O_{h-1} = [X^{h-1}] L = -e_1(non-anchored roots) + const. A conditioning cell
Omega is a subset of D_h(mu_n) = {monic squarefree deg-h L with roots in mu_n},
after fixed/paid roots removed.

## Why the old route died (proved, do not retry)
No nonconstant F_q-affine line L_t=L_0+tB of actual mu_n-locators exists: an
incidence count gives q(h-g) <= n-g, impossible since q>n. So actual locator
cells have NO positive-dimensional additive-affine pieces; exact additive
cancellation does not apply. single_obstruction_valueset is NOT refuted (scan
UNIFORM_CONSISTENT) — only the exact-affine PROOF route is.

## The ask (grid character-sum bound)
> For every official row, h in (20,A], conditioning cell Omega, and nontrivial
> additive character psi, prove
>    | sum_{L in Omega} psi( [X^{h-1}] L ) | <= CharBudget(Omega, h, n, q)
> after removing paid pullback/norm-gate classes, with CharBudget small enough
> that sov_hminus1_fiber_fourier_duality (PROVED) yields the small-fiber
> single_obstruction_valueset bound.

The unconditioned sum is a multiplicative-grid sum:
    S_h(a) = sum_{P subset H, |P|=h} psi(-a sum_{x in P} x)
           = [u^h] prod_{x in H}(1 + u psi(-a x)),   a != 0.
- **Lane 1** distinct-coordinate / symmetric-power sieve on the Euler product
  (anchors remove factors; quotient/pullback cells paid first).
- **Lane 2** Artin-Schreier sheaf on the divisor chart: [X^{h-1}]L = -e_1 + const;
  show the sheaf is geometrically nontrivial off the paid norm-gate locus and
  bound the trace by conductor * q^{dim/2}.
- **Lane 3** norm-gate exceptional accounting: the degeneracy locus = cells
  pulled back from a proper quotient / dihedral map / forced norm relation
  (already paid); everything else must supply analytic cancellation.
- **(B)** a positive-density non-cancelling family after paid classes removed
  (would break the small-fiber lemma).

Downstream: single_obstruction_valueset -> midlarge_h20_A -> XR/staircase cluster
-> r2_clean_rates -> mca_safe.
