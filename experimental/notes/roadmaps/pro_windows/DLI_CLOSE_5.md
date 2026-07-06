# PRO WINDOW — "DLI-CLOSE-5" (round 7; your round-6 correction verified, accepted, and absorbed)

*Your DLI-CLOSE-4 fulfilment was verified end-to-end — 26/26 checks, including
the counterexample row (Pocklington for 65537, g=3, omega=15028, the primitive
weight-3 relation, the exact rational RHS 185459517751297/2^256 < 2^-208.6),
the per-generator cap r·N·2^-L ≤ 256L·2^-L (exact sweep, all L ≤ 34,
N ≤ 20000), and the aggregate table with the threshold bracketed in exact
rational arithmetic: S(13.290784077959) ≤ 100 < S(13.290784077960). The
correction is ACCEPTED: the printed orbit decomposition was ours, introduced
at the round-5 re-pose, and it is false as a bound on E_j for exactly the
reason you gave — our own D3 display already said the lambda = 0 term is 1.
Damage audit: none numeric. Every banked bit figure was already the excess
form; your S(1) = 51.169972398501 equals our round-5 fantasy stack to the
last digit. Your conditional theorem — R_L = 0 and M_L ≤ M* = 13.2907840779
for all 34 levels ⟹ DLI-AGG — is now the pinned working form, and your §5
certificate format is adopted verbatim. Seventh round; the window law holds:
the false statement died, the aggregate architecture survived, and the leaf
is now a NUMBER.*

## The corrected target (as you posed it; now pinned)

For R* tower rows, with r_j = q^{L_j}/2^{N_j} ≤ 1 and B_j := E_j − 1:

> **(H)  B_j ≤ R_j + M_j · r_j · 2N_j · 2^{−(L_j+1)}**, with
> M_j = Σ_{new independent generators g} s_g (shadow-weighted:
> s_g = 1 + Σ_{shadow orbits of g} 2^{−(w′−L−1)}), R_j = residual
> non-generator near-peak mass; and
> **(C)  Σ_j log2(1 + R_j + M_j·r_j·2N_j·2^{−(L_j+1)}) ≤ 100 ⟹ DLI-AGG.**

## New evidence since your note (all replayable, in the node's notes/)

**1. The exact shadow-weighted ledger at all ~700 census primes**
(`empirical_M_ledger.py`): we recomputed M = Σ_g s_g exactly (union-find
components, minimal-weight orbit as generator, shadows priced 2^{−(w′−2)} at
L=1) at every multi-orbit prime:

| regime | worst prime | raw orbits | generators | exact M |
|---|---|---|---|---|
| SUPER-volume (config B, forced window mass) | 21569 | 16 | 12 | **12.875** |
| SUPER-volume | 21377 | 10 | 10 | 10.0 |
| SUB-volume (config C — the prize-scale analogue) | 204353 | 10 | 7 | **7.75** |
| sub-volume, next worst | — | — | — | ≤ 5.25 |

Every census prime satisfies M ≤ M*, but the super-volume worst case is
within 3% of the threshold. CONSEQUENCE: **the uniform M-bound cannot be
posed over all rows with near-volume low-weight windows** — forced window
mass alone walks M up to the threshold. The theorem must carry the
sub-volume hypothesis. Production towers satisfy it astronomically (the
minimal windows are ~2^216-fold sub-volume at q ~ 2^255.9), and there the
census-consistent coincidence model puts M at Poisson(≪ 1) per level.

**2. Two honesty flags we raise against OUR OWN target before you fire at it
(window-law hygiene, as always):**

- (i) **Naive full uniformity is heuristically FALSE.** Over all ~2^250
  admissible primes q < 2^256, Poisson tails at the sub-volume rate still
  predict a nonzero count of primes with M > M* (invisible, unfindable, but
  nonzero in expectation). So "M_L ≤ 13.29 for EVERY admissible q" is not
  the right theorem. The right forms are: (a) M ≤ M* for all q above an
  explicit size threshold at explicit volume ratio, proved by sieve/counting;
  or (b) an average/exceptional-set form: the set of q with M_L > M* has
  density ≤ 2^{-X}, plus the endpoint consuming only non-exceptional q; or
  (c) engineering-hardness: no PPT/explicit construction reaches M > M*
  (weaker, but matches the adversarial semantics of the endpoint).
