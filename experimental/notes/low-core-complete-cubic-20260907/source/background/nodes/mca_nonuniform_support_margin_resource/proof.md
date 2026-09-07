# Proof: nonuniform support-margin resource

Mathematical verdict: NO ISSUE. This reconstructs an existing imported
result, not a new numerical payment. Source: PR #1174 at the commit in
[the review index](../../../notes/correspondence/hand_review_20260905/README.md), `thm:mca-nonuniform-support-margin`, inherited
from #1168. No numerical certificate is used.

## Statement

Let `F` be a finite field, `D` a set of `n` distinct field elements,
`1<=K`, and `K<m=K+d<=n`, so `d>=1`. Work with degree-`<K` RS
polynomials. Let `C'` be a polynomial subspace of actual dimension
`1<=s<=K`, and fix an affine explanation space `h_*+C'`, with `h_*` also
a degree-`<K` polynomial.

For each slope `gamma` in a finite set `Z`, retain one polynomial
`h_gamma in h_*+C'` and one set `S_gamma subset D` of size `m` such that
`r_0+gamma*r_1=h_gamma` there, but no degree-`<K` polynomial pair explains
`(r_0,r_1)` on that same set. Define

```text
theta_gamma = min(d+1, min_(b in C') |{x in S_gamma: r_1(x)!=b(x)}|).

C_s = floor(max(
    n_falling_(s+1) / (m * (d+1)_rising_(s-1)),
    (n-K+s)_falling_(s+1) / (d+1)_rising_s
)).
```

Then `theta_gamma>=1` for every record, and `sum_gamma theta_gamma<=C_s`.
An empty product is one. All falling and rising products here have positive
integer factors. The count is over distinct selected slopes, not supports.

## Proof

Choose a basis `c_1,...,c_s` of `C'`. A selected explanation gives the
parameter point `(gamma,lambda_1,...,lambda_s)` with
`h_gamma=h_*+sum lambda_i*c_i`. Its coordinate agreement equation has
normal `v_x=(r_1(x),-c_1(x),...,-c_s(x))` and right side `h_*(x)-r_0(x)`.

The incident normals on `S_gamma` span `F^(s+1)`. An annihilator with zero
slope coordinate gives a nonzero degree-`<K` polynomial vanishing on at
least `m` points, impossible. An annihilator with nonzero slope coordinate
gives `r_1=b` on `S_gamma`, for some `b in C'`; then
`(h_gamma-gamma*b,b)` explains the pair there, also impossible. This proves
`theta_gamma>=1` as well.

For a `j`-dimensional normal subspace `W`, `j<s`, the kernel of the slope
coordinate on `W^perp` has dimension at least `s-j`. It gives that many
independent polynomials in `C'`, all vanishing on
`X_W={x in D: v_x in W}`. If `r` independent degree-`<K` polynomials
vanish on a set `X`, division by its locator embeds their space into
degree-`<K-|X|` polynomials, so `|X|<=K-r`. Consequently
`|X_W|<=K-s+j`.

After `j` independent incident normals have been selected, for
`1<=j<s`, there remain at least `m-(K-s+j)=d+s-j` incident choices
outside their span. Their product is `(d+1)_rising_(s-1)`.

After `s` independent choices, the annihilator is one-dimensional. If its
slope coordinate is zero, a nonzero polynomial leaves at least `d+1`
incident choices outside that span. Otherwise its normalized equation is
`r_1=b`, `b in C'`, and at least `theta_gamma` choices lie outside. The
last extension factor is thus at least `theta_gamma` in both cases.

Let `z` count all zero normals, and let `g` count those whose affine
equation is identically satisfied. These parameters are independent of the
selected slope, and `0<=g<=z<=K-s`. At most `g` points of any selected
support have zero normal. The first nonzero choice therefore has at least
`m-g` possibilities.

Each record owns at least
`(m-g)*(d+1)_rising_(s-1)*theta_gamma` ordered independent coordinate
tuples. An independent `(s+1)`-tuple determines at most one parameter
point, so these tuples are disjoint between distinct selected slopes.
There are at most `(n-z)_falling_(s+1)` available tuples. Summation gives

```text
sum_gamma theta_gamma
  <= (n-z)_falling_(s+1) / ((m-g)*(d+1)_rising_(s-1)).
```

For fixed `z`, this is largest when `g=z`. Put
`f(z)=(n-z)_falling_(s+1)/(m-z)`. Where consecutive values exist,

```text
f(z+1)/f(z) = (n-z-s-1)*(m-z) / ((n-z)*(m-z-1)).
```

The sign of this ratio minus one is the sign of
`n-(s+1)*m+s*z`. This expression increases with `z`, so the sequence can
only decrease and then increase. Its maximum on `0<=z<=K-s` is at an
endpoint. Those endpoints give exactly the two expressions defining `C_s`.
The left side is an integer, so the floor is valid. This completes the proof.

## Scope

The theorem is uniform in the finite field, domain, received pair, and actual
explanation dimension. It is not a sharp prize-row bound by itself. It must
not be derived by summing a family-size bound using only the minimum margin;
the weighted tuple count above is the load-bearing argument.
