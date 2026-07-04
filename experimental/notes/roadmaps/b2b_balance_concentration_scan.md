# B2b balance-point concentration scan — does the mod-p extras count spike near first-moment balance?

- **Status:** DONE — 39/39 rows PASS (B2b not falsified; no concentration, no
  crossing spike; see Results + Verdict). Interpretation/thresholds were
  pre-registered before running; the one design amendment (Tier B window) is
  disclosed inline. Falsifier scan for DAG node `b2_modp_giant_extras` (the
  mod-p giant-block "extras" bound at prize-max). Sibling of the PROVED char-0
  node `b1_char0_giant_coset_theorem`. Machinery inherited from the U2-C scan
  (`u2c_falsifier_scan.md`); this scan differs in ONE decisive way — it runs
  **at** the first-moment balance point, not far above it.
- **Verifier / scanner (one file):**
  `experimental/scripts/verify_b2b_concentration_scan.py`
  (single process, memory ceiling ~2 GB, deterministic seed 20260704;
  recomputes every exact count, re-verifies every t-null hit by direct
  power-sum evaluation, PASS/FAIL per row).

## What is being falsified

**B2b (no-concentration form).** At official prize-max rows the count of
**non-coset-union** t-null blocks (the finite-field-only "extras" — see the
Frobenius gap in `b1`) is `<= n^3 = 2^123`, a fixed arithmetic cushion above
the balanced first-moment mean. The prize-max giant regime sits within ~2% of
the counting threshold (`t log2 q ~ 2.15e12` vs `log2(2^n) ~ 2.2e12`), so pure
counting can never close it; B2b is the claim that **no `2^{123}`-fold
concentration above the balanced mean occurs**.

**Falsifier (pre-registered target).** A scaled toy row, sitting **near its own
first-moment balance point**, at which the observed non-coset t-null count
exceeds the balanced mean (plus the exactly-counted known classes) by a large
factor — pre-registered threshold `>= 2^{20}` above `mean+known` **and** an
absolute non-coset count `>= 2^{20}`. Such a spike would be B2b FALSIFIED at
scaled parameters; its excess blocks' anatomy would be the "sixth guise" seed.

## Contrast with the earlier U2-C scan (why this one is different)

The U2-C scan ran at `q ~ 2^31..2^40` with `n=64/128`, i.e. `t log2 q` FAR
above `n` (`8*31=248 >> 64`) — deep in the regime where the random mean
`2^n/q^t` is astronomically tiny, so *any* hit is structural. That scan
confirmed the char-0 dichotomy survives where counting is trivially safe.
**B2b lives at the opposite edge:** `t log2 q ~ n`, where the random mean is
`O(1)` and the coset class (a fixed `2^{n/M0}`) is comparable to it. The whole
question is whether, *precisely where counting is marginal*, a non-coset class
concentrates. This scan reproduces that near-critical ratio at toy scale and
**sweeps q through the balance point from below to above**.

## Structural frame (exact, char q>t; inherited from U2-C)

`mu_n = {zeta^s}`, `n = 2^s`, `n | q-1`, `zeta` = least-primitive-root
`^((q-1)/n)`. For `S subset Z/n`, `p_r(S) = sum_{s in S} zeta^{rs}` (indicator
DFT at frequency r); **t-null `<=>` `p_1=...=p_t=0` mod q**.

- **Coset class (the charged / char-0 class).** `M0 =` least 2-power `> t`;
  `stride = n/M0`; `R = n/M0`. Every char-0 t-null block is a union of
  `mu_{M0}`-cosets (`b1` theorem), i.e. a `Z/n` support invariant under
  `+stride`. There are exactly **`2^R - 1` nonempty** such blocks, t-null over
  **any** field with `n|q-1` (q-independent). CLASSIFY: `S` is `coset` iff
  invariant under `+stride`; every other t-null block is a **non-coset extra**
  (the B2b quantity).
- **Balanced mean (first moment).** A uniform random subset is heuristically
  t-null with probability `q^{-t}`; hence
  `E[#non-coset t-null] ~ (2^n - 2^R) q^{-t} ~ 2^n / q^t` (total), and
  `~ C(n,b) q^{-t}` at fixed weight b (minus the coset count at coset weights).
  **Balance point:** `n = t log2 q` <=> mean_total `~ 1`.
