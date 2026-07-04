# Flip packet: r2_clean_rates

- **Node:** `r2_clean_rates`
- **Current critical label:** UNPROVED
- **Verdict:** PROMOTE-CONDITIONAL
- **Referee summary:** the current critical DAG has replaced the old global
  `r2_rigidity` node with this compiled clean-rate target. Once the clean
  residual any-gate and its arithmetic/import children are granted, the parent
  is the exact clean-rate compiler target.

## Statement

> CURRENT FORM (the compiled target, superseding the X-1 emptiness framing — see the day's arc in notes): at each clean-rate decision candidate, for every pair (u,v), the post-strip residual slope count satisfies R_post(u,v; A) <= 16 n^3 (dihedral and extension columns INSIDE R_post). Sufficiency for the determination is PROVED exact integer arithmetic (the poly-forcing compiler: 16 n^3 <= s_lo at all six candidates, prize rows tight at 29 n^3). The supply side is the face-4 rung ladder under xr_clean_residual_any_gate. TOOL ASSIGNMENT stands: exclusion-type per-pair dichotomies here; the KLLM/globalness composition reserved for rate 1/2's E[X] >= 1 rows.

## Req Children

| child | live status | critical label | role |
|---|---:|---:|---|
| `xr_globalness_from_ledger` | PROVABLE | PROVABLE | Import/shortcut context for globalness, especially outside the clean-rate exclusion route. |
| `xr_small_set_engine` | PROVABLE | PROVABLE | Import context for the KLLM/globalness engine. |
| `xr_radius_arithmetic` | PROVABLE | PROVABLE | Computes which rows are clean-rate rows and where the hard rate-1/2 regime begins. |
| `xr_clean_residual_any_gate` | TARGET | UNPROVED | Supplies the actual clean-rate per-pair residual bound through the face-4 ladder. |

## Referee Argument

The parent is the compiled campaign target, not the old all-rate R2 theorem.
The exact budget sufficiency is already proved by the poly-forcing compiler:
`16 n^3` residual mass fits the safe-side allowance at all six clean-rate
decision candidates. The remaining supply-side statement is precisely
`xr_clean_residual_any_gate`, which rewrites the dead emptiness target as a
polynomial residual bound.

Granting the children:

1. `xr_radius_arithmetic` identifies the clean-rate operating points and
   excludes the rate-1/2 contentful FM rows from this target.
2. `xr_clean_residual_any_gate` supplies the required per-pair post-strip
   polynomial residual at those operating points.
3. The two globalness children are available imports/context for the broader
   XR composition, but do not add extra local content to the clean-rate
   compiler once the any-gate is granted.

Therefore the parent should be CONDITIONAL: the hard content is the residual
any-gate and its descendants, not this compiled target node.

## Caution

The node text still mentions KLLM/globalness as tool assignment context while
also saying that KLLM/globalness is reserved for rate 1/2. If the roadmap lane
wants strict minimal req edges, it can demote `xr_globalness_from_ledger` and
`xr_small_set_engine` from req children to evidence/context edges. That is not
needed for the conditional promotion: extra granted children are harmless.

## Evidence Pins

- `r2_clean_rates`: `09d963096b27ee33`
- `xr_globalness_from_ledger`: `66698d8ee5d497a7`
- `xr_small_set_engine`: `22d4196e33ea3135`
- `xr_radius_arithmetic`: `8492a9a618ec287d`
- `xr_clean_residual_any_gate`: `15e5616ad4375364`

## Source Quotes

- `r2_identification.md` says the live critical path goes through
  `r2_clean_rates <- xr_clean_residual_any_gate <- the smallcore/spread chain`
  and records the pin replacing old `r2_rigidity`.
- `xr_clean_poly_forcing_reduction.md` proves that a `16 n^3` post-strip
  residual is absorbed at every clean-rate candidate.
- `qx15_xr_assembly_draft.md` identifies the clean-rate demand as the
  worst-case conversion priced within the `2^100` / `16 n^3` budget.
