# X78: h=5 square-shift supports

- **DAG node:** `x78_h5_square_shift_supports`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved h=5 algebraic compression.
- **Verifier:** `experimental/scripts/verify_x78_h5_square_shift_supports.py`.
- **Certificate:**
  `experimental/data/certificates/x78-h5-square-shift/x78_h5_square_shift_supports.json`.

## Statement

Let `F` be a field of odd characteristic.  Let `P,Q` be disjoint 5-subsets of
`F` with locator polynomials

```text
L_P(X) = prod_{a in P} (X-a),
L_Q(X) = prod_{b in Q} (X-b).
```

Then `P,Q` have the same top four elementary-symmetric coefficients if and
only if

```text
L_Q = L_P + delta
```

for a nonzero constant `delta`.  If `R=P union Q`, this is equivalent to the
union locator admitting a square shift

```text
L_R(X) + lambda = S(X)^2
```

where `S` is monic of degree 5 and `lambda` is a square in `F`.  The split
`R=P union Q` is unique up to swapping `P` and `Q`.  Since the supports are
disjoint, the relevant square `lambda` is nonzero.

Consequently, h=5 pair counting can be replaced by square-shift 10-support
counting:

```text
unordered h=5 trades <= #{10-subsets R: L_R + lambda is a monic square
                          for some nonzero square lambda}.
```

For ordered pairs, multiply the right side by at most `2`.

## Proof

For degree five, equality of the top four elementary-symmetric coefficients
is exactly equality of every locator coefficient except the constant term.
Thus

```text
L_Q = L_P + delta.
```

The supports are disjoint, so `L_P` and `L_Q` cannot be the same polynomial;
hence `delta != 0`.

Set

```text
S = (L_P + L_Q)/2 = L_P + delta/2.
```

Since the characteristic is odd,

```text
L_R = L_P L_Q = L_P(L_P+delta)
```

and therefore

```text
L_R + delta^2/4 = (L_P + delta/2)^2 = S^2.
```

So every h=5 trade gives a square-shift 10-support with square shift
`lambda=delta^2/4`.

Conversely, suppose

```text
L_R + lambda = S^2
```

with `lambda=a^2` and `a != 0`.  Then

```text
L_R = (S-a)(S+a).
```

Both factors are monic degree-five polynomials and differ only in their
constant term.  Since `R` is a split support and `a != 0`, the two factors are
coprime and their roots partition `R` into two disjoint 5-subsets with equal
top four locator coefficients.

Finally, the square shift is unique.  If

```text
L_R + lambda = S^2,      L_R + mu = T^2
```

with monic degree-five `S,T`, then

```text
(S-T)(S+T) = lambda - mu
```

is constant.  Since `S+T` is nonconstant, the integral-domain property forces
`S=T`, and then `lambda=mu`.  Thus a 10-support contributes at most one
unordered split, or two ordered splits.

## Why This Helps

X77 reduced h=5 to first-level p-specific sparse norm gates.  X78 adds an
independent h=5-specific compression:

```text
same-top-four pair
  -> one 10-support R
  -> one forced monic square root S, if it exists
  -> one split, up to swapping sides.
```

The remaining h=5 proof is therefore not a count over partitions of every
10-support.  It is a count, or exclusion, of square-shifted 10-point locators
inside `mu_n`.

Equivalently, writing `C=L_R`, the candidate square root is forced
recursively by the coefficients of `C` in degrees `10,9,...,5`; the
coefficients in degrees `1,2,3,4` are the obstruction equations, and the
constant discrepancy is the candidate `lambda`.

This is the h=5 analogue of the h=4 interval-witness compression: it does not
yet close the h=5 terminal branch, but it removes partition multiplicity and
turns the branch into a canonical support test.

## Replay

The verifier checks the polynomial identities directly and exhaustively
compares h=5 trade pairs with square-shift 10-supports on small rows:

```text
F17 / mu16
F97 / mu16
F257 / mu16
```

All three sanity rows have zero h=5 trades and zero square-shift supports, in
agreement with the criterion.  The boundary sanity row `F257/mu16` is the
first row of the X25 full prime window.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x78_h5_square_shift_supports.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x78_h5_square_shift_supports.py --write-certificate
```
