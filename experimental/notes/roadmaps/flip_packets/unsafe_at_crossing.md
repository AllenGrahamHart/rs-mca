# Flip packet: unsafe_at_crossing

- **Node:** `unsafe_at_crossing`
- **Current critical label:** UNPROVED
- **Verdict:** DEFECT
- **Referee summary:** the collided averaged-conversion branch is now wired,
  but the collision-free qfloor/value-set branch remains prose-only. The
  remaining issue is still a wiring defect rather than a clean TRUE-RED
  mathematical singleton.

## Statement

> For each admissible row: B_C(a_safe - 1) > B* witnessed at the ADJACENT grid point — collision-free branch: qfloor value-set family; collided branch: averaged fiber-to-slope conversion.

## Req Children

| child | live status | critical label | role |
|---|---:|---:|---|
| `averaged_slope_conversion` | CONJECTURE | CONDITIONAL | Supplies the collided averaged fiber-to-slope conversion branch. |

That is only a partial repair. The statement itself cites two branch
hypotheses:

- collision-free branch: the qfloor/value-set family;
- collided branch: averaged fiber-to-slope conversion.

Those are not merely explanatory phrases. They are proof obligations for the
unsafe witness at the adjacent point.

## Referee Argument

This packet does not recommend `TRUE RED` because the local content has not
been isolated as a single open theorem. The live graph now wires the collided
branch, but it still leaves the collision-free branch in prose. The route note
`q3r5_three_rate_dossier_skeleton.md` already records open slots for the
branch inputs:

```text
UNSAFE-2  Witnesses at the adjacent point. Collision-free branch: the
          qfloor value-set family ... collided branch: the averaged
          fiber-to-slope conversion ... assembled any-gate
          [OPEN SLOT -> DAG: unsafe_at_crossing].
```

The live graph therefore still hides a dependency in prose. A referee cannot
check whether `unsafe_at_crossing` follows from its children while the
collision-free witness node is not a req child.

The precise fix is to choose one of two shapes:

1. Keep `unsafe_at_crossing` as an assembly node and wire the missing req edge
   from the appropriate collision-free qfloor/value-set certificate node
   (`qfloor_exact` if that is intended to carry the branch, otherwise the
   row-specific witness certificate).
2. Rewrite it as a primitive target with no branch clauses, e.g. "construct
   adjacent-grid unsafe witnesses for every admissible row." Under that rewrite
   the node should be TRUE RED until the construction is proved.

In the live wording, the correct referee verdict is DEFECT.

## Evidence Pins

- `unsafe_at_crossing`: `ce0dc79f00cfed1f`
- `averaged_slope_conversion`: `58feb09620e4ea1b`
- `qfloor_exact`: `da5de7e28aee0eeb`
- `certified_valueset_lower`: `00335d6a53907bd9`

## Source Quotes

- `q3r5_three_rate_dossier_skeleton.md` Section 3.2 names
  `averaged_slope_conversion` as the collided-branch open slot and
  `unsafe_at_crossing` as the assembled any-gate slot.
- `assembly_sweep_ring1.md` promotes `mca_unsafe` only because
  `unsafe_at_crossing` states the per-row witness content; it does not prove
  the witness node itself.
