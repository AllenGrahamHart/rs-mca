# Two Independent Joint Constraints At A Good Coordinate

Status: PROVED by the elementary incidence argument in proof.md;
independent external mathematical review remains due.

Let F be any field, D a domain of n distinct elements, K<=A<=n, and
(u,v) an arbitrary received pair on D. Let P=f_*+W be an affine F-space
of polynomial pairs, each component of degree<K, with actual affine
dimension r. Count distinct pairs in P jointly agreeing at at least A
coordinates; write that count M and Q=(n-K+1)/(A-K+1).

The credited affine specialization of joint LIST incidence gives

    M <= Q^r.                                           (AFF)

Suppose r>=2 and joint evaluation W -> F^2 has rank two outside a
set E of e<A domain coordinates. Then

    M <= ((n-e)/(A-e))*Q^(r-2).                         (TWO)

In particular, if dim_(F(X)) span_(F(X)) W=2 and A>2K-2, then

    M <= ((n-2K+2)/(A-2K+2))*Q^(r-2).                  (DET)

No characteristic restriction, field-size hypothesis, source-density
premise or global rational-pencil exclusion on child sections is used.
Each good joint section loses two dimensions ONCE. Subsequent incidence
steps use (AFF), which only promises one dimension per coordinate.

The rank-one-over-F(X) case is deliberately excluded from (DET): even an
affine pair family of F-dimension two can be a rational pencil. Likewise,
bad anchor coordinates cannot be silently omitted from the agreement
threshold. Both mistakes have actual small-field controls in verify.py.

These are polynomial-pair LIST counts, not MCA slope counts. A downstream
consumer must retain pair ownership, every original label and any source
normalization or near allowance.
