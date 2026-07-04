# X42: h=4 centered energy accounting

- **DAG node:** `x42_h4_centered_energy_accounting`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved accounting plus finite evidence.
- **Verifier:** `experimental/scripts/verify_x42_h4_centered_energy_accounting.py`.
- **Certificate:**
  `experimental/data/certificates/x42-h4-centered-energy-accounting/x42_h4_centered_energy_accounting.json`.

## Statement

For each nonzero pair-sum shell

```text
S_s = {{x,y} subset H : x+y=s},        s != 0,
```

let

```text
U_s = {xy : {x,y} in S_s}.
```

Then products are distinct inside a shell.  Centered h=4 trades with center
`s/2` are exactly additive two-sum collisions among unordered pairs of
elements of `U_s`, with disjoint pair indices.

Consequently, if

```text
m_s = |S_s| = |U_s|,
```

then the shell contributes at most

```text
C(m_s,4)
```

centered h=4 trades, and the whole centered affine branch satisfies the
accounting bound

```text
R_centered <= sum_{s != 0} C(m_s,4).
```

## Proof

Distinctness of products is immediate: two unordered pairs with the same sum
`s` and the same product `u` are the two roots of the same quadratic

```text
T^2 - sT + u.
```

So they are the same unordered pair.

By X40, a centered h=4 support in the shell is a choice of two distinct shell
pairs, with product sum

```text
u_i + u_j.
```

Two such supports have equal top-three locator coefficients if and only if
their product sums agree.  Since distinct pairs in a fixed shell are disjoint
unless they are equal, disjointness of the two h=4 supports is exactly
disjointness of the two chosen index pairs.

Thus the exact count in shell `s` is

```text
#{ {{i,j},{k,l}} :
     i,j,k,l distinct and u_i+u_j = u_k+u_l }.
```

For any four distinct products, there are three partitions into two unordered
pairs.  In odd characteristic, at most one partition can have equal sums:
if

```text
u_1+u_2 = u_3+u_4
u_1+u_3 = u_2+u_4,
```

then `2(u_2-u_3)=0`, so `u_2=u_3`, contradicting distinctness.  Hence each
four-subset of `U_s` contributes at most one centered trade, proving

```text
R_s <= C(m_s,4).
```

Summing over nonzero shells gives the stated bound.

## Finite Evidence

The verifier computes the exact shell energy and the `sum C(m_s,4)` bound.
It includes low-characteristic stress rows where the centered residue is
nonzero, and campaign-boundary rows where the centered residue remains empty.

Checked campaign rows:

```text
n=32,  alpha=2
n=64,  alpha=2
n=128, alpha=2 and 3
n=256, alpha=2
```

In these rows the exact centered trade count is zero.  The shell bound also
fits the rewired `n^3` terminal column in every checked campaign row.

## Consequence

X42 turns the centered affine branch into a small energy certificate:

```text
compute shell sizes m_s and pair-product two-sum buckets.
```

No h=4 support sorting is needed.  Together with X41, any nonzero mass in this
branch is p-specific h=2 norm-gate mass, priced by the explicit shell energy
above.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x42_h4_centered_energy_accounting.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x42_h4_centered_energy_accounting.py --write-certificate
```
