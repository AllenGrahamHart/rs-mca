# Degree-free rational-pencil cover payment

Status: PROVED, 2026-09-07. Use the normalized KoalaBear source on
(n,K,m)=(1048576+J,J,67472+J), actual common carrier dimension eleven,
empty universal carrier core, and 4801<=J<=169999. Keep the original
near add-back 134944 and budget B=274980728111395087.

Choose the raw minimizers at cutoff T=500 on this fixed carrier. If the
represented LOW polynomial pairs admit either of the following covers,
the WHOLE original source is paid:

1. At most thirteen affine lines over F(X), each with nonconstant
   component direction: total <=269643200488601452, reserve
   5337527622793635.
2. One constant-direction affine line over F(X) and one nonconstant-
   direction affine line: total <=272837082864553899, reserve
   2143645246841188.

There is NO primitive-row-height or received-remainder-degree premise.
In particular a single arbitrary rational pencil is paid. A pencil over
F(X) is not a constant-component-direction line over F. The canonical
selector's rank-two condition over F does not exclude such pencils.

## 1. Partition and charge the original resource once

Assign each distinct LOW pair to one covering line, and assign all its
labels with it. Let U_i be the union of COMPLETE cores in this group,
e_i=n-|U_i| and G_i=sum_(assigned gamma)(1-raw_gamma/501).
The generic supplier `rational_line_cores.md` proves

    N_original <= 134944+F(J)/501+sum_i G_i.              (1)

This is a partition of LOW labels. No label in another LOW group is
declared HIGH. Preferred directions, higher-margin labels and source
values outside the various U_i are all retained in the proof.

For a group with two distinct pairs, primitive normalization of a pair
difference gives an EXACT polynomial identity A_0*a+A_1*b=Q.
All complete cores give that same identity on their union, including
roots of the original difference gcd. Its primitive height h may be
any value up to J-1. No old h<=66972 gate is used.

## 2. Uniform cost of a nonconstant-direction group

For h>=1 the pair parameters lie in an ordinary scalar polynomial
carrier of dimension at most ten. If |U_i|>=m, the generic group bound
is

    G_i <= n+e_i sum_(t=1)^500 V_(i,t)/(t(t+1)).           (2)

Here V_(i,t) is an ordinary scalar LIST cap on (|U_i|,J,m-t).
The n term pays preferred rational directions; it cannot be deleted.

Use the existing 99 intervals [a,b] covering e_i=0,...,981104,
the existing depth endpoints 1,...,20,50,100,200,300,400,500, and
the ordinary rank-ten LIST certificates at

    r=1048576-a, w=67472-v, k_max=254999.

Padding embeds both the current degree range and the smaller actual
domain in these certificates, within the unchanged field. For a depth
block u+1,...,v replace its cumulative count by the certificate at v.
The exact block weight is (v-u)/((u+1)*(v+1)). Therefore a uniform
integer ceiling for (2) is

    ceil max_[a,b] [1303575
        + b sum_blocks V_(a,v)*(v-u)/((u+1)*(v+1))]
      = 17111519376310956 < W=17200000000000000.          (3)

The maximum interval is [90000,99999]. These are ordinary LIST
certificates, not unexported numerical MCA Johnson/Hensel caps.

If |U_i|<m, two complete cores would overlap in at least
2(m-500)-(m-1)=J+66473>J points. Thus all pairs in the group coincide.
For that single pair, every assigned full-bad scalar support has at
least one noncore point, and those points are disjoint across labels.
Hence G_i<=n-|H_f|<=n<W. The same argument covers an arbitrary
singleton; an empty group costs zero. No small-union gap remains.

On the current J interval, F(J)<=C=23067643444721720934. Using
integrality of N_original, thirteen copies of (3) give

    N_original <= floor(C/501)+13*W+134944
                =269643200488601452 < B.                (4)

## 3. Constant-direction plus nonconstant-direction cover

For a constant-direction group, complete-core coverage and the empty
universal carrier core imply nonzero evaluation on C' at every point
of U_i. Anchor JOINT pairs there and divide by X-x. This gives the
same-carrier dimension-ten child LIST bound

    M_(i,t) <= |U_i|*V_(i,t)/(m-t),

with child row (|U_i|-1,J-1,m-t-1). Thus

    G_i <= 1+e_i sum_t
             (R+J-e_i)*V_(i,t)/((d+J-t)*t*(t+1)).        (5)

At most one finite kernel direction is included in the 1. This
groupwise argument does not need the other groups to disappear.

The already checked constant-branch numerical envelope, on the larger
4801<=J<=254999 interval, bounds the EXPRESSION

    134944+F(J)/501+the right side of (5)
       <=255637082864553899.                             (6)

Its convexity in J and its 99 by 26 block certificate are unchanged.
We reuse this coupled expression bound, not a bound formed by
independently maximizing its two terms. Small constant groups instead
cost <=n; adding the largest F(J)/501 still lies well below (6).
Adding one nonconstant group's W to (6) gives

    N_original <=272837082864553899 < B.                 (7)

The independent verifier rechecks all integer LIST transitions and
uses upward rounding to audit (3) and the constant expression (6).
All source geometry, cover partitioning and the degree-free step are
proved by hand; the arithmetic replay is not their proof.

## 4. Scope and strictness

The actual F_(19^6) control in the generic supplier has eighteen
canonical raw-one labels, lies on a rational pencil of height three,
and has ZERO full E-row space at the old cutoff ell=2. The extension
therefore addresses a genuinely omitted source mechanism. It is not
an unsafe witness or a claim that the deployed KoalaBear remainder
necessarily contains such an example.

The separate 27-point polynomial parabola needs at least fourteen
lines despite using a two-dimensional common carrier. Thus neither
function-field affine rank two nor carrier dimension eleven proves
either cover premise. The current unpaid family must fail both printed
cover tests, but a collective count for it remains open. No original
critical red, higher-rank source, unrestricted bracket or prize closes.
