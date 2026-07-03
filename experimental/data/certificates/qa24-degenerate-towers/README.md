# QA.24 Degenerate-Tower Bookkeeping Certificate

This certificate supports the QA.24 audit for the lifting lemma's F2 flag.

Run:

```bash
python3 experimental/scripts/verify_qa24_degenerate_towers.py
```

The verifier enumerates all dyadic periods `M | n`, `M >= 2`, for the six
clean-rate rows from `xr_budget_audit` / QA.22 and flags the `M > t` consumer
subtable.

Verdict: degenerate towers are **not absent**.  For every nontrivial period
`M`, a class closure with `D < M` has `m=M/D > 1` and can lose the lifting
lemma's cardinality equality.  The correction factor is:

```text
|K|^(m-d),   d = [K(gamma):K].
```

The JSON certificate records the base-level bit columns `(m-d) log2(q)`;
multiply those bit columns by `e=[K:B]` for larger intermediate fields.
