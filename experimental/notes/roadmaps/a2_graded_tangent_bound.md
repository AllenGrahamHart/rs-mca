# A2: graded tangent ledger bound assembly

- **DAG nodes:** `xr_partial_tangent_band`, `xr_heavy_triangle_charge`.
- **Task:** A2.
- **Status:** CONDITIONAL-ROUTED.  The routing and charge table are complete;
  the quantitative bound is not proved.
- **Verifier:** `experimental/scripts/verify_a2_graded_tangent_bound.py`.
- **Certificate:**
  `experimental/data/certificates/a2-graded-tangent-bound/a2_graded_tangent_bound.json`.

## Completed Routing

A2 composes three integrated inputs:

```text
X-3 / xr_smallcore_rungs_2a_2b: two-slope forcing map
W2: graded tangent cell table and heavy-triangle routing
A1: fixed-subcore rich-line cap assembly, with its remaining accounting gap
```

The completed routing is:

```text
r = k                         -> rank/spread boundary
k+1 <= r <= A-2               -> tangent-depth d = r-k
r >= A-1                      -> pencil cascade boundary
heavy triangle with 2b edge    -> direct tangent-depth charge
heavy triangle with no 2b edge -> deep-link staircase route
```

In every partial cell,

```text
d = r-k,
s = A-r,
d+s = t.
```

Thus the qx13 fresh codimension `s` and the tangent depth `d` are exactly
complementary.

## Verified Constants

The replayed verifier checks:

```text
W2 partial cells for t=1..8:          21 total
heavy profiles checked:              256,649
heavy profiles with direct 2b edge:   64,838
heavy profiles routed to deep links:  26,333
A1 observed fixed-subcore constant:   5
```

It also replays the X-3 two-slope forcing map and the W2 heavy-boundary
integer profiles.

## Remaining Residues

The quantitative graded tangent bound still has two named residues.

```text
a2_depth_cell_residual_occupancy
```

After the unified strip, bound the number of occupied tangent-depth-`d`
residual cells, and the emissions from each cell, uniformly for
`1 <= d <= t-2`.

```text
a1_lower_overlap_occupied_subcore_accounting
```

Route lower-overlap heavy-boundary partners to `O(n)` occupied deep-subcore
witnesses so the A1 fixed-subcore cap applies.

## Interpretation

A2 completes the charge routing.  No additional pairwise band exists beyond
the residual boundary, partial tangent cells, and cascade boundary.  The heavy
triangle boundary also introduces no new object: it has either a direct 2b
edge or a deep-link route.

The bound itself should not be promoted until `a2_depth_cell_residual_occupancy`
and `a1_lower_overlap_occupied_subcore_accounting` are proved.

## Verification

Run:

```bash
python3 experimental/scripts/verify_a2_graded_tangent_bound.py
```

The verifier replays:

```bash
python3 experimental/scripts/verify_w2_graded_tangent_ledger.py
python3 experimental/scripts/verify_xr_smallcore_rungs_2a_2b.py
python3 experimental/scripts/verify_a1_staircase_cap_assembly.py
```
