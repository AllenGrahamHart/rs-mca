# P1 Deep-Link Staircase Conditional Certificate

This certificate pins the P1 conditional proof packet for DAG node
`deep_link_staircase`.

Run:

```bash
python3 experimental/scripts/verify_p1_deep_link_staircase_conditional.py
```

The verifier checks:

- the exact embedding of a fixed `(k-1)`-subcore link into rich points of an
  affine line arrangement in parameters `(z,a)`;
- an explicit RS toy fixture showing that the raw per-subcore constant cap is
  false for arbitrary received pairs before post-paid stripping;
- the conditional counting arithmetic once the post-paid per-subcore cap and
  occupied-subcore accounting are supplied.
