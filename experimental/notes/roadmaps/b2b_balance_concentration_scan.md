# B2b balance-point concentration scan — does the mod-p extras count spike near first-moment balance?

- **Status:** PRE-REGISTERED (this section written before running). Falsifier
  scan for DAG node `b2_modp_giant_extras` (the mod-p giant-block "extras"
  bound at prize-max). Sibling of the PROVED char-0 node
  `b1_char0_giant_coset_theorem`. Machinery inherited from the U2-C scan
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
- **Tier B** is EXHAUSTIVE within the stated weight window `b in [5,16]` at
  each swept q (0/1 blocks only); weights outside the window are not covered by
  Tier B (Tier A already gives the complete picture at n=32).
- **Tier C** coset/mean/boundary are exact arithmetic; the MITM number there is
  a sampled LOWER BOUND (finds, cannot certify absence) — coverage stated
  per row.

## Results

_(filled after running; PASS = no `>=2^20` non-coset spike above mean.)_

<!-- RESULTS-ANCHOR -->

## Reproduce (deterministic, seed 20260704)

```
python3 experimental/scripts/verify_b2b_concentration_scan.py --selfcheck
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier A      # full census n=32
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier B      # n=64 window
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier C      # n=256/512 exact+probe
python3 experimental/scripts/verify_b2b_concentration_scan.py --tier all
```
