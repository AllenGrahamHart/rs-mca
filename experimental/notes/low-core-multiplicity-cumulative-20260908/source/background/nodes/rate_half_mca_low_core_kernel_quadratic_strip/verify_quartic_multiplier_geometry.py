"""Tiny exact multiplier, height, exception and projection-price checks."""

from fractions import Fraction as Q


def check(ok, label):
    if not ok:
        raise ValueError(label)


def height(j):
    return max((111*j-960724)//15, (146*j-1295624)//10)


def dim_multipliers(j, h):
    w, s = j-1, 66976-3*j-h
    return sum((i+1)*max(s-i*w, 0) for i in range(5))


def verify():
    for j in (8764, 9014, 9015, 9099, 9100, 9294, 9295, 9526):
        a, w, n = j+66972, j-1, 1048576+j
        full = sum((i+1)*(a-i*w) for i in range(9))
        low = full-n
        check(low == 1965404-196*j and low-10*w > 0,
              "full kernel and positive multiplier blocks")
        h = height(j)
        check(dim_multipliers(j,h) >= low > dim_multipliers(j,h+1),
              "exact integer height envelope")
        check(dim_multipliers(j,0)-low == 111*j-960724,
              "complete-core union bound")
    check((height(8764),height(9294),height(9526)) == (805,6130,9517),
          "leading coefficient ceilings")
    check(216*9099 < 1965424 < 216*9100, "truncated block transition")
    check(66976-3*9526-height(9526) == 28881, "minimum graph-forbidden agreement count")

    rows = [(1027700,114,9014), (1094677,118,9276),
            (1161655,123,9444), (1228634,129,9524), (1295614,136,9526)]
    for t, (constant, slope, endpoint) in enumerate(rows,1):
        triangular = t*(t-1)//2
        check(constant == 960724+66976*t+triangular and
              slope == 111+3*t+triangular, "Newton constraint polynomial")
        check(constant-slope*endpoint > 0 >= constant-slope*(endpoint+1),
              "strict off-pair staircase endpoint")
    check(2009300-110*8764 == 1045260 and 2009300-110*9526 == 961440,
          "union density endpoints")

    check(height(9294)//4 == 1532 and height(9295)//4 == 1536,
          "projection height scope")
    q16, q17 = Q(1048577-1532,66973-1532), Q(1048577-2379,66973-2379)
    check(1 < q16 < 16 and 1 < q17 < 17, "true larger-degree LIST ratios")
    forbidden = Q(1048577-2379-28881,66973-2379)
    check(forbidden == Q(1017317,64594) < 16,
          "off-curve pair supplies enough forbidden agreements")
    table16 = [4**(22-d-(d+3)//4)*16**((d+3)//4) for d in range(4,12)]
    table17 = [4**(22-d-(d+3)//4)*17**((d+3)//4) for d in range(6,12)]
    check(max(table16) == 4**19 == 274877906944, "all large-kernel graph cases")
    check(max(table17) == 4**14*17**2 == 77577846784, "d>=6 graph cases")
    check(max(4**19,4**18,4**16*17) == 4**19, "actual dimension-drop cases")
    base, labels = 23067643444721720934//5500+134944, 981604
    total = base+labels*(4**19+4)
    strong = base+labels*(4**14*17**2+4)
    budget = 2130706433**6//2**128
    check(total == 274015369961868939 and budget-total == 965358149526148,
          "single original resource/near and four off-curve pairs")
    check(strong == 80344841708572299 < total < 274979661975561635 < budget,
          "sharper graph price and unchanged residual alternative")
    print("PASS: quartic height ceilings, 0/1/2/3/4 exceptions and dense complete-core union")
    print("PASS: moving graph source price", total, "reserve", budget-total)
    print("No new complete interval or prize closure; geometric/source arguments are hand proofs")


if __name__ == "__main__":
    verify()
