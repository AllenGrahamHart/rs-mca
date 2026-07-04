# X34: h=4 staged common-gcd anatomy

- **DAG node:** `x34_h4_staged_gcd_anatomy`.
- **Consumer:** `active_core_count_bound`.
- **Status:** finite evidence / proof-target anatomy.
- **Verifier:** `experimental/scripts/verify_x34_h4_staged_gcd_anatomy.py`.
- **Certificate:**
  `experimental/data/certificates/x34-h4-staged-gcd-anatomy/x34_h4_staged_gcd_anatomy.json`.

## Purpose

X33 proves the exact h=4 common-gcd checker:

```text
G123 = gcd(Phi_n, E_1, E_2, E_3).
```

X34 asks where the top-level branch actually dies.  It measures the staged
filter

```text
G1   = gcd(Phi_n, E_1),
G12  = gcd(G1, E_2),
G123 = gcd(G12, E_3).
```

The result is useful for proof design: the second elementary equation already
kills almost every non-antipodal first-sum norm gate, and the third equation
kills the tiny survivor tail.

## Finite Rows

```text
row             top-level E1 pairs     deg G1          deg G12          deg G123
---------------------------------------------------------------------------------
F257 / mu16              712           {1: 712}        {0:704, 1:8}     {0:712}
F4993 / mu32           19860           {1:19804,2:56}  {0:19848,1:12}   {0:19860}
```

Interpretation:

- `G1` is positive for every listed pair because the row is selected from
  actual first-sum coincidences at the chosen generator.
- `E2` kills `704/712` and `19848/19860` of those pairs.
- `E3` kills all remaining `8` and `12` `G12`-positive cases.

So the top-level h=4 branch is not a large three-equation mystery in these
rows.  It is:

```text
prove the E2 kill generically,
then handle a very small G12-positive tail with E3.
```

## Proof Fragment

For any fixed h=4 exponent pattern `P,Q`, the staged degrees are nested:

```text
deg G123 <= deg G12 <= deg G1 <= phi(n).
```

If `deg G12 = 0`, then no primitive root can satisfy both `E_1=0` and `E_2=0`,
so the pattern and all Galois scalings are ruled out before the `E_3`
condition is used.  If `deg G12 > 0` but `deg G123 = 0`, the third elementary
equation rules out the remaining possible primitive-root scalings.

This is the same X33 common-gcd criterion, exposed as a staged proof route.

## What Remains

The next proof target suggested by the data is:

```text
For non-antipodal h=4 top-level first-sum gates, prove G12=1 except for
a structured small tail; then show the tail is killed by E3 or paid.
```

This packet does not claim that theorem.  It records the exact shape of the
obstruction in small rows and gives a verifier-backed target for a general
argument.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x34_h4_staged_gcd_anatomy.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x34_h4_staged_gcd_anatomy.py --write-certificate
```
