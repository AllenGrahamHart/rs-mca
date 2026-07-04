# Pro brief (v4, SATURATED ASSEMBLY) — Hankel termination

*Your round-4 reformulation is adopted. This states the assembly and points at
the proved piece that may already do the heavy lifting.*

## Adopted: count root-closures, not raw supports
Verified: your loop-free pair-family (weighted syndrome S_m = sum_{a in A} u_a
a^m on a NON-COSET A) is gcd-trivial AND primitive, with all pairs of A weight-2
circuits, raw #L = 2^|A| - |A| — yet rcl_P({a}) = A for every a, so all pair-
atoms share ONE root-closure. Raw union-closure is the wrong invariant; the
descent state is the forced-root closure rcl_P(B u S), and grouping atoms by
closure collapses the artifact. (This refines the QF.12 support-lattice
identity, which bounds STATE size only — member/fiber counts are a separate
leaf input, as you noted.)

## The assembly (what the repo already has)
The target is: reachable UNPAID PRIMITIVE saturated closures are poly(n), with
moment-clean terminal leaves. The heavy lifting may already be PROVED:
- **f_many_sparse_structure (PROVED):** many-sparse flats are multiplicative-
  pullback, DIHEDRAL/Chebyshev-quotient (X^e g(X^M + X^{-M})), tangent, or
  descent-reducible — nothing UNPAID survives all four branches. It explicitly
  handles the reciprocal/dihedral flats (gcd-trivial, aperiodic, super-poly
  raw lattice) by routing them to the enlarged quotient class. This is exactly
  your "route paid structure to the ledgers."
- **f_gcd_reduction (PROVED):** strips common roots. **f_scale_recursion
  (PROVED):** strips pullbacks to scale n/M.
Contrapositive chain: unpaid + primitive => NOT many-sparse (by
f_many_sparse_structure) => few sparse atoms => poly reachable root-closures.

## The ask
- **(A) Write the assembly / find the gap:** does f_many_sparse_structure,
  applied to the Hankel-kernel subfamily under root-closure saturation, yield
  poly reachable unpaid-primitive closures? Identify precisely what is missing
  — most likely (i) that the dihedral/enlarged-quotient paid branch routes to
  an actual repo reduction at the Hankel instance, and (ii) the moment-clean
  leaf statement (direction-dual cleanliness of terminal unpaid primitive
  flats), which f_support_lattice does NOT provide.
- **(B) Break it:** exhibit a Hankel kernel with many INDEPENDENT saturated
  primitive atoms that is provably NOT pullback/dihedral/tangent/descent-
  reducible — i.e. a counterexample to f_many_sparse_structure in the Hankel
  case. Per your own read, this would be a NEW PAID LEDGER CLASS, not a descent
  failure — and would be extremely valuable (it reopens f_many_sparse_structure,
  which is currently marked PROVED and load-bearing).

## Scrutiny request
Because f_many_sparse_structure is now load-bearing for this closure, please
also sanity-check its four-branch completeness at the Hankel instance: is
"nothing unpaid survives all four branches" genuinely a theorem, or is the
dihedral/Chebyshev branch's completeness itself conditional?
