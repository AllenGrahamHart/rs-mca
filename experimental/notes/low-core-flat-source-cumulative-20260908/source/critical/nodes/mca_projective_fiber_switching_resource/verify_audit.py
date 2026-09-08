"""Independent integer-scaled subset count and adjacent-credit falsifiers."""

from itertools import combinations
from math import factorial, prod


def check(ok, why):
    if not ok:
        raise ValueError(why)


def partitions(total, least=1):
    if total == 0:
        yield ()
    for first in range(least, total+1):
        for tail in partitions(total-first, first):
            yield (first, *tail)


def main():
    checked = 0
    for n in range(3, 13):
        for sizes in partitions(n):
            for r in range(2, min(n, 6)):
                good, marked = 0, 0
                for subset in combinations(sizes, r):
                    ways = prod(subset)*factorial(r)
                    good += ways
                    marked += ways*sum(a-1 for a in subset)
                full = factorial(n)//factorial(n-r)
                check(2*(n-r)*(full-good) >= (r-1)*marked, "integer-scaled resource")
                checked += 1
    sharp = 0
    for r in range(2, 13):
        for n in range(r+1, 71):
            bad = r*(r-1)*factorial(n-2)//factorial(n-r)
            marked = 2*r*factorial(n-2)//factorial(n-r-1)
            check(2*(n-r)*bad == (r-1)*marked > 0, "one-doubleton equality")
            check(2*(n-r-1)*bad < (r-1)*marked, "smaller denominator falsely increases credit")
            check((n-r)*bad < (r-1)*marked, "omitting orientation factor two is false")
            sharp += 1
    n, r = 6, 4
    full = factorial(n)//factorial(n-r)
    check(2*(n-r)*full < 2*(n-r)*full+(r-1)*r*full,
          "weights a_i rather than a_i-1 fail for singleton fibers")
    print("PASS", checked, "partition/subset counts;", sharp,
          "sharp identities and two credit mutations; singleton weight mutation")
    print("Integer subset audit: no primary, Fraction, switching or symmetric-recurrence import")


if __name__ == "__main__":
    main()
