"""Independent integer-scaled arithmetic; imports no primary certificate."""


def require(ok, message):
    if not ok:
        raise ValueError(message)


def falling(n, count):
    result = 1
    for i in range(count):
        result *= n-i
    return result


def scaled_basis(k):
    result = 1
    for i in range(11):
        result *= 10*67467+i*(k-1)
    return result


def floor_certificate(numerator, denominator, expected):
    require(denominator > 0, "positive denominator")
    require(expected*denominator <= numerator < (expected+1)*denominator, "floor remainder")


def main():
    low, high, near = 268913508505087358,166836445768446334,134944
    low_num = falling(1071576,12)*10**11
    low_den = 12*scaled_basis(23000)
    high_num = 125*falling(1078575,12)
    high_den = 90472*falling(67482,10)*10488
    floor_certificate(low_num,low_den,low-near)
    floor_certificate(high_num,high_den,high-near)
    require(11*1071565>24*97465, "LOW analytic derivative certificate")
    require(1848<67473 and 84*67396*125>10488*67473, "HIGH coefficient certificate")
    require(max(low,high)==low and (2130706433**6)//(2**128)-low==6067219606307729,
            "independent field reserve and maximum")
    for j,edge in ((8,24537),(9,28916),(10,33734)):
        for k,expected in ((edge,True),(edge+1,False)):
            require((30*(k-11+j)<=j*(k+67466)) == expected, "direct rank gate")
    upper = falling(67476,10)*(67466+11*24990)
    require(10**11*upper < scaled_basis(25000), "actual large-fiber upper below unguarded product")
    for numerator,denominator,correct in ((low_num,low_den,low-near),(high_num,high_den,high-near)):
        for wrong in (correct-1,correct+1):
            try:
                floor_certificate(numerator,denominator,wrong)
            except ValueError:
                continue
            raise ValueError("accepted corrupt integer floor")
    print("PASS independent scaled-integer LOW",low,"HIGH",high,"and four rejected wrong floors")
    print("All density-restricted sources on J=23000..29999; not a whole-interval payment")


if __name__ == "__main__":
    main()
