# Adapt The Original Pencil Gates To The Actual Degree Interval

Fix a profile J0<=J<=J1, R=1048576,d=67472,S=R+1 and
W44=581590844909990298. The source is unchanged; only auxiliary LIST
instances are relaxed. A full primitive P43 pencil has complete union U,
complement e, and every off-pair has at least d-42-h agreements outside U.
This is the full row degree J+h-1 escape theorem, including gcd roots.

For any declared gate g and height h<=u, off-pair padding and degree
relaxation give the shared-dimension11 LIST parameters

    (r,w,Kmax,s)=(g-J1,d-42-u-J1,J1,11).               (OFF)

All corridor, degree and field-size conditions are certified. Each
off-pair's original deficit is at most(43/44)*981147; the on-pencil
complement e is NOT used for off-pair ownership.

## Nonconstant Height

The existing groupwise scalar-on-pencil proof has parameter dimension
at most10, and the analytic maximum of e*(S-e)^10 is
S^11*10^10/11^11. With the stronger original resource, use

    BASE=W44/44+R+21499+near
              +(43/44)*S^11*10^10/[11^11*(d-42)^10].

For h0<=h<=h1=u, the certificate selects a legal OFF trace L_off with

    ceil(BASE+(43/44)*981147*L_off)<=270000000000000000.

This is the prior exact groupwise argument with J1 in the auxiliary
degree relaxation, not an old theorem with silently changed parameters.
All preferred labels, higher raw records and near remain included.
The record's chosen gate need not be optimal.

## Constant Height Without A New Refund

The inherited source theorem already pays e<=567500. For the extension
567501<=e<=g, the ON scalar parameter carrier has dimension<=11.
Its length is R+J-e, degree J and agreement d+J-43. Padding the length
to R+J-567501 gives a uniform-in-J scalar cap L_on at

    (r,w,Kmax,s)=(R-567501,d-43,J1,11).                (ON)

There is at most one preferred original finite label, charged by1.
Every other on-pencil pair has at most e total raw weight outside U,
so its deficit contributes at most(43/44)*e. The chosen gate satisfies

    ceil(W44/44+near+1
            +(43/44)*(g*L_on+981147*L_off))
        <=270000000000000000,

where OFF has u=0. Using g instead of e and L_on from the largest
padded on-domain is conservative. The earlier e<=567500 theorem and
this extended range combine by maximum, not addition. No fractional
refund, receiver division or second original resource is used.

## Hereditary Use

At every height, the full P43 union contains the union of ANY P_t
pencil subfamily or anchor fibre, t=1,2. Thus absence of the paid
whole-source alternatives implies e_fibre>=g+1 for every such fibre.
This supplies the hypotheses used in the terminal calculation without
assuming its actual affine span fills the larger source pencil.
