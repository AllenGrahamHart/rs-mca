# Linear low-margin weights and cumulative counts

Status: PROVED. Specialize this node's selected-slope resource to
s=11 and gap Delta=67472. The allowed zero-normal count still gives
M=m-g>=Delta+11. For EVERY raw integer r>=1,

    w_11(r;g)>=11*min(r,500).                          (LW)

No minimum-margin or new source-selection assumption is added.

## 1. Keep a linear lower bound, not just the minimum weight

For 1<=r<=500, the completed weight has eleven positive factors:
one is 1-r/M, the other ten are 1-r/(Delta+i). Each denominator
is at least Delta+1. Bernoulli's product inequality gives

    b_11(r;g)>=12*r*(1-r/67473)^11
              >=12*r*(1-11*r/67473)>11*r.

The final inequality holds at the worst endpoint r=500 because

    12*(67473-5500)-11*67473=1473>0.

For real 500<=r<=5500, the logarithmic derivative of the positive
completed-weight expression is at least

    1/r-11/(67473-r)>0,

since 12*5500<67473. Thus b_11(r;g)>=b_11(500;g)>5500 on
that range. For r>=5500 the old truncated weight min(67473,r)
is already >=5500, even when r>Delta and the completed term is zero.
This proves (LW) for all raw margins.

## 2. Convert the SAME resource into nested LOW counts

Let C bound the sum of these recordwise weights, let N be the number
of distinct selected finite labels, and put L_t=#{gamma:r_gamma<=t}.
For any integer 1<=T<=500, (LW) implies

    w_11(r;g)>=11*min(r,T),
    sum_gamma min(r_gamma,T)
       =T*N-sum_(t=1)^(T-1) L_t.

Consequently

    N<=floor(C/(11*T)+(1/T)*sum_(t=1)^(T-1) L_t).      (CL)

Every raw margin is from the EXISTING selected source. The L_t form
nested subsets of that source, not independently reselected records.
This is an exact cumulative-count conversion, not addition of the old
/501-discounted group gains to a different HIGH resource.

For T=500 it retains the whole raw-margin profile below 500 and the
one /5500 resource. Each label is counted T-r times in the cumulative
sum if r<T, and zero times otherwise. Finite consumers own the
complete-core pair-to-label bounds for L_t and the original near add-back.

## 3. Equivalent raw-weighted cumulative form

Let S_t=sum_(gamma:r_gamma<=t) r_gamma. The exact identity

    sum_(t=r)^(T-1) r/(t*(t+1))=1-r/T

shows that (CL) is equivalently

    N<=floor(C/(11*T)+sum_(t=1)^(T-1) S_t/(t*(t+1))). (CR)

For T=1 both sums are empty. This is still one resource on the same
selected source. A consumer that has stronger bounds on S_t than on
L_t should retain them instead of discarding the per-pair raw budget.
