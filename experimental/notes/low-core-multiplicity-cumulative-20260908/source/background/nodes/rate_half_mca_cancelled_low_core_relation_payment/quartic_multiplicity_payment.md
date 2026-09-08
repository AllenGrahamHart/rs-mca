# Every prescribed quartic pays by double-point interpolation

Status: PROVED restricted source payment. Use the same canonical normalized
source and LOW_500 selection, now with 8764<=J<=9821. Suppose all but
at most 64 represented LOW pairs lie on ONE irreducible degree-four curve
G over F(X). No coefficient-height, smoothness, graph or normalization
hypothesis is required. Then the entire original source satisfies

    N=|Gamma|+134944 <=4194117119656075,
    B=274980728111395087,
    reserve>=270786610991739012.                       (DP4)

This consumer does not assert a quartic cover for arbitrary sources. Its
full-kernel child separately proves exhaustive coverage through 9526.

## 1. The exact full-space escape gap

Set A=J+66972, w=J-1, n=1048576+J and d=2*A. The new required
mca_multiplicity_interpolation_curve_escape supplier uses r=2, g=4:

    gap=Phi_w(2*A)-Phi_w(2*A-4*w)-4*n.

The full spaces have pair degrees 17/13 through J=8930, 16/12 through
9568, and 15/11 afterwards. Direct monomial summation therefore gives

    gap=4646608-480J, 8764<=J<=8930;
    gap=4110764-420J, 8931<=J<=9568;
    gap=3574924-364J, 9569<=J<=9821.                  (1)

All three affine expressions decrease. Their last values are 360208,
92204 and 80, so the gap is strictly positive on the whole range.
At the transitions the next values are 359744 and 91808. At J=9526
the gap is 109844. At J=9822 it is -284; that row is not certified.
All these counts keep the strict weighted degree and actual truncated
blocks. In particular the multiplicity conditions cost FOUR per point.

The supplier thus bounds all LOW pairs on G by

    4*floor((2*A-1)/w)<=4*17=68.                     (2)

This is a function-field point count, not a bound on only the positive-
dimensional coefficient families. It covers every singular and isolated
case automatically. All original evaluation coordinates are retained.

## 2. Original labels, exceptions and near

The <=64 off-curve pairs and all their labels stay present. Each LOW
pair has at most n-A=981604 original finite labels, by the unchanged
complete-core source contract. HIGH_500 consumes at least 5500 on the
one completed-basis resource C=23067643444721720934. Consequently

    N<=C//5500+134944+981604*(68+64)
      =4194117119656075.

This proves (DP4). No curve group is charged HIGH, no old /501 discount
is combined with the /5500 base, and no original scalar defect or near
allowance is removed or repeated. The general supplier uses no actual
carrier dimension; the resource and label conversion do use this exact
canonical source. This restricted theorem alone is not an original-row
endpoint or a proof of the entire 8764..9821 interval.
