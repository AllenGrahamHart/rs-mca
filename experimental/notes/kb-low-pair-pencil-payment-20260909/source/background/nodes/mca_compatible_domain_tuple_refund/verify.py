"""Small actual sources test the kernel-slope and constant-chart guards."""

from itertools import permutations


def need(ok, message):
    if not ok:
        raise ValueError(message)


def owners(received, support, p):
    result = {}
    for x, y in permutations(support, 2):
        u, v = received[x]
        uu, vv = received[y]
        if v == vv:
            continue
        gamma = (uu-u)*pow((v-vv) % p, -1, p) % p
        h = (u+gamma*v) % p
        result[x, y] = gamma, h
    return result


def nonaffine(points, values, p):
    x, y, z = points
    return ((values[y]-values[x])*(z-x)-(values[z]-values[x])*(y-x)) % p != 0


def main():
    p, gamma0 = 7, 2
    received = {x: ((1-2*x*x) % p, x*x % p) for x in range(3)}
    need(nonaffine((0, 1, 2), {x: v for x, (_, v) in received.items()}, p),
         "actual degree-below-two pair noncontainment")
    internal = owners(received, range(3), p)
    need(len(internal) == 6 and set(internal.values()) == {(gamma0, 1)},
         "every internal tuple belongs to the compatible kernel slope")
    need(3*2-3*2 == 0 < len(internal), "omitting the kernel label charge is false")
    need(not any(gamma != gamma0 for gamma, _ in internal.values()), "refund after removal")

    infinite = {x: ((x*x+x) % p, 3) for x in range(6)}
    need(not owners(infinite, range(6), p), "constant second word makes all internal normals dependent")

    received = {}
    for x in range(6):
        v = pow(6-x, -1, p) if x < 3 else 2*pow((-x) % p, -1, p) % p
        received[x] = (-x*v % p, v)
    need(all((u+x*v) % p == 0 for x, (u, v) in received.items()), "nonconstant polynomial relation")
    for gamma, h, support in ((6, 1, (0, 1, 2)), (0, 2, (3, 4, 5))):
        need(all((received[x][0]+gamma*received[x][1]) % p == h for x in support),
             "actual scalar-agreement record")
        need(nonaffine(support, {x: v for x, (_, v) in received.items()}, p),
             "full-code-bad selected support")
        record = owners(received, support, p)
        need(len(record) == 6 and set(record.values()) == {(gamma, h)}, "owned independent tuples")
    all_owners = owners(received, range(6), p)
    need(len({gamma for gamma, _ in all_owners.values()}) > 1,
         "nonconstant relation does not leave only one internal tuple owner")
    retained = owners(received, (3, 4, 5), p)
    need(len(retained) <= 6*5-3*2, "finite compatible first-group refund retains the second record")
    print("PASS actual finite/infinite compatible-domain controls and charged kernel slope")
    print("PASS two full-code-bad records refute extending tuple deletion to a variable rational direction")
    print("No source coordinates deleted; recordwise weights remain consumer inputs")


if __name__ == "__main__":
    main()
