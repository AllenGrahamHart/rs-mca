"""Small algebraic controls for rational compression, not MCA source sampling."""
from fractions import Fraction as Q


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    # A0=1,A1=X; H=span((X,-1),(X^2,-X)), z=(-X,X^2).
    # The row on z is X^3-X: its full degree is K+h-1=3.
    p = 101
    roots = [x for x in range(p) if (x*x*x-x)%p == 0]
    need(roots == [0, 1, 100], "full annihilator degree can be attained")
    need(len(roots) > 3-1 and len(roots) == 3+1-1, "height cannot be dropped")
    for x in range(p):
        need((x+x*(-1))%p == 0 and (x*x+x*(-x))%p == 0, "pencil row")
        need((-x+x*(x*x))%p == (x*x*x-x)%p, "quotient row")
    # The product carrier 1,X,X^2 has dimension3 and height1.
    need(2*1 == 3-0-1, "sharp quadratic-product degree")
    for sh in (1040000, 1048576, 1048577):
        threshold = 349525
        need(3*(threshold+1)>sh, "two large integer masses")
        masses = [threshold+1, threshold+1, sh-2*(threshold+1)]
        need(min(masses)>0 and sum(masses)==sh, "positive shared-mass fixture")
        alpha,beta = Q(7,3),Q(11,2)
        used = sum(alpha*x+(beta if x>threshold else 0) for x in masses)
        need(used<=alpha*sh+2*beta, "one budget and two excess charges")
    print("PASS primitive row, full-degree annihilator, product carrier and integer packing controls")
    print("Fixtures do not test full-code badness, original minimization, or universal geometry")


if __name__=="__main__":
    main()
