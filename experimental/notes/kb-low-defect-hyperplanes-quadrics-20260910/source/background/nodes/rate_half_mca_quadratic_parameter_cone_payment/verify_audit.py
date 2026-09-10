"""Independent integer-only cone ledger; inherited W0/W1 are proved inputs."""


def need(ok, message):
    if not ok:
        raise ValueError(message)


def multiply(values):
    result = 1
    for value in values:
        result *= value
    return result


def main():
    R, d, E, near, budget = 1048576, 67472, 21499, 134944, 274980728111395087
    for T, lo, W, expected, deficit, outside in (
        (3, 9965, 624373932788019251, 269692335594445840, 5288392516949247, 7051190022598997),
        (2, 14000, 522680876725222604, 274290004332197866, 690723779197221, 1036085668795833),
    ):
        num = 2*multiply(range(R+lo-10, R+lo+1))
        den = 11*(d+lo-T)*multiply(range(d-T+1, d-T+10))
        mass, remainder = divmod(num, den)
        need(0 <= remainder < den and mass*den <= num < (mass+1)*den, "both floor inequalities")
        for j in (lo, E):
            lhs = (R+j+1)*(d+j-T)
            rhs = (R+j-10)*(d+j+1-T)
            need(rhs-lhs == R+j-10-11*(d+j-T) > 0, "ratio identity and endpoint gate")
        need(10*(E-lo) > 0, "linear monotonicity minimum is the right endpoint")
        pn, pd, rank, shared = 1, 1, 22, 11
        for step in range(11):
            need(rank == 2*shared and rank > shared > 0, "all joint rank guards")
            bad = E+shared-rank
            pn *= R+E-bad
            pd *= d+E-T-bad
            rank, shared = rank-2, shared-1
        need((rank, shared) == (0, 0), "point child")
        pair = pn//pd
        exceptional = 21490+2*pair
        amount = W+T*(mass+exceptional)
        total = amount//(T+1)+near
        need(total == expected and budget-total == deficit > 0, "source-bound whole payment")
        target = (T+1)*(budget-near+1)-amount
        need(T*(outside-1) < target <= T*outside, "exact outside-label threshold")
        need((amount+T*(outside-1))//(T+1)+near == budget, "last safe recipe count")
        need((amount+T*outside)//(T+1)+near == budget+1, "next recipe count")
        print("PASS independent T", T, "MASS", mass, "PAIR", pair, "AMOUNT", amount, "TOTAL", total)
    print("Independent proof sources still required for W0/W1, cone tuple ownership and original normalization")
    print("No primary/compiler imports or claim that either envelope is attainable")


if __name__ == "__main__":
    main()
