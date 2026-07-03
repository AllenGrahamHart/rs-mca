# QA.16 scoping packet: the multiplier pipeline is impossible — rank-1 mod p, and no good multiplier exists

- **Status:** mixed, labelled per section. Lemmas 0-1 and Proposition 4:
  PROVED (full proofs written below). Theorem 2 (nonexistence at three
  toys): PROVED by exhaustive finite computation, re-run by the verifier.
  Section 4 (scale extrapolation): [HEURISTIC], labelled. This packet is
  the SPEC CORRECTION for DAG nodes `multiplier_exactness` /
  `multi_multiplier_reduction` announced on PR #178; the DAG file itself
  is NOT edited here (edits happen on integration, per claiming protocol —
  this note is the source of record).
- **Verifier:** `experimental/scripts/verify_multiplier_impossibility.py`
  (deterministic, stdlib-only; re-derives every quantitative claim below;
  all PASS).
- **Corrects also:** the cost expectation in the QA.16 queue entry
  (`execution_queue.md` Tier D7) and, as posed, QA.19 part (i)
  (`certifier_uniformity` uniform-multiplier existence) — see SS6.
- **Context:** `proof_sketch/s2_paid_ledger.md` SS3 (zones, norm threshold
  `p > (2l')^{N'/2}`, `l' = rho N' + 1`), `evidence_plan_codex.md` E24
  (BKZ hunt), `execution_queue.md` QA.16-QA.20 (Tier D7/D8).

## 0. Pinned notation

```text
p          odd prime; F_p^* its unit group.
mod± p     the balanced residue: bal(a) = the unique representative of
           a mod p in (-p/2, p/2).  bal(-a) = -bal(a).
zeta       an element of EXACT multiplicative order N' in F_p^* (N' | p-1);
           mu_N' = <zeta> the order-N' subgroup.  N' is a 2-power
           throughout (official rows are 2-power domains), so
           zeta^{N'/2} = -1 in F_p.
v          a ternary vector: v in {-1,0,+1}^{N'}; wt(v) = |supp(v)|.
K_p        the collision (kernel) lattice {v in Z^{N'} :
           sum_x v_x zeta^x = 0 mod p}   (E24's object).
P          the cyclotomic relation module: Z-span of e_x + e_{x+N'/2},
           x = 0..N'/2-1.  Fact (proved in SS5): for 2-power N', P is
           EXACTLY the module of relations valid for every p (equivalently
           over C), and its ternary elements are exactly the v with
           v_{x+N'/2} = v_x for all x.
l'         = rho N' + 1; this packet instantiates rho = 1/2, l' = N'/2+1,
           per the task threshold p/(4(N'/2+1)); the SS4 boundary statement
           is given for general rho.
GOOD c     c in F_p^* is a good multiplier if
           max_{0 <= x < N'} |bal(c zeta^x)| <= p/(4 l').
           This depends only on the coset c*mu_N', not on the choice of
           generator zeta (the max runs over the whole coset), so
           "any element w of exact order N'" gives the same counts.
```

## 1. What is being corrected

The proposed lattice-certificate pipeline (DAG nodes `multiplier_exactness`,
`multi_multiplier_reduction`, feeding `integer_code_distance_cert` /
`lattice_cone_certificate`) ran:

1. a good multiplier `c` makes all reduced residues
   `r_x = bal(c zeta^x)` simultaneously small (`<= p/(4l')`), so any
   sparse ternary mod-p relation becomes an EXACT integer relation
   (`multiplier_exactness`);
2. `k` different multipliers give `k` exact integer relations, hence a
   `k x N'` integer matrix whose ternary kernel contains all collisions;
   Gilbert-Varshamov counting at `k ~ 10` (each row "worth ~log p bits")
   then excludes all weights `<= 2l'` (`multi_multiplier_reduction`).

Both steps fail, for different reasons:

- **Rank-1 (SS2):** the `k` mod-p relations are scalar multiples of one
  another — rank 1 over `F_p`, zero new information mod p, for every `k`.
  The "k log p bits" count presupposed an independence that never holds.
