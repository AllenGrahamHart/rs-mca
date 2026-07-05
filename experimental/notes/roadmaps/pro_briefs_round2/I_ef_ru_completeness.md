# Pro brief — pole-free cycle classification completeness (ef_ru)

*Self-contained Galois-descent completeness problem. All exit classes are
proved; the open content is that they EXHAUST pole-free cycles (no leakage).
An assembly closes it; a hidden-fiber leakage refutes it.*

## Setting
Fields B <= E <= F, E/B finite Galois with G = Gal(E/B). Over B: the
extension-fiber alignment incidence variety X and the extension-pole divisor D
(both B-defined). "Horizontal cycles" are the reduced horizontal components of
X. A cycle is **pole-free** if it avoids D. The row B is admissible
intermediate (E > B; the generating case E = B is trivial: G = 1).

## Proved inputs (take as black boxes)
- **ext_pole_floor / ext_import / paid_ext_fn (PROVED):** the extension-pole
  floor — a genuinely full-field (E-valued, not descended) extension fiber
  MEETS the pole divisor D; such orbits are paid by the pole ledger.
- **ef_full_orbit_cycle_descent (PROVED):** a horizontal component with TRIVIAL
  G-stabilizer has its full orbit union Z = union_{g in G} gC; Z is G-stable,
  hence descends to a B-defined reduced horizontal cycle (Galois descent of a
  G-stable reduced closed subscheme).
- **ef_galois_stabilizer_descent (PROVED):** a component with NONTRIVIAL
  stabilizer H <= G is fixed by H, hence defined over the proper intermediate
  fixed field E^H -- tower/subfield-confined.
- **noncontain_degeneracy (PROVED):** containment = degenerate pencil
  (a = b = 0) = residue -- the noncontainment-degenerate class.
- **ef_full_orbit_pole_forcing is PROVED CONDITIONAL on this exclusion:** a
  full-field orbit avoiding D descends (above) to a B-defined pole-free cycle;
  IF every such cycle is base-descended / tower-confined / noncontainment-
  degenerate, then no full-field orbit can avoid D. So this exclusion is the
  one missing input to Theorem K.

## The claim to prove (the terminal obligation)
> Every B-defined pole-free horizontal cycle produced by full-orbit descent is
> one of: (i) base-descended, (ii) proper-subfield/tower-confined, or (iii)
> noncontainment-degenerate. Equivalently: there is NO "Galois-skew hidden-
> fiber leakage" -- no unpaid Galois orbit over an intermediate row B < E that
> fails to descend, is not subfield-confined, avoids D, and survives
> noncontainment.

The apparent shape: the stabilizer dichotomy (trivial vs nontrivial) is
exhaustive on components, giving (i) or (ii); noncontainment handles (iii); and
ext_pole_floor forces any genuinely-E cycle onto D, so a pole-free cycle is not
genuinely-E. The task is to verify these compose into a COMPLETE classification
with no gap -- in particular that the descended B-cycle in (i) carries no new
unpaid horizontal structure beyond the three classes.

## The ask (choose your target)
- **(A) Completeness proof:** assemble the stabilizer dichotomy + ext_pole_floor
  + noncontainment into a proof that the three classes exhaust pole-free cycles,
  identifying precisely why no hidden fiber survives. (Referee note in the repo:
  this may follow directly from the banked extension-fiber arithmetic -- if so,
  make the implication explicit.)
- **(B) Leakage counterexample:** exhibit (or prove exists) a pole-free B-defined
  horizontal cycle over an intermediate row that is none of the three classes --
  a genuine Galois-skew hidden fiber. This would be a NEW paid ledger class and
  would reshape Theorem K.
- **(C) Conditional:** completeness modulo a clean stated hypothesis on the
  descended cycle's structure.

## Downstream
Closing (A) discharges ef_pole_free_cycle_exclusion -> ef_full_orbit_pole_forcing
-> ef_ru -> f1_full_field_pole_forcing (two critical reds at once).
