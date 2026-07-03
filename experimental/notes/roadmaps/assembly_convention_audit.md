# ASSEMBLY-AUDIT: convention consistency packet

- **DAG node:** `safe_assembly_uniformity`.
- **Task:** ASSEMBLY-AUDIT, X-10 support wave.
- **Verifier:** `experimental/scripts/verify_assembly_convention_audit.py`.
- **Certificate:** `experimental/data/certificates/assembly-convention-audit/assembly_convention_audit.json`.
- **Status:** AUDIT.  Classified convention drift; no unclassified mismatch.

This packet audits the convention axes that must compose in the final
clean-rate assembly:

1. support-wise alignment definition;
2. exact-vs-`>=` agreement;
3. exchange-distance / `s` convention;
4. paid-strip clause form.

The verifier extracts convention-setting lines from:

- `qx13_pair_rank_ledger.md`;
- `xr_clean_poly_forcing_reduction.md`;
- `xr_smallcore_rungs_2a_2b.md`;
- `w2_graded_tangent_ledger_design.md`;
- `a2_graded_tangent_bound.md`;
- `a1_staircase_cap_assembly.md`;
- `e33_deep_link_staircase.md`;
- `dihedral_staircase_deep_regime.md`.

## Findings

### 1. Support currency dual notation

This is a real mismatch, but it is classified.

`qx13_pair_rank_ledger.md` and the X-3 rungs use agreement supports `S` of
size `A`.  The dihedral staircase packet uses exact disagreement supports `R`
of size `j=n-A`.  Any composed proof must explicitly dualize

```text
R = H \ S,    |R| = j,    |S| = A.
```

The mismatch is notation/currency, not a mathematical contradiction.

### 2. Paid-strip scope layering

The clean compiler strips the proved quotient and tangent ledgers, then calls
the remaining slope mass `R_post`.  The A1/A2 packets use the later unified
pullback strip, which also includes the post-X-4/X-9 pullback classes.

These are different assembly layers.  The final proof should not silently
identify the compiler's quotient+tangent strip with the later unified strip.

### 3. Exactness inheritance gap

`qx13_pair_rank_ledger.md` and `xr_smallcore_rungs_2a_2b.md` pin exact
agreement/support conventions.  The W2, A2, and E33 packets route or count
aligned partners, but do not locally restate exact-vs-`>=` agreement.

The audit treats this as a documentation gap, not a falsifier: the packets are
using the inherited exact convention.  The final assembly should print that
inheritance once before invoking W2/A2/E33.

### 4. Exchange distance consistency

The `s` convention is consistent where used:

```text
r = |S cap T|,    s = A-r,    d = r-k,    d+s = t.
```

This matches QX.13's exchange distance and the W2/A2 partial-tangent cells.

## Verdict

The composed proof has no unclassified convention drift across the audited
packets.  The two required assembly hygiene rules are:

1. dualize dihedral disagreement supports before composing with agreement
   support packets;
2. print the inherited exact-agreement convention before invoking W2/A2/E33.

