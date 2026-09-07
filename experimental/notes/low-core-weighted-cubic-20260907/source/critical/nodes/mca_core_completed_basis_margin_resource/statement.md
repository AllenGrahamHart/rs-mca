# Completing bases from a minimizing pair core

Status: PROVED. Use the exact selected-slope setup of
`mca_nonuniform_support_margin_resource`: n distinct points, degree <K,
m=K+d, d>=1, actual explanation dimension 1<=s<=K, full-code
same-support pair noncontainment. Let r_gamma be the UNTRUNCATED
minimum mismatch to a second polynomial b in C'. Let z count zero
incidence normals and g the universally satisfied zero normals.

Write P=product_(i=1)^(s-1)(d+i). Define

    b_s(r;g)=(s+1)*r*(m-r-g)/(m-g)
                     *product_(i=1)^(s-1)(d-r+i)/(d+i),  1<=r<=d,
    b_s(r;g)=0,                                          r>d,
    w_s(r;g)=max(min(d+1,r), b_s(r;g)).

Then the strengthened resource is

    sum_gamma w_s(r_gamma;g)
       <=(n-z)_falling_(s+1)/((m-g)*P).                 (W)

If d>=s*(s+1), every weight is at least

    alpha_s=(s+1)*d/(d+s).

Consequently the UNCONDITIONAL selected-slope count is at most

    floor((d+s)/((s+1)*d) * max(
      n_falling_(s+1)/(m*P),
      (n-K+s)_falling_(s+1)/product_(i=1)^s(d+i))).       (C)

No prime-subfield, low-union, relation, cyclic-row or minimum-margin
hypothesis is needed for (C). It does not by itself assert prize-row
safety. The recordwise alpha lower bound is attained by a one-defect
support in the full s-dimensional degree-<s code.
