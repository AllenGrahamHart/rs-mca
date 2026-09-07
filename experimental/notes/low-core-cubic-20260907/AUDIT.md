# Audit scope and review guards

The analytic proofs were read again before export. The arithmetic replay
and controls supplement that hand audit; they do not formally establish
the geometry. Independent external hand review remains due.

## Mathematical guards

1. Generic jet conditions concern auxiliary constant-field points, not a
   generic Reed--Solomon domain. The characteristic hypothesis p>=K
   applies to the output polynomial carrier and has a small-characteristic
   counterfamily. Actual nonlinear image degrees are not discarded.
2. For moving projections, the same d=dim ker(A,B) controls both dimension
   and coefficient cost. The scalar input has degree <K+h, not <K; its
   receiver is defined on all original coordinates. No denominator pole
   is removed from the source's agreement count.
3. Smooth cubic dimension uses an actual family of elliptic sections
   before taking tangents. Constant elliptic products are treated
   separately from surfaces with singular fibers. Original pair-coordinate
   degree, rather than a transformed Weierstrass degree, prices the locus.
4. The normalization unit and its reciprocal both satisfy monic equations.
   Both valuation directions are bounded. Exceptional pairs and all
   divisor classes remain in the algebraic degree cover.
5. The kernel is the entire weighted interpolation kernel. Primitive
   division and dimension bound its gcd; no single guessed relation is
   promoted to exhaustive coverage. Strict weighted degree is essential.
6. The constant-line Johnson split uses different on-line/off-line
   agreements. The resource and original near allowance are added once,
   after assigning each pair with all its labels to one group.
7. One point on the projective boundary and one point on its normalization
   are different conditions. The singularity-at-infinity test retains that
   distinction. The affine singular pair may have no rational preimage
   on the normalization and is explicitly counted as one extra exception.
8. Neither nodal nor cuspidal one-boundary families inherit a dimension-one
   conclusion. The remaining normal-form parameter can have poles. Its
   payment, higher source ranks and both prizes remain open.

## Exact checks

Both exported replays passed on 2026-09-07 under a 256 MiB RAMguard
ceiling. The normal run took 9.15 seconds with maximum RSS 16512 KiB;
the optimized-wrapper run took 8.08 seconds with maximum RSS 20708 KiB.
These are measured local resource figures, not forecasts for every host.

The packet has 111 frozen source files and 31 serial checks, including
the earlier conic/strip regressions. Independent arithmetic implementations
recompute the cubic weighted ceiling using a common integer denominator,
the kernel dimensions by individual monomials, and the moving-projection
maxima by dimension blocks. Controls reject the next insufficient kernel
endpoint, reduced Johnson caps, the next projection-height recipe bound,
and inappropriate smoothness or degree assumptions.

The wrapper checks the exact source inventory and SHA-256 hashes. It
starts assertion-enabled children in both normal and optimized-wrapper
modes, with a 15-second timeout and immediate partial PASS output after
each completed check. It needs only the Python standard library.

No formal proof, full-upstream build, external approval, exhaustive field
enumeration, or repaired global DAG/crosswalk is claimed by this replay.
The original conic export is unchanged and remains independently replayable.

## Compute requests

None. All checks are bounded, serial and local; no Modal use or expenditure.