- **No good multiplier exists (SS3-SS4):** exhaustive search over ALL
  `c in F_p^*` at three toys finds ZERO good multipliers, with the best
  achievable max-residue a factor 4.75-8.55 ABOVE the threshold; the
  counting heuristic says the deficit is overwhelming (2^{-hundreds}) at
  every prize-relevant `N'`. So step 1's hypothesis is never satisfiable
  where it is needed, and step 2's integer matrix never exists.

What survives — the multiplier-FREE direct meet-in-the-middle certificate,
the exact branch-and-bound solver, and the BKZ search — is stated
precisely in SS5, with corrected costs.

## 2. Two lemmas [PROVED]

**Lemma 0 (exactness bridge — true but vacuous).** Fix `c in F_p^*` and
set `r_x = bal(c zeta^x)`. If `max_x |r_x| <= p/(4l')`, then every ternary
`v` with `wt(v) <= 2l'` and `sum_x v_x zeta^x = 0 mod p` satisfies the
exact integer identity `sum_x v_x r_x = 0`.

*Proof.* `sum_x v_x r_x = c * sum_x v_x zeta^x = 0 mod p` (each
`r_x = c zeta^x mod p`). Also `|sum_x v_x r_x| <= wt(v) * max_x |r_x|
<= 2l' * p/(4l') = p/2 < p`. The only multiple of `p` of absolute value
`< p` is `0`. QED.

The lemma is correct as stated in the DAG node; SS3-SS4 show its
hypothesis is unsatisfiable at every toy tested and (heuristically) at
every prize-relevant `N'` — the node is true-but-vacuous, dead as routed.

**Lemma 1 (rank-1: k multipliers carry no new mod-p information).** Fix
`p`, `zeta` of exact order `N'`, and any `c_1, ..., c_k in F_p^*`. Let `R`
be the `k x N'` integer matrix `R_{i,x} = bal(c_i zeta^x)`. Then:

1. `R = c z^T mod p` where `c = (c_i)_i`, `z = (zeta^x)_x`: an outer
   product, so `rank_{F_p}(R) = 1`;
2. for every `v in Z^{N'}`: `R v = 0 mod p` (all `k` coordinates)
   `<=>` `sum_x v_x zeta^x = 0 mod p`.

In particular the `k` mod-p constraints are, for every `k`, exactly the
single base constraint: the mod-p kernel of the stacked system equals
`K_p`.

*Proof.* `R_{i,x} = c_i zeta^x mod p` by definition of the balanced
residue, giving (1). For (2): `(Rv)_i = c_i * sum_x v_x zeta^x mod p`,
and `c_i` is invertible. QED.

**Where the pipeline's integer claim breaks.** The exact integer kernel
`{v : Rv = 0 in Z}` IS a sublattice of `K_p` (an exact relation reduces
mod p). The pipeline claimed the converse inclusion for sparse ternary
vectors — that every collision `v in K_p` with `wt(v) <= 2l'` satisfies
`Rv = 0` exactly. By Lemma 0 that follows IF the `c_i` are good; without
goodness, `v . r^{(i)}` is merely a multiple of `p`, generally nonzero,
and the claim is false. So `multi_multiplier_reduction` fails on both
horns: mod p the `k` rows are one row (Lemma 1); over `Z` the kernel
claim needs good multipliers, which do not exist (SS3-SS4).

**Concrete demonstration (verifier, exhaustive).** At `(N', p) = (8, 41)`
(chosen small enough to have extras) the ternary part of `K_p` has 160
elements: 80 cyclotomic and 80 non-cyclotomic collisions. For the tested
multipliers `c in {2, 3, 5, 7}` (none good; no good c exists at `(8,41)`
at all — exhaustive best `M(c) = 14` vs threshold `41/20 = 2.05`; also
forced by pigeonhole, 8 distinct coset elements cannot fit in
`+-{1, 2}`), 176 of the 320 (collision, multiplier) pairings are NONZERO
multiples of `p`: the claimed exact integer relations simply do not
hold. Tiny-`p` accidents run in both directions — 16 of the 80 extras
happen to pair to zero against all four rows, so even the stacked
`4 x 8` INTEGER system retains non-cyclotomic ternary kernel vectors
(per-extra distribution of failing rows: 16/4/8/52/0 for 0/1/2/3/4).
At `(8, 257)`, by contrast, the FULL ternary kernel (all `3^8` vectors,
every weight) is exactly the 80 cyclotomic vectors — a bonus PROVED
fact: folding `zeta^{x+4} = -zeta^x` collapses any ternary relation to
`a + 4b + 16c + 64d = 0 mod 257` with digits in `[-2, 2]`; since
`2(1+4+16+64) = 170 < 257` the congruence is an exact equation, and
base-4 digit uniqueness (reduce mod 4 repeatedly) forces
`a = b = c = d = 0`, i.e. `v_x = v_{x+4}`. So certificate C(8) of SS5.2
holds unconditionally at `(8, 257)`.

