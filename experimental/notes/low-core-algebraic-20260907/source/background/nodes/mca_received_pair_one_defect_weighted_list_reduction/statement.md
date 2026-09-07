# Gluing defect at most one: a coupled ordinary-list bound

Status: PROVED. Use the margin supplier's exact selected-record setup,
with n=K+R, m=K+d, actual carrier h_*+C' of dimension s>=1,
and one raw-margin-minimizing b_gamma in C' per distinct selected slope.
Let H_gamma be the COMPLETE core of (h_gamma-gamma b_gamma,b_gamma).
Choose 1<=T<=d. Let U be a subset of the original domain containing
the complete core of EVERY record with raw_gamma<=T, and put e=n-|U|.
Assume |U|>=m and n-m>=s. In particular U may be the union U_T of
only these low cores, or the original union of all complete cores.

Suppose a nonzero projective combination of the two received components
is a degree-<K polynomial on U. When U is the low-core union, this is
equivalently received-pair gluing defect c_T<=1 for that core family.
For every 1<=t<=T let V_t>=1 bound every ordinary
affine dimension-at-most-(s-1) list on

    (R-e+j,j,d-t+j), 1<=j<=K.

Put

    P=prod_(i=1)^(s-1)(d+i),
    F(g)=(n-g)_falling_(s+1)/((m-g)P),
    C(g)=max(F(g),F(K-s)),
    W(g)=C(g)/(T+1)
         + e sum_(t=1)^T [ V_t (n-e-g)/(m-t-g) / (t(t+1)) ].

Then the original number of distinct selected slopes obeys

    |Gamma| <= 1 + max(W(0),W(K-s)).                       (GL1)

These are upper bounds in the original slope units. They do not identify
ordinary list words with slopes: repeated words are charged to outside
coordinates. No all-projective scalar ceiling, ambient MDS hypothesis,
smoothness, or near-rational premise is assumed.
High-margin cores do not have to lie in U or glue there. Their labels
remain included in the GLOBAL margin resource and the final count.
