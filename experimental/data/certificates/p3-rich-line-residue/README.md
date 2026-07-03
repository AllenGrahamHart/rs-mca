# P3 Rich-Line Residue Certificate

This certificate supports the P3 packet for DAG node `deep_link_staircase`.

Run:

```bash
python3 experimental/scripts/verify_p3_rich_line_residue.py
```

The verifier embeds the P1 affine-net obstruction on the 2-power
multiplicative domain `mu_64 <= F_193^*` and checks the intended rich supports
against local tangent-pencil, quotient-tail, and dihedral full-fiber predicates.
