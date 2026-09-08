# A Heavy Receiver Color Pays Its Own Tuple Cost

Use the source hypotheses of receiver-fiber peeling: actual dimension s>=2,
degree<K affine polynomial explanations, fixed receiver, original finite
labels, size-m full-code-bad supports with m=K+d, and empty universal
carrier core. Let A be one COMPLETE nonzero evaluation fiber of size a.
Freeze minimizing pairs and their actual receiver colors on A.

There is at most one color C with size t>a/2. All other pair cores meet
A in at most a-t coordinates. Put 1<=T<=d, M=m-T, ell=s-1,
e=K-a-ell>=0, c=M-K+1, and

    F_A(z)=(M-z)*product_(i=1)^(ell-1)(M-z-e-i)
             *(s*z+max(c-z,0)).

Every LOW record, raw<=T, assigned to C has at least
(s+1)*F_A(t) independent incidence tuples. Its M-point complete-core
subset can be chosen to include ALL t coordinates of C.
Every other LOW record has at least (s+1)*b_L(t) tuples, where

    b_L(t)=min(F_A(0),F_A(a-t),F_A(c) if c<=a-t).

Let beta0>=0 be any further proved lower cost for each LOW record, and
let beta_high>0 bound every HIGH record. Define

    beta_L=min(beta_high,max(beta0,(s+1)*b_L(t))),
    beta_H=min(beta_high,max(beta0,(s+1)*F_A(t))).

More generally one may use ANY uniform positive light cost and nonnegative
heavy cost no larger than these proved bounds, including parameter-box
lower bounds. If Q is a proved FULL cap for child explanation families
of affine dimension at most s-1, degree K-a, length n-a and agreement
m-a, with no child near hypothesis, put H_up=Q+a-t.
Writing U for the original independent-tuple resource, one has

    |Gamma| <= floor(U/beta_L
                 +max(0,1-beta_H/beta_L)*H_up).       (TWO-COST)

Without a heavy color, every core has occupancy<=a/2 and the light-only
bound applies. A nonnegative relaxed heavy term at t=a/2 also covers it.

Both costs use ONE original tuple resource, not independent budgets.
Actual heavy occupancy is essential. No original near allowance is included;
full child caps and original-row transport belong to finite consumers.
