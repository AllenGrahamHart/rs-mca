# Dependency subgraph

```text
elementary duality + polynomial interpolation/root bound
  -> mca_polynomial_core_gluing [PROVED, no req inputs]
       -> mca_received_pair_zero_defect_payment [existing consumer]
       --evidence--> rate_half_band_crossing_location
       --evidence--> xr_band_fullrank_window_divisor_count
       --evidence--> xr_band_remaining_selected_charge
```

The last two evidence edges carry the proved high-band zero-or-two
dichotomy and its single-pair payment. Neither edge is a proof of the
consumer's remaining population count. The consumers remain red leaves;
no new conditional node or requirement is added.
