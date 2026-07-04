# The list_grand assembly implication (statement-level theorem)

- **Status:** PROVED (statement-level implication; AUDIT-grade referee
  argument — no computation; the verifier pins the hypotheses' exact
  wording against the live DAG).
- **Claim:** if the five requirement children of `list_grand` hold AS
  STATED in `prize_dag.json`, then `list_grand` holds as stated.
- **Consequence:** `list_grand` flips TARGET -> CONDITIONAL (amber
  under the local color semantics): the prize's list half is proved
  conditional on its five inputs.
- **Verifier:** `experimental/scripts/verify_list_grand_assembly.py`
  — checks the five req edges exist and that every statement this
  packet quotes still matches the DAG verbatim (sha256 pins below).
  If any child's statement is edited, this packet FAILS and the
  implication must be re-refereed.

## The target (pinned 622f54432e3d690b)

> For each admissible C and constant m: exhibit adjacent delta with |Lambda(C^{==m},.)| crossing 2^-128 |F| at it.

## The implication, statement by statement

1. **The exhibit** — `list_adjacency_closing` (pinned 0db1902038e33944):
   > For each admissible row and constant m: exhibit adjacent delta with sup_U |Lambda(U, delta-1)| > eps*|F| >= sup_U |Lambda(U, delta)| (per the official m-quantifier). The determination's list half, previously unpriced — the exact mirror of adjacency_closing.

   This IS the grand's operational content per admissible row: the
   adjacent-delta crossing exhibit under the official m-quantifier.
   Its own requirement set carries rate 1/2 (`rate_half_coverage_gap`
   is wired as its req), so "each admissible C" is covered with no
   silent rate exclusion.

2. **The two bounds the exhibit consumes** — `list_safe` (pinned 2f2916c84424728f):
   > #Lambda(C^{==m}, delta) <= 2^-128 |F| above the window: ImgFib bound + codegree conversion + m-handling per the official quantifier.

   and `list_unsafe` (pinned 9c2a69f576a231a6):
   > List unsafe at gate: qcore counting (conventions pending)

   Together: the list is small above the window and crosses at the
   gate. The exhibit needs exactly these two facts at the adjacent
   pair of radii.

3. **The object-identity guard** — `s0_zero_open` (pinned df384f63456868b1):
   > Every object axis EQUAL or BRIDGED(loss printed); zero OPEN axes before any prize-facing claim.

   This converts "our Lambda" into "the official Lambda": every axis
   EQUAL or BRIDGED with printed loss, zero OPEN axes before any
   prize-facing claim. The seam between list_safe's "above the
   window" convention and the exhibit's adjacent-delta convention is
   an axis in s0's ledger — the implication leans on s0 exactly here,
   which is why s0 is a hypothesis and not a remark.

4. **The domain-family guard** — `mixed_radix_frontier` (pinned 9bb2a65e06a3e64c):
   > LIKELY VACUOUS — the standard reading of 'smooth' in the FRI/STARK proximity literature is 2-smooth (power-of-2 order), and every repo row is 2-power. The live prize page leaves it undefined, so the ePrint confirmation (Q0.1 freeze row) closes this. IF the official family were broader: (a) wp0_2's c

   Guarantees the row family ranged over covers the official smooth
   family (likely vacuous under the 2-power reading; conservative
   otherwise).

## Why this is a proof and not a plan

The grand's statement is the conjunction-unpacking of (1)-(4): an
adjacent-delta crossing exhibit (1) built from the two bounds (2),
asserted of the official objects (3) over the official family (4).
No mathematical content beyond the children is consumed; the only
non-definitional step is the seam/quantifier accounting, which is
exactly what (3) prices. Redundancy note: (2) is partially restated
inside (1)'s per-row form; harmless — the conjunction remains
sufficient.

## Statement pins

- `list_grand`: sha256/16 = `622f54432e3d690b`
- `s0_zero_open`: sha256/16 = `df384f63456868b1`
- `list_safe`: sha256/16 = `2f2916c84424728f`
- `list_unsafe`: sha256/16 = `9c2a69f576a231a6`
- `mixed_radix_frontier`: sha256/16 = `9bb2a65e06a3e64c`
- `list_adjacency_closing`: sha256/16 = `0db1902038e33944`