- (ii) **Absence below w\* is not computationally certifiable at production
  q.** Your §5 certificate certifies exhibited generators; it cannot certify
  that NO ternary element of weight ≤ w* ~ 68L has q-divisible evaluation at
  q ~ 2^255.9 — that window has ~2^400 elements. So the per-row certificate
  route alone cannot close the node; a theorem (sieve, or vanishing-sums
  classification transported to F_q) must carry the unexhibited mass. This
  is now, in our judgment, the single hardest remaining object in the node.

**3. Resultant/ideal-norm engineering experiments — the attacker's side of
the M-bound** (`resultant_gate_experiments.py` + `pair_gcd_web.py`, n′ = 32
toy, exact integer arithmetic). The gate: two vanishers at one prime force
q | Res(P₁,P₂); k-orbit engineering = hitting the ideal norm N((P₁,…,P_k)).

- E1, PRIME-FIRST (your round-5 selection route), 250 trials → 61 engineered
  admissible primes: the planted orbit was found at every one, and the bonus
  independent-orbit count was **0 observed against 35.2 naive-Poisson** —
  at every one of the order-n′ embeddings. Norm-selection buys exactly the
  plant and its Galois-dilation copies; it never donates a second generator.
- E2, PAIR-FIRST, 243 pairs + 1000-pair confirmation: the pair ideal
  N((P₁,P₂)) is **1 for every random independent pair** — generic pair
  ideals are COPRIME, so a common prime does not even exist, let alone an
  aligned one. The sensitive gcd-web sweep found exactly 3/1000 pairs with a
  common embedding, ALL at q = 97 — the super-volume floor prime (the
  weight-5 window is ~45× over-volume there). Zero two-orbit pairs anywhere
  sub-volume.
- E3, TRIPLES: every triple ideal norm = 1. Tuple-first engineering is dead
  at k ≥ 3.

So the only remaining route to M ≥ 2 at a sub-volume prime is to CONSTRUCT
P₂ inside the specific prime ideal above q — i.e., to exhibit a second
independent short ternary vector in a lattice of covolume ~q. That is
precisely the second-minimum obstruction of ask (A1), route (1).

## THE ASK

> **(A1) Prove the sub-volume M-BOUND in one of the three honest forms of
> flag (i).** Suggested routes, in our priority order: (1) SECOND-MINIMUM /
> ideal-lattice route — the census and E1 data both say the binding
> obstruction is that one ideal rarely contains two independent short ternary
> vectors; a Minkowski-type second-minimum bound over the cyclotomic ideal
> lattice, transported to F_q divisibility, would give M ≤ 1 + o(1) for all
> but an explicit exceptional set. (2) Large-sieve over the orbit family at
> fixed q. (3) Conway–Jones / Lam–Leung vanishing-sums classification mod p:
> structured solutions = shadows + subgroup relations (both priced), sieve
> the remainder.

> **(A2) The R-BOUND.** R_j is the excess of bulk trade mass over its
> mean-field value — the old gap+tail content, now named. The analytic route
> has a 100% margin (circle average of log2 cos² is exactly −2 per
> coordinate; the requirement is −1): prove the per-λ log-sum bound for
> λ ≠ 0 outside the generator orbits, or show us the obstruction.

> **(B) REFUTE — the bars, updated.** (B1) One Pocklington-certified
> admissible SUB-VOLUME prime with TWO multiplier-independent generators
> (still the open channel; your round-5 method buys exactly one, and E1 says
> its Galois orbit never donates a second). (B2) Engineered effective
> M > 13.29 at one sub-volume level (kills the uniform form (a), forces (b)
> or (c)). (B3) The full budget: engineered mass across levels summing past
> 100 bits (kills DLI-AGG; nothing you have produced in six rounds costs
> more than 2.25 bits against 122). Non-counting escapes as before: ternary
> multiples, lifts, signed shifts, same-norm conjugates (unobserved in 700
> primes — if you can FORCE one, show it), rows outside R*, q above the cap,
> and now also: super-volume windows (forced mass is priced in R's
> mean-field, not in M — your own footing, we adopted it).

Rules of engagement unchanged: exact rational arithmetic, explicit
certificates, all conventions printed, refutations shipped with a replayable
verifier. Everything above is already banked and replayable on our side.
