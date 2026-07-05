# Pro brief — light-triangle eliminant nonvanishing (parametric)

*Self-contained determinantal / generalized-Vandermonde problem. A parametric
proof closes it; a single identically-vanishing unpaid profile refutes it.*

## Setup (elementary linear algebra over a field)
Reed-Solomon RS_k over evaluation domain of distinct points x_1,...,x_n in a
field F (prize: mu_n, but the statement is characteristic-generic). For a
support T subset [n] with |T| = A = k + t, the "Lambda space" Lambda_T is the
weight-<=A dual space: all vectors lam supported on T with
sum_{i in T} lam_i x_i^d = 0 for d = 0..k-1 (the k moment conditions). By the
Vandermonde shortening, dim Lambda_T = t, with an explicit chart basis: fix k
"pivot" points and t "free" points of T; each free point gives one basis
vector (free coord = 1, pivot coords solved from the k x k Vandermonde).

A **light triangle** is a triple (T0,T1,T2) of such supports with slopes
(z0,z1,z2), in the light regime  pair_sum - trip <= 2k, where
pair_sum = |T0&T1|+|T0&T2|+|T1&T2| and trip = |T0&T1&T2|. Its **normal-form
matrix** M(T0,T1,T2,z0,z1,z2) is the 2|U| x 3t matrix (U = T0 u T1 u T2) of the
map
    (a0,a1,a2) |-> ( sum_i B_i a_i ,  sum_i z_i B_i a_i )   restricted to U,
where B_i is the chart basis of Lambda_{T_i}. A triangle **syzygy** (kernel)
exists iff rank M < 3t iff all 3t x 3t maximal minors vanish. The **eliminant**
of a profile is (the ideal of) these maximal minors as polynomials in the
support coordinates x_. and slopes z_..

## The claim to prove
A **profile** is the combinatorial type: the overlap shape (pair_sum, trip,
union_size) together with the pivot/free incidence pattern. Call a profile
**paid** if tangent/quotient-pullback structured, **boundary** if
pair_sum - trip = 2k. Prove:

> For every light profile that is neither paid nor boundary, the normal-form
> matrix has at least one maximal minor that is a NONZERO polynomial in the
> support coordinates and slopes. Equivalently: no unpaid non-boundary light
> profile has the eliminant vanishing identically (a generic instance of the
> profile has full rank 3t / no syzygy).

Since a nonzero value at one admissible specialization certifies a nonzero
polynomial, this is a genericity/nonvanishing statement per profile type.

## Evidence (Modal census, this repo)
A faithful census over k=2..6, t=2..5, A=4..11 found, for ALL 152 realized
light profile types, an explicit full-rank (3t) instance — ZERO identically-
vanishing profiles. Nonvanishing is uniform as (k,t) grow. So the theorem is
true; the profile-type count grows with (k,t), so the prize-scale quantifier
(k up to 2^40) needs a parametric argument, not enumeration.

## The ask (choose your target)
- **(A) Parametric proof:** exhibit, for each profile type as a function of
  (k, t, overlap shape, incidence), a specific maximal minor and prove it is a
  nonzero polynomial. The natural route the construction is built for: the
  generalized-Vandermonde shortening bases make the minors explicit; find a
  TRIANGULAR maximal minor with nonzero diagonal (nonzero by a monomial /
  leading-term argument), uniformly in the profile parameters. A stabilization
  lemma ("nonvanishing for the base profile type implies nonvanishing at all
  larger sizes of that type") would also suffice, combined with the finite
  census over base types.
- **(B) Counterexample:** a light profile, neither paid nor boundary, whose
  eliminant vanishes identically (all maximal minors are the zero polynomial).
  This would be a genuinely-degenerate class the paid ledger must absorb — a
  new named stratum. (The census suggests none exists, so this would be a
  surprise with real consequences.)
- **(C) Conditional:** nonvanishing modulo a clean stated incidence hypothesis
  that the paid/boundary exclusion supplies.

## Downstream
Closing (A) discharges `xr_profile_eliminant_nonvanishing`, hence
`xr_eliminant_vanishing_class` (the structured-branch danger is removed; the
residual coordinate-special vanishing is a proper hypersurface, already
proved, rationed by the staircase machinery).
