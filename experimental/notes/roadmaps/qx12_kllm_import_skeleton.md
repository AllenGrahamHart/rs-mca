# QX.12 — KLLM import skeleton: uniform-slice global hypercontractivity (SKELETON)

- **Status:** SKELETON — draft-grade BY DESIGN. Nothing below is proved,
  imported, or bibliographically confirmed. Every external constant,
  exponent, admissible range, theorem number, and bibliographic datum is an
  explicit `[CITATION NEEDED]` slot, to be filled by a human/agent with the
  actual PDFs (the SS4 checklist). Purpose: pin the statement shape and the
  consumption interface so that completing the import means FILLING SLOTS,
  with no structural rework (queue items QX.12 + QX.12-FLAGS,
  `execution_queue.md` Tier D4).
- **DAG node:** `xr_small_set_engine` (the import), feeding
  `xr_kms_parameter_matching` (the composition) and the campaign target
  `r2_clean_rates`. The DAG file is NOT edited here.
- **Parents (in-repo; every quoted claim below is sourced from these):**
  `prize_dag.json` node statements (`xr_globalness_from_ledger`,
  `xr_kms_parameter_matching`, `xr_small_set_engine`, `r2_clean_rates`,
  `xr_gvn`); `qx6_qx8_kms_bridges.md` (the PROVED bridges + the cell
  dictionary); `qx14_xr_coverage_table.md` (wave-1 verdict, pinned pair
  ledger, the mid band); `qa3_e14_fm_margin_tables.md` (clean-rate
  margins); `execution_queue.md` Tiers D3/D4/D6/3R;
  `campaign_split_2026_07_03.md` (tasks A-M1/A-M2/A-M3/C-1/X-1).
- **Verifier (lint only):** `python3
  experimental/scripts/verify_qx12_skeleton_lint.py` — deterministic
  document-hygiene lint: slot census, bare-numeric audit (every numeric
  token must be in-repo-sourced, structural, or inside a tagged slot),
  checklist state, interface-symbol coverage. It checks NO mathematics.

## 0. Pinned notation (in-repo conventions only; nothing new here)

```text
J(n,j)      Johnson graph/scheme on co-supports T, |T| = j = n - A, exact
            agreement A = k + t (qx6_qx8_kms_bridges.md SS0; qx14 SS0.1).
            mu(A) = |A|/C(n,j) for A a vertex subset.
A_post      the post-strip alignment set of a FIXED pair (u,v): aligned
            co-supports with the paid tangent/quotient strata removed
            (s3b_iii_2 SS3; the strip normal form is the QX.11 packet's
            business — campaign task A-M2, in flight on this branch).
r-core link the restriction of A_post to a cell Cell_C(tau): co-supports
            with prescribed intersection pattern tau on a core C, |C| = r;
            internally the Johnson instance J(n-r, j-|tau|)
            (qx6_qx8 SS1.7(b) and SS2.3). "Link density" = density of
            A_post inside that cell.
eps0        = L_tan/(n-j+1): the post-strip link-density cap, uniform over
            core sizes r <= j-1 (prize_dag.json node
            xr_globalness_from_ledger — top-core double count, PROVED
            modulo the strip normal form; L_tan = 1 vs 2 pending the
            normal-form ruling, QX.11 packet). Polynomial scale in n.
FM          = max(1, C(n,j) q^{1-t}), the FM scale at exact agreement
            (qx14 SS0.1; s2_paid_ledger SS2).
mu-scale    the vanishing-measure regime mu ~ q^{1-t}-scale — the regime
            any imported statement must survive (per the
            xr_small_set_engine node statement).
pair ledger q^{-min(s,t-1)} extra suppression per support pair at exchange
            distance s (qx14 SS0.3 — PINNED INPUT there; repo-standard
            packaging = the QX.13 packet, campaign task A-M1, in flight).
            Moment-level scope.
E_3, phi    the exchange energy and the edge expansion of qx6_qx8 SS0
            (both bridges PROVED there; all verifier checks PASS).
clean rates rates 1/4, 1/8, 1/16. Campaign target r2_clean_rates: beat
            only 2^100 x FM there (measured wave-1 margins ~121-243 bits;
            qa3_e14_fm_margin_tables.md and the r2_clean_rates node
            statement).
```

