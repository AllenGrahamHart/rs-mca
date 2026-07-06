# PRO WINDOW — "DLI-CLOSE" (fresh window)

*Self-contained. This is the CLOSING form of the deepest node of the primitive
core — pinned, counterexample-hardened, with three verified-equivalent displays
and an explicit weight-split architecture. The empirical contract below is
extensive; every known falsifier family is pre-empted by a verified structural
hypothesis. Prime-field only.*

## Setting (verified structural facts)

F_q, q PRIME, admissible (q < 2^256, q ≡ 1 mod n), n = 2^s. Level parameter
L (34 levels in the tower, L = L_j, sum L_j = t = 2^33); N = 256·L seen
coordinates. Section X = {zeta^i : 0 <= i < n/2} (the square-root section),
x_1..x_N its points at the level. VERIFIED section facts (load-bearing):
(S1) X contains no antipodal pair {x,-x};
(S2) X contains no full mu_M-coset (M >= 2).

## The object and the target

An **odd-trade** of weight w: a nonzero d in {-1,0,+1}^N (w nonzero entries)
with sum_y d_y x_y^r = 0 for every odd r <= 2L-1 — equivalently disjoint
P, Q subset X with p_r(P) = p_r(Q) for all odd r <= 2L-1 (P = {d=+1}, Q = {d=-1}).

>>> **TARGET: W := sum over odd-trades of 2^{-w(d)} <= 3.** <<<

Three equivalent displays (identity VERIFIED exactly at toy rows):
- (D2) E_U[rho] = q^L Pr[A d = 0] = (q^L/2^N)(1 + W), where d is iid per
  coordinate with P(0)=1/2, P(+1)=P(-1)=1/4 and A_{l,y} = x_y^{2l-1}. This
  measure is DERIVED (it is exactly the U-weighted central ternary/inactive
  profile family), not chosen.
- (D3) E_U[rho] = sum_{lambda in F_q^L} prod_{y=1}^N cos^2(pi a_y(lambda)/q),
  a_y(lambda) = sum_l lambda_l x_y^{2l-1}. All terms nonnegative; lambda = 0
  gives exactly 1.

Sufficiency: W <= 3 per level gives prod_j E_U[rho_j] <= (q/2^256)^t · 4^34
<= 2^68, deep inside the primitive-core budget. (Stated hypothesis, not asked
here: the central tower measure is a product across levels — levels use
disjoint coordinate sets.)

## What is PROVED (black boxes you may use)

- **Vandermonde floor** (skew_support_threshold): no odd-trade has weight <= L.
- **Circle constant** (dli_circle_log_integral_constant):
  integral of log2 cos^2(pi u) du over [0,1] = -2 exactly.
- **Bounded-coefficient norm gate** (bounded_coeff_norm_gate): a ternary vector
  in the kernel forces q | Res(X^{n/2}+1-type folded resultants, Q_{d,r}) at
  every imposed odd r — no bounded-coefficient escape.
- **Subfield/trace gate** (subfield_trace_paid_gate): extension rows reduce;
  prime q has no subfield trade families.

## Empirical contract (your proof must be consistent with ALL of this)

1. E_U[rho] computed exactly three independent ways at toy rows (DP, MITM
   trade count, exhaustive-lambda cos^2 sum): identical to 1e-6; values
   1.0000008–1.0002 at window-closed rows (i.e. W tiny), rising only via
   calibrated small-q accident windows.
2. **Window law** (calibrated, same law as verified elsewhere in the campaign):
   weight-w trades appear iff C(N,w) 2^w >~ q^L, and then in the RANDOM-MODEL
   count (e.g. (q,n,L)=(97,32,2): expected ~15 at w=5, observed; L=3 expected
   0.56, observed 0). At admissible q the window is CLOSED throughout the gap
   L < w <= w* ~ 68L.
3. **Structure hunts clean**: exhaustive + MITM censuses at five window-closed
   rows (expected counts 6.0 down to 6.8e-4) found ZERO trades. The candidate
   structured families are pre-empted: antipodal (killed by S1), full-coset
   (killed by S2 — note a full even-M coset HAS all odd moments zero, so S2 is
   load-bearing), scaling (c^1 = 1 forces c = 1), Frobenius (trivial, q ≡ 1
   mod n), subfield (q prime), rotation-engineered (hunted, none found).
4. **Analytic margin**: the per-coordinate log2 cos^2 needed is -1 bit; the
   circle average is -2 (proved). Exhaustive-lambda ledger sweeps (every
   lambda != 0, n = 32..2048) show the worst-case per-block cancellation decays
   and effective conductors stay O(1).

## The ask

> **(A) Prove W <= 3** (any absolute constant; even W <= q^{o(1)}·(2^N q^{-L}+1)
> suffices with trivial rebudgeting). Suggested architecture:
>   (a) w <= L: the proved Vandermonde floor.
>   (b) the GAP L < w <= w*: zero trades — e.g. via the norm gate: a weight-w
>       ternary kernel vector forces q to divide a nonzero folded resultant of
>       height ~ (w log n)-bits << L log q for w <= w*; count/exclude survivors.
>   (c) the TAIL w > w*: true count <= K x random per weight (K absolute), OR
>       the analytic route: for every lambda != 0,
>       sum_y log2 cos^2(pi a_y(lambda)/q) <= -(256+delta) L + O(log q)
>       — HALF the typical decay, a 100% margin.
> **(B) Refute**: exhibit a structured odd-trade family in the gap at a
> window-closed admissible row (we could not find one), or a lambda family
> with per-coordinate margin approaching -1 bit, or a coupling that breaks the
> level-product hypothesis. Any of these re-poses the node per its
> failure-conversion clause.
> **(C) Conditional**: reduce to ONE clean classical statement (e.g. an explicit
> anti-concentration inequality for bounded-coefficient linear combinations of
> the odd-power Vandermonde system), stated with exact constants.

## Notes

- The gap claim (b) is where the content lives. The norm-gate route is
  suggested because it is ALGEBRAIC (divisibility counting) and avoids
  tiny-subgroup equidistribution entirely: |H| ~ 2^40 in q ~ 2^256 is below
  all known equidistribution thresholds, so routes that need equidistribution
  of the section itself will stall — but the target's slack (factor-2 in the
  exponent everywhere) is designed so that crude counting suffices.
- Everything here is machine-checkable: the executable predicates (trade
  verification, the three displays, the window law) run in seconds; any
  candidate family or bound you produce can be validated immediately.
- Downstream: closes dli -> (compressed packet) -> x4_exactlist_staircase_split
  -> the exact-list split, the largest hypothesis of the lane.
