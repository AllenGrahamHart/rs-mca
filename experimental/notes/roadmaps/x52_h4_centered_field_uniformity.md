# X52: h=4 centered field uniformity

- **DAG node:** `x52_h4_centered_field_uniformity`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved field-uniform extension of X48-X50.
- **Verifier:** `experimental/scripts/verify_x52_h4_centered_field_uniformity.py`.
- **Certificate:**
  `experimental/data/certificates/x52-h4-centered-field-uniformity/x52_h4_centered_field_uniformity.json`.

## Statement

Let `F` be any field of odd characteristic and let `H <= F^*` be a cyclic
subgroup of even order `n`.  For `s != 0`, define

```text
m_s = #{{x,y} subset H : x+y=s}.
```

Then

```text
m_s = (1/2) #{ r in H \ {1} : 1+r in sH }.
```

Consequently `m_s` depends only on the quotient coset `sH in F^*/H`.

If `F = F_q` is finite and `n | q-1`, then the `n`-th power map

```text
F_q^* -> F_q^*,       z -> z^n
```

has kernel `H`.  Thus quotient cosets can be represented by `s^n`, and the
X49 quotient-energy accounting and X50 threshold are field-uniform:

```text
R_centered <= n sum_C C(m_C,4),
sum_C m_C = (n-2)/2,
R_centered <= (C(M,4)/M) * n(n-2)/2.
```

In particular, the X50 condition

```text
(M-1)(M-2)(M-3)(n-2) <= 48 n^2
```

closes the centered h=4 branch over `F_q` just as it does over prime fields.

## Proof

The ratio argument from X48 is field-theoretic.  For an ordered pair
`(x,y) in H^2` with `x != y` and `x+y=s`, put

```text
r = x/y.
```

Then `r in H`, `r != 1`, and

```text
1+r = (x+y)/y = s/y in sH.
```

Conversely, if `r in H \ {1}` and `1+r in sH`, choose `y in H` with

```text
1+r = s/y.
```

Then `x=ry` lies in `H`, `x != y`, and `x+y=s`.  This is a bijection between
ordered distinct pairs with sum `s` and the displayed ratio set.  Passing to
unordered pairs divides by two.

For finite fields, `F_q^*` is cyclic.  Since `H` has order `n` and `n | q-1`,
the kernel of `z -> z^n` is exactly `H`.  Therefore two nonzero elements are
in the same `H`-coset exactly when their `n`-th powers agree.

The X49 mass identity is also field-uniform.  The nonzero pair-sum shells
partition all unordered pairs in `H` except the zero-sum antipodal pairs
`{x,-x}`.  Since `n` is even, there are `n/2` such pairs, so

```text
sum_{s != 0} m_s = C(n,2) - n/2 = n(n-2)/2.
```

Each quotient coset contains `n` nonzero field elements, so

```text
sum_C m_C = (n-2)/2.
```

The rest is X49-X50 verbatim.

## Extension Checks

The verifier replays the quotient-shell identities in quadratic extension
fields where the subgroup is not contained in the prime field:

```text
GF(25)  / mu_8
GF(49)  / mu_16
GF(121) / mu_24
```

For each row it checks:

- the subgroup has order `n` and is not prime-field-contained;
- the `n`-th power kernel is exactly `H`;
- direct pair-sum shell sizes are constant on quotient cosets;
- quotient shell mass is `(n-2)/2`;
- quotient ratio counts are twice shell sizes;
- X49's quotient energy equals the direct shell energy;
- the measured shell maximum satisfies X50's threshold.

## Consequence

The centered h=4 branch no longer has a prime-field caveat.  Its remaining
uniform input is exactly the same shifted-subgroup concentration target over
`F_q^*/H`:

```text
max_C #{ r in H \ {1} : 1+r in C } <= 2T(n).
```

## Verification

Run:

```bash
python3 experimental/scripts/verify_x52_h4_centered_field_uniformity.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x52_h4_centered_field_uniformity.py --write-certificate
```
