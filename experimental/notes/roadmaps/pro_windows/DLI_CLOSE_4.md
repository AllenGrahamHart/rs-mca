# PRO WINDOW — "DLI-CLOSE-4" (round 6; your round-5 refutation verified, absorbed, and re-posed)

*Your engineered-prime refutation of DLI-NPM\* was verified end-to-end: the
Pocklington certificate replays, q = 0.528·2^256 divides the norm of
1 − z^33 + z^40 − z^136 − z^143 + z^145 (z of order 512), the 512 folded signed
shifts are distinct weight-6 kernel vectors, W ≥ 8 > 6.5735 and E ≥ 4.753 > 4
inside R*, no scoping escape. The per-level uniform constant is dead —
permanently. But the endpoint never consumed per-level constants: it consumes
the PRODUCT over levels, budget 2^122. Your row costs log2(4.753/4·…) = 2.25
bits at ONE level of ~34. The Vandermonde floor w ≥ L+1 makes engineered cost
DECAY with depth (L=1: ≤7.0 bits, L=5: ≤5.4, L=12: ≤0.8, L≥20: ~0), so even the
fantasy stack — an engineered orbit at ALL 34 levels simultaneously — totals
51.2 bits against 122. Sixth window-law instance: the uniform quantifier died,
the aggregate survived. Round 6 is the first round where the remaining surface
is a single counting question.*

## The aggregate target (DLI-AGG)

For the R* tower rows (as pinned in DLI-CLOSE-3: q ≡ 1 (mod n'), X = c·(full
half-section of mu_{n'}), N = n'/2, 2^N ≥ q^L, levels indexed j with their own
(n'_j, L_j)):

> **DLI-AGG:  Σ_j log2 E_j ≤ 100 for every admissible row,**

with E_j = E_U[ρ_j] exactly as in rounds 2–5 (identity ρ_j(M) =
q^{L_j}|Z_j(M)|/U_j(M)), and the orbit decomposition

> E_j ≤ (q^{L_j}/2^{N_j}) · (1 + K_j · 2N_j · 2^{−(L_j+1)}),

where **K_j(q) = the number of minimal-weight relation ORBITS at level j whose
defining ternary element has q-divisible evaluation**. Everything is proved
except the size of K_j. The kernel is now purely a counting question:

> **ORBIT-COUNT: how many independent low-weight ternary cyclotomic elements
> can a single admissible prime q < 2^256 divide?**

## Conventions (all printed; census-corrected)

Ternary element at level with order n' = 2N: P = Σ_i ε_i z^{e_i}, ε_i ∈ {±1},
distinct REDUCED exponents 0 ≤ e_i < N (reduced form, z^N = −1, so ring
identities cannot occur); weight w = #terms. Pinned embedding: ω = g^((q−1)/n')
mod q, g the smallest primitive root. P VANISHES iff P(ω) ≡ 0 (mod q). ORBIT =
signed-shift class (z-multiplication with fold, global sign). PRIMITIVE = no
proper sub-sum of P's terms vanishes.

**INDEPENDENT — the convention the data forces.** We falsified the naive
per-orbit independence ourselves before this round: one vanisher P spawns a
deterministic shadow of ternary multiples m·P (m ternary of weight 2–3, ternary
via cancellation alignment), all vanishing with P. In a 700-prime census the
apparent heavy tails collapse under this closure (worst primes: 13 → 4 orbits,
10 → 1, 11 → 5 — the last is q = 65537 = F_4). Likewise the exponent-doubling
lift e → 2e maps a level vanisher to the next level IDENTICALLY (57/57
verified) — one coincidence, charged once at its minimal level. So:

> Two orbits are INDEPENDENT iff neither is obtained from the other by
> signed shifts, ternary-multiplier products, or level lifts.
> K_j splits as (independent generators new at level j) + (their shadow,
> which is deterministic, weight-graded, and cost-decaying).

## Census evidence (5 configs, ~700 primes; replayable, gates PASS)

Per-prime counts of multiplier-independent generators vs the coincidence
model mean μ = #orbits/q (Poisson):

| config | n' | weights | q band | mean obs/pred | P(k≥2) obs/Poisson |
|---|---|---|---|---|---|
| A | 32 | 3–6 | 2e4–1e5 | 0.605 / 0.630 | 0.005 / 0.132 |
| C | 64 | 3–5 | 2e5–4e5 | 0.460 / 0.4625 | 0.050 / 0.079 |
| D | 128 | 3–4 | 2e4–1e5 | 1.22 / 1.64 | 0.27 / 0.49 |

- Sub-volume regimes: means match the coincidence model almost exactly;
  multiples run AT OR BELOW Poisson (config A: doubles 26× RARER than
  independence predicts — the ideal lattice rarely affords two independent
  short ternary vectors).
- Super-volume windows (#orbits ≳ q) show forced counts — the priced
  "random-window mass"; at prize scale the low-weight windows are ~2^216-fold
  sub-volume.
- **No dilation-class stacking anywhere**: no prime was ever observed dividing
  two conjugate factors of the same norm (max same-dilation-class = 1 at all
  ~700 primes).
- Worst post-closure residual in 200 primes of the densest config:
  one prime at P(k≥7 | μ=1.55) ≈ 6e-4 — expected count ~0.12, one observed.

## THE ASK

> **(A) PROVE the multiplier-closed orbit-count bound.** For every admissible
> q and level j: the number of multiplier-independent generators new at level
> j is bounded (absolute constant, or poly(log q)), with the shadow priced
> geometrically by weight — any form strong enough to give Σ_j log2 E_j ≤ 100.
> Suggested routes: (i) large-sieve/character-sum bound for the divisibility
> events over the orbit family at fixed q; (ii) vanishing-sums-of-roots-of-
> unity classification transported to F_q (Conway–Jones / Lam–Leung style:
> structured solutions = shadows + subgroup relations, both priced; the
> unstructured remainder is sieve-counted); (iii) if a uniform theorem
> resists: a per-row certificate format for exhibited rows (we supply the
> census machinery as the verifier skeleton).

> **(B) REFUTE.** Engineer ONE Pocklington-certified admissible prime
> q < 2^256 dividing TWO OR MORE multiplier-INDEPENDENT minimal-weight ternary
> elements whose combined ledger cost exceeds the budget — i.e., beat the
> absorption arithmetic honestly. Your round-5 method buys one orbit by
> construction (select q inside one norm). The obstruction as we compute it:
> a second independent orbit means q simultaneously divides a second
> independent norm — a ~2^−216-density coincidence you cannot select for
> while keeping q < 2^256 and q ≡ 1 (mod n'). If CRT/lattice tricks (P_1, P_2
> engineered to share a large common norm factor; resultant structure;
> ideal-class alignment) can beat this, that is exactly the fight we want.
> What will NOT count: P_2 a ternary multiple, level lift, signed shift of
> P_1 (shadow — priced, charged once); a conjugate/dilation of P_1 landing in
> the SAME norm (unobserved in 700 primes — but if you can FORCE it, show it:
> that would be new structure); rows outside R*; q above the field cap.

Rules of engagement as in rounds 1–5: exact rational arithmetic, explicit
certificates (Pocklington for primes), all conventions printed, refutations
shipped with a replayable verifier. We replay everything and integrate within
a day: verified refutations get absorbed or the target re-posed; five rounds
of this protocol have so far only made the object stronger.
