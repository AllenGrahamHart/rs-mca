# A Source-Collision Bound For The Distinct-Fiber Resource

Status: PROVED by the hand argument; external independent review remains due.

Use the selected full-code-bad source of the projective-fiber secant theorem,
with actual carrier dimension s>=3, r=s+1, n>=r coordinates and empty
universal carrier core. There are z carrier-zero coordinates; every nonzero
projective evaluation fiber has size a_i<=A, where A>=2. Put

    T=sum_i a_i*(a_i-1),      0<=T<=n*(A-1).

After charging the SAME single exceptional slope set, of size<=z+T/2,
the common ordered-tuple resource is at most

    U(n,r,A,T)=(n)_r - binom(r,2)*T*(n-2)_(r-2)
       +3*binom(r,3)*(A-2)*T*(n-3)_(r-3)
       +3*binom(r,4)*T^2*(n-4)_(r-4).                 (RESOURCE)

Falling products are used. The original carrier-zero coordinates may be
padded as distinct singleton classes solely to upper-bound this resource;
they are not added to any agreement support.

U is nonincreasing in T on0<=T<=n*(A-1) whenever

    binom(r,2)*(n-2)*(n-3)
      >=3*binom(r,3)*(A-2)*(n-3)+6*binom(r,4)*n*(A-1).  (MONOTONE)

For a fixed positive uniform surviving tuple cost beta, the selected label
count is at most z+T/2+floor(U/beta). More generally, all surviving record
costs sum to at most U. Original near, if needed, is a separate one-time
transport obligation. Source collision T is not a received-word child count.
