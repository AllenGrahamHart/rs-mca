# PRO WINDOW W2 — "SOV-AFFINEPIECE"

*Fresh window. Self-contained character-sum problem. Scan evidence already
supports it (UNIFORM_CONSISTENT across all rows/h). Closes a deeply load-bearing
red on the mca_safe path.*

## Setting
RS over mu_n, official-shape rows; anchored-core locators L (monic, k-1 fixed
roots forming a near-core). For h in (20, A] (A = agreement), the first
obstruction O_{h-1} is the (h-1)th coefficient of a forced-root conditioning of
L. c(L) = [X^{h-1}] L is the top-coefficient map on a forced-root higher-
coefficient conditioning cell Omega of anchored-core locators.

## What must be proved (the terminal)
For every official-shape row, every h in (20, A], and every conditioning cell
Omega, provide a partition of Omega into:
- AFFINE PIECES P_alpha where c(L) = [X^{h-1}] L is affine-linear with NONZERO
  LINEAR PART (so the additive character sum sum_{L in P_alpha} psi(c(L))
  CANCELS -- proved cancellation lemma sov_nonconstant_affine_character_cancellation);
  and
- PAID / norm-structured EXCEPTIONAL pieces whose total size is below the
  character-sum budget.
This gives (via the proved Fourier-duality + character-sum-bound chain) the
first-obstruction value distribution: O_{h-1} takes >= C(n,h)/budget distinct
values (small fibers) -- the single_obstruction_valueset lemma.

## Proved inputs (black boxes)
- sov_nonconstant_affine_character_cancellation (PROVED): on a piece where c(L)
  is affine with nonzero linear part, the character sum cancels.
- sov_hminus1_fiber_fourier_duality (PROVED): the fiber distribution <-> the
  character sums.
- sov_forced_root_recursion_algebra, sov_active_core_obstruction_vanishing
  (PROVED): the forced-root recursion for O_{h-1}.

## Evidence (verified, Modal)
Value-distribution scan: n=128/256, h=21..40, 60k samples/config -- ALL
UNIFORM_CONSISTENT (collision ratio ~1.00, max fiber 3-15, no heavy collisions).
So the small-fiber conclusion holds numerically; the open work is the partition
PROOF.

## The ask
- **(A)** Construct the affine-piece partition: show c(L) = [X^{h-1}] L is, as a
  function of the free (non-anchored) locator parameters, affine-linear with
  nonzero linear part EXCEPT on a paid/norm-structured exceptional set of size
  below the character-sum budget. The nonzero-linear-part condition is a
  nonvanishing statement on the top coefficient (analogous to the xr eliminant
  nonvanishing); the exceptional set (linear part = 0) is a proper subvariety
  charged to the paid/norm-gate ledger.
- **(B)** A conditioning cell with no such partition (exceptional mass above
  budget) -- would refute the small-fiber lemma.
- **(C)** Conditional on a clean bound on the exceptional (degenerate-linear-part)
  locus.

Downstream: single_obstruction_valueset -> midlarge_h20_A -> ... -> the XR/
staircase cluster -> r2_clean_rates -> mca_safe.
