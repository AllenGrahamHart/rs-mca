# X55: h=4 surplus-threshold bridge

- **DAG node:** `x55_h4_surplus_threshold_bridge`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved sufficient surplus barrier.
- **Verifier:** `experimental/scripts/verify_x55_h4_surplus_threshold_bridge.py`.
- **Certificate:**
  `experimental/data/certificates/x55-h4-surplus-threshold-bridge/x55_h4_surplus_threshold_bridge.json`.

## Statement

Let `T(n)` be the exact X50 shell threshold, so that the centered h=4
branch is inside the rewired terminal `n^3` column whenever

```text
M <= T(n),
```

where `M = max_C m_C` is the quotient-coset shell maximum.

Let

```text
N_surplus = n * sum_C C(m_C, 2)
```

be the X54 h=2 norm-gate shell surplus.  If

```text
N_surplus < n * C(T(n)+1, 2),
```

then `M <= T(n)`, hence X50 closes the centered h=4 branch.

This is a sufficient condition, not a necessary one.

## Proof

If some quotient shell has size

```text
M >= T(n)+1,
```

then X54 gives the forced surplus lower bound

```text
N_surplus >= n * C(M, 2) >= n * C(T(n)+1, 2),
```

because `C(m,2)` is increasing for `m >= 1`.  Therefore the strict
opposite inequality

```text
N_surplus < n * C(T(n)+1, 2)
```

rules out every over-threshold shell.  Thus `M <= T(n)`, and the X50
threshold theorem applies.

## Scale Comparison

The surplus barrier has the same exponent as the h=2 norm-gate surplus
scale:

```text
n * C(T(n)+1, 2) ~= 6.6 n^(5/3).
```

The verifier checks the comparison exactly, without floating point.  A
putative total-surplus bound

```text
N_surplus <= 6 n^(5/3)
```

would fit under the X55 barrier whenever

```text
216 n^2 < C(T(n)+1,2)^3.
```

This holds for every X50 threshold-table row, including `n=2^41`.  The
prime-field `2 n^(5/3)` scale is checked by the same integer comparison with
`8 n^2` on the left.

This does **not** assert that the existing h=2 line theorem already bounds
the total surplus `N_surplus`.  X53 showed that the fixed-line max-shell
route is too weak.  X55 only identifies the right aggregate surplus target:
an h=2 norm-gate surplus theorem at the `6 n^(5/3)` scale would be strong
enough for the h=4 centered branch.

## Replay

The certificate replays the X54 rows:

- rows satisfying the surplus barrier are verified to satisfy `M <= T(n)`;
- the `low_n64_p193` stress row is recorded as safe but not barrier-passing,
  which prevents reading X55 as a necessary criterion;
- every X50 scale row has enough exact surplus-barrier room for the
  `6 n^(5/3)` comparison.

## Consequence

The centered h=4 terminal branch has now been localized to one aggregate
lower-degree inequality:

```text
N_surplus < n * C(T(n)+1, 2).
```

By X54 this is a total h=2 sparse norm-gate surplus bound, not an h=4
support-counting problem.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x55_h4_surplus_threshold_bridge.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x55_h4_surplus_threshold_bridge.py --write-certificate
```
