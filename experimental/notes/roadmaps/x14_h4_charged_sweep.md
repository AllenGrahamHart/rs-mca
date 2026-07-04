# X14-H4: charged sweep for the first campaign trade size

- **DAG node:** `active_core_count_bound`.
- **Status:** exact finite evidence; post-strip residue is zero in all checked
  h=4 rows.
- **Verifier:** `experimental/scripts/verify_x14_h4_charged_sweep.py`.
- **Certificate:**
  `experimental/data/certificates/x14-h4-charged-sweep/x14_h4_charged_sweep.json`.

## Scope

The campaign's smallest actual trade size is `h=t+1`.  For the clean
`t=3` lane this is `h=4`, so X14 scans the first real terminal size rather
than another h=3 base-case row.

For

```text
n in {32, 64, 128}
alpha in {2, 9/4, 5/2, 3},
```

the verifier scans the first prime

```text
p == 1 mod n,        p > floor(n^alpha),
```

and enumerates anchored h=4 split pairs

```text
1 in P,      P cap Q = empty,      |P| = |Q| = 4,
e_i(P) = e_i(Q),      i = 1,2,3.
```

The charged classifier is the same cyclic/dihedral SP-CENSUS strip used by the
terminal-node censuses.

## Result

Every checked active h=4 partner is charged by a cyclic pullback partition.
The post-cyclic/dihedral non-toral residue is zero in every checked row.

```text
row                  p          collision groups   active pairs   charged   non-toral
------------------------------------------------------------------------------------
n32, alpha=2         1153       1                  7              7         0
n32, alpha=9/4       2593       1                  7              7         0
n32, alpha=5/2       5857       1                  7              7         0
n32, alpha=3         32801      1                  7              7         0

n64, alpha=2         4289       1                  15             15        0
n64, alpha=9/4       11777      1                  15             15        0
n64, alpha=5/2       32833      1                  15             15        0
n64, alpha=3         262337     1                  15             15        0

n128, alpha=2        17921      193                43             43        0
n128, alpha=9/4      55681      1                  31             31        0
n128, alpha=5/2      186113     1                  31             31        0
n128, alpha=3        2100097    1                  31             31        0
```

The nontrivial row is `n=128, alpha=2`: it has 193 signature-collision
groups before anchoring, but the anchored active partners are all paid:

```text
cyclic:m=4  -> 31 pairs
cyclic:m=6  -> 12 pairs
```

At higher q in the same n=128 row, only the persistent `cyclic:m=4` family
remains.

The `cyclic:m=4` family is the full-fiber case of
`cyclic_fiber_collision_lemma.md`.  The `cyclic:m=6` boundary family is
explained by `cyclic_pullback_trade_lift.md`: here `gcd(128,6)=2`, so h=4
supports are unions of two 2-point cyclic fibers, and same-top-three equality
upstairs is the lift of same-top-one equality on the quotient `mu_64`.

## Interpretation

This is not a proof that h=4 is uniformly empty after the strip, and it does
not touch h >= 5.  It is nevertheless stronger than the previous h=3-only
evidence because it tests the first campaign trade size directly.

The observed shape is:

```text
raw h=4 active partners exist,
but they are already cyclic pullback-paid.
```

So the next proof attempt for h=4 should start with a classification lemma:
same-top-three 4-trades in 2-power rows appear to be forced into cyclic
pullback cells, at least in the tested high-q regime.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x14_h4_charged_sweep.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x14_h4_charged_sweep.py --write-certificate
```

Current replay: **90 PASS, 0 FAIL**.
