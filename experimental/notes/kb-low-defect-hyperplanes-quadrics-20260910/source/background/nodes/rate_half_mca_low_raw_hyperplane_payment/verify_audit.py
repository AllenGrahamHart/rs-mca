"""Independent integer-only reconstruction; no primary or compiler imports."""


def need(ok, message):
    if not ok:
        raise ValueError(message)


def product(values):
    out = 1
    for value in values:
        out *= value
    return out


def main():
    R, d, cap, W, near = 1048576, 67472, 274980728111395087, 613022127444579907, 134944
    numerator = product(R+10-i for i in range(11))
    denominator = 11*(d+8)*product(d-2+j for j in range(1, 10))
    M, rem = divmod(numerator, denominator)
    need(M == 78301130139301820 and 0 <= rem < denominator, "auxiliary low floor")
    need(numerator >= M*denominator and numerator < (M+1)*denominator, "two floor inequalities")
    for J in (9965, 21499):
        pair_numerator, pair_denominator = 1, 1
        n, A, s, r = R+J, d+J-2, 11, 22
        for step in range(11):
            need(r == 2*s and r > s > 0, "every rank guard holds")
            bad = J+s-r
            need(A > bad and (n-bad, A-bad) == (R+s, d-2+s), "original coordinate factor")
            pair_numerator *= n-bad
            pair_denominator *= A-bad
            r, s = r-2, s-1
        need((r, s) == (0, 0), "point terminal")
        pair = pair_numerator//pair_denominator
        need(pair == 12763910835039, "unrestricted low-pair cap")
    # Discrete monotonicity is linear after clearing the positive denominators.
    for k in (10, 21499):
        lhs = (R+k+1)*(d+k-2)
        rhs = (R+k-10)*(d+k-1)
        need(rhs-lhs == R+k-10-11*(d+k-2) > 0, "endpoint monotonicity identity")
    need((R+10-10-11*(d+10-2))-(R+21499-10-11*(d+21499-2)) == 10*(21499-10),
         "whole-interval linear decrease")
    priced = (W+2*M+2*pair)//3+near
    need(priced == 256549971848419485 and priced < cap, "original full-source payment")
    need((W+2*M)//3+near == 256541462574529459, "proper carrier payment")
    want = 3*(cap-near+1)-W-2*(M+pair)
    outside = -((-want)//2)
    need(outside == 27646134394463404 and 2*(outside-1) < want <= 2*outside,
         "sharp integer consequence of the proved envelope")
    need((W+2)//3+near <= priced, "vertical or singleton case")
    need(2*(M+pair) == 156627788100273718 and W+2*(M+pair) == 769649915544853625,
         "integral deficit and price constants")
    print("PASS independent guarded anchors, decreasing auxiliary quotient and exact integer floors")
    print("GRAPH", priced, "RESERVE", cap-priced, "OUTSIDE_MIN", outside)
    print("No primary imports; source normalization, tuple transport and ownership require the hand proofs")


if __name__ == "__main__":
    main()
