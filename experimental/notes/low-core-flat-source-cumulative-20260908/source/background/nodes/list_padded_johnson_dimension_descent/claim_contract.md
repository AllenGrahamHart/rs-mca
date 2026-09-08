# Claim contract and provenance

Shared-carrier joint continuation, 2026-09-07: every component lies
in a translate of one polynomial space V, whose dimension is charged.
Arity is unrestricted, and agreement is joint on the same coordinates.
The tuple's affine dimension need not equal dim V. The compiler is
unchanged; all padding and anchor maps act on every component. This
does not supply an MCA ownership or multiplicity bound by itself.

Original scalar contract:

- Object/unit: distinct ordinary scalar codewords, not slopes or supports.
- Scope: every affine carrier of the declared dimension, every receiver,
  every distinct-point domain, and every K in the printed corridor.
- Same finite field throughout; q>=r+K_max supplies padding points.
- This is a direct elementary reconstruction of ordinary Johnson counting
  and shortening. The idea parallels the local MCA padded compiler, but
  the zero-cost LIST removal is proved here and imports no MCA/Hensel cap.
- Falsifier: a legal list exceeding a chosen cap, a padding field without
  enough points, or a noninjective claimed list transfer.
- Nonclaim: a direct LIST-to-MCA theorem, or optimality of chosen caps.
