# Modal Dispatch Manifest

Detached cloud jobs for the campaign's remaining computational red nodes.
Retrieve results with: `~/.venvs/modal/bin/modal app logs <app-id>` (each job
prints ONE JSON line prefixed with the node name once its scan completes).
Every script embeds the pre-registered spec (verbatim) in its docstring and runs
a correctness GATE reproducing banked ground truth BEFORE the main scan; if the
gate fails the job prints `"status":"GATE_FAILED"` and does not report scan data.

Launch command used: `~/.venvs/modal/bin/modal run --detach <script>.py`
(local entrypoint uses `.spawn()`, so the job runs fully detached in the cloud;
the local "App completed" line refers only to the entrypoint returning).
All functions: `cpu=4, memory=8192, timeout=10800`, image `debian_slim` (stdlib
only, no sympy needed). All gates were also replayed locally (lightweight) and
PASS before launch.

---

## LAUNCHED

### 1. single_obstruction_valueset
- **app ID:** `ap-rLAsDplh1N7jQAiy0gmOEE`  (fc-01KWQJT0FC17B44NCPHH1TJ4C5)
- **script:** `nodes/single_obstruction_valueset/notes/modal_single_obstruction_valueset.py`
- **computes:** the pre-registered O-value collision-rate scan. For h = 21..40 at
  official-shape calibration rows (n=128 q~n^2 and q~n^3; n=256 q~n^2) it samples
  random 2h-supports R ⊂ mu_n, forces the monic degree-h square root S of L_R+λ
  (X78/X79 recursion, generalized from h=5 to arbitrary h), and records the value
  distribution of the FIRST obstruction O_{h-1} = coeff of X^{h-1} in S²−L_R:
  distinct values, max fiber, and observed-vs-uniform collision ratio (baseline
  C(N,2)/p). Per-config wall-time budget guarantees completion.
- **GATE:** reproduces X79's h=5 obstruction fact (constructed trade → 4 zero
  obstructions, λ a nonzero square); validates the h→general square-root at
  h∈{6,10,21,40}; proves O_{h-1} isolates the X^{h-1} coefficient.
- **pre-registered interpretation:** collision ratio ≈ uniform ⇒ fibers small ⇒
  lemma shape right (`UNIFORM_CONSISTENT`); ratio far above uniform at ANY
  calibration row ⇒ falsified, route dead (`HEAVY_COLLISIONS`).

### 2. midlarge_h7_20
- **app ID:** `ap-vQcKCgn6xEDBu2mAipdR7u`  (fc-01KWQJTQQ79DX8G9TGGMSN6B4K)
- **script:** `nodes/midlarge_h7_20/notes/modal_midlarge_h7_20.py`
- **computes:** the active-core exclusion scan for h = 7..20. Anchored
  meet-in-the-middle census (verbatim C1a machinery) over mu_n, n∈{16,32,64,128,
  256,1024}, at q~n^2 and q~n^3. Complete per-orbit census where the subset count
  fits (≤6e6); a genuine EXHAUSTIVE window sub-census over the first W roots
  otherwise (W auto-sized per (h,n)). Counts NON-TORAL active cores (trades whose
  halves are not both mu_h-cosets). Per-config time budget; incomplete cells are
  flagged (never silently reported as zero).
- **GATE:** reproduces banked counts — h3: 352 (n16 F17), 16 (n16 F97), 18/129
  anchored cores (n128/n256); h4 n16 F17: 120 non-toral + 6 toral (the decisive
  non-toral DETECTION); h5 n32 F97: 96.
- **pre-registered interpretation:** any non-toral active core found = FALSIFIER
  (charged/counted); zero across all calibrations ⇒ exclusion lemma licensed
  (`ZERO_ACTIVE_CORES_EXCLUSION_SUPPORTED`).

### 3. petal_excess_induction
- **app ID:** `ap-zd7RoOmGJ1hyL4MooOBOqg`  (fc-01KWQJV43X5JJ5NWXJ6FVFC1EJ)
- **script:** `nodes/petal_excess_induction/notes/modal_petal_excess_induction.py`
- **computes:** the re-scoped residue-line / full-petal-extras census as a
  function of excess c = d−ℓ = 2..8, on calibration rows built from the L1
  coset-chart residue bridge (t petals = cosets of the order-ℓ subgroup of F_p*,
  t∈{3,5}, ℓ∈{2,3}, p∈{1009,2003,4001,8009}). Per c it records the residue-line
  count = rank(π_{>d}R_{I,d}), dim K = (d+1)−rank (Lemma-13 bound c+1), the
  REFUTED exact-rank prediction, and the EXACT realizable extra count over missed
  cores (CRT-residue-degree ≤ d), enumeration-capped/time-budgeted.
