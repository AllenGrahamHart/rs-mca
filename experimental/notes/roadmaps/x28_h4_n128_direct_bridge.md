# X28: n=128 direct h=4 bridge to the quotient ledger

- **DAG node:** `x28_h4_n128_direct_bridge`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite evidence.
- **Verifier:** `experimental/scripts/verify_x28_h4_n128_direct_bridge.py`.
- **Certificate:**
  `experimental/data/certificates/x28-h4-n128-direct-bridge/x28_h4_n128_direct_bridge.json`.

## Scope

X27 measured the cheap quotient h=2 ledger for the h=4 antipodal-lift
mechanism in the full `n=128,256` boundary windows.  X28 checks selected
`n=128` primes directly in h=4 support space and compares the observed
fingerprints with the quotient prediction.

The selected primes are:

```text
17921, 33409, 65537, 665857, 697601, 2095361.
```

They include:

- the first boundary prime `17921`;
- a lower extra row `33409`;
- the maximum X27 `n=128` quotient-extra row `65537`;
- two other high extra rows `665857` and `697601`;
- a clean high-end row `2095361`.

This is a selected-row bridge, not a full `n=128` h=4 prime-window sort.

## Method

For each selected prime the verifier enumerates all h=4 supports in `mu_128`,
sorts by the top-three elementary symmetric signature, and counts anchored
disjoint partners.  Supports are packed as `uint32` four-tuples, so the scan is
still low-memory compared with Python-int support masks.

Each anchored h=4 partner is classified by the X20 fingerprints:

```text
mu4_full_fiber
antipodal_h2_quotient_lift
other
```

The resulting counts are compared against the X27 quotient h=2 row:

```text
mu4_full_fiber count                 = zero-sum quotient baseline
antipodal_h2_quotient_lift count     = extra quotient h=2 sum collisions
raw anchored h=4 count               = total quotient h=2 collisions
```

## Results

```text
p        collision groups   raw h=4   mu4   antipodal lift   quotient extra   other
----------------------------------------------------------------------------------
17921          193             43      31          12               12           0
33409          321             67      31          36               36           0
65537          257             83      31          52               52           0
665857         193             71      31          40               40           0
697601         193             71      31          40               40           0
2095361          1             31      31           0                0           0
```

Every selected direct h=4 row matches the quotient prediction exactly.

## Interpretation

X27 showed the lower h=2 quotient exception mechanism stays sparse and paid in
the large boundary windows.  X28 verifies, on selected `n=128` rows with actual
h=4 support sorting, that the observed h=4 active pairs are exactly that lower
quotient ledger:

```text
actual h=4 row = mu_4 baseline + antipodal quotient h=2 lift.
```

This strengthens the working h=4 structural target but does not prove it.  The
remaining proof obligation is still the uniform structural exclusion:

```text
all h=4 finite-p reductions are full mu_4 fibers,
antipodal quotient h=2 lifts, or genuine primitive residue.
```

The selected large-row evidence finds no genuine primitive residue.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x28_h4_n128_direct_bridge.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x28_h4_n128_direct_bridge.py --write-certificate
```

Current replay: **53 PASS, 0 FAIL**.
