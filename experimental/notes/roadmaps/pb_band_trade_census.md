# P-B: band-trade census

- **DAG node:** `u1_beta_band_trade_reduction`.
- **Task:** P-B.
- **Status:** EVIDENCE / CENSUS PASS.  No toy family avoids all three
  registered exits.
- **Verifier:** `experimental/scripts/verify_pb_band_trade_census.py`.
- **Certificate:**
  `experimental/data/certificates/pb-band-trade-census/pb_band_trade_census.json`.

## Scope

The verifier extends the H1 toy harness from minimal star trades to canonical
band trades.  For each H1 row it enumerates disjoint equal-size pairs

```text
|P| = |Q| = h,
t + 1 < h <= min(floor(log2 n)^2, floor(n/2)),
e_i(P) = e_i(Q), 1 <= i <= t.
```

Equivalently, these are the trades with

```text
deg(L_P - L_Q) <= h - t - 1.
```

The implementation is low-memory: same-signature subsets are sorted in compact
`uint32` arrays and processed one signature group at a time.  The full run
completed with peak RSS about `149 MB`.

## Exit Classifier

Every canonical dihedral-orbit representative is routed through the three
exits in `u1_beta_band_trade_reduction`:

```text
exit 1: contains a minimal size-(t+1) subtrade after bounded-tail deletion;
exit 2: v1 pullback/dihedral charged by the frozen W3 dictionary;
exit 3: primitive moment/PTE residual, handed to the U2 certifier lane.
```

Exit 3 is intentionally not hidden.  It is a classified hand-off to the
moment/PTE column, not a proof that official rows are empty.

## Results

Across all H1 rows:

```text
canonical band-trade orbits: 1016
exit 1 minimal subtrade:       15
exit 2 v1 pullback:            79
exit 3 primitive moment/PTE:  922
unclassified:                  0
```

Rows with nonzero mass:

```text
F13_mu12_A5_t3:   1 orbit, all exit 2
F13_mu12_A6_t3:   1 orbit, all exit 2
F17_mu16_A6_t3:  28 orbits, 4 exit 2, 24 exit 3
F17_mu16_A8_t3:  28 orbits, 4 exit 2, 24 exit 3
F97_mu16_A8_t3:   2 orbits, all exit 2
F41_mu20_A8_t3: 146 orbits, 4 exit 1, 14 exit 2, 128 exit 3
F41_mu20_A10_t3: same as F41_mu20_A8_t3
F97_mu24_A8_t3: 664 orbits, 7 exit 1, 39 exit 2, 618 exit 3
```

The largest same-signature group size observed is `24`, at `F97_mu24_A8_t3`.

## Interpretation

The three-exit reduction survives the toy census: no canonical band trade
avoids the registered exits.

The dominant exit is primitive moment/PTE.  This confirms that P-B is mostly a
routing statement, while quantitative closure depends on U2-A/U2-B and the
moment/PTE grammar budget.

One small warning is recorded.  In `F97_mu24_A8_t3`, two exit-3 residuals have
`h > 2t+4` (namely beyond the older F2 empirical cap `b <= 10` for `t=3`).
They are not P-B falsifiers, but they say the U2 window split should cover the
full frozen grammar window used here, not only the old F2-EXT toy band.

## Verification

Run:

```bash
python3 experimental/scripts/verify_pb_band_trade_census.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_pb_band_trade_census.py --write-certificate
```
