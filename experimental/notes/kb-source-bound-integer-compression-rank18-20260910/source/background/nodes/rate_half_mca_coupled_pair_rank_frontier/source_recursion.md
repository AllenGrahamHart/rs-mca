# Keep Every Weighted Anchor And Rank-Two Exit

Set A_t=d+J-t and retain original degrees<J. After a common anchors,
a function-field-rank-two pair space has determinant factor

    H_a(t,J)=(R-J+a+2)/(d-J+a+2-t).

The denominator is positive and R>d-t, so H_a increases with J. Its
rank-reduced child has one more common anchor. Write
P_v=max(C_(t,v),P_(t,v)) for the two weighted pencil caps. The valid
general enclosure bounds needed here are

    G_0(a)=R-d+t; G_1(a)=P_1;
    G_2(a)=max(P_2,H_a*G_0(a+1));
    G_3(a)=max(P_3,H_a*G_1(a+1)).

A rank-two space of affine dimension v uses H_a G_(v-2)(a+1);
a rank-one space uses its appropriate pencil cap. Every child type
is retained, including the zero-dimensional original same-pair weight.

Starting from enclosure rank q=17 or18 in scalar dimension11, apply
a=q-12 shared-carrier anchors. At stage i the pair/shared dimensions are
q-2i,11-i, and every stage satisfies s<r<=2s. Thus the weighted product is

    A_(q,t)=prod_(c=2)^(q-11) (R+c)/(d-t+c).

The endpoint dimensions are (7,6) after FIVE anchors for q17, or
(6,5) after SIX for q18. Divide only pair differences by H_a and delete
the anchors from the auxiliary domain. Then K'=J-a,N'=R+J-a and
N'-K'+1=R+1>2(K'-1); the Pluecker dichotomy applies.

In its SPARSE case, at most E_J=2(J-a)-2 good children have rank one,
and equality rigidity makes them constant-direction. Their cap is C_(t,s-1),
s=23-q. Every other good child is rank two and has cap

    L2=H_(a+1)*G_(s-3)(a+2).

Explicitly, q17 uses H_6*max(P_3,H_7*P_1); q18 uses
H_7*max(P_2,H_8*(R-d+t)). The determinant subscript is the number
of anchors ALREADY present. No hypothetical eight-factor rank18 shared
descent is used.

Let b be the number of bad evaluations on the divided carrier.
Then b<=K'-1. Weighted good-coordinate incidence gives the bound with
numerator (N'-b)*L2+E_J*max(0,C_(t,s-1)-L2) and denominator A_t-a-b.
It increases with b, so replacing b by K'-1 gives

    T_sparse=[S*L2+E_J*max(0,C_(t,s-1)-L2)]/(d+1-t).

For J-boxes, L2 and E_J increase, while the expression increases in
each on 0<=E_J<=S. Hence the upper J endpoint safely prices SPARSE.
Compression caps are J-uniform. Take the MAXIMUM of allowed sparse and
compression terminals, then multiply by A_(q,t). This bounds M_t for
the SAME source. Insert both cutoff bounds in(SOURCE), using W at the
lower J endpoint, floor once and add near once. This proves every
recorded interval, not just its sampled endpoints.
