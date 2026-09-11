# One Degree-Excess Variable Works At Every Anchor Stage

For an original shared dimension11 source, put M=J1 on a degree profile.
At shared dimension s, the primitive degree satisfies D<=M+s-12.
For a maximal constant hyperplane define

    zeta=E-(s-2), 0<=zeta<=M-10.

A non-root child has degree-excess <=zeta. A root child has full constant
carrier. On a band[lo,hi], the root-coordinate count is at most

    G=M-10-lo,

independently of s. The regular-anchor excluded count is at most D-s+4.
For ordinary child price C and root child price F, incidence gives

    Omega<=((R+s-3+v)*C+G*max(F-C,0))/(d+s-3-t+v).

The ratio decreases with v>=0. Define the remaining anchor factor

    A_s=product_(ell=1)^(s-3) (R+ell)/(d-t+ell), A_3=1.

All prices below are normalized by A_s. At s=4, a non-root child has
a constant plane of primitive degree <=hi+1, so price C_2(hi+1).
A root child is whole constant3 of degree <=hi+2, so price U3(hi+2).
Therefore a valid normalized band price is

    P_4=C_2(hi+1)+G/(R+1)*max(U3(hi+2)-C_2(hi+1),0).

For s>=5, let C be the maximum previously certified P_(s-1) over all
bands up to the current one. This covers every non-root child, including
degree-excess decreases and full-gcd changes.

A full constant child of shared dimension s-1 remains full constant
for s-5 more anchors, reaching shared dimension4 and pair dimension5.
Its final primitive degree is at most

    (s-2+hi)-(s-5)=hi+3.

It is codimension-one constant compression with scalar dimension4,
and costs C_4(hi+3). Its normalized price is

    F=C_4(hi+3)/A_4,

independently of s. Thus

    P_s=C+G/(R+s-3)*max(F-C,0), s=5,...,11.

The same upper bound applies for every actual D and unused degree.
The recursion is a proved weighted inequality, not an assumed
probabilistic transition or an independent reset of original raw weights.

At s=11, A_11*max_band P_11 bounds the original P_t raw weight in this
source class. Both cutoffs use the SAME P2 enclosure, even if the
actual P1 subset does not span it. The original higher-raw resource
and near term are then included once by the finite consumer.