## 3. Theorem 2: no good multiplier exists at the toys [PROVED by exhaustion]

For each pair below, `w` is an element of exact order `N'` (found
deterministically; by the coset remark in SS0 the counts are independent
of which one), `l' = N'/2 + 1`, and ALL `c in F_p^*` were enumerated.
`M(c) = max_x |bal(c w^x)|`; good means `M(c) <= p/(4l')`.

```text
 N'   p       l'   p/(4l')     #good c   min_c M(c)   ratio best/(p/4l')
  8   257      5     12.85        0         61  (c=13)      4.75
 16   65537    9   1820.47        0      15556  (c=3313)    8.55
 16   12289    9    341.36        0       2890  (c=821)     8.47
```

Best cosets (balanced residues, sorted):

```text
 (8, 257),   c = 13:   +-{13, 49, 52, 61}
 (16, 65537), c = 3313: +-{3313, 3853, 3889, 12529, 13252, 15412, 15421, 15556}
 (16, 12289), c = 821:  +-{821, 1273, 2250, 2262, 2352, 2550, 2569, 2890}
```

(Cosets are symmetric under negation because `zeta^{N'/2} = -1`; only
`N'/2` magnitudes are free — this drives the refined heuristic in SS4.)

**Correction to the prior spot-check.** The task spec's parenthetical
("a prior spot-check found best = threshold+1 in all three cases") does
NOT reproduce: the exhaustive best values are 61 vs threshold-floor 12,
15556 vs 1820, and 2890 vs 341 — factors 4.75 / 8.55 / 8.47 above the
threshold, i.e. `min_c M(c) ~ 0.47 * (p/2)` in all three cases. The
nonexistence conclusion is therefore STRENGTHENED: failure is not
marginal but by a large factor. [EXPERIMENTAL observation, not relied on
anywhere: the observed best sits at 0.94-0.95 of `p/4` in all three
cases, so a mis-thresholded reading (`p/4` in place of `p/(4l')`) is a
plausible source of the earlier figure.] The refined random model of SS4
predicts `min_c M(c) ~ 54 / 11585 / 2678` for the three pairs — the
right scale (observed/predicted = 1.14 / 1.34 / 1.08), consistent with
"no structure rescues the multiplier".

**These toys are honest miniatures.** All three sit BELOW the s2 norm
threshold: `(2l')^{N'/2} = 10^4 > 257` and `18^8 = 1.1e10 >> 65537,
12289`. That is exactly the zone-(b)-like regime (`p < (2l')^{N'/2}`)
where the pipeline was supposed to operate; see the boundary statement
in SS4.

## 4. The counting heuristic at scale [HEURISTIC]

Model each residue `bal(c zeta^x)` as uniform on `(-p/2, p/2)`. A single
residue is `<= p/(4l')` in absolute value with probability `~ 1/(2l')`.
Treating the `N'` residues as independent (they are NOT — see below):

```text
E[#good c]  ~  p * (1/(2l'))^{N'}          (naive; the task-pinned form)
```

Because `zeta^{N'/2} = -1` forces `r_{x+N'/2} = -r_x` exactly, only
`N'/2` magnitudes are free; the same model applied to the free half
gives the refined form:

```text
E[#good c]  ~  p * (1/(2l'))^{N'/2}        (refined)
```

At `log2 p = 250`, `rho = 1/2` (`l' = N'/2+1`), machine-evaluated:

```text
 N'    log2 E (naive)     log2 E (refined)
  32       +87.20             +168.60
  64      -136.84              +56.58
 128      -648.86             -199.43
 256     -1800.87             -775.44
 512     -4360.88            -2055.44      (supplementary row)
```

