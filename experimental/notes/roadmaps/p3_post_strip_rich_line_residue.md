# P3: post-strip rich-line cap residue

- **DAG:** `deep_link_staircase`.
- **Status:** CONDITIONAL / negative obstruction to the proposed proof.
- **Verifier:** `experimental/scripts/verify_p3_rich_line_residue.py`.

## Conclusion

The P3 cap is not proved by the current paid strip

```text
tangent pencil + quotient-with-tails L_B(X)G(X^M) + dihedral/Chebyshev.
```

The remaining residue is:

```text
p3_affine_net_richline_residue
```

It is the affine-line-arrangement residue inside P1's fixed-subcore reduction:
after normalizing by a fixed `(k-1)`-subcore, the off-core points define lines
in the `(z,a)` parameter plane, and many `(t+1)`-rich points can come from a
multi-direction affine net rather than from a pencil or a quotient/dihedral
full-fiber staircase.

## Verified Obstruction

The verifier embeds the P1 three-direction net on a 2-power multiplicative
domain:

```text
F_193,     domain mu_64,     k=4, t=2, A=6.
```

The line families are

```text
H_i: a=i,
P_j: a=z+j,
N_l: a=-z+l.
```

The triples `H_i, P_j, N_l` meet at `z=i-j`, `l=2i-j`.  With `m=10`, this
gives 65 intended rich parameters, more than the domain size `n=64`.  Each
rich parameter is verified as an exact aligned support of size `A=6` through
the same fixed `(k-1)`-subcore.

The verifier also checks:

```text
max multiplicity per rich point = t+1 = 3,
quotient-tail paid supports     = 0,
dihedral paid supports          = 0.
```

So the obstruction is not a tangent pencil, and it is not removed by the
local full-coset quotient-tail or dihedral full-fiber predicates.

## What This Means

P1's reduction is still correct:

```text
fixed deep subcore  ->  rich points of an affine line arrangement.
```

But P3 needs one more classification statement:

```text
After the paid strip, no affine-net rich-line residue remains.
```

Equivalently, either:

1. prove that every affine-net residue is secretly one of the paid strata under
   the full global definitions, or
2. add affine-net rich-line cells as a separate paid/residual stratum and
   charge them.

Without that extra statement, the constant per-subcore cap is false in the
local algebraic model that P1 proved.

## Conditional Cap

The clean conditional form is:

```text
If, after tangent, quotient-tail, dihedral, and affine-net stripping,
each fixed deep subcore has at most C residual (t+1)-rich parameter points,
then P1's counting theorem gives the deep-link staircase bound:

    # partners <= C * (# occupied deep subcores).
```

Together with occupied-subcore accounting, this is exactly the P1 route.  The
new work is the affine-net classification/charge, not the subcore algebra.

## Verification

Run:

```bash
python3 experimental/scripts/verify_p3_rich_line_residue.py
```

Current certificate replay: **10 PASS, 0 FAIL**.
