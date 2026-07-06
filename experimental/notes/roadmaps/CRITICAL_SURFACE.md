# THE CRITICAL DAG — the published surface

This folder holds the node artifacts of the CRITICAL DAG: the req-ancestry of
the two grand nodes (mca_grand, list_grand) plus any-gate alternates. This is
the surface we maintain to publication standard and host online. Everything
else lives in background/ — a sea of exploratory statements that is USEFUL BUT
NOT MAINTAINED; treat background content as unreliable until promoted.

## The three-color law (the entire status taxonomy of this surface)

- GREEN  (PROVED): the claim is true with a proof artifact in its folder.
  Computation claims are proved by a pinned result + replayable verifier.
  Law: every req child of a green node is green.
- AMBER  (CONDITIONAL): the implication "hypotheses => claim" is PROVED and
  every hypothesis is a wired req edge. Law: amber nodes are INTERIOR nodes
  (>= 1 wired hypothesis); when all hypotheses turn green, auto_discharge
  flips amber to green (modus ponens).
- RED    (TARGET): an open obligation. Law: red nodes are logical LEAVES —
  only ev/ref in-edges (nothing can logically depend on an unproved claim's
  internals; evidence may point at it). Artifact-closure targets (dossiers,
  tables) are the one exemption: their req edges stage ingredients (RIPE).

No other status may appear on this surface (validator-enforced). PROVABLE is
banned: a proof that "can just be written up" gets written up. A CONJECTURE
that lands on a req-path is owed — i.e. it IS a target.

Node semantics: EVERY node is a truth claim (the node-semantics law,
notes/CHAIN_COMPRESSION_POLICY.md). The DAG asserts: if the red leaves are
proved, the grands follow by the wired implications alone.
