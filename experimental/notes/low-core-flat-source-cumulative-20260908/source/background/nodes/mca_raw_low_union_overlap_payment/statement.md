# Small raw-low core unions force a single pair

Status: PROVED. Requirement: `mca_nonuniform_support_margin_resource`.

Use its exact selected-record setup, actual affine explanation carrier,
and minimizing pairs (a_gamma,b_gamma). Write C=C_s, m=K+d.
For 1<=T<=d let

    Gamma_T={gamma: raw_gamma<=T},
    U_T=union_(gamma in Gamma_T) H_gamma,

where H_gamma is the COMPLETE joint core of its minimizing pair.
If

    |U_T| <= 2(m-T)-K,                                    (O)

then all pairs represented in Gamma_T coincide (vacuously if empty),
and the TOTAL original selected slope count satisfies

    |Gamma| <= M + floor((C-M)/(T+1)),
    M=min(C,n-m+T).                                       (P)

No gluing-defect hypothesis is needed. In particular the theorem applies
when the union of all minimizing cores satisfies (O), but only the low
cores need to be small. High-margin records are included in (P).

The threshold in the pair-coincidence assertion cannot be enlarged by
one using the same hypotheses: the actual F_7 control in verify.py has
two distinct minimizing pairs at union size 2(m-T)-K+1. This does not
assert sharpness of the total slope cap or its numerical applications.
