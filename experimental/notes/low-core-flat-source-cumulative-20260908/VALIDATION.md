# Publication Replay Record

Executed in the outbound worktree on 2026-09-08. These are deterministic
arithmetic/control replays, not external mathematical review or formal proof.

| Replay | Result | Wall Time | Peak RSS |
| --- | --- | ---: | ---: |
| Full normal Python wrapper | 95/95 PASS | 51.83 seconds | 25192 KiB |
| Quotient-only block 32000, four children under -O | 4/4 PASS | 10.95 seconds | 23884 KiB |
| Quotient-only block 34000, four children under -O | 4/4 PASS | 11.08 seconds | 24132 KiB |
| Quotient-only block 36000, four children under -O | 4/4 PASS | 11.42 seconds | 24136 KiB |
| Quotient-only block 38000, four children under -O | 4/4 PASS | 11.25 seconds | 24140 KiB |

Every run checks all 486 frozen sources, the 46-node acyclic requirement
inventory and six rejected source/inventory mutations: wrong hash, duplicate
file, omitted file, nonlocal path, omitted proof root and cyclic requirement.
The unchanged baseline passes again. Manifest SHA-256:

~~~text
014161c90c8701a893c036bc8c0ff8e183c53547fa51c5404ede9ae73fcc883e
~~~

Parent a16bd73b's manifest hash is
`25e4c976416ac303755f7c55945ebe81ffcd21e16630535c5835c8bc7ec6b989`.
The exporter checked all 471 frozen parent sources before adding 15 sources
and revising seven assembly sources from the dirty origin. The other 464
remain byte-identical. There are 1428674 source bytes. The prior validation
is preserved at
[parent a16bd73b](https://github.com/AllenGrahamHart/rs-mca/blob/a16bd73bf3705eb5d84c9bc3b5e7e1dbf8814434/experimental/notes/low-core-flat-source-cumulative-20260908/VALIDATION.md).

## New Checks

- Nine actual small polynomial configurations check maximum density,
  quotient rank, exact basis classes and inside-extension identities.
  Forty-five tangents and a wrong-sign shortcut control pass.
- Primary and independent integer implementations cover all 112640
  record-cost boxes and 14080 source boxes. They use different coordinate
  scales, derivative formulas and polynomial composition, importing
  neither implementation from the other. All four streaming digests
  match the frozen certificates; 28160 adjacent wrong floors are rejected.
- Uniform quotient-degree and gap gates, downward rounding, tangent
  remainders and endpoint shifts are checked exactly. The separately
  paid rank-one fiber class is included in the final maximum, not in
  each later block's smaller reported maximum.
- The original-source assembly now leaves J=9941..31999, with 22059
  integers. Its six mutations and eleven fiber-boundary controls pass
  normally and under -O; the original near allowance remains unique.

## Retained Complete-Core Checks

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
- This previous extension left J=9941..39999. The updated original-source
  checker now uses the new interval recorded above.

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
  and now records the residual J=9941..31999. The sole near allowance remains
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

The wrapper runs children serially, with a 15-second timeout for inherited
checks and 45 seconds for each full quotient-density checker. Bytecode
is disabled and PYTHONOPTIMIZE cleared. Older assertion-based children
run normally. The four new extension/assembly checkers passed with -O
and explicit checks, using `--quotient-only --start J0` separately for
each of 32000, 34000, 36000 and 38000. Each block checks the full source
inventory but explicitly reports its partial arithmetic scope. Together
the four blocks cover the new interval, not the inherited supplier replay.

For more scheduling headroom use `--inherited-only` and those four separate
block commands instead of the full wrapper. A caught child timeout prints
its completed output prefix and exits INCOMPLETE, never PASS. No timeout
occurred in the publication runs. These are certificate replays, not
exploratory searches or scans of original-field sources.

Each run was enclosed in RAMguard tiny: 256 MiB RAM, 64 MiB swap and
60 seconds. A timeout is INCOMPLETE, not a successful proof. Measured
peak RSS is not a worst-case guarantee. No local fanout, large matrix,
CAS, TeX/Lean build, field-scale enumeration, installation, Modal job or
compute spending was used.

The universal basis inequality, analytic completeness, support transport
and inherited supplier proofs require human review. Hashes establish
source identity only. No globally clean local DAG, active-v4 row value,
unrestricted adjacent endpoint or completed Prize problem is claimed.
