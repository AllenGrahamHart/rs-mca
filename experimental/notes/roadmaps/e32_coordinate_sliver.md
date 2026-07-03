# E32-COORD: coordinate-special eliminant sliver

DAG node: `xr_eliminant_vanishing_class`.

Status: AUDIT.  This is the coordinate-level refinement after E32-MERGED.  It
does not prove the global hypersurface-rationing statement.

## Scope

E32-MERGED ruled out profile-forced light-triangle eliminant vanishing: the
canonical representative of every checked full-rank light profile has full
normal-form rank.

This packet applies the same evaluator pointwise inside the profile cells.  It
exhausts all ordered light triples of size-`A` supports for two exact `n=8`
toys over `F_11`:

| row | full-rank light profiles | coordinate placements | defects |
| --- | ---: | ---: | ---: |
| `n=8,k=2,A=4,t=2` | 19 | 87,360 | 0 |
| `n=8,k=3,A=4,t=1` | 40 | 294,840 | 0 |

Total pointwise placements checked: `382,200`.

## Interpretation

No coordinate-special vanishing appears in the audited toys.  Thus the
remaining sliver is empty in practice at this scale, and the program's safe
route can continue to treat the coordinate-special branch as a proper
hypersurface-rationing term rather than a new paid class.

If a future larger row finds a defect, the verifier records examples with a
paid-boundary label set (`light_heavy_boundary`, `sunflower_core`,
`disconnected_pair_overlap`, `rung_2b_boundary_or_tangent`) and leaves any
residue explicitly as `unclassified_coordinate_special`.

## Non-Claim

The `n=16` profile census represents billions of coordinate embeddings, so this
packet deliberately does not enumerate all `n=16` placements on this machine.
It is an exact toy audit and a density-table harness for future bounded rows.

## Verifier

Run:

```bash
python3 experimental/scripts/verify_e32_coordinate_sliver.py
```

The pinned certificate is
`experimental/data/certificates/e32-coordinate-sliver/e32_coordinate_sliver.json`.
