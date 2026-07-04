# f_dim1 proof

Let `P = {ell_0 + t ell_1}` be a gcd-trivial pencil.

For each domain point `x`, the equation

```text
ell_0(x) + t ell_1(x) = 0
```

has at most one solution in `t`. If `ell_1(x) != 0`, the solution is
`t_x = -ell_0(x) / ell_1(x)`. If `ell_1(x) = 0`, then either `ell_0(x) != 0`
and there is no vote, or `ell_0(x) = 0`, which would make `x` a common root of
the whole pencil and contradict gcd-triviality.

Thus the `n` domain points cast at most `n` votes across pencil members. A
member of `D_j` needs at least `j` votes, so there are at most `floor(n / j)`
such members, up to the standard one point at infinity/leading-coefficient
degeneracy. This is polynomial with large room.
