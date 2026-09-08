# Balanced Bases Or An Actual Dense Core Flag

Status: PROVED by the hand argument; independent external review remains due.

Let V have actual dimension s>=2 and degree <K on N=D+K distinct
points H, with D>=1, K>=s and all evaluations nonzero. Put

    P_s(D,K)=product_(i=0)^(s-1)(D+K-i*(K-1)/(s-1)).

If the number of independent ORDERED s-tuples is less than P_s(D,K),
then s>=3 and there are nested subspaces F<G of V*, spanned by H
evaluations, with dim F=t-1, dim G=t, 1<=t<=s-2. For the COMPLETE
flat coordinate sets inside H, put

    a=|{x in H: ev_x in F}|, b=|{x in H: ev_x in G}|.

They satisfy

    (s-t)*b-(s-t-1)*a > N,                               (FLAG)
    a>=t-1, b<=K-s+t.

Thus either the full balanced basis product holds or an actual dense
flag exists. Both conclusions may hold; this is not an exclusive dichotomy.
No maximum-density hypothesis, recursive envelope or statistical premise
is used. At s=2 the balanced product always holds and there is no flag.

For MCA, apply this to a FIXED M=m-6 point subset of the full joint core
of the original selected minimizing pair. The flag uses that actual core,
not an arbitrary dense flat elsewhere in the carrier. It does not itself
count bad slopes or supply a received-word descent through the flat.
