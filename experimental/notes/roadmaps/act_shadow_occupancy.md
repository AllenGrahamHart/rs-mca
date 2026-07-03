# ACT-SHADOW: active occupied subcores and depth cells

- **DAG nodes:** `a1_lower_overlap_occupied_subcore_accounting`,
  `a2_depth_cell_active_shadow_bound`, `u1_alpha_active_core_incidence`.
- **Task:** ACT-SHADOW.
- **Status:** toy falsifier negative; active-shadow evidence.
- **Verifier:** `experimental/scripts/verify_act_shadow_occupancy.py`.
- **Certificate:**
  `experimental/data/certificates/act-shadow-occupancy/act_shadow_occupancy.json`.

## Purpose

OCC-1 and OCC-2 showed the same failure mode: the formal cell lattice is far
too large, so a constant cap per formal cell cannot close the accounting.  The
needed object is the active shadow: cells actually occupied by aligned partners
after the paid strip.

This verifier extends the E33/OCC-1 sampled aligned-pair engine with the A2
depth-cell activity filter.  It counts, in the same pass:

```text
lower-overlap occupied subcores:  k/2 < r < k
partial-tangent depth cells:      r = k+d, 1 <= d <= t-2
```

For the E33 toy shape `n=16, k=8, A=11, t=3`, these are:

```text
lower band: r = 6, 7
depth band: r = 9, with d=1 and s=A-r=2
```

## Result

The lower-overlap column reproduces OCC-1.  The new depth-cell active column
does not find a falsifier.

```text
row                  lower max active   lower max K   depth max active   depth max K   depth formal cells
F_97 / mu_16         9                  5             10                 4             55
F_17 / mu_16         42                 5             10                 6             55
```

Budget products stay below `n^2 = 256`:

```text
F_97: lower active*maxK = 45, depth active*maxK = 40
F_17: lower active*maxK = 210, depth active*maxK = 60
```

The observed aligned events by overlap are:

```text
F_97: lower r=6 -> 186, r=7 -> 684; depth r=9 -> 263
F_17: lower r=6 -> 852, r=7 -> 2882; depth r=9 -> 926
```

## Interpretation

The formal depth-cell count at `r=9` is `C(11,9)=55`, but the active shadow
never exceeds `10` occupied cells in the sampled anchors.  This matches the
P-A and OCC-1 shape:

```text
raw/formal lattice: too large;
active post-strip shadow: small;
active * local multiplicity: within n^2.
```

The result supports treating `a1_lower_core_shadow_incidence_bound` and
`a2_depth_cell_active_shadow_bound` as the same rarity-counting problem: count
activity, not formal cells.  It is evidence, not a proof.

## Verification

Run:

```bash
python3 experimental/scripts/verify_act_shadow_occupancy.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_act_shadow_occupancy.py --write-certificate
```

Current replay: **14 PASS, 0 FAIL**.  Timed replay peak RSS was `115688 KB`,
with no swaps.
