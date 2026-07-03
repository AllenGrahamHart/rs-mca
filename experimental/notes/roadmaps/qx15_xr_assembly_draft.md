# QX.15 — the XR wall's master statement: assembly DRAFT (post wave-1)

- **Status:** AUDIT / DRAFT. No proofs are claimed anywhere in this
  note. This is the wall's master statement written down with its
  quantitative spine attached (the wave-1 coverage table) and every
  unproved link named as a slot with the DAG node id that fills it.
  Sources quoted, never re-derived: `qx14_xr_coverage_table.md`
  (215 PASS), `qx6_qx8_kms_bridges.md` (167 PASS),
  `qa3_e14_fm_margin_tables.md` (117 PASS),
  `proof_sketch/s3b_iii_2_displacement_spectral.md`,
  `execution_queue.md` Tiers D3-D6/3R.
- **DAG node:** `xr_distance_dichotomy` (queue QX.15, Tier D6; campaign
  task A-M5).
- **Consumer:** the SAFE-5 slot of `q3r5_three_rate_dossier_skeleton.md`
  (`r2_clean_rates`) and, at rate 1/2, the endgame residual R-1/2-a.
- **Lint verifier:** `python3 experimental/scripts/verify_m5_drafts_lint.py`.

## 0. Pinned notation

Inherited from qx14 sect. 0: row `(n, k, q)`, `A = k + t`, `j = n - A`,
co-supports = vertices of `J(n,j)`, exchange distance `s`,
`B* = floor(q/2^128)`, `X = X_{u,v}(A)` = aligned-support count,
FM scale `E[X] <= C(n,j) q^{1-t}`, pair-ledger exponent
`c(s,t) = min(s, t-1)` (pinned input; packaging = QX.13/A-M1). Corridor
edge `t*` = smallest `t` with `FM <= B*`. Post-strip = after removing
the quotient-periodic strata (DAG `strip`). Energies `E_3`, expansion
`phi`, cells/juntas per qx6_qx8 sect. 0.

## 1. The master statement (draft form)

**Draft MS (xr_distance_dichotomy).** Fix a rate, an in-corridor
agreement `A`, and a post-strip pair `(u, v)`. Decompose the aligned
count `X` exhaustively by exchange-distance scale and link structure:

```text
X  <=  X_close(s <= s_L)   [tool T1: the pair ledger, reach s_L]
     + X_far(independent)  [tool T2: plateau/anticode scale]
     + X_struct(link-dense) [tool T3: globalness -> KLLM -> paid]
```

and the wall closes at an operating point iff the three coverages
overlap there with total loss below that point's headroom (sect. 4).
The split is exhaustive BY CONSTRUCTION (every pair of co-supports has
an exchange distance; link-dense vs spread is a dichotomy on the energy
side); what is open is the pricing of each part and the composition
arithmetic that adds them up.

**The wave-1 correction baked into MS.** The pre-wave-1 hope was that
T1 alone closes corridors at small reach. The coverage table's verdict:
`s* = t*-1` — under the pinned-ledger two-regime model EVERY corridor
edge needs FULL reach `s* = t*-1` (all shapes, all four rates), and the
requirement freezes (does not shrink) deeper in band:

```text
rate 1/2 : t* = 8,592,912,739    s* = 8,592,912,738    s*_C = 566,581,429
rate 1/4 : t* = 7,014,660,390    s* = 7,014,660,389    s*_C = 467,502,331
rate 1/8 : t* = 4,722,556,392    s* = 4,722,556,391    s*_C = 321,589,749
rate 1/16: t* = 2,943,177,800    s* = 2,943,177,799    s*_C = 205,816,237
```

Full reach `t*-1` means billions of per-distance residual
certifications (`~ n * 2^-8` exchange steps at rate 1/2); even the
generous three-regime scenario needs `s*_C ~ t*/15`. **The honest
note: extending the residual ledger to full reach t*-1 is implausible
as a proof strategy**, and this draft does NOT route the conversion
through it. The ledger keeps two real jobs (sect. 2, T1); ALL
worst-case conversion pressure moves to T3 (globalness/KLLM), exactly
as the wave-1 verdict on the DAG node records.

## 2. The three tools, post-verdict

### T1 — the pair ledger (close pairs, small fixed reach)

