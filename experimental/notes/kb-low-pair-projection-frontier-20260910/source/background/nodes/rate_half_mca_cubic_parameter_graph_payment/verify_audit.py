"""Independent integer-only reconstruction; no primary or compiler imports."""


def need(ok, message):
    if not ok:
        raise ValueError(message)


def multiply(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def main():
    R, gap, lower, upper = 1048576, 67472, 9965, 21499
    W, near, budget = 624373932788019251, 134944, 274980728111395087
    n4 = 4*multiply(range(R+lower-10, R+lower+1))
    d4 = 11*(gap+lower-1)*multiply(range(gap, gap+9))
    need(n4//d4 == 302790601542847445 < W and n4//d4+near > budget,
         "independent degree-four sufficient-recipe boundary")
    inputs = ((8, 227325639596777196, 12776402205892, 271476187024062739, 3942608723248893),
              (43, 228493023165539663, 12849534849046, 237527989066104848, 38323732976576059))
    for cutoff, mass, pairs, total, outside in inputs:
        numerator = 3*multiply(range(R+lower-10, R+lower+1))
        denominator = 11*(gap+lower-cutoff)*multiply(range(gap-cutoff+1, gap-cutoff+10))
        need(denominator*mass <= numerator < denominator*(mass+1), "exact raw mass floor")
        for wrong in (mass-1, mass+1):
            need(not denominator*wrong <= numerator < denominator*(wrong+1), "wrong mass rejected")
        pn, pd = 1, 1
        for step in range(11):
            s = 11-step
            r, K, n, A = 2*s, upper, R+upper, upper+gap-cutoff
            bad = K+s-r
            need(r > s and A > bad >= 0 and n-bad == R+s and A-bad == gap-cutoff+s,
                 "guarded original-domain rank-two anchor")
            pn, pd = pn*(n-bad), pd*(A-bad)
        need(pd*pairs <= pn < pd*(pairs+1), "exact pair floor")
        need(R+upper-10-11*(gap+upper-cutoff) > 0, "linear minimum of decreasing-ratio gate")
        exceptions = upper-8+3*pairs
        amount = W+cutoff*(mass+exceptions)
        need(amount//(cutoff+1)+near == total < budget, "same-source whole price")
        target = (cutoff+1)*(budget-near+1)-amount
        need(cutoff*(outside-1) < target <= cutoff*outside, "strict over-budget outside count")
        need((amount+cutoff*(outside-1))//(cutoff+1)+near == budget, "last safe recipe count")
        need((amount+cutoff*outside)//(cutoff+1)+near == budget+1, "first unproved recipe count")
        print("PASS independent cubic T", cutoff, "TOTAL", total, "RESERVE", budget-total)
    print("W0/HIGH44, original-source validity and tuple ownership remain hand-proof inputs")
    print("No primary imports, attainability assertion or unrestricted Prize payment")


if __name__ == "__main__":
    main()
