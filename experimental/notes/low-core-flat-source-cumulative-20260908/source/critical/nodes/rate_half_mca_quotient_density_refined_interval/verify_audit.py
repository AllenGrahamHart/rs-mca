"""Independent inherited cost engine and rational source accounting."""

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT / "critical/nodes/rate_half_mca_quotient_density_interval/verify_audit.py"
SPEC = importlib.util.spec_from_file_location("independent_quotient_costs",PATH)
a = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(a)
CERTIFICATES = (
    (30000,30199,274471852330442343,"2b555595910fe4bea323f0a7719a9cc935939079cddbdfb2dff503bdcc202a17"),
    (30200,30799,273508821582726287,"c39f56ccb137b9e734c9d9e947cfc08015382b13d9b687e2c71b5b7829321f58"),
    (30800,31999,270145570079495459,"0dcac2746597fd792431d53a4977930503028c0eca571062affc3598ca4ea3c4"),
)


def audit(lo,hi,expected,expected_digest):
    a.check(30000 <= lo <= hi <= 31999,"refined degree scope")
    total = prod(range(a.N0+hi-11,a.N0+hi+1))
    high = (a.GAP+lo)*prod(range(a.GAP+1,a.GAP+11))*10488//125
    density = prod((lo+a.DC)*11-i*lo for i in range(11))//11**11
    maximum = total//min(high,12*density)+134944
    digest = hashlib.sha256()
    records = sources = mutations = 0
    for j in range(1,11):
        for r in range(j,11):
            for u in range(8):
                costs = []
                for v in range(64):
                    value = min(high,a.cost(lo,hi,j,r,u,v))
                    costs.append(value)
                    digest.update(f"C:{lo},{hi},{j},{r},{u},{v}:{value}\n".encode("ascii"))
                    records += 1
                for v in range(8):
                    left = F((2*j-1)*8+v,16*j)
                    right = left+F(1,16*j)
                    light = 2-F(1,j)-left
                    light_end = (64*light).__floor__()
                    heavy_start = (64*left).__floor__()
                    heavy_end = (64*right).__ceil__()
                    bl = min(costs[i] for i in range(64) if i <= light_end)
                    bh = min(costs[i] for i in range(64) if i+1 >= heavy_start and i <= heavy_end)
                    size0 = F(a.endpoint(lo,j,r,u+1),a.UNIT)
                    size1 = F(a.endpoint(hi,j,r,u+1),a.UNIT)
                    q = (a.N0+lo-size0)*a.CAPS[10-j]/(a.GAP+lo-right*size0)+(1-left)*size1
                    child = q.__ceil__()
                    source = F(total+max(0,bl-bh)*child,bl)
                    floor = source.__floor__()
                    a.check(floor <= source < floor+1,"independent source floor")
                    for wrong in (floor-1,floor+1):
                        a.check(not wrong <= source < wrong+1,"wrong source floor accepted")
                        mutations += 1
                    value = floor+134944
                    digest.update(f"S:{lo},{hi},{j},{r},{u},{v}:{value}\n".encode("ascii"))
                    sources += 1
                    maximum = max(maximum,value)
        print("AUDIT PREFIX",lo,hi,"rank",j,"cap",maximum,flush=True)
    a.check((records,sources,mutations) == (28160,3520,7040),"entire independent inventory")
    a.check(maximum == expected,"independent maximum")
    a.check(digest.hexdigest() == expected_digest,"independent every-cost digest")
    print("AUDIT BLOCK",lo,hi,"cap",maximum,"DIGEST",digest.hexdigest(),
          "wrong-floor controls",mutations,flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start",type=int,choices=[x[0] for x in CERTIFICATES])
    args = parser.parse_args()
    a.check((a.N0,a.GAP,a.DC,a.CC) == (1048576,67472,67466,67467),"audit original corridor")
    a.check(CERTIFICATES[0][0] == 30000 and CERTIFICATES[-1][1] == 31999,"audit total interval")
    a.check(all(x[1]+1 == y[0] for x,y in zip(CERTIFICATES,CERTIFICATES[1:])),"audit adjacency")
    for row in CERTIFICATES:
        if args.start is None or args.start == row[0]:
            audit(*row)
    a.check(max(row[2] for row in CERTIFICATES) == 274471852330442343,"audit final maximum")
    a.check(248408859318207582 < 274471852330442343 < 274929007493481160,"audit class union")
    a.check(274980728111395087-274471852330442343 == 508875780952744,"audit reserve")
    if args.start is not None:
        print("PARTIAL audit: only block starting",args.start,"was replayed")
    print("PASS: independent exact replay, not certification of universal analytic coverage")
