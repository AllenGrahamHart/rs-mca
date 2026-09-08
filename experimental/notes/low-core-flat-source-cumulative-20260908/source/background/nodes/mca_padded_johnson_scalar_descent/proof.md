# Proof

## 1. Padding preserves the actual bad slopes

Consider a row (R+K,K,d+K) with K<=L. Choose L-K new field
points G disjoint from D; |F|>=R+L suffices. Let P_G be their
locator. On D define u'=P_G*u, v'=P_G*v, and on G set both
words to zero. For every selected explanation h_gamma use
h'_gamma=P_G*h_gamma, a polynomial of degree <L.

An original bad support S becomes S union G, of size d+L. If a
degree-<L pair explained (u',v') there, each polynomial would vanish
on G, so division by P_G would give a degree-<K pair explaining
(u,v) on S. This contradicts original same-support badness.

Thus every original bad slope is a bad slope of ONE padded pair in the
SAME field. The map on errors is multiplication by nonzero coordinate
weights on D and extension by zeros on G; it is injective and linear.
It preserves the affine error rank of a selected family. Polynomial
multiplication also preserves its explanation affine dimension.

No new field, slope denominator, smoothness hypothesis, or independent
copy of a worst-case family is introduced. A full bound J at degree L
therefore bounds every smaller degree K as well. The padded domain need
not be smooth; the required rounded Johnson theorem allows arbitrary
distinct evaluation points.

## 2. Removing a common evaluation zero costs at most one

Write the explanations as h_*+C', with actual dimension s. Suppose
x in D is a common evaluation zero of C', so every h_gamma(x)=h_*(x).
If (u(x),v(x))=(h_*(x),0), keep every slope. Otherwise at most one
slope can satisfy u(x)+gamma*v(x)=h_*(x); discard that label if it
exists. If v(x)=0 and u(x)!=h_*(x), no label is discarded.

Subtract the common polynomial pair (h_*,0), delete x, and divide
the received words and explanations by X-x on D\{x}. The explanations
are polynomials of degree <K-1 and still have affine dimension at most
s. For every retained support, either x was universally matched, or
x did not belong to it. The remaining support has at least m-1 points.

A pair of degree <K-1 explaining this remaining support would lift by
multiplication by X-x and addition of (h_*,0). It would explain the
whole original support, including x when x was universally matched.
Consequently the child support remains bad in the FULL shortened code.

If it has more than m-1 points, a bad subset of exactly m-1 exists.
Otherwise the explaining pairs on all (m-1)-subsets agree on overlaps
of size m-2>=K-1; one-point exchanges glue them into a pair on the
whole support, a contradiction. This preserves the selected explanation.

The resulting row is (R+K-1,K-1,d+K-1). At most ONE original
slope was lost. There is no assumption that the child is post-near,
that the removed zero was universal, or that the direction space still
has actual dimension s after discarding the exception.

## 3. Double induction with one fixed Johnson anchor

Assume the uniform dimension-(s-1) cap U from the statement. Prove
the dimension-s cap by induction on K. For K<=L, section 1 and
the full Johnson input give |Z|<=J<=A.

Let K>L. If the actual explanation dimension is smaller than s,
use U<=A. Otherwise, if a common evaluation zero exists, section 2
and induction give

```text
|Z| <= 1 + A + max(0,K-1-L) = A+K-L.
```

If no common zero exists, the required scalar-agreement theorem
anchors each selected support at all its m coordinates. Every child
has explanation dimension at most s-1 on (R+K-1,K-1,d+K-1).
Counting incidences gives

```text
m|Z| <= n*U,
|Z| <= floor((R+K)*U/(d+K))
    <= floor((R+L+1)*U/(d+L+1)) <= A.
```

The middle inequality uses R>=d, so the ratio decreases with K.
This proves (PJ), including every same-dimension zero branch. It is
an induction proof for all K, not a computational scan over K.

## 4. Seven fixed certificates give the printed constants

Use the required weighted-line cap V_1=4070947. At s=2,3,4,
the scalar theorem gives V_s=floor((R+s)*V_(s-1)/(d+s)). For
s=5,...,11 apply (PJ) using the seven L,J pairs in certificates.md.
In every printed row the scalar endpoint exceeds both J and V_(s-1),
so

```text
V_s=floor((R+L+1)*V_(s-1)/(d+L+1)) + R-L.
```

The rounding allowance R-L is retained explicitly. Every V_s exceeds
V_(s-1), so lower-dimensional families are covered as well. The
Johnson input counts full original finite slopes including the higher
agreement tail. Its exact gate and all integer ceilings are certified
separately; no sketched sharp-constant Johnson theorem is imported.

The original KoalaBear field has far more than 2R elements, as do its
unchanged-field children. The theorem does not replace an original
ambient budget by the size of a padded domain or coefficient field.
