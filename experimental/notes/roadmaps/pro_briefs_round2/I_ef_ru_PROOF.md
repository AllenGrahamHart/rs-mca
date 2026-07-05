# conditional: ef_descended_cycle_inventory_payload (Pro's completeness proof)

## Predicate nodes

- `ef_fullfield_bridge`

## Claim
The three-class inventory is COMPLETE for pole-free cycles (Pro's stabilizer
trichotomy), conditional on the full-field scope bridge.

## Proof (Pro, refereed — Galois-descent part unconditional)
Let Y be a B-defined pole-free horizontal cycle; decompose Y_E into G-orbits of
reduced horizontal components (G = Gal(E/B)). For a component C, its stabilizer
H = Stab_G(C) is exhaustively one of:
- **H = G:** C is defined over E^G = B -> base-descended.
- **1 != H != G:** by ef_galois_stabilizer_descent, C is defined over the proper
  intermediate fixed field E^H -> tower-confined.
- **H = 1:** by ef_full_orbit_cycle_descent the full orbit union Z = U_g gC
  descends to B. Split by noncontainment: if it FAILS, noncontain_degeneracy
  puts C in the degenerate residue class (a=b=0). If noncontainment HOLDS, then
  (trivial stabilizer + noncontainment + not base/tower) => C is a genuinely
  full-field extension fiber [THE BRIDGE, ef_fullfield_bridge], so ext_pole_floor
  forces C ∩ D_E != empty, hence Y_E ∩ D_E != empty, contradicting pole-freeness.
No new structure hides in Z: G acts transitively on {gC}, so the only G-stable
subcycles are empty and the whole orbit — no proper B-defined horizontal
subcycle, hence no fourth ledger class. The trichotomy is exhaustive, so the
three classes cover all pole-free cycles.

## The one seam (ef_fullfield_bridge)
The proof is unconditional EXCEPT the scope match: that a trivial-stabilizer,
noncontainment, non-tower horizontal component of X IS an extension fiber to
which ext_pole_floor applies. The legacy s6 sketch (s6_extension_lift.md line 95)
names this exact point as F1 — "a genuinely-F obstruction NOT of pole/confined
type -> new ledger column; the honest place the Lean-ledger case split would
first fail to typecheck." So it is a genuine (clean, sharp) predicate, not free.
