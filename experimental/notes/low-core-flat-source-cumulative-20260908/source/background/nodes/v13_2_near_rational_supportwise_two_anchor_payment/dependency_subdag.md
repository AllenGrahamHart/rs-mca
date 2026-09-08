# Dependency sub-DAG

```text
v13_2_near_rational_pair_proximity [PROVED]
    |
    v
v13_2_near_rational_supportwise_two_anchor_payment [PROVED]
    | ev                 | ev
    v                    v
mca_safe [CONDITIONAL]   rate_half_band_crossing_location [TARGET]
```

The new node adds the same-witness root-counting and coordinate-ratio
injection missing from pair proximity. Both outgoing edges are evidence
only: the `2w` local charge does not supply the complementary owner ledger or
an adjacent crossing.
