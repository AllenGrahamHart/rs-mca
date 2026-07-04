# U2C-PRIME Boundary Fiber-Test Certificate

This certificate records the exact toy boundary test for DAG node
`u2c_boundary_scale_column`.

Run:

```bash
python3 experimental/scripts/verify_u2c_prime_boundary_fiber_test.py
```

The verifier enumerates the X-8 antipodal-free quotient zero-sum patterns,
lifts them to `mu_n`, and checks that the old `M > t` classifier rejects them
while the repaired `M >= t` classifier charges them at the boundary scale.
