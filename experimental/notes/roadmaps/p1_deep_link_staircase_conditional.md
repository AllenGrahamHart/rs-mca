# P1: deep-link staircase, conditional proof packet

DAG node: `deep_link_staircase`.

Status: CONDITIONAL.  The E33 measurement route is now algebraically reduced
to a precise missing lemma.  The raw statement is not true for arbitrary
received pairs before the paid/tangent stripping convention is imposed.

## 1. Setup

Let `C=RS[H,k]`, `A=k+t`, and fix an aligned anchor

```text
(T0, z0, c0),       |T0|=A,
```

for a pair `(u,v)`.  A partner is another alignment `(T,z,c)` with
`z != z0` and

```text
r = |T cap T0|,       k/2 < r < k.
```

The target is a linear bound in `n` for the number of such partner events
after paid strata have been removed.

## 2. The Exact Subcore Reduction

The first nontrivial boundary is a fixed `(k-1)`-subcore

```text
R subset T0,       |R|=k-1.
```

Choose the monic degree-`k-1` polynomial

```text
h_R(X)=prod_{x in R}(X-x).
```

For a finite slope `z`, every codeword `c` agreeing with `u+zv` on `R`
has the form

```text
c = p_z + a h_R,
```

where `p_z` is any fixed degree-`<k` interpolation of `u+zv` on `R`, and
`a` is one free scalar.  For an off-core point `x`, the extra agreement
condition is therefore one affine line in the parameter plane `(z,a)`:

```text
u(x)+zv(x) = p_z(x)+a h_R(x).
```

Thus partners through `R` are exactly rich points of the induced affine line
arrangement: a parameter `(z,a)` with at least `t+1` off-core incident lines
gives agreement on `R` plus those `t+1` points, hence agreement at least
`A`.

This is the algebraic form of the E33 signal.  The observed "maximum 5 through
one fixed subcore" is a statement about rich points in this special line
arrangement after stripping, not a formal consequence of qx13 alone.

## 3. Why The Raw Cap Is False

The coefficients of the off-core lines contain the arbitrary values of
`u` and `v` off `R`.  Before paid stripping, they can realize rich line
arrangements.

The verifier embeds the three-family arrangement

```text
H_i: a=i,
P_j: a=z+j,
N_l: a=-z+l.
```

The triples `H_i,P_j,N_l` meet when `z=i-j` and `l=2i-j`.  For `m=10` this
produces more rich parameters than the ambient block length `n`, all through
one fixed `(k-1)`-subcore, and the verifier embeds them as actual RS
alignments over `F_211` with `k=4,t=2,A=6`.

So the unconditional theorem

```text
every fixed near-k subcore supports O(1) partners
```

is false for arbitrary received pairs.  The missing statement must be a
post-paid statement: after tangent/rich-line arrangements have been charged,
each fixed deep subcore has bounded residual richness.

## 4. Conditional Theorem

Define the missing P1 input:

```text
DL-cap(L,B):
  For every fixed pair and anchor T0 after paid stripping,
  the near-k partner set admits a canonical witness map to at most B*n
  occupied deep subcores, and each occupied deep subcore supports at most L
  residual partner events.
```

Then P1 follows immediately:

```text
# partners <= L * B * n.
```

This is the complete counting proof once the post-paid rich-line cap and the
occupied-subcore accounting are supplied.  E33 calibrates the expected
constants: `L<=5` on both toy rows for fixed-subcore occupancy, and total
maxima `13` at `F_97` and `72=4.5n` at the denser `F_17` stress row.

## 5. Named Gap

The named gap is:

```text
p1_post_paid_subcore_richline_cap
```

Statement: after quotient/dihedral/extension/tangent-pencil stripping, the
affine line arrangement induced by every fixed deep subcore has uniformly
bounded residual `(t+1)`-rich points, and the occupied subcores are
linearly many in `n`.

This is exactly the route selected by E33.  The packet proves the reduction
and the final counting implication; it does not prove the post-paid cap.

## Verifier

Run:

```bash
python3 experimental/scripts/verify_p1_deep_link_staircase_conditional.py
```

The recomputed summary is pinned in
`experimental/data/certificates/p1-deep-link-staircase-conditional/p1_deep_link_staircase_conditional.json`.