Sign crossover: naive between `N' = 44` and `46`; refined between
`N' = 78` and `80`.

**Reading, honestly.** The queue's expectation "~ -500 to -2000,
overwhelming" holds for the NAIVE column at the zone-(b)-relevant orders
`N' in {128, 256}` (and refined at 256); at `N' in {32, 64}` one or both
columns are POSITIVE — good multipliers plausibly exist there. This does
not rescue the pipeline, because of the following boundary coincidence.

**The existence boundary is the zone-(a) boundary (rate-uniformly).**
The refined existence threshold `E ~ 1` reads
`log2 p = (N'/2) log2(2l')`, i.e. `p = (2l')^{N'/2}` — LITERALLY the
prop:qfloor norm threshold that defines the zone-(a)/(b) boundary in
`s2_paid_ledger.md` SS3, at every rate `rho` (the same expression in
`l' = rho N' + 1`). So, heuristically:

```text
good multipliers exist  <=>  p > (2l')^{N'/2}  <=>  zone (a),
```

which is precisely the region where prop:qfloor already gives EXACT
counts and no certificate is needed. In zone (b) (`80 < N' < ~512` at
rho = 1/2, prize scale), where the pipeline was aimed, the expected
number of good multipliers is `2^{-199}` to `2^{-2055}` (refined) —
overwhelming nonexistence. The multiplier route's (heuristic) domain of
existence is exactly the domain where it has nothing to add.

**Ground truth vs extrapolation.** Residues within one coset are pairwise
dependent beyond the negation pairing (they lie on one multiplicative
orbit), so neither formula is a theorem. The SS3 exhaustions are the
ground truth: both formulas predict `E << 1` at all three toys (refined:
0.026 / 5.9e-6 / 1.1e-6), and the observed counts are 0; the refined
model also predicts the observed `min_c M(c)` scale within 35%. The scale
table is the extrapolation, labelled as such.

## 5. The surviving pipeline, stated precisely

### 5.1 Cyclotomic relations pinned [PROVED]

For 2-power `N'`, `Phi_{N'}(X) = X^{N'/2} + 1` is monic, so the kernel of
`Z[X]/(X^{N'}-1) -> Z[zeta_{N'}]` is `Phi_{N'} * Z[X]` reduced mod
`X^{N'}-1`, i.e. the Z-span of `X^j Phi_{N'}`, `j < N'/2` — in vector
form, exactly `P = span_Z{e_x + e_{x+N'/2}}`. Since the `N'/2` generators
have pairwise disjoint supports, an integer combination
`sum a_x (e_x + e_{x+N'/2})` is ternary iff all `a_x in {-1,0,+1}`; hence
the ternary elements of `P` are exactly `{v : v_{x+N'/2} = v_x}` and
number `sum_{j=1..m} C(N'/2, j) 2^j` at weight `<= 2m` (nonzero, counted
up to global sign: half that).

### 5.2 The direct MITM certificate — NO multiplier needed [PROVED]

**Certificate C(w) for a row `(p, N', zeta)`:** "every ternary `v` with
`1 <= wt(v) <= w` and `v in K_p` lies in `P`" — i.e. no ternary collision
of weight `<= w` beyond the cyclotomic ones.

**Proposition 4 (MITM decision procedure; sound and complete).** Let
`s = ceil(w/2)` and

```text
H_s = { (T, eps) : T subset Z_N', |T| <= s, eps in {+-1}^T },
val(T, eps) = sum_{x in T} eps_x zeta^x  mod p       (val(empty) = 0).
```

A ternary `v` with `1 <= wt(v) <= w` lies in `K_p` iff it splits as a
disjoint union of two halves `h_1, h_2 in H_s` with
`val(h_1) + val(h_2) = 0 mod p`. Hence tabulating `val` on `H_s` and
collecting all disjoint-support pairs with opposite values (including
pairs with an empty half, which catch weights `<= s` directly) finds
EVERY weight-`<= w` element of `K_p`; C(w) holds iff every collected
vector lies in `P` (the `v_{x+N'/2} = v_x` test).

