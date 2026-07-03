# E32-MERGED — stagnation + exception profile census

DAG consumers: `xr_eliminant_vanishing_class`, `spread_syzygy_ident`,
`xr_light_triangle_eliminant`.

Status: EVIDENCE / profile-exact negative census.  This packet does not prove
the consumer nodes; it removes the profile-forced S9 scenario at the checked
rows and restates the face-3 exception classes in the 2c eliminant language.

## Scope

The verifier is intentionally light-compute.  It enumerates **all Venn
profiles** of three equal-size agreement supports and evaluates a canonical
realization of each profile with the `xr_triangle_eliminant_form` normal
matrix.  It also records the exact number of coordinate embeddings represented
by the profiles.  It does **not** enumerate every coordinate embedding: even
the smallest `n=16` light row below represents `2,770,267,500` ordered
coordinate triples.

This is the right scope for detecting identically-valid/profile-forced
eliminant branches.  Coordinate-special vanishing remains a possible future
E32-coordinate refinement, but it is not a heavy run to do on this machine.

## Results

### E27 corridor row

For the actual E27 corridor row

```text
F_97, H = mu_16, n = 16, k = 8, A = 11, t = 3
```

there are `150` Venn profiles of three size-`11` supports.  Of these, `9`
are far-spread (`r_ij < k` for all pairs).  The stacked eliminant matrix has
full rank `3t` on all `9`; no profile-forced far-spread stagnation appears.

The light-triangle inequality is impossible on this row.  Since

```text
sigma = r_01 + r_02 + r_12 - r_012 = 3A - |T_0 union T_1 union T_2|
```

and the union has size at most `n`, every profile has

```text
sigma >= 3A - n = 33 - 16 = 17 > 2k = 16.
```

So E27's corridor row has no light configurations to classify; its triple
content is heavy/boundary, not beta-3 light.

### n=16 light rows

The verifier then checks three `F_17^*` rows where the light regime is
nonempty:

```text
row                 total profiles   light profiles   represented triples
k=2, A=4, t=2       81               34               2,770,267,500
k=4, A=5, t=1       150              91               20,570,598,048
k=4, A=6, t=2       252              163              371,862,499,008
```

For every light profile satisfying

```text
sigma <= 2k
max_i sum_{j != i} |T_i cap T_j| >= k+1
```

the canonical normal-form matrix has full rank.  No identically-vanishing
light profile is found, and therefore no unpaid S9 profile class is found.

## E13 classes in the normal form

The face-3 exception classes are the same syzygy anatomy, expressed without
requiring the supports to come from aligned slopes.

| E13 class | Eliminant normal-form reading |
| --- | --- |
| AG/net | Incidence-design normal form: row dependencies come from repeated low-dimensional block incidences. Rank drop is paid by finite-geometry/net structure, not a primitive light eliminant. |
| v-degenerate | One coordinate leg carries a constrained-support dual word with zero `v`-syndrome. In the two-coordinate normal form this is a tangent/degenerate branch rather than a primitive rank-stagnating light triangle. |
| syzygy circuit | A one-dimensional full-support kernel of the normal-form matrix, with every deletion independent. This is exactly the minimal-circuit determinantal branch; it feeds `circuit_nongeneric` / `circuit_locus_density` rather than an unclassified paidness failure. |

Thus E13's observed classes are expressible in the 2c eliminant language.
The census found no fourth profile-forced branch.

## Interpretation

No S9 event is present in the checked profile census.

What remains for the consumer nodes is not a named mystery:

- `xr_eliminant_vanishing_class`: still needs a coordinate-level or symbolic
  classification if later evidence finds coordinate-special vanishing.
- `deep_link_staircase` / E33: still needed for population bounds near the
  heavy/light boundary.
- `spread_syzygy_ident`: the language bridge is now written; the quantitative
  face-3 burden remains the circuit/locus-density branch already named in the
  DAG.

## Verifier

Run:

```bash
python3 experimental/scripts/verify_e32_merged_census.py
```

The recomputed summary is pinned in
`experimental/data/certificates/e32-merged-census/e32_merged_profile_census.json`.
