# p3_affine_net_richline_residue

- **status:** PROVED
- **closure:** proof
- **refs (legacy repo):** ['experimental/notes/roadmaps/e33_deep_link_staircase.md']

## Statement

P3 verdict (CONDITIONAL, 10/10): the current paid strip (tangent pencil + quotient-with-tails + dihedral) does NOT yield the rich-line cap — after normalizing by a fixed (k-1)-subcore, off-core points define lines in the (z,a) parameter plane, and (t+1)-rich points can arise from MULTI-DIRECTION AFFINE NETS rather than pencils or quotient/dihedral structures. The remaining obligation: bound post-strip rich points from affine nets. TWO candidate routes: (a) the nets may be chargeable to the UNIFIED pullback class (affine maps are degree-1 rational maps; net directions = mixed low-degree pullbacks — check against the Luroth frame before inventing new machinery); (b) if genuinely primitive, this is finite-field incidence geometry (Szemeredi-Trotter/Vinh-type rich-point bounds) — classical tools exist. NOTE the theme: affine/additive structure surfacing for the third time today (the involution witness, the moment blocks, now nets).

## Attack surface

first check route (a): express net-generated rich configurations as mixed degree-1 pullback trades; if that charges them, P3 completes with the unified strip. Else route (b): finite-field incidence bounds at the exact parameters (rich points of line arrangements over F_q, t+1-rich, poly-many lines)

## Falsifier

a post-unified-strip toy net achieving super-linear rich points (extend E33's scan with a net detector)

## Ledger (migrated notes)

U3 — THE NET-ABSORPTION CONJECTURE (route (a) promoted): the multi-direction affine nets are mixed degree-1 pullback trades, charged by the unified strip — nets in the (z,a) plane are graphs of affine maps = fibers of degree-1 rational families, i.e., the fourth guise of the one class discovered today. Checkable at toys in an afternoon (net detector vs fiber dictionary); if true, the rich-line cap completes via P1's proved reduction + the unified strip. | U3 PROVED (F3, #20, 33/33 replayed): the affine-net residue CHARGES to mixed b=2 degree-1 pullback cells under the unified strip — 14 net cases over F_193 incl. the original P3 net (342 rich points, 726 pair trades, 4314 local identities, all verified). The unification's fourth guise confirmed absorbed.
