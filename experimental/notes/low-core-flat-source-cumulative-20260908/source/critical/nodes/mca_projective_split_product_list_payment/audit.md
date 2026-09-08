# Proof audit and provenance

Local hand proof, 2026-09-07; no external review or formal certification.
The upstream #1175 discussion is the source-contract context, not a
supplier of this projective counting lemma. Earlier immutable public
packet 72f99be8 contains none of this new result.

The required affine-product node already proves finite divisor classes
and coefficient dimension <=1, with generic degree cost (m+1)^(2s-1).
The new ingredient is an explicit degree-weighted count of the projective
classes before recovering affine scales. For the quartic specialization,
the old bound does not fit the row budget; the new one does.

Primary geometric background checked against the
[Stacks Segre embedding](https://stacks.math.columbia.edu/tag/01WD)
and [Hilbert polynomial lemma](https://stacks.math.columbia.edu/tag/08AE).
The bidegree-(1,m) embedding, its monomial Hilbert function, and the
finite-fiber hyperplane argument are proved in this packet. The proper
hyperplane degree fact comes through the required graph supplier's
`algebraic_list_bound.md`. No finite-field genericity assumption occurs:
the choices of hyperplanes are over algebraically closed constants.

Load-bearing checks in the hand argument:

- product R is nonzero, so every factor is a valid projective point;
- bounded poles and fixed divisor sum give both upper and lower orders;
- all monomials, including mixed ones, appear in the embedding even if
  the characteristic divides m;
- hyperplanes are chosen nonzero on EVERY remaining component;
- affine offsets add a projective dimension unless their coset contains zero;
- the asymmetric scale equation lambda*mu^m=c^(-1) leaves m choices
  in one mixed case, and potentially many in the both-linear case;
- the latter class count pays actual common zeros before using incidence;
- fixed rational offsets are never evaluated at a pole in that argument;
- constant factor directions, not arbitrary moving directions, preserve V.

The canonical Fable tree was inspected read-only at 0dd5b324. Its
Segre/product statement matches concern other rank/owner constructions;
no matching split-product joint-list supplier was found in that targeted
search. This is not an exhaustive non-overlap or literature claim.

The controls audit exact small identities and integer prices only. The
finite consumer retains all labels and original near. General integral
quartics, source transport, higher ranks and both prizes remain open.
