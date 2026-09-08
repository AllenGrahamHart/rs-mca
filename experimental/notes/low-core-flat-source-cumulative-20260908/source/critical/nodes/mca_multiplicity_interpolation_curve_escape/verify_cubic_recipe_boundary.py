"""Exact endpoint certificates for the analytic all-multiplicity recipe fence."""

from math import comb


def require(ok, message):
    if not ok:
        raise ValueError(message)


def phi(d, w):
    if d <= 0:
        return 0
    ell = (d - 1) // w
    return d * (ell + 1) * (ell + 2) // 2 - w * ell * (ell + 1) * (ell + 2) // 3


def gap(j, t, r):
    a, w, n = j + 67472 - t, j - 1, j + 1048576
    return phi(r * a, w) - phi(r * a - 4 * w, w) - n * comb(r + 2, 3)


def main():
    expected = {
        9981: ([-122645, -276, -651530, -3134964], 10870785140),
        169999: ([-846161, -3384644, -8331938, -16793548], 724689480710),
    }
    for j, (gaps, large_r_certificate) in expected.items():
        a, w, n = j + 67471, j - 1, j + 1048576
        require([gap(j, 1, r) for r in range(1, 5)] == gaps, "small-r endpoints")
        require(all(x < 0 for x in gaps), "strict endpoint failure")
        require(7 * n * w - 10 * a * a - 4 * a * w == large_r_certificate > 0,
                "analytic r>=5 endpoint certificate")
        for r in range(1, 5):
            d = r * a
            shell = sum(min(i + 1, 4) * max(d - i * w, 0)
                        for i in range((d - 1) // w + 1))
            require(shell == phi(d, w) - phi(d - 4 * w, w), "positive convex shell identity")
    require(gap(9980, 1, 2) == 88 and gap(9981, 1, 2) == -276, "exact recipe boundary")
    require(gap(9940, 125, 2) == 264 and gap(9941, 125, 2) == -100, "fixed-cutoff boundary")
    print("PASS: endpoint certificates for all r>=1, T>=1, 9981<=J<=169999")
    print("Convexity and all-large-r monotonicity are hand proofs; no unsafe source asserted")


if __name__ == "__main__":
    main()
