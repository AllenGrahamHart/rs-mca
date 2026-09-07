# Proof

Use the supplier's incidence normals v_x=(v(x),-c_1(x),...,-c_s(x))
for one fixed basis of C'. Every selected support has full incident rank
s+1, and distinct finite selected slopes own disjoint independent ordered
(s+1)-tuples. The original proof supplies at least

    (m-g)*P*min(d+1,r)

such tuples per record. We prove an additional lower bound on the SAME
record's tuples. These lower bounds are combined by MAXIMUM, not addition.

## 1. Count tuples with exactly one noncore coordinate

Fix a minimizing b in C' with raw mismatch r<=d. On its selected
scalar support S, the pair f=(h_gamma-gamma*b,b) matches the receiver
exactly where v=b. Thus its in-support pair core H has size m-r.
The H-normals lie in the hyperplane annihilated by (1,b_1,...,b_s),
where b=sum b_i c_i. Every one of the r other normals lies OUTSIDE
that hyperplane.

The H-normals span this s-dimensional hyperplane: m-r>=K, so a
polynomial in C' vanishing on H must be zero. Their common zero normals
number at most g. Hence the first independent H-normal has at least
m-r-g choices. After j independent H-normals, 1<=j<s, evaluation on
C' and the usual root-space dimension bound put at most K-s+j
coordinates in their span. There are at least

    m-r-(K-s+j)=d-r+s-j

new H-normal choices. There are therefore at least

    (m-r-g)*product_(i=1)^(s-1)(d-r+i)

ordered bases of the H-hyperplane. Choose any of the r outside
coordinates and insert it in ANY of the s+1 tuple positions. Every
result is independent. It has exactly one coordinate outside H, so
both its outside coordinate and its insertion position are unique.
No multiplicity is hidden in this factor s+1. This gives the second
recordwise lower bound (m-g)*P*b_s(r;g).

The supplier's global independent-tuple budget and the maximum of
the two lower bounds prove (W). No assertion about points outside S
or about transporting old margins through a different support is needed.

## 2. A uniform weight floor

The supplier gives g<=K-s, hence M=m-g>=d+s. For real 1<=r<=s,
the positive part of b_s(r;g) is proportional to

    r*(M-r)*product_(i=1)^(s-1)(d+i-r).

Its logarithmic derivative is at least

    1/r - s/(d+1-r) >0

when d>=s(s+1). Thus every integer 1<=r<=s has

    b_s(r;g)>=b_s(1;g)
      =(s+1)*(M-1)/M * d/(d+s-1)
      >=(s+1)*d/(d+s)=alpha_s.

For r>=s+1, min(d+1,r)>=s+1>alpha_s. This includes r>d,
where the new core count is not used. All records therefore have weight
at least alpha_s, without making any raw-margin assumption.

Finally maximize the right side of (W) over 0<=g<=z<=K-s exactly
as in the supplier. At fixed z it increases in g. At g=z its successive
ratios change from decreasing to increasing at most once, so z=0 and
z=K-s give the two displayed endpoints. Divide by alpha_s and floor
only at the end. This proves (C).

## 3. Sharpness of the recordwise improvement

Take K=s and C'=F[X]_(<s). Put (u,v)=(0,0) on m-1 distinct
points and (-gamma,1) at one further point. The zero explanation has
one-defect full-code-bad support of size m: a degree-<s second
polynomial vanishing on m-1>=s points cannot also equal one.
There are exactly (s+1)*(m-1)_falling_s independent ordered normal
tuples, since each must use the sole outside point. Their ratio to
the supplier's (m)*P is precisely alpha_s. This is recordwise
sharpness, not attainment of the global selected-family count.
