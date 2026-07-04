# E30 Dimension-3 Flat Census Certificate

This certificate records the deterministic family fingerprints for the E30
dimension-3 flat census under the enlarged taxonomy.

Run:

```bash
python3 experimental/scripts/verify_e30_dim3_flats.py
```

The verifier recomputes every registered family from fixed seeds, checks each
count/class histogram/fingerprint against the embedded `EXPECTED` table, and
then verifies that the JSON certificate matches the recomputed family summary.
