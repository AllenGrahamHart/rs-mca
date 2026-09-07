# Ordinary LIST: padding and dimension descent

Status: PROVED. No imported mathematical requirements.

Fix integers 1<=w<=r and K_max>=1 over one field with
q>=r+K_max. All domains below are arbitrary distinct field points.
Let U>=1 bound ordinary codeword lists in every affine polynomial space
of dimension at most s-1, on every row

    (N,K,A)=(r+K,K,w+K), 1<=K<=K_max.

For any 1<=L<=K_max with

    D_L=(w+L)^2-(r+L)(L-1)>0,
    J_L=floor((r+L)(w+1)/D_L),

the corresponding dimension-at-most-s lists are bounded by

    J_L                                      if L=K_max,
    max(J_L,floor((r+L+1)U/(w+L+1)))          otherwise.       (P)

For s<=K_max the additional uniform bound is

    floor((r+s)U/(w+s)).                                    (S)

Start at U_0=1 and take any minimum of these proved upper bounds.
Common evaluation zeros cost NO list word. This is ordinary LIST,
not an unconditional MCA conversion. The accompanying compiler returns
the chosen certificates; correctness does not depend on optimal search.

The [shared-carrier extension](shared_carrier_joint_lists.md) proves
the identical bounds for every joint-list arity when each component
belongs to an affine translate of the SAME dimension-at-most-s
polynomial space. The dimension is that shared space, not the tuple
list's possibly larger affine dimension. An MCA conversion needs a
separate proved count; this extension alone does not provide one.
