# T-TOY Toral Classification Scan Certificate

This certificate records the exact bidegree-`(1,1)` toral/affine sanity scan
for DAG node `u1_tame_toral_fiberproduct_classification`.

Run:

```bash
python3 experimental/scripts/verify_ttoy_toral_classification_scan.py
```

The verifier checks tame toy rows with `deg psi in (t,20]`, rules out
translation and inverse-toral polynomial factors in that range, and confirms
that every affine line-factor case is a power-pullback normal form after
linear conjugacy.
