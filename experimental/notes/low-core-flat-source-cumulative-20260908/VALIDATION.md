# Publication Replay Record

Executed in the outbound worktree on 2026-09-08. These are deterministic
arithmetic/control replays, not external mathematical review or formal proof.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Normal Python wrapper | 78/78 PASS | 4.69 seconds | 17352 KiB |
| Optimized Python wrapper | 78/78 PASS | 4.57 seconds | 20696 KiB |
| Five new checkers directly under -O | 5/5 PASS | 0.49 seconds | 16320 KiB |

Both full runs check all 406 frozen sources, the 36-node acyclic requirement
inventory and six rejected source/inventory mutations: wrong hash, duplicate
file, omitted file, nonlocal path, omitted proof root and cyclic requirement.
The unchanged baseline passes again. Manifest SHA-256:

~~~text
97262ebcafd696b331152effec6491826a70d6c7adef861967f22acd2d7a349d
~~~

Parent ef8e3316's manifest hash is
`c57bd6ce8d182c463496943efce5eee333cf314afb169162a806eda7ae861d51`.
All 241 inherited source files are retained unchanged. There are 165
additions, 469104 new bytes, and 1214185 total source bytes. The parent
record remains in [EARLIER_VALIDATION.md](EARLIER_VALIDATION.md).

## New Checks

- Independent Gaussian and Bareiss tuple censuses, with actual polynomial
  carriers, check the exact inside-extension identities and disjoint
  incidence tuples. Three controls have inside rank smaller than the flat.
- Fraction products and scaled-integer products independently check all
  91 finite endpoints, exact curvature/derivative inequalities, resource
  ceilings and field reserve. All 91 off-by-one floor mutations fail.
- The original-source interval checker validates the exhaustive g partition,
  child intervals, maximum of whole-source bounds and one near add-back.
  Six endpoint/budget mutations fail.
- The F_23 transport control has 22 labels and three carrier zeros but
  only two universal-core points; all labels and actual rank are retained.
- The F_17 support control checks saturated bad supports and the warning
  that unrestricted reselection can change the old raw margin.
- Earlier core-extreme, padded-Johnson and scalar-descent controls replay
  as explicit prerequisites. Their older optional regression scans are
  not substituted for the hand-proved padding and endpoint arguments.

## Resource And Assurance Limits

The wrapper runs children serially, with a 15-second timeout per child,
bytecode disabled and PYTHONOPTIMIZE cleared. Older assertion-based
children remain unoptimized even in the optimized-wrapper run. The five
new checkers also passed directly with -O using explicit checks.

Each run was enclosed in RAMguard tiny: 256 MiB RAM, 64 MiB swap and
60 seconds. A timeout is INCOMPLETE, not a successful proof. Measured
peak RSS is not a worst-case guarantee. No local fanout, large matrix,
CAS, TeX/Lean build, field-scale enumeration, installation, Modal job or
compute spending was used.

The universal basis inequality, analytic completeness, support transport
and inherited supplier proofs require human review. Hashes establish
source identity only. No globally clean local DAG, active-v4 row value,
unrestricted adjacent endpoint or completed Prize problem is claimed.
