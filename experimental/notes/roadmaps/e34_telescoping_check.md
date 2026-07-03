# E34: the jointness telescoping check (face 1 of the rigidity kernel)

- **Status:** AUDIT (toy-scale exact linear algebra, 519 cells, 15/15
  verifier rows PASS) + two small PROVED lemmas (J1, J2 below). Nothing
  here proves Conjecture TR or any corridor bound.
- **Agent/model:** Claude (Fable 5), L1 lane, branch `allen/prize-dag-delta`.
- **Date:** 2026-07-03.
- **DAG target:** `tr_joint_telescope` (face 1 core candidate), feeding
  `gap1_noneq_mass`.
- **Evidence item:** E34 (Wave 5, `evidence_plan_codex.md`).
- **Inputs:** `gap1_terminal_reserve.md` (Conjecture TR, the `A_r`; M4),
  `verify_gap1_terminal_reserve.py` (the F_13 toy instrumentation),
  PR #212 / E6 packet (`x1_gap1_nonequivariant_periodic_evidence.md`).
- **Verifier:** `experimental/scripts/verify_e34_telescoping.py`.

## 0. The question

`tr_joint_telescope` proposes: simultaneous `K_M`-stability across an
active character set `R` IS agreement with the **joint stabilizer
subcode** — so TR's product over `R` should telescope into a SINGLE
quotient-row instance at the joint scale, making TR's jointness
structural (tower bookkeeping) rather than analytic. E34 tests this
mechanically: for every stable support `S` and active set `R`, compare

```text
joint(S,R)  the actual simultaneous object
prod(S,R)   Conjecture TR's per-character product target
tel(S,R)    ONE instance at the joint stabilizer scale, exact
```

and check `joint <= tel <= prod`, whether `tel < prod` ever (structural
gain), and whether `joint = tel` (exact telescoping). Falsifier:
`joint > tel` anywhere kills the candidate.

## 1. The joint stabilizer, pinned

`K_M = <zeta>`, `zeta = omega^(n/M)`. For `R subseteq Z/M` nonempty set

```text
D := gcd(M, {r - r' : r, r' in R}),   (D = M when |R| = 1)
```

**Lemma J1 (joint stabilizer).** All `r in R` are congruent to one
residue `r_0 mod D`, and the subgroup of `K_M` acting by a SCALAR on
every function with character support in `R` is exactly
`K_D = <eta>`, `eta := zeta^(M/D)`; the scalar is the single character
`eta -> eta^(r_0)`. *Proof.* `D` divides every difference, so `R` sits
in one class mod `D`. `zeta^i` acts on the `r`-component by
`zeta^(ri)`; these agree over `R` iff `i(r-r') == 0 mod M` for all
pairs iff `(M/D) | i`. On `eta = zeta^(M/D)`: `eta^r = eta^(r_0)` since
`D | r - r_0`. QED. So the "joint stabilizer subcode" is the
`r_0`-isotypic code of the SUBGROUP `K_D` — a single character at one
quotient-row scale `n/D`, exactly the node's telescoping candidate.

**Lemma J2 (containment; equality on full classes).** On a `K_M`-stable
`S`, the joint data space `{sum_(r in R) U_r}` (each `U_r` `r`-isotypic
w.r.t. `K_M`, base amplitudes on `S/K_M`) is contained in the
`r_0`-isotypic `K_D` data space (base amplitudes on `S/K_D`); dimensions
are `|R| * |S/K_M|` vs `(M/D) * |S/K_M|`, so the two coincide iff
`|R| = M/D`, i.e. iff `R` is a FULL congruence class mod `D`.
*Proof.* `U_r(eta x) = eta^r U_r(x) = eta^(r_0) U_r(x)` (J1), sum over
`R`; values stay in `B`. `|R| <= M/D` since a class mod `D` has `M/D`
residues mod `M`; equality of contained spaces of equal dimension. QED.

Consequences (before any computation): `joint <= tel` always, and
`joint = tel` exactly on full-class `R` — the verifier checks both
numerically cell by cell (a failure would mean the formalization above
is not what the toy computes).

## 2. Model and toy rows

