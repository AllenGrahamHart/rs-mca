# X36: h=4 n=64 high-row power-gate check

- **DAG node:** `x36_h4_n64_highrow_power_gate`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite evidence.
- **Verifier:** `experimental/scripts/verify_x36_h4_n64_highrow_power_gate.py`.
- **Certificate:**
  `experimental/data/certificates/x36-h4-n64-highrow-power-gate/x36_h4_n64_highrow_power_gate.json`.

## Scope

X36 extends the X33/X35 signed `4+4` moment-gate evidence to the first
`n=64` row above `n^3`:

```text
F_262337 / mu_64,        262337 > 64^3,        262337 == 1 mod 64.
```

It is a single-row check, not the full X22 all-prime sweep.

## Result

The verifier enumerates all `C(64,4)=635376` h=4 supports, groups by `E_1`,
and checks the X35 signed power-sum common gcd on every anchored non-antipodal
first-sum candidate.

```text
anchored E1 pairs:              79341
non-antipodal top-level E1:     65856
antipodal E1:                   13485
top-three pairs:                15
top-level power-gcd survivors:  0
```

All top-three pairs are the paid `mu_4` baseline:

```text
15 = 64/4 - 1.
```

So at this high row the signed h=4 top-level branch is empty:

```text
gcd(Phi_64, S_1, S_2, S_3) = 1
```

for every anchored non-antipodal first-sum candidate.

## Interpretation

This is exactly the phenomenon suggested by X33-X35:

```text
first-sum norm gates exist,
but the full signed 3-moment gate kills all top-level h=4 candidates.
```

It extends the small-row checks from `n=16,32` to `n=64` at `q ~ n^3`, the
same high-q rung where the terminal node's empirical vanishing pattern is
strongest.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x36_h4_n64_highrow_power_gate.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x36_h4_n64_highrow_power_gate.py --write-certificate
```
