# PRO WINDOW — "PETAL-PRIMITIVE-COORDINATE" (fresh window)

*Self-contained. This is the SHARED FOUNDATION of the petal cluster: one definition
+ one extraction lemma that unblocks all three open gates (N, D, L) of the full-petal
list-decoding branch. It is a DEFINITION/PROOF task with an executable predicate and
hard empirical constraints attached (a candidate already reproduces the key behaviour).*

## Setting
Reed–Solomon list decoding, full-petal branch. Domain mu_n subset F_q (q = poly(n) in
the generated-field window). A "full-petal extra" is a non-planted listed codeword with:
- touched-petal set I, t = |I| >= 3 petals; each petal T_i subset F_q has size ell;
- petal locators L_i(X) = prod_{z in T_i}(X - z) (squarefree, distinct roots);
- fixed scalars c_i in F_q*;
- a core "defect" d with ell <= d <= (t-1)ell; excess e := d - ell.

The CRT rank operator (PROVED machinery, Lemma 8 "Full-Petal Rank Certificate"):
    R_{I,d}(F) = ( c_i * F  mod L_i )_{i in I},     F in F_q[X], deg F <= d.
CRT-combine the residues into G in F_q[X]_{< t*ell}; let pi_{>d} extract coefficients of
degrees d+1, ..., t*ell-1. The residue-line kernel is
    K_{I,d} = ker( pi_{>d} R_{I,d} ),      dim K_{I,d} <= d - ell + 1 (PROVED).
A **squarefree-realizable component** = a kernel point F in K_{I,d} whose monic degree-d
normalization splits into d DISTINCT roots in F_q (an actual full-petal extra locator).

## The problem (the missing primitive coordinate)
The petal charging descent (PRK_pet, conditionally PROVED) needs a **moment window**:
- Gate N: every squarefree-realizable component's residue-kernel equations FORCE a window
  of >= c - kappa_N consecutive "quotient-compatible moments" (power sums), kappa_N absolute.
- Gate D: while the window m >= theta*Q, a coarser paid quotient (fiber >= mu*Q) saturates it.
- Gate L: terminal short window (m < theta*Q) => a paid low-defect quotient-complement sheet.
Descent charges coarser quotients until short; uncharged survives only for c < theta+kappa_N
(bounded) => dim Pi_prim <= B_pet => q^{B_pet} points, c-independent.

**The gap (verified):** the window is measured in the "primitive/quotient coordinate", which
is NOT defined in the repo. In the NAIVE ROOT COORDINATE (power sums sum_x x^t of the d roots)
the window is SMALL and does NOT grow with c -- so K-membership alone does NOT give Gate N's
window in the ambient coordinate. The primitive coordinate is genuinely load-bearing.

## Empirical contract (my Modal experiments -- your construction must match these)
Using the executable predicate above (K_{I,d} kernel points, split-squarefree):
1. **Naive window is capped.** Over 3.4M candidates / ~23k realizable points (t,ell<=6, d<=~20,
   q<=101): the naive (Q=1) moment window is <= 3, and does NOT grow with component size/excess.
2. **A quotient coordinate lifts it.** Define the quotient-Q window as the initial vanishing run
   of sum_x x^{Q t}, t=1,2,.... The MAX over Q reaches 5. Concrete witness:
   q=37, d=6, ell=5 (excess 1), roots {4,5,10,12,17,29}, Q=6 gives window 5 (> naive; > excess).
3. So a candidate coordinate = argmax_Q (quotient-Q window) already reproduces "small naive,
   large primitive". But argmax_Q over a GENERIC power x->x^Q is almost surely NOT the intended
   invariant -- it is unmotivated by the petal structure and its window did not visibly grow
   with c in the tested range.

## The ask
> **(A) Define** the quotient-compatible primitive coordinate / moment window intrinsically
> from the petal data (I, {T_i}, {c_i}, d) and the CRT operator R_{I,d} -- e.g. as power sums
> in a petal-adapted quotient variable, or Newton sums of a canonical primitive projection
> Pi_prim of the kernel point. It must be canonical (petal-structure-tied), not "best over all
> x->x^Q".
> **(B) Prove the extraction (Gate N):** every squarefree-realizable K_{I,d} kernel point has
> primitive-coordinate moment window >= c - kappa_N for an ABSOLUTE kappa_N (independent of
> n, c, t). Equivalently: the residue-kernel equations translate, via Newton's identities in
> the primitive coordinate, to >= c - kappa_N leading vanishing moments.
> **(C) Refute** if false: exhibit a squarefree-realizable family whose primitive-coordinate
> window stays O(1) while c -> infinity (in ANY canonical petal-adapted coordinate). This would
> break the descent and force a different charging mechanism.

## What this unblocks (all three gates share it)
- **Gate N** (petal_newton_window) IS part (A)+(B): the window definition + extraction.
- **Gate D** (petal_quotient_descent_step): its "long window => coarser quotient" is measured in
  THIS coordinate. (Numerically: realizability caps the naive window, so the bare counterexamples
  are excluded; the real descent lives in the primitive coordinate you define.)
- **Gate L** (petal_low_defect_quotient_charge): the short-window low-defect sheets are the
  C(M,delta) quotient-complement families (VERIFIED count); the coordinate bridge is link (b) of
  their chargeability to the proved fixed-excess layer petal_fixed_excess.

## Executable predicate (for checking your construction)
The kernel machinery is exact-F_q, stdlib: build L_i = locator(T_i); R_{I,d} columns from
residues c_i * X^k mod L_i CRT-combined; K_{I,d} = nullspace of the pi_{>d} rows; a component is
realizable iff a kernel combination is monic-degree-d and split-squarefree. Power sums / Newton
sums of the roots (or of Pi_prim) give the window. Any candidate coordinate can be validated
against constraints (1)-(2) above in seconds.
