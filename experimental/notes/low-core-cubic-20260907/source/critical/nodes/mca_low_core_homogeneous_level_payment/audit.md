# Audit and provenance

Primary standard inputs checked on 2026-09-07:

- A finite extension of k(X) is the function field of a normal
  projective curve: [Stacks, Theorem 53.2.6](https://stacks.math.columbia.edu/tag/0BY1).
- A proper integral curve over algebraically closed k has only constant
  global regular functions: [Stacks, Lemma 33.9.3](https://stacks.math.columbia.edu/tag/0366).
  A divisor-zero rational function and its reciprocal are regular on
  the normal curve, so their ratio conclusion follows directly.

No result about the number of rational points, S-unit solutions,
Mordell bounds, a varying splitting field, or asymptotic estimates is
imported. Pole bounds and the product identity prove finite divisor
patterns directly. The numerical count then uses the algebraic degree
cover, not a count of those patterns.

Hand audit checks the fixed finite-dimensional function spaces, upper
AND lower order bounds, irreducibility against a finite union of
closed lines, affine-linear recovery from two scalars, and the nonzero
degree-e part of the remaining level equation. The affine factors need
not concur, and a constant-term argument is not substituted for that
top-degree check. These avoid confusing
projective classes with individual functions or injecting an inseparable
point map without a dimension argument.

The JOINT LIST induction uses one proper component hyperplane whenever
joint agreement is not universal. The degree charge is e^(2s-1),
not a graph's smaller e^(s-r). Gain accounting uses cumulative RAW
weights before telescoping and retains other pairs' core coordinates.

Exact small controls cover the actual canonical hyperbola source and
both missing-hypothesis dimension failures. Universal geometry and the
exclusion from degree-two-through-seven rational-X graphs are hand
proofs. Independent finite arithmetic is owned by the consumer.
External independent hand review remains outstanding.

Final small-control replay, including the nonconcurrent affine and
parallel-distinct-factor guards: 0.07 seconds, 16640 KiB, under
ramguard tiny. Primary and independent finite replays are recorded in
the consumer and cycle record. No large computation is a premise.
