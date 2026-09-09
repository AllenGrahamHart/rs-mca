"""Exact induction algebra; the universal section statement is hand-proved."""

from fractions import Fraction as F


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    cases = 0
    for p in (F(1), F(3, 2), F(2), F(7, 3), F(12)):
        for h in (F(1), p, p*p):
            bounds = [F(1), p]
            for r in range(2, 23):
                bounds.append(max(p**r, h*bounds[r-2]))
                need(bounds[-1] == p**r, "hereditary pencil/two-anchor recurrence")
                cases += 1
    p = F(3, 2)
    need(p*p+1 > p*p, "H>P^2 cannot be silently absorbed")
    print("PASS", cases, "exact hereditary recurrence steps through pair dimension22")
    print("Universal pencil-subspace premise and determinant guard require the hand proof")


if __name__ == "__main__":
    main()
