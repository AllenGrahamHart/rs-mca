# One Global Inside Charge And Two Large Fibre Masses

For height h, the required rational-compression theorem gives
S_h=1048577-h and x_c=|C_c|-J-h+1, with
x_c>=67473-h-t and sum x_c<=S_h. The fibres have scalar dimension<=2.
Their scalar LIST parameters, after eight shared anchors, are

    (r,w,Kmax,s)=(x+2h-1,67472+h-t,J-8-h,2).

For a profile J0..J1 and a height band h0..h1, relax to
S0=1048577-h0 and cover

    67473-h1-t <= x <= S0-g-1.

Every integer in this interval is covered, not just sample endpoints.
The padded scalar instance for a mass box[ell,u] is

    (r,w,Kmax,s)=(u+2h1-1,67472+h0-t,J1-8-h0,2).

Length padding, agreement lowering and uniform degree relaxation are
all in the SAME source field. Scalar counts are not directly slope counts.

Set T=349525. Since3*(T+1)>S0, at most two actual fibres have x>T.
For small boxes x<=T and large boxes x>=T+1, let L(u) be a certified
two-step LIST cap and choose

    alpha=max_small (S0-ell)*L(u)/ell,
    beta=max(0,max_large ((S0-ell)*L(u)-alpha*ell)).

The maxima exist over the displayed finite partitions and are nonnegative.
The ratio(S0-x)/x decreases on small boxes, while
(S0-x)*L(u)-alpha*x decreases on large boxes. Therefore the true
weight(S_h-x)*L_actual(x) is bounded by alpha*x on small masses
and alpha*x+beta on large ones.

Summing once over the ACTUAL fibres gives

    L_t = inside + alpha*S0 + 2*beta,
    inside=t if h=0, otherwise R+J1.

For nonconstant height the inside term comes from injectivity of the
original slope owner at each coordinate; it is NOT t per fibre times
a union size. The outside terms still retain all original raw values.
For constant height the common preferred finite label costs t once.

The verifier regenerates the chosen finite bounds. The independent audit
checks each proposed LIST trace against the proved scalar inequalities,
reconstructs these envelopes, and verifies the original available-weight
test. It imports no new primary-proof code. Both retain rational weights
until the final source-template floor; displayed integer terminal floors
are not substituted prematurely.

The thirteen profiles are data shards, not thirteen new conjectural nodes.
The available-weight test has maximum272127061148955779. It makes this
terminal class affordable in the existing template; it does not provide
bounds for unclassified or whole-pencil terminal children.