- **Boundary / zero-sum class (QA.25 / X-8).** The finite-field boundary
  extras: at scale `M0`, partial (sub-coset) patterns whose quotient-value sum
  vanishes. In the full census these appear AS non-coset hits; we report their
  quotient-profile anatomy (per-`mu_{M0}`-coset occupancy vector) rather than
  assume the giant-regime formula. QA.25 giant-regime model, for reference:
  `boundary_mass ~ 2^{R/2} / q^e`, `e = floor(t/M0)`.
- **Complement duality** `L_B L_{D\B} = X^n - gamma` => b <-> n-b symmetry
  (used as an internal consistency check, not to restrict the census).

## Design — scaled balance-point rows

### Tier A — FULL exhaustive t-null census (flagship), n=32
`n=32` (`2^s`), half-domain 16 => **full-subset MITM enumerates EVERY t-null
block** (all `2^32` subsets, no weight restriction): hash all `2^16` subsets of
one half by their exact `(p_1..p_t)` vector, match against the negated vectors
of the other half. Exact and complete. Three t-values, EACH swept through its
OWN balance point `log2 q = n/t`:

| row | t | M0 | R | coset unions `2^R-1` | balance `log2 q` | q sweep (primes `=1 mod 32`) |
|-----|---|----|---|----|----|----|
| A2 | 2 | 4 | 8 | 255 | 16.0 | 97,193,577,2081,8353,16417,32801,**65537**,131297,262337,524353 |
| A3 | 3 | 4 | 8 | 255 | 10.7 | 97,193,257,577,1153,**2081**,4129,8353,32801,262337 |
| A4 | 4 | 8 | 4 | 15 | 8.0 | 97,193,**257**,577,1153,2081,4129,16417,65537 |

Sweep spans far-below balance (mean up to `~2^18.8` at A2/q=97 — still
enumerable, `<~5e5` hits) to above balance (mean `<1`). **Per q**: exact total
t-null count, coset count, non-coset count, mean, ratio non-coset/mean; and the
quotient-profile anatomy of non-coset hits (capped sample stored, full tally by
signature). Directly answers: does the non-coset count track the mean
(no concentration) or spike, and does anything happen sharply AT the crossing?

### Tier B — fixed-weight window at larger n (corroboration), n=64, t=4
Full census infeasible (`2^32`/half). Exhaustive **fixed-weight all-split**
MITM at the near-minimal weights: every split shape `(w1, w2)`, `w1+w2=b`,
across the two halves is searched (smaller side hashed, larger side streamed
via vectorized outer-adds), so the window census is a genuine certificate —
NOTE this is *stronger* than the U2-C engine, whose balanced-split
(`b//2, b-b//2`) search plus random bipartitions covers unbalanced splits only
probabilistically. 64-bit mixed key + exact re-verification of every collision
by two independent exact methods. `M0=8`, so weights `5,6,7,9,10` are not
multiples of `M0` — a t-null block there is automatically primitive. Window
**`b in [5,10]`** at 7 primes `log2 q in {7,9,11,13,15,16,17}` swept through
balance (`log2 q=16`).

> **Amendment (disclosed; made after Tier A ran, before any Tier B result):**
> the originally registered Tier B window `[5,16]` with the balanced-split
> U2-C engine was replaced by the all-split engine with window `[5,10]` — a
> balanced-split engine at `b in [11,16]` would NOT have been exhaustive
> (it misses unbalanced splits), and mislabeling it "exhaustive" is worse
> than an honestly smaller window; `[5,10]` is what is affordable all-split
> within the single-process/2GB budget. The falsifier target (near-minimal
> weights `b in [t+1, t+small]`) is unchanged. The new engine is brute-force
> cross-checked at `n=16, t=2` against `O(2^16)` enumeration in `--selfcheck`.

### Tier C — exact known-class + honest probe at the prompt scales, n=256/512
`n=256,t=16` and `n=512,t=32` (the prompt's scaled analogues, balance
`log2 q~16`). Enumeration is impossible (`C(256,17) ~ 2^{97.6}`). We report
**exactly** (no enumeration): coset count `2^R-1=255`, mean `2^n/q^t`, the
QA.25 boundary model. A SAMPLED MITM probe at the minimal weight is included
but is **falsifier-only and near-vacuous** (coverage `~2^{-77}`): it can catch
an astronomically large concentration and nothing subtler — labeled honestly.

## Pre-registered interpretation & PASS/FAIL

