# Double-point interpolation closes the entire remaining quartic strip

Current scope: `double_point_cubic_tail.md` has now completed the
subsequent 9527..9821 tail. The proof below remains the independent
8764..9526 stage; its closing next-action paragraph is historical.

Status: PROVED. For EVERY canonical normalized source of this node on
8764<=J<=9526, without any curve-description hypothesis,

    N=|Gamma|+134944 <=274979661975561635,
    B=274980728111395087,
    reserve>=1066135833452.                           (QS)

Together with the earlier proofs, EVERY source on 4801..9526 is paid
at the uniform bound in (QS). This closes 763 additional integer J values.
The remaining normalized interval starts at 9527, not 8764.

## Exhaustive alternatives

Use only sections 1--5 of quartic_obstruction.md. They independently
prove the full W8 kernel has gcd degree <=4, with at most 64 off-gcd
pairs. Every factor pattern except one geometrically integral quartic
already pays by the right side of (QS). This earlier dichotomy uses
neither double-point interpolation nor the later quartic refinements.

In the remaining case, all but <=64 LOW pairs lie on one irreducible
quartic over F(X). The finite consumer's quartic_multiplicity_payment.md
now gives the much smaller whole-source bound 4194117119656075.
It uses the required general multiplicity-escape lemma, with no restriction
on this quartic's genus, singularities, coefficient height, projection
kernel, positive-dimensional families or isolated pairs.

Thus BOTH exhaustive alternatives pay. Take their MAXIMUM, not their
sum. Each alternative already includes all original LOW labels, HIGH
resource, exceptions and the single near add-back. This proves (QS).
The earlier intervals have no larger upper bound, proving the combined
4801..9526 statement at the unchanged source contract.

## Dependency and scope checks

The multiplier-space height/off-pair refinements and the special split-
product or projection-graph quartic payments remain correct independent
results. They are NOT needed for this closure: the original 64-pair
quartic dichotomy plus the new general escape payment suffice. No proof
of that old dichotomy is allowed to invoke the current closure in reverse.

The finite quartic payment by itself extends to J=9821, but the present
full W8 factor classification stops at 9526. Arbitrary sources on
9527..9821 are not silently assumed to have a quartic cover. The new
supplier's `kernel_corollary.md` proves that the double-point full kernel
has gcd degree <=3 and <=256 off-gcd pairs on 9527..9821. But its
factor weighted degree is <2*A, not <A. Those actual new heights,
exception counts and cubic payments must be assembled before claiming
any further interval closure.

Higher original error ranks, exhaustive original-source/near/owner
transport, unrestricted adjacent endpoints, ordinary LIST and both prize
problems remain open. No original red node is promoted by this interval.
