# X31: h=2 quotient norm criterion

- **DAG node:** `x31_h2_quotient_norm_criterion`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved specialization of X30.
- **Verifier:** `experimental/scripts/verify_x31_h2_quotient_norm_criterion.py`.
- **Certificate:**
  `experimental/data/certificates/x31-h2-quotient-norm-criterion/x31_h2_quotient_norm_criterion.json`.

## Statement

Let `m=2^s`, let `zeta` be a primitive `m`-th root in odd characteristic `p`,
and consider anchored quotient h=2 sum collisions

```text
1 + zeta^a = zeta^b + zeta^c,
```

with the two unordered pairs disjoint.

Put

```text
f_{a,b,c}(X) = 1 + X^a - X^b - X^c.
```

Then exactly one of the following mechanisms is responsible:

1. **Zero-sum baseline.**

   ```text
   a = m/2,        c = b + m/2.
   ```

   This is the `Phi_m`-descended branch.  It has anchored count

   ```text
   m/2 - 1.
   ```

2. **Sparse norm gate.**  The word is not `Phi_m`-descended, and

   ```text
   p | Res(Phi_m, f_{a,b,c}).
   ```

Conversely, if `p | Res(Phi_m, f_{a,b,c})`, then over `F_p` the polynomial
`f_{a,b,c}` vanishes at some primitive `m`-th root.  Relative to the chosen
domain generator `zeta`, this is the same collision after multiplying all
exponents by a unit of `Z/mZ`.

Thus quotient h=2 extras are precisely sparse cyclotomic norm gates, modulo
the natural Galois exponent scaling.

## Proof

The quotient collision is exactly

```text
f_{a,b,c}(zeta) = 0.
```

Since `m` is a power of two,

```text
Phi_m(X) = X^(m/2) + 1.
```

The word `f_{a,b,c}` has coefficients in `{-1,0,1}`.  By the X30 coefficient
criterion, `Phi_m | f_{a,b,c}` over `Z` if and only if the positive support
`{0,a}` and the negative support `{b,c}` are each antipodal pairs.  Since the
positive pair is anchored, this means

```text
a = m/2.
```

Since the negative pair is an antipodal pair and is disjoint from `{0,m/2}`,
it is `{b,b+m/2}` with `b` not equal to `0` or `m/2`.  Hence the number of
disjoint target zero-sum pairs is

```text
m/2 - 1.
```

If `Phi_m` does not divide `f_{a,b,c}`, then `Phi_m` and `f_{a,b,c}` are
coprime over `Z`.  A finite-field collision makes their reductions have a
common root, so their resultant is zero modulo `p`:

```text
p | Res(Phi_m, f_{a,b,c}).
```

For the converse up to Galois scaling, if `p` divides the resultant, then
`Phi_m` and `f_{a,b,c}` have a common root over `F_p`.  Because `p == 1 mod m`
in the rows under consideration, all primitive `m`-th roots lie in `F_p` and
are powers `zeta^r` with `r in (Z/mZ)^*`.  Thus

```text
f_{a,b,c}(zeta^r) = 0,
```

which is the anchored collision for the exponent-scaled pattern

```text
{0, ra} and {rb, rc}.
```

## Exact Resultant Rows

The verifier computes exact integer resultants for every extra quotient
collision in three representative rows from X26-X28:

```text
m      p        extras   |Res| bits      v_p(Res) histogram
-----------------------------------------------------------
32     4993       12       14..14        {1: 12}
64     65537      52       18..35        {1: 40, 2: 12}
128    65537      88       35..69        {1: 36, 2: 40, 4: 12}
```

Every extra word is non-descended and p-norm-gated.  Every zero-sum baseline
word for `m in {8,16,32,64,128}` is `Phi_m`-descended.

## Interpretation

X29 proved that the h=4 antipodal branch is the quotient h=2 sum-collision
ledger.  X31 identifies the arithmetic of that ledger:

```text
quotient h=2 = zero-sum baseline + sparse norm gates.
```

Therefore the h=4 paid exception column has no hidden third mechanism inside
the quotient layer.  The remaining terminal work is to count or rule out
sparse norm gates outside the already-paid quotient branch.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x31_h2_quotient_norm_criterion.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x31_h2_quotient_norm_criterion.py --write-certificate
```

Current replay: **20 PASS, 0 FAIL**.
