"""Independent binomial/integer audit; no primary, Fraction or field helper import."""

from math import comb, factorial


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    budget = 2130706433**6//2**128
    count, floors, low = 0,0,None
    for start,stop,c,expected in ((9941,13999,10,379243051432496463),
                                  (14000,17000,2001,275795460861917515)):
        N,b = 1048576+c,67471+c
        need(12*(b-10)-11*(N-11)<0 and N>12, "uniform derivative signs")
        previous = None
        for J in range(start,stop+1):
            a = J-c
            L = 2*(N+a-12)
            w = L+11*(a-1)
            numerator = factorial(12)*(comb(N,12)*L+a*comb(N,11)*w)
            denominator = 12*factorial(11)*(comb(b,11)*L+a*comb(b,10)*w)
            quotient,remainder = divmod(numerator,denominator)
            need(0<=remainder<denominator and quotient>=expected>budget,
                 "all degrees exceed budget without near")
            for wrong in (quotient-1,quotient+1):
                need(not wrong*denominator<=numerator<(wrong+1)*denominator,
                     "adjacent integer floors rejected")
                floors += 1
            if previous is not None:
                pn,pd = previous
                need(numerator*pd<pn*denominator, "strict degree monotonicity control")
            previous = numerator,denominator
            need(a+9<J and a<67471+J<1048576+J, "construction lengths/degrees")
            if J>=14000:
                need(a==J-2001<J-2000, "source gate avoided at its actual scope")
            need(J<20481<21000<23000, "other existing gates not in scope")
            count += 1
            low = quotient if low is None else min(low,quotient)
        need(quotient==expected, "whole-regime minimum at final endpoint")
        print("AUDIT REGIME",start,stop,"minimum floor",quotient,flush=True)
    need(count==7060 and floors==14120 and low==275795460861917515,
         "complete independent streaming inventory")
    need(low-budget==814732750522428, "exact pre-near obstruction margin")
    print("PASS7060 degrees,14120 wrong floors; no primary/Fraction import")
    print("Control of a hand-proved method boundary, NOT unsafe MCA slopes")


if __name__=="__main__":
    main()
