# Proof

## 1. Propagate one low minimizer through all supports

Fix a low label and a carrier explanation h whose complete scalar
agreement set A has a bad m-subset. Every bad m-subset for this h has
raw<=T, since the maximum was taken over all explanations and supports.
Start at one such subset S, with minimizing b in V.

The graph of ALL m-subsets of A joined by one-coordinate exchanges is
connected. Suppose a neighboring S' is bad. Its minimizer b' in V
agrees with b on at least

    (m-1)-2T=K+d-1-2T>=K

coordinates, hence b'=b by the polynomial root bound. If S' is instead
pair-contained in the FULL degree-<K code, its containing second
polynomial b' agrees with b on at least m-1-T>=K coordinates.
Again b'=b, so this b' lies in V even though full-code containment
initially supplied no carrier membership. Thus b has <=T mismatches
on every m-subset, including all pair-contained neighbors.

If b had more than T mismatches on A, choose an m-subset containing
T+1 of them, a contradiction. Thus its global defect r_A<=T.
Any other degree-<K polynomial within T on A would agree with b on
at least |A|-2T>=m-2T>=K+1 points, proving uniqueness.

There is at least one defect, since A has a bad m-subset. Include all
r_A defects and any m-r_A core points. These exist because |A|>=m.
The support is full-code-bad: m-r_A>=K points determine b uniquely,
and a defect contradicts that containing second polynomial. Every other
candidate in V has more mismatches than b, by the same root bound.
This support has raw r_A, the largest possible for this h.

Apply this to the selected maximizing h_gamma. Its raw maximum equals
r_A, so the selected S_gamma contains ALL defects of its complete A.
The asserted decomposition and freedom to choose its core part follow.

## 2. Rank-one collisions force a high alternative

Suppose two allowed pairs have the displayed rank-one difference and
large cores H,H'. At gamma=-alpha/beta, their scalar explanations
coincide as a polynomial h in h_*+V. Their union lies in its scalar
agreement set A. Since b'-b is nonzero, |H intersect H'|<=K-1, so

    |A|>=2(m-T)-(K-1)=m+d+1-2T>m.

A bad m-subset exists: choose K points from H and one point of
H' minus H, then fill to m points inside A. The point outside H has
P(x)!=0 and b'(x)!=b(x), so no degree-<K second polynomial can
contain that support. The scalar explanation remains h everywhere.

If gamma were a low selected label, part 1 would give a second
polynomial c within T on A for this h, whether or not h was the
selected explanation. On each of H,H', it agrees with b or b' on
at least m-2T>=K+1 points. Thus c=b=b', a contradiction. This is
why the maximum ranges over ALL carrier explanations, not only one h.

At a cross-core incidence for a low owner f, choose any represented
f' covering x. If their component differences were dependent, they
would have the displayed form. The actual nonzero second mismatch
at x forces beta!=0. Their collision slope is exactly the selected
scalar-agreement label, which part 2 excludes. Rank zero is impossible
because x is outside H_f. Hence the difference rank is exactly two.

## 3. Scope and choice

Only finite maximization is used; no claim of a practical algorithm for
the deployed field. The receiver, fixed carrier, code, labels and domain
are unchanged. Explanation choices and error rank can change, so any
subsequent rank test must be applied AFTER this selection. In the finite
consumer the selection is made on the already normalized empty-carrier-
core row. Its literal universal carrier core is therefore unchanged.
No earlier arbitrary support's raw minimum is transported through this
operation, and no extra prime-field premise is introduced.
