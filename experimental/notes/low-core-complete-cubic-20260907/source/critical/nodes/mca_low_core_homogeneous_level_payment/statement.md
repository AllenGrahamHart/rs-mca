# Affine-product levels: one-dimensional coefficient families

Status: PROVED, 2026-09-07. Let Kappa=F(X). Let P(U,V) in
Kappa[U,V] have total degree e>=2 and split into affine linear
factors over an algebraic extension, with at least TWO nonparallel
factor directions. Fix a NONZERO level R in Kappa. Consider
polynomial pairs of component degree <K satisfying the exact identity

    P(a,b)=R.                                          (HL)

Translated binary homogeneous levels H(a-c_0,b-c_1)=R are included,
but concurrence of the affine factors is NOT required. The node ID
retains the homogeneous-level origin of the proof.

In any fixed affine pair carrier (a_0+V) x (b_0+V), dim_F V=s>=1,
the algebraic coefficient locus of (HL) has every component of
dimension at most ONE. It is covered by a pure one-dimensional
coefficient variety of degree at most Delta=e^(2s-1).

For actual represented LOW pairs, with complete pair cores of size
at least m-t, K<=m-T and 1<=t<=T, their cumulative count satisfies

    M_t <= floor(Delta*(n-K+1)/(m-t-K+1)).                (1)

This counts joint pairs, not independent scalar projections. In the
original support-margin setup, for any group assigned to this curve,

    G=sum_(assigned gamma)(1-raw_gamma/(T+1))
      <=Delta*sum_(t=1)^T
        (n-m+t)*(n-K+1)/((m-t-K+1)*t*(t+1)).             (2)

One global margin resource and the original near charge can then be
combined with gains from other groups. They are not charged per curve.

In odd characteristic this includes every nonsingular affine conic
whose quadratic homogeneous part has rank two. It also includes
centered homogeneous cubic levels with at least two factor directions,
such as a^3+b^3=R in characteristic not three, or a^2*b=R.
The nonconcurrent affine-product cubic a*b*(a+b+1)=R is also included.
It does NOT include zero levels, products with only parallel directions, all
parabolas in moving coordinates, arbitrary cubics, or arbitrary curves.

The finite consumer pays degrees two and three and a mixed degree-seven
factor cover. The dimension theorem itself is degree-uniform; a failed
higher-degree numerical recipe is not an unsafe source.
