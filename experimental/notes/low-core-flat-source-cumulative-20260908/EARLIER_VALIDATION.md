# Publication Replay Record

Historical replay at ef8e3316; see [VALIDATION.md](VALIDATION.md) for the extension.

Executed in the outbound snapshot on 2026-09-08, before publication.
No external independent mathematical review or formal certification is claimed.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Python normal wrapper | 62/62 PASS | 3.58 seconds | 17024 KiB |
| Python optimized wrapper | 62/62 PASS | 3.74 seconds | 21000 KiB |
| Seven new or updated checkers, each directly under -O | 7/7 PASS | 0.62 seconds total | 16636 KiB |

Both full runs verify 241 frozen sources, 745081 bytes of source content.
Against immutable parent 1a87f28f, 224 source hashes are unchanged, seven
sources are revised for real h, and ten large-fiber sources are added.
Only these explicitly selected sources were copied from the local worktree;
the unbanked maximum-density argument and generated DAG were excluded.
The parent manifest SHA-256 is
`2e308de51f9638b64293d6e71358e04f7505e3428e129c87df7d846996e2ddeb`.
The current manifest SHA-256 is
`c57bd6ce8d182c463496943efce5eee333cf314afb169162a806eda7ae861d51`.
Four malformed manifest variants are rejected: changed hash, duplicate
file, omitted file and nonlocal path. The unchanged baseline passes again.

The wrapper runs children serially with a 15-second timeout per child,
clears PYTHONOPTIMIZE and disables bytecode writes. Older children can use
assertions; the optimized wrapper deliberately leaves them unoptimized.
Separately, all seven new or updated checkers ran directly with Python -O;
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
  tuples, exceeding the integer-h lower count 420 and real-h count 616.
- Carrier zeros, repeated fibers and rational infinity are retained.
- Rational floors and independent integer cross products check the two
  whole-source bounds, reserves and analytic derivative certificates.
- Independent raw-margin sums and monomial counts check the 9940
  extension. Endpoint certificates support the all-multiplicity boundary;
  convexity and large-multiplicity monotonicity remain hand proofs.
- Saturated and nonsaturated fiber examples have 240 and 432 completed
  tuples. The nonsaturated quotient has 16 ordered bases, refuting the
  unsupported zero-excess count 20 while exceeding the valid count 15.
- A nonuniversal carrier-zero defect is retained. Dropping the g=0
  hypothesis produces an invalid lower bound in a separate control.
- All 645 small endpoint controls pass. Two implementations check eight
  large-fiber finite floors, rejecting every off-by-one mutation, along
  with exact derivative certificates, the HIGH floor and original budget.

These tests check arithmetic and small controls, not the universal proof
or exhaustive original-source transport. Passing hashes is source identity,
not an assumption that the mathematics is correct. Both prizes remain open.
