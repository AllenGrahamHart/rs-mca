# A Quantitative Balanced Basis Product Beyond The Exact Density Gate

Let V have actual rank s>=2 and degree <K on N>K distinct nonzero
polynomial evaluations. Put D=N-K. Suppose every proper rank-j flat has
at most j*h coordinates. Choose a real number lambda satisfying

    1<=lambda<=2, floor(s^2/4)*h<=lambda*N.

For real x>=1 define F_1(D,x;lambda)=D+x and

    F_2(D,x;lambda)=(D+x)*(D+1),
    F_r(D,x;lambda)=(D+x)*F_(r-1)(D,1+(1-lambda/(r-1))*(x-1);lambda)
        for r>=3.

Then the ordered basis count is at least F_s(D,K;lambda).
Equivalently, for s>=2 the product is

    (D+1)*product_(a=2)^s [D+1+(K-1)*product_(j=a)^(s-1)(1-lambda/j)].

Every factor is positive. The product is nondecreasing and convex in
x>=1, and nonincreasing in lambda on [1,2]. At lambda=1 it is exactly
the earlier balanced product. The interval [1,2] is a proved sufficient
scope, not a claim of failure for every larger lambda.

This is a basis count, not a received-word descent or an MCA numerator.
It needs density on ALL proper flats, not only projective fibers.
