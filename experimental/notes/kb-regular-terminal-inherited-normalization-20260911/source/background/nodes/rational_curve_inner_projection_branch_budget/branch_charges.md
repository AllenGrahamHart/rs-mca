# Each Bad Centre Creates Many Branches After A Generic Projection

First take ANY finite set of inner centres P_i with mu_i>=2. Choose a
general smooth q in C such that its inner projection is birational, the
fibres of all projections from P_i through q are unramified, and the lines
qP_i are distinct. Such q exists: each map has degree at most d<p and is
separable; finitely many prescribed centres and joining lines are avoided.

The line qP_i contains mu_i normalization points away from P_i, including q.
The b_i branches above P_i are additional normalization points. After
projection from q, the remaining b_i+mu_i-1 distinct normalization points
all map to one image point, different for different i.

Continue taking general smooth inner projections until the ambient space
is P2. Each is birational, removes one degree, and can preserve those
distinct image points without using them as centres. The final plane curve
has degree d-(r-2). The chosen points have at least b_i+mu_i-1 branches.
The proved planar normalization inequality delta>=binom(branches,2) gives

    sum_i binom(b_i+mu_i-1,2) <= binom(d-r+1,2)=G.

This holds for every finite set. Every charge is at least1, proving finiteness
and the total budget. Geometric auxiliary centres are only a counting proof;
they are not asserted to be legal original-domain anchors.

## Branch-Weighted Conversion

For mu>=h>=2 and integer b>=1,

    binom(b+mu-1,2) >= binom(h,2),
    binom(b+h-1,2)-(2h-3)*b
       = (b-(h-1))*(b-(h-2))/2 >=0.

The two roots are adjacent integers, so the last product is nonnegative.
This proves the centre and branch-count bounds separately. Every original
polynomial fibre has at most nu times its branch count by finite flat
normalization; multiplying the BRANCH sum by nu gives the coordinate bound.

For the refinement, the fixed divisor at P has degree m>=b. Inner-image
nondegeneracy gives degree at least r-1, hence d=m+mu*d_child implies
b<=d-h*(r-1)=B. If B<1 no such point exists. Over integers1<=b<=B,
binom(b+h-1,2)/b is minimized at b0=min(B,max(1,h-2)); this follows by
successive differences or from its terms b/2+(2h-3)/2+(h-1)(h-2)/(2b).
Using this minimum in the total charge proves BRANCH CAP.
