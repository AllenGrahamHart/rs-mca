# QA.23 Wild Row Audit Certificate

This certificate supports the QA.23 audit for DAG node `wild_row_audit`.

Run:

```bash
python3 experimental/scripts/verify_qa23_wild_row_audit.py
```

The verifier enumerates the `26` admissible Mersenne wild rows below `2^256`,
checks coset inheritance by dilation conjugacy, and exhaustively enumerates the
`413`-subgroup Dickson lattice of the `F_49/mu_8` toy via `PGL_2(F_7)` acting
on `P^1(F_7)`.

The toy window audit finds five orbit partitions present in the full Dickson
lattice and absent from the tame dihedral/Sylow-2 lattice:
`(1,1,3,3)`, `(1,1,6)`, `(1,7)`, `(2,3,3)`, `(2,6)`.
