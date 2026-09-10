# Charge A Slope Once And At Most H Large Integer Masses

Use the required compression-fibre raw-weight theorem. Its ACTUAL occupied
fibres have integer shifted masses x_c in[L,Z], L>=1, sum_c x_c<=S,
where S=n-K+1. Their nonpreferred original raw weight is at most
w(x_c)=(S-x_c)*L_list(x_c). The common preferred label costs at most t.

Fix an integer threshold T>=L and a nonnegative integer H such that
(H+1)*(T+1)>S. Each large fibre has integer mass at least T+1, so there
can be at most H such fibres. The assertion is about ACTUAL fibres, not
an assumed number of scalar lists or independent maximizers.

Choose nonnegative rational alpha,beta with

    w(x)<=alpha*x                 for L<=x<=min(T,Z),
    w(x)<=alpha*x+beta            for max(L,T+1)<=x<=Z.

Summing over the actual fibres gives

    total raw weight <= t+alpha*sum_c x_c+beta*N_large
                     <= t+alpha*S+beta*H.

This uses the one shifted-core resource ONCE. The extra beta charge is
paid only for the at-most-H large fibres. It is not an additional tuple
budget or a repeated preferred-slope allowance. Empty classes are allowed.

A consumer may use any proved scalar LIST bound for w, but its two
envelopes must hold on every legal integer mass, not only at endpoints.
The theorem supplies no scalar LIST bound or source-to-slope identity by
itself. Original labels, receiver, field and complete cores are unchanged.
