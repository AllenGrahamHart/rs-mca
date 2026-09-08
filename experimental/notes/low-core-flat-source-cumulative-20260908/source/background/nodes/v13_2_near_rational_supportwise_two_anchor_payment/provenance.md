# Provenance

- Upstream packet: przchojecki/rs-mca PR `#1160`,
  `[MCA] Repair support-wise near-rational reduction by 2w`.
- Audited source commit:
  `c5f4ea7a0c78828c901ae5f3428894a8b2e2806b`.
- Audited source note:
  `experimental/notes/thresholds/kb_mca_supportwise_near_rational_two_anchor_repair_v1.md`.
- Public-DAG source imported by upstream and reused here:
  `v13_2_near_rational_pair_proximity`.

The proof in this node was checked independently from the displayed
hypotheses. Its validity does not depend on PR `#1160` being merged.

Coordinator audit 2026-08-12: proof line-verified against the upstream
threshold note at `c5f4ea7a`; independent second code path added
(`verify_audit.py`, exhaustive `mu_16` census + fresh-field `F_29`
falsifier replay + deployed-row arithmetic). The upstream packet's
reconciliation section read our DAG at head `3edb8b31` (2026-08-10),
which predates this node; its claim that our `GF(17)` fixture "does not
refute the final displayed one-slope inequality" was true of that head
but is superseded by the `mu_16` witness banked here at `45b01e4e0`.
