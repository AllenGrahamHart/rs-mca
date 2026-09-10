"""Complete-core PACK fixture showing why original anchor factors must stay."""

def need(ok, why):
    if not ok:
        raise ValueError(why)


def main():
    domain = set(range(9))
    locator = lambda x: x*(x-1)
    second_union = {0, 1, 5, 6, 7, 8}
    receiver = {x: locator(x) if x in second_union else 0 for x in domain}
    unions = [{x for x in domain if receiver[x] == c*locator(x)} for c in (0, 1)]
    need(unions == [{0, 1, 2, 3, 4}, second_union], "actual complete joint cores")
    need(unions[0] & unions[1] == {0, 1}, "one common original annihilator root set")
    masses = [len(u)-3+1 for u in unions]
    need(masses == [3, 4] and sum(masses) == 9-3+1, "PACK equality")
    need(sum(map(len, unions)) > 9+1, "dropping the prior anchor root breaks the union estimate")
    need(all(0 in u for u in unions), "common anchor")
    print("PASS original H_a*g root set and sharp compression PACK fixture")
    print("This checks core geometry only, not a full-code-bad MCA realization")


if __name__ == "__main__":
    main()
