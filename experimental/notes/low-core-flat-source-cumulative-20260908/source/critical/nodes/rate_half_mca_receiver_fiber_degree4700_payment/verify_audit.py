"""Independent integer bracketing and positive-polynomial endpoint checks."""

from math import prod


def need(ok,why):
    if not ok:
        raise ValueError(why)


def main():
    n,m,k = 1053276,72172,4699
    need(1600*m*m>=1681*n*k and 36*k<=1681*n,"exact anchor gates")
    for num,den,ceiling in ((1681*n*k,4,1442208),(1681*n,4*k,307)):
        need(den*(ceiling-1)**2<num<=den*ceiling**2,"least square-root ceiling")
    need(12*k*(31400-1)<1681*n<=12*k*31400 and 31400>=307,"least Z ceiling")
    child = 8536194661768235
    need(child==2*1442208*307**2*31400+(n-m+1)*307+31400,"full-source Johnson arithmetic")
    j,d,r,hi = 23000,67466,1048576,52999
    factors = [d+j]+[d+j-4690-i for i in range(1,10)]
    need(all(0<a<=d+hi for a in factors) and 10*(r+j-11)>12*(d+hi),"uniform derivative factors")
    numerator,denominator = prod(range(r+j-11,r+j+1)),12*(d+1)*prod(factors)
    need(numerator<(161394160592554522+1)*denominator,"HIGH dominates entire LOW interval")
    total = 246756107210901806
    need(total==10*child+10*hi+161394160592554522+134944,"disjoint whole-source composition")
    need(2130706433**6//2**128-total==28224620900493281,"original finite budget")
    for wrong in (1442207,1442209):
        need(not 4*(wrong-1)**2<1681*n*k<=4*wrong**2,"wrong root ceiling rejected")
    print("PASS independent anchor ceilings, positive factor bounds, composition and mutations")
    print("No child near event, uncharged exception or all-source fiber hypothesis")


if __name__ == "__main__":
    main()
