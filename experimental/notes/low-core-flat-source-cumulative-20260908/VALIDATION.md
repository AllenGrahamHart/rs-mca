# Publication Replay Record

Executed in the outbound worktree on 2026-09-08. These are deterministic
arithmetic/control replays, not external mathematical review or formal proof.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Full normal Python wrapper | 92/92 PASS | 8.26 seconds | 25196 KiB |
| Eight extension checkers directly under -O | 8/8 PASS | 3.50 seconds | 28288 KiB |

Both runs check all 471 frozen sources, the 44-node acyclic requirement
inventory and six rejected source/inventory mutations: wrong hash, duplicate
file, omitted file, nonlocal path, omitted proof root and cyclic requirement.
The unchanged baseline passes again. Manifest SHA-256:

~~~text
25e4c976416ac303755f7c55945ebe81ffcd21e16630535c5835c8bc7ec6b989
~~~

Parent 4d665ca9's manifest hash is
`22b2a176c8acc23e12441b1d08b7c99a0922616abca22b4d4566e6eb843cc469`.
The exporter checked all 439 frozen parent sources before adding 32 sources
and revising eleven sources from the dirty origin. The other 428
remain byte-identical. There are 1380112 source bytes. The prior validation
is preserved at
[parent 4d665ca9](https://github.com/AllenGrahamHart/rs-mca/blob/4d665ca98510bfe8c8021e24721ec86176f0a3a0/experimental/notes/low-core-flat-source-cumulative-20260908/VALIDATION.md).

## New Checks

- Rank-five actual inside ranks 1..5 check signed coefficient absorption.
  The rank-six zero-calibration sign-discarding boundary remains a
  method warning, not a counterexample to the new calibrated count.
- An actual rank-two flat with singleton fibers, nonconstant scales and
  a retained carrier zero checks the projected-pair child. Four original
  labels give one essential exception, three full-code-bad children at
  agreement m-t and eighteen anchored controls. Strict heaviness and
  overlapping cores are checked separately.
- Two implementations check all 80 analytic 45000-interval profiles;
  160 off-by-one endpoint mutations are rejected. The uniform quadratic
  half-credit and all-J derivative conditions are included.
- Twenty-one exact rank-six Vandermonde controls check calibrated
  tangents and signed inside coupling. Actual full-code-bad witnesses
  omit the flat; complete-core tuple packing retains their original
  labels and defects. The two-cost positive-part branch is checked.
- Rational and independent integer-scaled certificates check all 6400
  source-parameter and 2560 rank-six record-occupancy boxes. All inner
  lower bounds are positive, and 17920 incorrect box floors are rejected.
  Maxima are 264060029243645954 and 231762550270308532 respectively;
  the separate low-density total is 240281411914853457.
- The original-source checker now leaves J=9941..39999, with 30059
  integers, and retains one near allowance and the remaining fiber gate.

## Retained Receiver-Fiber Checks

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
  original near allowance; the updated interval is checked by the assembly.

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
  and now records the residual J=9941..39999. The sole near allowance remains
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
children are run normally. The eight extension checkers also passed
directly with -O using explicit checks,
via `python3 -B -O replay.py --flat-only`. That optional mode
checks the entire source inventory but runs only the eight selected scripts;
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
