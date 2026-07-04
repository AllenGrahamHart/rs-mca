# X58: h=4 reduced additive-energy normal form

- **DAG node:** `x58_h4_reduced_additive_energy`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved exact normal form.
- **Verifier:** `experimental/scripts/verify_x58_h4_reduced_additive_energy.py`.
- **Certificate:**
  `experimental/data/certificates/x58-h4-reduced-additive-energy/x58_h4_reduced_additive_energy.json`.

## Statement

Let `H = mu_n` in odd characteristic.  Define

```text
I = #{(a,b,c) in H^3 :
      a notin {1,-1},
      1+a = b+c},
```

and let

```text
D = #{a in H\{1,-1} : (1+a)/2 in H}.
```

Here `D` counts ordered diagonal targets `b=c`.  Let
`A_anchor_surplus` be the X56 anchored nonzero h=2 surplus.  Then

```text
A_anchor_surplus = (I - D - 2(n-2)) / 2.
```

Equivalently, X56's target is a reduced shifted-additive-energy bound: after
subtracting the two ordered copies of the source pair `{1,a}` and the diagonal
targets, the remaining ordered incidence must be below twice the X56 barrier.

## Proof

Fix an anchor `a in H\{1,-1}` and put

```text
s = 1+a.
```

The ordered target pairs `(b,c) in H^2` with `b+c=s` split into three classes.

First, the source pair itself contributes exactly two ordered pairs:

```text
(b,c) = (1,a), (a,1).
```

Second, there may be one diagonal target

```text
b=c=s/2,
```

which is not an h=2 target subset.

Third, every valid disjoint unordered target pair `{b,c}` contributes exactly
two ordered pairs `(b,c)` and `(c,b)`.  In a nonzero shell, a target sharing
one element with `{1,a}` must be the source pair itself, so no additional
overlap correction is needed.

Therefore, for this anchor,

```text
# valid disjoint unordered targets
  = (D_s - delta_s - 2) / 2,
```

where `D_s = #{(b,c) in H^2 : b+c=s}` and `delta_s` is `1` when `s/2 in H`.
Summing over the `n-2` anchors gives

```text
A_anchor_surplus = (I - D - 2(n-2)) / 2.
```

## Consequence

The h=4 centered terminal subproblem can now be stated without h=4 language:
prove that the shifted subgroup incidence

```text
I = #{(a,b,c) in H^3 : a notin {1,-1}, 1+a=b+c}
```

is only trivially larger than

```text
D + 2(n-2).
```

X55-X56 require

```text
I - D - 2(n-2) < 8 * C(T(n)+1,2).
```

This isolates the remaining nontrivial content as a reduced additive-energy
or p-specific norm-gate surplus bound.

## Replay

The verifier replays the X56 rows by directly counting ordered pair sums in
`H` and checks:

- the reduced ordered incidence is even;
- `(I - D - 2(n-2))/2` equals the X56 anchored surplus;
- the diagonal correction satisfies `0 <= D <= n-2`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x58_h4_reduced_additive_energy.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x58_h4_reduced_additive_energy.py --write-certificate
```
