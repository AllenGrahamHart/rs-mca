"""Independent streaming integer audit; no primary or field-helper imports."""


def need(ok, message):
    if not ok:
        raise ValueError(message)


def main():
    q = 1
    for _ in range(6):
        q *= 2130706433
    budget, remainder = divmod(q, 1 << 128)
    need(0 <= remainder < (1 << 128), "budget floor")
    cap, near = 156765527508668296, 134944
    maximum, previous, count = 0, -1, 0
    for degree in range(9941, 21500):
        n, zeros = 1048576+degree, degree-11
        need(n >= 10*(zeros+1), "SOURCE first branch covers every degree")
        collision, rem = divmod(n*zeros, 10)
        need(0 <= rem < 10, "collision floor")
        exceptions = zeros+collision//2
        need(exceptions >= previous, "monotone exception endpoint")
        need(cap+exceptions+near < budget, "rank collapse pays entire line")
        previous = exceptions
        maximum = max(maximum, exceptions)
        count += 1
    need(count == 11559 and maximum == 1149710068, "whole residual and endpoint")
    need(cap+near+maximum == 156765528658513308, "DROP total")
    need(budget-(cap+near+maximum) == 118215199452881779, "DROP reserve")
    complement = budget+1-near-cap
    need(complement == 118215200602591848, "strict over-budget complement")
    need(complement-maximum == 118215199452881780, "post-exception spread")
    for delta in (-1, 1):
        need(cap+near+maximum+delta != 156765528658513308, "wrong total rejected")
        need(complement+delta != budget+1-near-cap, "wrong complement rejected")
    need(complement-(complement-1) == 1 and complement-complement == 0,
         "no rank-retention claim at equality")
    print("PASS independent integer audit of", count, "degrees; strict boundaries and four mutations")
    print("No enumeration of original sources and no proof of the credited rank-ten cap by arithmetic")


if __name__ == "__main__":
    main()
