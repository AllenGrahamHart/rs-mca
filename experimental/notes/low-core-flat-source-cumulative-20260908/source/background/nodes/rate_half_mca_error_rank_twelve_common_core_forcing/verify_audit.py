"""Independent even-multiplicity Johnson replay and decimal endpoint audit."""

from decimal import Decimal, localcontext


def root_ceiling(numerator, denominator):
    lo, hi = 0, 1
    while denominator*hi*hi < numerator:
        hi *= 2
    while hi-lo > 1:
        trial = (lo+hi)//2
        if denominator*trial*trial >= numerator:
            hi = trial
        else:
            lo = trial
    assert denominator*(hi-1)**2 < numerator <= denominator*hi*hi
    return hi


def main():
    checked = 0
    for k in range(2, 4801):
        n, a, degree = 1048576+k, 67472+k, k-1
        multiplicity = 2
        while 4*multiplicity*multiplicity*a*a < (2*multiplicity+1)**2*n*degree:
            multiplicity += 2
        sigma = 2*multiplicity+1
        length = root_ceiling(sigma*sigma*n*degree, 4)
        y_upper = root_ceiling(sigma*sigma*n, 4*degree)
        numerator, denominator = sigma*sigma*n, 12*degree
        z_upper, remainder = divmod(numerator, denominator)
        z_upper += remainder != 0
        z_upper = max(y_upper, z_upper)
        cap = 2*length*y_upper*y_upper*z_upper + (n-a+1)*y_upper + z_upper
        assert cap <= 100000000000000000
        checked += 1
    assert checked == 4799
    with localcontext() as context:
        context.prec = 100
        r, d, k, s = map(Decimal, (1048576, 67472, 255000, 11))
        n, m, h = r+k, d+k, k-s+2
        balanced = n*(2*n-h)/(m*(2*m-h))
        # Use the unsimplified one-large-fiber formula rather than the main code.
        w = k-s+1
        spike = (w*(n-w)/(m-w) + (n-w)*(n-1)/(m-1))/m
        u = Decimal(10755802499540570)
        cap = int(u*max(balanced, spike))
        assert cap == 273540953997732057
        num, den = 11153988094749115*int(u), 438581833089399
        assert den*cap <= num < den*(cap+1)
        assert cap+1048576+134944 == 273540953998915577
    print(f'PASS: independent even-multiplicity certificates for {checked} rows; '
          'binary root ceilings, unsimplified endpoint and exact floor audit')


if __name__ == '__main__':
    main()
