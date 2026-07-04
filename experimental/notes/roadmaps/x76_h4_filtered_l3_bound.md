# X76: h=4 filtered-triple L3 bound

- **DAG node:** `x76_h4_filtered_l3_bound`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=4 row-count consequence.
- **Verifier:** `experimental/scripts/verify_x76_h4_filtered_l3_bound.py`.
- **Certificate:**
  `experimental/data/certificates/x76-h4-filtered-l3-bound/x76_h4_filtered_l3_bound.json`.

## Statement

The primitive h=4 filtered linear-triple mass satisfies

```text
F_prim(n,p) < n^3
```

for every relevant 2-power row `n`.

More explicitly,

```text
F_prim(n,p) <= 8 n(n-1) < n^3        for n >= 8.
```

## Proof

X65 proves the exact currency conversion:

```text
F_prim(n,p) = 8 O_prim(n,p),
```

where `O_prim` is the primitive h=4 canonical row-orbit count after quotient
content has been stripped.

X75 proves

```text
O_prim(n,p) <= n(n-1).
```

Therefore

```text
F_prim(n,p) <= 8 n(n-1).
```

Disjoint h=4 supports require `n >= 8`.  For every such 2-power row,

```text
8 n(n-1) < n^3,
```

with equality still avoided at the first possible row `n=8` because
`8*8*7 = 448 < 512`.

Thus the h=4 primitive finite-p branch fits the rewired L3 `n^3` row-count
column after translating out of canonical-orbit currency.

## Replay

The verifier cross-checks the X65 and X75 certificates:

```text
row                  primitive triples   uniform bound   n^3
----------------------------------------------------------------
low_n16_p17          160                 1920            4096
low_n64_p193         1072                32256           262144
boundary_n64_p7937   184                 32256           262144
boundary_n128_p17921 96                  130048          2097152
boundary_n256_p91393 176                 522240          16777216
```

The uniform row-count bound is now in the same filtered-triple currency as
X60/X65, not merely in canonical-orbit currency.

## Consequence

X75 already gives the stronger conceptual statement in orbit currency.  X76
records the compiler-facing h=4 primitive row-count consequence:

```text
h=4 primitive filtered finite-p mass < n^3.
```

This still does not close `active_core_count_bound`; larger trade sizes and
the full split-pair assembly remain open.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x76_h4_filtered_l3_bound.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x76_h4_filtered_l3_bound.py --write-certificate
```