*Proof.* Soundness: a colliding disjoint pair reassembles to a ternary
vector with `sum v_x zeta^x = val(h_1) + val(h_2) = 0 mod p`.
Completeness: sort `supp(v)`, give its first `ceil(wt/2) <= s` elements
(with their signs) to `h_1`, the rest (`<= floor(wt/2) <= s`) to `h_2`.
QED.

The comparison is between values IN `F_p`; the conversion to integer
relations — the only step that ever needed a multiplier — is absent.
Cost: `|H_s| = sum_{j<=s} C(N',j) 2^j ~ C(N', s) 2^s` table entries,
time ~ table size (at prize `p ~ 2^250` the expected number of random
value coincidences `|H_s|^2 / p ~ 2^{133-250}` is negligible, so the
pair-collection step does not blow up; at toy `p` it does, harmlessly).
Memory = the table; time-memory trade-offs exist but are not priced here.

### 5.3 Cost table at N' = 128 and the CORRECTED feasibility [verified arithmetic]

`log2 cost(w) = log2 C(128, w/2) + w/2` (exact, `math.comb`):

```text
  w  :  12     14     16     18     20     22     24     26     28     30
 cost: 38.34  43.46  48.38  53.12  57.69  62.11  66.40  70.55  74.59  78.52
```

Free height baseline at `(N', log2 p) = (128, 250)`: a nonzero ternary
weight-`w` combination of `mu_N'` has all archimedean conjugates
`<= w`, so `|Norm| <= w^{N'/2} = w^{64}`, and `p | Norm` is impossible
while `w^{64} < 2^250`, i.e. `w <= 14` — equivalently the proved graded
radius `d* = 7` swaps (`w = 2d`). MITM adds value from `w = 15` up.

```text
 op budget    max w    certified radius (swaps, w/2)
   2^40        12         6   (below the free d* = 7)
   2^50        16         8
   2^60        20        10
   2^70        24        12
   2^80        30        15
```

**Correction to the queue entry.** QA.16's "feasible to w ~ 24-30 at
~2^40-2^50 operations" is wrong under the pinned cost model: 2^40-2^50
buys `w = 12-16` (radius 8 swaps at `2^48.4`); `w = 24` (the radius-12
target) costs `2^66.4` naive — global-sign and `N'`-rotation symmetries
shave at most ~`2^8`, leaving ~`2^58`, with memory the binding
constraint; `w = 30` costs `2^78.5`. The radius extension 7 -> 8-10
swaps is practical today; 7 -> 12 is a serious computation, not a
routine one. (Representation-technique refinements might lower this;
[HEURISTIC], unpriced, not claimed.)

### 5.4 Toy instantiation of Proposition 4 [PROVED by computation]

At `(N', p) = (16, 12289)` and `(16, 65537)`, certificate C(8) was run
BOTH ways: full exhaustion over all ternary `v`, `1 <= wt <= 8` (up to
global sign), and the MITM procedure with `s = 4`
(`|H_4| = 34113` entries). Results, both primes:

```text
 kernel vectors of weight <= 8 (canonical, up to sign):  848
 of which cyclotomic (v_x = v_{x+8}):                    848
 non-cyclotomic ("extra") collisions:                      0
 MITM output == exhaustive output:                       yes
 predicted ternary-P count sum_{j<=4} C(8,j)2^j / 2:     848  (match)
```

So C(8) HOLDS at both toys with zero extras. This is real certification
work, not a height freebie: at `p = 12289` the norm bound only covers
`w <= 3` (`3^8 = 6561 < 12289 < 4^8`), so weights 4-8 are decided by
the MITM alone — the certified radius extends `d* = 1 -> 4` swaps, the
honest miniature of the `7 -> 12` extension at scale (QA.18's design
note asks for exactly this regime).

### 5.5 Untouched components

- **Exact branch-and-bound / pruned-exhaustion solver (QA.18):** decides
  the finite statement "no ternary kernel vector of weight `<= 2l'`
  beyond `P`" directly over `F_p`; never used a multiplier. Its
  COMPLETENESS remains the totality anchor under Reading B
  (procedure-as-determination semantics, project ruling 2026-07-03).
  Untouched by this correction.
- **BKZ search (E24):** hunts for actual short/sparse vectors in `K_p`
  (the falsifier side); built from `K_p` by pure linear algebra, no
  multiplier anywhere. Untouched.
