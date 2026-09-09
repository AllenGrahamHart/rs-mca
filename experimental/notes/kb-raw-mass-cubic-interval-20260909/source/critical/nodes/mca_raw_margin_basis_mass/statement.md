# Retain Every Defect In A Common Core-Basis Resource

Status: PROVED. External independent mathematical review remains due.

Fix a selected full-code-bad MCA family on n distinct finite field points,
with1<=s<=K<m=K+d<=n, and a fixed affine explanation carrier
h_*+V with actual dim V=s. Require the universal carrier core

    {x: V(x)=0, u(x)=h_*(x), v(x)=0}

to be empty. Select one explanation and size-m bad support per distinct
label gamma. Let r_gamma>=1 be the minimum mismatch of v to b in V on
that support. No canonical selection or post-near premise is required.

Fix integers 1<=T<=d and 1<=kappa<=T+1. Suppose every nonzero rank-s
polynomial evaluation space of degree<K on m-T points has at least B>0
independent ordered bases. Put

    beta=(s+1)*B, P=product_(i=1)^(s-1)(d+i), U=(n)_falling_(s+1).

If

    (T+1)*m*P >= kappa*beta,                         (HIGH)

then the SAME original tuple resource gives

    sum_gamma min(r_gamma,kappa) <= floor(U/beta)=W. (MASS)

In particular, if L_t counts labels with raw<=t,1<=t<kappa, and
N=|Gamma|, then

    (t+1)*N-sum_(j=1)^t L_j
      =sum_gamma min(r_gamma,t+1)<=W,                (FLAG)
    (t+1)*N-t*L_t<=W,
    L_t>=max(0,ceil(((t+1)*N-W)/t)).                 (TAIL)

If a separate proved theorem bounds L_t<=H, the whole selected source is
bounded by floor((W+t*H)/(t+1)). This is one shared resource, not the
sum of independently maximized LOW and HIGH quotients. The theorem does
not assert a bound on L_t or a prize endpoint; its consumer must supply
the core-basis bound, HIGH gate and original-source/near accounting.

More generally, replace(HIGH) by ANY separately proved uniform lower
bound H on the number of independent tuples owned by EACH raw>T record,
with H>=kappa*beta. All conclusions are unchanged. H concerns the SAME
incidence tuples, not a different resource or an unproved normalized
weight. The baseline choice above is H=(T+1)*m*P.

## A Complete-Pair Owner Ledger

Assign each raw<kappa label to its chosen minimizing pair f=(a,b).
Let H_f be its COMPLETE joint core, and c_f=max(1,m-|H_f|). Then

    sum_(gamma assigned to f)(kappa-raw_gamma)
      <=floor((kappa-c_f)*(n-|H_f|)/c_f).             (OWNER)

Only actual represented pairs are counted; each has c_f<kappa. The
formula sums their original-label deficits, not separate whole-line
budgets. A consumer still has to bound the number of these pairs.
