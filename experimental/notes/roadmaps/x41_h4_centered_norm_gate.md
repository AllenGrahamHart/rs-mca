# X41: h=4 centered norm-gate localization

- **DAG node:** `x41_h4_centered_norm_gate`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved localization.
- **Verifier:** `experimental/scripts/verify_x41_h4_centered_norm_gate.py`.
- **Certificate:**
  `experimental/data/certificates/x41-h4-centered-norm-gate/x41_h4_centered_norm_gate.json`.

## Statement

The nonzero centered affine branch from X39/X40 is p-specific.  More precisely:
if two distinct unordered pairs in `mu_n` have the same nonzero finite-field
sum, then their signed `2+2` word is a sparse cyclotomic norm gate.

Thus every nonzero centered h=4 affine residue is built on lower h=2
norm-gated pair-sum shells.

## Characteristic-Zero Lemma

Let `x,y,u,v` be complex roots of unity and suppose

```text
x+y = u+v = s,        s != 0.
```

Taking complex conjugates gives

```text
x^{-1}+y^{-1} = u^{-1}+v^{-1}.
```

Since

```text
x^{-1}+y^{-1} = (x+y)/(xy) = s/(xy)
```

and similarly for `u,v`, the nonzero sum implies

```text
xy = uv.
```

The two unordered pairs therefore have the same sum and product, so they are
the same pair.  Hence no distinct nonzero pair-sum collision exists over
characteristic zero roots of unity.

The zero-sum shell is the excluded antipodal case:

```text
y=-x.
```

That branch is the descended/cyclic-paid shell from X38 and X31.

## Finite-p Consequence

Let `n=2^r`, let `zeta` be a primitive `n`-th root in characteristic `p`, and
suppose two distinct unordered pairs have the same nonzero sum:

```text
zeta^a+zeta^b = zeta^c+zeta^d != 0.
```

Form the signed sparse word

```text
f(X)=X^a+X^b-X^c-X^d.
```

Then `f(zeta)=0` in the finite field.  The characteristic-zero lemma says
`Phi_n` cannot divide `f` over `Z`: if it did, the same nonzero pair-sum
collision would hold over the complex primitive `n`-th roots, forcing the
pairs to be equal.

Therefore X30 applies:

```text
p | Res(Phi_n, f).
```

This is exactly the h=2 sparse norm-gate mechanism from X31, without the
anchoring convention.

## Consequence For X40

X40 reduced the nonzero centered affine h=4 residue to pair-product
two-sum collisions inside a fixed nonzero pair-sum shell.  X41 shows that the
existence of the shell itself is already finite-p norm-gated.

So the centered affine branch is not a new characteristic-zero h=4 mechanism.
It is a p-specific lower h=2 norm-gate layer, plus the extra pair-product
collision condition from X40.

## Checks

The verifier records:

- zero-sum pair shells are `Phi_n`-descended;
- low-characteristic nonzero shell collisions are non-descended and have
  `p | Res(Phi_n,f)`;
- boundary examples such as `F_1153/mu_32` and `F_17921/mu_128` satisfy the
  same norm-gate criterion.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x41_h4_centered_norm_gate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x41_h4_centered_norm_gate.py --write-certificate
```
