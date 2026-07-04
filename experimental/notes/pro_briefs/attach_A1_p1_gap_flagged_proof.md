# p1_post_paid_subcore_richline_cap proof

## Claim

After the unified paid strip, the number of aligned partners through any fixed
near-`k` subcore is bounded by an absolute constant.

## Inputs

- The P1 subcore reduction: for a fixed near-`k` subcore, any failure of the
  constant partner cap is a rich line in the normalized `(z,a)` parameter
  plane, except for the already-paid tangent, quotient-with-tails, and
  dihedral families.
- `p3_affine_net_richline_residue`: the only remaining rich-line residue,
  namely multi-direction affine nets in that plane, is charged by mixed `b = 2`
  degree-1 pullback cells under the unified strip.

## Proof

Fix the received pair, anchor support, and near-`k` subcore `Q`. Apply the P1
subcore reduction to the family of aligned partners passing through `Q`.
Partners falling into tangent pencils, quotient-with-tails, or dihedral
staircases are removed by the paid strip.

If the post-strip family through `Q` were not bounded by an absolute constant,
the P1 normal form forces a rich-line configuration in the `(z,a)` parameter
plane. The reduction's named residue is exactly the multi-direction affine-net
case; no other uncharged rich-line type remains in the fixed-subcore normal
form.

The node `p3_affine_net_richline_residue` proves that every such affine net is a
mixed degree-1 pullback trade and is therefore also removed by the unified
strip. Hence a post-strip, uncharged, unbounded partner family through the fixed
subcore cannot exist.

The residual non-rich-line cases are the tame cases already bounded by the P1
interpolation step. Combining the tame local bound with the charged affine-net
residue gives a constant `C` independent of `n`, `q`, and the ambient row.

This proves the fixed-subcore cap. It does not by itself prove
`deep_link_staircase`: that downstream node still requires the separate
occupied-subcore accounting which counts how many active subcores can occur.
