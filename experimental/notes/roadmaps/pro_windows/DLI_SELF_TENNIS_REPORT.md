# S7 — FINAL STRUCTURE REPORT: the dli node after seven Pro rounds + seven self-tennis rounds
# (2026-07-07, self-tennis terminal state: IRREDUCIBLE CORE reached per SELF_TENNIS_GOAL.md)

## Verdict

The node did not CLOSE outright and DLI-AGG was not refuted. The goal's
third terminal condition is reached: everything provable with known tools
is proved and verified; everything refutable is refuted, priced, or
killed; and the remainder is compressed to TWO named conjectures, each
having resisted the required ≥3 proof approaches and ≥3 attack families.
The node's status flips TARGET → CONDITIONAL on exactly:

>  **C1 (DYADIC-K CORE, conjecture):** for every balanced admissible row
>  and every dyadic level j ≥ j₁: #{λ ≠ 0 : T(λ) ≥ 2^−j} ≤ K·q^L·P_iid,
>  with K ≤ 3.34, and the top range j < j₁ empty outside the killed
>  geometric family. Equivalent (moment transfer) to bounded-alphabet
>  kernel counting in the sieve-uncovered zone
>  {(L,w) : 2 ≤ L ≤ 19, w₁(L) < w ≤ w*(L)} ∪ {L ≥ 20, w ≤ w*}.
>  Measured: K = 1.45 (exhaustive toy scan); census, exact-E, and band
>  data all consistent with K = 1 + o(1).
>
>  **C2 (LEVEL-FACTORIZATION, conjecture/import):** the tower loss
>  factorizes across levels up to 2^{o(t)} — either the packet-side
>  product lemma (the measure definition lives with the consumer
>  x4_exactlist_staircase_split), or unconditionally via Hölder +
>  moment transfer, which folds C2 into C1 at higher alphabets.

PROVED CHAIN (all verified this session): C1 ⟹ DLI-AGG (S2 compression,
threshold exact); DLI-AGG + C2 ⟹ the q^{o(t)} product loss the endpoint
consumes (round-6 S(M) arithmetic, exact rational).

## What was PROVED tonight (all with verifiers, ALL PASS)

1. **A1-PROD norm-sieve theorem (S1)**: unconditional count form; at
   production, level 1's FULL window (w ≤ 55) at exceptional density
   2^−47.6; coverage table for all 34 levels; wall at L = 20 shown
   fundamental to first/second-moment counting.
2. **Moment-transfer lemma (S2)**: Σ_λ T^s = weighted (2s+1)-ary kernel
   count (exact); corollary: analysis and counting are one problem.
3. **DYADIC-K compression theorem (S2)**: C1 ⟹ DLI-AGG with K* = 3.34.
4. **Dual ultra-top emptiness + geometric kill (S3/S4)**: determinant and
   orthogonality transference at the extremes; the order-forced cosine
   dead-zone (ω^{N−1} ≡ −ω^{−1}); coverage kills; the F8 factorization
   locks production base-2.

## What was REFUTED tonight (self-found, corrections pinned in place)

5. The pinned per-λ analytic display (S2) — tail rate 0.21 ≠ 1.
6. The pinned "~68L" w* estimate (S1) — exact is 57.7L − 2.
7. The pinned "(disjoint coordinate sets)" justification for level
   independence (S6) — levels share cells; the hypothesis is real.
8. My own S3 "gluing constants" optimism (S4 audit) — the middle dual
   scale IS the core.

## Evidence dossier for C1 (why it is believed)

- Seven Pro rounds: every attack absorbed at ≤ 2.25 bits (budget 122).
- ~800 census primes across two campaigns: post-closure counts Poisson;
  worst empirical shadow-weighted M = 12.875 (super-volume) / 7.75
  (sub-volume) vs threshold 13.29; exact E at every extreme row ≤ 1.0104
  (0.0149 bits).
- The attacker's side instrumented: prime-first engineering donates zero
  bonus generators (61 primes); generic pair ideals coprime (243/243);
  triples dead; dual-geometric killed by algebra, not luck.
- The q-independent window-mass invariant: expected ledger mass =
  C(N,w)·2^{w−N−L−1} — no row can turn both dials.

## What would change the status

- PROVE C1 in the uncovered zone (new tool needed — the five consumed
  approach families are documented with their exact walls) → node PROVED.
- Refute C1: a balanced-row dyadic level with orbit-robust K > 3.34, or a
  middle-scale dual peak — the attack surfaces are precisely mapped and
  all known mechanisms are killed; a new mechanism would be major news.
- Resolve C2 by exhibiting the packet measure (consumer-side, likely the
  cheapest next step for a human day: read the x4 packet definition and
  either prove the product lemma or run the Hölder route).

## Handoff notes

Pro window DLI-CLOSE-6 remains open (superseded in part by tonight: the
norm-sieve ask (A1) is now PROVED here — S1 subsumes it; the R-bound ask
(A2) should be re-posed as C1). Recommend a DLI-CLOSE-7 brief presenting
C1/C2 and the S1 theorem, asking Pro to attack C1's uncovered zone or
prove the packet-side C2. All verifiers replayable; every claim in this
report has a PASS gate in the node's notes/.
