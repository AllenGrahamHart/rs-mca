# proof: dli_bohr_flatness_prime — target (C), reduction PROVED (Pro T3, verified)

PROVED conditional on the single new leaf dli_prime_block_conductor_mass.

## The reduction (proved: second-moment split + Deligne)
Split S_{j,lambda} = sum_r m_{j,r}|mu_hat_r(lambda)|^2 over exceptional X_{j,lambda}
(singletons, exact atoms, pole-failure/near-linear blocks) vs non-exceptional:
- Exceptional: |mu_hat_r|<=1 => sum_{X} m_{j,r} <= X_j.
- Non-exceptional: Deligne block estimate |mu_hat_r(lambda)| <= cond_{j,r}(lambda)/
  sqrt(|A_{j,r}|) (the phase has a proved prime-to-p pole, dli_phase_pole_conductor_
  manifest: order <= ed+C_tame) => sum m_{j,r}|mu_hat_r|^2 <= C_j =
  sum m_{j,r} cond^2/|A_{j,r}|.
Hence S_{j,lambda} <= C_j + X_j. If both = o(L_j), then S_{j,lambda}=o(L_j) => (via
the proved charge lemma) eta_j=o(L_j) => sum_j eta_j=o(t) over 34 levels.

## Why the hypotheses are necessary (VERIFIED counterexamples)
- P_lambda=0 => psi=1 => |mu_hat_r|=1 => S=256 L_j. So the nonconstant/prime-to-p
  pole manifest MUST be a hypothesis, not background.
- Singleton block |A_{j,r}|=1 => |mu_hat_r|=1 regardless of prime field or Deligne.
  So X_j=o(L_j) is not optional.
- Deligne cancellation is NOT automatic: a LINEAR phase over an interval-like block
  has |mu_hat|~1 (geometric sum, VERIFIED |mu_hat|=0.94), no sqrt-cancellation —
  such blocks are exactly the exceptional X_j. Genuine deg>=2 algebraic phases DO
  cancel (VERIFIED 0.05, 0.099).

## Remaining leaf: dli_prime_block_conductor_mass
Prove sup_{M,lambda!=0} [ sum_{r not in X} m_{j,r} cond_{j,r}^2/|A_{j,r}| +
sum_{r in X} m_{j,r} ] = o(L_j). Sufficient concrete version: #{active blocks at
level j}=O((log n)^A), cond_{j,r}=O((log n)^B), m_{j,r} << |A_{j,r}|, exceptional
mass o(L_j) — then S_{j,lambda} << (log n)^{A+2B} = o(L_j). This is a CONCRETE
structural/counting question about the DLI residue blocks (possibly checkable).
