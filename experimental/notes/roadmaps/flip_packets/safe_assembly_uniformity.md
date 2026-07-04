# Flip packet: safe_assembly_uniformity

- **Node:** `safe_assembly_uniformity`
- **Current critical label:** UNPROVED
- **Verdict:** DEFECT
- **Referee summary:** the node is trying to be a statement-level assembly
  implication, but its only req child, `descriptor`, is an artifact node rather
  than a truth-apt proposition. The local implication cannot be refereed until
  that child is reworded as a checkable descriptor theorem.

## Statement

> The implicit lemma 'counting_frame + fm1 + strip + paid_closure + r2 + ext_lift => mca_safe' holds UNIFORMLY over the admissible family: (i) every exponent (B <= 3, B_F, budget arithmetic) is an absolute constant, not n-drifting; (ii) the stratified sum + first-match dedup compose with endpoint conventions printed once (descriptor-generated); (iii) the composition survives k up to 2^40 scales symbolically (wp3_2). The last unpriced composite implication of the adjacency/payment-completeness class.

## Req Children

| child | live status | critical label | role |
|---|---:|---:|---|
| `descriptor` | TARGET | UNPROVED | Supposed source of the generated row constants and endpoint conventions. |

`descriptor` currently says:

> (p, e, s, rho) -> full derived row table, O(poly), double regression (pinned row + master table); sole source of dossier constants.

That is an artifact specification, not a proposition whose truth can imply the
uniform assembly statement. It does not state existence of the script,
regression success, convention coverage, or symbolic validity for all
admissible rows.

## Referee Argument

This packet cannot recommend `PROMOTE-CONDITIONAL`. If `descriptor` were a
truth-apt proposition saying, for example,

```text
symbolic_row_descriptor_exists_and_validates:
  the descriptor generator exists, runs in poly(log q, s), reproduces the
  pinned row and master table regressions, and is the unique source for all
  constants consumed by the safe-side compiler over every admissible row.
```

then `safe_assembly_uniformity` would be close to a statement-level
implication: the assembly convention audit already classifies the remaining
currency, exactness, and strip-layer convention issues. But with the live child
as written, the parent would inherit an artifact, not a theorem.

The fix is precise: reword or split `descriptor` into a propositional node with
its verifier/certificate pins, then re-referee `safe_assembly_uniformity`
against that node. Do not promote this node before that repair.

## Evidence Pins

- `safe_assembly_uniformity`: `aea2d57ac82bf3f9`
- `descriptor`: `e7304c18f03a0d1c`

## Source Quotes

- `wp_detail/wp3_2_symbolic_scaling.md` gives the descriptor spec and
  acceptance tests: `(p, e, s, rho)` input, O(poly) output, pinned-row
  regression, and top-of-range master-table regression.
- `assembly_convention_audit.md` reports no unclassified convention drift, but
  only as an AUDIT packet; it does not turn the artifact child into a
  proposition.
