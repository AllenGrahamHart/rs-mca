# Proof: polynomial gluing and the actual received-pair defect

Mathematical verdict: NO ISSUE for the three statements below. Source:
PR #1175 at the pin in
[the review index](../../../notes/correspondence/hand_review_20260905/README.md).
These proofs use only finite-
dimensional linear algebra and the polynomial root bound, not a computation
or the rank-eleven numerical payment.

## 1. Restriction and supported annihilators

Let `D` be a finite set of distinct points over a field `F`, let `K>=1`, and let
`H_1,...,H_t subset D` be a nonempty finite family, with union `U`.
Write `C_K(X)` for the evaluation image of degree-`<K` polynomials on `X`;
this denotes the image even when `|X|<K`.

In the dual of `F^U`, define

```text
A_H = {lambda: supp(lambda) subset H and lambda(C_K(U))=0},
A = sum_i A_(H_i),
L = {f in F^U: f restricted to H_i is in C_K(H_i) for every i}.
```

Then

```text
A^perp = L,
A_U^perp = C_K(U),
dim A_U-dim A = dim L-dim C_K(U).
```

Indeed, restriction `F^U -> F^H` is surjective, and the restrictions of
`C_K(U)` are exactly `C_K(H)`. Thus `A_H` is the zero extension of the
annihilator of `C_K(H)`. Its annihilator consists exactly of functions whose
restriction to `H` lies in that code. The annihilator of a sum is the
intersection of the annihilators, proving the first equality. The second is
finite-dimensional double annihilation. Subtracting complementary dimensions
proves the third. In particular, `A=A_U` if and only if every local section
is one global degree-`<K` evaluation word on `U`.

## 2. Received-pair defect trichotomy

For each retained actual record on the same received line, let
`H_e={x in D: (r_0(x),r_1(x))=(a_e(x),b_e(x))}`, where `a_e,b_e` are
degree-`<K` polynomials. Repetitions of cores are allowed. On their union,
both received restrictions lie in `L`. Set

```text
Q = L/C_K(U),
c = dim span{[r_0|U],[r_1|U]}.
```

Exactly one of the following occurs:

- `c=0`: both restrictions are globally polynomial on `U`.
- `c=1`: exactly one projective combination of the received components is
  globally polynomial on `U`.
- `c=2`: no nonzero combination is globally polynomial on `U`.

This follows by applying rank-nullity to
`F^2 -> Q`, `(alpha,beta) -> [alpha*r_0+beta*r_1]`. It is an identity for
the actual received pair and cores; there is no choice of an abstract
replacement family, no support multiplicity, and no change of slope labels.

The integer `dim Q` can exceed two. Only the image of this two-dimensional
map has rank at most two. Also `c=0` does not imply `Q=0`: this particular
received pair can be global even when other local sections fail to glue.

## 3. A sufficient overlap criterion

Suppose the cores can be ordered so that `|H_1|>=K` and, for `i>=2`,

```text
|H_i intersection (H_1 union ... union H_(i-1))| >= K.
```

Then `Q=0`. To prove this, choose a polynomial representing a local section
on `H_1`. Inductively, the polynomial representing it on the next core
agrees with the already fixed polynomial on at least `K` points. Their
difference has degree `<K`, hence is zero. This produces one polynomial
representing the section throughout `U`.

This is a sufficient condition, not a claim that actual minimizing cores
admit such an ordering. Counting nominal constraints or core excesses alone
does not prove the equality of annihilator spaces. No converse is imported.

## Integration boundary

These statements make the core-compatibility obstruction precise, but do
not count the families in any of the three classes. The separate
[zero-defect bound](../mca_received_pair_zero_defect_payment/statement.md) counts slopes in the first class
using additional, explicitly stated hypotheses. The other two classes are
unpaid. In particular, `c=1` is not yet an identification with an existing
one-function, conic, or split-pencil owner.

## 4. High-band continuation, 2026-09-06

[high_band_defect.md](high_band_defect.md) adds a complete proof under the
all-projective agreement ceiling. Two cores whose depths sum to at least
h force actual received-pair defect two. It supplies the exact two-core
quotient, the stronger intersection cap, and the trivial payment of the
zero-defect high-band branch; the one-defect high-band branch is empty.
This is a local continuation, not a claim made by PR #1175. Its conclusion
does not pay the remaining defect-two population.
