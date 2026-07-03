# Q3R.5 — the three-rate dossier skeleton: submission shape under Reading B

- **Status:** AUDIT / SKELETON. Structure only — no new mathematics, and
  none pretended. Every quantitative cell below is QUOTED from a named,
  verifier-backed source (`qa3_e14_fm_margin_tables.md`, 117 PASS;
  `qx14_xr_coverage_table.md`, 215 PASS) or is an open slot marked with
  the DAG node id that fills it. No determination is claimed made here.
- **Queue item:** Q3R.5 (Tier 3R, `execution_queue.md`); campaign task
  A-M5 (`campaign_split_2026_07_03.md`).
- **Companion:** `qx15_xr_assembly_draft.md` (the XR-wall master-statement
  draft that the safe-side slot of this skeleton consumes).
- **Lint verifier:** `python3 experimental/scripts/verify_m5_drafts_lint.py`
  (structural: required sections, slot/DAG-id resolution against
  `prize_dag.json`, cross-source margin arithmetic, label hygiene).

## 0. Pinned notation and conventions

All conventions are inherited, not re-derived:

```text
FM(A) = C(n,j) q^(1-t), j = n-A, t = A-k     (qa3 sect.1; upper form of
                                              Lemma FM1's exact mean)
B*    = floor(q_line / 2^128)                 (the MCA gate)
A*    = max{A : FM(A) > B*}                   (adjacent-pin form:
                                              FM(A*) > B* >= FM(A*+1))
ZM(A) = log2(n^3 FM(A));  GM(A) = ZM(A) - log2 B*;  A_zero, A_gate per qa3
sigma*, LM(s), sigma_zero                     (list mirror, qa3 sect.5)
t*    = qx14's corridor edge = smallest t with FM <= B*; NOTE the index
        alignment: qx14's edge t* sits at agreement A*+1 in qa3's
        indexing (cross-checked below in sect. 4-6 margin arithmetic).
Headroom(A) = log2 B* - log2 FM(A)            (bits of conversion slack
                                              available at agreement A).
```

Prize caps `k <= 2^40`, `|F| < 2^256` are confirmed (DAG `field_cap_check`,
status proved). Idealized rows use `log2 q in {250, 255.9}` as scale
stand-ins (qa3 flags C1(b)/(c)); they are conventions, not official rows.

## 1. Reading B semantics (procedure-as-determination)

**The reading.** Per the project ruling of 2026-07-03 (recorded in
`execution_queue.md`: the QA.18 READING-B addendum and item Q3R.5), the
challenges' operative verb "determine" is discharged by exhibiting

1. a **decision procedure** with a proof of correctness AND completeness
   (completeness is what makes totality free under this reading), and
2. **per-row machine-checkable certificates** of the decisions the
   procedure makes at the exhibited rows, plus
3. an explicit **conditions table** for anything the procedure consumes
   that is not unconditional.

A determination is then an artifact: procedure + certificates +
conditions, per rate and (for the list challenge) per constant `m`.

**Rules anchors.** The `m`-quantifier is resolved: blueprint line 116
reads the list challenge as a FAMILY of determinations, one per constant
`m` (DAG `rules_m_reading`, status proved) — so per-`m` determinations
are valid prize objects. The exact official wording for the
procedure-as-determination construal itself is a rules-freeze row that
must be pinned (quote + hash) before submission
[OPEN SLOT -> DAG: rules_freeze]; the compiler-semantics variant of the
question (queue QA.20: does a certifying decision procedure satisfy
"determine for each admissible C"?) sets how much certifier uniformity
part (ii) actually requires [OPEN SLOT -> DAG: certifier_uniformity].

## 2. The headline claim shape

**Headline partial:** both grand-challenge determinations — MCA and
list — at rates 1/4, 1/8, 1/16, per row class and per constant `m`,
assembled from the certificate chains of sect. 3 and instantiated in
sect. 4-6. **Rate 1/2 is explicitly excluded** (sect. 7): it is the
endgame with three named residuals, and nothing in this dossier decides
any rate-1/2 row.

