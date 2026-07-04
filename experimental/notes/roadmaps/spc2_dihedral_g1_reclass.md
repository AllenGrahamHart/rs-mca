# SP-CENSUS-2 coprime-dihedral reclassification

- **DAG node:** `spc2_dihedral_g1_reclass`.
- **Consumer:** `anchored_nontoral_pte_bound`.
- **Status:** exact negative result.
- **Verifier:** `experimental/scripts/verify_spc2_dihedral_g1_reclass.py`.
- **Certificate:**
  `experimental/data/certificates/spc2-dihedral-g1-reclass/spc2_dihedral_g1_reclass.json`.

## Question

SP-CENSUS-2 found an in-range strict-form falsifier:

```text
F_1153 / mu_32,        t = 3,        h = 8,
A_8^nt = 976 > h n = 256.
```

The frozen SP-CENSUS support classifier charges cyclic pullbacks and dihedral
fiber-unions with `gcd(n,m)>1`.  A natural cheap repair is that the 976
survivors might actually be fibers of coprime dihedral maps

```text
X^m + alpha X^-m,        gcd(n,m) = 1,
```

whose fibers are 2-point inversion-pair classes rather than larger cyclic
fibers.

## Test

The verifier re-runs exactly the h=8 cell of the falsifier row and compares:

```text
old classifier:       frozen SP-CENSUS cyclic/dihedral support strip
augmented classifier: old classifier
                      + all coprime dihedral pair-fiber partitions
                        in the same degree window t < m <= floor(log2 n)^2
```

The augmented partitions range over all offsets, matching the SP-CENSUS
offset convention for `X^m + alpha X^-m`.

## Result

The augmented classifier charges no additional pair.

```text
old charged:      249
old non-toral:    976

new charged:      249
new non-toral:    976
```

The old charged pairs are:

```text
cyclic:m=4    105
cyclic:m=6    144
```

The added coprime-dihedral reasons have count zero.

## Interpretation

The `F_1153 / mu_32, h=8` boundary mass is not an artifact of omitting
`gcd(n,m)=1` dihedral pair-fibers from the SP-CENSUS support classifier.

So the remaining 976 survivors require a real explanation:

```text
1. another paid dictionary clause outside coprime dihedral pair-fibers; or
2. acceptance that the strict anchored target A_h^nt <= h n is false at the
   q ~ n^2 boundary, with W4's row-wise n^3 currency absorbing it.
```

This leaves the current terminal target unchanged:

```text
post-strip row-wise primitive residue <= n^3.
```

## Verification

Run:

```bash
python3 experimental/scripts/verify_spc2_dihedral_g1_reclass.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_spc2_dihedral_g1_reclass.py --write-certificate
```

Current replay: **9 PASS, 0 FAIL**.
