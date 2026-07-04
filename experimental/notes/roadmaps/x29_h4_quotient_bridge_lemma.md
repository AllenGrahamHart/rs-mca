# X29: h=4 quotient-bridge lemma

- **DAG node:** `x29_h4_quotient_bridge_lemma`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved algebraic bridge.
- **Verifier:** `experimental/scripts/verify_x29_h4_quotient_bridge_lemma.py`.
- **Certificate:**
  `experimental/data/certificates/x29-h4-quotient-bridge-lemma/x29_h4_quotient_bridge_lemma.json`.

## Statement

Let `4 | n`, let `H = mu_n` over a field of odd characteristic, and let

```text
pi: H -> mu_{n/2},        pi(x) = x^2.
```

Anchored h=4 supports in `H` that are unions of antipodal pairs are in
bijection with anchored 2-subsets of `mu_{n/2}`:

```text
A subset mu_{n/2}, |A|=2, 1 in A
    <-> pi^{-1}(A) subset H, |pi^{-1}(A)|=4, 1 in pi^{-1}(A).
```

Under this bijection, two disjoint lifted supports

```text
P = pi^{-1}(A),        Q = pi^{-1}(B)
```

have the same h=4 top-three elementary symmetric signature if and only if the
quotient pairs have the same sum:

```text
sum(A) = sum(B).
```

Therefore the anchored h=4 antipodal-union count is exactly the anchored h=2
quotient sum-collision count.

The zero-sum quotient baseline has size

```text
n/4 - 1,
```

and it lifts exactly to the `mu_4` full-fiber family.

## Proof

Let `A={u,v}` be a 2-subset of `mu_{n/2}`.  Its full preimage under `x -> x^2`
is the antipodal-union h=4 support

```text
pi^{-1}(A) = {a,-a,b,-b},        a^2=u, b^2=v.
```

Its locator polynomial is

```text
L_{pi^{-1}(A)}(X)
  = (X^2-u)(X^2-v)
  = X^4 - (u+v)X^2 + uv
  = L_A(X^2).
```

In h=4 notation

```text
L_P(X) = X^4 - e_1(P)X^3 + e_2(P)X^2 - e_3(P)X + e_4(P),
```

this gives

```text
e_1(pi^{-1}(A)) = 0,
e_2(pi^{-1}(A)) = -(u+v),
e_3(pi^{-1}(A)) = 0.
```

Thus two lifted supports have the same top-three h=4 signature precisely when
their quotient sums match:

```text
e_i(pi^{-1}(A)) = e_i(pi^{-1}(B)), i=1,2,3
    <=>      u+v = r+s.
```

Disjointness is also preserved: `pi^{-1}(A)` and `pi^{-1}(B)` are disjoint
exactly when `A` and `B` are disjoint.

The anchoring convention is preserved as well.  If `1 in A`, then
`1 in pi^{-1}(A)`; conversely, if a lifted antipodal support contains `1`,
then its quotient pair contains `1`.

This proves the bijective count transfer.

For the baseline, the zero-sum quotient pairs in `mu_{n/2}` are

```text
{w,-w}.
```

There are `(n/2)/2 = n/4` such unordered pairs.  In the anchored quotient
count the source pair is fixed to `{1,-1}`, so the disjoint target pair can be
any of the remaining

```text
n/4 - 1
```

zero-sum pairs.  Their lifts are exactly full `mu_4` fibers:

```text
pi^{-1}({w,-w}) = a mu_4,        a^2=w.
```

So the persistent `mu_4` count in X20-X28 is not an empirical artifact; it is
the quotient zero-sum baseline.

## Checked Rows

The verifier checks the bridge and the baseline formula on representative
finite rows:

```text
n     p        quotient total   zero-sum baseline   extra quotient lifts
------------------------------------------------------------------------
16    257              3                3                    0
32    1153             7                7                    0
64    4993            27               15                   12
128   65537           83               31                   52
256   65537          151               63                   88
```

It also checks the closed baseline formula through `n=1024`.

## Interpretation

This packet does not say that every h=4 trade is an antipodal union.  That is
the remaining h=4 structural exclusion.

It does prove that once an h=4 trade is in the antipodal-union branch, all
counting and charging can be done exactly in the quotient h=2 sum-collision
ledger:

```text
h=4 antipodal branch = quotient h=2 sum collisions
                     = mu_4 baseline + extra paid antipodal lifts.
```

This is the count-transfer justification behind X26, X27, and X28.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x29_h4_quotient_bridge_lemma.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x29_h4_quotient_bridge_lemma.py --write-certificate
```

Current replay: **30 PASS, 0 FAIL**.
