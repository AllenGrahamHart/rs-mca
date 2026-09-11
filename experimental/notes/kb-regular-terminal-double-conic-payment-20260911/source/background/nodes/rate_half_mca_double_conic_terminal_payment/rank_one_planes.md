# Rank-One Planes Have At Most Fifteen Actual Pairs

Use kappa=2nu+1 and the proved primitive carrier parameters
N_v=R+2nu+1+v, A_v=d+2nu+1-t+v, with nu>=1 and v>=0.
Only rank-one evaluation fibres are removed here, NOT all eigen roots.
The conic kernel isomorphism gives unique directions at every other point,
including possible eigenvector collision directions.

Fix a rational rank-one evaluation point p0 and ANY actual affine plane
of pairs with parameter direction H0=ker ell0. Write its pair count as m.
At the p0 fibre, at most m pairs agree per coordinate. At a possible second
rank-one point p1, an agreeing section has direction H0 intersection H1,
an F-eigenvector line, and contains at most7 actual pairs.

At nonbase points the restriction to H0 is injective except possibly at
ONE point: the geometric supplier proves that P(H0) meets the kernel conic
in d(p0) and at most one other point. At that additional fibre an agreeing
section is a line with at most7 pairs. Everywhere else at most1 pair agrees.
Each evaluation fibre has at most nu actual coordinates. Padding absent
exceptional fibres and using the complete core bound therefore gives

    m*A_v <= N_v+nu*(m-1)+2*nu*(7-1),
    m <= (R+1+13nu+v)/(d+1-t+nu+v) < 16.

The last strict inequality follows from
16*(d+1-t)-(R+1)+3nu+15v>0 for t=1,2, nu>=1 and v>=0.
Thus m<=15. Empty planes require no division. Receivers may vary within
a fibre: at each coordinate its agreeing set is some affine H0-plane,
and the same hereditary count applies to that set using its full cores.

There are at most2 rank-one evaluation points, each with at most nu
coordinates. Their TOTAL actual incidence is at most B=30nu. No assumed
three-eigenvalue spectrum or paid whole-constant terminal is used.
