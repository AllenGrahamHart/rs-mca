"""Independent integer and direct-Cauchy audit, with no primary imports."""


def check(ok, label):
    if not ok:
        raise RuntimeError(label)


def verify():
    C, budget = 23067643444721720934, 274980728111395087
    low_weight, high_weight, labels, near = 11, 1200, 981205, 134944
    check(high_weight - low_weight == 1189, "pointwise resource conversion")
    check(12*102*(67473-11*102) > 1200*67473, "Bernoulli HIGH lower bound")
    check(67472 > 121 and 67473 > 14400, "LOW and monotonicity guards")

    # Reconstruct the dimension polynomial from weighted monomial sums.
    counts, degrees = 0, 0
    for i in range(9):
        counts += i+1
        degrees += i*(i+1)
    check((counts, degrees) == (45, 240), "entire kernel coefficients")
    mc = sum(i+1 for i in range(5))
    md = sum((i+4)*(i+1) for i in range(5))
    constant = (counts-mc)*67371 + degrees-md - 1048576
    slope = counts-mc-degrees+md-1
    check((constant, slope) == (972694, -111), "independent surplus")
    check(constant + slope*8763 == 1 and constant + slope*8764 == -110,
          "strict integer endpoint")

    # Exclude 4623 directly by Cauchy, not a rounded Johnson quotient.
    m, a0, s0, e = 4623, 67973, 2099558, 2720
    check(2*(m-3)*a0-(1895038+4381)-3*(m-1)*e > 0,
          "direct defect-g monotonicity")
    check(2*(m-4)*a0-1827666-4*(m-1)*e > 0,
          "direct height monotonicity")
    linear = (6*m-7)*a0-(m+2)*s0
    quadratic = 9*m-7*(m+2)
    check(quadratic == 9232 and linear+2*quadratic*e < 0,
          "direct parameter-degree monotonicity")
    a, s = a0+3*e, s0+7*e
    violation = m*a*a-s*(a+(m-1)*e)
    check(violation > 0 and (m-1)*a*a-s*(a+(m-2)*e) <= 0,
          "4623 excluded; integer floor 4622")
    lower = (6**20 * (2*1044196)**2) // (2**15 * 3**7 * 62991**2)
    check(lower == 56078104495, "independent finite-lift division")
    check(43046721*27*27 == 3**22, "original-degree component count")
    component = 4622*43046721+lower+1
    check(component == 255040048958, "all cubic components")

    pair_caps = [component, 80530893115, 163774741769, 73222472421,
                 6, 3*696, 127031877504+696]
    for d in range(12):
        if d in (7, 10):
            continue
        h = 0 if d in (0, 11) else 8762 // (10 // (11-d))
        r = (d+2)//3
        pair_caps.append(2**d*3**(22-d-r)*(1048577-h)**r // (67372-h)**r)
    low7 = 128 * 531441 * 1047977**3 // 66772**3
    check(low7 == 262988722817, "independent low-height cubic cap")
    pair_caps.append(low7)
    biggest = 255637083438792239
    for cap in pair_caps:
        low_labels = labels*(cap+64)
        num = C+(high_weight-low_weight)*low_labels
        selected, rem = divmod(num, high_weight)
        check(0 <= rem < high_weight, "integer label floor")
        biggest = max(biggest, selected+near)
    check(biggest == 274903465748372176, "independent complete ledger")
    check(budget-biggest == 77262363022911 and 8763-8655 == 108,
          "positive reserve and 108 new J values")
    print("PASS: independent kernel, direct 4623 exclusion, nonpure lift and resource ledger")
    print("Finite arithmetic is not an external hand audit of the universal geometry")


if __name__ == "__main__":
    verify()
