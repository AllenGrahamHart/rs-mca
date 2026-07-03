# W2 Graded Tangent Ledger Certificate

This certificate pins the arithmetic/design verifier for the W2 graded tangent
ledger packet.

Run:

```bash
python3 experimental/scripts/verify_w2_graded_tangent_ledger.py
```

The verifier checks the depth/exchange identities for the 2b partial band and
the heavy-triangle boundary routing into either a direct 2b tangent edge or the
`deep_link_staircase` population bound.
