# REFUTATION — the AQB c=2 amortization route (Pro, verified)

Target (B) of the brief: the canonical c=2 AQB amortization route does NOT
close the rate-1/2 band. Structural, not numerical.

## The convex-combination obstruction (verified: numbers + logic)
Abstract the mechanism compatibly with the stated floor: quotient-support
configs Omega = {S subset mu_N : |S|=m}, |Omega| = C(N,m); box datum map
Phi: Omega -> B, |B| = q^{d-1}; single-word box count |Omega_b| = |Phi^{-1}(b)|.
Plain floor = mean box fiber |Omega|/|B| = C(N,m)/q^{d-1}.

The PROVED averaging transfer needs the family-AVERAGE list mass
  Avg(F) = (1/|F|) sum_{r in F} |Omega_{b(r)}| = sum_b p_b |Omega_b|,
a CONVEX COMBINATION of single-box counts. Hence Avg(F) <= max_b |Omega_b|,
and the uniform family gives Avg = |Omega|/|B| EXACTLY (zero gain). "Paying the
box charge once" computes the UNION sum_{b in A}|Omega_b|, but the transfer
divides by |A|: the saved log2|A| box bits reappear as family entropy in the
denominator and cancel EXACTLY.

## Consequence
Gaining G = 429,645,547 bits requires Avg(F) >= 2^G * mean, which by convexity
forces SOME single box |Omega_b| >= 2^G * mean -- a HEAVY-FIBER (nonuniform
per-fiber) theorem for Phi, NOT box-charge amortization. Assuming it inside the
AQB ledger violates the admissibility guard (consumes the perfiber counts it
must establish). Verified: 2d = sigma*, deficit = 429,645,546.77, per-fiber
0.00039076 / per-extra-fiber 0.0999998 all match.

VERDICT: every admissible c=2 quotient-box family is a convex mixture of
independent single-word boxes; the family average gives no net gain beyond the
plain floor. The AQB route is dead. rate-1/2 must close via a sibling route
(safe-side push through sigma*, or B2b-balance) or stays bracket-grade on the
razor slice log2 q in (255.900, 256).
