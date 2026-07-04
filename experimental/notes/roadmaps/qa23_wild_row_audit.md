# QA.23: wild-row Dickson audit

DAG node: `wild_row_audit`.

Status: AUDIT.  This packet closes the requested arithmetic and the fully
computable `F_49/mu_8` support/window toy.  It does not prove a prize-scale
Dickson budget theorem for every wild row.

## Wild rows below `2^256`

For 2-power `n`, the wild subfield-circle mechanism requires

```text
n = p+1,  p = 2^r-1 a Mersenne prime,
q = p^(2s) < 2^256.
```

The verifier enumerates the requested rows:

| `r` | `n` | admissible `s` | count |
| --- | ---: | --- | ---: |
| 13 | `8192` | `1..9` | 9 |
| 17 | `131072` | `1..7` | 7 |
| 19 | `524288` | `1..6` | 6 |
| 31 | `2147483648` | `1..4` | 4 |

There are `26` admissible wild `(n,q)` rows.  The full exact `q` values are in
the pinned certificate.

Cosets inherit wildness: `alpha*mu_n` is obtained from `mu_n` by a dilation, so
its `PGL_2` stabilizer is conjugate to the subgroup-circle stabilizer.

## `F_49/mu_8` toy audit

The Cayley model identifies the wild toy with `P^1(F_7)`.  The verifier builds
`PGL_2(F_7)` as permutations of the eight projective points and checks:

```text
|PGL_2(F_7)| = 336,
the action is sharply 3-transitive,
the subgroup lattice has 413 subgroups,
the selected tame Sylow-2/dihedral lattice has 19 subgroups.
```

For every enumerated subgroup, every subgroup-invariant support is exactly a
union of subgroup orbits.  Thus the support/window toy has no escape outside
the Dickson-derived quotient strata.

## Window arithmetic verdict

The enlarged Dickson symmetry creates orbit-window partitions absent from the
tame dihedral lattice.  The new partitions at `F_49/mu_8` are:

```text
(1,1,3,3)
(1,1,6)
(1,7)
(2,3,3)
(2,6)
```

The tame dihedral/Sylow-2 sublattice sees only

```text
(1,1,1,1,1,1,1,1), (1,1,2,2,2), (2,2,2,2),
(2,2,4), (4,4), (8).
```

So the wild rows are not a program failure, but they do require a separate
Dickson-lattice window column.  A dihedral-only ledger is incomplete there.

## Verifier

Run:

```bash
python3 experimental/scripts/verify_qa23_wild_row_audit.py
```

The pinned certificate is:

```text
experimental/data/certificates/qa23-wild-row-audit/qa23_wild_row_audit.json
```
