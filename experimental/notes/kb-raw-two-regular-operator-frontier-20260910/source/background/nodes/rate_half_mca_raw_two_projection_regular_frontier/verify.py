"""Finite rank/codimension exhaustion; the normal theorem is a hand-proof input."""


def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    remaining = []
    for rank in range(19, 23):
        codimension = 22-rank
        degrees = [d for d in range(1, 11) if d+2 <= codimension]
        need(degrees == ([1] if rank == 19 else []), "exhaustive deficient degrees")
        remaining.append(codimension)
    need(remaining == [3, 2, 1, 0], "regular finite exception bounds")
    caps = (274462040894062110, 256541462574529459, 252214244730017023)
    total = max(caps)
    need(total == 274462040894062110 and 274980728111395087-total == 518687217332977,
         "maximum of alternative entire-source payments")
    print("PASS rank19 deficient degree1 only; ranks20..22 no deficient full-carrier case")
    print("PASS whole-source maximum", total, "regular exception maxima", remaining)
    print("No finite matrix sampling proves the universal polynomial-projection dichotomy")


if __name__ == "__main__":
    main()
