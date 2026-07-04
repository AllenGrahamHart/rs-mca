# X37: h=4 quartic-fiber form

- **DAG node:** `x37_h4_quartic_fiber_form`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved reduction.
- **Verifier:** `experimental/scripts/verify_x37_h4_quartic_fiber_form.py`.
- **Certificate:**
  `experimental/data/certificates/x37-h4-quartic-fiber-form/x37_h4_quartic_fiber_form.json`.

## Statement

Let `P,Q` be disjoint 4-subsets of a field, and let

```text
L_P(X)=prod_{a in P}(X-a),       L_Q(X)=prod_{b in Q}(X-b).
```

Then

```text
e_1(P)=e_1(Q), e_2(P)=e_2(Q), e_3(P)=e_3(Q)
```

if and only if `P` and `Q` are two completely split fibers of the same monic
quartic:

```text
L_P(x)=0       for x in P,
L_P(y)=c       for y in Q,
```

where

```text
c = e_4(P)-e_4(Q).
```

If `P` and `Q` are disjoint and the top-three coefficients agree, then
`c != 0`.

## Proof

Write

```text
L_P(X)=X^4-e_1(P)X^3+e_2(P)X^2-e_3(P)X+e_4(P),
L_Q(X)=X^4-e_1(Q)X^3+e_2(Q)X^2-e_3(Q)X+e_4(Q).
```

If the first three elementary symmetric sums agree, then

```text
L_Q(X) = L_P(X) + e_4(Q)-e_4(P).
```

For every `y in Q`, `L_Q(y)=0`, hence

```text
L_P(y)=e_4(P)-e_4(Q)=c.
```

Conversely, if every `y in Q` has the same value `L_P(y)=c`, then the monic
quartic `L_P(X)-c` has the four roots `Q`.  Therefore

```text
L_Q(X)=L_P(X)-c,
```

so the top three coefficients agree.

Finally, if `c=0`, then `L_P=L_Q`; as monic split polynomials this implies
`P=Q`, contradicting disjointness.  Thus a disjoint h=4 trade has nonzero
fiber separation.

## Consequence

Together with X35, the h=4 residue has two equivalent forms:

```text
signed 4+4 sparse word with moments 1,2,3 zero,
degree-4 map with two split H-fibers.
```

The paid cyclic and dihedral cases are quartic pullback fibers.  Any remaining
top-level branch is a primitive quartic with two completely split `mu_n`
fibers.

## Checks

The verifier records:

- the `mu_4` baseline as two fibers of `X^4-a`;
- an antipodal quotient extra as two fibers of the lifted quartic;
- a top-level first-sum-only nontrade where the four `Q` values under `L_P`
  are not constant;
- a full tiny exhaustion over all disjoint h=4 pairs in `F_257 / mu_16`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x37_h4_quartic_fiber_form.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x37_h4_quartic_fiber_form.py --write-certificate
```
