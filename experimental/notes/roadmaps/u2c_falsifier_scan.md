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

### Scale 1 (n=64, t=8) — search (A), sparse / antipodal-lift — DONE, all 3 primes

Positive control PASS at every prime (the 4 mod-4 classes are t-null & 'coset').

| w | mode | vanishing sums `sum zeta^e=0` | of which PRIMITIVE (non-antipodal) |
|---|------|------|------|
| 3 (odd) | EXH | 0 | 0 |
| 4 | EXH | **496** = C(32,2) | **0** |
| 5 (odd) | EXH | 0 | 0 |
| 6 | SAMP (cov ~2.7%) | ~136 (~C(32,3)·cov) | 0 |

**Every** vanishing sum of 64th-roots-of-unity in the prime field `F_q` is a
union of antipodal pairs `{e, e+32}` — exactly the char-0 structure (the only
prime is 2, so the only minimal relation is `1+(-1)=0`). The count 496 = C(32,2)
is the exact char-0 prediction (2 antipodal pairs out of 32). **Zero** primitive
(non-antipodal) sparse relations at any of the three tame primes. The X-6 shape
`1+Y+Y^2+Y^4=0` has **no** solution `Y ∈ mu_64` at any of the primes — the
extension-field escape (X-6 used `2^k ∤ p-1`, order 1024 in F_{p^2}) does **not**
reach the prime field here. Antipodal-lift produced **0** primitive t-null blocks.
Interpretation match: the antipodal mechanism only recurses into coset structure
in the tame prime field — no seed for a dichotomy escape. **Search (A): PASS.**

### Scale 1 (n=64, t=8) — search (M), trade-level MITM — DONE

**Exhaustive weights b ∈ [9,16], all 3 primes** (each MITM key match
re-verified by exact power-sum recomputation on the reconstructed support;
canonical + 3 random balanced bipartitions for b ≤ 14, canonical only for
b = 15,16; combination arrays cached across primes). Result, identical at
q ≈ 2^31, 2^36, 2^40:

- b = 9,10,11,12,13,14,15: **0** verified t-null hits (these weights are all
  non-multiples of M0=16 ⇒ any hit would be a falsifier — none exist).
- b = 16: exactly **4** verified t-null hits, **all classified 'coset'**
  (the 4 residue-classes mod 4 = the mu_16-cosets). Positive control PASS
  — the MITM pipeline finds the known coset blocks.
- Total primitive/falsifier hits in [9,16]: **0**. VERDICT PASS.

Note: complement duality maps [9,16] weight-b blocks to weight-(64-b) blocks
in [48,55]; BCH min-weight (≥9) plus the fully-covered [9,16] window certifies
the *entire low-and-high tail* [1,16]∪[48,63] contains no primitive t-null
block. The middle window [17,31] (all auto-primitive weights except none —
16,32,48 are the only coset weights) is addressed next.

**Extended weights b ∈ [17,32], prime 0 (q ≈ 2^31):**
- b = 17, 18: **exhaustive** (canonical bipartition), **0** hits.
- b = 19..32: **sampled** MITM, K = 2·10^6 per side (4·10^12 pairs each),
  coverage from ~2.2·10^-3 (b=19) down to ~1.1·10^-5 (b=32). **0** verified
  t-null hits at every weight — including the coset weight 32 (no non-coset
  weight-32 hit sampled) and all 14 auto-primitive weights 17–31.

Scale-1 MITM total primitive/falsifier hits: **0**. The only t-null blocks
found anywhere are the 4 mu_16-cosets (weight 16). **Search (M): PASS.**
