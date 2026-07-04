# E32-COORD Coordinate Sliver Certificate

This certificate supports the E32-COORD audit for DAG node
`xr_eliminant_vanishing_class`.

Run:

```bash
python3 experimental/scripts/verify_e32_coordinate_sliver.py
```

The verifier applies the `xr_triangle_eliminant_form` evaluator pointwise, not
just by Venn profile.  It exhausts two exact `n=8` toy rows over `F_11` and
records defect densities per full-rank light profile:

- `k=2,A=4`: `87,360` coordinate placements across `19` profiles;
- `k=3,A=4`: `294,840` coordinate placements across `40` profiles.

No coordinate-special eliminant vanishing is found.
