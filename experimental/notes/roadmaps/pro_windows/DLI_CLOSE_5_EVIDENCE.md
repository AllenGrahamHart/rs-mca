# RESULTANT-GATE / IDEAL-NORM experiments (round-7 evidence, 2026-07-06)

Scripts: `resultant_gate_experiments.py` (E1/E2/E3, seed 20260706, 250 trials
each, 20s/trial SIGALRM watchdog) + `pair_gcd_web.py` (E2b confirmation, seed
715, 1000 pairs) + `empirical_M_ledger.py` (exact shadow-weighted M at all
multi-orbit census primes). Raw: `resultant_gate_results.json`,
`pair_gcd_web_results.json`, `empirical_M_ledger.json`. Toy scale n' = 32,
N = 16, weight-5 elements, exact integer arithmetic throughout (Fraction
resultants, gcd-echelon ideal norms, Brent-rho factoring, M-R primality).

THE GATE (pairwise analogue of the proved bounded_coeff_norm_gate): two
ternary vanishers at one prime share a root mod q, so q | Res(P1,P2); the
correct k-orbit engineering object is the ideal norm N((P1,...,Pk)) — its
admissible prime divisors are exactly the k-orbit primes.

## Findings

1. **E1 (prime-first, the round-5 selection route): engineering buys exactly
   one generator.** 61 engineered admissible primes from 250 draws; planted
   orbit recovered at every one; bonus independent orbits = 0 observed vs
   35.2 naive-Poisson-predicted, across ALL order-n' embeddings (the plant
   reappears at every embedding as its Galois-dilation copy — norm
   divisibility is embedding-symmetric). The naive mu-Poisson baseline is
   wrong for the conditioned ensemble; the right reading is the census's
   sub-Poisson double suppression (26x), seen from the attacker's side.

2. **E2 + E2b (pair-first): generic pair ideals are COPRIME.** Ideal norm
   N((P1,P2)) = 1 at every random independent pair (243/243); at 1000 pairs
   the gcd-of-norms web finds 29 pairs sharing SOME admissible norm factor
   but only 3 with a common embedding — ALL at q = 97, the super-volume
   floor prime (weight-5 window ~45x over-volume). ZERO two-orbit pairs
   anywhere sub-volume. Alignment costs ~10x beyond divisibility (shared
   factors usually sit in different conjugate/dilation classes).

3. **E3 (triples): dead.** All 243 triple ideal norms = 1.

4. **Empirical shadow-weighted multiplicity (Pro's M) at ~700 census primes:**
   worst M anywhere = 12.875 (q = 21569, config B — SUPER-volume forced
   regime), within 3% of Pro's threshold M* = 13.2907840779; worst
   sub-volume M = 7.75 (q = 204353). Every census prime satisfies M <= M*,
   but the near-miss shows the uniform bound MUST carry the sub-volume
   hypothesis — forced window mass alone walks M to the threshold.

## What this buys the corrected leaf (round-6 return)

The remaining M-BOUND (shadow-weighted M_L <= 13.29 at sub-volume levels) has
its obstruction identified from both sides: statistically (census doubles 26x
sub-Poisson) and adversarially (E1 zero bonus, E2 coprime ideals, E2b
successes only at the volume floor). The one remaining attack is constructing
a SECOND independent short ternary vector inside the prime ideal above q —
a second-minimum event in a lattice of covolume ~q. Route (A1)(1) of
DLI-CLOSE-5: a Minkowski-type second-minimum bound over cyclotomic ideal
lattices, transported to F_q divisibility.

## Honesty flags

- Toy ring Z[zeta_32] has class number 1; at production n' = 512 the class
  group is nontrivial — ideal-class alignment could change the pair-ideal
  story. Flagged in the brief as Pro's opening if one exists.
- E2 proper skipped 7/250 trials (ideal-norm echelon coefficient explosion
  > 20s); E2b's echelon-free gcd-web at 4x sample is the sound instrument
  and supersedes it.
- E1's SELECTION_NEUTRAL verdict uses a pre-registered threshold against a
  baseline (mu-Poisson) that the conditioned ensemble violates downward;
  the honest claim is "zero bonus" not "matches Poisson".

## Ops lessons

- The earlier full-run hang had TWO causes: census.smallest_primitive_root's
  trial-division factoring of q-1 (fixed: Brent-rho primitive root; e1 now
  1s/250 trials) and gcd-echelon coefficient explosion on ~3% of pair/triple
  ideal norms (contained: 20s SIGALRM watchdog per trial, skips logged).
- Piping a background run through `tail` hides all interim progress
  (block buffering); write to a file and tail separately next time.
