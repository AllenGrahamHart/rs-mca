# DLI-CLOSE: the pinned target (2026-07-06)

The minimal sufficient obligation to close this node, in counterexample-hardened
form. Every hypothesis explicit; every equivalent display verified; every known
falsifier family pre-empted. This document is the source for the Pro brief and
the Codex adversarial goal.

## Setting (all verified structural facts)

- q PRIME (prime-field scoping: extension rows reduce via subfield_trace_paid_gate,
  PROVED; prime q kills subfield/trace trade families). Admissible: q < 2^256,
  q ≡ 1 (mod n), n = 2^s.
- Level j: L = L_j, N = N_j = 256·L seen coordinates. Section
  X = {zeta^i : 0 <= i < n/2} (the square-root section).
- VERIFIED section hypotheses (these kill the structural trade families — they are
  load-bearing, not decorative):
  (S1) X contains NO antipodal pair {x, -x}  [verified; -zeta^i = zeta^{i+n/2} is
       outside the index window] — kills the antipodal trade family (x,-x both +1
       is an odd-trade).
  (S2) X contains NO full mu_M-coset for any M >= 2 [verified; equally-spaced
       points cannot fit in a half-window] — kills the coset trade family (a full
       even-M coset has all odd power sums zero).
  Also killed: scaling trades (c^r = 1 for r=1 forces c=1), Frobenius trades
  (q ≡ 1 mod n makes Frobenius trivial), subfield trades (q prime).

## The obligation — three equivalent displays (identity VERIFIED exactly, D2=D3 to 1e-6)

Let A be the L x N matrix A_{l,y} = x_y^{2l-1} (odd powers of the section points).

- (D1, combinatorial) An ODD-TRADE is a nonzero d in {-1,0,+1}^N with A d = 0 —
  equivalently a pair of disjoint subsets (P,Q) of X with p_r(P) = p_r(Q) for every
  odd r <= 2L-1. Weight w(d) = |P|+|Q|. Define
      W_j = sum over odd-trades of 2^{-w(d)}.
- (D2, probabilistic/closed form) With d iid per coordinate (P(0)=1/2, P(+-1)=1/4
  each — this measure is EXACTLY the U-weighted central ternary/inactive family;
  derivation: sum_S 3^{|S|} rho(S) / sum_S 3^{|S|} telescopes to it):
      E_U[rho_j] = q^L * Pr[A d = 0] = (q^L / 2^N) * (1 + W_j).
- (D3, analytic) E_U[rho_j] = sum_{lambda in F_q^L} prod_{y=1}^{N}
  cos^2(pi * a_y(lambda) / q),  a_y(lambda) = sum_l lambda_l x_y^{2l-1}.
  (lambda = 0 contributes exactly 1; all terms nonnegative.)

## THE TARGET

> **For every level j: W_j <= 3.**  (Equivalently E_U[rho_j] <= (q^L/2^N)·4, or
> D3-excess sum_{lambda != 0} prod cos^2 <= 3·q^L/2^N + 3.)

Sufficiency for the endpoint: prod_j E_U[rho_j] <= (q/2^256)^t · 4^{34} <= 2^68
(the prefactor is <= 1 at admissible q; 34 levels), far inside the q^{o(t)}
budget the compressed packet consumes. EXPLICIT REMAINING HYPOTHESIS (flagged,
not proved here): the central tower measure is a product across levels (levels
use disjoint coordinate sets), so E[prod] = prod E. This is the packet's
framing; it must appear as a stated hypothesis of the closure.

## Proof architecture (weight split), with the evidence per piece

Let w*(q,L) = max{ w : C(N,w)·2^w <= q^L · 2^{-10} } (~68·L at q = 2^{255.9}).

- (a) w <= L: NO trades. **PROVED** (Vandermonde / skew_support_threshold).
- (b) THE GAP, L < w <= w*: claim ZERO trades at admissible rows. This is the
  real content. Evidence: (i) exhaustive + MITM structure hunts at 5 random-empty
  toy rows (expected counts from 6.0 down to 6.8e-4) found ZERO trades;
  (ii) at open-window toy rows (small q), trades appear in EXACTLY the
  random-model count (e.g. (q,n,L)=(97,32,2): expected ~15 at w=5, found; L=3
  expected 0.56, found 0) — the same window law verified for u2c, with no
  structural surplus anywhere.
- (c) THE TAIL, w > w*: need the true weight-w trade count N_w <= K · C(N,w) 2^w q^{-L}
  (K absolute). Then sum_{w>w*} N_w 2^{-w} <= K · 2^N q^{-L} <= K at admissible q.
  ALTERNATIVE (analytic route subsuming (b)+(c)): via D3, it suffices that for
  every lambda != 0, sum_y log2 cos^2(pi a_y(lambda)/q) <= -(256+delta)·L + O(log q):
  the circle average of log2 cos^2 is EXACTLY -2 (the proved
  dli_circle_log_integral_constant), so the typical value is -2·256·L — the
  requirement is HALF of typical: a 100% (one-bit-per-coordinate) margin.

