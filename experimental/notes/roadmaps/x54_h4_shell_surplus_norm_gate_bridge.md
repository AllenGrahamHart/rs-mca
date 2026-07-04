# X54: h=4 shell-surplus norm-gate bridge

- **DAG node:** `x54_h4_shell_surplus_norm_gate_bridge`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved accounting bridge.
- **Verifier:** `experimental/scripts/verify_x54_h4_shell_surplus_norm_gate_bridge.py`.
- **Certificate:**
  `experimental/data/certificates/x54-h4-shell-surplus-norm-gate-bridge/x54_h4_shell_surplus_norm_gate_bridge.json`.

## Statement

Let `H = mu_n` and let

```text
S_s = {{x,y} subset H : x+y=s},      s != 0,
m_s = |S_s|.
```

Then every unordered choice of two distinct pairs in `S_s` is a nonzero h=2
pair-sum collision.  Distinct pairs in one shell are automatically disjoint.
By X41, every such collision is non-`Phi_n`-descended and is a sparse h=2
norm gate.

Therefore the centered shell-surplus norm-gate count is exactly

```text
N_surplus = sum_{s != 0} C(m_s, 2).
```

By X48 and X52, `m_s` is constant on multiplicative `H`-cosets.  If `m_C` is
the shell size attached to the quotient coset `C=sH`, then

```text
N_surplus = n * sum_C C(m_C, 2).
```

## Proof

If two unordered pairs in one nonzero shell share an element, say

```text
{x,y}, {x,z} subset S_s,
```

then

```text
x+y = s = x+z,
```

so `y=z`.  Thus distinct shell pairs are disjoint.

For every unordered two-choice

```text
{{x,y}, {u,v}} subset S_s,
```

we have

```text
x+y = u+v = s != 0.
```

This is exactly a nonzero h=2 pair-sum collision.  X41 proves that any such
finite-field nonzero collision cannot descend from characteristic zero and
therefore has

```text
p | Res(Phi_n, X^a + X^b - X^c - X^d)
```

after writing the four elements as powers of a primitive `n`-th root.  Hence
each contributes one sparse norm-gate collision in the h=2 pair-sum layer.

Conversely, any nonzero h=2 pair-sum collision is a choice of two distinct
pairs in one nonzero shell.  This gives the exact count

```text
sum_{s != 0} C(m_s,2).
```

The quotient compression follows from X48/X52: every nonzero quotient coset
contains `n` field elements, and all `s` in the same coset have the same shell
size.

## Relation To Centered h=4 Energy

X42 bounds centered h=4 trades by

```text
R_centered <= sum_{s != 0} C(m_s,4).
```

X54 records the lower-degree ledger sitting underneath this energy:

```text
N_surplus = sum_{s != 0} C(m_s,2).
```

Thus any large centered h=4 shell must first appear as a large concentration
of h=2 sparse norm gates in one quotient-coset shell.  A row with max shell
`M` already contains at least

```text
n * C(M,2)
```

such surplus norm-gate collisions across the corresponding quotient coset.

## Replay

The verifier reads the X48 certificate and checks for each replay row:

- direct `sum_s C(m_s,2)` equals `n sum_C C(m_C,2)`;
- direct quartic shell energy equals `n sum_C C(m_C,4)`;
- the maximum shell forces at least `n C(M,2)` surplus collisions;
- rows with quartic centered energy also have nonzero quadratic surplus.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x54_h4_shell_surplus_norm_gate_bridge.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x54_h4_shell_surplus_norm_gate_bridge.py --write-certificate
```
