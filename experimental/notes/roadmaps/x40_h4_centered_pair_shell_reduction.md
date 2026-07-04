# X40: h=4 centered pair-shell reduction

- **DAG node:** `x40_h4_centered_pair_shell_reduction`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved reduction plus finite evidence.
- **Verifier:** `experimental/scripts/verify_x40_h4_centered_pair_shell_reduction.py`.
- **Certificate:**
  `experimental/data/certificates/x40-h4-centered-pair-shell-reduction/x40_h4_centered_pair_shell_reduction.json`.

## Statement

The nonzero-centered branch isolated by X39 reduces to an h=2 collision inside
one pair-sum shell.

Let `H = mu_n`, let `s != 0`, and consider unordered pairs

```text
{x,y} subset H,        x+y=s.
```

Write their product as

```text
u = xy.
```

Any h=4 support even around the center `c=s/2` is exactly a union of two such
pairs.  If the two pair products are `u` and `v`, then the top-three
elementary symmetric sums of the four roots are

```text
e_1 = 2s,
e_2 = s^2 + u + v,
e_3 = s(u+v).
```

Therefore, for fixed nonzero `s`, two centered h=4 supports have equal
top-three coefficients if and only if their pair-product sums agree:

```text
u_1+u_2 = u_3+u_4.
```

Thus the named residue from X39,

```text
h4_centered_power_affine_residue,
```

is precisely a same-sum collision among pair products inside a fixed nonzero
pair-sum shell.

## Proof

A support even around `c` is stable under the reflection

```text
x -> 2c-x.
```

Putting `s=2c`, its roots split into two unordered pairs

```text
{x, s-x},        {y, s-y}.
```

Let their products be

```text
u=x(s-x),        v=y(s-y).
```

The locator factors as

```text
(X^2-sX+u)(X^2-sX+v)
  = X^4 - 2sX^3 + (s^2+u+v)X^2 - s(u+v)X + uv.
```

Comparing with

```text
X^4-e_1X^3+e_2X^2-e_3X+e_4
```

gives the displayed formula.  When `s != 0`, the pair `(e_2,e_3)` contains
exactly the same information as `u+v`, so equality of the top three
coefficients for two supports with the same center is equivalent to equality
of their pair-product sums.

Disjointness of the h=4 trade is the disjointness of the two chosen two-pair
unions.  This proves the reduction.

The excluded shell `s=0` is the zero-center antipodal/cyclic branch already
paid by X38 and the quotient ledger.

## Finite Evidence

The verifier audits pair-sum shells directly, without enumerating all h=4
signatures.  In the checked rows it finds many nonzero-centered even supports
but no same-product-sum disjoint pair of such supports:

```text
n=32,  alpha=2 and 3
n=64,  alpha=2 and 3
n=128, alpha=2 and 3
n=256, alpha=2
```

This is evidence, not a uniform proof of emptiness.  The proved content is the
exact reduction to the pair-product h=2 shell problem.

## Consequence

After X39 and X40, the h=4 primitive affine-line residue is no longer a
quartic map problem.  It is the concrete pair-shell statement:

```text
For every nonzero s, products xy from pairs x+y=s in H have no disjoint
2-sum collision after the paid shells are removed.
```

This is a smaller target for either a proof or a row-local certifier.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x40_h4_centered_pair_shell_reduction.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x40_h4_centered_pair_shell_reduction.py --write-certificate
```
