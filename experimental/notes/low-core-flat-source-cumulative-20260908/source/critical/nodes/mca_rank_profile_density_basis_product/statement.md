# Ordered Bases With A Rank-Dependent Density Profile

Let V be an actual rank-s polynomial space of degree <K on N=D+K
distinct nonzero evaluations, where D>=1 and K>=s>=2. Every proper
rank-j flat is assumed to contain at most j*h coordinates, with h>=1.
Fix integers s<=K0<=K<=K1. For r=3,...,s put j=s-r and

    mu_r = max(1/(r-1),
               min((K1-s+1)/(D+K1-s+r),
                   ((j+1)*h-j)/(D+K0-j))).

Then the ordered basis count is at least

    (D+1)*product_(a=2)^s
      [D+1+(K0-1)*product_(r=a+1)^s(1-mu_r)].       (PROFILE)

All mu_r lie in [1/(r-1),1), so every factor is positive.
For a fixed profile, this polynomial in K0-1 has nonnegative coefficients;
it is nondecreasing and convex in its scalar argument >=1, and decreases
with each mu_r. Its hypotheses hold over the ENTIRE degree interval
K0..K1, not just at an endpoint.

For K0=K1=K, (PROFILE) is at least the preceding quantitative-density
product whenever that product's lambda in [1,2] satisfies its density
guard. No global lambda<=2 guard is needed for (PROFILE) itself.

This counts polynomial bases, not MCA slopes or received-word children.
Density is coordinate density on ALL proper flats. No monotonicity or
convexity is asserted for the envelope obtained by recomputing the profile.
