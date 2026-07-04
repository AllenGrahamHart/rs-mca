# X59: h=4 Mobius collision normal form

- **DAG node:** `x59_h4_mobius_collision_form`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved exact normal form.
- **Verifier:** `experimental/scripts/verify_x59_h4_mobius_collision_form.py`.
- **Certificate:**
  `experimental/data/certificates/x59-h4-mobius-collision-form/x59_h4_mobius_collision_form.json`.

## Statement

Let `H = mu_n`.  The X56 anchored surplus equals

```text
A_anchor_surplus
  = (1/2) * #{(r,h) :
              r in H\{1,-1},
              h in H,
              h(1+r)-1 in H,
              h notin {1,r^-1,2/(1+r)}}.
```

Thus X55-X56 require the nontrivial Mobius collision count

```text
N_Mob = #{(r,h) :
          r in H\{1,-1},
          h in H,
          h(1+r)-1 in H,
          h notin {1,r^-1,2/(1+r)}}
```

to satisfy

```text
N_Mob < 8 * C(T(n)+1,2).
```

## Proof

Fix an anchor ratio `r in H\{1,-1}`.  A target unordered pair lies in the same
nonzero pair-sum shell as `{1,r}` exactly when one of its ordered ratios `t`
satisfies

```text
1+t in (1+r)H.
```

Equivalently, for some `h in H`,

```text
1+t = h(1+r),
t = h(1+r)-1.
```

The source pair `{1,r}` appears twice in ordered-ratio form:

```text
t = r      when h = 1,
t = r^-1   when h = r^-1.
```

The diagonal target appears as the ordered ratio

```text
t = 1      when h = 2/(1+r),
```

provided this value of `h` lies in `H`.  After excluding the two source ratios
and this possible diagonal ratio, every valid disjoint unordered target pair
contributes exactly two ordered ratios, `t` and `t^-1`.  Therefore the
anchored surplus for this `r` is half the number of remaining Mobius
collisions.  Summing over all anchors proves the formula.

## Consequence

X58 states the target as reduced shifted additive energy.  X59 gives the
equivalent multiplicative-surface form:

```text
h(1+r)-1 in H.
```

This is the cleanest p-specific norm-gate object left by the centered h=4
branch.  A proof can now attack the number of nontrivial subgroup points on
the two-dimensional correspondence

```text
(r,h) -> h(1+r)-1
```

rather than h=4 support families or quotient shell buckets.

## Replay

The verifier replays the X56 rows and checks:

- the `h=1` branch contributes exactly one source ratio per anchor;
- the `h=r^-1` branch contributes exactly one inverse source ratio per anchor;
- the `h=2/(1+r)` branch is the diagonal correction from X58;
- the remaining Mobius collision count is even;
- half of it equals the X56 anchored surplus.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x59_h4_mobius_collision_form.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x59_h4_mobius_collision_form.py --write-certificate
```
