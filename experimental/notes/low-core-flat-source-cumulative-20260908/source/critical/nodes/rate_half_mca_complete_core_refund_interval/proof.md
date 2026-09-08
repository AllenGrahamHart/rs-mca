# Proof By Complete-Core Costs On An Exhaustive Parameter Cover

Set L=40000,H=44999,T=6,D=d-T=67466,c=D+1=67467,
M=J+D, P_d=prod_(i=1)^10(d+i), w=10488/125,
U_0(J)=(R+J)_falling_12 and near=134944.

## 1. Exhaustive Maximum-Density Split

Choose a maximum-density proper flat of the actual nonzero evaluation
configuration. Write its rank j, cardinality a and density h=a/j.
The required basis theorem gives a<=J-11+j, hence h<=h_j(J), where

    h_r(J)=1+(J-11)/r.

If h<=h_7=(J-4)/7, the hybrid count pays each LOW record by at least

    12*B_low,
    B_low=(J+D)*prod_(i=1)^6(J+D-i*h_7)
                  *prod_(i=7)^10(D+11-i).

The seven variable factors have positive slopes summing to four and
values at most D+H. The exact inequality
4*(R+L-11)>12*(D+H) makes U_0/(12*B_low) decrease on the whole
interval. Its floor at L plus near is 240281411914853457.

Every HIGH raw>=7 record has charge at least beta_high=(J+d)P_d*w,
including raw>d. This is the same previously proved completed-weight
floor; its elementary gates are retained in verify.py. The coarse upper
U_0(H)/floor((L+d)P_d*w)+near is smaller than the LOW total. LOW and
HIGH consume the same resource and combine by maximum.

Otherwise h>h_7, so h<=h_j forces 1<=j<=6. Also

    j*h_7<a<=j*h_j, a<c.

This split has no structural source hypothesis. Freeze one minimizing
pair per selected record; no support or minimizer is changed below.

## 2. Parameter Cover For Ranks One Through Five

For these ranks use the proved pointwise basis count

    F(J,a,z)=P(M-z)*g_j(z),
    P(X)=X*prod_(i=1)^(10-j)(X-min(J-a-(11-j)+i,i*a/j)),
    g_j(z)=prod_(i=0)^(j-1)(c+i-z)+11*A_(j-1)*z,
    A_k=prod_(i=0)^(k-1)(c+i).

It is positive log-concave in z on [0,a]. Rank five uses its proved
a<=c,c>=100 supplement. By the complete-core packing lemma, a LOW
record whose FULL pair core has occupancy z can use this exact value:
the M-point counted core includes every one of those z flat points,
even if some were outside the old selected witness. The old defect and
minimizing pair remain unchanged. The charge is at least 12*F.

For r=j,...,6, split the density/degree region between j*h_(r+1) and
j*h_r into A=8 equal affine pieces. Their endpoints are

    a(J,u)=j*(1+(J-11)*(r*A+u)/(A*r*(r+1))), u=0,...,A.

Use the five consecutive integer blocks [40000,40999],...,[44000,44999].
Each block is bounded on its full closed real hull. There is no untested
integer between blocks. For a fixed block [J0,J1], r and u, the region
in (J,a) is the convex quadrilateral with its four listed endpoint values.

The degree/density branch in every P factor is fixed on this region:
use density when j+i<=r and degree otherwise, with equality harmless
at a boundary. For fixed lambda, every factor of P(M-lambda*a) is
positive affine in (J,a), and log g_j(lambda*a) is concave. Therefore
log F(J,a,lambda*a) is concave on that quadrilateral. Its minimum is
at one of the four vertices. This is the reason corner checks cover
the intervening sources; no numerical interpolation is assumed.

## 3. Actual Heavy Cost And Its Child Bound

The projected-pair theorem gives distance Delta=a/j and at most one
heavy projected pair, with complete core size t>a-a/(2j). The other
pair cores have occupancy at most b(t)=2a-a/j-t. The full heavy-label
bound, including exceptions, is

    Q(t)=(R+J-a)*U_j/(d+J-t)+a-t,

with the existing FULL anchored caps

    U_1=10755802499540570, U_2=737012707696078,
    U_3=50371450079970, U_4=3424826154478,
    U_5=231038329409.

The retained child has empty universal core, degree J-a, agreement m-t,
and the original field and labels. No child near event is imposed.

Split t/a between 1-1/(2j) and 1 into B=8 intervals with endpoints

    kappa_v=((2j-1)*B+v)/(2j*B), v=0,...,B.

