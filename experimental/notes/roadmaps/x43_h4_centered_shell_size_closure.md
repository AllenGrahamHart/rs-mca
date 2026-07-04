# X43: h=4 centered shell-size closure

- **DAG node:** `x43_h4_centered_shell_size_closure`.
- **Consumer:** `active_core_count_bound`.
- **Status:** proved criterion plus certificate replay.
- **Verifier:** `experimental/scripts/verify_x43_h4_centered_shell_size_closure.py`.
- **Certificate:**
  `experimental/data/certificates/x43-h4-centered-shell-size-closure/x43_h4_centered_shell_size_closure.json`.

## Statement

Let

```text
m_s = #{{x,y} subset H : x+y=s},        s != 0,
```

be the nonzero pair-sum shell sizes.  If

```text
max_s m_s <= 4,
```

then the h=4 centered affine branch is below `n^2`, hence far below the
rewired `n^3` terminal column.  If `max_s m_s <= 3`, the centered branch is
empty.

## Proof

X42 proves

```text
R_centered <= sum_{s != 0} C(m_s,4).
```

If `m_s <= 3`, then `C(m_s,4)=0`.

If `m_s <= 4`, then

```text
C(m_s,4) <= m_s/4
```

for every shell.  Therefore

```text
R_centered <= (1/4) sum_{s != 0} m_s.
```

The sum of the shell sizes is at most the number of unordered pairs in `H`:

```text
sum_{s != 0} m_s <= C(n,2).
```

So

```text
R_centered <= C(n,2)/4 < n^2.
```

This closes the centered affine branch under the one-number shell-size
condition `max_s m_s <= 4`.

## Replay Against X42

The verifier reads the X42 certificate and checks the criterion on every row
audited there.  All campaign rows in X42 satisfy the small-shell criterion:

```text
n=32,  alpha=2
n=64,  alpha=2
n=128, alpha=2 and 3
n=256, alpha=2
```

The low-characteristic stress rows deliberately violate the criterion and have
nonzero centered residue, showing that the hypothesis is real rather than
cosmetic.

## Consequence

The centered affine branch now has a compact terminal-side closure target:

```text
prove or certify max_{s != 0} m_s <= 4.
```

This is much weaker than proving pair-sum injectivity, and it is enough to
charge the branch below `n^2`.

## Verification

Run:

```bash
python3 experimental/scripts/verify_x43_h4_centered_shell_size_closure.py
```

To refresh the certificate:

```bash
python3 experimental/scripts/verify_x43_h4_centered_shell_size_closure.py --write-certificate
```
