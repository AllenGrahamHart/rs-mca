# P3: post-strip rich-line cap residue

- **DAG:** `deep_link_staircase`.
- **Status:** RESOLVED by F3 under the unified pullback strip.  The old
  tangent/quotient/dihedral strip alone still has the negative obstruction
  recorded below.
- **Verifier:** `experimental/scripts/verify_p3_rich_line_residue.py`.
  F3 replay: `experimental/scripts/verify_f3_net_absorption.py`.

## F3 Resolution

F3 proves that the named residue is not primitive after the unified strip is
adopted.  In the fixed-subcore plane each off-core point gives an affine branch
`L_i(z)=alpha_i+beta_i z`.  At any multi-direction rich point, a pivot branch
and every other incident branch give a nonzero degree-1 equality fiber
`L_i-L_0`; the `b=2` fiber dictionary records the pair by
`e_1=L_0+L_i`, `e_2=L_0L_i`.  These mixed pair cells cover the rich block.

Thus affine nets are paid mixed degree-1 pullback trades.  See
`f3_net_absorption.md`.

## Conclusion

The P3 cap was not proved by the pre-unified paid strip

```text
tangent pencil + quotient-with-tails L_B(X)G(X^M) + dihedral/Chebyshev.
```

The remaining residue under that old strip was:

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

F3 supplies the missing classification statement:

```text
After the paid strip, no affine-net rich-line residue remains.
```

Specifically, every affine-net residue is a mixed degree-1 pullback trade under
the unified strip.

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
