# Proof

Every low pair has at least A=m-T common agreements on U and lies
in (h_*,0)+C' x C': a_gamma=h_gamma-gamma*b_gamma is in h_*+C'.
The common scalar carrier, not merely two equal dimensions, is important.

## 1. Exact relation and the covered gcd roots

Apply the required two-component relation theorem on the ACTUAL domain U.
For every low pair (a,b), root counting gives the polynomial identity

    R_0 a+R_1 b=Q_R.

The difference has degree <A and at least A roots. Fix one low pair
(a_*,b_*), which exists because |U|>=m. Then G divides Q_R. Put
Q=Q_R/G. Every low pair satisfies

    A_0 a+A_1 b=Q.                                        (1)

Unlike an arbitrary joint-list domain, U is COVERED by the complete
agreement cores of these pairs. For every x in U some low pair equals
(u(x),v(x)); equation (1) therefore implies

    A_0(x)u(x)+A_1(x)v(x)=Q(x)                            (2)

on ALL of U, including roots of G. This proves there are no source-
incompatible gcd roots on U. It does not erase the gcd-root guard from
the general LIST supplier on unrelated domains.

If h=0, the A_i are constants, not both zero, and Q=A_0 a_*+A_1 b_*
has degree <K. Equation (2) is a constant projective polynomial kernel,
so the received-pair defect is <=1.

## 2. A nonconstant primitive row drops the scalar carrier dimension

Assume h>=1. Coprimality implies both A_i are nonzero and their ratio
is nonconstant. All bounded-degree polynomial solutions of (1) have

    a=a_*+A_1 H, b=b_*-A_0 H, deg H<K-h.

The relevant H lie in the F-linear space

    V={H: deg H<K-h, A_0 H in C', A_1 H in C'}.

When K-h<=0 this is the zero space. Otherwise multiplication by A_0
is injective, so dim V<=s. If equality held, A_0 V=A_1 V=C'.
Multiplication by A_1/A_0 would
preserve the nonzero finite-dimensional polynomial space C'. For any
nonzero f in it, all f(A_1/A_0)^j would be polynomials in C'. If A_0
has positive degree, coprimality forces A_0^j to divide f for every j,
impossible. If A_0 is constant, A_1 has positive degree and these
polynomials have unbounded degree, also impossible. This proves the drop.

No claim of this form is valid for two unrelated s-dimensional component
spaces: C_a=span{X}, C_b=span{1}, A_0=1,A_1=X already permits a
one-dimensional H space when s=1. Here BOTH differences belong to C'.

Since A_0,A_1 have no common evaluation root, (2) defines a unique scalar
receiver w on U by

    (u-a_*,v-b_*)=(A_1,-A_0)w.

The complete core of a represented H is exactly {w=H} on U. Its
entire core lies in U by definition of the low-core union. The relevant
H have degree <K, so V_t bounds their cumulative scalar list at
agreement m-t even though we do not use the available degree gain h.

## 3. Exceptional slopes must be charged

Let E consist of finite labels gamma for which
A_1(x)-gamma A_0(x)=0 at some x in U. Coprimality implies that such
a point has A_0(x)!=0 and supplies only gamma=A_1(x)/A_0(x).
Hence |E|<=|U|<=n. Remove all selected labels in E at this cost.

For any remaining low label, its scalar agreement on U is equivalent
to joint agreement: the scalar error equals

    (A_1-gamma A_0)(w-H),

whose first factor never vanishes on U. Let a_H be the core size and
t_H=max(1,m-a_H). Each selected support representing H therefore needs
at least t_H points outside U. The max with one follows from pair
noncontainment even when a_H>=m. Also raw_gamma>=t_H.

For a fixed H, an outside point can occur in at most one of its labels:
two distinct solutions of (u-a)+gamma(v-b)=0 would put that point in
the COMPLETE pair core, contradicting its being outside U. Thus at most
e/t_H labels represent H. This argument needs no polynomial relation
on outside coordinates.

## 4. Weighted count including the high records

Let N be the number of retained labels after removing E. The original
global margin resource still bounds their total theta. Since high
records have theta>=T+1 and low ones have theta=raw,

    N-C_s/(T+1) <= sum_retained_low (1-raw/(T+1))
                <= e sum_H (1/t_H-1/(T+1)).

If M_t counts represented H with t_H<=t, summation by parts gives

    sum_H (1/t_H-1/(T+1))=sum_(t=1)^T M_t/(t(t+1)).

The previous scalar parameterization gives M_t<=V_t. Restore at most
n removed labels to obtain (PR). Empty retained low families are
already covered by N<=C_s/(T+1). No high-label count is added a
second time, and no projective label is silently identified with a
scalar codeword. This proves the theorem.
