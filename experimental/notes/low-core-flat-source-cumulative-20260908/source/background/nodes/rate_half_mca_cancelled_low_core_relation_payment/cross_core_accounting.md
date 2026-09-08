# Exact weighted cross-core accounting

Status: PROVED, 2026-09-07. This is an unconditional inequality with
an explicitly measured cross-core term, not an assertion that this
term is small on arbitrary sources. No new conjectural node is needed.

Use the empty-universal-core setup of this dossier, with complete
low cores at cutoff T, |U|>=m, e=n-|U|, and actual margin resource F.
For each low selected record write r_gamma=raw_gamma and H_gamma
for its complete minimizing pair core, and define

    i_gamma=|S_gamma intersect (U minus H_gamma)|,
    Omega_T=sum_low i_gamma*(1/r_gamma-1/(T+1)).

Let M_t count DISTINCT represented complete polynomial pairs with
max(1,m-|H|)<=t. Then

    |Gamma| <= F/(T+1)
          + e sum_(t=1)^T M_t/(t*(t+1)) + Omega_T.        (CC)

If V_t bounds the shared-carrier rank-(s-1) JOINT list on
(|U|-1,K-1,m-t-1), the proved joint LIST extension gives

    M_t <= |U| V_t/(m-t).                                (JL)

Every high label remains in the original global resource. No source
relation is assumed, no cross-core slope is silently discarded, and
neither (CC) nor (JL) asserts that Omega_T is affordable.

## Proof

On a selected scalar agreement support, matching the minimizing
second component is equivalent to matching the complete polynomial
pair. Hence the raw margin is exactly the number of selected noncore
coordinates. Write o_gamma=|S_gamma minus U|. Then r_gamma=i_gamma+
o_gamma, and the global resource inequality gives

    |Gamma|-F/(T+1)
       <=sum_low (1-r_gamma/(T+1))
        =Omega_T+sum_low o_gamma*(1/r_gamma-1/(T+1)).

For one represented pair f=(a,b), every associated explanation is
a+gamma b. Each outside-U coordinate can agree with at most one
of those labels: agreement at two distinct slopes would give
(u,v)=(a,b), putting it in H_f subset U. Thus the sum of o_gamma
over that pair is at most e. Also r_gamma>=t_f=max(1,m-|H_f|).
The outside contribution is at most e*(1/t_f-1/(T+1)). Summing
over represented pairs and telescoping proves (CC).

At a point of U where C' vanishes, ANY represented pair would have
value (h_*,0). Since some represented pair agrees there, this would
be a universally agreeing carrier zero, contradicting the empty core.
Thus evaluation on C' is nonzero at every point of U. Every pair in
M_t has at least m-t joint agreements there. At an anchor, subtract
one agreeing tuple, then divide both components by X-x. Their
differences lie in the SAME evaluation kernel of C', of dimension
s-1, so the joint LIST supplier bounds the anchored list by V_t.
Counting joint agreement incidences proves (JL).

## Exact KoalaBear consequence

For T=500 and 4801<=J<=254999, the existing constant-chart interval
certificate bounds F/501 plus the (JL) outside sum plus the original
near charge by 255637082864553898. This is the earlier certificate
with its optional one kernel label REMOVED. Therefore

    original total <=255637082864553898+Omega_500.         (KB)

An affordable sufficient cross charge is

    Omega_500<=19343645246841189.

This weakens the polynomial-relation hypothesis to an exact weighted
accounting condition. It does not claim that arbitrary relation-free
sources satisfy it. Small/empty unions retain their unconditional
76153884700948142 payment and need no Omega hypothesis.

The unfiltered replacement using n-|H_f| instead of e remains too
large. `verify_unrestricted_joint_recipe.py` shows its first-depth
term alone exceeds budget at J=6000,20000,100000,254999 with U=D.
Those are failures of that particular upper recipe, not unsafe rows
or a proof that every possible joint-list bound must fail.

## Margin separation at a cross-core anchor

If b is a minimizing second polynomial with raw margin r on a
size-m support, every different degree-<K b' has at least d+1-r
mismatches there. Indeed b and b' agree at at most K-1 coordinates,
while b agrees with the receiver at m-r coordinates. In particular
the minimum is unique if 2r<d+1, as for every raw<=500 record here.

If x is one of this record's cross-core coordinates, any second
polynomial forced to agree with the receiver at x differs from b.
After a carrier-compatible anchor gauge and division by X-x, its
child margin is therefore at least d+1-r. The anchor removed an
agreement, not a mismatch of those constrained candidates. This
penalty is valid, but summing crude child resources has not supplied
the affordable Omega bound. Do not replace that missing estimate by
the separation statement alone.