Per row we report `(known coset | non-coset observed [EXH or LB] | balanced mean
`2^n/q^t` | ratio observed/mean)`.

- **PASS (no-concentration survives):** non-coset observed `<= (mean+1)*n^2 +
  n^3` at every swept q — i.e. within a small polynomial factor of the mean, no
  `2^{20}` spike. The scan then *calibrates the concentration exponent*
  `log2(non-coset / mean)` across the sweep and reports whether the (small)
  excess is smooth or transitions at the crossing.
- **FAIL (B2b falsified at scaled params):** at some near-balance q, non-coset
  observed `>= 2^{20} * (mean+1)` AND `>= 2^{20}`. Emit every excess block's
  anatomy (quotient profile; antipodal closure; is it a NEW structured class —
  the sixth-guise question). Highest-value outcome.
- Also recorded: does the count spike EXACTLY at the balance crossing
  (phase-transition shape) or decay smoothly (power-law, mean-tracking).

## Coverage statement (exact, honest)

- **Tier A rows are EXHAUSTIVE and COMPLETE** — every t-null block of `mu_32` is
  enumerated at every swept q; the non-coset counts are exact, not lower bounds.
- **Tier B** is EXHAUSTIVE within the (amended, see above) weight window
  `b in [5,10]` at each swept q (0/1 blocks only; ALL split shapes); weights
  outside the window are not covered by Tier B (Tier A already gives the
  complete all-weight picture at n=32).
- **Tier C** coset/mean/boundary are exact arithmetic; the MITM number there is
  a sampled LOWER BOUND (finds, cannot certify absence) — coverage stated
  per row.

## Results — ALL TIERS RUN, ALL PASS

_(PASS = no `>=2^20` non-coset spike above mean; all runs seed 20260704.)_

Selfcheck PASS: census engine matches `O(2^8)` brute enumeration at `n=8`;
the Tier B all-split window engine matches `O(2^16)` brute enumeration at
`n=16,t=2,q=193` per-weight exactly. Every reported hit re-verified by direct
power-sum evaluation; Tier A coset counts matched `2^R-1` exactly at all 30
rows (positive control); Tier B found all 8 `mu_8`-cosets at all 7 primes;
Tier C single-coset positive controls t-null at both rows.

### Tier A — FULL census, n=32 (EXHAUSTIVE at every row) — 30/30 PASS

`t=2` (`M0=4`, coset unions `2^8-1=255`, balance `log2 q=16`):

| q | log2 q | total t-null | coset | non-coset (EXACT) | mean `2^n/q^t` | nc/mean |
|---|---|---|---|---|---|---|
| 97 | 6.60 | 455743 | 255 | 455488 | 2^18.80 | 2^-0.00 |
| 193 | 7.59 | 116511 | 255 | 116256 | 2^16.82 | 2^0.01 |
| 577 | 9.17 | 14495 | 255 | 14240 | 2^13.66 | 2^0.14 |
| 2081 | 11.02 | 1471 | 255 | 1216 | 2^9.95 | 2^0.29 |
| 8353 | 13.03 | 575 | 255 | 320 | 2^5.94 | 2^2.38 |
| 16417 | 14.00 | 543 | 255 | 288 | 2^3.99 | **2^4.18** |
| 32801 | 15.00 | 255 | 255 | **0** | 2^2.00 | 0 |
| 65537 | 16.00 (balance) | 255 | 255 | **0** | 2^-0.00 | 0 |
| 131297/262337/524353 | 17–19 | 255 | 255 | **0** | 2^-2..2^-6 | 0 |

`t=3` (balance `log2 q=10.67`): non-coset 6336 (q=97, ratio 2^0.43) → 768
(q=193) → 128 (q=257, ratio 2^-0.98) → 64 (q=577, ratio 2^1.52) → **0 at ALL
q >= 1153** (`log2 q=10.17`) through 2^18. 10/10 PASS.

`t=4` (`M0=8`, coset unions 15, balance `log2 q=8`): non-coset 160 at q=97
(ratio 2^1.72) → **0 at ALL q >= 193** through 2^16. 9/9 PASS.