Campaign rationale (Tier 3R, quoted): conversion slack 100+ bits at the
clean rates vs 3-13 bits at rate 1/2; corridor decision points
integrality-clean; no coverage band at the clean rates (DAG
`rate_half_coverage_gap`: rates 1/4, 1/8, 1/16 have first-open-radius
margins < -121 bits at Row C and < -3.4e11 bits at prize-max).

## 3. The certificate chain template

Instantiated with rate-specific numbers in sect. 4-6. Chain steps
labelled SAFE-1..6, UNSAFE-1..5, FMT, M-FAM.

### 3.1 Safe-side chain (count <= B* at and above the pinned agreement)

```text
SAFE-1  Stratified sum.  B_C <= B_tan + B_quot + B_ap + B_ext, deduped
        per certificate grammar v2 (spine S1). Totality + first-match
        disjointness of the T0-T7 strata is the load-bearing partition
        fact [OPEN SLOT -> DAG: stratification_partition_thm]
        (in flight: PR #192).
SAFE-2  Paid terms per row.  B_tan by the tangent staircase compiler
        (DAG `staircase`, status proved, #147); B_quot as INTERVAL
        cells; B_ext by the s6 import rule; assembled into a single
        computable Paid(A) [OPEN SLOT -> DAG: paid_closure].
SAFE-3  Strip.  Periodic strata exact (DAG `strip`: combinatorics
        proved upstream; completeness rests on GAP-1 pricing)
        [OPEN SLOT -> DAG: gap1_noneq_mass]; the pullback stratum is
        charged to the profile budget per Q3R.4
        [OPEN SLOT -> DAG: pma_pullback_lists], with the 2-power
        profile input [OPEN SLOT -> DAG: dyadic_profile_evaluation].
SAFE-4  Aperiodic term, A >= A*+2 (integrality zone).  n^3 FM(A) < 1
        with the per-rate margins quoted in sect. 4-6, monotone beyond
        (qa3 Lemma M) — the corrected form of the integrality node:
        A_zero = A*+2, never A*+1
        [OPEN SLOT -> DAG: aperiodic_zero_at_crossing].
SAFE-5  Aperiodic term at the decision point A*+1 (the live cell).
        FM(A*+1) <= B* by definition of A*, but the mean is not the
        worst case: the row is decided by the worst-case conversion,
        i.e. THE r2_clean_rates slot — worst-case unpaid aperiodic
        count <= 2^100 x FM at the prize-max operating points
        [OPEN SLOT -> DAG: r2_clean_rates]. Calibration honesty: the
        2^100 budget clears the A*+1 gate at the PRIZE-MAX rows
        (headroom 181.3 / 130.7 / 171.6 bits, sect. 4-6) but NOT at
        Row-C-class rows (headroom 40.1 / 61.8 / 23.2 bits) — Row-C
        rows consume the tighter n^3-budget form, and Row C 1/16 is
        gate-knife-edged (GM(A*+1) = +6.85: needs A*+2 handling or a
        sharper-than-mean input, qa3 F3). The certificate format
        carries an explicit slack column for exactly this reason.
SAFE-6  Conditioning.  S0 object-equality axes printed with status
        [OPEN SLOT -> DAG: s0_zero_open]; rules freeze per sect. 1.
```

### 3.2 Unsafe-side chain (count > B* at the adjacent grid point)

```text
UNSAFE-1  Existence + localization.  B_C is a nonincreasing integer
          staircase, so a unique adjacent crossing exists
          unconditionally; the corridor arithmetic brackets it to 2-3
          candidate grid points per rate
          [OPEN SLOT -> DAG: crossing_localization].
UNSAFE-2  Witnesses at the adjacent point.  Collision-free branch: the
          qfloor value-set family (DAG `qfloor_exact`, status proved
          above the norm threshold); collided branch: the averaged
          fiber-to-slope conversion
          [OPEN SLOT -> DAG: averaged_slope_conversion]; assembled
          any-gate [OPEN SLOT -> DAG: unsafe_at_crossing].
UNSAFE-3  Census / exact counts.  Deciding scale pinned in an absolute
          window N' in [~120, ~400] (n-uniformity)
          [OPEN SLOT -> DAG: census_bounded_scales]; exact bignum
          class counts K at the bounded scales — expansions retired
          from tie decisions [OPEN SLOT -> DAG: census_exact_counts];
          undecided rows as explicit prime-counting windows
          [L(n,A), K(n,A)) in B*-space
          [OPEN SLOT -> DAG: census_window_arithmetic].
UNSAFE-4  Dodge verification.  Every exhibited dossier row verified
          OUTSIDE all windows (Row C margins 2^22 / 2^79 per E1 —
          expected clean) [OPEN SLOT -> DAG: census_dodge_selection].
UNSAFE-5  Residue + far anchor.  Knife-edge rows remain the census
          residue [OPEN SLOT -> DAG: knife_edge_census] — at the clean
          rates this is the generic Diophantine window, NOT a named
          coverage gap (contrast rate 1/2, sect. 7). The deep unsafe
          side is anchored by the Paper D universal cap (DAG
          `cap_theorem`, status proved: unsafe above 1 - rho - 2^-9,
          2^-10 at rate 1/16).
```

