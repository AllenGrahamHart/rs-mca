# PRO WINDOW — "DLI-CLOSE-2" (continuation of DLI-CLOSE; your refutation is
# verified and integrated — this is the round-3 form)

*Your B-refutation of "W <= 3" was verified end-to-end (the 110 relation-trades,
the identity bound) and accepted. Verification also found two facts beyond your
note, which change the corrected close:*

1. *Your uniform DLI-AC leaf is FALSE at toy rows: at the matched top-of-range
   row (q=257, n=32, L=2, N=16), sup_(lambda!=0) T(lambda) = 5.3e-3 exceeds
   Delta/(q^L-1) = 4.6e-5 by ~117x — near-peak frequencies concentrate. Only
   the SUMMED form survives.*
2. *The top-prime condition is unnecessary: the W-display was the wrong
   normalization. At low-q rows the huge W is BALANCED mass (E ~ 1 forces
   W ~ 2^N/q^L); your 110 trades contribute only ~2^-236 to E. The row-uniform
   object the endpoint consumes is E itself — and at YOUR counterexample row
   (q=65537, n=512, L=1), E = 1.000000 exactly (computed exhaustively over all
   65537 frequencies; sup T = 7e-155).*

## The round-3 target (row-uniform, verified at three row types)

Setting as before: q prime, q ≡ 1 mod n, n = 2^s, section X = {zeta^i : 0 <= i < n/2}
(no antipodes, no full cosets — verified), level L with N seen coordinates,
a_y(lambda) = sum_l lambda_l x_y^{2l-1}, T(lambda) = prod_{y=1}^N cos^2(pi a_y(lambda)/q).

>>> **TARGET (DLI-NPM, near-peak mass): for every level,
    sum_{lambda != 0} T(lambda) <= 3.** <<<

Equivalently E_U[rho] = 1 + sum_{lambda!=0} T <= 4; then prod over 34 levels
<= 4^34 at EVERY admissible row (no top-prime condition), inside the endpoint
budget. Empirics: E = 1.000000 (your row), 1.75 (matched top-of-range toy,
the tightest observed), 1.0000008 (the original calibration DPs).

## What is proved / verified (usable)

- Vandermonde floor; circle constant (avg log2 cos^2 = -2 exactly); the
  bounded-coefficient norm gate; prime scoping (as in round 1).
- The identity E = (q^L/2^N)(1+W) = sum_lambda T (verified exactly).
- Exhaustive-lambda ledger sweeps at n = 32..2048: worst-case per-block
  cancellation DECAYS with scale; effective conductors O(1).
- Near-peak structure at the tightest toy: sup T = 5.3e-3 attained by O(1)
  frequencies; the sum 0.75 is dominated by a handful of near-peak lambda.

## The ask

> **(A) Prove DLI-NPM** — suggested dyadic route: bound
>   N_j := #{lambda != 0 : T(lambda) >= 2^{-j}}  and sum N_j 2^{-j}.
>   For T(lambda) >= 2^{-j}, at least N - j/c coordinates have
>   |a_y(lambda)/q| near 0 (cos^2 >= 1/2 forces ||a_y/q|| <= 1/4): a near-peak
>   lambda makes the low-degree odd polynomial P_lambda SMALL at many section
>   points — count such lambda via the norm gate / resultant divisibility
>   (algebraic route) or a second-moment over lambda (sum_lambda T has the
>   exact trade expansion — bound the small-w trade terms via the Vandermonde
>   floor and the window law).
> **(B) Refute**: a row family with sum_{lambda!=0} T > 3 — i.e. genuinely many
>   near-peak frequencies. Note your 3-term-relation construction does NOT do
>   this (verified: it moves W, not E). A refutation needs relations DENSE
>   enough to lift the Fourier mass, e.g. a row where P_lambda is small on
>   half the section for many lambda.
> **(C) Conditional**: reduce to one clean statement about small-value
>   concentration of low-degree odd polynomials on half-sections of mu_n,
>   with exact constants (the -1 bit/coordinate SUM version, not per-lambda).

## Guardrails from three rounds of tennis

sup-over-profiles died (low-mass) -> weighted average survived;
W-display died (low-q balanced mass) -> E-display survived;
uniform per-lambda died (near-peak concentration) -> the SUM survived.
Do not introduce a new uniform/sup quantifier anywhere: every intermediate
step should be an average or a counted sum. The target above is the exact
object the endpoint consumes — there is no slack left to lose to normalization.
