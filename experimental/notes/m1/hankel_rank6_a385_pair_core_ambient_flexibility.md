# Hankel Rank-6 A385 Pair-Core Ambient Flexibility

Status: PROVED / AUDIT.

This note records a route cut for the `A=385` no-fixed-core pair-core program.
The rank/remainder-kernel condition is not by itself restrictive enough when
the base weights are arbitrary nonzero weights.

Fix a 24-point external core `E` and a projective `Q`-line `P(U)` inside the
five-dimensional degree-`<5` `Q`-space.  Choose a basis `Q0,Q1` of `U`.
The conditions

```text
L_Q0(s)=0,        L_Q1(s)=0        for every s in E
```

are homogeneous linear equations in the base weights `W_x=Omega_x/a_x` on
`X`.  There are at most

```text
2 * 24 = 48
```

constraints on

```text
|X| = 128
```

variables, so the solution space has dimension at least `80`.

The key point is that this solution space contains a vector with every base
weight nonzero.  No coordinate `W_x0` is forced to vanish.  If the coordinate
vector at `x0` lay in the rowspace of the constraints, then after clearing the
external denominators over

```text
C_E(T)=prod_{s in E}(T-s),
```

one would get a numerator of degree at most

```text
|E|-1 + 4 = 27
```

vanishing on all `127` points of `X \ {x0}` but not at `x0`, impossible.

Thus the solution space is not contained in any coordinate-zero hyperplane.
Since

```text
|F_17^32| > 128,
```

the union of the 128 proper coordinate-zero hyperplane sections cannot cover
the solution space.  Hence there are solutions with all `W_x` nonzero.

Consequently, for any 24-point external core and any chosen `Q`-line, the
ambient linear transfer can be made to satisfy

```text
dim ker Phi_E >= 2.
```

This is not a bad-slope construction: it does not impose the split-locator
divisor gate, quotient payment, or finite noncontainment.  Its purpose is to
show that the no-fixed-core branch cannot be closed by proving the rank-`<=3`
condition impossible at the level of arbitrary nonzero base weights.  The next
closure attempt must use the split/divisor gates or a genuinely Hankel-specific
constraint beyond this ambient linear system.

Replay:

```sh
python3 experimental/scripts/verify_f17_32_m3_rank6_a385_pair_core_ambient_flexibility.py \
  --check experimental/data/certificates/hankel-f17-32-m3-rank6-a385-pair-core-ambient-flexibility/f17_32_n512_k256_m3_rank6_a385_pair_core_ambient_flexibility.json
```

Nonclaims:

```text
no split-locator bad slope construction;
no proof that the no-fixed-core A=385 frontier is nonempty;
no quotient-divisor gate;
no finite noncontainment;
no closure or refutation of the full no-fixed-core A=385 branch;
no overlapping-support rank-6 classification;
no row-level M3 safe-side bound.
```
