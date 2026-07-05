# PRO THREAD T3 — "DLI-BOHR-PRIME" (fresh window)

*Self-contained. The deepest node's residual, now CLEAN: the subfield/trace
obstruction was just removed (proved separately), so this is a pure PRIME-FIELD
fixed-frequency flatness estimate. Closing it unlocks the entire primitive core.*

## Setting (PRIME field only)
F_p, p prime, p ~ 2^256; mu_n subset F_p^*, n = 2^41. A square-root section
sigma: mu_n -> mu_{2n} (one representative per opposite pair; no opposite pair in
the image). Tower levels j = 0..33 (only 34), level size L_j = ceil(floor(t/2^j)/2),
t = 2^33, with sum_j L_j = t. For a central profile M (a bounded-multiplicity
assignment on the section), a nonzero frequency lambda in F_p, and a LOW-DEGREE
ODD polynomial P_lambda, the phase at a section point y is P_lambda(sigma(y)).
Group the 256 L_j evaluation coordinates by residue r with multiplicity m_{j,r}
(sum_r m_{j,r} = 256 L_j); mu_hat_r(lambda) = normalized additive-character
transform of the phase over residue block r, |mu_hat_r| <= 1. psi(z)=e^{2 pi i z/p}.

## What is proved (black boxes)
- **Charge argument:** the per-level geometric-vs-arithmetic loss is charged only
  to near-peak residues, eta_j <= C_loc * sum_{r in E_{j,lambda}} m_{j,r}, C_loc=O(1).
- **Second-moment reduction:** with S_{j,lambda} := sum_r m_{j,r}|mu_hat_r(lambda)|^2,
  one has sum_{r in E(delta)} m_{j,r} <= S_{j,lambda}/(1-delta), so
      S_{j,lambda} = o(L_j)  =>  eta_j = o(L_j)  =>  sum_j eta_j = o(t) (34 levels)
  => the primitive-core budget pcf_evaluation_flatness => b2b_primitive_core.
- **Subfield/trace gate (PROVED separately):** over EXTENSION rows a trace-zero
  frequency can collapse psi to 1; that locus is now a handled paid class. Over a
  PRIME field this cannot happen: Tr = id, so psi(lambda .) is a nontrivial additive
  character for EVERY nonzero lambda. This brief is exactly the prime-field remainder.
- **Low-degree exact-atom bound:** P(z)=P(x) has <= deg P solutions, so exact phase
  atoms (|mu_hat_r|=1 exactly) have <= (deg)|block| multiplicity — the exact-peak part.
- **Deligne/Weil machinery (available):** the odd-eval phase P_lambda o sigma has a
  prime-to-p pole (dli_phase_pole_conductor_manifest, PROVED: pole order <= ed +
  C_tame), so the additive character sum has Deligne square-root cancellation.

## Correction to avoid (from prior rounds, verified)
Exact coincidence counting P(sigma(y1))=P(sigma(y2)) is NOT sufficient — by Parseval
it controls only the FREQUENCY-AVERAGE, not each fixed lambda (counterexample: an
injective linear map has zero collisions yet a lambda=1 near-peak). The needed bound
is FIXED-frequency.

## The ask (target: dli_bohr_flatness_prime)
> Over prime rows, prove S_{j,lambda} = sum_r m_{j,r} |mu_hat_r(lambda)|^2 = o(L_j)
> uniformly in the central profile M and nonzero lambda, for psi(lambda P_lambda(
> sigma(y))). Equivalently the eps-Bohr-pair mass B_{j,lambda}(sqrt delta) = o(L_j).

- **(A) Prove it.** NOTE the bar is only o(L_j) (polynomial loss), NOT the sharp
  geometric-mean constant -2log2 — so a Weil/Deligne error that is "non-saving" for
  the sharp constant may still give o(L_j). Two candidate routes: (i) DELIGNE — the
  prime-to-p pole gives per-block square-root cancellation |mu_hat_r(lambda)| <=
  (conductor)/sqrt(|block|); sum the second moment sum_r m_{j,r}|mu_hat_r|^2 and show
  it is o(L_j) using the low total conductor mass; (ii) SECOND-MOMENT / additive
  energy of the odd evaluations directly. Handle the m=1 zero atom (contributes
  exactly its m_{j,r} to S, so paid once S=o(L_j)) and the signed-midpoint stress
  (eta*/L = 0.019 at mu_32, decreasing in N).
- **(B) Refute:** a PRIME-row profile/frequency with S_{j,lambda} = Omega(L_j) at a
  fixed nonzero lambda — would kill the second-moment route and force a new
  equidistribution mechanism for the primitive core.
- **(C) Conditional:** o(L_j) modulo a clean non-degeneracy of P_lambda o sigma (e.g.
  a uniform lower bound on the reduced pole order, or a bounded near-peak block count).

## Calibration (ground truth) + downstream
mu_32 ternary eta*/L = 3.6e-7 (essentially flat, decreasing in N); 3 rows reproduced
exactly. So the estimate is TRUE numerically; the open work is the uniform fixed-
frequency proof. Closing (A) discharges dli_harmonic_conductor_ledger ->
pcf_evaluation_flatness -> b2b_primitive_core -> ... -> mca_safe (the safe half of
grand challenge 1).
