# Hand audit

The general symbolic theorem is now submitted in
[PR #1175](https://github.com/przchojecki/rs-mca/pull/1175#issuecomment-5564605195).
The export includes a self-contained proof and an actual loss-one control,
but excludes the numerical KoalaBear application and its Johnson input.
Fresh public-body equality, author and ID checks passed; four embedded-code
mutations were rejected. See the scoped export record in node.json.
This publication does not change the local mathematical requirements or
claim independent external acceptance.

Checked padding in the original field and full code, including the locator
divisibility that preserves SAME-support noncontainment. The field-size gate
supplies actual unused domain points. Polynomial degrees, slopes and both
affine ranks are preserved. No extra padded slopes need to be counted back.

At a common zero, a nonuniversal agreeing coordinate is removed only after
discarding its unique slope label. A small exact example in verify.py loses
one ACTUAL bad slope: the child direction is a codeword, so its bad set is
empty. This rejects the false lossless-zero shortcut. Universally matched
zeros permit a direct return from a padded pair. Larger child agreements
are reduced by connected subset exchange, not assumed exact automatically.

The proof uses induction on explanation dimension and, within one step,
on ambient degree. The additive R-L is explicit. The seven fixed Johnson
certificates cover all degrees through padding and induction; no exhaustive
million-degree table or monotonicity of optimized Johnson constants is used.
Every child is counted in the full code without an inherited near condition.

The new V_9 and V_10 have the |F|>=2R gate. Existing field-independent
constants remain valid separately. The original KoalaBear field and its
children satisfy the stronger gate, without changing the prize budget.

The verifier checks the printed certificate tables and tiny source controls.
It passed locally under RAMguard tiny in 0.03 seconds at 12672 KiB RSS.
The strengthened consumer's rational and independent decimal checks also
passed, as did its actual rank-twelve core-transport regression. All checks
stayed below 14 MiB RSS. No Modal work or spending occurred.
The all-row statement rests on the hand induction, not those controls.
Independent external review of this compiler and the rounded Johnson
supplier remains due. No full rank-twelve or grand-prize closure is claimed.
