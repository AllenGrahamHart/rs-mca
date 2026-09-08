# Publication Replay Record

Executed in the outbound worktree on 2026-09-08. These are deterministic
arithmetic/control replays, not external mathematical review or formal proof.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Normal Python wrapper | 85/85 PASS | 4.73 seconds | 18560 KiB |
| Optimized Python wrapper | 85/85 PASS | 4.90 seconds | 22224 KiB |
| Four receiver checkers, normal | 4/4 PASS | 0.37 seconds | 18604 KiB |
| Four receiver checkers directly under -O | 4/4 PASS | 0.64 seconds | 21968 KiB |

Both full runs check all 439 frozen sources, the 40-node acyclic requirement
inventory and six rejected source/inventory mutations: wrong hash, duplicate
file, omitted file, nonlocal path, omitted proof root and cyclic requirement.
The unchanged baseline passes again. Manifest SHA-256:

~~~text
22b2a176c8acc23e12441b1d08b7c99a0922616abca22b4d4566e6eb843cc469
~~~

Parent 47d527e5's manifest hash is
`6f70eb2a437c17eeb06b34c04eedbcc01b2e4919ebe8ac5c683a7db9d35fb521`.
The exporter checked all 424 frozen parent sources before adding 15 sources
and revising seven assembly sources from the dirty origin. The other 417
remain byte-identical. There are 1291442 source bytes. The prior validation
is preserved at
[parent 47d527e5](https://github.com/AllenGrahamHart/rs-mca/blob/47d527e5f0ffce97bec470d36e5aabffea0558d7/experimental/notes/low-core-flat-source-cumulative-20260908/VALIDATION.md).

## New Checks

- Two tiny actual polynomial sources check receiver colors, complete
  versus selected cores, exact scalar-agreement sets and full-code
  badness before/after transport. The exception charge is necessary in
  one control; the other retains nonconstant scales, two heavy colors
  and a nonuniversal carrier zero. Equality is not counted as heavy.
- Independent rational and scaled-integer arithmetic checks the
  degree-2000 Johnson ceiling, four LOW floors, two HIGH floors,
  interval derivative gates and disjoint heavy/light composition.
  Eight off-by-one LOW-floor mutations are rejected.
- The assembly checker keeps its six interval/budget mutations and
  adds eleven receiver-fiber gate boundary controls. It retains the
  same original numerical residual and one near allowance.

## Retained Contraction Checks

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
children remain unoptimized even in the optimized-wrapper run. The four
receiver-fiber checkers also passed directly with -O using explicit checks,
via `python3 -B -O replay.py --receiver-only`. That optional mode
checks the entire source inventory but runs only the four selected scripts;
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
