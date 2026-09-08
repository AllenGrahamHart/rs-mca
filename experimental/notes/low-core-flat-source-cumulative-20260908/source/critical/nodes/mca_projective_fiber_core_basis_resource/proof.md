# Proof by coupling the fiber and its annihilator

## 1. The actual polynomial quotient

Let F_0 be the given line in V* and A its set of a nonzero original
evaluation coordinates. Its annihilator W in V has dimension l=s-1.
Every W-polynomial vanishes on A. Divide by the actual locator G_A:

    W=G_A*W', dim W'=l, deg W'<K-a=l+e.

This proves a<=K-l and e>=0. The division is algebra on polynomials;
it does not puncture the scalar supports or descend the received pair.

Consider any M-point subset H of an actual joint core, with M>=K.
Its evaluation vectors are nonzero: at a carrier zero a joint agreement
would give v=0 and u=h_*, contradicting g=0. Put t=|H intersect A|.
The X=M-t outside evaluations restrict nontrivially to W, since their
nonzero V-evaluations are not in F_0. Dividing by G_A preserves their
linear ranks and has no zero denominator outside A.

A j-dimensional span of W'-evaluation vectors contains at most e+j
original outside coordinates for 1<=j<l. Indeed its annihilator has
dimension l-j, consists of degree-<(l+e) polynomials, and vanishes at
those coordinates. A polynomial space of that dimension cannot have
more than (l+e)-(l-j)=e+j common distinct roots. Greedy choice therefore
gives at least P_e(X) ordered W-evaluation bases on H outside A.
Since X>=M-a>=K-a=l+e, all required factors are positive.

## 2. Two disjoint kinds of full core bases

First take any such ordered l-tuple outside A and one of the t points
inside A. The outside tuple is a basis modulo F_0; adding the nonzero
inside vector gives a V*-basis. Inserting it at any of s positions gives

    s*t*P_e(M-t)

ordered bases with EXACTLY ONE coordinate in A. This insertion has no
overcount: the sole inside coordinate identifies its position.

For bases with NO coordinate in A, start with the same ordered outside
l-tuple and append one more outside point. Its span is a hyperplane in
V*: a nonzero degree-<K annihilator has at most K-1 roots. At least
max(M-t-K+1,0) outside points extend it. This gives a further

    P_e(M-t)*max(c-t,0), c=M-K+1,

ordered bases. These have zero inside points and are disjoint from the
previous bases, so these two counts DO add. Their sum is

    f(t)=P_e(M-t)*(s*t+max(c-t,0)).                  (1)

On each interval separated by t=c, this is a product of positive affine
functions of t. Its logarithm is concave. A positive log-concave function
on a closed interval is bounded below by the minimum of its endpoint
values. Thus the minimum on 0<=t<=a is at 0, a, or c when c<=a.
These are exactly the three terms defining b(M).

## 3. Complete incidence tuples and retain one global resource

For a record with raw r<=d its actual in-support pair core has size
m-r>=K. Apply the preceding count with M=m-r. The normals of each core
basis span the hyperplane annihilating (1,b), where b is a minimizing
second polynomial. Each of the r actual defect normals is outside it.
Insert a defect at any of s+1 positions. The unique defect recovers the
ordered core basis, giving tau(r) independent incidence tuples.

An independent tuple fixes the full affine parameter (gamma,lambda), so
different selected labels own disjoint tuples. The completed-basis
supplier also bounds this SAME record's independent tuples from below.
Its count may overlap tau(r); only their MAXIMUM may be summed.
All tuples avoid zero incidence normals. This proves (FIBER).

For raw<=T, instead choose an arbitrary fixed subset of m-T points from
the actual core and repeat the proof. The r actual defects remain outside
this subset. Each such record has at least (s+1)*r*b(m-T), hence at least
(s+1)*b(m-T), tuples. For raw>T use its proved completed-weight floor.
Assign the smaller of the two counts to every record and divide the one
tuple resource. This proves (SOURCE), with no monotonicity assumption
about b(m-r) and no deletion of labels, defects or receiver coordinates.
