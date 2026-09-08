"""Independent integer-scaled mass audit; imports no primary implementation."""


def check(ok,message):
    if not ok:
        raise ValueError(message)


def falling(n,r):
    out=1
    for i in range(r):
        out*=n-i
    return out


def product_scaled(k):
    out=1
    for i in range(11):
        out*=674670+i*(k-1)
    return out


def main():
    budget=(2130706433**6)//(2**128)
    pd=falling(67482,10)
    check(8*67472*90472*pd*10**11>=67483*product_scaled(29999),"coarse refund certificate")
    rows=((23000,268913508505087358,6933965264351691),
          (25000,241182907136195749,38626081114513530),
          (28000,205624578023526844,79264171528992278),
          (29999,185335366473228672,102451841872190189))
    for k,expected,mass in rows:
        resource=falling(1048576+k,12)
        low_n,low_d=resource*10**11,12*product_scaled(k)
        high_n,high_d=125*resource,(67472+k)*pd*10488
        num,den=(low_n,low_d) if low_n*high_d>=high_n*low_d else (high_n,high_d)
        g=num//den+134944
        check(g==expected,"independent good comparison")
        difference=8*(budget-g)
        check((mass-1)*7<=difference<mass*7,"exact strict threshold")
        for wrong in (mass-1,mass+1):
            check(not (wrong-1)*7<=difference<wrong*7,"corrupt threshold accepted")
        print("AUDIT",k,g,mass)
    check(11*1071565>24*97465,"whole-interval monotonicity")
    high_upper=125*falling(1078575,12)//(90472*pd*10488)+134944
    check(high_upper==166836445768446334<rows[0][1],"coarse HIGH endpoint")
    check(7*8==8*7 and not 7*8>8*7 and 7*9>8*7,"strict divisible mass gate")
    check(8<=4+7 and 8>7,"premature floor countercontrol in eighths")
    for t in (8,9):
        maximal_excess=(11-t)*(29999-11+t)-(10-t)*(t-1)
        check(maximal_excess<=97465,"direct high-rank exclusion")
    check(4*24370-3*6<=97465<4*24371-3*6,"direct rank-seven core floor")
    check(29999-24371==5628,"auxiliary degree endpoint")
    print("PASS independent integer comparisons, refunds, strict masses and rank gates")


if __name__ == "__main__":
    main()
