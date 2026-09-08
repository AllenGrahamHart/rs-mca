# Assemble the d=7 source bound

The required weighted supplier gives dimension <=ceil(7/3)=3 for the
whole original coefficient locus Y. Split represented nonsingular pairs
into those lying on a three-dimensional irreducible component and those
outside the union of all such components. Components and their dimensions
are geometric; no rationality over the original finite field is assumed.

## 1. All three-dimensional components

`component_degree.md` bounds their number by 3^16=43046721.
`component_list.md` gives <=315 rich nonsingular pairs per component,
uniformly on the exact source and 1301<=h<=4327. Thus their total
contribution is at most

    315*43046721=13559717115 pairs.                    (1)

Possible intersections of components are only overcounted. There is no
assumption that Y has one component or that one component represents
all original labels.

## 2. Pairs outside all three-dimensional components

Use the weighted supplier's finite power cover with 15 image variables
of weight two and seven kernel variables of weight three. Choose its
auxiliary shifts away from the finite set of counted pairs. Each pair
has exactly 2^15*3^7 lifts. The WHOLE lifted equation locus Z is
defined by equations of degree <=6 in 22 coordinates and satisfies

    sum_i deg(Z_i)*6^(dim Z_i)<=6^22.                  (2)

Every lift of a pair outside all three-dimensional components of Y is
outside every three-dimensional component of Z: the finite map sends
such a component onto a three-dimensional component of Y. Its lifts
are therefore covered by the components of Z of dimension <=2.

Retain just these components in (2). The required scalar-projection
incidence proof bounds their rich points by deg(Z_i)*(2Q_h)^dim(Z_i),
where

    Q_h=(1048577-h)/(66973-h)>=3.

The projection retains finite fibers on every subvariety. Dropping the
nonnegative three-dimensional terms from the budget and using Q_h>=3
gives, after division by the exact lift multiplicity,

    M_low <= floor(2^7*3^13*Q_h^2)
          <= floor(2^7*3^13*(1044250/62646)^2)
           = 56703328989.                             (3)

This is NOT application of a dimension-two theorem to the entire
dimension-three locus. It is its proof's nonpure budget restricted to the
lower-dimensional components of the actual lift. No artificial pure
over-cover or uncontrolled scalar-constant component is introduced.

## 3. Original-label and resource accounting

Add the one possible singular pair and the at most 64 off-curve LOW
pairs supplied by the full-kernel consumer. Equations (1)--(3) give

    M_ALL <=13559717115+56703328989+1+64
           =70263046169.

The extra singular allowance may duplicate a lower-dimensional count,
which is a harmless upper relaxation. Every LOW pair has its complete
joint core of size >=m-500. Its nonempty scalar defects for distinct
finite labels are disjoint outside that core, so it carries at most
n-m+500=981604 labels. This counts original finite slopes, not supports.

The required completed-HIGH weight is >=5500. With the SAME global
resource C=23067643444721720934 and original near added once,

    N <= C//5500+134944+981604*M_ALL
       =73164604161759423,
    B-N >=201816123949635664.                          (4)

No LOW component is relabelled HIGH, and the resource is not repeated
between the component split. No original coordinates or near labels are
discarded by a parameter change. The count is over the original field;
constant extension only supplies geometric upper bounds.

## 4. The full-kernel consumer

Its existing necessary restriction on 7117..8655 is

    N<=274979661292365251,
    OR the affine-singular d=7,dim Y=3,1301<=h<=4327 source.

The second alternative pays by (4), below the first constant. Thus every
canonical normalized source in that entire strip pays by the first bound.
This last application is owned by the consumer, not a reverse premise of
this supplier. The earlier d=10 result and all kernel/factor-coverage
theorems keep their actual requirements. No arbitrary cubic source
description is assumed as a substitute for the full-kernel proof.

The previous quadratic strip ends at 7116, so the newly paid interval
has 1539 integer J-values and the combined paid interval is 4801..8655.
The remaining normalized range begins at 8656; higher J, higher original
error ranks, the unrestricted adjacent endpoint and both prizes stay open.
