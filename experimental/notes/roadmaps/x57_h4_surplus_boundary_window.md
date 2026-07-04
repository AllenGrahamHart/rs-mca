# X57: h=4 surplus boundary-window census

- **DAG node:** `x57_h4_surplus_boundary_window`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite-window test.
- **Verifier:** `experimental/scripts/verify_x57_h4_surplus_boundary_window.py`.
- **Certificate:**
  `experimental/data/certificates/x57-h4-surplus-boundary-window/x57_h4_surplus_boundary_window.json`.

## Statement

X51 checked the max-shell X50 condition on complete boundary prime windows.
X55 and X56 sharpen that target to the aggregate anchored h=2 surplus barrier

```text
A_anchor_surplus < 4 * C(T(n)+1, 2).
```

This packet exhaustively checks the stronger X56 surplus barrier on the same
complete windows

```text
n^2 < p <= n^3,       p == 1 mod n,
n in {32, 64, 128, 256, 512}.
```

## Method

For each row, reuse the X51 quotient invariant

```text
(1+r)^n,
```

for `r in H`, excluding `r=1` and `r=-1`.  If the quotient bucket sizes are
`2 m_C`, compute

```text
A_anchor_surplus = 4 * sum_C C(m_C, 2)
```

as proved in X56, and check the strict X56 barrier.

This remains a quotient-shell census.  It does not enumerate h=4 supports.

## Results

```text
n     primes   barrier   max A_anchor_surplus   margin   rows attaining max
32    212      364       24                     340      1217
64    693      544       104                    440      7937
128   2411     840       88                     752      65537
256   8383     1300      168                    1132     107777
512   29774    1984      316                    1668     320513
```

Every row in every checked boundary window satisfies the X56 surplus barrier.
The largest observed anchored surplus is `316`, still well below the `n=512`
barrier `1984`.

## Interpretation

The aggregate surplus target is not only compatible with the boundary data; it
has substantially more empirical slack than the max-shell target suggests.
The stress is specific-prime and low-dimensional, not a generic density
phenomenon.

This supports the next proof target stated by X56:

```text
For p >= n^2, nonzero sparse h=2 norm-gate surplus inside shifted
subgroup shells is O(n^(2/3)) in anchored currency,
```

or a p-specific exclusion strong enough to imply the X56 barrier.  The full
boundary windows through `n=512` show no counterexample to that target.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x57_h4_surplus_boundary_window.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x57_h4_surplus_boundary_window.py --write-certificate
```
