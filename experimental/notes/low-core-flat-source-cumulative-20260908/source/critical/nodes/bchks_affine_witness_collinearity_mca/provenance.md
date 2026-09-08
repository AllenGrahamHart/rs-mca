# Provenance and import boundary

Exact-gate continuation (2026-09-06): reread the first primary source's
Lemma 3.1 and following smaller-m paragraph, printed pp.22-23. That
paragraph already supplies the max(Y,Z_0) interpolation extension.
The local companion verifies its use with the rounded chosen-witness
assembly, weakens the agreement gate to X<=m*a, and proves the
remaining collinearity load at m=1,2. This does not adopt the exact
sketched MCA constant or change the outstanding external-review boundary.

Primary mathematical sources:

1. Ben-Sasson, Carmon, Habock, Kopparty and Saraf, *On Proximity Gaps for
   Reed-Solomon Codes*, November 7, 2025, ECCC TR25-169.
   https://eccc.weizmann.ac.il/report/2025/169/download/
   Lemma 3.1 (printed pp.22-24) supplies the low-Z-degree interpolant.
   Section 3.2 (pp.24-26) motivates the per-factor degree summation.
2. Ben-Sasson, Carmon, Ishai, Kopparty and Saraf, *Proximity Gaps for
   Reed-Solomon Codes*, ECCC TR20-083, revision 3, July 3, 2021.
   https://eccc.weizmann.ac.il/report/2020/083/revision/3/download/
   Section 5.2.6 preserves chosen P_z under simple-root specialization;
   Section 5.2.7 forces affine coefficients by coordinate interpolation;
   Appendix A Lemma A.1 / Claim A.2 provide norm and numerator estimates;
   Appendix C (pp.57-59) provides the inseparable version.

Local contribution: a full chosen-bad-witness assembly, elementary
fixed-line cancellation lemma, conservative Frobenius degree accounting,
integer lifting length, a separate content exception term, and an
explicit degree-deficit numerator recurrence in hensel_weight_ledger.md.
The latter recovers the coarse estimates without a saturated-degree
assumption on the specialized leading coefficient. These
establish the rounded constant in statement.md, not the exact constant
of BCHKS Theorem 4.6 or its M>1 generalization.

Upstream comparison, pinned main
93fba1be3f3299b0ba4708d88715377bbb656e45:
experimental/notes/audits/audit_bchks25_thm46_conditional_johnson_import.md
holds the exact printed linear theorem conditional while accepting a
quadratic MCA mechanism. This packet supplies a separately written
slightly weaker linear theorem for independent review. It does not
retroactively change that upstream audit or assume its conditional row.

The 2026-09-06 title/body PR searches returned no open BCHKS match and
Johnson matches #1165, #1162 and #1151. This is a targeted overlap check,
not a complete PR audit. No new PR, commit, push or canonical edit.
