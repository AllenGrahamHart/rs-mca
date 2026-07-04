# X45: h=4 common-gcd orbit compression

- **DAG node:** `x45_h4_common_gcd_orbit_compression`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved certifier compression.
- **Verifier:** `experimental/scripts/verify_x45_h4_common_gcd_orbit_compression.py`.
- **Certificate:**
  `experimental/data/certificates/x45-h4-common-gcd-orbit-compression/x45_h4_common_gcd_orbit_compression.json`.

## Statement

Let `n = 2^s`, let `p == 1 mod n`, and let `P,Q` be disjoint exponent
4-subsets of `Z/nZ`.  For the X33 h=4 common-gcd gate

```text
D(P,Q) = deg gcd(Phi_n, E_1, E_2, E_3),
```

where `E_r` is the r-th elementary-difference polynomial, `D(P,Q)` is
invariant under:

```text
P,Q -> P+d,Q+d                 common translation,
P,Q -> uP,uQ                   u in (Z/nZ)^*,
P,Q -> Q,P                     side swap.
```

Consequently any h=4 row certifier may check one representative of each
affine exponent orbit rather than every translated, Galois-conjugate, and
side-swapped copy.

## Proof

For translation by `d`, every r-fold exponent sum is shifted by `rd`, so

```text
E_r(P+d,Q+d)(X) = X^(rd) E_r(P,Q)(X).
```

Since `Phi_n(0)=1`, the monomial factor is coprime to `Phi_n`, and the common
zero set on primitive roots is unchanged.

For unit dilation by `u`, exponent sums are multiplied by `u`, hence

```text
E_r(uP,uQ)(X) = E_r(P,Q)(X^u)  mod X^n - 1.
```

Because `u` is a unit modulo `n`, the map `zeta -> zeta^u` permutes the
primitive `n`-th roots.  The number of primitive roots on which all three
`E_r` vanish is therefore unchanged.  Since `p == 1 mod n`, `Phi_n` splits
separably in `F_p`, so this number is exactly the common-gcd degree.

Swapping `P` and `Q` multiplies every `E_r` by `-1`, which does not change the
gcd.  These three invariances prove the compression.

## Canonical Representative

The verifier uses the affine action

```text
a -> u a + d,       u odd,
```

plus side swap.  A lexicographically minimal representative has `0` in the
union, so it is enough to try translations that send one of the eight support
exponents to `0` after each unit dilation.

This canonicalization is a certifier convenience only; the proof above is the
mathematical content.

## Replay

The verifier checks the symbolic polynomial identities and representative
invariance examples in `F_257 / mu_16` and `F_4993 / mu_32`.

It also runs a full anchored-pair orbit compression at `n=16`:

```text
anchored ordered pairs:  C(15,3) C(12,4)
canonical affine orbits: computed by the verifier
```

Every canonical orbit has constant common-gcd degree.  In this row, every
positive-degree orbit is descended through the antipodal quotient and is
therefore already paid; no top-level positive-degree orbit remains.

## Consequence

X33 gives the exact h=4 top-level gate, and X35 rewrites it as a signed
8-sparse three-moment gate.  X45 removes redundant copies from that gate.  A
future official-row h=4 certificate can now be stated as:

```text
for every canonical affine exponent-orbit representative outside the paid
antipodal branch, deg gcd(Phi_n,E_1,E_2,E_3) = 0,
```

or else count the positive-degree canonical representatives as a norm-gate
column and expand by their orbit sizes.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x45_h4_common_gcd_orbit_compression.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x45_h4_common_gcd_orbit_compression.py --write-certificate
```