Input: `c(s,t) = min(s, t-1)` (derived and verified upstream;
provenance external + hand/Monte-Carlo checks; repo-standard packaging
is the QX.13 deliverable [OPEN SLOT -> DAG: xr_ledger_qpower]). Roles
that SURVIVE the verdict:

```text
(i)  head domination at small s: per-step decay j(n-j)/q (~176-178
     bits per step at prize shapes), so s = 1 dominates the
     excess-over-plateau — this is what makes the second-moment
     profile computable at all (qx14 sect. 2);
(ii) the small-t exemplar: the stripped A=265 instance needs only
     reach s* = 4 << t-1 = 8 — a partial small-t ledger IS enough for
     the P2 target (the #152 generalization stays queued as the
     small-t diagnostic [OPEN SLOT -> DAG: exchange_ledger_gen_t]).
```

What T1 does NOT do (wave-1): close any corridor row by itself at any
affordable reach.

### T2 — far pairs (the plateau, priced; anticode scale honest)

The distinct-slope far-pair mass rides the independence PLATEAU
`E[X]^2` — exactly, by Vandermonde (qx14 sect. 2: the far sum equals
`E[X]^2`, and the same-slope tail is pointwise plateau/q). This part is
banked arithmetic, not a hope. The Delsarte/anticode toolkit remains
the honest scoping layer for what combinatorial bounds alone can give
(they cap at `(j/n)^s` — q-scale must be algebraic)
[OPEN SLOT -> DAG: xr_anticode_toolkit].

### T3 — structured mass (globalness -> KLLM -> paid): the load-bearing tool

Three links, statuses distinct:

```text
T3.1  E_3 bridges (proved upstream, 167/167 verified): E_3-large =>
      non-expanding (phi <= 1 - E_3/mu), and junta-correlated mass
      lands on tangent-type/complementary paid strata at a 2^-d
      pigeonhole discount (DAG `xr_e3_to_expansion`,
      `xr_junta_to_paid`; qx6_qx8). Cells are EXACTLY extremal —
      the tightness pattern is a theorem there, not a scan.
T3.2  Globalness certificate: the top-core double count — every
      unpaid (j-1)-core has <= L_tan aligned completions => bounded
      link densities post-strip (proof written and verified upstream
      MODULO the strip normal form: the L_tan = 1 vs 2 convention
      must be pinned against the actual T0-T7 tree, QX.11/A-M2)
      [OPEN SLOT -> DAG: xr_globalness_from_ledger]. GATED BY the
      leak adjudication: 10 post-strip link-leak candidates from the
      #209 corpus must each be classified (strippable under the
      L_tan convention vs genuine unpaid tangent leak) — Q3R.2
      (Fleet C-1) — before the globalness hypothesis is usable at
      ANY rate.
T3.3  The KLLM engine: global hypercontractivity (global sets expand,
      losses poly in link parameters rather than 1/mu) — the
      density-robust replacement for raw KMS constants at FM-scale
      densities mu ~ q^{1-t}
      [OPEN SLOT -> DAG: xr_small_set_engine], with the KMS/DKKMS
      statement import alongside [OPEN SLOT -> DAG: xr_kms_import].
      Every quoted constant is [CITATION NEEDED] until the import
      note verifies it against the actual papers; the QX.12 skeleton
      (A-M3) names these unknowns — see sect. 3, slots K1-K3.
```

## 3. The composition inequality chain (named slots)

