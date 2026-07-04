# X61: h=4 linear degeneracy ledger

- **DAG node:** `x61_h4_linear_degeneracy_ledger`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved degeneracy ledger and diagonal-line affordability.
- **Verifier:** `experimental/scripts/verify_x61_h4_linear_degeneracy_ledger.py`.
- **Certificate:**
  `experimental/data/certificates/x61-h4-linear-degeneracy-ledger/x61_h4_linear_degeneracy_ledger.json`.

## Statement

For the linear equation

```text
x + y - z - 1 = 0,        x,y,z in H,
```

the only proper vanishing subsum degeneracies are

```text
x = 1,
y = 1,
y = -x.
```

The two additional X60 exclusions

```text
y = x,
z = 1
```

are not S-unit degeneracies.  They are source-overlap/diagonal line branches,
and each has size

```text
D + 1,
```

where `D` is the X58 diagonal correction

```text
D = #{a in H\{1,-1} : (1+a)/2 in H}.
```

Moreover, the existing h=2 fixed-line input bounds each such branch by

```text
12 n^(2/3) + 1,
```

which is below the X60 barrier

```text
8 * C(T(n)+1,2)
```

on every X50 threshold-table row.

## Proof

View the equation as the four-term S-unit equation

```text
x + y - z - 1 = 0.
```

No one-term subsum can vanish because `H subset F^*`.  Two-term vanishing
subsum possibilities are:

```text
x - 1 = 0      <=> x = 1,
y - 1 = 0      <=> y = 1,
x + y = 0      <=> y = -x,
x - z = 0      <=> x = z,
y - z = 0      <=> y = z,
-z - 1 = 0     <=> z = -1.
```

On the full equation, `x=z` forces `y=1`, `y=z` forces `x=1`, and `z=-1`
forces `y=-x`.  Thus the degeneracy union is exactly

```text
x = 1  or  y = 1  or  y = -x.
```

The branch `y=x` gives

```text
z = 2x - 1.
```

Writing `a=z`, this is counted by `D`, plus the point `x=y=z=1`; hence it has
size `D+1`.  The branch `z=1` gives

```text
x + y = 2.
```

The point `(1,1,1)` contributes the `+1`, and the remaining solutions are
parametrized by

```text
a = x/y,        (1+a)/2 = 1/y in H,
```

so this branch also has size `D+1`.

Finally, `D+1` is a fixed-line intersection count for a translate of `H`:

```text
2u - a = 1,        a,u in H.
```

The proved h=2 line input gives `D <= 12 n^(2/3)`.  The verifier checks the
integer comparison

```text
12 n^(2/3) + 1 < 8 * C(T(n)+1,2)
```

by cubing the stricter sufficient inequality

```text
1728 n^2 < (8*C(T(n)+1,2)-1)^3.
```

## Consequence

If a future proof imports a nondegenerate S-unit or finite-field linear
subgroup theorem for

```text
x + y - z - 1 = 0,
```

the three true S-unit degeneracies are already exactly identified, and the two
extra X60 branches are affordable by the existing h=2 line bound.  Thus the
remaining centered h=4 obstruction is precisely the nondegenerate linear
triple count.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x61_h4_linear_degeneracy_ledger.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x61_h4_linear_degeneracy_ledger.py --write-certificate
```
