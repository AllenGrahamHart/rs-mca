# X44: h=4 centered max-shell bound

- **DAG node:** `x44_h4_centered_max_shell_bound`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved criterion plus finite replay.
- **Verifier:** `experimental/scripts/verify_x44_h4_centered_max_shell_bound.py`.
- **Certificate:**
  `experimental/data/certificates/x44-h4-centered-max-shell-bound/x44_h4_centered_max_shell_bound.json`.

## Statement

Let

```text
m_s = #{{x,y} subset H : x+y=s},        s != 0,
M = max_s m_s.
```

Then the centered affine h=4 branch satisfies

```text
R_centered <= C(M,4) C(n,2) / M.
```

Consequently any row with

```text
C(M,4) C(n,2) / M <= n^3
```

has the centered affine branch safely inside the rewired terminal column.

## Proof

X42 gives the exact accounting bound

```text
R_centered <= sum_s C(m_s,4).
```

For `m >= 4`, the ratio

```text
C(m,4)/m = (m-1)(m-2)(m-3)/24
```

is increasing in `m`.  Therefore, for every shell with `m_s <= M`,

```text
C(m_s,4) <= (C(M,4)/M) m_s.
```

Summing over nonzero shells gives

```text
R_centered
  <= (C(M,4)/M) sum_s m_s
  <= (C(M,4)/M) C(n,2).
```

The last inequality uses that the nonzero shells partition a subset of the
unordered pairs of `H`.

## Why This Improves X43

X43 closed the centered branch under `M <= 4`.  That condition is sufficient
but too strict: in the full `n=64` boundary window, one prime has `M=6`.
X44 still closes it immediately:

```text
R_centered <= C(6,4) C(64,2)/6 = 5040 < 64^3.
```

The verifier also computes the exact centered energy in that full window; it
is zero in every row.

## Replay

The verifier records:

- low-characteristic stress rows where centered trades are nonzero, confirming
  the branch is real;
- selected campaign rows including an `M=6` row and an `M=5` row;
- the full `n=64`, `n^2 < p <= n^3`, `p == 1 mod n` boundary window.

The full `n=64` window has one row where X43 fails (`p=7937`, `M=6`), but the
X44 bound and the exact centered count both remain harmless.

## Consequence

The centered affine branch can now be certified row-wise by a single number:

```text
M = max nonzero pair-sum shell size.
```

No h=4 support sort is required.  If `M` stays constant, this branch is
`O(n^2)`; if the displayed row inequality holds, it fits the compiler column.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x44_h4_centered_max_shell_bound.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x44_h4_centered_max_shell_bound.py --write-certificate
```
