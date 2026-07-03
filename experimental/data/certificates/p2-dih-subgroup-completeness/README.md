# P2 Dihedral Subgroup Completeness Certificate

This certificate supports the P2 packet for DAG node
`f_dih_subgroup_completeness`.

Run:

```bash
python3 experimental/scripts/verify_p2_dih_subgroup_completeness.py
```

The verifier checks:

- exact `PGL_2` set-stabilizers of small quadratic-field 2-power domains by
  ordered triples;
- the wild subfield-circle exceptions `F_9/mu_4` and `F_49/mu_8`;
- nearby non-wild rows where the stabilizer is exactly dihedral;
- the row-level congruence test used as a sufficient tame condition.