- **LP/Delsarte (QA.18 candidate (3)):** operates on the single mod-p
  relation; unaffected in principle, though any instantiation that
  assumed the `k x N'` exact integer system must be restated against
  `K_p` itself.

## 6. Consequences for the DAG (spec correction record)

Recorded here; the JSON edits happen on integration, citing this note.

```text
multiplier_exactness       PROVABLE -> DEAD-as-routed. Lemma 0 is true
                           (proof in SS2) but its hypothesis is
                           unsatisfiable: exhaustively at all three toys
                           (SS3), heuristically at every zone-(b) N'
                           (SS4). Keep the lemma as a remark; the node's
                           role in the pipeline is void.
multi_multiplier_reduction PROVABLE -> REFUTED as stated. Rank-1 collapse
                           mod p (Lemma 1) kills the "k log p bits" GV
                           count; the integer-kernel claim requires good
                           multipliers, which do not exist. The two
                           recorded failed alternatives (scale splitting,
                           2-adic nesting) are joined by the primary
                           route.
weight_graded_mitm         survives, RESTATED multiplier-free (SS5.2,
                           Proposition 4) with corrected costs (SS5.3):
                           radius 8-10 swaps practical, 12 at ~2^58-2^66.
integer_code_distance_cert re-scoped: the object is the single mod-p
                           relation / the lattice K_p, not a k x N'
                           integer system. Certifier slate: exact solver
                           (totality anchor), MITM bands (baseline,
                           SS5.3 prices), LP/Delsarte (theory side),
                           BKZ (search side, E24).
certifier_uniformity (i)   ANSWERED NEGATIVELY as posed in QA.19
                           ("good compression multipliers exist for
                           every admissible p"): they exist for NO
                           tested p, and heuristically for no p at
                           zone-(b) N'. Uniformity must be sought in
                           the multiplier-free certifiers.
execution_queue QA.16      cost expectation corrected per SS5.3.
```

## 7. Non-claims

- No claim about relations with coefficients outside `{-1,0,+1}` or of
  weight above the stated `w`; C(w) is exactly what SS5.2 says.
- The scale tables in SS4 are [HEURISTIC]; the only PROVED nonexistence
  statements are the three finite exhaustions of SS3. The prize-scale
  nonexistence is an extrapolation — overwhelming, but not a theorem.
- No claim that a structured multiplier DESIGN for primes of special
  form is impossible; SS3 excludes ALL multipliers for the three tested
  pairs, and SS4 prices the generic count. But the pipeline required
  multipliers for EVERY admissible p (uniformity), and that is dead on
  the tested cases alone.
- No claim that `w = 24` MITM is practical on repo hardware; SS5.3
  prices it (~2^58-2^66 ops, memory-bound) and stops there. No
  representation-technique speedup is claimed.
- The toy pairs are not admissible prize rows; they are miniatures
  chosen to sit below the norm threshold (the zone-(b)-like regime).
  No transfer theorem from toys to prize scale is claimed.
- The `min_c M(c) ~ 0.47 p/2` regularity and the `~0.95 * p/4`
  observation are [EXPERIMENTAL] curiosities, relied on nowhere.
- Lemma 1 does not say the k-row INTEGER matrix has rank 1 over Q
  (generically it has rank k); only its mod-p reduction is rank 1,
  which is what the information count needed.

## 8. Verification

`python3 experimental/scripts/verify_multiplier_impossibility.py` — all
PASS, deterministic, stdlib only. Checks: [L1] rank-1 + kernel equality
at (8, 257) and (8, 41); the concrete integer-claim failure at (8, 41)
(80 extras, 176/320 nonzero pairings, per-extra distribution 16/4/8/52/0)
and the all-cyclotomic bonus fact at (8, 257); [T2] the three exhaustive
multiplier searches (counts, best values, best cosets, generator
independence, negation pairing); [H] both heuristic tables, crossovers,
the boundary coincidence with s2's zone arithmetic, toy-prediction
consistency; [MITM] the exact cost table, budget bands, free radius
w = 14 / d* = 7; [C8] certificate C(8) at both N' = 16 toys, MITM ==
exhaustion == 848 all-cyclotomic, height-freebie boundary w <= 3 at
p = 12289.