**Shape of the crossing (the pre-registered question):** NO spike at the
balance crossing — the opposite. Far below balance the non-coset count sits
**exactly on** the balanced mean (ratio 2^0.00–2^0.3); approaching balance it
decays FASTER than the mean until only field-specific structured residues
survive (max excess ratio 2^4.18, absolute count 288 — vs cushion
`n^3 = 2^15`); at/above the crossing the count hits the exact coset floor
`2^R-1` and stays there. The transition to the floor completes strictly BELOW
nominal balance in all three sweeps (last non-coset survivor at
`t log2 q ~ 28/30.5/26.4` out of `n=32` for t=2/3/4). The near-balance excess
is granular: hits arrive in symmetry-orbit quanta (multiples of 32), which is
also why slightly-below-balance rows with mean ~4 show 0. Calibrated
concentration exponent over 30 exhaustive rows: `log2(nc/mean) <= 4.2`.

**Anatomy of the non-coset extras (sixth-guise question):** far below balance
the extras are generic (all partial-occupancy profiles — the random
mean-tracking population). The LAST survivors near the crossing are strongly
structured: at `t=2,q=16417` all 288 have per-class partial occupancy
`(2,2,...,2)` — unions of 5–8 two-element in-class fiber patterns (pair
relations inside single `mu_{M0}`-quotient classes); at `t=3,q=577` the 64
survivors are antipodal `(2,2,2,2,2,2)`-profile blocks. Both are exactly the
X-8/QA.25 boundary-scale zero-sum mechanism, already counted in the budget.
**No new (sixth-guise) class appeared at any exhaustive row.**

### Tier B — n=64, t=4, EXHAUSTIVE all-split window b in [5,10] — 7/7 PASS

7 primes `log2 q in {7.59, 9.17, 11.05, 13.06, 15.00, 16.00, 17.01}` (balance
16). At every prime: weights 5,6,7,9 EMPTY; weight 8 = exactly the 8
`mu_8`-cosets; weight 10 empty EXCEPT q=193 (far below balance): **192
non-coset t-null blocks vs per-weight mean `C(64,10)/q^4 = 2^6.77 ~ 109`,
ratio 2^0.53** — mean-tracking, generic profiles (no structure). The
sub-coset-weight window is CERTIFIED empty at the 6 primes `q >= 577`; at
balance itself the whole window `[5,10]` contains only the coset dictionary.

### Tier C — prompt scales n=256/512 at balance q=65537 — exact + probe

Exact (no enumeration): coset unions `2^R-1 = 255` both rows; balanced mean
`2^n/q^t = 2^-0.00` (both — exactly at balance); QA.25 boundary model
`2^{R/2}/q^e = 2^-12.00` (both); cushions `n^3 = 2^24 / 2^27`. Known classes
fit with the full cushion intact. Sampled probe at `b=t+1` (K=120000/side):
0 hits at coverage `~2^-50.7` (n=256) and `~2^-136.2` (n=512) — HONEST LABEL:
falsifier-only, certifies nothing.

## VERDICT — B2b's no-concentration form NOT falsified; 39/39 rows PASS

1. **No concentration anywhere**: max non-coset/mean ratio 2^4.18 (at absolute
   count 288 << `n^3`); the pre-registered `>=2^20` falsifier threshold was
   never approached within 15 bits, at any covered row.
2. **No phase-transition spike at the crossing** — the non-coset count decays
   through balance AHEAD of the mean and lands on the exact coset floor
   strictly before `t log2 q = n`; above balance every t-null block is a coset
   union (the b1 char-0 dictionary), at every exhaustively covered row.
3. **Every structured survivor identified as X-8/QA.25 boundary-type**
   in-class pair/zero-sum patterns. No sixth guise.
4. Calibration for the (B)-side proof brief: toy concentration exponent
   `<= ~4` bits vs the 123-bit cushion, and the extras die BEFORE balance —
   consistent with B2b holding at prize-max with the entire cushion intact.

**Honest coverage residual:** exhaustive coverage = n=32 all weights (30 q-rows)
+ n=64 weights 5–10 (7 q-rows). n=64 weights >10, and everything non-exact at
n=256/512, are NOT covered (probe coverage `2^-50.7`/`2^-136.2` is vacuous).
A mechanism first activating above n=64, or only at weights >10 of n=64, is
not excluded — that residual is what the divisor-frame counting route in the
`b2_modp_giant_extras` node must close.

## Reproduce (deterministic, seed 20260704)

```
python3 experimental/scripts/verify_b2b_concentration_scan.py --selfcheck
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier A      # full census n=32
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier B      # n=64 window
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier C      # n=256/512 exact+probe
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier all
```
