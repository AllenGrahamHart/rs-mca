# PRO THREAD T4 — "SOV-GRIDSUM" (fresh window)

*Self-contained. The sov residual, now CLEAN: the trace-flat/subfield locus was
just proved to be a paid class (removed), so this is the residual multiplicative-
grid character-sum on the NON-degenerate cells.*

## Setting
RS over mu_n subset F_q^* (n | q-1, so q>n), official-shape rows. Anchored-core
locators L (monic deg h, k-1 near-core roots fixed). For h in (20, A], the first
obstruction is O_{h-1}=[X^{h-1}]L = -e_1(non-anchored roots)+const. A conditioning
cell Omega subset D_h(mu_n) = {monic squarefree deg-h L, roots in mu_n}, after
fixed/paid roots removed. psi = nontrivial additive character.

## What is proved (black boxes)
- **Affine-piece route REFUTED:** no nonconstant F_q-affine line of actual
  mu_n-locators exists when q>n (incidence q(h-g)<=n-g impossible). Do NOT retry
  exact additive cancellation.
- **Trace-flat/subfield gate PROVED (T1):** the locus where x->Tr(ax) is constant
  on a positive-density free-root cell is an exact PAID class (SOV price
  binom(N_c(a),h) via the descended Euler product S_h(a)=[u^h]prod_c(1+u w^c)^{N_c(a)},
  N_c(a)=#{x in H: Tr(ax)=c}). These cells are REMOVED before this estimate.
- **sov_hminus1_fiber_fourier_duality PROVED:** the fiber distribution of O_{h-1}
  <-> the character sums.

## The ask (target: sov_gridsum_residual)
> After removing the trace-flat/subfield-norm PAID cells (T1) AND the quotient/
> pullback/dihedral paid classes, prove the residual grid character-sum
>    | sum_{L in Omega} psi([X^{h-1}]L) | <= CharBudget(Omega,h,n,q)
> small enough for sov_hminus1_fiber_fourier_duality to yield the small-fiber
> single_obstruction_valueset bound (O_{h-1} takes (1-o(1))-many values).

The unconditioned sum is [X^{h-1}]L=-e_1+const, so
    S_h(a) = [u^h] prod_{x in H_rem}(1 + u psi(-a x)),   a != 0.
- **(A)** Prove it. Lane 1: a distinct-coordinate / symmetric-power sieve on the
  Euler product (a power-sum bound |sum_{x in Gamma} psi(jax)|<=B, 1<=j<=h, on the
  residual root set Gamma gives [u^h](1-u)^{-B}(1-u^{p0})^{-(|Gamma|-B)/p0}). Lane 2:
  an Artin-Schreier sheaf on the divisor chart, geometrically nontrivial OFF the
  paid trace-flat/norm-gate locus, trace <= conductor * q^{dim/2}.
- **(B)** a positive-density residual (non-trace-flat, non-quotient) cell with no
  cancellation — would break the small-fiber lemma.
- **(C)** conditional on a clean sheaf-nontriviality / power-sum bound.

Evidence: the sov value-distribution scan is UNIFORM_CONSISTENT (n=128/256, h=21..40,
no heavy collisions). Downstream: single_obstruction_valueset -> midlarge_h20_A ->
XR/staircase cluster -> r2_clean_rates -> mca_safe.
