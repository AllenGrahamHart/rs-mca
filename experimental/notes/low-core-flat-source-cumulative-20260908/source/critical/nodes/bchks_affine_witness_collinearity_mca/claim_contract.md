# Claim contract

The code consists of degree-<k polynomials, not degree-<=k. The density
used in the interpolation bounds is (k-1)/n, not k/n. The original
finite field supplies all slopes, and normalization is by its size.

Every bad slope has a chosen support and scalar polynomial. Noncontainment
is on that same support; choosing a nearby pair globally is not enough
to remove the slope. The proof retains those chosen witnesses through
Hensel specialization and only then uses the fixed-line cancellation
lemma. Witnesses with more than a agreements remain included.

Only k>=2, k<n and the printed integer agreement gate are assumed.
The gate uses 2m+1, not 2m+2. Multiplicity m is a positive integer.
For m=1, Z is the maximum of Y and t^2*n/(3d); dropping that
maximum is permitted only if 4d<=n. The new companion verifies
the independent collinearity load condition at m=1 and m=2.
Small fields are handled by the trivial numerator <=|F| branch.
Small characteristic is handled with the weighted Frobenius degrees in
proof.md, not by an implicit separability assumption.

The conclusion is an upper bound, not a matching extremal construction,
a maximal-safe formula, or a proof of the exact BCHKS Theorem 4.6
constant. Curve samplers of degree M>1 are outside scope.

An independent reviewer should attack the preserved-witness step, the
Appendix C numerator weights, and the integer lifting length first.
Numerical survival is neither needed nor sufficient for this theorem.
