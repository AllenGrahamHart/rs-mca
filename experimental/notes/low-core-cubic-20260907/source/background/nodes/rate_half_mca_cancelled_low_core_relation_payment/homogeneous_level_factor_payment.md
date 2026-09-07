# Affine-product levels and a mixed degree-seven factor payment

Status: PROVED, 2026-09-07. Keep (n,K,m)=(1048576+J,J,67472+J),
actual common carrier dimension eleven, empty universal carrier core,
4801<=J<=169999, T=500, original near 134944 and
budget B=274980728111395087. All unions and supports are complete
and selected as in the current consumer contract.

## 1. Pay nongraph quadratics and cubics with their full degree cost

The new generic supplier proves dimension <=1 for the exact pair
identity P(a,b)=R, with fixed nonzero R and degree-e polynomial P
over F(X) that splits geometrically into affine linear factors with
at least two nonparallel directions. It includes fixed rationally
centered homogeneous levels, nonsingular conics whose quadratic part
has rank two, and nonconcurrent affine-product cubic levels.
Its coefficient degree charge on this carrier is e^21, not a graph
degree charge or a claim of one coefficient component.

Write C=23067643444721720934 for the current upper bound on F(J).
For a group of LOW labels assigned to this curve, the cumulative
raw-weighted gain from the supplier is at most e^21 times

    Z=sum_(t=1)^500
      (981104+t)*1048577/((67473-t)*t*(t+1)).             (1)

The exact integer ceilings are

    G_2<=31914462418027,
    G_3<=159185671413625180.                             (2)

The whole original source on a single such quadratic or cubic is
therefore bounded, respectively, by

    floor(C/501)+G_2+134944=46075114951019479,
    floor(C/501)+G_3+134944=205228871902226632.           (3)

Their reserves are 228905613160375608 and 69751856209168455.
These are original-source payments, including HIGH labels and near.
The e=4 version of THIS conservative degree recipe exceeds budget;
that is not an unsafe example or a general quartic obstruction.

The weighted count matters. For raw r, expand
1-r/501=sum_(t=r)^500 r/(t*(t+1)); per pair the cumulative RAW
at depth t is at most n-|H_f|<=981104+t. The complement is
of its own complete core, not the union. Use the depth-dependent
JOINT pair bound e^21*1048577/(67473-t) before summing. A single
unweighted depth-500 label cap discards useful cubic reserve.

## 2. Affordable ordinary factors cost at most their degree times W

Set W=17200000000000000. The following group gains cost at most
delta*W for a polynomial factor of total component degree delta:

1. A nonconstant-direction affine F(X)-line, delta=1. Use the
   existing degree-free group bound <W, retaining preferred directions.
2. A rational-X polynomial graph of degree delta=2,...,7, after
   one fixed constant invertible component change. The coordinate
   changes may be different for different groups and count pairs only.
3. An affine-product level quadratic from section 1, delta=2.

For graphs let r=6 for delta=2 and r=5 otherwise. The earlier
pair theorem gives a raw LOW-label bound

    delta^(11-r)*(63/4)^r*981604,

since 1048577/66973<63/4. The quadratic case is checked separately.
For 3<=delta<=7, divide by delta; the remaining factor delta^5
increases, so the single endpoint delta=7 proves cost<=delta*W.
Group gain is at most this LOW-label count. No global resource is
charged per graph. The affine-product quadratic bound (2) is much
smaller than 2W. A constant-direction line is NOT given price W.

## 3. Mixed cover theorem

Suppose the represented LOW pairs have a cover by polynomial curve
identities over F(X), whose total component degrees sum to at most
seven. Every covering curve must be one of the affordable types in
section 2, except for at most ONE affine-product level cubic as in
section 1. Assign each pair to one covering curve, keeping its labels
with it. Then

    N_original <= floor(C/501)+sum_group G_i+134944.

With no exceptional cubic, the bound is

    floor(C/501)+7W+134944=166443200488601452.            (4)

With one, the remaining total degree is at most four, giving

    floor(C/501)+G_3+4W+134944=274028871902226632,
    reserve=951856209168455.                             (5)

This includes one affine-product level cubic plus four nonconstant
rational pencils. It also includes graph and quadratic components
under the same total-degree allowance. No other LOW group is treated
as HIGH, and the original resource and near are used exactly once.

Two general affine-product level cubics, constant-direction line factors,
unrecognized conics/cubics and arbitrary higher-degree factors are not
silently included. The old parallel-fiber and other payment routes
remain available at their own printed scopes.

## 4. Connection to the forced relation

On 4801<=J<=10244 the preceding homogeneous interpolation theorem
forces a nonzero plane relation of total component degree <=7 on
every represented LOW pair. If its distinct factors over F(X) all
have the types in section 3, with at most one exceptional cubic, the
mixed cover theorem pays the WHOLE original source. Their degrees
sum to <=7 even after repeated factors are removed.

This factor recognition is an explicit source test, not a claim that
all factors pass it. The remaining task is a collective count for
unrecognized factors or a different payment for their shared source.
The general lower strip, larger J interval, higher ranks and both
prizes remain open. No large interpolation or factorization computation
was performed to prove these dimension and payment statements.
