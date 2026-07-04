# X65: h=4 linear orbit-budget currency

- **DAG node:** `x65_h4_linear_orbit_budget`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved currency conversion.
- **Verifier:** `experimental/scripts/verify_x65_h4_linear_orbit_budget.py`.
- **Certificate:**
  `experimental/data/certificates/x65-h4-linear-orbit-budget/x65_h4_linear_orbit_budget.json`.

## Statement

X60 puts the centered h=4 residue in filtered linear-triple form:

```text
F(n,p) = #{(x,y,z) in H^3 :
          x + y - z = 1,
          x != 1, y != 1, z != 1, y != x, y != -x}.
```

The X55-X56 barrier is

```text
F(n,p) < 8 * C(T(n)+1, 2),
```

where `T(n)` is the exact X50 threshold.  X64 proves that the filtered
triples form free eightfold chord-pair orbits.  Therefore the same target is
exactly

```text
O(n,p) < C(T(n)+1, 2),
```

where `O(n,p)` is the number of canonical filtered chord-pair orbits.

After the X63 quotient strip, the top-level primitive target is

```text
O_prim(n,p) < C(T(n)+1, 2),
```

where `O_prim` counts only content-one canonical orbits
`gcd(n,a,b,c)=1` for words

```text
X^a + X^b - X^c - 1.
```

The content `d > 1` orbits are quotient-pullback mass and descend to
`mu_(n/d)`.

## Proof

X60 proves that twice the X56 anchored surplus equals `F(n,p)`.  Since the
anchored surplus barrier is

```text
4 * C(T(n)+1, 2),
```

the filtered-triple barrier is exactly

```text
8 * C(T(n)+1, 2).
```

X64 gives a free action of size `8` on the X60 filtered locus.  Thus

```text
F(n,p) = 8 * O(n,p).
```

Dividing the strict filtered inequality by `8` gives

```text
O(n,p) < C(T(n)+1, 2).
```

Conversely, multiplying the orbit inequality by `8` recovers the X60
filtered inequality.  Hence the two targets are equivalent, not merely
comparable up to constants.

X64 also proves that `gcd(n,a,b,c)` is invariant on these orbits.  X63 proves
that every orbit with content `d > 1` is a quotient pullback: after writing

```text
a = d a',  b = d b',  c = d c',
```

the same filtered equation holds on the quotient row `mu_(n/d)`.  Therefore
the genuine top-level residue is exactly the content-one orbit count
`O_prim(n,p)`, with quotient-descended content charged recursively.

## Replay

The verifier checks the X50, X60, and X64 certificates row by row.

```text
row                  total orbits / barrier   primitive orbits / barrier
--------------------------------------------------------------------------
low_n16_p17          21 / 66                  20 / 66
low_n64_p193         147 / 136                134 / 136
boundary_n64_p7937   26 / 136                 23 / 136
boundary_n128_p17921 15 / 210                 12 / 210
boundary_n256_p91393 28 / 325                 22 / 325
```

The low-characteristic `n=64, p=193` stress row fails the total orbit barrier
but passes after the quotient strip: its excess over the barrier is
quotient-descended mass.  All campaign-boundary replay rows pass the
primitive orbit target with large margin.

## Consequence

The remaining centered h=4 proof target can now be stated in canonical
four-term norm-gate currency:

```text
#{canonical content-one chord-pair orbits with
  p | Res(Phi_n, X^a + X^b - X^c - 1)}
  < C(T(n)+1, 2).
```

This does not prove the terminal estimate.  It removes the ordered-triple
factor and separates quotient-recursive content from the primitive
p-specific residue.  The next proof/certifier should operate in this orbit
currency.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x65_h4_linear_orbit_budget.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x65_h4_linear_orbit_budget.py --write-certificate
```
