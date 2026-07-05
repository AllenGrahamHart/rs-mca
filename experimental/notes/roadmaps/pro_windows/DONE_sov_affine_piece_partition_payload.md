# proof: sov affine-piece route REFUTED; re-posed to grid character-sum (Pro W2, verified)

## Refutation of the affine-piece route (verified structurally + brute force)
If H=mu_n subset F_q^*, then q>n. There is NO nonconstant F_q-affine line
L_t = L_0 + t B (deg B <= h-1, B!=0) of actual monic degree-h locators all split
in H. Incidence count: |I|=#{(t,x): L_t(x)=0} = q*h by t; <= g q + (n-g) by x,
where g=#{x in H: B(x)=0, L_0(x)=0} <= h-1. So q(h-g) <= n-g, impossible since
h-g>=1 and q>n. VERIFIED: no_affine_line_possible(q,n,h) holds for all RS rows and
all h; brute force at p=17, mu_8, h=3 (56 actual locators) finds ZERO affine lines.
Hence actual locator cells contain no positive-dimensional affine piece, so the
proved sov_nonconstant_affine_character_cancellation has nothing to act on. The
affine-piece partition PROOF ROUTE is dead. (single_obstruction_valueset itself is
NOT refuted -- the scan is UNIFORM_CONSISTENT; only this proof route dies.)

## Re-posed target: SOV-GRID-CHARACTER-SUM
The needed input is a genuine multiplicative-grid / divisor-variety character-sum
bound, after paid pullback/norm-gate classes removed: for every official row,
h in (20,A], conditioning cell Omega, nontrivial psi,
    | sum_{L in Omega} psi([X^{h-1}]L) | <= CharBudget(Omega,h,n,q)
small enough for sov_hminus1_fiber_fourier_duality to give the small-fiber bound.
Since [X^{h-1}]L = -e_1(roots)+const, the unconditioned sum is
    S_h(a) = [u^h] prod_{x in H_rem}(1 + u psi(-a x)),  a!=0.
Proof lanes: (1) distinct-coordinate/symmetric-power sieve on the Euler product;
(2) Artin-Schreier sheaf on the divisor chart, geometrically nontrivial off the
paid norm-gate locus, trace <= conductor * q^{dim/2}; (3) norm-gate exceptional
accounting (the degeneracy locus = pulled-back-from-quotient/dihedral/norm cells,
already paid). This is the SAME downstream shape; only the proof input changes
from exact affine cancellation to analytic grid cancellation.
