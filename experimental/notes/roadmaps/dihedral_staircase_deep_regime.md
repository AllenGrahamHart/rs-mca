# Dihedral staircase: deep-regime proof and clean-rate obstruction

- **Status:** PROVED in the deep regime; NOT APPLICABLE to the QA.21
  clean-rate candidates.
- **DAG:** `dihedral_staircase`.
- **Verifier:** `experimental/scripts/verify_dihedral_staircase_deep_regime.py`
  checks the row arithmetic and the `j`/complement correction.

## 1. The proved lemma

Let `C = RS[H,k]` on `|H| = n`.  Fix a received pair `(u,v)`.  For a finite
slope `z`, write `w_z = u + z v`.  An exact `j`-support is a set
`R subset H`, `|R| = j`, such that for some codeword `c_R in C`,

```text
w_z(x) = c_R(x)  for x in H \ R,
w_z(x) != c_R(x) for x in R.
```

If

```text
3j <= n-k,
```

then the number of aligned exact `j`-supports over all finite slopes is at
most `n+1`.  If the projective slope at infinity is included, the same proof
gives `n+2`.

This statement does not use dihedrality.  Therefore it bounds the dihedral
subfamily as well.

## 2. Proof

First, for a fixed slope `z`, there is at most one exact `j`-support under the
weaker condition `2j <= n-k`.  If `R_1,R_2` align at the same slope with
codewords `c_1,c_2`, then their agreement sets meet in at least `n-2j`
points.  Under `n-2j >= k`, Reed-Solomon uniqueness gives `c_1=c_2`; exactness
then forces the two disagreement supports of `w_z-c_1` to be equal.

Now suppose there are at least two supports.  Choose two distinct supports
`R_1,R_2`, with slopes `z_1 != z_2` and codewords `c_1,c_2`.  On
`I=(H\R_1) cap (H\R_2)`, whose size is at least `n-2j`, solve

```text
U = (z_1 c_2 - z_2 c_1)/(z_1-z_2),
V = (c_1-c_2)/(z_1-z_2).
```

Then `u=U` and `v=V` on `I`.

For any third aligned support `R` at slope `z` with codeword `c`, the set
`(H\R) cap I` has size at least `n-3j`.  Under `n-3j >= k`, the codewords
`c` and `U+zV` agree on at least `k` points, hence are equal.  Thus every
aligned support is the exact nonzero support of

```text
e_u + z e_v,   where e_u = u-U and e_v = v-V.
```

For each coordinate `x`, the expression `e_u(x)+z e_v(x)` is a linear function
of `z`.  If `e_v(x) != 0`, it vanishes at the single finite slope
`z = -e_u(x)/e_v(x)`.  Otherwise its zero/nonzero status is independent of
`z`.  Hence the zero set can change at at most `n` finite slope values, and
all other finite slopes share one generic zero set.  There are at most `n+1`
finite exact supports.  Including the slope at infinity adds at most the
support of `e_v`, giving `n+2`.

## 3. Applicability to QA.21

The QA.21 clean-rate candidates use `j = n-A`, the exact disagreement support
size.  They do not satisfy the deep-regime hypothesis.

```text
row    rate  A              j              t=A-k        k+3j-n
RowC   1/4   261            763            5            1521
RowC   1/8   133            891            5            1777
RowC   1/16  67             957            3            1911
prize  1/4   558345748481   1640677507071  8589934593   3272765079549
prize  1/8   283467841537   1915555414015  8589934593   3822520893437
prize  1/16  141733920769   2057289334783  4294967297   4110283702269
```

So this lemma does not close QA21-G1.

The common slip is visible at RowC rate `1/16`: the crude support count
`N_dih ~= 2^173.6759` is

```text
2 * C(511,478) = 2 * C(511,33).
```

The number `33` is the complementary moving-pair count.  The clean candidate
has `A=67` and `j=957`; the complementary support size is `67`.  The deep
lemma applies to that complementary high-agreement row, not to the clean-rate
disagreement support used by QA.21.

## 4. What remains outside the deep regime

When `3j > n-k`, the two-anchor proof stops for a real reason: a third
agreement set need not meet the two-anchor core in `k` points.  The dihedral
family then contains a Chebyshev quotient copy of ordinary RS list decoding.

For a sign `epsilon in {+1,-1}`, set

```text
Q = (H \ {+1,-1}) / (x ~ x^-1),       y = x + x^-1,
N = |Q| = (n-2)/2,
K = floor(k/2),
m = (j-1)/2.
```

For quotient polynomials `h(y)` of degree `< K`, the lift

```text
F_h(X) = (X + epsilon) X^(K-1) h(X + X^-1)
```

has degree `< k`.  If a quotient word `W:Q -> F` has many degree-`<K`
polynomials agreeing on exactly `N-m` quotient points, then the lifted words
give exact dihedral supports

```text
{epsilon} union pi^-1({y : h(y) != W(y)})
```

at the corresponding support size.  The quotient agreement excess is
approximately `t/2`, so this is the same corridor list problem transported
through the Chebyshev quotient, not a terminating staircase recursion.

The clean missing statement is therefore:

```text
x3_chebyshev_quotient_line_list_bound:
  for every fixed pair (u,v), sign epsilon, and folded Chebyshev quotient line,
  the number of exact size-m quotient bad sets B that lift to dihedral
  disagreement supports is <= poly(n).
```

The scalar quotient RS list bound is a necessary substatement, by the explicit
lift above.
