# The Lifting Lemma (face 1 of the rigidity kernel): telescoping holds for the ALIGNED sets

- **Status:** **PROVED** (Lemmas LL0-LL2 and Theorem LL(i)-(iv), complete
  written proofs below) + AUDIT (aligned toy census, 330 cells, 21/21
  verifier rows PASS). The count-transfer corollary is exact on
  NON-DEGENERATE towers and one-sided on degenerate ones — that split is
  part of the statement, not a gap. Nothing here proves Conjecture TR or
  any corridor bound.
- **Agent/model:** Claude (Fable 5), L1 lane, branch `allen/prize-dag-delta`.
- **Date:** 2026-07-03.
- **DAG target:** `tr_joint_telescope` (face 1) — this is exactly the lift
  that `e34_telescoping_check.md` sect. 5 left open ("lifting the identity
  to the ALIGNED sets `A_r` ... is precisely the remaining face-1
  statement"); feeds `gap1_noneq_mass`.
- **Inputs:** `e34_telescoping_check.md` (Lemmas J1/J2, class-closure
  amendment), `gap1_terminal_reserve.md` (the `A_r`, Conjecture TR; #212
  Thm 1 conventions inherited from there).
- **Verifier:** `experimental/scripts/verify_tr_lifting_lemma.py`.

## 0. The question

E34 proved J1/J2 (joint stabilizer `K_D`, telescoped subcode) for the
LINEAR data model and verified exact telescoping in the E6/M4 slope-image
counts. Face 1 needs the same identity for the objects TR actually
quantifies over: the aligned sets `A_r` — fixed received word `w`, degree
cut `deg < k`, `K_M`-stable agreement `>= A`. This note proves that lift:
**the simultaneous membership data of the aligned per-character sets over
an active set `R` IS the corresponding single-instance aligned data at the
joint scale `D`, character class `r_0`** — with the two provisos (genuine
scale-`D` filter: containment; degenerate tower: one-sided counts) stated
exactly, each with a verified toy witness.

## 1. Pinned notation

Inherited: `gap1_terminal_reserve.md` sect. 1/4 and E34 sect. 1.

```text
row       RS_q(H_n, k): deg < k polys over B = F_q on H_n = <omega>, n | q-1.
K_M       <zeta>, zeta = omega^(n/M), M | n; tower B <= K <= F,
          beta := alpha^M in K, alpha in F^*.
c_r       r-isotypic part of c under K_M: X^r G_r(X^M), G_r over B
          (monomials of c with degree == r mod M; #212 Thm 1 convention).
C(w,A,M)  := {c in RS_q(H_n,k) : Agr(c,w) K_M-stable, |Agr(c,w)| >= A}
          (the qualifying ensemble; TR's quantifier domain).
v_r(c)    := alpha^r G_r(beta) in alpha^r K,  so  A_r = {v_r(c) : c in C}.
J_R       := {(v_r(c))_{r in R} : c in C(w,A,M)}   (JOINT aligned data:
          the simultaneous membership data {(A_r)_{r in R}}; the A_r are
          its coordinate projections).
D, r_0    D := gcd(M, {r-r' : r,r' in R}) (= M if |R|=1); all r in R lie
          in one class r_0 mod D (E34 Lemma J1); Rbar := (r_0 + D Z) cap Z/M
          (class closure, |Rbar| = M/D); K_D = <eta>, eta = zeta^(M/D)
          = omega^(n/D), the joint stabilizer (J1).
c^(s)     s-isotypic part of c under K_D: X^s H_s(X^D), H_s over B.
gamma     := alpha^D, so gamma^(M/D) = beta;  telescoped aligned value of c:
          tv(c) := alpha^(r_0) H_{r_0}(gamma);  T := {tv(c) : c in C(w,A,M)}.
sigma     : prod_{r in Rbar} alpha^r K -> F, (x_r)_{r in Rbar} |-> sum_r x_r.
NON-DEG   the joint tower is non-degenerate iff [K(gamma):K] = M/D
          (max possible, since gamma^(M/D) = beta in K).
A_r(w,A,D,alpha)  gap1's aligned set at period D, class r_0: the GENUINE
          scale-D single instance, whose own filter is K_D-stability.
```

Throughout `p = char(B)`; `D | M | n | q-1` forces `p` coprime to `D`, so
`1/D` exists in `B` — used silently in isotypic averaging.

## 2. Three lemmas

**Lemma LL0 (J1 on polynomial spaces, degree-aware).** For every `k <= n`:

```text
{ f : deg f < k, every monomial degree of f == r_0 mod D }
   =  (+)_{r in Rbar} { f : deg f < k, every monomial degree == r mod M },
```

and on `H_n` these are exactly the `r_0`-isotypic functions under `K_D`
(resp. the `r`-isotypic under `K_M`) representable with `deg < k`.
*Proof.* A degree `i` satisfies `i == r_0 mod D` iff `i == r mod M` for
exactly one `r in Rbar` (residues mod `M` refine residues mod `D`, and
`Rbar` is the full preimage of `r_0`). Both sides are monomial-spanned, and
the degree cut `deg < k` selects monomials individually, so it commutes
with both groupings. For the isotypic identification: `{X^i}_{i<n}` is a
basis of functions on `H_n` and the `K_M`-action is diagonal on it
(`zeta * : X^i |-> zeta^i X^i`), so isotypic = monomial-degree class; `K_D`
likewise with `eta = zeta^(M/D)` and classes mod `D` (J1's subgroup
computation restated); `k <= n` keeps poly <-> function faithful on the
span. QED.

This is the precise sense in which "`K_M`-stability (of data) for all
`r in R` = `K_D`-stability at class `r_0`": the two isotypic filtrations
coincide on the class closure, INCLUDING the degree cut — the E34
non-claims item "fixed `w`, `deg < k`" splits here into the `deg < k` half
(this lemma, clean because the filtration is monomial-diagonal) and the
fixed-`w` half (Theorem LL below).

**Lemma LL1 (pointwise telescoping identity).** For every `c in RS` (no
agreement condition), with `G_r`, `H_s` as pinned:

```text
H_{r_0}(Y) = sum_{s=0}^{M/D - 1} Y^s G_{r_0 + Ds}(Y^{M/D}),   and hence
alpha^(r_0) H_{r_0}(gamma) = sum_{r in Rbar} alpha^r G_r(beta),
i.e.  tv(c) = sigma( (v_r(c))_{r in Rbar} ).
```

*Proof.* Write `c = sum_{i<k} c_i X^i`. By definition `H_{r_0}(Y) =
sum_{i == r_0 mod D} c_i Y^((i-r_0)/D)` and `G_r(Z) = sum_{i == r mod M}
c_i Z^((i-r)/M)`. Group the indices `i == r_0 mod D` by their residue
mod `M` (LL0): `i == r_0 + Ds mod M` for a unique `s in [0, M/D)`, and for
such `i`, `(i - r_0)/D = s + (M/D) * (i - r_0 - Ds)/M`, so
`Y^((i-r_0)/D) = Y^s (Y^(M/D))^((i-r_0-Ds)/M)`. Summing the class gives the
first display. Evaluate at `Y = gamma`: `gamma^(M/D) = alpha^M = beta`, so
the `s`-summand is `gamma^s G_{r_0+Ds}(beta) = alpha^(Ds) G_{r_0+Ds}(beta)`;
multiply by `alpha^(r_0)` and reindex `r = r_0 + Ds` over `Rbar`. QED.

**Lemma LL2 (isotypic projection commutes with agreement on exactly stable
sets).** Let `c in C(w,A,M)` and `S = Agr(c,w)`. Then for every `D | M` and
every `s in Z/D`, the `K_D`-isotypic parts agree on all of `S`:
`c^(s)(x) = w^(s)(x)` for every `x in S`, where `w^(s)(x) :=
(1/D) sum_{j<D} eta^(-sj) w(eta^j x)`. *Proof.* `K_D <= K_M` and `S` is
`K_M`-stable, so `S` is `K_D`-stable: `x in S => eta^j x in S` for all `j`,
hence `c(eta^j x) = w(eta^j x)`. Average: `c^(s)(x) = (1/D) sum_j
eta^(-sj) c(eta^j x) = w^(s)(x)` (`1/D` exists, sect. 1). The averaging
formula computes the monomial selection of LL0: on `X^i` it gives
`X^i * (1/D) sum_j eta^((i-s)j) = X^i * [i == s mod D]` since `eta` has
exact order `D`. QED.

**Where LL2 is and is not used.** Theorem LL below does NOT need the
agreement condition to decompose isotypically at all — that is the point
of the proof (the condition filters the ensemble; the identity is
pointwise). LL2 is what makes the MULTI-SCALE reading honest (the
telescoped value is the aligned value of a genuine quotient instance whose
received word is the `D`-quotient of `w^(r_0)`, with quotient agreement
`>= A/D` on `S/K_D`); it is stated here because it is exactly the step
that BREAKS under approximate stability — see flag F3.

## 3. Theorem LL (the Lifting Lemma) [PROVED]

Fix `q, n, k, A, M`, a tower `B <= K <= F` with `beta = alpha^M in K`, a
received word `w`, and an active set `R` with joint data `(D, r_0, Rbar)`.
All aligned objects are over the SAME qualifying ensemble `C = C(w,A,M)`
unless said otherwise.

**(i) (Class closure / sparse R.)** `R subseteq Rbar`, and `J_R` is the
coordinate projection of `J_Rbar` onto the `R`-coordinates; in particular
`|J_R| <= |J_Rbar|`, and each `A_r` is a further projection. *Proof.*
Every `r in R` satisfies `r == r_0 mod D` (J1), so `r in Rbar`. Both tuple
sets are images of the same `C` under maps that agree coordinatewise on
`R`. QED. (This inherits E34's amendment: the telescoping statement is
about the class closure; sparse `R` rides along by projection.)

**(ii) (Exact aligned telescoping, ensemble-matched.)** `sigma(J_Rbar) = T`
— the joint aligned data maps ONTO the telescoped aligned data, exactly.
*Proof.* By LL1, `sigma((v_r(c))_{r in Rbar}) = tv(c)` POINTWISE for every
`c in RS`, in particular for every `c in C`. Therefore
`sigma(J_Rbar) = {sigma(tuple(c)) : c in C} = {tv(c) : c in C} = T`, an
identity of images of the same index set under pointwise-equal maps. QED.

Note what made this work: the agreement/alignment condition NEVER has to
decompose — it appears only as the restriction `c in C` of the domain of a
pointwise identity, and restriction commutes with taking images. The same
one-line argument gives (ii) for ANY subensemble of `RS` (exact agreement
`= A`, extra side conditions, weighted versions), so J1/J2 commute with
the alignment restriction in complete generality. This is stronger than
the "agreement indicator decomposes isotypically" route the node sketch
proposed, and it has no boundary cases.

**(iii) (Count transfer; the non-degeneracy dichotomy.)** `sigma` restricted
to `prod_{r in Rbar} alpha^r K` is injective iff the joint tower is
non-degenerate, `[K(gamma):K] = M/D`. Hence:

```text
non-degenerate:  J_Rbar <-> T is a BIJECTION;  |J_R| <= |J_Rbar| = |T|.
degenerate:      only  |T| <= |J_Rbar|  (sigma is a surjection onto T).
```

*Proof.* A tuple in the product is `(alpha^(r_0) gamma^s u_s)_{s < M/D}`
with `u_s in K` (as `alpha^(r_0+Ds) = alpha^(r_0) gamma^s`), and
`sigma = alpha^(r_0) * sum_s gamma^s u_s`. Since `alpha^(r_0) != 0`,
injectivity of `sigma` (a `K`-linear map) is exactly: `sum_s gamma^s u_s
= 0 => all u_s = 0`, i.e. `1, gamma, ..., gamma^(M/D - 1)` are `K`-linearly
independent, i.e. `[K(gamma):K] >= M/D`; the reverse inequality always
holds because `gamma^(M/D) = beta in K`. If injective, `sigma` bijects
`J_Rbar` onto its image `T` (by (ii)); combined with (i) this gives the
chain. If not injective, distinct joint tuples can share a telescoped
value, and only the image inequality `|T| <= |J_Rbar|` survives. QED.

**(iv) (Containment in the genuine scale-D instance.)** With
`A_{r_0}(w,A,D,alpha)` the gap1-defined aligned set at period `D`, class
`r_0`, same `w`, same threshold `A`, tower `B <= K(gamma) <= F`:

```text
T  subseteq  A_{r_0}(w, A, D, alpha),      and therefore, non-degenerate:
|J_R|  <=  |J_Rbar|  =  |T|  <=  |A_{r_0}(w, A, D, alpha)|.
```

*Proof.* Let `c in C(w,A,M)`. Then `Agr(c,w)` is `K_D`-stable (`K_D <=
K_M`, LL2's first line) and `|Agr| >= A`, so `c` qualifies for the
period-`D` ensemble `C(w,A,D)`; its `r_0`-isotypic part under `K_D` is
`X^(r_0) H_{r_0}(X^D)` (LL0), and its aligned value is
`alpha^(r_0) H_{r_0}(gamma) = tv(c)` — precisely gap1's definition with
`(M, zeta, K)` replaced by `(D, eta, K(gamma))` (legitimate tower:
`alpha^D = gamma in K(gamma)`, and `B <= K(gamma) <= F` since `gamma^(M/D)
= beta in K`). So every element of `T` is an element of
`A_{r_0}(w,A,D,alpha)`. QED.

**Summary statement (the lift of J1/J2).** For an active set `R` with joint
stabilizer scale `D` and class `r_0`, the simultaneous membership data
`J_Rbar` of codewords with `K_M`-stable agreement `>= A` IS the
single-instance aligned data at the joint scale — exactly, as the
sigma-image (ii), bijectively iff the joint tower is non-degenerate (iii)
— and it sits inside the genuine period-`D` aligned set `A_{r_0}` whose
own filter is the weaker `K_D`-stability (iv). TR's jointness burden over
`R` therefore reduces, on non-degenerate towers, to a SINGLE TR instance
at scale `D`: `prod`-vs-`FM` bookkeeping aside, `|J_Rbar| <=
|A_{r_0}(w,A,D,alpha)|`, and the `q^(M-1)` over-aggregation of M4
sect. 3(c) disappears at the joint scale, as E34 predicted.

## 4. Flags: exactly where the decomposition is NOT clean

- **F1 (genuine-instance equality FAILS; containment only).** (iv) is
  one-directional: `A_{r_0}(w,A,D,alpha)` is fed by ALL codewords with
  `K_D`-stable agreement `>= A`, and `K_D`-stable does not imply
  `K_M`-stable. Equality would need every such codeword's class-`r_0`
  value to be realized by some `K_M`-stably-agreeing codeword — false in
  general. Verified witness: 52 of 150 F17-M4 cells (and 4/30, 52/150 in
  the F13 rows) have `T` STRICTLY inside `A_gen`. For TR this is the
  harmless direction (upper bounds only need containment).
- **F2 (degenerate towers lose the count transfer).** When `[K(gamma):K] <
  M/D`, `sigma` has kernel and `|J_Rbar| = |T|` can fail; only `|T| <=
  |J_Rbar|` is available, which is the WRONG direction for bounding the
  joint count by the scale-`D` instance. This is not hypothetical: the
  verifier's engineered word W5 produces 10 F13-M4 cells (D in {1,2},
  `alpha^2 = 2 in B`) with distinct joint tuples and equal telescoped
  values. On degenerate towers face 1 must either bound `|J_Rbar|` by
  `|T| * (fiber count)` — the fiber is controlled by `ker(sigma)`, a
  `K`-space of dimension `M/D - [K(gamma):K]` per E34's line-collapse
  reading — or work with the tuple data directly. E34's linear-model
  exactness on F13-M4 (rank saturation) does NOT lift to cardinalities.
  Any use of (iii)'s equality must therefore carry the hypothesis
  `[K(gamma):K] = M/D`; uses without it are CONDITIONAL.
- **F3 (exact stability is load-bearing).** LL2 (and (iv) through it)
  uses `eta^j x in S` for ALL `j` — exact `K_M`-stability. Under a
  stability defect (`|S Delta zeta S| = delta > 0`) the isotypic
  projection of the agreement condition acquires boundary terms and LL2
  fails pointwise. Weakest repair if a defect version is ever needed:
  restrict to the stable core `S* = intersection_j zeta^j S` and assume
  `|S*| >= A - M*delta` stays in the corridor; (i)-(iii) survive verbatim
  (they never see `S`), only (iv)'s threshold degrades to `A - M*delta`.
  TR as pinned in gap1 sect. 4 demands exact stability, so nothing in this
  note is conditional for TR's sake.
- **F4 (exact-vs->= agreement: no issue, by construction).** Both sides of
  (ii) quantify over the SAME `C(w,A,M)`; `>= A` vs `= A` never has to be
  split isotypically. Re-basing the scale-`D` instance on QUOTIENT
  agreement (`>= A/D` on `H_{n/D}`, per the multi-scale reading) only
  widens the receiving ensemble further (accidental quotient agreement
  off `S/K_D` is possible), so it weakens (iv)'s right-hand side in the
  same harmless direction as F1.
- **F5 (D = 1 degenerates to the whole row).** Sparse `R` spanning classes
  with `gcd = 1` (e.g. `{0,1}`) gives `K_D = 1`: the "instance at scale 1"
  is the unrestricted row (`A_gen` at `D=1` is fed by every codeword with
  plain agreement `>= A`), and the containment, while true, is useless.
  Face 1 should only ever invoke the lemma at `D >= 2` — the class-closure
  amendment of E34 sect. 4, inherited.

## 5. Non-claims

- Nothing here proves Conjecture TR, `gap1_noneq_mass`, or any corridor
  bound. The lemma moves TR's jointness to a single scale-`D` instance
  (on non-degenerate towers); the scale-`D` instance's own count is NOT
  bounded here — that is TR itself, still open.
- The census is toy-scale (`F_13`, `F_17`, `k = 4`, conventions of the
  M4/E34 packets, five deterministic words, `A in {4,8}`), nowhere near
  corridor agreement; it certifies the identities, not any reserve content.
- On degenerate towers no cardinality equality is claimed (F2); no claim
  is made for stability-defect ensembles (F3).
- The DAG JSON is untouched; `tr_joint_telescope`'s node status is for the
  maintainer to move — this note supplies the proof it was waiting on,
  amended by F1/F2/F5.

## 6. Verification

```bash
python3 experimental/scripts/verify_tr_lifting_lemma.py
```

Deterministic, stdlib only, ~1 s, 21/21 PASS. Real codeword enumeration
(all `p^k` polynomials, `deg < k`), real received words, real `K_M`-stable
agreement sets — the aligned analogue of E34's census. Rows F13-M2
(`p=13, n=12, alpha = sqrt 2, M=2, k=4`), F13-M4 (same, `M=4`; DEGENERATE
tower), F17-M4 (`p=17, n=16, alpha^4 = 3, M=4, k=4`; non-degenerate); five
words each (exact codeword, orbit-corrupted, 2-way orbit mix, arithmetic
pseudo-random, 3-way mix engineered to sigma-collide on the degenerate
tower), `A in {4,8}`, all 15 resp. 3 active sets: 330 cells. LLV0 pins the
non-degeneracy profile by rank; LLV1 checks LL1 pointwise per qualifying
codeword from two INDEPENDENT coefficient groupings (mod `M` + scalar
`beta` route vs mod `D` + `gamma`-power route); LLV2-LLV5 check Theorem
LL(i)-(iv) cell by cell (including `C(w,A,M) subseteq C(w,A,D)` by
independent rotation tests); LLV6 pins the census, including the 10
degenerate collision cells (F2 witness) and 52+52+4 strict-containment
cells (F1 witness). Exit 0 iff all PASS.
