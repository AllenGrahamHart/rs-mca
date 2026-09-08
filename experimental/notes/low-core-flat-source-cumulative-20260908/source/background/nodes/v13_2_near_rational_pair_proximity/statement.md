# Paper D v13.2 near-rational pair proximity

- **status:** PROVED
- **closure:** proof
- **source:** correction of Paper D v13.2 `cor:capfp-line`

Let `C` be a linear code in `F^D`, with `|D|=n`. Let `z1!=z2` be
finite slopes and suppose

```text
u+z1 v = c1+eta1,    u+z2 v = c2+eta2,
c1,c2 in C,          wt(eta1),wt(eta2)<=w.
```

Then there are `cu,cv in C` such that

```text
supp(u-cu) union supp(v-cv)
    subseteq supp(eta1) union supp(eta2).
```

In particular, `(u,v)` has a common codeword-pair explanation on at
least `n-2w` coordinates. Under the v13.2 near-rational dichotomy's
hypotheses, including `2w<=n-K`, two slopes with `d1(u+z_i v)<=w` and
nonzero census imply this pair-proximity conclusion.

This does not pay support-wise MCA witnesses. Existence of one common
agreement support does not imply that every other support explaining a
line word extends to a codeword-pair explanation.
