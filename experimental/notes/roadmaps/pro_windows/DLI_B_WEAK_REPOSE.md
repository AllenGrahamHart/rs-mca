# RE-POSE (2026-07-07, user decision): the node is now the conjecture "B-WEAK is true"
# — the corridor floor, the weakest statement satisfying the x4 obligation

## The obligation, pinned from the consumer's packet

x4_exactlist_staircase_split's interface has 19 wired inputs
(REDUCTION_PACKET.md); this node is its frontier red — "the U-weighted/RES
counting obligation". The terminal consumption is displayed in the
compressed chain's pcf_evaluation_flatness step:

>  B_j(M) = #{d ∈ D_j(M) : Q_d(ζ^{2l−1}) = 0 in F_q, 1 ≤ l ≤ L_j}
>  aggregated with the actual profile weights, with prize budget
>  **q^{−t+H} · W_cen ≤ 2^122**

and the packet itself records that nothing sharper is consumed
("STRATEGIC (verified): the sharp DLI is stronger than the primitive core
needs — polynomial-loss per level suffices; 34 levels, reserve ≫ O(log n)").

## CONJECTURE B-WEAK (the node's new statement)

>  **At the official prize rows (the two grand-challenge parameter sets):
>  q^{−t+H} · W_cen ≤ 2^122** — the U-weighted central-profile mass of TRUE
>  valid-skew counts, taken JOINTLY across the tower (equivalently:
>  E_U[Π_j ρ_j] within its mean-field normalization stays inside the
>  endpoint budget). No per-level bound, no factorization, no uniform
>  constant, no route structure is asserted — those are all strictly
>  stronger statements (every one refuted or unproved to date), and their
>  fates do NOT bear on this conjecture.

Rationale (user-set strategy): we are stuck at this node; nine adversarial
rounds killed only statements strictly stronger than B while B was never
scratched. Posing the floor itself (i) makes downstream confidence the
measurable object — the conjecture stands exactly as long as it resists
direct falsification; (ii) if B is FALSE, a counterexample at the joint
level is precisely the evidence that would force a genuine rethink of x4 —
evidence no route-level refutation can supply (F-round precedent: both
route conditions died, B and x4 unmoved).

## PRE-REGISTERED FALSIFIER (fixed BEFORE any new data; route failures do NOT count)

B-WEAK at deployed scale is not directly computable, so refutation goes
through the packet's own nested tower construction at toy scale, against
the SAME functional budget:

>  **Refutation standard:** exact toy towers (the b2b nested construction,
>  the machinery of verify_level2_tower.py / f2b) showing the JOINT loss
>  factor E_U[Π_j ρ_j] exceeding (C · log q)^{J} — polynomial-per-junction
>  loss, J = #junctions, for EVERY constant C — i.e. a demonstrated
>  super-polylog PER-JUNCTION growth trend in the JOINT object, sustained
>  across ≥ 3 increasing q-scales at ≥ 2 tower depths, with the coset/
>  structured component routed through the packet's EXACT accounting (it
>  is part of the budget arithmetic, not a violation).

What does NOT count (the F-round taught us each of these): violations of
factorized/per-level/uniform-constant proxies; single-row window accidents
(Poisson-priced); super-volume/boundary-volume toy regimes; correlation
ratios of CONDITIONAL means (composition effects through exactly-priced
components). What DOES count besides the standard above: any replayable
construction at ANY scale whose transported arithmetic exceeds 2^122 at
the official rows.

## Evidence ledger at re-pose time (survival record of B itself)

- 7 Pro rounds + 7 self-tennis rounds + the F-round: every successful
  refutation killed a strictly-stronger A; the strongest attack ever
  priced against the budget: 2.25 bits of 122.
- Exact joint measurements wherever computable: every extreme row found by
  either side costs ≤ 0.015 bits (exact D3 sums; boundary rows r-diluted).
- The b2b nested tower is EXACT at all 8 archive test rows (TEST 1) — the
  joint object at those rows sits inside its scaled arithmetic including
  the coset column.
- Unconditional theorems narrowing the falsification search: A1-PROD
  norm-sieve (level-1 window closed at density 2^−47.6; walls mapped),
  moment transfer, dual-top kills (F8 lock, cosine dead-zone).

## Route material (evidence lane — NOT conditions of this node)

C1′ (ledger-conditioned dyadic bound; calibrated K′ ≤ 4 at 4 rows, zero
adversarial rounds survived); C2″ (nested-junction shape: exact coset +
mean-field noncoset + counted accidents; not yet precisely posed); the S1
sieve theorem; the DLI-CLOSE-6 Pro window. Routes may be attacked,
refuted, and replaced freely without touching this node; promotion of any
route into a conditional close requires it to survive its own adversarial
rounds first (F-round rule).

## First experiment of the B-falsification program (next step)

The junction-correlation scaling study aimed at the JOINT object: sweep
the exact toy towers in q (≥ 3 scales) and depth (t = 2..4+), measuring
E_U[Π ρ] against (C log q)^J with the coset column routed through exact
accounting — the direct test of whether the F-round's growing conditional
ratios compound in the joint (B in danger) or are absorbed by the exact
coset arithmetic (B safe, C2's failure was route noise).
