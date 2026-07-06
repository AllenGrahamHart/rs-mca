# ORBIT-COUNT census (round-6 evidence, 2026-07-06)

Script: `modal_dli_orbit_census.py` (Modal, 25 sharded inputs, all < 60 s;
gates G1/G2/G3 PASS; raw output `orbit_census_results.json`).  Object: per-prime
count of primitive ternary vanisher ORBITS at the pinned embedding
(omega = g^((q-1)/n'), g = smallest primitive root), toy scales
n' in {32, 64, 128}, weights 3..6, ~700 primes total across 5 configs.

## Headline findings

1. **MULTIPLIER SHADOWS are the dominant clustering mechanism.**  One vanisher
   P spawns ternary multiples m*P (m ternary, weight 2-3, via cancellation
   alignment).  Raw "primitive orbit" counts cluster hard (config A: 60% of
   pilot primes multi-orbit); modulo weight-<=2-multiplier closure this
   collapses (A: frac k>=2 drops 0.22 -> 0.005), and the heavy tails of config
   B collapse under weight-<=3 multipliers (63361: 10->1, 65921: 10->1,
   48449: 13->4, 65537 (=F4): 11->5).  Every surviving residual is ordinary
   Poisson mass at its per-prime lambda = #orbits/q (worst case in 200 primes:
   P(>=7 | lambda=1.55) ~ 6e-4 once — expected ~0.12).
   CONSEQUENCE: the ORBIT-COUNT kernel must be posed MODULO ternary-multiplier
   generation (charge each independent generator once; its shadow is
   deterministic, weight-graded, and cost-decaying).  The naive per-orbit
   independence claim is FALSE as stated — self-falsified here before Pro
   could weaponize it (window-law hygiene).

2. **After closure, independence holds at the Poisson level.**  Sub-volume
   configs match the prediction lambda = #orbits/q almost exactly:
   A (n'=32, w<=6): mean 0.605 vs 0.630; C (n'=64 high band): 0.460 vs 0.4625;
   D (n'=128, w<=4): 1.22 vs 1.64 (sub-Poisson).  Doubles run AT OR BELOW the
   Poisson rate in sub-volume regimes (A: 0.5% vs 13.2% predicted — strongly
   sub-Poisson; the ideal lattice rarely affords two independent short
   ternary vectors).

3. **No dilation-class stacking.**  max_same_dilation_class = 1 at every one
   of the ~700 primes: a prime was never observed dividing two conjugate
   factors of the same norm.  The "two hits inside one norm" channel is empty
   in the census.

4. **Volume law (window-law consistency).**  Super-volume windows
   (#orbits >~ q: config B w=5, vol ratio 2.2) show forced counts — the
   priced "random-window mass" of the kernel statement.  At prize scale the
   low-weight windows are ~2^216-fold SUB-volume, i.e. deep in the regime
   where the census validates Poisson behaviour.

5. **Cross-level lifts are identities, not coincidences.**  The exponent
   doubling e -> 2e maps level-32 vanishers to level-64 vanishers identically
   (57/57 verified).  Level-independence bookkeeping must charge a coincidence
   once at its minimal level; the positive cov(k32, fresh64) = 0.39 is
   confounded by shared 1/q scaling within the band (both counts rise at
   small q) — flagged, not evidence of coupling.

## What this buys DLI-AGG

The kernel question "how many independent low-weight ternary cyclotomic
elements can one prime divide" now has a measured shape: independent
generators are Poisson-rare (never > 2 per prime after closure in any
sub-volume config), shadows are deterministic and chargeable to their
generator, dilation stacking unobserved, level lifts are identities.  The
theorem to prove (or the certificate to produce per row) is the
multiplier-closed orbit-count bound; DLI-CLOSE-4 poses exactly this.