### 3.3 Per-row certificate format (FMT)

Certificates are emitted in **certificate grammar v2** — the proved
packaging layer of the Paper D spine (DAG `certificate_grammar_v2`,
status proved; `tex/cs25_cap_v12.tex`, printed deployed-row integer
certificates). Per the DAG note: ALIGN with this grammar; do not invent
a parallel one. One certificate per (row, side), fields:

```text
F1 row descriptor        (n, k, q or scale stand-in, rate, provenance)
                         single-constants-source
                         [OPEN SLOT -> DAG: descriptor]
F2 stratified-sum table  per-stratum integer cells, dedup per grammar
                         v2, quotient cells as INTERVALS (never point
                         values while conditional)
F3 margin block          ZM/GM/Headroom lines as exact integers or
                         bracketed log2 values, with the slack column
                         of SAFE-5
F4 unsafe witness block  family, exact count, window/dodge line
F5 conditions column     every conditional input by DAG node id (the
                         S0 axes, R2-form input, census conventions)
F6 checker line          which verifier replays this certificate, and
                         its exit status
```

Assembly: the wp7_2/7_3/7_4 build — the dossier is a GENERATED
document; the build script refuses any version whose gate list is not
green [OPEN SLOT -> DAG: dossier_partial], compiled with the verdict +
refusal logic [OPEN SLOT -> DAG: compiler], with tier-1 kernel-checked
gate certificates [OPEN SLOT -> DAG: lean_tier1]. Emitter pipeline for
the clean-rate rows: Q3R.3 (Fleet C-2).

### 3.4 m-family handling (M-FAM): per-constant-m determinations

Per `rules_m_reading` (status proved: family of determinations, one per
constant `m`), the list-side dossier section is a PER-m TABLE, not one
theorem:

```text
m <= 3            worst-case interleaved route (DAG `m_le3_route`,
                  conditional on the imgfib input at exponent ~1;
                  budget 128/(m*40) verified upstream)
                  [OPEN SLOT -> DAG: imgfib].
m <= sqrt((n-k)/t) ~ 16-31
                  for-all-m affordable (DAG `m_sweep`, status proved).
larger constant m require a-regular collapse
                  [OPEN SLOT -> DAG: a_regular_collapse]; exhaustive-
                  over-readings framing via DAG `m_handling`.
```

List unsafe side per m: thm:qcore planted counting (DAG `qcore`, status
proved; endpoint conventions pending the s7 F1 audit) + exact planted
arithmetic and Diophantine windows
[OPEN SLOT -> DAG: list_planted_arithmetic]; localization by the list
staircase [OPEN SLOT -> DAG: list_crossing_localization].

## 4. Rate 1/4

### 4.1 Row family

```text
Row-C-class   n = 2^10, k = 256, log2 q = 250 (idealized; true prime
              UNPINNED — qa3 flag C1(b))
prize-max     n = 2^41, k = 2^39, log2 q = 255.9 (idealized; below the
              k-cap)
pinned-class  exact-prime rows at this rate: to be located by the
              Q3R.3 pipeline [OPEN SLOT -> DAG: row_slate]
```

### 4.2 Safe-side numbers (chain of sect. 3.1)

Quoted from qa3 Table 1 / qx14 sect. 4-5:

