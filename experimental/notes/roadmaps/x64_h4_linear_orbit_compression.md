# X64: h=4 linear orbit compression

- **DAG node:** `x64_h4_linear_orbit_compression`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved orbit compression.
- **Verifier:** `experimental/scripts/verify_x64_h4_linear_orbit_compression.py`.
- **Certificate:**
  `experimental/data/certificates/x64-h4-linear-orbit-compression/x64_h4_linear_orbit_compression.json`.

## Statement

The X60 equation

```text
x + y = z + 1
```

is an equality of two unordered pairs with the same sum:

```text
{x,y}        and        {z,1}.
```

Swapping within either pair, swapping the two pairs, and then re-anchoring the
chosen fourth point at `1` gives an eight-element symmetry group on X60
filtered triples.  In exponent coordinates

```text
x = zeta^a,        y = zeta^b,        z = zeta^c,
```

the eight transforms are:

```text
(a,b,c),
(b,a,c),
(a-c,b-c,-c),
(b-c,a-c,-c),
(c-a,-a,b-a),
(-a,c-a,b-a),
(c-b,-b,a-b),
(-b,c-b,a-b),
```

all modulo `n`.

On the X60 filtered locus this action is free, so every filtered triple has
orbit size exactly `8`.  The content

```text
gcd(n,a,b,c)
```

is invariant on these orbits.  Therefore the primitive content-one X63
residue can be certified on canonical eight-orbit representatives.

## Proof

The equation `x+y=z+1` has two unordered sides.  The first two displayed
transforms swap the positive pair `{x,y}`.

Swapping the negative pair `{z,1}` and re-anchoring at the old `z` divides the
whole equality by `z`, giving

```text
x/z + y/z = 1 + 1/z,
```

which contributes

```text
(a-c,b-c,-c),        (b-c,a-c,-c).
```

Swapping the two sides and re-anchoring at the old `x` divides by `x`:

```text
z/x + 1/x = 1 + y/x,
```

giving

```text
(c-a,-a,b-a),        (-a,c-a,b-a).
```

Re-anchoring instead at the old `y` gives

```text
z/y + 1/y = 1 + x/y,
```

and hence

```text
(c-b,-b,a-b),        (-b,c-b,a-b).
```

Each transform is obtained by subtracting one of `0,a,b,c` from all four
exponents and then assigning the two non-anchor exponents to the positive
side.  Thus it preserves the equation and preserves

```text
gcd(n,a,b,c).
```

The X60 exclusions force the four points `x,y,z,1` to be distinct:

```text
x != 1,        y != 1,        z != 1,        x != y.
```

Also `z=x` would force `y=1`, and `z=y` would force `x=1`.  Finally the
excluded branch `y=-x` removes the zero-midpoint chord stabilizer.  Therefore
no nontrivial pair-symmetry fixes a filtered triple, so the orbit size is
exactly `8`.

## Consequence

X63 reduced the primitive X62 residue to content-one words

```text
X^a + X^b - X^c - 1,        gcd(n,a,b,c)=1.
```

X64 reduces the row-local certifier further: it is enough to check canonical
representatives under the eight pair-sum symmetries, and then expand by a
factor of exactly `8`.

This is a small constant reduction, not a terminal estimate by itself.  Its
value is conceptual: the remaining primitive four-term norm-gate problem is
now in canonical chord-pair currency rather than ordered triple currency.

## Replay

The verifier replays all X60 finite rows.  The primitive orbit counts are:

```text
row                  primitive triples   primitive canonical orbits
low_n16_p17          160                 20
low_n64_p193         1072                134
boundary_n64_p7937   184                 23
boundary_n128_p17921 96                  12
boundary_n256_p91393 176                 22
```

Every replayed filtered orbit has size exactly `8`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x64_h4_linear_orbit_compression.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x64_h4_linear_orbit_compression.py --write-certificate
```
