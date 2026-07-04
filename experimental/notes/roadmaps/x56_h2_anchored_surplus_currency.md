# X56: h=2 anchored surplus currency

- **DAG node:** `x56_h2_anchored_surplus_currency`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved exact currency conversion.
- **Verifier:** `experimental/scripts/verify_x56_h2_anchored_surplus_currency.py`.
- **Certificate:**
  `experimental/data/certificates/x56-h2-anchored-surplus-currency/x56_h2_anchored_surplus_currency.json`.

## Statement

X54 counts centered h=4 shell surplus in unanchored shell-pair currency:

```text
N_surplus = n * sum_C C(m_C, 2).
```

The h=2 rung is normally stated in anchored currency.  Define the anchored
nonzero h=2 surplus

```text
A_anchor_surplus
  = #{ (a, {b,c}) :
       a in H \ {1,-1},
       {b,c} subset H,
       {b,c} cap {1,a} = empty,
       1+a = b+c }.
```

Then

```text
A_anchor_surplus = 4 * sum_C C(m_C, 2),
N_surplus = (n/4) * A_anchor_surplus.
```

Consequently X55's unanchored barrier

```text
N_surplus < n * C(T(n)+1, 2)
```

is equivalent to the anchored target

```text
A_anchor_surplus < 4 * C(T(n)+1, 2).
```

## Proof

For a fixed anchored source pair `{1,a}` with `a != 1,-1`, put

```text
s = 1+a.
```

Then `{1,a}` is one pair in the nonzero shell `S_s`.  By X54, distinct pairs
in one nonzero shell are automatically disjoint.  Hence the number of
admissible target pairs `{b,c}` for this source is exactly

```text
m_s - 1.
```

Summing over anchors gives

```text
A_anchor_surplus = sum_{a in H\{1,-1}} (m_{1+a} - 1).
```

Now group the anchors by quotient coset `C = (1+a)H`.  X48 says

```text
m_C = (1/2) #{ a in H\{1} : 1+a in C }.
```

Since `C` is nonzero, `a=-1` is absent automatically.  Thus each quotient
coset contributes

```text
2 m_C (m_C - 1) = 4 C(m_C, 2)
```

to `A_anchor_surplus`.  Therefore

```text
A_anchor_surplus = 4 * sum_C C(m_C,2).
```

X54 gives

```text
N_surplus = n * sum_C C(m_C,2),
```

so

```text
4 N_surplus = n A_anchor_surplus.
```

The equivalence of X55's unanchored barrier and the anchored barrier follows
by multiplying the strict inequality by `4/n`.

## Consequence

This packet removes a convention ambiguity.  The proved h=2 rung

```text
A_2^nt <= 6 n^(5/3)
```

does **not** itself imply X55, because X55 requires the anchored surplus
subcount to satisfy

```text
A_anchor_surplus < 4 * C(T(n)+1,2) ~= n^(2/3).
```

The verifier checks this comparison exactly on the X55 threshold rows.  The
general `6 n^(5/3)` total h=2 line-bound scale is above the X55 anchored
target on every recorded row.  The prime-field `2 n^(5/3)` scale has one
tiny-row exception at `n=16`, and is above the X55 anchored target from
`n=32` onward, including all large rows.  Therefore the remaining h=4
centered proof needs a genuinely p-specific norm-gate surplus exclusion or a
stronger distribution theorem, not just the existing h=2 line theorem.

## Replay

The certificate replays the X48, X54, and X55 rows and checks:

- `4*N_surplus = n*A_anchor_surplus`;
- the X55 barriers convert by the same identity;
- the surplus condition is invariant under the two currencies;
- the low-characteristic stress row that fails the sufficient X55 barrier is
  still recorded as a no-claim row, not a contradiction.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x56_h2_anchored_surplus_currency.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x56_h2_anchored_surplus_currency.py --write-certificate
```
