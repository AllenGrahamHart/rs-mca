# X48: h=4 centered shells are quotient-coset intersections

- **DAG node:** `x48_h4_centered_coset_shell_param`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved parametrization.
- **Verifier:** `experimental/scripts/verify_x48_h4_centered_coset_shell_param.py`.
- **Certificate:**
  `experimental/data/certificates/x48-h4-centered-coset-shell-param/x48_h4_centered_coset_shell_param.json`.

## Statement

Let `H = mu_n` in `F_p`, and let

```text
m_s = #{{x,y} subset H : x+y=s},        s != 0,
```

where pairs are unordered and have distinct elements.  Then

```text
m_s = (1/2) #{ r in H \ {1} : 1+r in sH }.
```

In particular, `m_s` depends only on the quotient coset `sH` in
`F_p^*/H`.  Therefore X44's max-shell statistic is a maximum over shifted
subgroup intersections in the quotient:

```text
M = max_{C in F_p^*/H} (1/2) #{ r in H \ {1} : 1+r in C }.
```

## Proof

For an ordered pair `(x,y)` with `x,y in H`, `x != y`, and `x+y=s`, put

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

Then `x=ry` lies in `H`, `x != y`, and

```text
x+y = y(1+r) = s.
```

Thus the displayed set of ratios is in bijection with ordered distinct pairs
`(x,y) in H^2` with sum `s`.  Passing from ordered pairs to unordered pairs
divides by two, proving the formula.

The condition `1+r in sH` only depends on the coset `sH`, so `m_s` is constant
on multiplicative `H`-cosets.

## Consequence

X44 already proves

```text
R_centered <= C(M,4) C(n,2) / M.
```

X48 identifies the exact object that must be bounded to make this uniform:

```text
max_C #{r in H \ {1} : 1+r in C}.
```

This is a shifted-subgroup intersection/cyclotomic-number target over
`F_p^*/H`, not an h=4 support-sort target.  Row certificates can compute the
quotient coset counts directly.

## Replay

The verifier checks the parametrization on:

- low-characteristic stress rows where centered residue is real;
- the `n=64, p=7937` row where X43's `M <= 4` criterion fails but X44 closes;
- selected campaign-boundary rows.

For every replayed row:

- direct pair-sum shell sizes match the ratio formula;
- shell sizes are constant on multiplicative cosets;
- the max direct shell equals the max quotient-coset shell.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x48_h4_centered_coset_shell_param.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x48_h4_centered_coset_shell_param.py --write-certificate
```