```text
              A*              t*(edge)      ZM(A*+1)  ZM(A*+2)  GM(A*+1)  A_gate
Row C         259             3             +111.90   -136.55   -10.10    A*+1
prize-max     556770474277    7014660390    +69.63    -184.71   -58.27    A*+1
corridor-edge E[X] (prize) = 2^-53.4  =>  Markov-trivial at the edge
Headroom(A*+1): prize-max 181.3 bits (= 127.9 + 53.4);  Row C 40.1 bits
                (= 122 - (111.90 - 30)).
```

SAFE-5 verdict shape: the 2^100 slack clears prize-max A*+1 by ~81
bits; Row C consumes the n^3 form (GM = -10.10, thin — flagged).

### 4.3 Unsafe-side numbers (chain of sect. 3.2)

Candidate list {A*, A*+1}; witnesses per UNSAFE-2 at A* = 556770474277
(prize) / 259 (Row C); census windows and dodge checks per UNSAFE-3/4
are unexecuted open slots at this rate (owners: Q3R.3 / QA.8-10).

### 4.4 Per-row certificate format

As sect. 3.3; certificate count = (#rows exhibited at this rate) x
(2 sides) + (list side: x #m values in the per-m table).

### 4.5 m-family handling

```text
sigma* (prize) = 7014660388;  LM(sigma*+1) = +68.07  =>  sigma_zero =
sigma*+2 (LOUDFLAG per qa3 F5: the +1 radius has a POSITIVE margin).
M_max (prize) = 2^33; proved-unsafe radii [1, 2^33 - 1] OVERSHOOT
sigma*: first open radius 2^33 has margin -4.0066e11 bits — no gap.
Row C: M_max = 4, sigma* = 3, first open radius 4 at -138.10 bits.
```

### 4.6 Rate-local non-claims

Row C true prime unpinned; sigma*+1 must be treated as live (positive
LM margin) exactly as the MCA side treats A*+1; qcore endpoint
conventions pending (s7 F1); no census window computed yet at this rate.

## 5. Rate 1/8

### 5.1 Row family

```text
Row-C-class   n = 2^10, k = 128, log2 q = 250 (idealized, prime unpinned)
prize-max     n = 2^41, k = 2^38, log2 q = 255.9 (idealized)
pinned-class  exact-prime rows: Q3R.3 [OPEN SLOT -> DAG: row_slate]
```

### 5.2 Safe-side numbers

```text
              A*              t*(edge)      ZM(A*+1)  ZM(A*+2)  GM(A*+1)  A_gate
Row C         130             2             +90.23    -157.01   -31.77    A*+1
prize-max     279600463335    4722556392    +120.21   -132.92   -7.69     A*+1
corridor-edge E[X] (prize) = 2^-2.8 — the THINNEST clean-rate edge
Headroom(A*+1): prize-max 130.7 bits (= 127.9 + 2.8);  Row C 61.8 bits
                (= 122 - (90.23 - 30)).
```

SAFE-5 verdict shape: the 2^100 slack clears prize-max A*+1 by ~31
bits — the tightest clean-rate composition point; GM(A*+1) = -7.69 at
prize-max is inside the qa3 LOUDFLAG band (> -20): this rate's decision
point is the first place the composition arithmetic should be checked.

### 5.3 Unsafe-side numbers

Candidate list {A*, A*+1}; witnesses at A* = 279600463335 (prize) /
130 (Row C); census/dodge slots unexecuted (Q3R.3 / QA.8-10).

### 5.4 Per-row certificate format

As sect. 3.3, with the F3 slack column mandatory at this rate (thin
margins above).

### 5.5 m-family handling

```text
sigma* (prize) = 4722556390;  LM(sigma*+1) = +117.43  =>  sigma_zero =
sigma*+2 (LOUDFLAG).  M_max (prize) = 2^33; proved-unsafe [1, 2^33 - 1]
overshoots sigma*; first open radius margin -9.7896e11 bits — no gap.
Row C: M_max = 4, sigma* = 2, first open radius 4 at -407.01 bits.
```

### 5.6 Rate-local non-claims

The -7.69-bit GM at prize-max A*+1 means the n^3-budget adjacency gate
is NOT comfortably certified from the mean alone there; the r2 slack
form carries the point but with the smallest clean-rate margin. All
sect. 4.6 caveats repeat.

## 6. Rate 1/16

### 6.1 Row family

```text
Row-C-class   n = 2^10, k = 64, log2 q = 250 (idealized, prime unpinned)
prize-max     n = 2^41, k = 2^37, log2 q = 255.9 (idealized)
pinned-class  exact-prime rows: Q3R.3 [OPEN SLOT -> DAG: row_slate]
```

### 6.2 Safe-side numbers

```text
              A*              t*(edge)      ZM(A*+1)  ZM(A*+2)  GM(A*+1)  A_gate
Row C         65              1             +128.85   -117.31   +6.85     A*+2
prize-max     140382131271    2943177800    +79.27    -172.75   -48.63    A*+1
corridor-edge E[X] (prize) = 2^-43.7
Headroom(A*+1): prize-max 171.6 bits (= 127.9 + 43.7);  Row C 23.2 bits
                (= 122 - (128.85 - 30)).
```

SAFE-5 verdict shape: prize-max clears with ~72 bits under the 2^100
budget; **Row C 1/16 is the clean-lane knife edge** — GM(A*+1) = +6.85
is POSITIVE (qa3 F3), so the adjacency gate at A*+1 cannot be certified
from the mean with n^3 slack at all: that row's decision point needs
either the +2 offset convention or a sharper-than-mean input.

### 6.3 Unsafe-side numbers

Candidate list {A*, A*+1}; witnesses at A* = 140382131271 (prize) / 65
(Row C); census/dodge slots unexecuted (Q3R.3 / QA.8-10). Note the Row
C 1/16 A_gate = A*+2 knife edge makes the dodge check (UNSAFE-4)
mandatory, not optional, for any exhibited Row-C-class 1/16 row.

### 6.4 Per-row certificate format

As sect. 3.3; the F3 block at Row-C-class rows must print the +6.85
knife-edge line explicitly.

### 6.5 m-family handling

```text
sigma* (prize) = 2943177798;  LM(sigma*+1) = +75.40  =>  sigma_zero =
sigma*+2 (LOUDFLAG).  M_max (prize) = 2^32; proved-unsafe [1, 2^32 - 1]
overshoots sigma*; first open radius margin -3.4070e11 bits — no gap.
Row C: M_max = 2, sigma* = 1, first open radius 2 at -121.15 bits.
```

### 6.6 Rate-local non-claims

Row C 1/16 carries TWO knife-edge flags (GM(A*+1) = +6.85 on the MCA
side; the smallest Row-C headroom, 23.2 bits). Both are qa3 LOUDFLAG
findings; certificates at this rate must not quote ties as decided
without the census (UNSAFE-3/4). All sect. 4.6 caveats repeat.

## 7. Rate 1/2: EXCLUDED (the exclusion is part of the submission)

Nothing in this dossier decides, or claims progress on, any rate-1/2
row. Rate 1/2 is the endgame with **three named residuals**, each with
a frozen statement and owner:

```text
R-1/2-a  THE TIGHT COMPOSITION.  Conversion slack at the rate-1/2
         prize-max corridor edge is 3-13 bits (Headroom(t*) = 7.8 bits
         = 127.9 - 120.1; the plateau/budget mechanisms hand off with
         ~3 bits; the corridor edge is second-moment CONTENTFUL,
         E[X] = 2^120.1) vs 100+ bits at the clean rates. The 2^100
         slack composition does not carry this point; a rate-1/2
         composition must be essentially lossless
         [OPEN SLOT -> DAG: xr_kms_parameter_matching].
R-1/2-b  THE ~3.0e6-RADIUS BAND.  At prize-max rate 1/2 the exact
         2-power quotient-core window undershoots the mean crossing:
         M_max = 2^33 vs sigma* = 8,592,912,738 leaves 2,978,147 radii
         neither proved-unsafe nor extras-zero — an uncovered band no
         current mechanism reaches
         [OPEN SLOT -> DAG: rate_half_coverage_gap].
R-1/2-c  THE -12.87-BIT MARGIN POINT.  Integrality at the rate-1/2
         prize-max candidate holds at A*+2 with only 12.87 bits to
         spare (ZM(A*+2) = -12.87, below zero but above the -20
         comfort bar; list mirror -12.84) — a knife-edge fact about
         (n, q) = (2^41, 2^255.9) that the census must own before any
         tie is quoted [OPEN SLOT -> DAG: knife_edge_census].
```

Rate 1/2 re-enters the dossier only when all three residuals have
either closures or priced partial coverage.

## 8. Global non-claims

- This is a SKELETON: no determination, at any rate, is claimed made.
  Every open slot above names the DAG node that must flip first.
- The quoted FM/ZM/GM/sigma* numbers are MEAN-level (average over
  pairs/words); worst-case conversion is exactly the open r2 slot
  (SAFE-5) and is not proved at any rate.
- The census machinery (UNSAFE-3/4) is route-pinned but UNEXECUTED at
  the clean rates; no window, count, or dodge verdict exists yet.
- Idealized rows (`log2 q in {250, 255.9}`) are scale conventions; Row
  C's true prime is unpinned; only exact-prime pinned-class rows can
  carry final certificates.
- List-side qcore endpoint conventions pending the s7 F1 audit; the
  raw extras mean vs the imgfib residual object per qa3 C5.
- Reading B's official-wording anchor is not yet frozen (sect. 1 slot);
  if the stricter reading (explicit uniform certifier, QA.20 answered
  negatively) prevails, the headline weakens from "determination" to
  "decided rows + procedure", and this skeleton's sect. 2 must be
  re-worded — the structure below sect. 2 is unchanged either way.
- No claim that the three rate-1/2 residuals are exhaustive of rate
  1/2's difficulty; they are the three NAMED ones (wave-1 findings).

## 9. Open-slot index

| slot | DAG node id | filled by |
|---|---|---|
| rules wording freeze | `rules_freeze` | Q0.2 |
| certifier semantics | `certifier_uniformity` | QA.20 reading |
| strata partition | `stratification_partition_thm` | PR #192 (Q2.10) |
| Paid(A) closure | `paid_closure` | Q1.2 |
| strip completeness | `gap1_noneq_mass` | GAP-1 lane (A-M4) |
| pullback stratum | `pma_pullback_lists` | Q3R.4 (C-3) |
| profile input | `dyadic_profile_evaluation` | Q2.11 |
| integrality convention | `aperiodic_zero_at_crossing` | banked (qa3), +2 offset |
| worst-case conversion | `r2_clean_rates` | Q3R.1 (X-1) + QX.15 chain |
| S0 axes | `s0_zero_open` | WP-0.1 |
| crossing candidates | `crossing_localization` | QA.1 |
| collided-branch witness | `averaged_slope_conversion` | Q2.12 |
| unsafe assembly | `unsafe_at_crossing` | Tier A |
| census scales | `census_bounded_scales` | QA.7 |
| census counts | `census_exact_counts` | QA.8 |
| census windows | `census_window_arithmetic` | QA.9 |
| dodge verdicts | `census_dodge_selection` | QA.10 |
| knife-edge residue | `knife_edge_census` | QA.4 + Tier CV |
| row descriptors | `descriptor` | WP-3.2 |
| dossier build | `dossier_partial` | Q1.4 |
| compiler refusal | `compiler` | WP-7.1 |
| Lean tier 1 | `lean_tier1` | Q2.6 |
| imgfib input (m<=3) | `imgfib` | L1 lane |
| large-m collapse | `a_regular_collapse` | Q4.4 lane |
| list planted arithmetic | `list_planted_arithmetic` | QL.3 |
| list localization | `list_crossing_localization` | QL.1 |
| pinned-class rows | `row_slate` | Q3R.3 (C-2) |
| rate-1/2 composition | `xr_kms_parameter_matching` | endgame (excluded here) |
| rate-1/2 band | `rate_half_coverage_gap` | endgame (excluded here) |

## 10. Verifier

`experimental/scripts/verify_m5_drafts_lint.py` — standalone python3,
stdlib only, deterministic, exit 0 iff green. Checks on this file:
required sections (Reading B; the three per-rate sections each with row
family / safe-side / unsafe-side / certificate format / m-family /
non-claims; the rate-1/2 exclusion with the three named residuals;
global non-claims; slot index), every open-slot marker resolving to
an existing `prize_dag.json` node id, the cross-source headroom
arithmetic (qa3 ZM values vs qx14 in-band margins), and label hygiene
(no all-caps proved-status label anywhere in this draft).
