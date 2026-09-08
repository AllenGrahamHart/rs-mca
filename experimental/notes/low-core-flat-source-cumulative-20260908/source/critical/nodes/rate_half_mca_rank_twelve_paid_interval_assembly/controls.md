# Focused Controls

No new large computation is needed. The existing actual F_23 rank-twelve
control in
background/nodes/rate_half_mca_error_rank_twelve_common_core_forcing/verify_core_transport.py
has 22 distinct labels, explanation rank eleven, three common evaluation
zeros and only two points in its complete shared core. Cancelling the two
shared points keeps ALL labels and affine error rank twelve. Removing
all three carrier-zero coordinates would lose one label. That distinction
is the exact source-transport issue resolved by this assembly.

The existing F_17 control in
background/nodes/mca_common_core_low_margin_transport/verify_small.py
checks 13 saturated full-bad records, all their raw minimizers, complete
pair cores and four relation spaces. Its unsaturated-support control
changes raw from two to one on reselection, preventing the false claim
that arbitrary old raw values must survive canonical child reselection.

Both were replayed under RAMguard tiny without optimization, retaining
their assertions: 0.10/0.03 seconds and 13312/10880 KiB peak RSS.
These are small controls, not formal proof certification.

The local verify.py checks the exact original-core interval partition,
its reversed child J intervals, the maximum of complete source bounds,
the field budget and residual endpoints. Its guards are explicit under
-O and reject boundary/budget mutations. No broad field or rank scan.
