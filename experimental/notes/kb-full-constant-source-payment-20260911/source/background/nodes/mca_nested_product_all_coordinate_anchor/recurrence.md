# A Two-Dimensional State Table, Not A Regular-Anchor Tree

For original shared dimension11 with J<=M, a=11-s and
D<=J-a-1 imply 0<=kappa=D-(s-1)<=M-11 at EVERY shared stage.
Use one partition of that entire degree-excess interval.

Let T[s,c,i] bound an enclosure with shared s, pair dimension2s-c,
nested product form, and kappa in band i. Here 0<=c<=min(3,s).
There are42 states for s0..11, four terminal states and38 recurrences.

At s=c>0, use the degree-refined whole-constant scalar bound of
dimension c and maximum degree c-1+hi_i. At s=c=0, use R-d+t.

At s>c, define

    C=max_(j<=i) T[s-1,c,j],
    F=max_(j<=i) T[s-1,c-1,j], if c>0.

Insert those values into the three-value envelope in statement.md.
For c0 set the root excess to zero. This induction is well-founded
because EVERY child has smaller shared dimension, even when pair rank
drops by only one. It does not assume an actual occupied pencil.

For each cutoff t, max_i T[11,3,i] bounds the ORIGINAL low-raw weight
in a full constant11/rank19 source. Combine the two cutoff maxima with

    floor(W_raw/3 + M1/2 + M2/6) + 134944.

W_raw is the inherited upper bound for sum min(raw,3), and M_t is the
sum of original raw values over labels with raw<=t, not a pair count.

This is the original source budget. No extra eight-anchor factor is
multiplied in, and no source resource is refunded at a rank-one anchor.
The finite consumer proves the base costs and every state-table entry.
