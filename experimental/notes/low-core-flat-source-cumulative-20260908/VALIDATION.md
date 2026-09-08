# Publication Replay Record

Executed in the outbound snapshot on 2026-09-08, before publication.
No external independent mathematical review or formal certification is claimed.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Python normal wrapper | 60/60 PASS | 3.64 seconds | 16512 KiB |
| Python optimized wrapper | 60/60 PASS | 3.75 seconds | 21028 KiB |
| Five new checkers, each directly under -O | 5/5 PASS | individually subsecond | not separately measured |

Both full runs verify 231 frozen sources, 715349 bytes of source content.
The export checked all 212 inherited hashes against the previous immutable
companion and copied those files unchanged, then added 19 new source files.
Four malformed manifest variants are rejected: changed hash, duplicate
file, omitted file and nonlocal path. The unchanged baseline passes again.

The wrapper runs children serially with a 15-second timeout per child,
clears PYTHONOPTIMIZE and disables bytecode writes. Older children can use
assertions; the optimized wrapper deliberately leaves them unoptimized.
Separately, all five new checkers were executed directly with Python -O;
their explicit checks remain active. A failed check exits nonzero, and a
child timeout is reported as INCOMPLETE rather than mathematical success.

Each execution was enclosed in RAMguard tiny: 256 MiB RAM, 64 MiB swap,
60 seconds. The measured numbers above are not worst-case guarantees.
No local fanout, field-sized enumeration, CAS, TeX/Lean build, package
installation, Modal job or compute spending was needed.

## Mathematical Controls

- Gaussian-rank and determinant implementations independently count small
  core/defect tuple families, including distinct-slope disjointness.
- A rank-two flat defeats the fiber-only substitution. An F_11 non-arc
  example satisfies the weaker occupied-subspace condition and has 792
  tuples, exceeding its valid positive lower count 420.
- Carrier zeros, repeated fibers and rational infinity are retained.
- Rational floors and independent integer cross products check the two
  whole-source bounds, reserves and analytic derivative certificates.
- Independent raw-margin sums and monomial counts check the 9940
  extension. Endpoint certificates support the all-multiplicity boundary;
  convexity and large-multiplicity monotonicity remain hand proofs.

These tests check arithmetic and small controls, not the universal proof
or exhaustive original-source transport. Passing hashes is source identity,
not an assumption that the mathematics is correct. Both prizes remain open.
