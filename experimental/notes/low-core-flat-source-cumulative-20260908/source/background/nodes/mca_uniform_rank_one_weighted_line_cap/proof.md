# Proof

## Weighted-line reduction

If every explanation equals h_*, pair noncontainment forces every selected
support to include a coordinate with r_1(x)!=0. Such a coordinate determines
gamma uniquely from r_0(x)+gamma*r_1(x)=h_*(x). Thus there are at most
`n<=2R<4070947` slopes. Otherwise use the affine explanation line
`h_*+lambda P`, with P a nonzero degree-<K polynomial.

The coordinate incidence equation in (gamma,lambda) is
`gamma*r_1(x)-lambda*P(x)=h_*(x)-r_0(x)`. Remove the u coordinates
where this equation is identically satisfied. They are roots of P, so
`u<=K-1`. Put j=K-u, N=R+j, M=d+j. A never-satisfied zero-normal equation
is unused; all other coordinates define affine lines. Merge identical
lines, retaining their weights; total weight is at most N.

Every selected parameter point has at least M incident coordinates and
at least two line classes. Indeed, a sole nonvertical line class supplies
one pair `(h_*+alpha P,beta P)` explaining the received pair there and on
the removed universal coordinates, contradicting same-support badness.
A sole vertical class plus universal coordinates consists entirely of
roots of P and cannot contain the original m>K coordinates. Select an
exact M-subset retaining at least two classes.

Put q=floor(M/2). If every class in that subset has size at most q,
its cross-class coordinate pairs number at least q(M-q): use
`sum w_i^2<=q*M` and `M>=2q`. A pair from distinct affine lines belongs
to at most one selected parameter point. This proves W_low.

Otherwise the chosen support has a unique dominant class, of size >q.
Let t distinct lines occur as dominant lines, with full coordinate weights
w_i. Then `t<=floor(N/(q+1))`. Define
`a_i=M-min(w_i,M-1)`, so `1<=a_i<=q` and `M-a_i<=w_i`.
For each dominant line, at most t-1 selected points also meet another
dominant line. Every other assigned point needs at least a_i coordinates
from nondominant lines. When w_i>=M-1 this uses the retained second class
to force at least one outside coordinate. A nondominant line meets the
fixed dominant line at most once. Relaxing its total available weight to
`N-t*M+sum a_i` proves the high-part objective in the statement.

Holding all other deficiencies fixed, the variable part is
`(C+a)*(Q+1/a)`. If C>=0 it is convex on [1,q], and every endpoint is
feasible. If C<0 it is increasing there, and raising a to q preserves
nonnegative remaining weight. Repeating proves that deficiencies {1,q}
suffice for the upper bound.

## Uniform low bound

Write c=R-d=981104, so N=M+c and M>=67473. Then

```text
q*(M-q)>=M*(M-1)/4,
N/(M-1)<=1048577/67472<311/20.
```

The latter strict inequality follows from
`20*1048577=20971540<20983792=311*67472`. Consequently

```text
binom(N,2)/(q*(M-q)) < 2*(311/20)^2=96721/200<484,
```

so W_low<=483.

## Uniform high bound

Let l deficiencies equal 1 and r equal q, so t=l+r. Put
`b=M-q>=q`, `W_0=N-l*(M-1)`. The high objective is

```text
F(l,r)=(l+r)*(l+r-1)+(W_0-r*b)*(l+r/q),
W_0-r*b>=0.
```

Here q>=33736 and `N/q<=2+981105/q<32`, hence t<=31. If l=0,
`F(0,r)<r*(r-1)+32r<=1922`. If l>=1, removal of the q-deficiencies
preserves feasibility, and exact subtraction gives

```text
F(l,r)-F(l,0)
 =r*(2l-1+W_0/q-l*b+r*(1-b/q)).
```

For r>0 its bracket is less than
`2l-1+32-l*q=31-(q-2)l<0`. Thus mixed endpoint histograms cannot
beat their all-deficiency-one counterpart. For r=0,

```text
F(l,0)=-(M-2)l^2+(N-1)l
      <=-67471l^2+1048576l,
```

since increasing M decreases this expression by l(l-1) per unit.
The last integer quadratic is maximized at l=8: its forward differences
at l=7 and l=8 are respectively 36511 and -98431 and decrease with l.
Its value at 8 is

```text
8*1048576-64*67471=4070464.
```

This histogram is feasible at j=1: remaining weight is 508801. Also at
j=1, `q*(q+1)=1138151432` and

```text
binom(1048577,2)-483*q*(q+1)=29196520
```

lies between 0 and q*(q+1), so W_low=483 there. Hence the certificate
maximum is exactly 4070947. The disjoint low/high split proves the slope
bound. No claim about the scan's step counts or actual extremal received
lines is needed.
