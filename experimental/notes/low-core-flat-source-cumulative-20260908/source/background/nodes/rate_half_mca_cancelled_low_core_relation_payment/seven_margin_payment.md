# Seven-margin payment and the very-low family

Status: PROVED, 2026-09-07. Use the same fixed normalized KoalaBear
carrier and row as `maximal_support_low_span.md`:

    R=1048576, d=67472, s=11, 4801<=J<=169999,
    n=R+J, K=J, m=d+J, q=2130706433^6,
    B=274980728111395087, original near charge=134944.

The actual explanation dimension is eleven and the universal carrier
core is empty. Raw always means the untruncated selected-support minimum
over the fixed second-polynomial carrier. The following are unconditional
payments of the stated source classes, not assumptions about every source.

1. If every selected raw margin is >=7, the whole original total is
   <=274928364476952114, with reserve 52363634442973.
2. The same total pays every nonzero row of degree <=66972 whose
   received remainder on the COMPLETE raw<=500 core union has degree
   <=m-7. This enlarges the previous remainder band by 132 degrees.
3. If the raw<=6 selected subfamily has error rank <=8, the whole
   original total is <=274971532963425180, reserve 9195147969907.

Consequently every unpaid source has at least 61100872739557 selected
labels of raw<=6, and that subfamily has error rank at least nine.
Under the canonical selection already proved, these supports contain all
defects of their complete scalar agreement sets, with at most six defects
per label, and have only rank-two cross-core differences.

## 1. Reuse the full weights, not just their minimum

The required core-completed-basis theorem supplies weights

    w(r;g)=max(min(d+1,r), b(r;g)),
    b(r;g)=12*r*(m-r-g)/(m-g)*prod_{i=1}^{10}(d-r+i)/(d+i)

for 1<=r<=d, with b=0 for r>d. They are charged to ONE tuple
resource; the old and new lower counts are not added. Put M=m-g.
Its proof gives M>=d+11. For fixed r<=d, b increases with M, so
the value at M=d+11 is a uniform lower bound. Define

    alpha =12*d/(d+11),
    omega =84*(d+4)/(d+11)*prod_{i=1}^{10}(d-7+i)/(d+i)
          =1359828247211942851691371569952
            /16206915841717723963443447881.

Every record has w>=alpha by the existing theorem. We claim every
record with r>=7 has w>=omega. On 7<=r<=84 the logarithmic
derivative of b at M=d+11 is at least

    1/r - 11/(d+1-r) > 0,

because 12*84<d+1. Thus b(r)>=b(7)=omega in that interval.
For r>=84, the old min(d+1,r) term is >=84>omega. This covers
all larger r, including r>d, without extrapolating the core formula.
Only positivity and the printed strict derivative inequality are used.

The empty-core endpoint resource was independently certified in the
low-span companion. Convexity gives throughout the CURRENT J interval

    sum_gamma w(raw_gamma;0) <= C=23067643444721720934.

If every raw>=7, divide by omega, floor once and add the original
near charge. The result is 274928364476952114, strictly below B.
The analogous uniform weight at raw six would give the over-budget
recipe 320697470408695467. This rejects that recipe, not actual safety
of raw-six sources, and is not a claimed sharp cutoff for the true count.

## 2. The bounded-remainder consequence

Keep T=500, ell=66972 and A=m-500. Let a nonzero row R_0,R_1
of degree <=ell and a received remainder Q with deg Q<=m-7 be
given on the SAME complete low-core union. If deg Q<A, the already
proved exact-relation branch gives total <=255637082864553899.

Otherwise A<=deg Q<=m-7. For every represented low pair f,
deg(R*f)<=K-1+ell=A-1, so R*f-Q is a NONZERO polynomial.
It vanishes on the COMPLETE pair core H_f, hence

    |H_f|<=deg Q<=m-7,
    raw_gamma=m-|S_gamma intersect H_f|>=7.

HIGH labels already have raw>=501. Thus every label satisfies the
previous weight payment. This retains the complete-core and whole-family
guards: no agreements outside an arbitrary chosen subdomain are discarded.
There is no subfield, cyclic-generator or new margin hypothesis on the row.
The same saturated common-core transport used before preserves this
remainder-degree condition; its proof is not tied to the old number 139.

The new band A..m-7 has 494 integer degrees; the former A..m-139
band had 362. Every unpaid cyclic generator's degree-adapted E-residual
now has degree >=m-6. There is NO upper degree <m asserted here:
remainders of degree >=m can still occur. In the removed J>=170000
interval the independent whole-interval payment already applies.

## 3. A small-margin rank branch is paid as well

Let L_6 be the number of labels with raw<=6, and H_7 the remainder.
The same resource, with no label omitted, gives

    alpha*L_6 + omega*H_7 <= C.

If the error affine rank of L_6 is at most eight, the existing
same-source error-rank gauge puts its explanations into dimension <=7.
The uniform padded-Johnson cap from this consumer's proved ancestry is

    L_6<=V7=50371450079970.

It counts arbitrary selected subfamilies, requires no child-near premise,
and uses the SAME q satisfying its field gate q>=2R. Therefore

    L_6+H_7 <= [C+(omega-alpha)*V7]/omega.

Floor and add near once to obtain the stated 274971532963425180.
This pays a new class even if the larger raw<=500 subfamily has error
rank twelve. It does not assume that rank drops when removing labels.

Conversely, if the original count exceeds B, the selected non-near
count is at least B-134944+1. Rearrangement gives

    L_6 >= ceil([omega*(B-134944+1)-C]/(omega-alpha))
        =61100872739557 > V7.

Thus its error rank is >=9 and <=12. Unlike the full-rank raw<=500
subfamily, this rank lower bound does NOT force its common agreement
core to be empty. Canonical support/explanation selection occurs first,
then both rank tests. The maximum-margin theorem applies also with T=6,
since 12<d, and provides the complete-defect and rank-two conclusions.

## 4. Short hand-checkable certificate

The conclusions do not depend on trusting a large rational numerator.
The following smaller coefficients give a slightly weaker independent
certificate:

    alpha >=5999/500,      omega >=10488/125.

The first follows by cross multiplication. For the second, the eleven
factors in b(7)/84 are each >=1-7/(d+1). The elementary product
inequality prod(1-x_i)>=1-sum x_i for 0<=x_i<=1 gives

    omega >=84*(1-77/67473)>10488/125;
    6468*125=808500 < 12*67473=809676.

Thus the whole weighted inequality has the integer relaxation

    5999*L_6 +41952*H_7 <=500*C.

If L_6=0, its original total is <=274929007493481160<B. If
L_6<=V7, the original total is <=274972175989493869<B, with
reserve 8552121901218. An unpaid source must have

    L_6>=ceil([41952*(B-134944+1)-500*C]/35953)
       =60350551072932 >V7.

The exact weights in the earlier sections improve these numbers to the
printed headline constants, but the simple integer relaxation independently
certifies both source payments and the rank-at-least-nine conclusion.

## Remaining task and limitations

This sharpens the actual source restrictions and pays additional whole
source classes. It neither pays the required large raw<=6 family nor
changes the residual interval 4801..169999 or any unrestricted bracket.
Do not open six speculative per-margin nodes or identify these raw margins
with the unrelated trade-height h from the older shift-pair program.
The next count must treat their actual coherent low family collectively.

The earlier single-support budget obstruction remains decisive: even
perfectly independent raw-one core tuples leave an over-budget upper
recipe at J=4801. Better counting of individual tuples alone cannot be
promised to close the interval. No general or paving-matroid extremal
theorem was imported into this proof; this is a direct specialization of
the already proved weight formula.
