# The mca_grand assembly implication (statement-level theorem)

- **Status:** PROVED (statement-level implication; AUDIT-grade — the
  mirror of `list_grand_assembly_implication.md`).
- **Claim:** if the five requirement children of `mca_grand` hold AS
  STATED in `prize_dag.json`, then `mca_grand` holds as stated.
- **Consequence:** `mca_grand` flips TARGET -> CONDITIONAL.
- **Verifier:** `experimental/scripts/verify_mca_grand_assembly.py`
  (statement pins + the rate-1/2 req wire on adjacency_closing).

## The target (pinned d30ad9a0f59b57cc)

> For each admissible C: exhibit adjacent a with B_C(a-1) > floor(q_line/2^128) >= B_C(a), all conventions printed.

## The implication

1. **The two bounds at the adjacent pair** — `mca_safe` (pinned
   e79900ef03bce187): B_C(a_safe) <= B*; `mca_unsafe` (pinned
   d9a047c757c6781c): B_C(a_safe - 1) > B*. Stated at the SAME
   a_safe, these two facts ARE the adjacent exhibit.
2. **The pair exists** — `adjacency_closing` (pinned
   dc61467625cafd3b): the corridor between the proved
   safe and unsafe agreements collapses to one grid step. Its own
   requirement set carries rate 1/2 (rate_half_coverage_gap, promoted
   ev -> req by this audit) so "each admissible C" has no silent rate
   exclusion.
3. **The guards** — `s0_zero_open` (pinned df384f63456868b1):
   "all conventions printed" is the grand's own closing clause;
   `mixed_radix_frontier` (pinned 9bb2a65e06a3e64c):
   the official smooth family.

Redundancy note (harmless, same as the list side): (1) partially
restates inside (2)'s corridor form. Supporting evidence not consumed:
ld_bridge (PROVED), second_pin_or_wall.

## Statement pins

- `mca_grand`: sha256/16 = `d30ad9a0f59b57cc`
- `s0_zero_open`: sha256/16 = `df384f63456868b1`
- `mca_safe`: sha256/16 = `e79900ef03bce187`
- `mca_unsafe`: sha256/16 = `d9a047c757c6781c`
- `mixed_radix_frontier`: sha256/16 = `9bb2a65e06a3e64c`
- `adjacency_closing`: sha256/16 = `dc61467625cafd3b`
