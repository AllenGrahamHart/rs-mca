# X60: h=4 linear-triple normal form

- **DAG node:** `x60_h4_linear_triple_form`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved exact normal form.
- **Verifier:** `experimental/scripts/verify_x60_h4_linear_triple_form.py`.
- **Certificate:**
  `experimental/data/certificates/x60-h4-linear-triple-form/x60_h4_linear_triple_form.json`.

## Statement

Let `H = mu_n`.  Twice the X56 anchored surplus is the number of solutions

```text
x + y - z = 1,        x,y,z in H,
```

avoiding the five trivial loci

```text
x = 1,
y = 1,
z = 1,
y = x,
y = -x.
```

Equivalently,

```text
2 A_anchor_surplus
  = #{(x,y,z) in H^3 :
      x+y-z=1,
      x != 1,
      y != 1,
      z != 1,
      y != x,
      y != -x }.
```

Thus the X55-X56 target is the linear-subgroup incidence bound

```text
#{filtered triples} < 8 * C(T(n)+1,2).
```

## Proof

Start from X59 and substitute

```text
x = h,
y = h r,
z = h(1+r)-1.
```

Since `h,r in H`, both `x` and `y` are in `H`; the X59 condition is precisely
`z in H`.  The defining equation becomes

```text
x + y - z = 1.
```

Conversely, any solution `(x,y,z) in H^3` of `x+y-z=1` gives

```text
h = x,
r = y/x,
```

and recovers the X59 Mobius condition.

The branch dictionary is:

```text
h = 1             <=> x = 1,
h = r^-1          <=> y = 1,
h = 2/(1+r)       <=> z = 1,
r = 1             <=> y = x,
r = -1            <=> y = -x.
```

Therefore X59's nontrivial Mobius count is exactly the filtered linear-triple
count above.  Since X59 proves that this count is `2 A_anchor_surplus`, the
claim follows.

## Consequence

The centered h=4 branch now has three equivalent proof targets:

```text
quotient shell surplus       (X56),
reduced additive energy      (X58),
filtered linear triples      (X60).
```

The linear form is the most standard additive-combinatorics presentation.  A
terminal proof may bound the number of subgroup triples on the affine plane

```text
x + y - z = 1
```

after removing the five forced loci above.

## Replay

The verifier replays the X59 rows and checks:

- the filtered linear count equals the X59 Mobius count;
- the filtered count is even;
- the zero-sum branch `y=-x` has exactly `n` raw points;
- the raw count splits into the excluded union plus the filtered locus.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x60_h4_linear_triple_form.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x60_h4_linear_triple_form.py --write-certificate
```