## 1. The statement shape required (the import template)

What the program needs — exactly and only this shape:

**global hypercontractivity / small-set expansion on the UNIFORM SLICE
(the Johnson scheme `J(n,j)`), for `(a, eps)`-global sets, at vanishing
measure `mu ~ q^{1-t}`.**

Cube versions (uniform or p-biased) do NOT transfer verbatim
(QX.12-FLAGS item (b)); every slot below insists on the slice domain.

### 1.1 Definitional slot D1 — the paper's globalness notion

[CITATION NEEDED: the source paper's exact definition of a global set /
global function on the slice]. Two candidate conventions occur in this
literature; which one the source theorem takes determines the conversion
constants `C_conv`, `g5`, `g6` of SS2:

```text
(abs)   absolute cap:  A is (a, eps)-global iff every r-core link,
        1 <= r <= a, has density <= eps.
(boost) relative cap:  A is (a, eps)-global iff no r-core link boosts the
        density of A by more than a factor tied to eps and mu(A)
        [CITATION NEEDED: the exact functional form, from the paper].
```

The in-program supply (SS2.1, item (I1)) is (abs)-form with `eps = eps0`.
If the source is (boost)-form, the conversion is NOT free at mu-scale
(unknown `g6` in SS2.2) — a load-bearing definitional check (C2).

### 1.2 Template KLLM-S (set form; every constant an explicit slot)

```text
KLLM-S (TEMPLATE — [CITATION NEEDED: paper, theorem number, exact
statement; this template is OUR consumption shape, not a quotation]).
There exist constants
    K0  = [CITATION NEEDED: the multiplicative constant],
    g1  = [CITATION NEEDED: the eps exponent],
    g2  = [CITATION NEEDED: the core-size exponent],
    g3  = [CITATION NEEDED: the 1/mu exponent — expected 0, see below]
such that: for all (n, j), all core sizes
    a  <= g4  = [CITATION NEEDED: the admissible core-size range],
and all measures
    mu(A) admissible per mu0 = [CITATION NEEDED: any measure floor,
                                ceiling, or regime hypothesis],
if A subset V(J(n,j)) is (a, eps)-global in the D1 sense, then ONE of:

(E-form, expansion)
    phi(A) >= 1 - K0 * a^{g2} * eps^{g1} * (1/mu(A))^{g3}
(S-form, stay probability / energy)
    E_k(A)/mu(A) <= [ K0 * a^{g2} * eps^{g1} * (1/mu(A))^{g3} ]^{c_k}
    for k up to [CITATION NEEDED: the k-range],
    c_k = [CITATION NEEDED: the per-step exponent]
(N-form, hypercontractive norm inequality)
    a bound of the shape ||T f||_p <= (loss factor) ||f||_p' for global f
    [CITATION NEEDED: the exact norm pair and loss factor — plus the
    derivation route from N-form to E/S-form, which would be ADDITIONAL
    imported content with its own slot]
(T-form, stability / structure)
    if additionally A is non-expanding (E_3(A) >= eps_E * mu(A)), then A
    has correlation >= [CITATION NEEDED: the correlation level, named
    g8 in SS2] with a junta of core size <= [CITATION NEEDED: named g9]
    — the form Bridge 2 (qx6_qx8 SS2, PROVED) consumes directly,
    landing the mass on priced strata.
```

Which of E/S/N/T the source actually states is checklist item C7. The
in-repo bridge dictionary (qx6_qx8, PROVED) converts between `phi` and
`E_3` exactly, but does NOT derive either from an N-form norm inequality.

**The load-bearing structural demand is `g3 = 0`** — "losses polynomial
in the link parameters rather than in `1/mu`" (quoted from the
`xr_small_set_engine` node statement). At `mu ~ q^{1-t}`-scale, any
`g3 > 0` loss is a `q`-power loss and kills the route (C9: if found,
report loudly; the fallback is a named harder statement, see N6).

