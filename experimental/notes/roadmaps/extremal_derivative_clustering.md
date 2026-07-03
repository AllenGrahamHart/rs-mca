# EXTREMAL-MINE: Derivative Clustering of Split-Pair Residues

- **DAG node:** `anchored_nontoral_pte_bound`.
- **Task:** EXTREMAL-MINE.
- **Status:** evidence; the in-range falsifier does not cluster into a few
  derivative classes.
- **Verifier:** `experimental/scripts/verify_extremal_derivative_clustering.py`.
- **Certificate:**
  `experimental/data/certificates/extremal-derivative-clustering/extremal_derivative_clustering.json`.

## Scope

This verifier post-processes the SP-CENSUS and SP-CENSUS-2 certificates.  It
does not enumerate new split pairs.  For every uncharged or anchored non-toral
pair already recorded, it reconstructs the `Q` locator, computes

```text
L_Q', roots of L_Q' in F_p, critical values L_Q(root),
domain-root exponents, and derivative-zero profile.
```

Pairs are clustered by the normalized derivative polynomial `L_Q'`.

## In-Range Rows

```text
row                    pairs   derivative classes   top class share   derivative-zero profile
----------------------------------------------------------------------------------------------
F601 / mu24               32          32               0.0312          0,0: 32
F1201 / mu24              16          16               0.0625          0,0: 16
F1153 / mu32            1236        1228               0.0024          0,0: 1158; 0,1: 39; 1,0: 39
```

The `F_1153 / mu32` falsifier has top derivative class size `3`.  Thus the
in-range excess is not a single shared derivative pencil, nor a small set of
shared derivative classes.

## Low-Q Comparison

```text
row                    pairs   derivative classes   top class share
--------------------------------------------------------------------
F13 / mu12                24          12               0.0833
F17 / mu16               976         832               0.0061
F41 / mu20              5480        5300               0.0004
F97 / mu24             30000       29784               0.0001
```

The low-q explosions are also broad rather than pencil-clustered.  The small
`F13 / mu12` row is the only visibly clustered case, and it is entirely the
minimal-subtrade route.

## Root-Structure Signal

The strongest shared signal is not a common derivative polynomial.  It is the
absence of domain critical points.

For the in-range falsifier:

```text
F1153 / mu32:
  1158 / 1236 pairs have no domain zero in either L_Q' or L_P'.
  510 pairs have L_Q' with no root in F_p.
  447 pairs have exactly one off-domain simple root of L_Q'.
```

For the large low-q row:

```text
F97 / mu24:
  21168 / 30000 pairs have no domain zero in either L_Q' or L_P'.
```

## Interpretation

The derivative-clustering route (route (i)) cannot be a proof by bounding a
small number of shared derivative classes.  The falsifier is a broad primitive
moment/PTE cloud:

```text
1236 pairs, 1228 normalized derivative classes.
```

Any successful replacement must either:

1. identify a toral or paid clause that charges these many distinct derivative
   classes by a different invariant, or
2. use a high-dimensional moment/PTE estimate that allows a constant/exponent
   loss beyond the strict `h n` target.

## Verification

Run:

```bash
python3 experimental/scripts/verify_extremal_derivative_clustering.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_extremal_derivative_clustering.py --write-certificate
```

Current replay: **20 PASS, 0 FAIL**.
