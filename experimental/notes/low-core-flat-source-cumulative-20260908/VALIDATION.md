# Publication Replay Record

Executed in the outbound worktree on 2026-09-08. These are deterministic
arithmetic/control replays, not external mathematical review or formal proof.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Normal Python wrapper | 82/82 PASS | 4.81 seconds | 18636 KiB |
| Optimized Python wrapper | 82/82 PASS | 4.87 seconds | 22112 KiB |
| Five extension checkers directly under -O | 5/5 PASS | 0.79 seconds | 21492 KiB |

Both full runs check all 424 frozen sources, the 38-node acyclic requirement
inventory and six rejected source/inventory mutations: wrong hash, duplicate
file, omitted file, nonlocal path, omitted proof root and cyclic requirement.
The unchanged baseline passes again. Manifest SHA-256:

~~~text
6f70eb2a437c17eeb06b34c04eedbcc01b2e4919ebe8ac5c683a7db9d35fb521
~~~

Parent 6562b807's manifest hash is
`97262ebcafd696b331152effec6491826a70d6c7adef861967f22acd2d7a349d`.
The 401 unchanged parent sources, 18 additions and five revised assembly
sources were checked against that Git parent and the dirty origin snapshot.
There are 1252293 source bytes. The prior validation is preserved at
[parent 6562b807](https://github.com/AllenGrahamHart/rs-mca/blob/6562b80720397fbc5f0815d53715c72c15c8f6f5/experimental/notes/low-core-flat-source-cumulative-20260908/VALIDATION.md).

## New Checks

- Four actual polynomial carriers check the full-fiber locator division,
  actual rank and degree, preserved gap and exact ordered-basis recurrence.
  Repeated fibers expose the error in dividing only the selected point.
- The independent generic audit checks 357 partition inequalities,
  72 derivative identities and 22 tight controls. These are controls of
  the universal proof, not a claim of field realizability for every partition.
- Normalized rational coefficients and independent unnormalized polynomial
  composition check eight fixed quadratic steps and their global remainder
  identities. Eight upward mutations and two incorrect LOW floors fail.
- Two exact method-boundary quotients exceed the budget. They limit
  uniform per-record pricing, not the desired MCA inequality.
- The revised original-source checker rejects six interval/budget mutations
  and records the residual J=9941..52999. The sole near allowance remains
  134944 and whole-source alternatives combine by maximum.

## Retained Supplier Checks

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
extension checkers also passed directly with -O using explicit checks,
via `python3 -B -O replay.py --contraction-only`. That optional mode
checks the entire source inventory but runs only the five extension scripts;
it is not reported as a full supplier replay.

Each run was enclosed in RAMguard tiny: 256 MiB RAM, 64 MiB swap and
60 seconds. A timeout is INCOMPLETE, not a successful proof. Measured
peak RSS is not a worst-case guarantee. No local fanout, large matrix,
CAS, TeX/Lean build, field-scale enumeration, installation, Modal job or
compute spending was used.

The universal basis inequality, analytic completeness, support transport
and inherited supplier proofs require human review. Hashes establish
source identity only. No globally clean local DAG, active-v4 row value,
unrestricted adjacent endpoint or completed Prize problem is claimed.
