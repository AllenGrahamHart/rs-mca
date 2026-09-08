# High-margin cores are not needed in the gluing hypothesis

Status: PROVED scope continuation, 2026-09-07.

Fix the same cutoff T used in the weighted resource. The proof needs a
projective polynomial combination only on a set U containing every
COMPLETE core of records with raw<=T. It uses no high-margin core:
high records enter solely through the global tuple resource, at weight
at least T+1. This is now explicit in statement.md and proof.md.

The smallest canonical such U is U_T, the union of low complete cores.
It supports the same local polynomial-section construction, with its own
received-pair defect c_T. A kernel on the full union restricts to U_T,
but the converse need not hold. The field, selected labels, supports,
minimizers and original resource remain unchanged.

## Strictness with unique minimizers

Over F_17 on D={0,...,12}, take K=2, d=3, m=5, T=1,
C'=span{1}, h_*=0, and

    u=(0,0,0,0,0,0,0,0,1,1,11,11,11),
    v=(0,0,0,0,1,1,1,1,16,9,2,2,2).

Choose these exact selected records:

    gamma=1: h=0, S={0,1,2,3,8},       b=0, raw=1;
    gamma=2: h=2, S={4,5,6,7,9},       b=1, raw=1;
    gamma=3: h=0, S={0,1,10,11,12},    b=2, raw=2.

Each minimizing b is UNIQUE among constants. Every support is
pair-noncontained: its v-values cannot be a degree-<2 polynomial.
The low complete cores are {0,1,2,3} and {4,5,6,7}, belonging to
pairs (0,0) and (0,1). The high pair (11,2) has core {10,11,12}.

On U_T={0,...,7}, u=0 while v is not degree-<2, so c_T=1 with
kernel (1,0). On the full union, a polynomial combination alpha*u+beta*v
would force beta=0 from the first eight coordinates, and then alpha=0
from the last three. Thus c_full=2. Swapping the received components
and inverting these nonzero slope labels gives an infinite-kernel example
with the same low/high margins and core unions.

This witnesses a genuine weakening of the gluing premise; it is not a
counterexample to any prize claim. The actual-field replay is
`rate_half_mca_received_pair_one_defect_payment/verify_low_core_localization.py`.
