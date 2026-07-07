# URGENT UPDATE to the F5 ABSORPTION window: the lemma AS STATED is FALSE
# — verified counterexample below. Re-aim before spending proof effort.

Our on-locus harvest settled the question hours after the brief went out:
the dependence locus of the minimal stratum (P = 8, m = 6) is codim 1,
and on it, absorption FAILS generically. Verified end-to-end certificate
(q = 97, k = 2, A = 4):

  supports: {22,26,76,60} {22,60,63,92} {22,63,51,19}
            {26,76,92,19} {26,60,51,19} {76,63,92,51}
  slopes:   50, 48, 3, 89, 68, 6
  alignment rank 11 of 12 (one dependence), and an explicit (u,v) exists
  (full certificate JSON in the repo: f5_absorption_counterexample.json)
  with ALL six supports EXACT agreement sets, all Pi_S(v) != 0, pairwise
  cores <= 2, distinct slopes.

So: dependent live families exist. If your window has partial proofs of
absorption, they contain an error wherever they exclude this
configuration — the counterexample is a useful debugger.

## THE RE-AIMED TARGET (what the theorem actually needs): L3''

> **RANK LOWER BOUND: for a live family of N supports (pairwise cores
> <= A−2, distinct slopes, all valid and exact at some (u,v)), the
> alignment system's rank is at least sigma·N / x for some x polynomial
> in n** (any x up to ~n^2 suffices for the 16n^3 floor; we believe
> x = O(1), plausibly rank >= sigma·N − N/6).

Equivalently: an upper bound on the NULLITY (number of independent
syzygies). Known and available: (L3a, proved) every syzygy's participant
set is a rigid subconfiguration — every participant point covered >= 3
times or slope-shared — hence >= 6 supports at A = 4; disjoint syzygy
clusters therefore give nullity <= N/6, which suffices. The open case is
STACKING: overlapping clusters sharing supports. Matroid girth alone
does not bound nullity (generic vectors in low dimension), so the
structure (full-support Lagrange rows, small pairwise cores, the
(a_S, z·a_S) slope form) must be used.

Attack lines: (1) apply the L3a per-point 2-moment collapse to a BASIS
of the dependence space simultaneously — shared points across syzygies
over-constrain the lambda blocks; (2) count: nullity s implies s
independent fresh directions in the solution space beyond the
pencil-degenerate plane, and each fresh direction is a pencil with 6+
exact 4-alignments on 8-14 points — bound how many such pencils fit;
(3) refute: engineer a family where nullity grows like sigma·N − o(N)
(this would genuinely threaten the floor's proof route, though not the
floor itself at official scales — the budget has ~2^100 slack).

Same conventions; we replay everything.
