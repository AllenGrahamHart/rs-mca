# X35: h=4 power-sum gate

- **DAG node:** `x35_h4_power_sum_gate`.
- **Consumers:** `active_core_count_bound`, `x4b_moment_trade_exclusion`.
- **Status:** proved reduction.
- **Verifier:** `experimental/scripts/verify_x35_h4_power_sum_gate.py`.
- **Certificate:**
  `experimental/data/certificates/x35-h4-power-sum-gate/x35_h4_power_sum_gate.json`.

## Statement

Let `P,Q` be disjoint 4-subsets in a field of characteristic `p > 3`.  Then

```text
e_i(P) = e_i(Q),        i=1,2,3
```

if and only if the first three power sums agree:

```text
sum_{x in P} x^r = sum_{y in Q} y^r,        r=1,2,3.
```

For exponent patterns in `mu_n`, this means the X33 h=4 common-gcd gate

```text
gcd(Phi_n, E_1, E_2, E_3)
```

is equivalent to the signed sparse moment gate

```text
gcd(Phi_n, S_1, S_2, S_3),

S_r(X) = sum_{a in P} X^{r a} - sum_{b in Q} X^{r b}.
```

Thus the h=4 top-level residue is exactly a signed `4+4` sparse word whose
moments `1,2,3` vanish.

## Proof

Newton identities for a 4-set give:

```text
p_1 = e_1,
p_2 = e_1 p_1 - 2 e_2,
p_3 = e_1 p_2 - e_2 p_1 + 3 e_3.
```

Since `2` and `3` are invertible, the first three elementary symmetric sums
determine and are determined by the first three power sums:

```text
e_1 = p_1,
e_2 = (e_1 p_1 - p_2)/2,
e_3 = (p_3 - e_1 p_2 + e_2 p_1)/3.
```

Apply these identities to `P` and `Q`.  Equality of `e_1,e_2,e_3` is therefore
equivalent to equality of `p_1,p_2,p_3`.

At the row level, a Galois scaling by `u in (Z/nZ)^*` evaluates the signed
power-sum word at `zeta^u`:

```text
S_r(zeta^u) =
  sum_{a in P} zeta^{u r a}
  -
  sum_{b in Q} zeta^{u r b}.
```

So the existence of a primitive-root scaling satisfying the h=4 equations is
equivalent to a positive-degree common gcd of `Phi_n` and `S_1,S_2,S_3`.

## Consequence

X32 and X33 reduced the first campaign trade size to a top-level h=4 norm-gate
certifier.  X35 identifies that certifier with the same sparse moment language
used by `x4b_moment_trade_exclusion`:

```text
signed 8-sparse word, moments 1,2,3 vanish.
```

The difference from U2's 0/1 block language is that here the support is signed
and balanced as `4+4`.  The same resultant/common-gcd architecture applies.

## Finite Cross-Check

The verifier compares the elementary-gcd and power-sum-gcd gates on every
selected top-level first-sum pattern in the two small rows used by X33/X34:

```text
row             checked top-level patterns     degree-pair histogram
---------------------------------------------------------------------
F257 / mu16                  712               {(0,0): 712}
F4993 / mu32               19860               {(0,0): 19860}
```

No mismatch occurs.

## What Remains

The h=4 top-level branch can now be attacked as:

```text
exclude signed 8-sparse 3-null words outside the paid antipodal quotient branch,
or certify/count them per row as a moment/norm-gate column.
```

That is the h=4 specialization of the broader `x4b_moment_trade_exclusion`
problem.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x35_h4_power_sum_gate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x35_h4_power_sum_gate.py --write-certificate
```
