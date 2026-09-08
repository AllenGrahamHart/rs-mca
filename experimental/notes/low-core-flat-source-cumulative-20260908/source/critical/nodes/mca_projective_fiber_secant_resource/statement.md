# Charge Fiber Secants Before Counting Independent Tuples

Status: PROVED by the hand argument; independent external review remains due.

Use the selected-slope setup of the nonuniform support-margin resource:
degree-<K carrier V of actual dimension s, affine explanations h_*+V,
received pair (u,v), distinct finite labels Gamma, and size-m full-code-bad
scalar-agreement supports, with m=K+d<=n and d>=1. Require an empty
universal carrier core {x:V(x)=0,u(x)=h_*(x),v(x)=0}.

Let z count carrier-zero coordinates. Partition all other coordinates
into COMPLETE projective evaluation fibers A_i, with sizes a_i. There is
an explicit set E of finite slope labels, determined by the receiver and
carrier, with

    |E| <= z + sum_i binom(a_i,2).                        (EXCEPTIONS)

For every gamma outside E, every independent ordered (s+1)-tuple of
coordinates agreeing with h_gamma uses distinct nonzero evaluation fibers.
Thus, if b_gamma is any proved lower count of such tuples for that record,

    sum_(gamma in Gamma minus E) b_gamma
       <= (s+1)! e_(s+1)(a_1,...,a_f),                   (FILTERED)

where e_r is the elementary symmetric polynomial. A uniform b_gamma>=b>0
gives the whole selected-family bound

    |Gamma| <= z+sum_i binom(a_i,2)
                   +floor((s+1)! e_(s+1)(a_i)/b).       (COUNT)

Counts using complete pair cores remain valid: their tuples agree with
the same original h_gamma, even outside the old selected support.
The exception set is charged ONCE, not once per label, fiber or basis.

If f<=F0 and F0>=s+1, the resource also obeys

    (s+1)! e_(s+1)(a_i)
       <= (F0)_falling_(s+1) * ((n-z)/F0)^(s+1).         (BALANCE)

No quotient receiver, smaller field, child near event or speculative
upper census is used. The dimension is that of the actual chosen V;
the selected explanations need not span it. This is not a universal
source-fiber bound or a Prize-row payment without a finite consumer.
