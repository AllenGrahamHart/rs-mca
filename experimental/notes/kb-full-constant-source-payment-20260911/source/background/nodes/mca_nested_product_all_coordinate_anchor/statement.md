# All-Coordinate Anchors For Nested Product Carriers

Retain one original MCA assignment, its original pair degrees<J,
complete joint cores of size at least d+J-t in a domain of size R+J,
and ORIGINAL weights omega_t(f): the sum of original raw values over
that pair's assigned labels with raw<=t. Assume R>=d>t.

After a distinct anchor set of size a and full-gcd changes of coordinates,
let the divided pair-direction enclosure, in a fixed F-basis of F squared, be

    W=(V,0)+(0,B), B subset V,
    dim V=s, dim B=b=s-c, 0<=c<=s.

The basis change describes pairs only; original finite slope labels and
weights are NOT reparameterized. Suppose V has full gcd1 and primitive
degree D. Write N=R+D+1+v and A=d+D+1-t+v with v>=0.

For b>0, every remaining finite coordinate is one of:

1. B(x) nonzero: joint evaluation rank2; child dimensions (s-1,b-1),
   with unchanged codimension c.
2. B(x)=0: joint evaluation rank1; child dimensions (s-1,b),
   with codimension c-1. There are at most D-b+1 such coordinates.

Shared dimension drops by one in BOTH cases. Full normalization gives
D_child<=D-1. Put kappa=D-(s-1)>=0; then kappa_child<=kappa.
If c=0, B=V and the second case is absent.

If C and F are nonnegative upper bounds for ORIGINAL child weights in
the two cases, then

    Omega <= [N*C+(D-b+1)*max(F-C,0)]/A.          (ALL)

For c=0 use N*C/A. No regular-coordinate exclusion or dimension-two
drop at every anchor is assumed.

On a band kappa in[lo,hi], (ALL) is at most

    max(C,
        ((R+s+lo)*C+(lo+c)*max(F-C,0))/(d+s+lo-t),
        ((R+s+hi)*C+(hi+c)*max(F-C,0))/(d+s+hi-t)).

Lower-degree prefix maxima of the preceding shared stage provide C,F.
The finite consumer verifies all costs. At b=0 the enclosure is whole
constant of scalar dimension c; at s=b=0 it contains at most one pair.
No universal source budget is asserted by this generic inequality.
