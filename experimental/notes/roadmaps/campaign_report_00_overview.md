# Clean-rate MCA campaign — maintainer report (overview)

- **Status:** DRAFT / living. Modular: this file is the overview; the
  proof-chain, the terminal open problem, and the falsification ledger
  live in sibling `campaign_report_*` files.
- **Audience:** the maintainer (przchojecki) and, for the terminal
  problem, the additive-combinatorics community.
- **Scope:** the clean-rate (rho in {1/4, 1/8, 1/16}) MCA
  determination. Rate 1/2 is the separate endgame, not covered here.

## One-paragraph summary

The clean-rate MCA safe side has been reduced, through a fully
verified chain, to a single arithmetic-geometry counting estimate:
the number of "primitive" (non-symmetry-charged) Prouhet-Tarry-Escott
trades inside the 2-power subgroup mu_n of F_q. Every reduction step
carries a machine-checked certificate; the terminal estimate is
proved for h = 2 and (at the n^3 rung) for h = 3, holds empirically
(single-digit counts in range, exact vanishing at q >= n^3), and is
squeezed to near-sharp form by verified low-q falsifiers. What remains
is either one more idea (a high-dimensional subgroup point-count that
the current literature lacks) or the shipping of the sharpest
open-problem statement the prize has produced.

## What is proved (chain, maintainer-checkable)

Each link has a note + a green stdlib verifier under
`experimental/{notes/roadmaps, scripts, data/certificates}`:

1. The poly-forcing **compiler**: the clean-rate obligation is
   `R_post(u,v;A) <= 16 n^3` per pair (exact integer sufficiency at
   all six candidate rows).
2. The **strip taxonomy** is symmetry-complete: tangent + pullback,
   where pullback = {multiplicative X^m, dihedral X^m + a X^-m,
   moment/PTE blocks, affine} — unified via the star-PTE lemma and
   classified by the tame Laurent-Ritt / toral-stabilizer theorem
   (self-contained, zero imports).
3. The **face reductions**: face 1 (jointness) closed by exact
   telescoping + the lifting lemma; faces 3/4 identified into the
   syzygy anatomy; the split-pair / active-core reduction (orbit +
   anchor-injectivity, both proved).
4. The **terminal estimate**, base cases: h = 2 rung
   `A_2 <= 6 n^{5/3}` (Corvaja-Zannier); h = 3 cubic cap
   `# active pairs < n^3` (degree-2n root bound on N_x^n - D^n).

DAG snapshot: 318 nodes, 91 PROVED (verifier-backed), 18 CONDITIONAL,
10 REFUTED-and-repaired. Validator enforces: criticals carry exact
statements; refuted nodes cannot be requirements; every conjecture
carries a wired falsifier.

## What remains

See `campaign_report_01_terminal.md`. In one line: bound the primitive
active-core count for h >= 4 (and sharpen h = 3 past the n^3 rung),
most promisingly as a high-q vanishing theorem `q >= n^c => count = 0`
for any `c <= 6` (official rows afford it; empirics vanish at c = 3).

## Asks of the maintainer

1. Integration sweep of `allen/prize-dag-delta` (the verified chain).
2. A ruling on the Reading-B (procedure-as-determination) semantics
   the compiler assumes.
3. The rules-freeze artifact (smooth = power-of-2 coset; k <= 2^40;
   |F| < 2^256 — all used as stated).
