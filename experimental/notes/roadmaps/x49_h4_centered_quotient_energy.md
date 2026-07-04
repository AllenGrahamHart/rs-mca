# X49: h=4 centered quotient-energy compression

- **DAG node:** `x49_h4_centered_quotient_energy`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved compressed accounting.
- **Verifier:** `experimental/scripts/verify_x49_h4_centered_quotient_energy.py`.
- **Certificate:**
  `experimental/data/certificates/x49-h4-centered-quotient-energy/x49_h4_centered_quotient_energy.json`.

## Statement

Let `m_C` be the X48 shell size attached to the quotient coset

```text
C = sH in F_p^*/H.
```

Then the X42 centered-energy bound compresses to

```text
R_centered <= n * sum_C C(m_C, 4).
```

Moreover

```text
sum_C m_C = (n-2)/2.
```

Consequently, with `M = max_C m_C`,

```text
R_centered <= (C(M,4)/M) * n(n-2)/2.
```

This is the quotient-coset form of X44's max-shell criterion, with the paid
zero-sum antipodal pairs removed before accounting.

## Proof

X42 proves

```text
R_centered <= sum_{s != 0} C(m_s,4).
```

X48 proves that `m_s` depends only on the quotient coset `C=sH`.  Each quotient
coset contains exactly `n` nonzero field elements, so

```text
sum_{s != 0} C(m_s,4) = n * sum_C C(m_C,4).
```

For the mass identity, every unordered pair `{x,y} subset H` has either:

```text
x+y = 0,
```

or contributes to exactly one nonzero pair-sum shell.  Since `n` is even, the
zero-sum unordered pairs are exactly

```text
{x,-x},        x in H,
```

and there are `n/2` of them.  Therefore

```text
sum_{s != 0} m_s = C(n,2) - n/2 = n(n-2)/2.
```

Dividing by the coset size `n` gives

```text
sum_C m_C = (n-2)/2.
```

Finally, `C(m,4)/m` is increasing for `m >= 4`, so

```text
sum_C C(m_C,4) <= (C(M,4)/M) sum_C m_C.
```

Multiplying by `n` proves the displayed max-shell bound.

## Consequence

The centered h=4 branch now has two equivalent row-certificate forms:

```text
X44 field-shell form:       max_s m_s
X49 quotient-coset form:    histogram of m_C over F_p^*/H
```

The quotient form is the more structural one.  It shows that the total
non-paid centered shell mass across all quotient cosets is only `(n-2)/2`, and
that the remaining task is controlling concentration of this mass into large
shifted-subgroup intersections.

## Replay

The verifier reads the X48 certificate and checks:

- the quotient mass identity `sum_C m_C = (n-2)/2`;
- `R_centered <= n sum_C C(m_C,4)`;
- the quotient max-shell bound dominates the quotient energy;
- all replay rows fit `n^3`.

The replay includes low-characteristic stress rows and boundary rows where
`M > 4`, so the compressed accounting is exercised nontrivially.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x49_h4_centered_quotient_energy.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x49_h4_centered_quotient_energy.py --write-certificate
```
