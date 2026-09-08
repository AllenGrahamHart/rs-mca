# Audit And Provenance

The tail9821.md continuation uses h>=1600 and ell<=2740 in the SAME
component Johnson expression; its denominator is 80873689>0. It counts
<=1943 pairs per top component and <=57709146976 in the entire lower
complement, then adds one singular and 256 off-curve pairs. The original
projective-degree proof is unchanged. The low-height cumulative payment
is owned by the consumer and is not a premise here. The kernel's two
verify_double_point_cubic_tail checks replay this boundary independently.

The `cutoff101.md` companion changes only the numerical agreement,
height and parameter-degree envelope. It uses the already proved
polynomial models and original-degree component count. Two coupled
derivative arguments give <=4622 rich pairs per top component; the
entire smaller-dimensional complement costs <=56078104495 pairs.
One possible singular pair gives 255040048958 in total. The consumer's
new LOW/HIGH budget and kernel coverage are separate, not dependencies
of this component proof. The kernel's `verify_low_cutoff_strip.py` and
independent audit replay this envelope, including a direct 4623-pair
contradiction, under tiny RAM limits. This is not external hand review.

The PROVED continuation `next_interval.md` extends the d=7 high-height
source bound to 8656..9526, 1301<=h<=4762, with N<=241058823023306107.
Coupling h in both Johnson budgets gives <=4271 pairs per top component;
all lower-dimensional components are counted. The new checks are
`verify_next_interval.py` and `verify_next_interval_audit.py`; the old
independent height rectangle fails here. No requirement changes or
quartic closure follows. Earlier records below keep their narrower scopes.

Status: PROVED local hand argument, 2026-09-07. Independent external
proof review remains outstanding. The arithmetic checks are not that review.

The previous turn paid the d=10 geometric-progression source pattern.
This turn pays d=7 by a different, componentwise argument, without
assuming or adding a speculative maximal-family classification.

## High-Risk Steps Checked By Hand

- The rational normalization parameters lie in a FIXED bounded space.
  On each irreducible component, choose an actual center and divide the
  gcd of parameter differences. Evaluation then varies at every finite
  coordinate, and the maximal-degree coefficient varies at infinity.
- The largest-pole and largest-degree terms are nonzero polynomials in
  those varying values. They cannot vanish on an infinite image. This
  proves regular output coefficients and their exact degree ceilings;
  no full affine parameter space or receiver genericity is assumed.
- The cubic leading vector has a polynomial common factor gamma because
  A,B are primitive. Constant output fibers are bounded by its degree.
  The nonzero quadratic-projection coefficient E also vanishes at every
  identical-agreement coordinate, yielding the -3g slot correction.
- g is bounded rather than fixed at its maximum. Both the quotient
  monotonicity and an independent direct 316-pair contradiction justify
  the uniform envelope, with positive denominators throughout.
- A per-component cap is insufficient alone. The projectivized cubic
  map has no basepoints, finite fibers and an explicit rational inverse
  off the singular pair. The finite degree formula gives degree >=3^r
  in ORIGINAL pair coordinates. This pays the number of components.
- Lower-dimensional points are restricted to the complement of all
  three-dimensional components before using the lower weighted budget.
  No bound for a pure cover is transplanted to the wrong equation locus.
- One singular pair, <=64 off-curve pairs, original complete-core label
  gains, one HIGH resource and one original near allowance are retained.
  Parameter changes neither discard coordinates nor alter slope units.

## Exact Checks And Scope

Primary Fraction/envelope check: PASS, 0.07 seconds, 11392 KiB RSS.
Independent direct-Cauchy/integer-degree/cover check: PASS, 0.01 seconds,
10240 KiB. The latter includes real triple and constant fibers over F_7.
No field-sized computation, CAS, matrix expansion or Modal spending.
The cycle record gives DAG compilation and before/after diagnostics.

The finite-map degree formula is [Stacks 33.45.11](https://stacks.math.columbia.edu/tag/0BEX),
applied at its exact scope in `component_degree.md`. The weighted supplier
provides its attributed nonuniform/basis, dimension and incidence inputs.
The new component model, list and degree-budget assembly are proved here.
No external theorem is asserted to prove the new source count for us.

Pins: canonical Fable `0dd5b324482194208be0289f76ed3f0817648a46`,
read-only; main `93fba1be3f3299b0ba4708d88715377bbb656e45`;
open #1175 `6c59f9aa75b897c9274e94c7aa8864acd26a85ea`, freshly
inspected. Local dirty HEAD is `3b51e86d2595f28a02e842c81effca1dfcf98e77`.
This result and the previous d=10 payment are NOT in immutable export
f4379ee6. No new public post, PR or upstream acceptance this cycle.

The whole-strip theorem is owned by the full-kernel consumer, which
supplies exhaustive source classification. The present supplier proves
the d=7 source-class count; it never requires that consumer in reverse.
Original-row and active-owner transport remain separate obligations.
