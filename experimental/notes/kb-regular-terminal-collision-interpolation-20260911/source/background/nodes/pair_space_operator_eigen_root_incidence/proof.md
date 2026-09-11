# Spectral Types Determine Which Actual Section Can Occur

At a coordinate with nonzero evaluation ell, the joint evaluation rows
are ell and ell*T. An agreeing family is an affine plane if the rows
have rank one, and an affine line if they have rank two. In the latter
case, if x is a root of an eigenpolynomial v_lambda, the one-dimensional
kernel is exactly F*v_lambda. Thus the section contains at most q1
represented points. A rank-one section contains at most q2.

If e=0 there is nothing to count. If e=1, each of at most D roots
has a section of dimension<=2, giving D*q2.

If e=2, the characteristic polynomial is (z-lambda)^2*(z-mu).
The lambda eigenspace is one-dimensional, so v_lambda=(T-lambda*I)w
for some w in the lambda-primary two-space. Every left eigenvector
annihilates v_lambda: at lambda this follows from the displayed image;
at mu it follows from distinct eigenvalues. Consequently EVERY rank-one
coordinate is a root of v_lambda. Charge all its at most D roots by q2.
Other roots of v_mu have joint rank two and cost q1, giving D*(q2+q1).
It is false that every rank-one coordinate here consumes two eigen-root
budgets; the simple-eigenvalue left direction can consume only one.

If e=3, the three eigenvectors form a basis. A rank-one nonzero
evaluation annihilates exactly two of them; a rank-two eigen-root
evaluation annihilates exactly one. Let b1,b2 count these respective
one-root and two-root types. There are no three-root coordinates,
by the common-zero exclusion. Hence b1+2*b2<=3*D, and

    q1*b1+q2*b2 <= (q2/2)*(b1+2*b2) <=3*D*q2/2.

This proves CAPACITY. It uses F-eigenvectors only; no scalar extension
or diagonalization of the repeated or nonsplit cases was assumed.

## Count A Fixed Number Of Actual Pairs

Take exactly M distinct represented pairs if that many exist. On the
remaining domain, let c_x be their core-incidence multiplicities and
S=sum c_x. CAPACITY gives S>=S0. Padding this domain back to n positions
with zero multiplicity preserves all counts. If two remaining cores
intersect in at most H coordinates, Cauchy--Schwarz gives

    S^2/n <= sum c_x^2 <= S+M*(M-1)*H.

The function S^2-n*S is increasing for S>=n/2. Since S>=S0>=n,
ENERGY contradicts this inequality. This works for an arbitrary
M-element subset, so no monotonicity in an unknown total pair count
or equality of original owner weights is required.

Without a uniform intersection cap, the exact second moment is S+2*I2.
The same monotonicity gives2*I2>=S0^2/n-S0. Under ENERGY this is strictly
greater than M*(M-1)*H, proving the actual-subset pair-mass consequence.

Outside E, an eigenvector difference has no zeros. A non-eigenvector
difference y gives independent polynomials y,T(y). If they had D
distinct common roots they would both be scalar multiples of the
degree-D locator, a contradiction. Their common-root count is <=D-1.
Combine this natural bound with the required projective-fibre bound.
