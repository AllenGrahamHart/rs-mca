# Weighted incidence for an affine-singular one-place cubic

Status: PROVED. Let F have characteristic zero, or p>3 with p>=K.
Let V be an s-dimensional space of degree-<K polynomials, s>=1, and
fix an affine pair carrier (a_0+V)x(b_0+V) of component degree <K.
Let G over F(X) be a geometrically integral plane cubic whose projective
completion has one geometric point at infinity, smooth there, and an
affine singular point. Take primitive A,B in F[X] so its top binary
form is c*(A Y+B Z)^3, and put

    h=max(deg A,deg B), d=dim ker[(v,w)->A*v+B*w on VxV],
    N_input=2s-d, r_0=ceil(d/3).

Every component of its original polynomial-pair coefficient locus has
dimension <=r_0. Suppose a stronger integer bound 0<=r<=r_0 is known for that
locus; otherwise use r=r_0. For n distinct evaluation points, joint
agreement >=A_agree>=K+h, and

    Q_h=(n-K-h+1)/(A_agree-K-h+1)>=3,

the number M of represented polynomial pairs satisfies

    M <= floor(2^d * 3^(2s-d-r) * Q_h^r).               (WC)

This includes the singular pair and every coefficient component.
The input degree K+h is retained. Neither normalization parameter poles
nor any original evaluation points are discarded. Weighted incidence is
proved by an elementary finite power cover, not assumed as a black box.

If 1<=d<s, m_0=floor((s-1)/(s-d))>=1 gives the additional bound

    m_0*h<=K-1.                                      (H)

If d=s, then h=0. If d=0, dimension is zero and M<=3^(2s),
without needing the LIST ratio. The proof of (H) is in `projection_height.md`.

## Finite consequence

The [completed-basis refinement](completed_high_weight.md) uses the
proved HIGH weight >=5500 and leaves only

    d=7, dim Y=3, 1301<=h<=4327;
    d=10, dim Y=4, 1<=h<=865.

The resulting paid alternative, including <=64 off-curve pairs, is
N<=274979661292365251, reserve 1066819029836. In particular d=11
is fully priced, not an unpaid case. A whole source on one constant-
infinity-direction affine-singular cubic, without off-curve exceptions,
pays N<=268384711205699531 throughout 4801..169999.

### Baseline using only the raw resource

On the canonical normalized KoalaBear source, s=11,
(n,K,m)=(1048576+J,J,67472+J), T=500 and 7117<=J<=8655,
this pays a LOW group on such a cubic whenever

    d in {0,1,2,3,4,5,6,8,9}.

With the one global resource/near allowance and <=64 off-curve pairs,
the largest resulting whole-source bound is

    |Gamma|+134944 <=261013572486287276,
    reserve =13967155625107811.

The d=7,10,11 cases also pay if coefficient dimension is at most
2,3,3 respectively. Therefore an unpaid source in the full-kernel
lower-strip reduction must have (d,dim coefficient locus) equal to

    (7,3), (10,4), or (11,4).

This parameter d is a projection-kernel dimension, not raw margin, error
rank or the trade-height h from a different lane. The three surviving
dimension patterns have actual polynomial examples. They are not declared
impossible or unsafe. No closure of the interval, original red, unrestricted
row or either prize is claimed.
