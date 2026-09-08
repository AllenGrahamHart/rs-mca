# Current required proof

The original KoalaBear application now additionally requires
`mca_padded_johnson_scalar_descent`: it supplies V_10 in the original
field, with a proved padding gate and explicit common-zero exceptions.
That supplier requires scalar descent, the weighted-line base, and the
rounded Johnson theorem. It does not depend on this consumer.
The field-independent U_s proof below remains valid separately.

```text
mca_uniform_rank_one_weighted_line_cap ------------+
                                                  |
mca_scalar_agreement_dimension_descent ------------+--req--> this node
                                                  |
v13_2_near_rational_supportwise_two_anchor_payment -+
```

The actual-error-rank gauge is proved inside proof.md. The raw-low
recurrence and heavy-core shortening nodes are no longer required by
this proof. They remain sound suppliers for other work, and support the
separate historical raw_low_alternative.md. No unproved rank cap or
optimized scan is a hidden dependency of the current theorem.
