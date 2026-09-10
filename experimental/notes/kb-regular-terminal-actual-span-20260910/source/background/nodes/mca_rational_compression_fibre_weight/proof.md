# Pack Actual Fibres And Charge Inside Defects Globally

Choose an actual pair f_* as affine offset and z outside H.
Since W has function-field rank two, G=A0*z_a+A1*z_b is nonzero.
Otherwise W would be contained in the one-dimensional function-field
kernel of (A0,A1). The original polynomial H_a*G has degree<=K+h-1.

Each actual fibre has the form f_*+H_a*(c*z+H), with distinct c in F.
If x lies in C_c intersect C_d for c!=d, two actual pairs in those
fibres both equal the receiver there. Applying the row to their
difference gives (c-d)*H_a(x)*G(x)=0. Hence all fibre unions are disjoint
outside one common root set of size b<=K+h-1. For nu occupied fibres,

    sum |C_c|<=n+(nu-1)*b<=n+(nu-1)*(K+h-1).

Subtract nu*(K+h-1) to obtain PACK. Each occupied union contains a core
of size>=A, so every shifted mass is positive. Empty families cost zero.

## Scalar Parameterization And Original Labels

Inside a fixed fibre choose an actual base pair f_c. Pair differences
are uniquely H_a*(A1,-A0)*u with u in T. Their degree<K implies
deg u<K-a-h. At every coordinate in C_c, receiver compatibility with
the primitive row holds. Away from the anchors define an auxiliary
scalar receiver using a nonzero component of (A1,-A0), pointwise.
Coprimality ensures such a component exists everywhere. Every joint
agreement outside the anchors is a scalar agreement for u. This gives
the printed LIST parameters and injectivity without dividing a received
polynomial or requiring the base pair to be divisible by H_a.

For an original selected defect x of pair f in its OWN union C_c,
compatibility gives
(u_received-a_f,v_received-b_f)=lambda*(A1(x),-A0(x)), lambda!=0.
The scalar agreement equation then forces the original finite label
gamma=A1(x)/A0(x). If A0(x)=0 there is no such finite-label defect.
This label depends only on x, not on the fibre or its represented pair.
The original assignment gives each label to one pair. Thus x is counted
as an inside defect at most ONCE across ALL pairs and fibres, even if
it lies in multiple unions. Total inside raw weight is at most their
union size. For h=0 all such labels coincide, so their total raw weight
is at most t instead.

Outside its own C_c, a fixed pair has at most n-|C_c| selected defects
across all its assigned labels: their defect sets are disjoint by the
same-pair owner theorem. Multiply this by the actual scalar LIST cap,
sum over fibres, and add the global inside bound. This proves WEIGHT.
It also improves the nonconstant single-pencil inside charge from
t*|C| to |C|; no older bound is invalidated.

## Two-Dimensional Nonconstant Planes In A Three-Dimensional Carrier

Assume dim T=2 and U has dimension3. Both A0*T and A1*T embed in U.
For h>0 both row entries are nonzero and A1/A0 is nonconstant.
Their intersection has dimension at least one. It cannot have dimension
two: equality would make multiplication by the nonconstant rational
function A1/A0 preserve a nonzero finite-dimensional polynomial space,
which would make it algebraic over F. Nonconstant elements of F(X)
are transcendental over F.

Choose nonzero p,q in T with A1*p=A0*q. Coprimality gives
p=A0*g and q=A1*g. They are independent, so T=g*span(A0,A1).
The three products g*A0^2,g*A0*A1,g*A1^2 are independent, again by
transcendence, and therefore span U. Their largest degree is deg g+2h,
which is <=K-a-1. This proves NORMAL over the original field, without
diagonalizing an operator or extending constants.