For one such interval [k0,k1], light occupancy is at most
lambda_L*a, lambda_L=2-1/j-k0. Let V0 be the four (J,a) vertices.
The following INTEGER charges are valid for every record of the respective
groups throughout that whole source-parameter box:

    beta_L=min(floor(12*min_(V0,z/a=0,lambda_L) F),
               floor((d+J0)P_d*w)),
    beta_H=min(floor(12*min_(V0,z/a=k0,k1) F),
               floor((d+J0)P_d*w)).

Log-concavity in occupancy gives its endpoint minimum first; joint
log-concavity gives the four-vertex minimum next. The full-core lemma
is essential for beta_H: the heavy group has the actual occupancy t,
not an arbitrary smaller selected-core intersection. HIGH records are
covered by the second term of both minima.

For fixed kappa>=1/2 the ratio (R+J-a)/(d+J-kappa*a) increases with a,
since kappa*(R+J)>d+J. On each upper size edge a=alpha*J+beta it
decreases with J: its derivative numerator is

    (1-alpha)d-(1-kappa*alpha)R+beta*(1-kappa)<=0,

because 0<alpha<=1, beta<=0 and R>d. Thus, with a0=a(J0,u+1)
and a1=a(J1,u+1), a valid full heavy-label cap is the integer

    Q_box=ceil((R+J0-a0)*U_j/(d+J0-k1*a0)+(1-k0)*a1).

The exception term is bounded separately; it is not silently omitted.
The same-source TWO-COST inequality gives the exact box total

    floor((U_0(J1)+max(0,beta_L-beta_H)*Q_box)/beta_L)+near. (LOW-RANK)

No heavy group is covered by the first occupancy interval v=0 with
zero heavy labels. Its box total dominates the light-only bound. This
accounts for equality at the strict heaviness threshold as well.

There are 5*8*8*sum_(j=1)^5(7-j)=6400 source-parameter boxes.
Their maximum total is 264060029243645954, at J0=40000,j=1,r=3,u=0,v=7.
Different possible heavy groups/flat choices are whole-source alternatives,
not payments to add. No choice is presumed to have a favorable parameter.

## 4. Rank Six Uses A Uniform Signed Inside Count

Here 6*h_7<a<=J-5. Use the same eight size slices with j=r=6,
the same five J blocks, and 64 occupancy slices z/a in [v/64,(v+1)/64].
This z belongs to each LOW record, not to a shared heavy group. No
receiver-group child is used in this branch.

Put a0=a(J0,u),a1=a(J1,u+1), lambda0=v/64,lambda1=(v+1)/64,
t0=lambda0*a0,t1=lambda1*a1,h1=a1/6. Then all such record occupancies
and flat densities obey t0<=z<=t1<c and a/6<=h1. Use the generic
signed BOX count with calibration q=t1. All its coefficients are fixed
inside that box; negative coefficients use t1^b, not a lower tuple count.
The exact certificates verify the resulting inner lower bound is positive.

Because a>=6*h_7, every quotient factor uses its degree branch:

    P(M-z)=(J+D-z)*prod_(i=1)^4(D+a+5-i-z).

The first factor attains its minimum at one of the eight (J,u,lambda)
corners: it is affine in each of these three parameters when the others
are fixed. The remaining factors are bounded below by
D+(1-lambda1)*a0+5-i. Multiplying these positive lower bounds by the
positive inner BOX bound, then by twelve, gives a valid LOW charge.
Take its integer floor and its minimum with floor((d+J0)P_d*w).

For fixed J block and size slice, DIFFERENT records may occupy different
z slices. Every record still consumes at least the MINIMUM charge over
those 64 slices on the ONE shared resource U_0(J1). Consequently the
whole-source quotient is bounded by the MAXIMUM of their individual
quotient upper bounds, not their sum. Other J/size slices are source-level
alternatives. The 5*8*64=2560 exact bounds have maximum
231762550270308532, at J0=40000,u=0,v=0.

## 5. Exact Arithmetic, Assembly And Scope

The three exhaustive branches have near-inclusive upper bounds

    low density: 240281411914853457;
    ranks 1..5 with exact heavy cost: 264060029243645954;
    rank six signed inside count: 231762550270308532.

They combine by maximum, proving (NEW). The primary rational checker
and independent integer-scaled checker cover every box. Integer scaling
retains exact signs, products, floors and ceilings; neither uses floating
point or a field-size search. Progress is printed per completed J block.
The universal geometry and coverage arguments above remain hand proofs.

The required previous interval pays 45000..169999 by 274929007493481160.
Its maximum with (NEW) proves (UNION). The original-source assembly
receives this theorem with identical field, label, badness and empty-core
hypotheses, and retains the single original near allowance. No original
rank bound, active-v4 owner charge, unrestricted row or Prize closure follows.
