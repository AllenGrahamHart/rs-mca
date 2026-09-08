# Dependency sub-DAG

```text
BCHKS Lemma 3.1 [published] ------------------+
BCIKS Section 5 and Appendices A/C [published]+-->
fixed-codeword-line cancellation [proof.md] -+
          bchks_affine_witness_collinearity_mca [PROVED]
                              |
                   prize_full_threshold_brackets [PROVED]
                              |
                          mca_grand
```

The leaf's proof contains the subset transport, all-field weighting,
rounding, content exception ledger and final cancellation argument.
Published lemmas are its external sources, not unresolved DAG premises.
It has no local req ancestor and no edge to a grand-prize descendant.
The consuming bracket node owns the incoming req edge.

No old (Q)/(A)/SPI red is promoted. No speculative child is created.
Generated graph replay is deferred under the user's no-scripts restriction.
