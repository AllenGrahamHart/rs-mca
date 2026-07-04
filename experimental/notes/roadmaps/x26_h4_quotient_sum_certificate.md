# X26: h=4 quotient-sum certificate

- **DAG node:** `x26_h4_quotient_sum_certificate`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite certificate.
- **Verifier:** `experimental/scripts/verify_x26_h4_quotient_sum_certificate.py`.
- **Certificate:**
  `experimental/data/certificates/x26-h4-quotient-sum-certificate/x26_h4_quotient_sum_certificate.json`.

## Scope

X20-X22 classify finite h=4 active pairs into two cyclic-paid families:

```text
mu4_full_fiber
antipodal_h2_quotient_lift
```

X26 computes the second family directly in the quotient h=2 problem.  If an
h=4 support is an antipodal union

```text
{a,-a,b,-b},
```

then the h=4 top-three condition descends through `x -> x^2` to the quotient
sum condition

```text
1 + u = v + w        in mu_{n/2}.
```

The zero-sum quotient collisions lift to the persistent `mu4_full_fiber`
family.  Any extra quotient sum collision lifts to the paid
`antipodal_h2_quotient_lift` family.

## Result

The verifier sweeps the full h=4 boundary windows for `n=16,32,64` by working
in the quotient h=2 space:

```text
family       quotient m       primes swept       extra quotient collisions
--------------------------------------------------------------------------
n=16             8                 61             none
n=32            16                212             none
n=64            32                693             listed below
```

For `n=64`, the extra quotient collisions occur exactly at:

```text
p        extra anchored quotient collisions
-------------------------------------------
4993     12
7937     12
10177     4
11329     4
26177     4
50177     4
51137     4
65537     4
156353    4
```

This is exactly the X22 h=4 antipodal-lift exception list.

## Interpretation

The h=4 exceptional-prime mass is not a new h=4 mechanism.  It is precisely
the lower h=2 quotient sum-collision mechanism lifted through the antipodal
map.

So the h=4 finite-p picture is now:

```text
zero-sum quotient h=2 collisions       -> mu4_full_fiber
extra quotient h=2 sum collisions      -> antipodal_h2_quotient_lift
primitive/non-fingerprinted residue    -> none observed in full n=16,32,64 windows
```

This gives the finite-p side a smaller target: certify the quotient h=2
sum-collision rows, then charge their antipodal lifts.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x26_h4_quotient_sum_certificate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x26_h4_quotient_sum_certificate.py --write-certificate
```

Current replay: **12 PASS, 0 FAIL**.
