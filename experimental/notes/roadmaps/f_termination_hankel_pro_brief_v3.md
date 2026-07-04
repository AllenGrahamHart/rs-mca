# Pro brief (v3, PRIMITIVE) — Hankel support-lattice termination

*Supersedes v1/v2. Your two counterexamples pinned the exact preconditions;
both are stripped by proved reductions. This is the genuinely open residual.*

## Why v2 was still refutable, and the fix
- v2 (weight <= D circuits): you gave P = q_A(X) K[X]_{<=j-r} with all x in A
  ZERO columns -> weight-1 loops -> #L = 2^|A|. Correct. FIX 1: these are
  common roots; f_gcd_reduction (PROVED) divides them out. Descent runs on
  gcd-trivial flats (no common root).
- BUT gcd-trivial is NOT enough. The pullback flat P = {g(X^2) : deg g <= m}
  is gcd-trivial yet has disjoint weight-2 coset circuits {x, -x} for all n/2
  antipodal pairs -> #L = 2^{n/2} (verified at n=16: #L = 256). FIX 2: these
  are the PERIODIC/pullback flats; f_scale_recursion (PROVED) handles them
  separately (an M-pullback ell = g(X^M) recurses to scale n/M:
  F(n) <= F_primitive(n) + sum_{M | gcd(n,j)} F(n/M)). They are never counted
  by the support lattice.

## The correct, downstream-faithful object
Both proved reductions strip exactly the two escape classes. The descent's
residual is the PRIMITIVE case: **gcd-trivial AND non-pullback**. Define, for
such P (dimension D):
    W(P) = minimal dependent column supports of weight 2 <= w <= D
           (weight-1 impossible: gcd-trivial; weight D+1: generic, excluded),
    L(P) = union-closure of W(P).
This is f_primitive_case specialized to Hankel; the downstream Conjecture F is
literally assembled as f_gcd_reduction + f_scale_recursion + f_primitive_case,
so this exact strength is what closes the chain.

## The reduction (PROVED, take as given)
Descent-tree size <= #L(P) (1 + Wmax). Hence the primitive Hankel family
terminates in poly(n) IFF  max over gcd-trivial non-pullback Hankel-kernel
flats P of #L(P)  is poly(n).

## Evidence
Generic gcd-trivial flats carry <= 1 exceptional weight-2 word (E17 type:
n16 k8 j5 t3 has a single weight-2 word on {2,3}), hence #L(P) <= 2 trivially.
The exponential families (2^|A|, 2^{n/2}) are ALL non-primitive (common-root
or pullback). Question: can a PRIMITIVE gcd-trivial Hankel flat have super-poly
#L? (A larger primitive-only census is being refocused.)

## The ask (choose your target)
- (A) Full proof: max_P #L(P) <= poly(n) over gcd-trivial NON-PULLBACK flats.
  Lever: Hankel displacement rank 2 + the primitivity constraint bound the
  number of disjoint exceptional circuits (the pullback case saturates the
  bound precisely because it is periodic; primitivity should forbid Theta(n)
  disjoint coincidences).
- (B) Counterexample: a gcd-trivial NON-PULLBACK Hankel family with super-poly
  #L (must avoid common roots AND pullback structure — the previous two escapes
  are now closed).
- (C) Conditional: poly modulo a clean bound on disjoint exceptional circuits
  in a primitive Hankel kernel.
Anchors: n=16 k=8 p=17 g=3, split t=3 j=5; pullbacks M in {2,4,8} are the
EXCLUDED periodic flats; the {2,3} word lives on a primitive flat.
