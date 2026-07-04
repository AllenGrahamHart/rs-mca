# X69: h=4 unit-anchor normal form

- **DAG node:** `x69_h4_unit_anchor_normal_form`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved certifier normal form.
- **Verifier:** `experimental/scripts/verify_x69_h4_unit_anchor_normal_form.py`.
- **Certificate:**
  `experimental/data/certificates/x69-h4-unit-anchor-normal-form/x69_h4_unit_anchor_normal_form.json`.

## Statement

Every primitive h=4 norm-gate certifier key from X68 has a representative

```text
(1, r, s)
```

in exponent coordinates.  Equivalently, the primitive sparse-resultant
certifier can enumerate normalized two-parameter words

```text
X + X^r - X^s - 1
```

and then quotient by the X68 key relation.

This is a certifier normal form, not a row-count normal form.  If a normalized
key survives the resultant exclusion, its finite-row mass is still expanded
using the X65 primitive X64 representative count.

## Proof

Let `n = 2^m` and suppose

```text
gcd(n,a,b,c) = 1.
```

Then at least one of `a,b,c` is odd.

If `a` is odd, the identity X64 transform already has an odd first
coordinate.  If `b` is odd, use the positive-pair swap `(b,a,c)`.

If neither `a` nor `b` is odd, then `c` must be odd.  The X64 side-swap
transform

```text
(c-a, -a, b-a)
```

has odd first coordinate because `c` is odd and `a` is even.

Thus some X64 transform has first coordinate equal to an odd residue `d`.
Since `n` is a power of two, odd residues are exactly the units modulo `n`.
Choose `u = d^{-1} mod n`.  X67 allows unit scaling of all exponents by `u`,
which sends the first coordinate to `1` and preserves:

```text
1. the X60 filter congruences,
2. primitive content,
3. the cyclotomic resultant prime set.
```

Therefore every X68 key has a filtered content-one representative `(1,r,s)`.

## Replay

The verifier recomputes the primitive X68 keys in the replay rows and checks
that each key's raw certifier orbit contains at least one member with first
coordinate `1`.

```text
row                  certifier keys   normalized members per key
----------------------------------------------------------------
low_n16_p17          19               2, 4, or 8
low_n64_p193         133              2, 4, or 8
boundary_n64_p7937   23               2, 4, or 8
boundary_n128_p17921 12               4 or 8
boundary_n256_p91393 22               4 or 8
```

The multiplicity is not charged as row-count compression.  It records how
many normalized `(1,r,s)` words represent one resultant key.

## Consequence

The primitive h=4 norm-gate certifier now has the following exact input
shape:

```text
for r,s mod n:
    test the normalized word X + X^r - X^s - 1,
    group it by the X68 key,
    expand survivors by X65 row-count representatives.
```

This reduces the certifier's ambient enumeration from triples to normalized
pairs without changing the mathematical row budget.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x69_h4_unit_anchor_normal_form.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x69_h4_unit_anchor_normal_form.py --write-certificate
```
