# Source Custody And Overlap

## Immutable Inputs

    upstream main: 93fba1be3f3299b0ba4708d88715377bbb656e45
    outbound parent: 3e97eb8bc65acfc3f6ce3d88aed56b3a6de96238
    research HEAD: 3b51e86d2595f28a02e842c81effca1dfcf98e77
    canonical prize: 0dd5b324482194208be0289f76ed3f0817648a46

The research tree is DIRTY. HEAD is a lineage pin, not a claim that it
contains the new results. Every exported source is bound independently
by its original path and SHA256 in SOURCE_MANIFEST.json.

    SOURCE_MANIFEST.json SHA256:
    e6b1399a5fb0646bf417abafa065fea72454345b5009778e05a98f15c6d830ce

The snapshot contains 63 new source files (177434 bytes), six new roots
and a 22-node all-PROVED required closure. It compares 49 unchanged
inherited proof documents and checks 1741 earlier listed source hashes
across 26 supplier manifests. Including the new files gives 1804 listed
source hashes; this is not a count of distinct theorems.

The replay uses the previous pinned inventory helper:

    packet: kb-raw-one-rank-nineteen-source-tail-20260911
    replay.py SHA256:
    e7291f047e48b42ae6fad27652201f16a7928af1fcc95823413944c1e93491d9
    SOURCE_MANIFEST.json SHA256:
    6077c2be5adb36136cd3ad062e1a278c07616fed053085a28b4a740a1759bae7

Published predecessor sources are not rewritten. Canonical prize is
read-only; it is not the source of a new unreviewed import this cycle.

## Attribution And Novelty Boundary

The source repository derives from Przemek Chojecki's RS-MCA program.
Node-local provenance files retain individual supplier attribution.
The new proofs and arithmetic audits were developed in the Codex research
tree for AllenGrahamHart; independently written arithmetic checks are
not external independent mathematical acceptance.

Relative to the preceding rank/projection packet, the new content is
four original-source receiver conditions without P1/P2 rank restrictions,
two generic colour lemmas, and a stronger actual-profile source inequality.
They do not replace the earlier rank/projection proofs or widen their scopes.

## Live Overlap Check

Current main, agents.md, its newest integration-log entry, and the live
four-row compiler were checked on 2026-09-11. Main is unchanged at the
pin above; all four compiler rows still say RED_OPEN_EXACT_INPUTS_MISSING.
No compiler was rerun and no null atom was filled.

Metadata for all 62 open PRs was refreshed. Relevant heads are unchanged:

| PR | Head |
|---|---|
| 1179 | c4e4e7918764a590c4b8cfeac11004d297e2480b |
| 1180 | 478bfc41278c7669543388107a2fabff4b9fbd1b |
| 1181 | 8543d330a9356df7a7b366e79c8105fd8d2173e1 |
| 1182 | c24afd9b961bee43eaf335a6278160465d880c53 |
| 1183 | 3b0db2af019b988945865e7a06e9614495e337fc |

This is scoped consolidation with #1180. It does not consume the
provisional marked-triple or selector-envelope results in #1181..1183,
nor modify those branches. All required source proofs are in the
manifest, independent of those provisional claims.

A bounded term/constant check of the current experiments.tex and
grande_finale.tex found no matching receiver-colour, trimmed-profile or
new endpoint statement. This is not an exhaustive novelty audit of all
62 PR proofs. The mathematical extension claimed here is relative to our
explicitly pinned preceding packet, not a priority claim over other authors.

Publication means EXPORTED FOR REVIEW only. No theorem is marked
accepted, merged or banked merely because its files are available.