Counts are the exact linear slope-image counts of E6/M4 (`p^rank` of an
`F_p`-linear image; data on `S` -> interpolant -> value at `alpha`; no
degree cut, no fixed received word — E6/M4's caveats inherited). Rows:

```text
F13-M2  p=13, n=12, omega=2, F = F_13(sqrt 2), alpha = sqrt 2, M=2
F13-M4  same toy, M=4  (DEGENERATE tower: [F:B] = 2 < M = 4, so the
        lines alpha^0 B = alpha^2 B and alpha^1 B = alpha^3 B collapse)
F17-M4  p=17, n=16, omega=3, F = F_17[a]/(a^4-3), alpha = a, M=4
        (NON-degenerate robustness row: [F:B] = 4 = M, independent lines)
```

All `K_M`-stable supports x all nonempty `R`: 189 + 105 + 225 = 519
cells; all three columns recomputed exactly per cell.

## 3. Census (verifier-pinned, 15/15 PASS)

```text
row     cells full-class exact(joint=tel) chain(j<=t<=p) gain(t<p) lossy(t>p)
F13-M2  189   189        189              189            0         0
F13-M4  105   49         105              105            49 (21 full) 0
F17-M4  225   105        105              105            0         120
```

- **No falsifier fires:** `joint <= tel` (with explicit span
  containment) in all 519 cells.
- **Exact telescoping on every full-class cell** (343/343), as J2
  forces; in F13-M4 even all sparse cells happen to be exact
  (the `[F:B] = 2` cap saturates both sides).
- **Structural gain (`tel < prod`) exists and is exactly the
  degenerate-tower collapse:** 49 cells, all in F13-M4 (e.g.
  `R = {0,2}`: both characters confined to the SAME line `B`, so
  `tel = joint = 13^1 < 13^2 = prod`). In the non-degenerate F17 row,
  gain count is 0: on full classes `tel = joint = prod` exactly.
- **Lossy cells (`tel > prod`) occur ONLY for sparse `R`**
  (`|R| < M/D`; 120 cells, all F17, excess up to `17^2`): e.g.
  `R = {0,1}` has trivial joint stabilizer (`D = 1`), so the telescoped
  instance is the whole unrestricted row and over-counts. The
  telescoping candidate MUST take `R` to its class closure mod `D`
  (equivalently: it is a statement about full congruence classes).

## 4. Verdict and interpretation (pre-registered mapping)

**Telescoping is EXACT, hence STRUCTURAL — with one amendment.** In the
tested model `joint = tel` on every full-class cell and `joint <= tel`
everywhere; no cell has `joint > tel`, so `tr_joint_telescope`'s
candidate survives its falsifier. Per the pre-registered reading: TR's
jointness content is a TOWER statement — the simultaneous-`R` object is
literally one single-character instance at the joint subgroup `K_D`
(J1/J2 make this an identity of data spaces, not an inequality), and
the `q^(M-1)` per-leaf over-aggregation of M4 sect. 3(c) disappears by
construction at the joint scale. **E29 demotes to constants
calibration** for the class-closed form. Amendment required in the node
statement: for `R` sparse in its class mod `D`, `tel` can exceed `prod`
(F17: 120 cells) — the correct telescoped target for TR is the full
class `r_0 + D*Z/M`, and sparse `R` inherits its class's instance
(`joint <= tel` still holds; the product bound over the sparse `R` may
then be the sharper of the two). Second finding: `tel < prod` strictly
happens exactly where the tower is degenerate (`[F(alpha):B] < M`) —
the telescope's rank-level GAIN is line collapse, which the
per-character product cannot see; on non-degenerate towers the gain
must come from aligned-count discounts, which this linear model cannot
measure (that is E29's job, now as calibration).

## 5. Non-claims

- Nothing here proves Conjecture TR, `gap1_noneq_mass`, or any corridor
  bound; the model has no degree cut and no fixed received word, so
  these are linear-model counts (E6/M4 convention), not `|A_r|` at
  corridor scale.
- J1/J2 are proved for this isotypic data model; lifting the identity
  to the ALIGNED sets `A_r` (fixed `w`, `deg < k`) is precisely the
  remaining face-1 statement — the toy shows its shape is an identity,
  not that the lift is automatic.
- The DAG JSON is untouched; the amendment to `tr_joint_telescope`
  (class closure) is recorded here only.

## 6. Verification

```bash
python3 experimental/scripts/verify_e34_telescoping.py
```

Deterministic, stdlib only, < 5 s. Per toy row: V1 `joint <= tel` +
span containment in every cell (falsifier check), V2 full-class
exactness `joint = tel <= prod`, V3 `tel > prod` only when sparse,
V4 singleton degeneracy `joint = tel = prod`, V5 census regression
pin. Exit 0 iff 15/15 PASS.
