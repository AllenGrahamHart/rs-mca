# X73: h=4 normalized-pair sieve

- **DAG node:** `x73_h4_normalized_pair_sieve`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved row-local certifier.
- **Verifier:** `experimental/scripts/verify_x73_h4_normalized_pair_sieve.py`.
- **Certificate:**
  `experimental/data/certificates/x73-h4-normalized-pair-sieve/x73_h4_normalized_pair_sieve.json`.

## Statement

Fix a replay row with `n | p-1`, `n=2^s`, and `p` odd.  Let `zeta` be the
chosen generator of `mu_n`.  For every filtered normalized pair

```text
(1,r,s),
```

form

```text
f_(r,s)(X) = X + X^r - X^s - 1.
```

Then `f_(r,s)` is a row-local p-norm gate if and only if

```text
f_(r,s)(zeta^u) = 0
```

for some unit `u in (Z/nZ)^*`.

Consequently, a complete row-local h=4 norm-gate certifier can enumerate all
filtered normalized pairs, apply this primitive-root test, and group survivors
by the X68 certifier key.  On the replay rows this complete normalized sieve
finds exactly the same X68 key set as the independent X60 finite-triple
replay.

## Proof

Since `n | p-1` and `p` is odd, `p` does not divide `n`.  The cyclotomic
polynomial has simple roots over `F_p`, and all primitive `n`-th roots are in
the row field:

```text
Phi_n(X) = product_{u in (Z/nZ)^*} (X - zeta^u).
```

Thus

```text
p | Res(Phi_n, f_(r,s))
```

if and only if `f_(r,s)` shares one of these primitive roots with `Phi_n`,
which is exactly the displayed primitive-root test.

X70 proves that

```text
f_(r,s) = (X-1) q_(r,s),
```

and no primitive root is `1`, so this is the same test as the X70 quotient
test.  X71 gives the interval form of `q_(r,s)`, and X72 optionally strips a
prime-safe `X+1` factor when the interval parity permits it; neither linear
factor changes the primitive-root test.

Finally, X68 proves that all members of a certifier key have the same
cyclotomic resultant prime set.  Grouping the normalized survivors by X68 key
therefore gives exactly the row-local certifier key set.

## Replay

The verifier enumerates every filtered normalized pair `(1,r,s)`.  The count
is closed form:

```text
(n-3)(n-1),
```

because `r` excludes `0`, `1`, and `1+n/2`, while `s` excludes `0`.

It then tests every candidate against all primitive roots and compares the
surviving X68 keys with the replay keys obtained from the finite-field X60
triple enumeration.

```text
row                  candidates   survivor pairs   survivor keys
-----------------------------------------------------------------
low_n16_p17          195          82               19
low_n64_p193         3843         596              133
boundary_n64_p7937   3843         100              23
boundary_n128_p17921 15875        52               12
boundary_n256_p91393 64515        100              22
```

Every row has:

```text
complete-sieve survivor keys = replay finite-triple keys.
```

There are no missing replay keys and no extra sieve keys.

## Consequence

X73 turns the h=4 primitive interval-resultant lane into a complete row-local
key certifier:

```text
enumerate (1,r,s)
  -> primitive-root test over F_p
  -> X68 key
  -> expand surviving row mass in X65 currency.
```

This is still a finite-row certifier, not the uniform terminal proof.  Its
value is that any proposed h=4 exclusion theorem can now be checked against a
small, complete, normalized key set rather than against ordered triples,
support families, or large integer resultants.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x73_h4_normalized_pair_sieve.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x73_h4_normalized_pair_sieve.py --write-certificate
```