## Counterexample pre-emption record (what Pro will try, and why it fails)

1. Antipodal / coset / scaling / Frobenius / subfield trade families: killed by
   (S1), (S2), c=1, Frobenius-trivial, q prime — all verified above.
2. Low-mass profiles: integrated into the measure (the closed form IS the
   weighted average); the old sup-form killer contributes 2^{-245L} (verified).
3. Small-q accidents (the u2c pattern): the window law is calibrated — accidents
   exist iff C(N,w)2^w >= q^L, impossible in the gap at admissible q. The
   statement carries the admissible-row hypothesis explicitly.
4. lambda = 0 / d = 0 atoms: excluded explicitly in every display.
5. L = 1,2 small levels: the gap is window-closed at admissible q for ALL L >= 1
   (C(512,5)·2^5 ~ 2^50 << q^2); the toy L=2 accidents are small-q artifacts.
6. Rotation-engineered trades (P with single surviving odd moment, Q = zeta^{2k}P):
   requires zeta^{2k r0} = 1 with the section-disjointness constraints; hunted in
   the MITM census (would appear at w ~ 4L) — none found. Flagged for Codex to
   attack specifically.

## Failure conversion

If (b) fails — a structured gap family exists — the node re-poses with that
family priced (the u2c playbook). If (c)'s constant K is unprovable, the node
re-poses as the explicit conditional "K-bounded tail". Either outcome is a
compression of the red to a strictly smaller kernel; the target above is the
full closure.

# ROUND-2 UPDATE (2026-07-06, after the Pro DLI-CLOSE response — all claims verified)

## What Pro found (VERIFIED)
1. REFUTATION of "W <= 3" as literally stated: the identity forces W >= (2^256/q)^L - 1,
   so the target needs q >= 2^{256-2/L}; explicit witness at (q,n,L)=(65537,512,1):
   zeta=15028, the relation 1 + zeta^95 = zeta^146 gives 110 in-section weight-3
   odd-trades, W >= 13.75. VERIFIED end-to-end (order, relation, section, trades).
2. A corrected conditional close: top-prime condition Delta(q,L) = 4(q/2^256)^L - 1 > 0
   plus the uniform per-frequency bound DLI-AC: T(lambda) <= Delta/(q^L-1) for all
   lambda != 0 implies W <= 3. Algebra VERIFIED exact.

## What verification found BEYOND Pro's note
3. Pro's uniform DLI-AC is itself FALSE at toy rows: at the matched top-of-range toy
   (q=257, n=32, L=2, N=16), sup T(lambda) = 5.3e-3 exceeds Delta/(q^L-1) = 4.6e-5 by
   ~117x (near-peak frequencies concentrate). Only the SUMMED form survives.
4. THE NORMALIZATION FIX (supersedes the top-prime patch): the W-display is not
   row-uniform — at low-q rows the huge W is BALANCED mass (E ~ 1 forces W ~ 2^N/q^L),
   not trades (Pro's 110 trades contribute ~2^-236 to E). The row-uniform object the
   endpoint consumes is E itself:
       >>> RE-POSED TARGET: E_U[rho_j] <= 4 per level  (<=> sum_{lambda!=0} T(lambda) <= 3) <<<
   This needs NO top-prime condition, gives prod_j E <= 4^34 at every admissible row,
   and SURVIVES Pro's own counterexample row: E = 1.000000 there (computed exhaustively,
   sup T = 7e-155). Verified at three row types: Pro's low-q row (1.000000), the
   matched top-of-range toy (1.75), the original DPs (1.0000008).

## The remaining kernel (round-3 leaf)
    sum_{lambda != 0} prod_{y=1}^{N} cos^2(pi a_y(lambda)/q)  <=  3   per level,
i.e. NEAR-PEAK MASS CONTROL IN SUM FORM (the uniform per-lambda form is false; the
dyadic route: #\{lambda : T(lambda) >= 2^{-j}\} counted against 2^{-j}). The exhaustive-
lambda ledger sweeps (n=32..2048, worst-case decay, O(1) conductors) bear directly on it.

## The tennis scoreboard (each round: uniform dies, average survives)
round 1: sup over profiles  -> U-weighted average   (low-mass profiles)
round 2: W-display (row-nonuniform) -> E-display    (low-q balanced mass)
round 3: uniform per-lambda -> summed over lambda   (near-peak concentration)
The E-form target is now triply battle-tested; every known falsifier family is priced
into the display itself.
