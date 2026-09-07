# Polynomial relations on low complete cores

## Degree-free extension

The [rational-pencil theorem](rational_line_cores.md) replaces the
bounded-row premise below by collinearity of the represented LOW pairs
over F(X). Primitive height may be any value below K; the exact pair
identity and covered-core compatibility follow directly from that premise.
For a partition into pencil groups, the original resource is charged once:
|Gamma|<=C_s/(T+1)+sum_i G_i, with the printed groupwise costs and
all preferred directions retained. The finite consumer pays thirteen
nonconstant groups, or one constant plus one nonconstant group. No such
cover is asserted for arbitrary families.

The [actual high-height control](rational_line_controls.md) has ZERO
bounded E-row space but lies on one rational pencil, so this is not a
mere renaming of the old relation hypothesis. External review remains due.

## Earlier bounded-row formulation

Status: PROVED. Use the exact support-margin setup, with carrier
h_*+C', actual dim C'=s>=1, m=K+d, and minimizing pairs
(a_gamma,b_gamma)=(h_gamma-gamma*b_gamma,b_gamma).

Choose 1<=T<=d. Let U be the union of COMPLETE cores of raw<=T
records, and assume |U|>=m. Put A=m-T, ell=d-T, e=n-|U|.
On U let u_U,v_U be the canonical received interpolants and P_U its
locator. Suppose a nonzero row R=(R_0,R_1), deg R_i<=ell, satisfies

    deg Q_R<A,
    Q_R=rem_(P_U)(R_0 u_U+R_1 v_U).

Write G=gcd(R_0,R_1), R_i=G A_i with gcd(A_0,A_1)=1, and
h=max(deg A_0,deg A_1).

If h=0, the received-pair gluing defect on U is <=1.
If h>=1, let V_t>=1 bound ordinary scalar lists of affine polynomial
dimension at most s-1 on (|U|,K,m-t), for every 1<=t<=T. Then

    |Gamma| <= n + C_s/(T+1)
                  + e sum_(t=1)^T V_t/(t(t+1)).             (PR)

The count includes EVERY original selected label, including high
records and exceptional rational-direction slopes. It needs no constant
gluing kernel when h>=1. The same C' for both polynomial components is
essential to the dimension drop. The finite consumer discharges the
ordinary-list inputs and removes the |U|>=m guard by the existing overlap
payment. No relation-free source bound is claimed.
