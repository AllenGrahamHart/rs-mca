# A385 Pair-Core Remainder Kernel

This packet repackages the `A=385` no-fixed-core pair-core obstruction as a
kernel problem for a polynomial remainder map.

Let `R` be the degree-`<128` interpolant with `R(x)=Omega_x/a_x` on the base
support `X`, and let `C_E` be the external-core polynomial.  Then

```text
L_Q = Rem(RQ,P_X),
Phi_E(Q)=Rem(Rem(RQ,P_X),C_E).
```

The pair-core rank condition is equivalent to

```text
dim ker Phi_E >= 2.
```

For every kernel vector,

```text
RQ = C_E F_Q + P_X T_Q,
deg F_Q < 128-|E|,        deg T_Q <= 3.
```

At the pressure-forced size `|E|>=24`, the two actual split members must have
exact quotient degree `103` and divide `(X^512-1)/C_E`.

Replay:

```sh
python3 experimental/scripts/verify_f17_32_m3_rank6_a385_pair_core_remainder_kernel.py \
  --check experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-remainder-kernel/f17_32_n512_k256_m3_rank6_a385_pair_core_remainder_kernel.json
```
