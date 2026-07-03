# F2-EXT: exact large-band MITM for b=9,10

- **DAG node:** `x4b_moment_trade_exclusion`.
- **Task:** F2-EXT.
- **Status:** EVIDENCE.  The `b=9,10` MITM bands are now scanned exactly at
  the registered `n=32,64`, `t=3` rows.  This is not a proof for official
  rows.
- **Verifier:** `experimental/scripts/verify_f2_ext_large_bands.py`.
- **Certificate:**
  `experimental/data/certificates/f2-ext-large-bands/f2_ext_large_bands.json`.

## Method

The scan searches for primitive `0/1` dual words on `mu_n` with

```text
sum_{e in E} zeta^(r e) = 0,      r = 1,2,3,
```

at weights

```text
b = 9, 10.
```

For `b=9`, it uses an exact `4+5` meet-in-the-middle.  For `b=10`, it uses a
bounded-memory `5+5` MITM: the `h=5` half-table is stored as numpy `uint64`
syndrome and mask arrays, lexicographically sorted, and target groups are
found by vectorized search.  This avoids a Python dictionary over
`C(64,5)=7,624,512` entries.

## Rows

For each `n in {32,64}` the verifier scans:

```text
first 10 primes p == 1 mod n,
representatives near n, n^2, n^3, and 2^61.
```

Rows already included in the first-ten sweep are deduplicated.

## Results

Primitive hits exist in the low-prime region:

```text
n=32: p=97 has primitive b=9 and b=10 hits.
n=64: p=193,257,449,577,641,769 have primitive b=9 and b=10 hits.
n=64: p=1153,1217,1601 have primitive b=10 hits.
```

The low-prime hit pattern is not monotone: for example `n=64, p=1409` has no
primitive `b=9,10` hit in the exact scan, while `p=1601` has a primitive
`b=10` hit.  This supports the resultant/divisibility interpretation rather
than a clean numerical threshold.

No primitive `b=9,10` hit appears in the representative high-scale rows:

```text
n=32: p near n^2, n^3, 2^61 clean.
n=64: p near n^2, n^3, 2^61 clean.
```

At `n=64, p=4289` (the `n^2` representative), the verifier does see
`4032` zero-syndrome `b=10` blocks, but all are quotient/dihedral-structured
under the primitive filter.

## Interpretation

F2-EXT closes the empirical `b=9,10` gap from the first F2 census.  The
large-prime official-row direction still survives: representative `n^2`,
`n^3`, and `2^61` rows are primitive-clean through the full requested
`b=4..10` toy window once this result is combined with F2/E37.

The new low-prime `b=10` hits also reinforce the X-6 correction: the right
route is per-row certification / resultant divisibility, not a universal
monotone large-prime theorem.

## Verification

Run:

```bash
python3 experimental/scripts/verify_f2_ext_large_bands.py
```

This is the heavy SOLO verifier in the F2 lane.  On this machine the full
registered sweep completed with bounded memory and wrote the pinned
certificate.
