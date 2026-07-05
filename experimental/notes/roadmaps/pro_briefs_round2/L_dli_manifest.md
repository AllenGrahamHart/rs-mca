# Pro brief — DLI reduced-phase manifest (Deligne-Weil equidistribution)

*Self-contained exponential-sum / Weil-type estimate. The deepest open node; it
underpins the primitive core. A manifest closes it; a peak that resists Deligne
refutes the geometric-mean route.*

## Setting
F_q, q ~ 2^256; mu_n subset F_q^* the n-th roots of unity, n = 2^41; a
square-root section sigma: mu_N -> mu_{2N} (one representative per opposite
pair; the section has no opposite pair). A "central profile" M is a bounded-
multiplicity assignment on the section (the b2b tower level j has L_j ~ 2^{33-j}
active odd constraints). For a nonzero frequency lambda and a low-degree ODD
polynomial P_lambda, the phase at a section point y is P_lambda(sigma(y)).

## The estimate needed (DLI_j)
For every central profile M and nonzero frequency lambda,
    - sum_{y in supp M} log | mu_hat_y( P_lambda(sigma(y)) ) |^2  >=  2(L_j - eps_j) log q - O(1),
with sum_j eps_j = o(t) (t ~ 2^33). Equivalently: the odd evaluations
P_lambda(sigma(y)) equidistribute on the section at the GEOMETRIC-mean
(log-integral) rate, whose exact circle constant is
    int_0^1 log |cos(2 pi x)|^2 dx = -2 log 2   (PROVED, dli_circle_log_integral_constant).
This yields J_2 <= q^{-L_j + 2 eps_j + O(1)}, hence EJM_2, hence the primitive-
core cascade. The ARITHMETIC mean gives only q^{-L}; GEOMETRIC behavior is
required (the seen-coordinate lever >= 255L+1 nonzero coords is PROVED but
INSUFFICIENT -- Dirichlet peaks leave ~129 near-peak residues).

## Proved machinery (black boxes)
- dli_circle_log_integral_constant: the -2 log 2 constant.
- dli_deligne_weyl_transfer: the Deligne/Weil square-root-cancellation transfer
  for an exponential sum whose phase has a pole of order prime to p.
- dli_artin_schreier_conductor_criterion: the non-Artin-Schreier / conductor
  criterion (a prime-to-p pole => the additive character sum is non-degenerate).
- dli_et_peak_mass_reduction, dli_truncated_log_transfer: reduce the log-sum to
  a peak-mass discrepancy controlled by the odd-eval exponential sum.

## The manifest to construct (the terminal obligation)
For every tuple (central profile, nonzero frequency lambda, DLI harmonic,
square-root component), provide:
1. the Artin-Schreier-REDUCED local expansion of the phase P_lambda(sigma(y));
2. a pole of positive order NOT divisible by p (so Deligne-Weil transfer
   applies and the odd-eval sum has square-root cancellation);
3. a certified upper bound for the reduced polar divisor (the conductor) of that
   same phase; and
4. a proof that the HARMONIC SUM of the majorants over all tuples is o(t).

## The ask (choose your target)
- **(A) Build the manifest:** exhibit, uniformly in the profile/frequency/
  harmonic, the prime-to-p reduced pole and a conductor majorant, and prove the
  harmonic total is o(t). The lever: the odd polynomial P_lambda composed with
  the square-root section sigma has, generically, a prime-to-p pole at the
  section's branch structure; the peak-mass reduction then bounds the log-sum by
  the Weil error, summing to o(t). Handle the STRESS CASE explicitly: the signed
  midpoint (eta*/L = 0.019 at mu_32, decreasing in N) and the m=1 zero-atom for
  signed domains.
- **(B) Refute the geometric route:** a central profile / frequency whose phase
  has NO prime-to-p reduced pole (Artin-Schreier-degenerate), so Deligne fails
  and a Dirichlet peak survives with eps_j not o(t). This kills the DLI route and
  forces a different equidistribution mechanism for the primitive core.
- **(C) Conditional:** the o(t) bound modulo a clean stated non-degeneracy of the
  phases (e.g. a uniform lower bound on the reduced pole order).

## Calibration (verified, use as ground truth)
No falsifier at the section toys; mu_32 ternary eta*/L = 3.6e-7 (essentially
flat); 3 rows reproduced exactly. So the estimate is TRUE numerically; the open
work is the uniform Weil manifest. Closing (A) discharges dli -> ejm ->
pcf_evaluation_flatness -> b2b_primitive_core (the skew-tower primitive core) ->
... -> mca_safe.