- **GATE:** reproduces Witness A (c=2,t=3) and Witness B (c=5,t=5) — each
  realizable by the CRT shortcut AND found by from-scratch exact RS list decode —
  plus the route-cut (order-3 coset petals: exact-rank formula fails for every
  scalar choice, Lemma-13 floor never violated).
- **pre-registered interpretation:** dim K / extra counts FLAT in c ⇒ induction
  shape right (`FLAT_IN_C_INDUCTION_SHAPE_SUPPORTED`); GROWTH in c ⇒ amplification
  route needs a new idea (`GROWTH_IN_C_ROUTE_NEEDS_NEW_IDEA`).

### 4. xr_eliminant_vanishing_class
- **app ID:** `ap-gVR6MjqiBK4vxY9U1ABUZ7`  (fc-01KWQJVGNCCQE3EHVJ8XR7J90B)
- **script:** `nodes/xr_eliminant_vanishing_class/notes/modal_xr_eliminant_vanishing_class.py`
- **computes:** the E32-extended exhaustive COORDINATE-level census, pushing
  beyond the banked n=8 (which the local machine could not exceed) to n=9..13,
  k∈{2,3}, A=4, over several primes (the vanishing is p-specific). For every
  ordered light-budget support triple inside a full-rank light profile it
  evaluates the light-triangle eliminant normal_rank (verbatim E32 evaluator);
  a positive rank = a coordinate-special identically-vanishing eliminant. Each
  row is time-budgeted and flagged completed-exhaustively or truncated.
- **GATE:** reproduces the banked E32-COORD n=8 result (rows coord_n8_k2_A4 and
  coord_n8_k3_A4 over F_11: light triples > 0, ZERO coordinate-special defects).
- **pre-registered interpretation:** any coordinate-special vanishing inside a
  full-rank light profile = an unpaid identically-vanishing class = FALSIFIER
  (`FALSIFIER_UNPAID_VANISHING_FOUND`); none ⇒ structured branch empty at the
  extended level (`NO_COORDINATE_SPECIAL_VANISHING_BRANCH_EMPTY`), with
  paid-taxonomy labels attached to any hit.

---

## SKIPPED (precise reasons; no invented spec — the E17 lesson)

### 5. u2_per_row_certifier — SKIPPED
The node's own banked machinery (`verify_u2b_resultant_respec.py`) carries an
explicit FAIL-CLOSED rule: *"without a pinned row prime and an exhaustive
compressed pattern list, U2-B remains TARGET and must not be reported as
certified."* Both required inputs are absent on the current base:
(a) the Row-C-class row prime is UNPINNED (`xr_budget_audit.md` flags "Row C
prime unpinned"; U2-A pins the row LIST but not its characteristic);
(b) no proved finite normal-form sparse-relation pattern list exists — and raw
subset enumeration is infeasible (dihedral-orbit lower bound > 2^80 even at
b≤20, per U2-B-RESPEC). The resultant-kernel check gcd(Φ_n, Σ X^{re}) is
executable but requires those two missing inputs; supplying an invented prime or
pattern list would be a plausible-but-wrong certificate. Skipped pending a
respec that pins the prime and the compressed pattern generator.

### 6. integer_code_distance_cert — SKIPPED
Codex's `execution_report.md` already concludes verbatim: *"This node should not
be flipped on the current base."* The only located artifact is the C-4 toy
totality anchor (N'=16, p=12289, w≤6); there is NO row-specific integer matrix,
row descriptor, allowed cyclotomic-relation basis, or machine-checkable full-row
certificate in-repo, and the adjacent dependency `multi_multiplier_reduction` is
REFUTED (so the old multi-multiplier matrix route cannot be silently reused).
What is "missing" is the official ROW OBJECT itself (a spec input), not a
well-defined computation — the report's N'=128 direct-MITM cost table (2^38..2^48
states) is a feasibility note that still needs that absent matrix to instantiate.
Skipped: no faithful construction exists to dispatch.
