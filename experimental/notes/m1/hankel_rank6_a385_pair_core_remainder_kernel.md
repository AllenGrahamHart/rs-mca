# Hankel Rank-6 A385 Pair-Core Remainder Kernel

Status: PROVED / AUDIT.

This note repackages the `A=385` no-fixed-core pair-core obstruction as a
polynomial remainder-kernel problem.

Use the notation from the Cauchy-moment note:

```text
P_X(T) = prod_{x in X} (T-x),        deg P_X = 128,
W_x = Omega_x/a_x.
```

Let `R(T)` be the unique degree-`<128` interpolant with

```text
R(x) = W_x        for x in X.
```

For a degree-`<5` auxiliary polynomial `Q`, the transferred locator is

```text
L_Q = Rem(R Q, P_X).
```

Indeed, both sides have degree `<128` and agree on every point of `X`.

Now let `E` be a common external root core and put

```text
C_E(T) = prod_{s in E} (T-s).
```

Define the linear map

```text
Phi_E : F[T]_{<5} -> F[T]/(C_E),
Phi_E(Q) = Rem(Rem(RQ,P_X), C_E).
```

Since `C_E` is squarefree and disjoint from `X`, evaluation on the roots of
`C_E` identifies `F[T]/(C_E)` with functions on `E`.  Therefore

```text
Q in ker Phi_E
```

is exactly the condition that `L_Q` vanishes on all of `E`.

Thus the pair-core rank test has the equivalent form

```text
dim ker Phi_E >= 2
```

or, since the source has dimension `5`,

```text
rank Phi_E <= 3.
```

For every `Q in ker Phi_E`, divisibility by `C_E` gives

```text
L_Q = C_E F_Q,        deg F_Q < 128-|E|.
```

Equivalently, before reducing modulo `P_X`, there is a correction polynomial
`T_Q` with

```text
R Q = C_E F_Q + P_X T_Q,
deg T_Q <= 3.
```

At the pressure-forced core size `|E|>=24`, this gives

```text
deg F_Q < 104.
```

For the two actual finite split-locator classes on the pair line, the quotient
reduction imposes the stronger split gate:

```text
deg F_Q = 103,
F_Q | (X^512-1)/C_E,
```

after normalization, plus finite noncontainment.

So the remaining frontier can be stated cleanly: a separated `A=385`
no-fixed-core over-budget survivor needs an external set `E` of size at least
`24` for which `Phi_E` has kernel dimension at least `2`, and two distinct
points of a kernel line pass the quotient-divisor and noncontainment gates.

The ambient-flexibility companion

```text
experimental/notes/m1/hankel_rank6_a385_pair_core_ambient_flexibility.md
```

shows that the kernel-dimension condition alone cannot close the branch: for
any 24-point external core and any chosen `Q`-line, there are nonzero base
weights making that line lie in `ker Phi_E`.  The remaining closure must use
the split-divisor, quotient-payment, noncontainment, or further Hankel-specific
gates.

Replay:

```sh
python3 experimental/scripts/verify_f17_32_m3_rank6_a385_pair_core_remainder_kernel.py \
  --check experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-remainder-kernel/f17_32_n512_k256_m3_rank6_a385_pair_core_remainder_kernel.json
```

Nonclaims:

```text
no closure of the no-fixed-core A=385 frontier;
no proof that dim ker Phi_E>=2 is impossible for |E|=24;
no proof that dim ker Phi_E>=2 is quotient-paid;
no proof that kernel points pass the split-locator divisor gate;
no finite noncontainment proof for kernel points;
no overlapping-support rank-6 classification;
no row-level M3 safe-side bound.
```
