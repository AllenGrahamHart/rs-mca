# QA.24: degenerate-tower bookkeeping

DAG node: `tr_joint_telescope`.

Status: AUDIT.  This packet does not alter the lifting lemma proof.  It prices
the F2 exception in `tr_lifting_lemma.md`.

## Statement

The lifting lemma gives cardinality transfer

```text
|J_Rbar| = |T|
```

only when the joint tower is non-degenerate:

```text
[K(gamma):K] = M/D,        gamma = alpha^D.
```

If `m=M/D` and `d=[K(gamma):K] < m`, then the sigma map has a `K`-kernel of
dimension `m-d`, so the corrected one-sided bookkeeping is:

```text
|J_Rbar| <= |T| * |K|^(m-d).
```

Equivalently, at base level `K=B=F_q`, the correction column is

```text
(m-d) log2(q) bits.
```

For larger `K/B` of degree `e`, multiply the bit column by `e`.

## Clean-Rate Verdict

The verifier enumerates all dyadic `M | n`, `M >= 2`, for the six clean-rate
rows and separately flags the `M > t` subtable consumed by the staircase/TR
quotient-row split.

Degenerate towers are not absent:

```text
total (row,M) triples:             153
degenerate-possible triples:       153
M > t consumer triples:             50
```

For every nontrivial period `M`, the `D=M` cell is forced non-degenerate
(`m=1`), but every class closure with `D<M` has `m>1` and needs either the
non-degeneracy hypothesis or the correction factor.

## Row Summary

```text
row    rate   periods  M>t  first M>t      first worst correction     max worst correction
RowC   1/4    10       8    8              1750 bits                  255750 bits
RowC   1/8    10       8    8              1750 bits                  255750 bits
RowC   1/16   10       9    4               750 bits                  255750 bits
prize  1/4    41       8    17179869184    4396328523929.7 bits       562730051095500.9 bits
prize  1/8    41       8    17179869184    4396328523929.7 bits       562730051095500.9 bits
prize  1/16   41       9    8589934592     2198164261836.9 bits       562730051095500.9 bits
```

The "first worst correction" is the base-level worst case for the first
`M>t` period in that row, using `D=1,d=1`.  The actual correction for a given
cell is the sharper `|K|^(M/D-d)`.

## Consequence

Any use of `tr_lifting_lemma.md` Theorem LL(iii)'s equality in TR must carry
one of:

1. the non-degeneracy hypothesis `[K(gamma):K]=M/D`;
2. the correction factor `|K|^(M/D-d)`;
3. a separate argument excluding the degenerate tower data being counted.

There is no row-level arithmetic absence statement for the clean-rate rows.

## Verifier

Run:

```bash
python3 experimental/scripts/verify_qa24_degenerate_towers.py
```

The pinned certificate is
`experimental/data/certificates/qa24-degenerate-towers/qa24_degenerate_towers.json`.
