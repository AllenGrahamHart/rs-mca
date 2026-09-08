"""Exact short-block certificate; the universal scope extension is in proof.md."""

import argparse
import hashlib
import importlib.util
from math import prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PATH = ROOT / "critical/nodes/rate_half_mca_quotient_density_interval/verify.py"
SPEC = importlib.util.spec_from_file_location("quotient_costs", PATH)
c = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(c)
BLOCKS = ((30000, 30199), (30200, 30799), (30800, 31999))
EXPECTED = (274471852330442343, 273508821582726287, 270145570079495459)
DIGESTS = (
    "2b555595910fe4bea323f0a7719a9cc935939079cddbdfb2dff503bdcc202a17",
    "c39f56ccb137b9e734c9d9e947cfc08015382b13d9b687e2c71b5b7829321f58",
    "0dcac2746597fd792431d53a4977930503028c0eca571062affc3598ca4ea3c4",
)


def verify_cover(blocks):
    previous = 29999
    for lo,hi in blocks:
        c.need(lo == previous+1 and lo <= hi, "consecutive nonempty degree blocks")
        previous = hi
    c.need(previous == 31999, "complete refined interval")


def verify_mutations():
    verify_cover(BLOCKS)
    changes = (BLOCKS[1:], ((30001,30199),)+BLOCKS[1:],
               ((30000,30198),)+BLOCKS[1:], BLOCKS+(BLOCKS[-1],),
               BLOCKS[:-1]+((30800,31998),))
    for wrong in changes:
        try:
            verify_cover(wrong)
        except ValueError:
            continue
        raise ValueError("accepted a broken degree cover")
    print("PASS five degree-cover mutations",flush=True)


def run(lo, hi):
    c.need(14000 <= lo <= hi <= 39999, "scope of the extended box proof")
    total = prod(c.R+hi-i for i in range(12))
    high = (c.GAP+lo)*prod(c.GAP+i for i in range(1,11))*10488//125
    low = prod((lo+c.D)*11-i*lo for i in range(11))//11**11
    maximum = total//min(high,12*low)+c.NEAR
    where, costs_seen, sources_seen = ("low-density",), 0, 0
    digest = hashlib.sha256()
    for j in range(1,11):
        for r in range(j,11):
            for u in range(8):
                data = c.source_data(lo,hi,j,r,u)
                costs = [min(high,c.core_cost(data,j,v)) for v in range(64)]
                for v,cost in enumerate(costs):
                    digest.update(f"C:{lo},{hi},{j},{r},{u},{v}:{cost}\n".encode("ascii"))
                costs_seen += 64
                scale = data[0]
                aa,ab = c.size(lo,j,r,u+1,scale),c.size(hi,j,r,u+1,scale)
                for v in range(8):
                    den = 16*j
                    k0,k1,light = (2*j-1)*8+v,(2*j-1)*8+v+1,(2*j-1)*8-v
                    bl = min(costs[:min(64,light*64//den+1)])
                    bh = min(costs[max(0,k0*64//den-1):min(64,c.ceildiv(k1*64,den)+1)])
                    numerator = ((c.R+lo)*scale-aa)*den*c.CHILD[j]
                    denominator = (c.GAP+lo)*scale*den-k1*aa
                    en,ed = (den-k0)*ab,den*scale
                    child = c.ceildiv(numerator*ed+en*denominator,denominator*ed)
                    cap = (total+max(0,bl-bh)*child)//bl+c.NEAR
                    digest.update(f"S:{lo},{hi},{j},{r},{u},{v}:{cap}\n".encode("ascii"))
                    sources_seen += 1
                    if cap > maximum:
                        maximum,where = cap,(j,r,u,v)
        print("PREFIX",lo,hi,"rank",j,"cap",maximum,"at",where,flush=True)
    c.need(costs_seen == 28160 and sources_seen == 3520,"complete box inventory")
    index = BLOCKS.index((lo,hi))
    c.need(maximum == EXPECTED[index],"frozen block maximum")
    c.need(digest.hexdigest() == DIGESTS[index],"every record cost and source bound")
    c.need(max(maximum,248408859318207582) < c.BUDGET,"all source classes below budget")
    print("BLOCK",lo,hi,"maximum",maximum,"where",where,
          "digest",digest.hexdigest(),flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start",type=int,choices=[lo for lo,hi in BLOCKS])
    args = parser.parse_args()
    c.need((c.R,c.GAP,c.D,c.C,c.NEAR,c.BUDGET) ==
           (1048576,67472,67466,67467,134944,2130706433**6//2**128),"exact row and gap")
    verify_mutations()
    c.need(c.APARTS == 8 and c.OCC == 64 and c.HEAVY == 8,"inherited fixed grids")
    c.need(84*125*(c.GAP+1-77) > 10488*(c.GAP+1) and c.GAP+1 > 12*84,"HIGH gate")
    for lo,hi in BLOCKS:
        if args.start is None or args.start == lo:
            run(lo,hi)
    c.need(max(EXPECTED) > 248408859318207582,"include the prior large-fiber class")
    c.need(max(EXPECTED) < 274929007493481160 < c.BUDGET,"whole-source union")
    c.need(c.BUDGET-max(EXPECTED) == 508875780952744,"new interval reserve")
    if args.start is not None:
        print("PARTIAL replay: only block starting",args.start,"was replayed")
    print("PASS: fixed certificate; hand proofs and original-source transport remain separate")
