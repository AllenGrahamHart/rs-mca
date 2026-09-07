# Completed-basis weights leave only two residual patterns

Use the SAME canonical normalized source, s=11, excess D_0=67472,
T=500 and empty universal core. The required completed-basis resource
gives sum_gamma w(r_gamma)<=F(J)<=C=23067643444721720934, where

    w(r)=max(min(D_0+1,r),b(r)),
    b(r)=12*r*(M-r)/M * product_(i=1)^10 (D_0-r+i)/(D_0+i),
    M=m>=D_0+11,

for r<=D_0, and b=0 beyond D_0. C is already proved on the whole
4801..169999 interval. No raw minimum is reselected or transported.

## 1. Every HIGH record has weight at least 5500

HIGH means r>=501. For r>=5500 the truncated weight suffices. For
501<=r<=5500, the logarithmic derivative of b(r) is at least

    1/r - 11/(D_0+1-r) >0,

since 12*5500=66000<67473. Also b increases with M. Thus it is
at least b(501) with M=D_0+11. On its eleven positive factors use
product(1-x_i)>=1-sum x_i to obtain

    b(501)>=6012*(1-5511/67473)>5500,
    6012*(67473-5511)-5500*67473=1414044>0.             (1)

Since LOW weights are nonnegative, |Gamma|<=C/5500+L for LOW label
count L. A cubic pair cap M_c and <=64 off-curve pairs therefore give

    N<=base_5500+981604*(M_c+64),
    base_5500=C//5500+134944=4194116990084347.           (2)

One global resource and original near allowance are counted. No other
LOW group is reclassified HIGH; discarding positive LOW weights is only
an upper relaxation. Retaining them could improve the result further.

## 2. Apply the same weighted pair counts

Using the pair/height table from `proof.md`, every d outside {7,10}
now pays. The largest total is the formerly unpaid d=11 case:

    base_5500+981604*(269141725396+64)=268384711268522187,
    reserve=6596016842872900.                         (3)

Here h=0. With no off-curve exceptions, a whole source on ANY such
constant-infinity-direction affine-singular cubic has total
268384711205699531 throughout 4801..169999. This larger-interval
claim uses the general dimension count and h=0, not an extrapolation of
the lower strip's h bounds or its kernel coverage.

For d=7,dim Y=3 the bound increases with h. At h=1300 it gives

    base_5500+981604*(floor(2^7*3^12*((1048577-1300)/(66973-1300))^3)+64)
      =274979661292365251 < B=274980728111395087,
    reserve=1066819029836.                            (4)

So every h<=1300 pays. At h=1301 the same sufficient expression is
274991255669975911>B, which is recipe failure, NOT an unsafe witness.
The earlier height lemma gives h<=4327 for d=7, and h<=865 for
d=10 on J<=8655. Height zero would give d=11, so d=10 has h>=1.
The earlier lower-dimension prices only improve under (2).

Hence the full-kernel child has the stronger dichotomy: either
N<=274979661292365251<B, or its affine-singular residual satisfies

    d=7,  dim Y=3, 1301<=h<=4327;
    d=10, dim Y=4,    1<=h<=865.                      (R2)

The larger paid-alternative constant in (4) must accompany this stronger
restriction. The old raw-resource table and its three patterns remain
valid baseline bounds, not the current unresolved set. Singular pairs,
all original labels and coordinates are retained. No interval closes.
