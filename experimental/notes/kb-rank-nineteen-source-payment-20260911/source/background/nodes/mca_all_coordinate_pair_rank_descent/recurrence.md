# Degree Bands And Two Source Tables

For original shared dimension11, after a=11-s actual anchors,
D<=J-a-1 implies 0<=kappa<=J-11. Full shared gcds may lower kappa.

Build tables U[s,c,i] for unrestricted enclosures and G[s,c,i] for
full-generic enclosures, on common degree-excess bands i.
Use 0<=c<=min(3,s), shared stages s0..11, and terminal states s=c.
Each table has42 states;38 are recurrences.

Before using any child, maximize its preceding-stage prices over every
band j<=i. This retains all smaller degrees after full gcd normalization.
For U, use child codimensions c,c-1,c-2 and the two nested increments
in (U). For G, use G-children c,c-1 and U-child c when c>=2.
Every branch reduces shared dimension even if pair rank stays unchanged.

On kappa in[lo,hi], both inequalities have the form

    [(R+s+kappa+v)*C + linear_nonnegative_charge(kappa)]
      /(d+s+kappa-t+v).

For fixed kappa its supremum over v>=0 is at most the value at v0
or its limit C. At v0 the ratio is monotone or constant in kappa,
so check both band endpoints. No sampling of degrees or unused v is needed.

The finite consumer supplies complete terminal prices.
In its G[3,3] state, unchanged codimension3 means all preceding eight
G-steps were rank-two regular anchors; a rank-one step could not return
to codimension3. This is the precise history needed by the inherited
small-normalization terminal allowance. No such allowance is used in U.

The final G[11,3] prices bound original raw1/2 weights, not pair counts.
Their original source identity includes higher raw and near once.
