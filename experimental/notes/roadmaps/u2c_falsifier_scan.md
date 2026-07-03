# U2-C falsifier scan — toy-scale attack on the giant-regime dichotomy

- **Status:** IN PROGRESS (pre-registered before running). Sibling of
  `u2c_giant_block_statement.md`; consumer = node
  `x4b_moment_trade_exclusion` (closure-plan piece (C), the giant regime).
- **Verifier:** `experimental/scripts/verify_u2c_falsifier_scan.py`
  (single process, laptop-bounded; recomputes every reported hit's
  power sums exactly + reclassifies; deterministic seeds; PASS/FAIL/scale).

## What is being falsified

**U2-C (dichotomy exit).** In the tame giant regime — `n` a 2-power,
tame domain `D` a coset of `mu_n` with `n | q-1`, `q >> n`, block size
`b >= t+1` with `t` comparable to `b` (up to `~n/2`) — every
`t`-null block `B ⊂ D` (i.e. `e_1(B)=...=e_t(B)=0`, equivalently the
first `t` power sums vanish since `char = q > t`) is a disjoint union
of full `mu_M`-cosets with `2`-power `M | n`, `M > t` (the already-
charged quotient staircase). A **primitive** `t`-null block (`t`-null
but not such a coset union) at any admissible-shaped toy analogue
**falsifies U2-C**.

## Structural reduction used (exact, char q > t)

Identify `mu_n = {zeta^s}` with exponents `S ⊂ Z/n`, `zeta` a primitive
`n`-th root of unity in `F_q`. Then `p_r(B) = sum_{s in S} zeta^{rs}`
is the indicator DFT at frequency `r`; `t`-null ⟺ the 0/1 word
vanishes at frequencies `r = 1..t` (a BCH-type cyclic code; BCH bound
gives min weight `>= t+1`, matching `b >= t+1`).

**Two facts that make the scan sharp and cheap:**

1. **Coset = residue-class union.** The `2`-power subgroups `mu_M`
   with `M > t` all *contain* the smallest one, `mu_{M0}` with
   `M0 = ` next `2`-power `> t`. So *every* dictionary block's support
   `S` is a union of cosets of `mu_{M0}`, i.e. a union of residue
   classes mod `n/M0`. For `n=64,t=8`: `M0=16`, classes **mod 4**
   (invariance under `+4`). For `n=128,t=12`: `M0=16`, classes
   **mod 8** (invariance under `+8`). Classification is a one-line
   translation-invariance test. Dictionary weights are multiples of
   `M0` (16), so in the window any `t`-null block of weight
   `∉ {16,32,48,64,...}` is *automatically primitive* (a falsifier).
2. **Complement duality** (handle 1): `L_B · L_{D\B} = X^n - gamma`,
   so `B` `t`-null ⟺ `D\B` `t`-null; weight `b` ↔ weight `n-b`. With
   BCH min-weight `t+1`, the entire spectrum is covered by searching
   `b ∈ [t+1, n/2]`. For `n=64,t=8`: `b ∈ [9,32]`.

## Toy parameters (deterministic)

Primes `q ≡ 1 (mod n)`, `q >> n`, one primitive `n`-th root `zeta` each:

- **Scale 1: n=64, t=8.** q ∈ {2147483713 (~2^31), 68719477313 (~2^36),
  1099511628161 (~2^40)}. Window `b ∈ [9,32]`.
- **Scale 2 (escalation, only if scale 1 clean): n=128, t=12.**
  q ∈ {2147483777, 68719484929, 1099511628161}. Window `b ∈ [13,64]`.

zeta = g^{(q-1)/n}, g = least primitive root; recorded + reverified.

## Search methods (single python process, < ~2 GB)

- **(M) Trade-level MITM** for `t`-null 0/1 blocks. Split exponents
  into halves H1,H2. Per target weight `b`, balanced split `(b1,b2)`;
  per half-subset store a 64-bit key mixing two random `F_q` linear
  forms of the `t` power sums; `p_r(S1)+p_r(S2)=0` ⟺ key match. Every
  key match is **re-verified exactly** (recompute all `t` power sums
  mod q on the reconstructed support) — the searcher is a filter, the
  verifier is ground truth. Coset hits (mod-`n/M0` classes) are the
  positive control.
  - **Coverage:** exhaustive for `b ≤ b_exh` (hash side `≤ C(32,8)=1.05e7`,
    i.e. `b ≤ 16` at n=64); randomized-sampled for larger `b`
    (report sample size + honest coverage, since sampling can only
    *find* a falsifier, not certify absence). Absence at `b ≤ b_exh`
    is a genuine certificate for the auto-primitive small-weight window.
- **(A) Antipodal-lift / X-6 mechanism.** In the *prime* field (not an
  extension), enumerate sparse `E ⊂ Z/n` (weight 3–6) with
  `sum_{e∈E} zeta^{re} = 0` for `r = 1..r_max`; separate the char-0-
  trivial relations (those containing an antipodal pair `{e, e+n/2}`,
  since `zeta^{n/2} = -1`) from any **primitive** vanishing sum. X-6
  needed `2^k ∤ p-1` (extension escape); here `n | q-1` puts `mu_n`
  directly in `F_q` — we test whether extra (resultant-divisibility)
  relations reach the prime field and whether they lift (antipodal
  closure) into a `t`-null non-coset block.

## Pre-registered interpretation

- **All hits coset-structured (mod-`n/M0` unions), no primitive
  first-moment relation** ⟹ U2-C's dichotomy exit survives at toys;
  statement graduates to GPT Pro as **X-7** for proof.
- **Any primitive `t`-null hit** ⟹ **U2-C falsified at toy scale**;
  emit the block, its locator coefficient profile, and its sparse-
  relation anatomy — that becomes the X-7 brief's counterexample seed.
- **Hits only via antipodal-lift in special fields** ⟹ characterize
  the field condition (the `n | q-1` door question, handle 4).

## Results

_(filled incrementally by the verifier; PASS = no primitive hit /
falsifier correctly absent, FAIL = primitive hit found.)_

_pending — scale 1 running._
