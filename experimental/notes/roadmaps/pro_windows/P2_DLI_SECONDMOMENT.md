# PRO WINDOW P2 — "DLI-SECONDMOMENT"

*Self-contained. The deepest node; underpins the primitive core. Reduced (over 3
prior rounds) to ONE fixed-frequency flatness estimate. No -2log2, no Deligne.*

## Setting
F_q, q ~ 2^256; mu_n subset F_q^*, n = 2^41; square-root section sigma (no
opposite pair). Tower levels j = 0..33 (only 34), level size L_j = ceil(floor(
t/2^j)/2), t = 2^33, sum_j L_j = t. For a central profile M, nonzero frequency
lambda, low-degree ODD polynomial P_lambda, the phase at section point y is
P_lambda(sigma(y)); group the 256 L_j coordinates by residue r with multiplicity
m_{j,r}; mu_hat_r(lambda) is the normalized additive-character transform,
|mu_hat_r| <= 1. psi(z) = e^{2 pi i Tr(z)/p}.

## Reduced seam (PROVED reductions)
- Charge argument (proved): the geometric-vs-arithmetic loss is charged ONLY to
  near-peak residues, eta_j <= C_loc sum_{r in E_{j,lambda}} m_{j,r}, C_loc=O(1).
- Second-moment bound (proved): if S_{j,lambda} := sum_r m_{j,r}|mu_hat_r(lambda)|^2,
  then sum_{r in E(delta)} m_{j,r} <= S_{j,lambda}/(1-delta). So
    S_{j,lambda} = o(L_j)  =>  eta_j = o(L_j)  =>  sum_j eta_j = o(t) (34 levels).
- CORRECTION (proved counterexample): exact coincidence counting P(sigma(y1))=
  P(sigma(y2)) is NOT sufficient — by Parseval it controls only the FREQUENCY-
  AVERAGE, not each fixed lambda (A={0..N-1}, P=id: zero collisions yet lambda=1
  gives a near-peak). Low degree DOES give the exact-atom part (P(z)=P(x) has
  <= deg P solutions => exact phase atoms have <= (deg)|S| multiplicity).

## The ask (fixed-frequency flatness)
> Prove S_{j,lambda} = sum_r m_{j,r} |mu_hat_r(lambda)|^2 = o(L_j) uniformly in
> the profile M and NONZERO lambda, for the odd evaluations psi(lambda P_lambda(
> sigma(y))). Equivalently the eps-Bohr-pair mass B_{j,lambda}(sqrt delta)=o(L_j).

- **(A)** Prove it (fixed-frequency Bohr/second-moment flatness for the low-degree
  odd phase on the square-root section). Handle the m=1 zero atom (contributes
  exactly m_{j,r} to S, so paid once S=o(L_j)) and the signed-midpoint stress
  (eta*/L=0.019 at mu_32, decreasing in N).
- **(B)** A profile/frequency with S_{j,lambda} = Omega(L_j) (fixed lambda) —
  kills the second-moment route.
- **(C)** Conditional on a clean non-degeneracy of P_lambda o sigma.

Calibration (ground truth): eta*/L = 3.6e-7 at mu_32 (flat). Closes dli -> ejm ->
pcf_evaluation_flatness -> b2b_primitive_core -> ... -> mca_safe.
