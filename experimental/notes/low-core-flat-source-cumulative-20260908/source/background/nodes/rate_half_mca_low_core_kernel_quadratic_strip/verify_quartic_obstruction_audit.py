"""Independent coefficient subtraction and integer factor-accounting audit."""


def audit():
    # Compute the linear J-coefficients of the monomial spaces directly.
    full = [0, 0]
    multiple = [0, 0]
    for degree in range(9):
        full[0] += (degree+1)*(1-degree)
        full[1] += (degree+1)*(66972+degree)
    for degree in range(4):
        shift = degree+5
        multiple[0] += (degree+1)*(1-shift)
        multiple[1] += (degree+1)*(66972+shift)
    assert (full[0]-multiple[0]-1, full[1]-multiple[1]-1048576) == (-136, 1295614)
    assert 696*80794384 <= 744400*75628 < 697*80794384
    assert 585*45770704 <= 26776570248 < 586*45770704
    # Monotonicity uses positive coefficients, not just endpoint samples.
    assert 592000-16*9525 == 439600 > 0
    assert 16*9525-2*66973 == 18454 > 0
    assert 466101-16*9525 > 0 and 57448-9525 > 0
    n, a, c = 466101, 66973, 9525
    assert 586*a*a > n*(a+585*c)

    budget = 2130706433**6//2**128
    base = 4194116990084347
    label = 981604
    cubic_pairs = 275860269762
    assert base+label*(cubic_pairs+64) == 274979661292365251
    cubic_line = base+label*(cubic_pairs+64+696)
    assert cubic_line == 274979661975561635
    assert budget-cubic_line == 1066135833452
    two_conics = base+label*(254063755008+64)
    assert two_conics == 253584115223779835 < cubic_line
    assert base+label*(12+64) < two_conics
    assert 9526 < 2130706433 and 4*3 == 12
    print("PASS: independent kernel coefficients, line ceilings and resource-once ledger")


if __name__ == "__main__":
    audit()
