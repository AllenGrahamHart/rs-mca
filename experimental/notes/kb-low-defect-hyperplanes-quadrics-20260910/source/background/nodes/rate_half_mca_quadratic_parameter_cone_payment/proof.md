# Pay Both Contained And Noncontained Lines In One Original Ledger

Put R=1048576,d=67472,E=21499,near=134944. The required original
low-raw filtration proves, on the SAME selected rank-twelve source,

    sum min(raw,4)<=W0=624373932788019251,
    sum min(raw,4)<=W1=522680876725222604 if J>=14000.

For the second case sum min(raw,3)<=sum min(raw,4)<=W1 is also valid.
All high records and the original near interface remain unchanged.
We never subtract two separately upper-bounded resources.

## 1. Count The Actual Low Pairs Before Taking Cone Sections

Let P_T consist of all represented raw<=T minimizing pairs, T=2 or3.
Each has at least m-T complete joint agreements. Enclose P_T in one
affine translate of V x V and apply the required shared-carrier anchor
at pair/shared ranks22/11,20/10,...,2/1. Every rank guard is strict.
The terminal child is a point, so

    |P_T|<=floor product_(j=1)^11 (R+j)/(d-T+j)=P_T^*,
    P_3^*=12765991804643, P_2^*=12763910835039.       (PAIR)

No coordinate, degree or original label is changed. Earlier anchor common
zeros remain included in the proved bad-coordinate bounds.

For a fixed cone(CONE), consider the graph line of one chosen pair f=(a,b).
With a'=a-a0,b'=b-b0, its restriction is the polynomial

    Q(z,a+z*b)=ell1(a')+z*(ell1(b')-ell2(a'))-z^2*ell2(b').

If it is nonzero, at most two finite labels of this pair can have their
actual parameter point inside the cone. Since each original label owns
one chosen pair, at most2*P_T^* inside labels belong to noncontained
lines. This counts all exceptions; no exhaustive contained-line premise
or unpriced line census is assumed.

## 2. Contained Lines Have One Common Two-Label Tuple Resource

If the restriction is identically zero, its three coefficients give

    ell1(a')=0, ell2(a')=ell1(b'), ell2(b')=0.

The generic cone supplier therefore applies to their actual low owners.
Its nonzero joint-evaluation hypothesis follows from the ORIGINAL empty
universal core: at V(x)=0 every a in h_*+V equals h_*(x), every b in
V is zero, and joint agreement would make x a forbidden universal point.

At most J-9 of these labels have a zero evaluation of their moving
ten-dimensional carrier on their selected joint core. The supplier
prices them by LABELS. On all other contained-line labels it proves

    sum raw <= floor F_T(J),
    F_T(J)=2*(R+J)_falling_11 /
      (11*(d+J-T)*product_(j=1)^9(d-T+j)).            (MASS)

The original receiver is translated once by a0,b0. Its coordinates are
not cancelled separately for each label. All the moving-carrier counts
share the fixed quadratic incidence system; a tuple has at most two
owners, not the fixed-hyperplane supplier's one owner.

The quotient decreases in J throughout the required ranges, since

    F_T(J+1)/F_T(J)
      =(R+J+1)/(R+J-10)*(d+J-T)/(d+J+1-T)<=1

is equivalent to11*(d+J-T)<=R+J-10. The linear difference has
minimum91417 for T=3, or91406 for T=2, at J=E. Thus use the
simultaneous positive lower endpoint for(MASS), and the conservative
exception endpoint J-9<=21490:

    T   J_min    M_T=floor F_T(J_min)    E_T=21490+2*P_T^*
    3   9965     151439604546110669      25531983630776
    2   14000    150069040313791513      25527821691568.

E_T prices both kinds of inside-cone exceptions. These independent upper
endpoints are conservative; no attainability or optimization is asserted.

## 3. Exact Original-Slope Composition

Let e count the actual raw<=T labels outside the one fixed cone. For
retained inside labels T+1-raw<=T*raw; each excepted or outside low
label costs at most T. On the SAME original full record family,

    (T+1)*|Gamma|=sum min(raw,T+1)+sum_(raw<=T)(T+1-raw)
                   <=W_T+T*(M_T+E_T+e).

For T=3 take W_T=W0, and for T=2 take W_T=W1. The two integral
right-side constants at e=0 are1078769342377243586 and
822870012996188766. Flooring and adding near ONCE proves(Q3),(Q2)
and their exception-tolerant versions.

If |Z_bad|>B*, then |Gamma|>=B*-near+1. Rearrangement gives the
printed outside-label lower bounds, uniformly for EACH chosen cone and
EVERY valid original assignment. At one fewer outside label the bound
is exactly B*; at the printed threshold it is B*+1. This is adjacency
of the sufficient envelope, not a realized unsafe source or true optimum.

## 4. Why This Goes Beyond Affine Hyperplanes

After choosing dual v1,v2 and U=ker ell1 intersect ker ell2, the
compatible pair directions are(alpha+t*v2,beta+t*v1),alpha,beta in U.
Their ambient dimension is2*9+1=19 and their component-image SUM
is the full11-dimensional V. Their parameter cone has coordinates
(gamma,c in U,t,w=gamma*t), whose affine span has dimension12.
Thus neither proper shared carrier nor proper affine parameter graph is
being silently assumed. Noncontained pair exceptions can increase the
actual pair affine hull further and remain explicitly paid.

In particular, on J>=14000 an over-budget P_2 cannot satisfy the three
displayed coefficient identities for any independent ell1,ell2 and
affine offsets. More general full low graphs, the lower-J quadratic
G_2 case, original error ranks>=13 and both Prize problems remain open.
