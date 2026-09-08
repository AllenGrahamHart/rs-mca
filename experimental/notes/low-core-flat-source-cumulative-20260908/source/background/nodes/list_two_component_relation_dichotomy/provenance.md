# Provenance

The scalar-tail continuation is a complete local derivation from
projection fibers and the RS root bound. It is compatible with the
classical erasure/branching viewpoint of Gopalan, Guruswami and
Raghavendra, [List Decoding Tensor Products and Interleaved Codes](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tensor-interleave.pdf),
section 2.2. That primary source was consulted for the distinction
between preserving decoding radius and controlling a finite list
budget. Its theorem is not an assumed scalar upper input, and no
novelty claim over its proof techniques is made. The mixed-radius
inequality used here is proved in full in scalar_tail_bound.md.

Local hand derivation on 2026-09-06, following the full LIST coefficient-
dimension compression and the scalar <=Q obstruction in this worktree.
The question was how to retain actual common-support codeword ownership
while separating scalar structure from the genuinely joint problem.

The complete proof is elementary and self-contained. It is not imported
from an unmerged PR and does not rely on numerical evidence. No claim of
priority over polynomial-relation or interleaved decoding literature is
made; an independent novelty/overlap review precedes upstream export.

Local overlap checks read the existing fixed-support defect Johnson,
inverse-ratio degree gate and deficient-window rational-direction
statements. Those concern fixed-support or MCA source charts; this
packet instead proves a worst-case identity for the full two-component
LIST count. Their payment constants and rank meanings are not imported.

Current upstream main checked during the cycle:
93fba1be3f3299b0ba4708d88715377bbb656e45. Its agents.md retains the
direct ordinary-list objective and requires correct codeword projection.
This is a candidate direct LIST reduction, not a claimed deployed Q,
balanced-core or list-interior upper payment. A fresh all-PR overlap
audit and independent proof review have not been performed.
