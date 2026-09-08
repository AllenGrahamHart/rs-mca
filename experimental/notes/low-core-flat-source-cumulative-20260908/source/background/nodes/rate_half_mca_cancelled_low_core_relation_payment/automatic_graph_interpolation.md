# Automatic graph-or-parallel-fibers interpolation payment

Status: PROVED, 2026-09-07. Keep the normalized KoalaBear source,
(n,K,m)=(1048576+J,J,67472+J), actual carrier dimension eleven,
empty universal carrier core, 4801<=J<=169999, canonical raw
minimizers and COMPLETE LOW_500 union U. Original near add-back is
134944 and B=274980728111395087. Put ell=66972 and A=J+ell.

The WHOLE original source is paid whenever

    |U| < D_graph(J),
    D_graph(J)=ell+1+sum_(i=0)^7 max(A-i*(J-1),0).       (AUTO)

No graph-description premise occurs in (AUTO). For example,
D_graph(4801)=506757, so |U|<=506756 is paid. Uniformly on
4801<=J<=9000, |U|<=J+413000 is sufficient. This is a criterion
on U_500, NOT an identification with the earlier U_6 union.

## 1. Rational-coefficient graph costs are unchanged

The generic `rational_coefficient_graphs.md` extends the graph theorem
to Psi in F(X)[Y]. Its component-dimension and degree costs are
unchanged. Thus on this finite source, degrees two through seven cost
at most 167137715680311148, retaining degree-two total
46570195123304300. The characteristic 2130706433 divides none of
these degrees. The existing primary and independent graph endpoint
certificates apply literally; no new numerical MCA cap is required.

## 2. Seven parallel constant-direction fibers also pay

Suppose all represented LOW pairs satisfy one of at most seven
identities L(f)=c_i(X), for ONE fixed nonzero constant component row
L and distinct degree-<J polynomials c_i. Partition pairs and labels
by these identities; write U_i for their complete core unions and
e_i=n-|U_i|. Each U_i lies in the scalar agreement set L(y)=c_i.
For i!=j, root counting gives

    |U_i intersect U_j|<=J-1,
    |U_i|+|U_j|<=n+J-1.                                 (2)

Thus at most one group exceeds (n+J-1)/2 points. All other groups
have e_i>=ceil((n-J+1)/2)=524289. The common direction is essential;
seven arbitrary constant-direction pencils are not asserted to pay.

Use the partitioned original margin resource from
`rational_pencil_cover_payment.md`:

    N_original<=134944+F(J)/501+sum_i G_i,
    G_i=sum_(assigned gamma)(1-raw_gamma/501).

Its joint anchor argument bounds a constant group's gain by

    G_i<=1+e_i sum_(t=1)^500
        (R+J-e_i)*V_(i,t)/((d+J-t)*t*(t+1)),             (3)

where R=1048576, d=67472 and V_(i,t) is the ordinary rank-ten
LIST cap for its divided common-carrier child. Preferred directions
are included in the 1. The bound uses complete cores and the empty
universal carrier core, not componentwise unrelated carriers.

Designate the potentially large group (any group if all are small).
The existing coupled constant-branch expression certificate gives

    134944+F(J)/501+G_large<=255637082864553899.          (4)

For every other group use the existing e-rectangles [a,b] that meet
[524289,981104]. Over a depth block u+1,...,v, its gain is at most

    1+b sum_blocks V_(a,v)*(v-u)/((u+1)*(v+1))
                        *(R+4801-a)/(d+4801-v).         (5)

The LIST caps use r=R-a,w=d-v,k_max=254999 as before. The ratio
(R+J-a)/(d+J-v) decreases with J because R-a-d+v>0;
the endpoint J=4801 is therefore valid. Taking a=520000 for the
first intersecting rectangle only enlarges the cap. Exact rational
arithmetic gives ceiling 895247541220804 for (5), attained at
[520000,529999]. The independent audit checks every included
integer LIST trace and rounds upwards.

If |U_i|<m, any two complete cores overlap in more than J points,
since 2(m-500)-(m-1)=J+66473>J. All pairs in the group coincide
and its gain is at most n, far below (5). This also handles singleton
groups in (4); empty groups cost zero. Consequently seven parallel
groups have the whole-source bound

    N_original<=255637082864553899+6*895247541220804
               =261008568111878723,
    reserve=13972159999516364.                           (6)

F(J), HIGH labels and the original near add-back are paid ONCE.
No other group's LOW labels are reclassified as HIGH to obtain (4).

## 3. Homogeneous interpolation: every outcome is paid

Use a fixed constant invertible component change if desired and denote
the transformed received pair by (u,v). Solve the homogeneous linear
system, one equation at every x in U,

    B(x)*v(x)=sum_(i=0)^7 P_i(x)*u(x)^i,
    deg B<=ell, deg P_i<A-i*(J-1).                       (7)

A nonpositive upper degree bound means P_i=0. The number of
coefficient unknowns is exactly D_graph(J). Under (AUTO) a nonzero
solution exists over the original field. There is no need to force
B!=0, set a coefficient equal to one, or delete its roots.

For every represented pair (a,b), the polynomial
B*b-sum P_i*a^i has degree <A and vanishes on its complete
core of size at least A. It is identically zero. Exhaust the cases:

1. B!=0 and deg_Y sum P_i Y^i>=2: a rational-coefficient polynomial
   graph of degree at most seven, paid by section 1.
2. B!=0 and this degree is at most one (including zero numerator):
   one affine line over F(X), paid by the existing degree-free pencil
   theorem, whether its direction is constant or nonconstant.
3. B=0: the nonzero polynomial sum P_i Y^i over F(X) has at
   most seven roots there. Hence the represented first polynomials
   have at most seven distinct values. These are the parallel fibers
   in section 2. If its Y-degree is zero, there are no LOW pairs.

The largest of the relevant conservative whole-source bounds is
272837082864553899 (the existing mixed-pencil envelope); each is
strictly below B. Thus (AUTO) is an unconditional source-class
payment. It is not an efficient algorithm for constructing the large
interpolation matrix, and no such matrix was allocated locally.

When all eight summands are positive,
D_graph(J)=602777-20J. On 4801<=J<=9000 this exceeds
J+413000 by at least 777. The general max formula, not that affine
simplification, applies at larger J.

## 4. A forced plane relation on the lower strip, not yet a payment

Continuation: `homogeneous_level_factor_payment.md` now pays certain
recognized nongraph factors and a total-degree-seven mixed cover.
It does not change the general-factor gap stated below.

Allow all monomials Y^a Z^b of a+b<=7 with X-coefficient degree
<A-(a+b)*(J-1). Their interpolation dimension is

    D_plane(J)=sum_(i=0)^7 (i+1)*max(A-i*(J-1),0).

On 4801<=J<=10244 all terms are positive and
D_plane(J)=2411160-132J>1048576+J=n. Thus for EVERY such
source, regardless of |U|, a nonzero total-(Y,Z)-degree-<=7 plane
relation is forced on all represented LOW pairs by the same root
argument. At J=10245 this strict dimension test already fails.

This does not say the relation is linear in one component or that its
factors are graphs. A collective payment for the remaining nongraph
components is open. The statement provides a concrete next counting
problem instead of another unproved graph-existence premise. Neither
the full J band, higher source ranks, unrestricted bracket nor either
prize closes here.
