# Pro brief B: the F-induction step (spread/coincidence dichotomy)

SETTING. Conjecture F's incidence frame (full definitions in the attached
proved base-case packets — read those first; they are self-contained):
parameter space of linear pencils P <= P^j, the divisor locus D_j, the
notions pullback / paid / gcd-trivial as defined there. The campaign has
PROVED: f_dim1 (the 1-dimensional case), f_dim2_skeleton (the
2-dimensional skeleton, 5/5 + a 25.7M-plane census), f_concurrency_equiv
(the concurrency reformulation), and the reductions f_gcd_reduction +
f_scale_recursion (full Conjecture F follows from the primitive case).
The remaining step is stated as:

  F_r for gcd-trivial r-flats by induction on r: at each point of
  multiplicity >= j, EITHER the hyperplanes through it are SPREAD in the
  flat (local pair-type counting binds, the dim-2 skeleton's mechanism)
  OR coincidences abound (twin-type structure) — forcing a shared divisor
  factor and descent to F_{r-1} of the reduced instance. Each dimension
  of excess buys one unit of divisor factor.

ASK. Prove the induction step F_{r-1} => F_r in this dichotomy form (the
target bound is n^{B_F} per flat, B_F an absolute constant), using the
attached base cases as black boxes. Partial results of value: the
dichotomy lemma alone (spread OR shared-divisor, precisely quantified);
or the descent step (coincidence => reduced instance strictly smaller).
A counterexample to the dichotomy at r = 3 would be equally decisive.

Attach: nodes/f_dim1/proof.md, nodes/f_dim2_skeleton/proof.md,
nodes/f_concurrency_equiv/proof.md, nodes/f_primitive_case/statement.md.