### 1.3 What "uniform slice" must mean in the source

Either (i) the theorem is stated on the slice / Johnson scheme directly
[CITATION NEEDED: paper + theorem number for the slice version], or
(ii) it is stated on the cube and a separate slice-transfer result is
invoked [CITATION NEEDED: the transfer source, its statement, and its
loss factors — named `g7` if they exist]. In case (ii), `g7` joins the
(REQ-A)/(REQ-B) arithmetic of SS2 as an extra loss exponent.

## 2. The consumption interface

### 2.1 What our side supplies (status label per item)

```text
(I1) link caps [PROVED modulo strip normal form; gated by adjudication]
     every r-core link of A_post, 1 <= r <= j-1, has density
     <= eps0 = L_tan/(n-j+1).
     Source: prize_dag.json xr_globalness_from_ledger (top-core double
     count; provenance GPT Pro, independently checked: hand algebra +
     brute-force trials, per the node notes); repo-standard packaging =
     the QX.11 packet (campaign task A-M2, in flight on this branch).
     GATES: (a) the strip normal form pins L_tan = 1 vs 2 against the
     actual T0-T7 tree (QX.11); (b) the post-strip link-leak candidates
     from the #209 corpus (ten of them, per the node notes) must be
     adjudicated (campaign task C-1 / queue Q3R.2).
(I2) bridges [PROVED]  the E_3 <-> expansion dictionary and the
     junta -> paid-strata transfer (qx6_qx8_kms_bridges.md; its verifier
     is green).
(I3) pair ledger [PINNED INPUT]  q^{-min(s,t-1)} at exchange distance s
     (qx14 SS0.3; QX.13 packet in flight, campaign task A-M1).
     Moment-level scope only.
(I4) budget [AUDIT]  the clean-rate slack: r2_clean_rates grants ANY
     loss up to 2^100 x FM at rates 1/4, 1/8, 1/16 (wave-1 measured
     margins ~121-243 bits; qa3_e14_fm_margin_tables.md).
(I5) the mid band [AUDIT]  qx14 SS5.2 finding 3: the exchange scales the
     pinned ledger cannot reach at prize shapes — s in (s*_C, t*-1] with
     s*_C ~ t*/15. The import is consumed EXACTLY to cover this band on
     the fixed-pair side (qx14 SS7 first non-claim: the worst-case
     conversion is the QX.10-QX.12 branch's job).
```

### 2.2 The contradiction chain (engine-only shape), unknowns named

