# All-Coordinate Pair-Rank Descent

Retain one original finite-label MCA assignment and weights
omega_t(f)=sum of original raw values over its assigned raw<=t labels.
Use a primitive polynomial carrier V of dimension s and degree D,
a pair-direction enclosure W subset V squared of dimension r=2s-c,
and 0<=c<s. The actual family need not span its enclosure.

After original anchors and full-gcd coordinate changes, write

    N=R+D+1+v, A=d+D+1-t+v, v>=0, R>=d>t,
    kappa=D-(s-1)>=0.

Every remaining finite coordinate has joint evaluation rank q in{0,1,2}.
Its nonempty agreement section has pair dimension r-q, shared enclosure
dimension s-1, and new codimension c+q-2. After full shared gcd division,
primitive degree drops by at least one and degree excess cannot increase.

The rank-at-most-one set has size at most kappa+c. The rank-zero set
has size at most kappa+floor(c/2). If C2,C1,C0 bound original child weights
for the three respective ranks, then

    A*Omega <= N*C2
        +(kappa+c)*max(C1-C2,0)
        +(kappa+floor(c/2))*max(C0-max(C2,C1),0).        (U)

Absent child types have no charge: rank0 is impossible when c<2, and
rank1 is impossible when c0.

If pi_z(a,b)=a+z*b maps W onto V over F(z), there are no rank-zero
coordinates. Outside a set of size at most kappa+c, rank-two children
retain full generic projection. Inside it, a rank-one child also retains
full generic projection, while a rank-two child may lose that property.
Such loss is impossible for c0 or c1.

Consequently, if C bounds regular rank-two children, F regular rank-one
children, and T unrestricted rank-two children, then

    A*Omega <= N*C+(kappa+c)*max(0,F-C,T-C).            (G)

For c0 omit both exceptional types; for c1 omit T.
These are exact weighted upper bounds, not claims that every anchor is
regular or that all possible terminal prices fit a source budget.
