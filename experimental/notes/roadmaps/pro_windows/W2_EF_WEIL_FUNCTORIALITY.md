# PRO WINDOW W2 — "EF-WEIL-FUNCTORIALITY"

*Fresh window. The SOLE remaining seam of the entire f1/ef program, reduced to
a functoriality property of an existing proof. Everything else is proved.*

## Recap of what is already established (take as given)
Fields B <= E <= F, E/B finite Galois, G = Gal(E/B). Over B: the extension-fiber
alignment incidence X and the extension-pole divisor D. Goal: every B-defined
POLE-FREE horizontal cycle is base-descended / tower-confined / noncontainment-
degenerate (no "Galois-skew hidden fiber"). Established across prior rounds:
- Stabilizer trichotomy (PROVED): H=G -> base; 1!=H!=G -> tower-confined; H=1 ->
  full orbit descends. The only escape is the trivial-stabilizer, noncontainment,
  non-tower case.
- That case is a genuinely full-field extension fiber; by the s6 linear-pencil
  dichotomy its non-B slope comes from F-valued word data OR the pole mechanism.
- The pole case meets D. The F-valued-word case: PROVED that it is an
  e-INTERLEAVED base-list multiplication-slice witness (e=[E:B]) -- syndrome
  commutes with B-basis expansion (D subset B), mult-by-z = M_z; the ordinary-
  base-list version is FALSE (the X-alpha counterexample).
- The interleaved list-counting is EXACT: L_eff = the extension-code list size,
  NOT L^e (interleaving filters the product to the common-support diagonal).
- FOR THE GEOMETRIC EXCLUSION a SINGLETON suffices: L_eff = 1 gives the floor
  numerator N_int(1) = ceil(X/(X + kappa)) = 1 for X = |F|-|B| > 0 (verified).

## The sole remaining obligation
> **interleaved_floor_import (singleton form):** the Paper D extension-pole
> floor proof is FUNCTORIAL under Weil restriction — it applies to a B-defined
> singleton e-interleaved base-list multiplication-slice witness, forcing that
> witness onto the extension-pole divisor D_E.

The floor is PROVED for ordinary B-valued base lists via
    N(L) = ceil( L(|F|-|B|) / (|F|-|B| + kL) ),  k = 2^40.
The question is purely whether that SAME PROOF survives replacing the scalar
base list by the Weil-restricted / interleaved incidence
    Phi(f) + M_z Phi(g)
(a B-defined finite witness list). This is the s6 sketch's flagged F1 typecheck
("a genuinely-F obstruction not of pole/confined type -> new ledger column S9").

## The ask
- **(A) Prove functoriality:** show the Paper D floor argument uses only
  B-linear / support structure that is preserved by Weil restriction, so it
  applies to the singleton interleaved witness (N_int(1)=1 => meets D_E). This
  discharges ef_pole_free_cycle_exclusion -> ef_full_orbit_pole_forcing ->
  ef_ru -> f1_full_field_pole_forcing. Identify the exact step that must be
  checked (the paper's floor proof is the extension-pole/list-window import
  N(L)).
- **(B) Exhibit S9:** a singleton interleaved witness the floor proof provably
  does NOT reach -- a genuine new extension-valued ledger class.
- **(C) Conditional:** functoriality modulo a clean stated property of the
  Paper D floor construction.

The Paper D floor is `cs25_cap_v12.tex` (extension-pole / list-window section)
in github.com/przchojecki/rs-mca. The crux is one scope check, not a new theorem.
