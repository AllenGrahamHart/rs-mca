# Flip packet: worst_word_planted

- **Node:** `worst_word_planted`
- **Current critical label:** UNPROVED
- **Verdict:** PROMOTE-CONDITIONAL
- **Referee summary:** the earlier E15 defect has been repaired in the live DAG
  by adding `worst_word_challenger_pricing`. With that child and `imgfib`
  granted, the parent is now an assembly statement: the supremum is carried by
  the planted class plus the priced/exhausted challenger class.

## Statement

> REVISED per the E15 COUNTEREXAMPLE (#197): the naive planted-only form is FALSE — a structured low-slack NON-planted challenger exists at sigma = 1 in the toy cell. Revised statement: at the crossing radii the sup-over-words list is attained by the planted sunflower family OR the E15 structured challenger class, and list_planted_arithmetic must price BOTH classes exactly. The challenger is structured (not a fifth-mechanism signal); the endgame arithmetic gains one classified column.

## Req Children

| child | live status | critical label | role |
|---|---:|---:|---|
| `imgfib` | CONDITIONAL | CONDITIONAL | Safe-side image-fiber bound; excludes unpriced extras once the modeled worst classes are fixed. |
| `worst_word_challenger_pricing` | TARGET | UNPROVED | Prices or exhausts the E15 structured challenger class so the revised sup-over-words claim is carried by planted plus challenger classes jointly. |

The sibling `list_planted_arithmetic` is not a req child of this node, but is a
req child of `list_adjacency_closing`; it is the arithmetic consumer that prices
the planted/challenger columns after this extremal-class reduction is granted.

## Referee Argument

The previous defect was that the revised statement mentioned an E15 challenger
class while the DAG only wired `imgfib`. That is no longer the live graph:
`worst_word_challenger_pricing` is now a req child and its statement is exactly
the missing modeled-class obligation:

```text
Price or exhaust the structured low-slack NON-planted challenger class ...
so the revised worst_word_planted statement's sup-over-words claim is carried
by planted + challenger classes jointly.
```

Granting that child supplies the non-planted column and its exhaustion/pricing
claim. Granting `imgfib` supplies the global image-fiber bound used to prevent
unpriced extras from escaping the modeled worst-word classes. The planted
column arithmetic is consumed one level up by `list_adjacency_closing` through
`list_planted_arithmetic`, which is already wired there.

So the current node should no longer be a red wiring defect. Its hard content
has been pushed into `worst_word_challenger_pricing` and `imgfib`; as a parent
assembly statement it should be `CONDITIONAL`.

## Caution

This packet does not prove the challenger child, nor does it prove the list
window arithmetic. It only certifies that the live `worst_word_planted` node now
has the req children needed for the revised E15 form to be an amber assembly
node.

## Evidence Pins

- `worst_word_planted`: `260596841634e691`
- `imgfib`: `0701cb2b6f534e11`
- `worst_word_challenger_pricing`: `530e4054a353aeda`
- `list_planted_arithmetic`: `981bbfa57a032011`

## Source Quotes

- `campaign_report_02_falsification_ledger.md` records the E15 falsifier and
  repair: planted-family OR E15 structured challenger class.
- `evidence_plan_codex.md` E22 states the intended successor task: decide
  whether planted plus the E15 structured class exhaust the extremal words and
  extract the challenger count formula.
- `execution_queue.md` QL.5 says the challenger class must be priced alongside
  planted counts in `list_planted_arithmetic`.
