# X13-H3: high-q sweep for h=3 active cores

- **DAG node:** `active_core_count_bound`.
- **Status:** exact finite evidence for the high-q vanishing route.
- **Verifier:** `experimental/scripts/verify_x13_h3_q_sweep.py`.
- **Certificate:**
  `experimental/data/certificates/x13-h3-q-sweep/x13_h3_q_sweep.json`.

## Scope

This packet reuses the banked X12 h=3 active-core machinery.  For

```text
n in {32, 64, 128, 256}
alpha in {2, 9/4, 5/2, 11/4, 3},
```

it scans the first prime

```text
p == 1 mod n,        p > floor(n^alpha),
```

and counts anchored h=3 active cores after the same cyclic/dihedral
SP-CENSUS strip used by X12.

The scan is deliberately finite and prime-specific.  It is evidence for the
high-q route, not a monotonicity theorem in `q`.

## Result

The exact non-toral active-core counts are:

```text
row                  p          collision groups   C_3^nt
---------------------------------------------------------
n32, alpha=2         1153       0                  0
n32, alpha=9/4       2593       32                 6
n32, alpha=5/2       5857       0                  0
n32, alpha=11/4      13921      0                  0
n32, alpha=3         32801      0                  0

n64, alpha=2         4289       0                  0
n64, alpha=9/4       11777      0                  0
n64, alpha=5/2       32833      0                  0
n64, alpha=11/4      92737      0                  0
n64, alpha=3         262337     0                  0

n128, alpha=2        17921      384                18
n128, alpha=9/4      55681      0                  0
n128, alpha=5/2      186113     0                  0
n128, alpha=11/4     623617     0                  0
n128, alpha=3        2100097    0                  0

n256, alpha=2        65537      5504               129
n256, alpha=9/4      262657     0                  0
n256, alpha=5/2      1049089    0                  0
n256, alpha=11/4     4201217    0                  0
n256, alpha=3        16777729   0                  0
```

So the two boundary rows with known h=3 mass vanish already by the first
`p > n^(9/4)` prime.  Every checked row vanishes by the first
`p > n^(5/2)` prime.

## Caution

The `n=32` row is intentionally retained because it shows finite-prime
non-monotonicity:

```text
p = 1153  (> n^2):     C_3^nt = 0
p = 2593  (> n^(9/4)): C_3^nt = 6
p = 5857  (> n^(5/2)): C_3^nt = 0
```

Thus the packet does not justify a monotone threshold statement.  It does
support the weaker and more relevant claim that the high-q vanishing route is
visible well below `q = n^3` at the tested sizes.

## Interpretation

Together with the h=3 cubic cap, this narrows the h=3 terminal picture:

```text
1. L3 is proved for h=3: anchored active pairs < n^3.
2. Empirically, the fully stripped h=3 count vanishes by q > n^(5/2)
   through n=256, and by q > n^(9/4) at n=128,256.
```

The remaining terminal work is still `h >= 4` or a proof of high-q vanishing
uniformly in `h`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x13_h3_q_sweep.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x13_h3_q_sweep.py --write-certificate
```

Current replay: **106 PASS, 0 FAIL**.
