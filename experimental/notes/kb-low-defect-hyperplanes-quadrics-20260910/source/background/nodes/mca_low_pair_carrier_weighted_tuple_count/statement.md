# Weighted Low-Label Count In An Affine Pair Carrier

Status: PROVED. External independent mathematical review remains due.

Let D consist of n distinct points of any field F. Fix integers
1<=s<=K,1<=T<=d and m=K+d<=n. Let U be an s-dimensional
subspace of F[X]_<K and fix a0,b0 in F[X]_<K; neither offset is
required to lie in U. Fix received functions u,v on D.

For each of a set of DISTINCT finite labels gamma, choose a pair
a_gamma in a0+U,b_gamma in b0+U and a support S_gamma of size m,
such that on S_gamma

    u+gamma*v=a_gamma+gamma*b_gamma.

Let tau_gamma count the mismatches v!=b_gamma on that support and
assume1<=tau_gamma<=T. Minimization, complete supports, an empty
original core and full-code-badness of an auxiliary source are NOT required.

Define

    Z={x in D: U(x)=0, u(x)=a0(x), v(x)=b0(x)}, z=|Z|,
    K'=K-z, n'=n-z, L=m-z-T=K'+d-T,
    P=product_(j=1)^(s-1)(d-T+j).

Then z<=K-s, and the ORIGINAL labels obey

    sum_gamma tau_gamma
      <= floor((n')_falling_(s+1) / ((s+1)*L*P)).    (LOW)

The product is1 if s=1. No sum over translated children is used.
The support S_gamma need not contain all of Z. All original defects
survive the auxiliary translation/cancellation. The theorem is a weighted
label count, not a census of pairs and not a full-source or Prize bound.