Target statement the chain must produce (the dossier's SAFE-5 input):

```text
worst-case unpaid aperiodic count  <=  LOSS x FM(A)   at the operating
point, with LOSS <= 2^100 at the clean prize-max rows (r2_clean_rates)
```

The chain, link by link, with every unknown named:

```text
C0  strip completeness.  Post-strip = aperiodic stratum exactly;
    combinatorics proved upstream, completeness rests on GAP-1
    pricing [OPEN SLOT -> DAG: gap1_noneq_mass] (A-M4 / Fleet task);
    node `strip` carries the conditional.
C1  energy dichotomy.  For the fixed post-strip pair: alignment mass
    is spread (small E_3) or link-dense (large E_3) — the E_3
    calculus supplies the split and its easy direction
    [OPEN SLOT -> DAG: xr_e3_calculus]; the inverse-content class
    (what link-dense mass looks like: fixed-core/fixed-hole) is the
    grounded conjecture [OPEN SLOT -> DAG: c_xr_content].
C2  link-dense => globalness violation => paid.  Via T3.1 (proved
    bridges) + T3.2 (globalness certificate; L_tan normal form +
    leak adjudication pending, sect. 2). Loss so far: the 2^-d
    pigeonhole discount + the L_tan poly factor.
C3  global => expansion (KLLM).  The engine consumes a globalness
    parameter and returns expansion for the spread/global part. The
    QX.12 skeleton's unknowns, each [CITATION NEEDED] until the
    import verifies them:
      K1  the loss exponents in KLLM's conclusion (which powers of
          the link parameters appear) — raw table = QX.10;
      K2  the UNIFORM-SLICE variant: cube statements do not transfer
          verbatim to J(n,j); the precise slice-version hypothesis
          set must be cited, not assumed;
      K3  the stability/structure version quoted by the shortcut
          route (what "correlates with a junta" quantitatively
          means there).
    [OPEN SLOT -> DAG: xr_small_set_engine]
C4  spread mass => second moment.  Pair ledger (T1) + ball profile:
    E[X^2] <= E[X]^2 (1 + 1/q) + E[X] (1 + j(n-j)/(q - j(n-j)))
    (banked, exact on toy rows, bracket-stable at prize shapes) =>
    Chebyshev/Markov at poly budget n^B, B <= 3 (DAG `budget_b3`,
    proved). The repo-standard write-up of the second-moment formula
    is its own queue item [OPEN SLOT -> DAG: averaged_xr]. Moment-
    level ONLY — this line never converts to a fixed pair by itself;
    the conversion is C5.
C5  THE COMPOSITION ARITHMETIC (the open core).  Add C2 + C3 + C4
    losses and compare against the operating point's headroom. The
    known tension (#211/E20, recorded on the DAG): the extracted
    KLLM stay-probability arithmetic CONSUMES globalness beta <= q^-g
    (a q-POWER demand) and yields a q^{-(g+t-1)/4} shape, while the
    proved top-core cap supplies only poly(n)-scale globalness. The
    open question in one line: does poly-globalness + the q-power
    pair ledger compose to n^B x FM with the KLLM engine used ONLY
    for the structured residue — or does the cap need a q-power
    strengthening (a new, harder statement)?
    [OPEN SLOT -> DAG: xr_kms_parameter_matching]
    Deliverable owner: Q3R.1 (external X-1), with #211's exponents
    and the wave-1 margin tables as given data; output = the chain
    with explicit losses, or the named gap.
```

## 4. Operating points: where the chain must land

### 4.1 The clean-rate operating point (rates 1/4, 1/8, 1/16)

Headroom at the prize-max corridor edge (`Headroom = log2 B* - log2
E[X]`, cross-checked qa3-vs-qx14):

```text
rate 1/4 :  headroom 181.3 bits   (E[X] = 2^-53.4 at the edge)
rate 1/8 :  headroom 130.7 bits   (E[X] = 2^-2.8 — thinnest clean edge)
rate 1/16:  headroom 171.6 bits   (E[X] = 2^-43.7)
```

All three edges are Markov-trivial at moment level (`E[X] < 1`), so the
ENTIRE clean-rate demand on this chain is the worst-case conversion,
priced at `LOSS <= 2^100` (`r2_clean_rates`): the chain may lose up to
~100 bits through C2's pigeonhole + poly factors, K1's exponents, and
C5's additions, and still clear every clean prize-max edge. That two-
orders-of-magnitude cushion is WHY the three-rate campaign routes
through this chain first [OPEN SLOT -> DAG: r2_clean_rates]. (Row-C-
class rows carry 23-62 bits only — per-row-class pricing per the
dossier skeleton's SAFE-5 note.)

### 4.2 The rate-1/2 operating point (excluded from the campaign headline)

```text
headroom at the edge:  7.8 bits   (E[X] = 2^120.1 — second-moment
                                   CONTENTFUL, only 7.8 bits under B*)
mechanism handoff margin:  ~3 bits (the (i)/(ii) near-coincidence at
                                   the corridor, qx14 sect. 5.2)
integrality point:  -12.87 bits at A*+2 (list mirror -12.84)
coverage band:  2,978,147 radii (M_max = 2^33 vs sigma* =
                8,592,912,738) [OPEN SLOT -> DAG: rate_half_coverage_gap]
```

At 3-13 bits of total slack, the same chain must be essentially
LOSSLESS at every link — no pigeonhole discount, no poly factors, exact
constants in K1-K3 — which is a different (and currently unpriced)
statement. Rate 1/2 is therefore the wall's endgame, not its first
target.

## 5. What remains (the exact list)

```text
1  LEAK ADJUDICATION (gates C2 at every rate).  Classify the 10
   post-strip link-leak candidates from the #209 corpus: strippable
   under the L_tan convention vs genuine unpaid tangent leak. Owner:
   Q3R.2 (Fleet C-1). A genuine leak = a counterexample to the
   globalness hypothesis as stated; the chain then needs the leak
   stratum priced separately
   [OPEN SLOT -> DAG: xr_globalness_from_ledger].
2  KLLM CONSTANTS (gates C3).  Verify K1-K3 against the actual
   papers; cite the uniform-slice variant precisely. Owner: QX.12
   skeleton (A-M3) then the full import (QX.12). Until then every
   constant in C3 is [CITATION NEEDED]
   [OPEN SLOT -> DAG: xr_small_set_engine].
3  THE COMPOSITION ARITHMETIC (C5).  The inequality chain with
   explicit losses vs the 2^100 clean-rate budget, resolving the
   poly-vs-q-power globalness tension. Owner: Q3R.1 (X-1)
   [OPEN SLOT -> DAG: xr_kms_parameter_matching].
Secondary (packaging, not blockers of the statement):  QX.13 ledger
packaging [OPEN SLOT -> DAG: xr_ledger_qpower]; the L_tan = 1 vs 2
normal-form pin (QX.11/A-M2); the QA.20 rules reading for how the
closed wall is consumed by the dossier.
```

If 1-3 land within budget at the clean rates, `xr_distance_dichotomy`
assembles from proved pieces plus one verified import, and the
dossier's SAFE-5 slot fills; if the composition fails even with 2^100
slack, the recorded falsifier branch applies (the clean rates move to
the SPI route, which inherits the F machinery).

## 6. Non-claims

- NOTHING in this note is proved here; the master statement MS is a
  DRAFT of a theorem statement, not a theorem. Statuses quoted from
  upstream notes/DAG are theirs, not this note's.
- Moment-level scope: every E[X]/E[X^2] figure is average-case; the
  fixed-pair (worst-case) conversion is exactly the open chain C1-C5.
  This note nowhere asserts the conversion exists.
- The pair-ledger exponent c(s,t) = min(s,t-1) is a pinned INPUT
  (external provenance, hand + Monte-Carlo checked; repo packaging
  pending QX.13); no published citation exists for it
  [CITATION NEEDED — the QX.13 note is the intended fix].
- The KLLM/KMS quantitative statements are unverified imports at this
  time: no constant from those papers is quoted as a number anywhere
  above, deliberately (slots K1-K3).
- s*, s*_C and "reach" use qx14's monotone-composition modeling
  choices, labelled there; "implausible" (sect. 1) is a judgement
  about proof-strategy cost, not a nonexistence claim about
  exchange_ledger_gen_t.
- No claim that the three-tool split's T3 branch succeeds: the
  poly-vs-q-power tension (C5) is open and could resolve negatively;
  the falsifier branch is stated in sect. 5, not hidden.
- The headroom table is arithmetic on quoted verifier-backed numbers;
  operating points at Row-C-class rows are thinner and are NOT covered
  by the 2^100 phrasing (sect. 4.1 parenthetical).
- Rate 1/2: excluded; the three residuals live in the dossier
  skeleton's sect. 7 and are not re-adjudicated here.

## 7. Verifier

`experimental/scripts/verify_m5_drafts_lint.py` — standalone python3,
stdlib only, deterministic, exit 0 iff green. Checks on this file:
required sections (master statement, three tools, composition chain,
operating points, what remains, non-claims), the `s* = t*-1` verdict
line and the honest implausibility note present, every open-slot
marker resolving to an existing `prize_dag.json` node id, KLLM slots
carrying [CITATION NEEDED], the headroom/band arithmetic
(127.9 - 120.1 = 7.8 etc.; 8,592,912,738 - 2^33 + 1 = 2,978,147), and
label hygiene (no all-caps proved-status label in this draft).
