# Audit

Shared-carrier joint extension, 2026-09-07: hand-checked distinct-tuple
root bound, simultaneous padding, common-zero deletion and the SAME
evaluation kernel for all anchored components. The dimension is the
common polynomial space, not tuple affine dimension. `verify_joint_small.py`
exhaustively checks 49299 candidate tuples for 27 source/carrier/arity
cases over F_5, including common zeros and arities one through three.
It also confirms the actual F_17 MCA cross-core counterexample to an
uncharged outside-of-union conversion. Replay: 0.21 seconds, 11648 KiB.
The joint LIST extension is proved; the false MCA shortcut is not an
installed supplier. External mathematical review remains outstanding.

Hand checks: exact agreement subsets in Johnson; positive denominator;
injective same-field padding; no lost word at a common zero; actual affine
dimension versus ambient degree; scalar anchoring on the actual receiver.
The K=1 and zero-dimensional cases do not divide an impossible nonzero
direction space by a degree-one factor.

The consumer's independent transition checker recomputes each selected
bound without trusting the selector or its crossing search. A deliberately
lowered selected bound must be rejected. Numerical certificates instantiate
the theorem; the general proof does not rely on numerical survival.
External independent mathematical review remains due.
