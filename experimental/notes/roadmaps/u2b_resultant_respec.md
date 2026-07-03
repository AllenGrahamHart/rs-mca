# U2-B-RESPEC: resultant certifier contract

- **DAG node:** `u2_per_row_certifier`.
- **Task:** U2-B-RESPEC, X-10 support wave.
- **Verifier:** `experimental/scripts/verify_u2b_resultant_respec.py`.
- **Certificate:** `experimental/data/certificates/u2b-resultant-respec/u2b_resultant_respec.json`.
- **Status:** RESPEC.  The certifier route is specified, but U2-B remains
  `TARGET`.

## Outcome

The low-memory resultant route is viable as a checker for a finite pattern
list, but it is not yet a complete certifier for the Row-C-class cells.

The verifier consumes U2-A and confirms:

- the prize rows have empty small-block windows, so U2-B has no prize-row
  small-window certificate to produce;
- the only live base rows are the three Row-C-class rows;
- the Row-C prime is currently unpinned in `xr_budget_audit.md`;
- raw subset enumeration is not a low-memory route, even before the full
  grammar window.

## Live Windows

U2-A gives the live Row-C cells:

```text
RowC rate 1/4:  n=1024, t=5, b=6..100
RowC rate 1/8:  n=1024, t=5, b=6..100
RowC rate 1/16: n=1024, t=3, b=4..100
```

For the proposed first stage `b <= 20`, the verifier lower-bounds the number
of dihedral-orbit normal forms by dividing the raw subset count by `2n`.
Already this gives about

```text
2^127
```

normal forms.  For the full Row-C grammar window `b <= 100`, the same lower
bound is about

```text
2^457.
```

Thus the phrase "enumerate sparse-relation patterns" cannot mean raw exponent
subsets, even modulo dihedral symmetry.  A future complete certifier needs a
proved compressed normal-form generator or a separate elimination theorem that
produces a finite candidate list.

## Resultant Kernel

For a fixed exponent pattern `E`, row length `n=2^m`, depth `t`, and row prime
`p`, the checker works modulo `p`:

```text
Phi_n(X) = X^(n/2) + 1,
P_r,E(X) = sum_{e in E} X^(r e),   1 <= r <= t.
```

If

```text
gcd(Phi_n, P_1,E, ..., P_t,E) = 1  in F_p[X],
```

then the row prime does not divide the common resultant/norm obstruction for
that pattern, so the pattern is ruled out at that row.

The verifier includes the F2 witness sanity check:

```text
n=64, t=3, E={0,1,2,4,16,45,50,60}.
```

At `p=193` the common gcd has positive degree, detecting the known witness.
At `p=641` the common gcd has degree zero, ruling out that same pattern at the
clean prime.

## Certifier Contract

A complete U2-B certificate needs four inputs:

1. a pinned row characteristic/prime `p`;
2. the row parameters `n,t`;
3. a finite normal-form list of exponent patterns
   `E` with `t < |E| <= floor(log2 n)^2`;
4. a coverage proof that the finite list exhausts all primitive patterns not
   already charged by quotient, dihedral, boundary, or pullback classes.

The resultant checker can then verify each listed pattern by the gcd test
above.  Without both the pinned prime and the exhaustive compressed pattern
list, U2-B must remain `TARGET` and should fail closed in Reading-B semantics.

