# Average Actual Subsets Before Pricing Fibres

Choose an s-subset S' uniformly from the M ACTUAL points. Intersect each
R_i with S', and choose a new tree if that intersection has size at least2.
The same geometry applies to every S': the sum of these tree-edge counts
is at most K_s. Reusing a previously chosen tree without reconnecting its
intersection would not justify this count.

Let X=|R_i intersection S'|. The identity (X-1)_+=X-1+1_(X=0) gives

    E[(X-1)_+]=s*r_i/M-1+binom(M-r_i,s)/binom(M,s)=f(r_i).

Averaging the exact graph inequality proves sum_i f(r_i)<=K_s. All
quantities are rational; no actual sampling or probabilistic premise occurs.
For r=0,1 the expression is zero, and in general f(r)>=0.

Now assume r<=a+b*f(r) for every integer occupancy0<=r<=q, with a>=1
and b>=0. Multiplying by the nonnegative fibre sizes and summing gives

    sum l_i*r_i <= a*sum l_i + b*sum l_i*f(r_i)
               <= a*N+b*nu*sum f(r_i)
               <= a*N+b*nu*K_s.

One chosen maximal ACTUAL group per fibre suffices even if receivers vary
between coordinates: its size bounds every coordinate in that fibre.
The theorem needs these chosen groups on distinct null lines. It is not
valid for arbitrary unrelated groups merely because each size is small.
