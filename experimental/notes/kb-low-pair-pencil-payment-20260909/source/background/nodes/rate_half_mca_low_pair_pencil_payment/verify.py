"""Generate or replay the bounded exact low-pair pencil certificate."""

import argparse
import hashlib
import importlib.util
from fractions import Fraction as F
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
ROOT = NODE.parents[2]
R, GAP, LO, HI, CUT, X = 1048576, 67472, 9965, 21499, 16, 5000
NEAR, BUDGET, TOTAL = 134944, 274980728111395087, 274136923022229951
MANIFEST = NODE/"certificate/manifest.json"
COMPILER = ROOT/"background/nodes/list_padded_johnson_dimension_descent/compiler.py"


def need(ok, message):
    if not ok:
        raise ValueError(message)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def basis():
    d = GAP-CUT
    c = F(1, 2*(d+2))
    a, b = d*(2*d+1)*c, (3*d+1)*c
    for rank in range(4, 12):
        need(b >= d*c, "input contraction gate")
        alpha, delta, h = F(rank-2, rank-1), F(1, rank-1), d+rank-1
        f = a+b*(rank-1)+c*(rank-1)**2
        s1, s0 = b-2*c+f/h, a-b+c-(rank-1)*f/h
        u3 = c*alpha**2/h
        u2 = (b*alpha+2*c*alpha*delta+d*c*alpha**2)/h
        u1 = (a+b*delta+c*delta**2+d*(b*alpha+2*c*alpha*delta))/h
        u0 = d*(a+b*delta+c*delta**2)/h
        need(u2 >= c and u3 >= 0, "nonnegative squared remainder")
        t1 = u1+2*(u2-c)*X+3*u3*X*X
        t0 = u0-(u2-c)*X*X-2*u3*X**3
        shift = max(F(0), t0+t1*rank-s0-s1*rank, t0+t1*HI-s0-s1*HI)
        a, b = t0-shift, t1
        need(min(a,b,c) > 0 and b >= d*c, "positive next certificate")
        need(all(a+b*k <= s0+s1*k for k in (rank, HI)), "whole spike branch")
    q = lambda j: a+b*j+c*j*j
    p, pd = prod(d+i for i in range(1,11)), prod(GAP+i for i in range(1,11))
    beta = lambda j: 12*p*q(j)
    need(GAP*b >= a and 187*(GAP+HI)*pd >= 3*beta(HI), "all-HIGH gate")
    need(17*(GAP+HI)*pd < 3*beta(HI), "baseline HIGH is insufficient")
    need((b+2*c*LO)*(R+LO-11) > 12*q(HI), "whole-J decreasing resource ratio")
    r0 = F(prod(R+LO-i for i in range(12)))/beta(LO)
    need(int(r0) == 613022127444579907 and r0.denominator > 1, "unrounded source ratio")
    return r0


def metadata(r0):
    return {
        "kind": "low-pair-pencil-tuple-refund-v1",
        "parameters": {"R":R,"d":GAP,"J_min":LO,"J_max":HI,"core_cutoff":CUT,
                       "mass_truncation":3,"pair_cutoff":2,"width":1000,"dimension":10},
        "R0": [str(r0.numerator), str(r0.denominator)],
        "compiler_sha256": hashlib.sha256(COMPILER.read_bytes()).hexdigest(),
        "claimed_ceiling": TOTAL,
        "status": "exact integer inequalities; no field enumeration or source-census premise",
    }


def rows():
    compiler = module("credited_padded_list", COMPILER)
    for left in range(0, R-GAP+1, 1000):
        right = min(left+999, R-GAP)
        caps = []
        for t in (1,2):
            cap, trace = compiler.compile_cap(R-left, GAP-t, HI-1, 10)
            need(cap == trace[-1][2], "final LIST cap")
            caps.append({"t":t, "trace":[list(step) for step in trace]})
        yield {"a":left,"b":right,"caps":caps}


def envelope(row, r0, refunded=True):
    left, right = row["a"], row["b"]
    n, m = R+LO, GAP+LO
    fraction = 1-F(prod(n-right-i for i in range(12)), prod(n-i for i in range(12))) if refunded else 1
    result = 1+NEAR+r0*fraction/3
    for cap in row["caps"]:
        t, value = cap["t"], cap["trace"][-1][2]
        result += F(right*(n-left)*value, (m-t)*t*(t+1))
    return result


def ceil(value):
    return -(-value.numerator//value.denominator)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    need(BUDGET == 2130706433**6//2**128 and NEAR == 2*GAP, "original field and near")
    need(11 <= LO <= HI < GAP-CUT and 187 == 11*(CUT+1), "source and HIGH cutoffs")
    r0 = basis()
    shards = module("sharded_result", ROOT/"tools/sharded_result.py")
    if args.write:
        with shards.ShardedResultWriter(MANIFEST.parent, metadata=metadata(r0), shard_records=128) as writer:
            for row in rows():
                need(envelope(row,r0) < BUDGET, "refunded box exceeds budget")
                writer.add(row)
        print("WROTE", MANIFEST.relative_to(ROOT), flush=True)
    counts = shards.verify(MANIFEST)
    need(counts["records"] == 982 and counts["shards"] == 8, "complete interval inventory")
    need(shards.load_manifest(MANIFEST)["metadata"] == metadata(r0), "certificate input pins")
    maximum, where, plain, transitions = F(0), None, F(0), 0
    for frozen, expected in zip(shards.iter_records(MANIFEST), rows(), strict=True):
        need(frozen == expected, "frozen selected certificates differ")
        value = envelope(frozen,r0)
        need(value < BUDGET, "every box paid")
        if value > maximum:
            maximum, where = value, (frozen["a"],frozen["b"])
        plain = max(plain,envelope(frozen,r0,False))
        transitions += sum(len(cap["trace"]) for cap in frozen["caps"])
    need(ceil(maximum) == TOTAL and where == (103000,103999), "exact envelope maximum")
    need(BUDGET-TOTAL == 843805089165136 and transitions == 19640, "reserve and transitions")
    small = ceil(r0/3+(R-GAP+2)+NEAR)
    need(small < TOTAL and 228260637755610995 < TOTAL, "small union and nonconstant pencil")
    need(plain > BUDGET, "dropping the coupled refund loses this recipe")
    print("PASS eight basis certificates; all-HIGH187 and unrounded R0",int(r0))
    print("PASS",counts,"LIST transitions",transitions)
    print("PENCIL",TOTAL,"AT",where,"RESERVE",BUDGET-TOTAL,"SMALL",small)
    print("UNREFUNDED RECIPE",ceil(plain),"not a no-go theorem")
    print("All low-pair pencils paid; function-field-rank-two families and both Prizes remain open")


if __name__ == "__main__":
    main()
