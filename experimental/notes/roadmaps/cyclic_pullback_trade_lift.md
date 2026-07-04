# Cyclic pullback trade-lift lemma

- **DAG node:** `cyclic_pullback_trade_lift`.
- **Consumers:** `active_core_count_bound`, `cyclic_fiber_collision_lemma`.
- **Status:** PROVED.
- **Verifier:** `experimental/scripts/verify_cyclic_pullback_trade_lift.py`.
- **Certificate:**
  `experimental/data/certificates/cyclic-pullback-trade-lift/cyclic_pullback_trade_lift.json`.

## Statement

Let `H = mu_n`, let `g | n`, and let `N = n/g`.  Write `zeta` for a generator
of `H`.  The cyclic quotient partition has fibers

```text
F_r = { zeta^(r + N j) : 0 <= j < g },        0 <= r < N.
```

Let `C` be a size-`s` subset of the quotient constants

```text
Q = { zeta^(g r) : 0 <= r < N } = mu_N.
```

Let `P_C` be the union of the fibers indexed by `C`.  Then

```text
L_{P_C}(X) = L_C(X^g).
```

Consequently, for two quotient supports `C,D` of size `s`,

```text
C and D have the same top (s-1) elementary symmetric sums
```

if and only if

```text
P_C and P_D have the same top (g s - 1) elementary symmetric sums.
```

Every such lifted split-pair collision is paid by the cyclic pullback
dictionary.

## Proof

For a fixed quotient constant `a = zeta^(g r)`, the fiber `F_r` is exactly the
root set of

```text
X^g - a.
```

Indeed, `zeta^(r + N j)` has `g`-th power `zeta^(g r)`, and these `g` roots
are distinct because the characteristic is prime to `n`.

If `C = {a_1,...,a_s}`, then the locator of the union of the corresponding
fibers is

```text
L_{P_C}(X) = product_i (X^g - a_i) = L_C(X^g).
```

Writing

```text
L_C(Y) = Y^s - E_1(C)Y^(s-1) + ... + (-1)^s E_s(C),
```

we get

```text
L_{P_C}(X) =
  X^(g s) - E_1(C) X^(g(s-1)) + ... + (-1)^s E_s(C).
```

All coefficients in degrees not divisible by `g` vanish.  The nonconstant
coefficients of `L_{P_C}` are exactly the quotient elementary symmetric sums
`E_1(C),...,E_{s-1}(C)`, placed in degrees

```text
g(s-1), g(s-2), ..., g.
```

Therefore two quotient supports have equal top `s-1` data exactly when their
full pullbacks have equal top `g s - 1` data.  Their locators differ only in
the constant term precisely when the quotient locators do.

Since `P_C` and `P_D` are unions of fibers for the cyclic quotient map
`X -> X^g` (equivalently for any `X^m` inducing the same fiber partition),
the lifted collision is cyclic-pullback paid.

## Relation To X14 And X19

The cyclic full-fiber collision lemma is the special case `s=1`: every single
fiber has locator `X^g-a`, so all top `g-1` coefficients vanish.

X19 is the case

```text
n = 32, g = 8, s = 1.
```

The persistent X14 h=4 family is the case

```text
g = 4, s = 1.
```

The additional X14 boundary family at `n=128, alpha=2` with classifier label
`cyclic:m=6` is the quotient-lift case

```text
g = gcd(128,6) = 2,        s = 2.
```

Here h=4 supports are unions of two antipodal fibers.  Same-top-three equality
upstairs is exactly same-top-one equality for the two quotient points in
`mu_64`, so this family is also cyclic-paid.

## Terminal-Node Consequence

Cyclic pullback cells should be stripped before any primitive split-pair bound
is attempted.  The raw same-top relation contains quotient-row copies at every
cyclic scale:

```text
same-top-(s-1) trades on mu_(n/g)
    lift to same-top-(g s - 1) trades on mu_n.
```

These trades are not primitive residue.  They belong to the paid cyclic
pullback column.

## Verification

Run:

```bash
python3 experimental/scripts/verify_cyclic_pullback_trade_lift.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_cyclic_pullback_trade_lift.py --write-certificate
```
