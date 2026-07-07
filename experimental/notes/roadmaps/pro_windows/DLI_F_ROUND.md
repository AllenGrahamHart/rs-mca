# F-ROUND: falsification attack on the frozen conjectures C1/C2 (2026-07-07, user-directed)
# (F1: f1_ledger_calibration_modal.py; F2: f2_level_correlation_modal.py; local K-tables inline in session log)

## F1 — C1 (DYADIC-K) as frozen: **REFUTED** (window-law instance #11, self-scored)

The frozen form said K ≤ 3.34 uniformly at balanced rows. Measured dyadic-K
tables at the NATURAL cluster rows (data we already possessed — the freeze
was sloppy):

| row | k_indep | K at j=20 | K at j=24 | K at j=28 |
|---|---|---|---|---|
| q=204353 | 7 | **23.2** | **10.9** | **3.77** |
| q=100609 | 5 | 23.6 | 4.9 | 2.87 |
| q=110849 | 4 | 21.4 | 2.2 | 1.30 |
| q=65089 (control) | 1 | 0 | 3.79 | 1.48 |

The flaw is the NORMALIZATION: cluster/generator mass is absolute (does not
scale with iid mass), so "K × iid" fails at any row carrying generators —
and such rows exist at every scale by Poisson tails (the same lethal
quantifier pattern we killed in round 7 for the M-bound; freezing C1 with
it was an unforced error, now corrected).

**C1′ (the re-pose, ledger-conditioned) — CALIBRATED:**
>  Σ_{λ≠0} T(λ) ≤ K′ · r · (1 + W_cl(row)),  W_cl = Σ over ALL primitive
>  vanisher orbits (w ≤ w_max, clusters included at their weights) of
>  2N·2^−w — computable per row by the census machinery.

Modal enumeration to w = 7 at all four rows:
q=100609: K′ = 0.15; q=110849: K′ = 0.29; q=204353 (worst cluster row):
K′ = 2.97. All ≤ 3 (sub-1 values = safe double-counting of mean-field mass
inside the w=6,7 ledger). **C1′(K′ ≤ 4, w_max = 7) holds at every measured
row including the k=7 cluster row.**

COMPOSITION CHANGE: C1′ ⟹ DLI-AGG now runs through the S1 sieve — rows
with large W_cl are the sieve's exceptional set (density ≤ 2^−40 per
covered zone); outside it W_cl is bounded and the S2 integral gives the
aggregate. The ENDPOINT-EXCEPTIONAL-RULE (how the consumer avoids/certifies
exceptional q) therefore enters the formal condition chain — it was
informal in S7; that was a gap, now explicit.

## F2 — C2 (level-factorization): the attack found a LANDMINE, and it cuts BOTH ways

The shared-cell two-level probe (levels = moment windows {1,3} and {2,6}
on ONE half-section of μ₃₂, exact MITM counts at 40 primes) found the
level-1 kernel is IDENTICALLY 3^{N/2} at every prime: the half-section of
μ₃₂ SQUARES ONTO THE FULL μ₁₆, reintroducing the antipodal collapse the
section hypotheses kill at level 0 (d with d_{i+8} = d_i is in the m ≡ 2
(mod 4) kernel for every q — verified 40/40). Consequences:

1. A shared-cell tower is STRUCTURALLY IMPOSSIBLE (level ≥ 1 factors blow
   up identically) — since the b2b packet verifies EXACTLY (TEST 1, 8
   rows), the packet cannot be sharing cells naively. **My S6 correction
   ("levels share cells") was itself wrong about the packet.**
2. The b2b archive shows the true structure: NESTED-CONDITIONAL — each
   level has its OWN skew variables on a domain G(state_{<j}) depending on
   the previous level's state ("tower total = Σ_{m₁} skewcount(G(m₁))",
   exact at all 8 test rows). Not shared-cell, not independent-product.
3. C2's real content, sharpened: does the nested conditional expectation
   factorize up to the remaining budget — E[Π_j ρ_j] ≤ 2^{22} · Π_j E[ρ_j]
   (0.65 bits/level of cross-level correlation allowance)? The b2b
   level-2 falsifier ALREADY shows the conditional counts vary beyond
   profile classes (per-k skewcount value-sets are not singletons — spread
   up to ~1.6× within a class), i.e. correlation is REAL; its aggregate
   magnitude is unmeasured. NEXT EXPERIMENT: conditional-vs-unconditional
   skewcount means at the 8 exact b2b rows (machinery:
   verify_level2_tower.py).

## Disposition

- dli STAYS CONDITIONAL, but the condition set is corrected to
  {C1′ (ledger form), C2 (nested-conditional form), ENDPOINT-EXC-RULE} —
  all three statements updated in the dag. C1-as-frozen's refutation and
  C1′'s freshness (calibrated at 4 rows, zero adversarial rounds survived)
  are flagged in the node statements. If the user prefers, the honest
  red-flip criterion is: C1′ failing its own first adversarial round, or
  the F2 nested correlation measuring > 22 bits.

## F2b — the nested-tower measurement: C2 REFUTED AS POSED

Exact conditional-vs-unconditional level-2 means at the eight b2b TEST-1
rows (f2b_nested_correlation.py, machinery = the archived exact verifier):

| t | q | E[sc|null] | E[sc|all] | ratio |
|---|---|---|---|---|
| 2 | 97 | 1.0268 | 1.0286 | 0.998 |
| 2 | 193 | 0.5224 | 0.5172 | 1.010 |
| 2 | 8353 | 0.0529 | 0.0125 | **4.25** |
| 2 | 32801 | 0.0332 | 0.0040 | **8.40** |
| 3 | 97/193 | — | — | 1.04 / 1.16 |
| 4 | 97/193 | — | — | **2.82 / 3.57** |

Geometric mean 2.14 > the 1.57/junction budget; the ratio GROWS with q.
Per-profile-class decomposition (the decisive cut): the correlation is
carried by (a) the k=0 COSET class — null states over-weight it, and it is
exactly the component the packet prices exactly (the "255 coset" column of
TEST 1); (b) rare spiky classes (6.6x at k=7/q=8353, 9.4x at k=5/t=4/q=97)
— toy-scale window accidents; while (c) most noncoset classes are
ANTI-correlated (conditional 0 vs positive unconditional). So BOTH the
unconditional and the per-profile factorization forms are false; the
honest successor C2'' must have the campaign's standard three-part shape:
coset component routed through the packet's EXACT accounting + noncoset
bulk at mean-field (measured anti-correlated = safe direction) + accident
spikes priced by counting. C2'' is NOT YET POSED precisely — that is real
open work on the packet's junction structure.

## FINAL DISPOSITION (both frozen conditions refuted within one round)

C1-as-frozen: REFUTED (F1). C2-as-frozen: REFUTED (F2b). The successors
(C1' calibrated at 4 rows; C2'' identified but unposed) have survived zero
adversarial rounds. Per honest-labels: **dli FLIPS BACK TARGET (red)**.
The S7 amber lasted exactly one falsification round — which is the
protocol working: the freeze documented exact falsifiers, the F-round
executed them, both fired. What survives unconditionally: the S1 norm-sieve
theorem, the moment-transfer lemma, the S2/S3 kill-lemmas, the F1 ledger
calibration, and a much sharper map of what the true closure needs.
