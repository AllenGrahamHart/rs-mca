# X62: h=4 linear triples are p-specific norm gates

- **DAG node:** `x62_h4_linear_norm_gate`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved localization.
- **Verifier:** `experimental/scripts/verify_x62_h4_linear_norm_gate.py`.
- **Certificate:**
  `experimental/data/certificates/x62-h4-linear-norm-gate/x62_h4_linear_norm_gate.json`.

## Statement

Let `H = mu_n` with `n = 2^s`.  The X60 filtered equation

```text
x + y - z = 1,        x,y,z in H,
```

has no solutions over the complex roots of unity after the five X60 exclusions

```text
x = 1,        y = 1,        z = 1,        y = x,        y = -x.
```

Consequently, if a finite-field row has a filtered solution

```text
zeta^a + zeta^b - zeta^c - 1 = 0 in F_p,
```

then the four-term sparse word

```text
f(X) = X^a + X^b - X^c - 1
```

is not divisible by `Phi_n` over `Z`, and hence

```text
p | Res(Phi_n, f).
```

Thus the remaining X60 centered h=4 obstruction is not an ordinary
characteristic-zero S-unit family.  It is entirely finite-p sparse
cyclotomic norm-gate mass.

## Proof

Work first over `C`.  The equation is

```text
x + y = z + 1
```

with all four points on the unit circle.

If `z != -1`, then the common midpoint

```text
(x+y)/2 = (z+1)/2
```

is nonzero and determines a unique chord of the unit circle.  Indeed, the
chord with midpoint `m` is the intersection of the unit circle with the line
perpendicular to the radius through `m`; its two endpoints are unique as an
unordered pair.  Hence

```text
{x,y} = {z,1}.
```

So either `x=1` or `y=1`, which is excluded by X60.

If `z = -1`, then the equation gives

```text
x + y = 0,
```

so `y = -x`, again one of the X60 exclusions.

Therefore the filtered complex locus is empty.

Now let `zeta` be a primitive `n`-th root in a finite field of odd
characteristic `p`, and suppose a filtered finite-field solution exists.  If

```text
Phi_n | f
```

over `Z`, then evaluating the same integral relation at a complex primitive
`n`-th root would give a filtered complex solution, contradicting the previous
paragraph.  Therefore `Phi_n` does not divide `f`.

But the finite-field solution gives a common root of `f mod p` and
`Phi_n mod p`.  Since `f` and `Phi_n` are coprime over `Z`, their resultant is
a nonzero integer and must vanish modulo `p`:

```text
Res(Phi_n, f) = 0 mod p.
```

This is exactly the X30 finite-p norm-gate mechanism, now specialized to the
four-term linear words produced by X60.

## Consequence

X61 already separated the true S-unit degeneracies

```text
x = 1,        y = 1,        y = -x
```

from the two extra bookkeeping branches

```text
y = x,        z = 1.
```

X62 strengthens the handoff: after those branches are stripped, there is no
characteristic-zero residue to estimate.  Every remaining centered h=4 triple
is p-specific and belongs to the same sparse-resultant certification lane as
the h=2 and h=4 norm-gate packets.

The next proof/certifier target can therefore be stated row-locally:

```text
exclude or charge four-term words X^a + X^b - X^c - 1
with p | Res(Phi_n, X^a + X^b - X^c - 1),
outside the X60 branches.
```

## Replay

The verifier checks:

- exact characteristic-zero rows `n = 8, 16, 32, 64`, represented in the
  `Phi_n = X^(n/2)+1` basis, have zero filtered solutions;
- every filtered finite-field triple in the X60 replay rows is non-`Phi_n`
  descended;
- the finite replay counts agree with the X60 certificate.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x62_h4_linear_norm_gate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x62_h4_linear_norm_gate.py --write-certificate
```
