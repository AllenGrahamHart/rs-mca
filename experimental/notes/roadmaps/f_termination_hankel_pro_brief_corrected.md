# Pro brief (CORRECTED) — Hankel support-lattice termination

*Supersedes pro_brief_broad.md. Fixes a definitional error that Pro's own
counterexample exposed: W(P) must exclude GENERIC circuits.*

## The correction (why the previous brief's target was trivially false)
Previous brief defined W(P) = ALL minimal dependent column supports. But a
dimension-D flat has ALL (D+1)-subsets dependent by dimension alone (the
uniform-matroid circuits) — GENERIC, present for every flat, including MDS.
Pro's counterexample P = span{1,X,...,X^{d-1}} (an MDS Reed-Solomon flat,
realizable as a rank-t Hankel kernel with a single nonzero syndrome entry)
then has #L(P) = 2^n - O(n^d): exponential. Correct, and it kills the target
AS STATED — but these are the GENERIC circuits the descent never processes.

## The corrected object
For a flat P of dimension D = dim(P), a SPARSE DUAL WORD (the only kind the
descent peels) is a minimal dependent column support of weight
    w <= D    (STRICTLY below the generic circuit size D+1),
i.e. an EXCEPTIONAL dependency: w columns dependent where a general-position
flat would have them independent. Let W(P) be these, and L(P) the union-
closure. Then, crucially and CONSISTENTLY:
- MDS / general-position flats: W(P) = empty, #L(P) = 1 (trivial). This is
  exactly the PROVED f_termination_mds corollary.
- E17 (n16 k8 j5 t3): a weight-2 word (support {2,3}), w=2 <= D, genuine.

## The (unchanged, now correctly-posed) reduction — PROVED, take as given
Descent-tree size <= #L(P) * (1 + Wmax). Hence the Hankel family terminates
in poly(n) IFF  max over Hankel-kernel flats P of #L(P)  is poly(n), with
L(P) now the EXCEPTIONAL (sub-generic) support lattice.

## Evidence (F_17 census; larger mu_32/64 max-search in progress)
- Generic flats carry <= 1 exceptional sparse word => #L(P) <= 2 (trivial).
- Exceptional weight-2 supports occur at ~random-flat rate, at all diameters.
- So max_P #L(P) is set by RARE structured (coset/degenerate) flats. Working
  conjecture: the max is the coset-lattice (poly), non-coset words isolated.

## The ask (choose your target; reformulation welcome)
Determine the growth of  max_P #L(P)  with L(P) the EXCEPTIONAL support
lattice (weight <= dim circuits only), over rate-1/2 Hankel-kernel flats.
(A) Full proof #L(P) <= poly(n) [displacement-rank-2 rigidity is the natural
    lever: bound the number of sub-generic circuits a Hankel kernel carries].
(B) Counterexample: a Hankel-kernel family with super-poly EXCEPTIONAL #L(P)
    (must use weight <= dim circuits — generic (D+1)-circuits do NOT count).
(C) Conditional: poly modulo a clean stated hypothesis on exceptional
    circuits.
Anchors: n=16,k=8,p=17,g=3, split t=3,j=5; pullbacks M in {2,4,8}.
