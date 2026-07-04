# X51: h=4 quotient-shell boundary-window census

- **DAG node:** `x51_h4_quotient_shell_window`.
- **Consumer:** `active_core_count_bound`.
- **Status:** exact finite-window test.
- **Verifier:** `experimental/scripts/verify_x51_h4_quotient_shell_window.py`.
- **Certificate:**
  `experimental/data/certificates/x51-h4-quotient-shell-window/x51_h4_quotient_shell_window.json`.

## Statement

X48 reduces the nonzero-centered h=4 shell statistic to

```text
m_C = (1/2) #{ r in H \ {1} : 1+r in C },
```

where `C` ranges over quotient cosets of `H = mu_n` in `F_p^*`.  X50 proves
that the centered branch is inside the terminal `n^3` column whenever

```text
M = max_C m_C <= T(n),
```

with `T(n)` the exact cube-root threshold.

This packet exhaustively checks that condition on the complete boundary prime
windows

```text
n^2 < p <= n^3,       p == 1 mod n,
```

for

```text
n in {32, 64, 128, 256, 512}.
```

## Method

Two elements `a,b in F_p^*` lie in the same `H`-coset exactly when

```text
a^n = b^n.
```

So the quotient coset of `1+r` is represented by

```text
(1+r)^n.
```

For each row, the verifier enumerates `r in H`, excluding `r=1` and `r=-1`.
The first exclusion removes diagonal ordered pairs; the second removes the
paid zero-sum antipodal shell.  It counts the values `(1+r)^n`; each quotient
ratio bucket has even size, and the shell size is half the bucket size.

This avoids h=4 support sorting and avoids discrete-log tables.

## Results

```text
n     primes   T(n)   max M   rows attaining max M
32    212      13     3       1217, 2113
64    693      16     6       7937
128   2411     20     4       65537, 665857, 697601
256   8383     25     5       91393
512   29774    31     5       265729, 285697, 330241, 366593, 566273
```

Across every checked boundary row, `M <= 6`.  This is far below both the exact
X50 threshold and the simpler sufficient cube-root threshold.

The coset image is broad throughout.  The minimum number of quotient cosets
hit in each full window is:

```text
n=32:  10
n=64:  19
n=128: 46
n=256: 92
n=512: 193
```

## Interpretation

The X50 threshold is not tight in boundary-window data.  The observed behavior
is closer to a bounded-shell or logarithmic-shell statement than to the
allowed `n^(1/3)` threshold.

This suggests the next proof target should not be a delicate optimization of
X49.  A much coarser shifted-subgroup intersection theorem would already close
the centered h=4 branch:

```text
max_C #{ r in H \ {1} : 1+r in C } = O(n^{1/3})
```

at official rows, while the data through `n=512` is consistent with `O(1)`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x51_h4_quotient_shell_window.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x51_h4_quotient_shell_window.py --write-certificate
```
