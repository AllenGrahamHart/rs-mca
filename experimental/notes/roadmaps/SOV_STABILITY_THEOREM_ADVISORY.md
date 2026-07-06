# SOV-BOHR-PRICING: Pro's response, verified (2026-07-06) — the isolated stability theorem

Status: ADVISORY for this retracted lane (the sov branch lives under this red per
retraction 3). Re-expansion trigger: a PROOF of the stability theorem below.

## What Pro delivered (all checkable claims VERIFIED)
- Correct reframing: price by SCALE-ADAPTIVE containment, not a fixed B*=0.93 gate
  (a fixed gate over-includes non-rigid cells and under-describes the budget-critical
  near-1 interval obstructions).
- Exact interval formulas: |V_h([1,m])| = h(m-h)+1 (= the Dias da Silva-Hamidoune
  bound h|A|-h^2+1, attained); B = |sin(pi m/p)|/(m sin(pi/p)). VERIFIED: the full
  R=48/64/96/128 calibration table matches to every printed digit; DdS-H attainment
  verified exactly (p=10007, m=30, h=4: 105=105).
- Literature anchors: DdS-H restricted sumsets; Bajnok-Edwards critical number
  C_h(Z_p) = floor((p-2)/h) + h -- above it every m-set is h-complete (V_h = F_p),
  so the pricing problem is CONFINED to m <~ p/h with intervals/APs as the extremal model.

## THE ISOLATED TARGET (the clean theorem that closes the lane's sov content)
> Prime p, h fixed, m <= p/h + O_h(1). If |V_h(Gamma)| < theta*p and
> C(m,h)/C(p-1,h) > 2^{-128-sigma} (budget-relevant density), then after
> dilation/translation Gamma is O_h(1)-close to an interval of length
> <= theta*p/h + O_h(1).
Lane-1 closure below the gate = the contrapositive; the price above the gate =
a count of near-interval/AP cells dominated by the coarsest admissible R, with
O_h(1)-perturbation cost ~ h*log2(1+t/m) bits (negligible at prize m).

## Risk families (Pro named them; I tested all three — the theorem SURVIVES)
1. Rank-2 GAP at budget-relevant size (m=1024): FILLS (exact-range argument +
   measured 0.57p+) -- not a small-V failure. h^2*m >= p forces filling.
2. Rank-2 GAP with small V_h (m=64): density 2^{-215} -- EXCLUDED by the density
   hypothesis (the same window law as u2c/dli: small-V structure below budget scale).
3. Sparse subset of a 2x-too-long container: EXACT bitset-DP |V_h| = 0.882p --
   FILLS, exactly per Pro's h*|I| >= theta*p criterion. (My first sampled estimate
   0.289p was a CLT-concentration estimator artifact -- caught and corrected;
   recorded as a known trap: sampling h-fold sums concentrates and undercounts V_h.)

## Assessment
The sov pricing content is now ONE literature-adjacent inverse/stability theorem
(Freiman-type stability for restricted sumsets at the DdS-H extremal). Genuinely
publishable shape. If proved, the retracted sov segment re-expands with proven
material per the retraction manifest.
