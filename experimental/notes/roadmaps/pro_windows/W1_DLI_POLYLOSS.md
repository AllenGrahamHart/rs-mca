# PRO WINDOW W1 — "DLI-POLYLOSS"

*Fresh window. Self-contained. A WEAKENED target (the sharp geometric-mean was
over-engineered); this is the polynomial-loss version the primitive core needs.*

## Setting
F_q, q = p prime ~ 2^256; mu_n subset F_q^*, n = 2^41; a square-root section
sigma with no opposite pair. Tower levels j = 0..33 (only 34 of them!), level
size L_j = ceil(floor(t/2^j)/2), t = 2^33, sum_j L_j = t. For a central profile
M, nonzero frequency lambda, and odd polynomial P_lambda, the phase at section
point y is P_lambda(sigma(y)); mu_hat_y is its additive-character transform.

## What is ACTUALLY needed (verified over-strong before)
The primitive core (via pcf_evaluation_flatness) needs only
    sum_j eta_j = o(t),   where B_j(M) <= q^{-L_j + eta_j} U_j(M).
Because there are only 34 levels and the rate-1/2 agreement reserve is ~2^35 >>
O(log n)=41, a PER-LEVEL POLYNOMIAL LOSS suffices: eta_j = O(polylog n) gives
sum eta_j = 34*O(polylog) = o(t) with ~2^21 margin. The SHARP geometric-mean
estimate (exact circle constant -2 log 2) is NOT required.

## Proved inputs (black boxes)
- The seen-coordinate lever: at least 255 L_j + 1 of the 256 L_j evaluation
  coordinates are nonzero. This gives the ARITHMETIC-mean bound q^{-L_j}.
- The obstruction it leaves: the Dirichlet distribution PEAKS, and even a
  degree-preimage refinement leaves ~129 NEAR-PEAK residues per level (|mu_hat|
  close to 1, contributing near-zero to -sum log|mu_hat|^2).
- Calibration (verified, use as ground truth): mu_32 ternary eta*/L = 3.6e-7
  (essentially flat, decreasing in N); 3 rows reproduced exactly; signed
  midpoint eta*/L = 0.019 at mu_32 (decreasing in N) is the stress case.

## The ask (choose your target)
- **(A) Prove the polynomial-loss bound:** eta_j = O(polylog n) per level
  (equivalently the relative deficit eta_j / L_j -> 0), hence sum_j eta_j =
  o(t). The natural route: the seen-coordinate lever gives q^{-L}; bound the
  geometric-vs-arithmetic gap by charging the ~129 near-peak residues -- show
  each contributes a bounded deficit so the per-level total is O(polylog),
  NOT O(L_j). The second-moment / character-sum route (a crude Weil/moment
  bound, non-saving for the SHARP constant but fine for a polynomial loss) is
  the other candidate. Handle the signed-midpoint stress case explicitly.
- **(B) Refute:** a central profile whose near-peak deficit is Omega(L_j) at
  some level (so eta_j/L_j does NOT vanish) -- then even polynomial loss fails
  and the primitive core needs a different route.
- **(C) Conditional:** the polynomial loss modulo a clean bound on the near-peak
  residue count or their per-residue deficit.

## Downstream
Closes dli -> ejm -> pcf_evaluation_flatness -> b2b_primitive_core (the
skew-tower primitive core) -> ... -> mca_safe. You do NOT need the -2 log 2
constant or any Deligne conductor ledger; a soft o(1)-relative-deviation
equidistribution suffices.