All unknown exponents are named here and re-appear, one checkbox each, in
SS4: `K0, g1, g2, g3, g4, g5, g6, g7, g8, g9, C_conv, mu0` (from the
paper) and `h1, eps_E` (in-program, NOT the paper's job).

```text
GOAL (r2_clean_rates): for every post-strip pair (u,v) at the clean-rate
operating points:   |A_post| <= 2^100 * FM.

Suppose not:  |A_post| > 2^100 * FM.

(P1) [OPEN IN-PROGRAM: xr_gvn, status TARGET — NOT part of the import]
     alignment excess pumps energy:
     |A_post| > 2^100 * FM  =>  E_3(A_post) >= eps_E * mu(A_post)
     with eps_E >= n^{-h1}  (h1 = the named in-program unknown the
     gvn/pumping step must supply).
(P2) [PROVED: qx6_qx8 Prop 1.5]
     E_3(A_post) >= eps_E * mu(A_post)  =>  phi(A_post) <= 1 - eps_E.
(P3) [SUPPLY (I1) + definitional conversion D1]
     A_post is (a, eps)-global with
     a <= min(j-1, g4),
     eps <= C_conv * eps0^{g5} * (1/mu(A_post))^{g6}
     (g6 = 0 iff the source is (abs)-form; g6 > 0 in (boost)-form is a
     q-power obstruction at mu-scale — checklist C2).
(P4) [THE IMPORT: KLLM-S, E-form; via S-form + (I2) if the source is
     stated as stay probability]
     phi(A_post) >= 1 - K0 * a^{g2} * eps^{g1} * (1/mu(A_post))^{g3}.
(P4')[ALTERNATIVE ENDING: T-form stability route]
     non-expansion => correlation >= g8-level with a junta of core size
     <= g9; Bridge 2 (qx6_qx8 SS2, PROVED) transfers the mass, at a
     2^{-g9} pigeonhole discount, onto tangent-depth cells and
     complementary instances — both priced by the PROVED consumers
     named in qx6_qx8 SS2.5. Then the paid budgets close instead of a
     contradiction.

(REQ-A) The chain closes r2_clean_rates iff (P3)+(P4) contradict (P2):
     K0 * a^{g2} * [ C_conv * eps0^{g5} * (1/mu)^{g6} ]^{g1} * (1/mu)^{g3}
        <  eps_E   ( >= n^{-h1} ),
i.e. in bits, writing lg = log2:
     lg K0 + g2*lg a + g1*lg C_conv + g1*g5*lg eps0
           + (g3 + g1*g6)*lg(1/mu)  <  -h1*lg n .
Reading: lg eps0 < 0 is a GAIN (polynomial in n); lg(1/mu) is
astronomical at mu-scale (order (t-1)*lg q). So (REQ-A) is satisfiable
ONLY IF g3 + g1*g6 = 0 — only the genuinely "global" (mu-free-loss) form
of the engine, consumed in the (abs) sense, can close this chain. That
single structural fact is why this import exists at all (and why raw
hypercontractivity does not suffice, per xr_kms_parameter_matching).
```

### 2.3 The assembly shape (QX.15 currency): where the ledger sits

```text
(REQ-B)  |A_post| <= CLOSE + MID + FAR, where
  CLOSE = exchange scales within the ledger reach: paid by the pair
          ledger q^{-min(s,t-1)} (supply (I3)); moment-level today —
          the fixed-pair reading is exactly what this import's
          conversion must license;
  FAR   = distance-independent scales: anticode/plateau factors
          (qx14 SS2);
  MID   = s in (s*_C, t*-1]: MUST come from the import — the (P4)/(S-form)
          bound instantiated at the operating points must give
          MID <= 2^100 * FM - CLOSE - FAR    [same slots as (REQ-A)].
qx14 SS5.2 finding 3: no budget reading removes MID; that band is this
import's entire job. The full composition with explicit losses is
Q3R.1's deliverable (external assignment X-1); this section fixes its
input interface.
```

### 2.4 The #211/E20 extraction (cross-branch shape exemplar)

The only quantitative KLLM-consumption arithmetic recorded anywhere in
the program is [CROSS-BRANCH: PR #211 / E20 — the extraction packet is
NOT on this branch; in-repo traces only, listed below]:

```text
quoted shape (verbatim from the prize_dag.json node
xr_kms_parameter_matching statement):
  the extracted stay-probability arithmetic consumes globalness
  beta <= q^{-g} and yields suppression q^{-(g+t-1)/4}     [#211 shape]
```

Read against supply (I1): the proved cap `eps0` is poly(n)-scale, i.e.
its q-exponent `g ~ lg(1/eps0)/lg q` is nearly `0`; naive substitution
into the shape above gives suppression exponent `~ (t-1)/4` [#211 shape,
cross-branch, UNVERIFIED]. Whether the extraction ADMITS poly-scale
`beta` (versus genuinely demanding a q-power) is exactly the open
arithmetic named in `xr_kms_parameter_matching` — recorded here as
**OPEN O1**, the central question this import must settle. In-repo
traces: `execution_queue.md` Q3R.1 ("#211's KLLM exponents"),
`evidence_plan_codex.md` E20 (the planned extraction — plan entry only,
no results note exists on this branch), `campaign_split_2026_07_03.md`
task X-1. [CROSS-BRANCH: cite the #211 packet itself when it lands.]

## 3. Candidate sources (bibliographic data ALL [CITATION NEEDED])

In-repo author-group names only. NOTHING below is confirmed against a
PDF; no titles, years, venues, arXiv ids, or theorem numbers are stated,
because none can be verified from in-repo sources.

```text
S1  Keevash-Lifshitz-Long-Minzer — global hypercontractivity
    [CITATION NEEDED: exact paper title, venue, year, arXiv id; the
    theorem number(s) for the (a,eps)-global small-set expansion /
    stay-probability statement; ALL constants K0, g1, g2, g3, g4, mu0]
    role: the primary engine — the xr_small_set_engine node names
    exactly this author group.
S2  Lifshitz-Minzer and/or Filmus et al. — slice / Johnson-scheme
    variants of global hypercontractivity
    [CITATION NEEDED: which paper(s) actually state the UNIFORM-SLICE
    version; exact statements and losses (g7); or a finding that S1
    already covers the slice directly]
    role: QX.12-FLAGS item (b) — cube results do not transfer verbatim.
S3  Khot-Minzer-Safra (and DKKMS) — Johnson / Grassmann expansion, the
    2-to-2 games engine
    [CITATION NEEDED: exact papers, theorem numbers, quantitative forms]
    role: the comparison row (QX.10 loss tables). The raw-KMS constants
    are EXPECTED to fail at FM scale (per xr_kms_parameter_matching) —
    verify from the actual statements; do not assume the failure either.
S4  the #211/E20 extraction packet
    [CROSS-BRANCH: PR #211 — not present on this branch; see SS2.4 for
    the in-repo traces; import its exponent arithmetic only AFTER the
    S1/S2 verification, never instead of it]
S5  the flagged DAG-notes constant
    [CITATION NEEDED: the xr_globalness_from_ledger node notes quote
    "delta = 10^-3 * r^-1 * eta^3 etc." WITH an explicit hallucination
    warning (GPT Pro provenance); verify against S1 or DISCARD — do not
    propagate it into any composition]
```

## 4. The verification checklist (fill WITH THE PDFs; one box per datum)

A box may be ticked only with the exact bibliographic locus (paper +
theorem/definition number) written next to it. Until every box relevant
to (REQ-A)/(REQ-B) is ticked, this note stays SKELETON and nothing
downstream may cite it as an import.

- [ ] **C1** — S1 bibliographic identity pinned: title, venue, year,
  arXiv id [CITATION NEEDED]
- [ ] **C2** — D1 resolved: the source's globalness DEFINITION ((abs) vs
  (boost); sets vs functions); this fixes `C_conv`, `g5`, `g6`
  [CITATION NEEDED]
- [ ] **C3** — domain confirmed: a uniform-slice statement located (in S1
  or S2); if cube-only, the transfer route and its losses `g7` pinned
  [CITATION NEEDED]
- [ ] **C4** — the theorem number of the consumed conclusion
  [CITATION NEEDED]
- [ ] **C5** — `K0` extracted; the S5 flagged constant verified or
  discarded [CITATION NEEDED]
- [ ] **C6** — `g1` (the eps exponent) [CITATION NEEDED]
- [ ] **C7** — conclusion form classified (E/S/N/T of SS1.2); if N-form,
  the route to E/S-form written out (new imported content, own slot); if
  T-form, `g8` (correlation level) and `g9` (junta core size) extracted
  [CITATION NEEDED]
- [ ] **C8** — `g2` (core-size exponent) and `g4` (admissible core-size
  range); check that `a <= j-1` is admissible at the operating points
  [CITATION NEEDED]
- [ ] **C9** — `g3` extracted; VERIFY the load-bearing claim "losses
  polynomial in the link parameters, NOT in `1/mu`" (`g3 = 0`); if
  `g3 > 0`: the route dies at mu-scale — report loudly [CITATION NEEDED]
- [ ] **C10** — `mu0` (measure hypotheses); check the `mu ~ q^{1-t}`-scale
  regime is admissible at the three operating points [CITATION NEEDED]
- [ ] **C11** — the #211 shape `q^{-(g+t-1)/4}` verified against S1/S2
  (paper-stated vs derived arithmetic); OPEN O1 adjudicated: is
  poly-scale `beta` admissible? [CROSS-BRANCH: #211] [CITATION NEEDED]
- [ ] **C12** — the S3 comparison row completed (queue QX.10): raw
  KMS/DKKMS loss exponents vs the FM gap, from the actual papers
  [CITATION NEEDED]
- [ ] **C13** — `L_tan` pinned (value `1` vs `2`) by the QX.11 packet's
  strip-normal-form ruling; `eps0` re-instantiated accordingly (in-repo
  gate; no PDF needed)
- [ ] **C14** — (REQ-A)/(REQ-B) instantiated numerically at the three
  clean-rate operating points with all slots filled; a deterministic
  verifier recomputes the bit arithmetic (the upgrade of this note's
  lint into a real checker)

## 5. Bridge-ledger row

```text
row:        xr_small_set_engine (import)
supplies    (P4)/(P4'): expansion / energy / stability conclusion for
            (a, eps)-global subsets of J(n,j) at mu-scale — PENDING the
            SS4 slots; nothing supplied yet.
consumes    (I1) eps0 link caps      <- xr_globalness_from_ledger
                                        [QX.11 packet, in flight]
            (I2) E_3/phi dictionary + junta->paid transfer
                                     <- qx6_qx8_kms_bridges.md [PROVED]
consumers   xr_kms_parameter_matching (the composition arithmetic),
            xr_distance_dichotomy / QX.15 assembly (the MID band),
            r2_clean_rates (the campaign target).
conventions vertices = co-supports (j = n - A); "links" = the cells
            Cell_C(tau) of qx6_qx8 SS1.7/SS2.3, restriction graph
            J(n-r, j-|tau|); measure = uniform on the slice; the
            source's slice parameters [CITATION NEEDED: their notation]
            map onto (n, j) by [slot: fill together with C3].
scope       fixed-pair (worst-case) side ONLY; the moment-level table
            (qx14) is untouched by this import.
```

## 6. Non-claims (honesty ledger)

```text
N1  NOTHING here is proved or imported. No bibliographic datum is
    confirmed; every external constant and exponent is a slot. This note
    asserts no mathematics beyond quoting in-repo statements with their
    own labels.
N2  No claim that template KLLM-S matches any real theorem: it is OUR
    consumption shape. If the source statement differs STRUCTURALLY (not
    merely in constants), SS1-SS2 must be revised — the skeleton's
    purpose is to make that the only possible rework, and the checklist
    is designed to detect it (C2, C3, C7 are the structural checks).
N3  (P1)/h1 — the gvn/pumping step — is an in-program OPEN TARGET
    (xr_gvn, status TARGET in prize_dag.json), NOT part of the import,
    and NOT assumed done anywhere above.
N4  The #211 exponent shape is cross-branch and UNVERIFIED here; it is
    used only as a shape exemplar (SS2.4), and OPEN O1 records the
    demand-shape question it raises.
N5  Supply (I1) is PROVED only modulo the strip normal form (L_tan
    unpinned) and the #209 leak adjudication (Q3R.2 / task C-1); if the
    leaks are genuine, (I1) fails and this import has no hypothesis to
    consume — that failure mode belongs to R2, not to the import.
N6  No claim that (REQ-A) or (REQ-B) is satisfiable. C9 (g3 = 0) and
    OPEN O1 are both plausible failure points; failure means the cap
    needs a q-power strengthening (a new, harder statement, per
    xr_kms_parameter_matching) — a named outcome, not a small fix.
N7  The lint verifier checks document hygiene only (slot census, numeric
    audit, checklist state, symbol coverage); it verifies NO mathematics
    and its PASS is NOT evidence for any claim in SS1-SS3.
N8  Nothing here edits prize_dag.json or touches the moment-level
    coverage table; the scope is the fixed-pair conversion interface
    only, and the clean rates are the only budget instantiated.
```
