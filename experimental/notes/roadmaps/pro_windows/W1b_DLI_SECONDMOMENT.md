# PRO WINDOW W1b — "DLI-SECONDMOMENT"

*Fresh window. Follow-up to W1: Pro's charge argument already reduced dli to a
near-peak multiplicity-mass seam; this reduces it further to a STANDARD second-
moment bound, and asks to prove that. No -2log2, no Deligne.*

## The exact remaining seam (from W1, verified)
Level j (j=0..33, only 34 levels), 256 L_j coordinates grouped by degree-preimage
residue r with multiplicity m_{j,r} (sum_r m_{j,r} = 256 L_j). Normalized
additive-character transform mu_hat_r(lambda), |mu_hat_r| <= 1. Pro's charge
argument (proved): the per-level geometric-vs-arithmetic loss satisfies
    eta_j <= C_loc * sum_{r in E_{j,lambda}} m_{j,r},   E = {near-peak residues},
so dli holds if the NEAR-PEAK MULTIPLICITY MASS is a vanishing fraction:
    sum_{r in E_{j,lambda}} m_{j,r} = o(L_j)   for every j, profile M, nonzero lambda.
Then sum_j eta_j = o(t). Calibration: eta*/L = 3.6e-7 => near-peak mass ~9.2e-5 L_j
(verified, so the seam holds numerically with margin).

## Reduction to the second moment (the ask)
By Chebyshev/Cauchy-Schwarz, the near-peak mass is controlled by the SECOND
MOMENT (additive energy) of the odd-evaluation map:
    sum_r m_{j,r} |mu_hat_r(lambda)|^2  =  (additive energy) / normalization.
If this second moment is near-diagonal,
    sum_r m_{j,r} |mu_hat_r(lambda)|^2 <= q^{-L_j} (1 + o(1)),
then residues with |mu_hat_r|^2 >= 1 - delta carry mass <= o(L_j) (a peak of
height ~1 costs ~1 of the second-moment budget), giving the near-peak seam.

**Prove:** the second moment (2m-fold additive energy at m=1) of the odd
evaluations P_lambda(sigma(y)) on the square-root section is near-diagonal,
sum_r m_r |mu_hat_r|^2 = q^{-L_j}(1+o(1)) per level, for nonzero lambda. This is
pcf_evaluation_flatness's explicitly-listed SURVIVING lever ("the second-moment/
character-sum route, untouched by the falsifier"). The phases are LOW-DEGREE odd
polynomials -- the additive energy should be near-diagonal because a low-degree
P_lambda has few coincidences P(sigma(y1)) = P(sigma(y2)).

## The ask
- **(A)** Prove the near-diagonal second-moment bound (=> near-peak mass o(L_j)
  => dli => primitive core). Handle the m=1 zero-atom for signed domains and the
  signed-midpoint stress (eta*/L=0.019 at mu_32, decreasing in N).
- **(B)** A profile/frequency with Omega(L_j) additive energy (=> the second
  moment fails => dli needs another route).
- **(C)** Conditional on a clean coincidence-count bound for the low-degree phase.

Downstream: dli -> ejm -> pcf_evaluation_flatness -> b2b_primitive_core -> mca_safe.
