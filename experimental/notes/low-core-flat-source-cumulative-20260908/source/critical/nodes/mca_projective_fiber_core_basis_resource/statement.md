# A populated projective fiber strengthens core-basis counting

Status: PROVED by the hand proof; external independent review remains due.

Use the completed-basis supplier's selected-slope setup: V has actual
dimension s>=2 and polynomial degree <K, m=K+d, d>=1, and each distinct
finite label has a size-m scalar support bad in the FULL degree-<K pair
code. The received pair and affine carrier h_*+V are fixed. Assume the
universal carrier core is empty (g=0); common zeros of V may still exist.
Canonical maximal-raw selection is NOT required.

Let a one-dimensional subspace of V* contain nonzero evaluations from
exactly a>=1 original coordinates. Necessarily a<=K-s+1. Set

    l=s-1, e=K-a-l>=0,
    P_e(X)=X*prod_(i=1)^(l-1)(X-e-i).

For M>=K, c=M-K+1, define

    b(M)=min{ P_e(M)*c,
              P_e(M-a)*(s*a+max(c-a,0)),
              s*c*P_e(K-1) if c<=a }.

Only include the third term when its condition holds. Every listed
factor is positive. A record of raw mismatch 1<=r<=d has at least

    tau(r)=(s+1)*r*b(m-r)

independent ordered incidence tuples. Put tau(r)=0 for r>d. With
P=prod_(i=1)^(s-1)(d+i), the old completed weight w_s(r;0), and z zero
incidence normals, the SAME resource satisfies

    sum_Gamma max(m*P*w_s(r;0), tau(r))
         <= (n-z)_falling_(s+1).                     (FIBER)

For 1<=T<=d, each raw<=T record has at least (s+1)*b(m-T) tuples,
by restricting its actual core to m-T coordinates. If w_s(r;0)>=L>0
for all raw>T, this yields the whole-source bound

    |Gamma|<=floor((n-z)_falling_(s+1)
              /min((s+1)*b(m-T), m*P*L)).            (SOURCE)

No free independence outside the fiber is assumed: e is the remaining
polynomial degree excess after dividing its annihilator by the fiber
locator. No fiber contraction changes the receiver, coordinates or slopes.
Finite row constants, original near and row/owner transport are consumer
obligations, not conclusions of this generic supplier.
