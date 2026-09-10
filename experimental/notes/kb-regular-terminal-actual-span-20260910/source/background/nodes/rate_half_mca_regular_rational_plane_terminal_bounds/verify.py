"""Finite source gates and rational-plane terminal envelopes; no universal cover."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE = Path(__file__).resolve().parent
NODES = NODE.parent
R, D, E, S, ANCHORS, THRESHOLD = 1048576, 67472, 21499, 1048577, 8, 349525
BUDGET, GATE_BUDGET, NEAR = 274980728111395087, 270000000000000000, 134944
W44 = 581590844909990298
SOURCE_PIN = "09a677b5f91a9abca6ace7e07dfbf7ab4f386905cec8e3f3551933007b027f68"
RANGES = [(9965,10964),(10965,11964),(11965,12964),(12965,13364),
          (13365,13964),(13965,14964),(14965,15964),(15965,16964),
          (16965,17964),(17965,18964),(18965,19964),(19965,20964),(20965,21499)]


def need(ok, why):
    if not ok:
        raise ValueError(why)


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fraction(value):
    value = Q(value)
    return [str(value.numerator), str(value.denominator)]


def ceiling(value):
    return -(-value.numerator//value.denominator)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def build():
    compiler_path = NODES/"list_padded_johnson_dimension_descent/compiler.py"
    compiler = load("rational_plane_list", compiler_path)
    source_path = NODES/"rate_half_mca_coupled_pair_rank_frontier/source_certificate.json"
    source_bytes = source_path.read_bytes()
    need(digest(source_bytes)==SOURCE_PIN, "unchanged source-box certificate")
    masses = {row["low"]:row["mass_floor"] for row in json.loads(source_bytes)["boxes"]}
    calls = 0

    def cap(r,w,k,s):
        need(1<=w<=r and 1<=s<=k and 2130706433**6>=r+k, "LIST corridor")
        answer, trace = compiler.compile_cap(r,w,k,s)
        return answer,[list(x) for x in trace]

    base = Q(W44,44)+R+E+NEAR+Q(43*S**11*10**10,44*11**11*(D-42)**10)
    profiles = []
    for low, high in RANGES:
        on,on_trace = cap(R-567501,D-43,high,11)
        def gate_price(g,h):
            off,trace = cap(g-high,D-42-h-high,high,11)
            if h==0:
                price = Q(W44+43*(g*on+981147*off),44)+NEAR+1
            else:
                price = base+Q(43*981147*off,44)
            return price,trace

        ranges = [(0,0)]+[(h,min(h+199,(high-ANCHORS-1)//2))
                          for h in range(1,(high-ANCHORS-1)//2+1,200)]
        heights = []
        for h0,h1 in ranges:
            left,right = (567500 if h0==0 else 250000),981147
            while right-left>1:
                mid=(left+right)//2
                if gate_price(mid,h1)[0]<=GATE_BUDGET:
                    left=mid
                else:
                    right=mid
            g=left
            price,trace=gate_price(g,h1)
            need(ceiling(price)<=GATE_BUDGET and g+1<R-D+1, "paid useful pencil gate")
            entry=dict(height=[h0,h1],gate=g,off_trace=trace,price=ceiling(price),cutoffs={})
            for t in (1,2):
                sh=S-h0
                lower,upper=D-h1+1-t,sh-g-1
                need(0<lower<=THRESHOLD<sh and lower<=upper and 3*(THRESHOLD+1)>sh,
                     "positive full mass corridor and two large fibres")
                small,large=[],[]
                for first,last,out in ((lower,min(THRESHOLD,upper),small),
                                       (THRESHOLD+1,upper,large)):
                    for ell in range(first,last+1,5000):
                        end=min(ell+4999,last)
                        bound,_=cap(end+2*h1-1,D+h0-t,high-ANCHORS-h0,2)
                        calls+=1
                        out.append((ell,bound))
                alpha=max([Q(0)]+[Q((sh-ell)*bound,ell) for ell,bound in small])
                beta=max([Q(0)]+[Q((sh-ell)*bound)-alpha*ell for ell,bound in large])
                inside=t if h0==0 else R+high
                terminal=inside+sh*alpha+2*beta
                entry["cutoffs"][str(t)]=dict(alpha=fraction(alpha),beta=fraction(beta),
                                              terminal=fraction(terminal),boxes=len(small)+len(large))
            heights.append(entry)
        terminals=[max(Q(*map(int,h["cutoffs"][str(t)]["terminal"])) for h in heights) for t in (1,2)]
        factors=[prod(Q(R+j,D-t+j) for j in range(1,9)) for t in (1,2)]
        price=int(Q(masses[low],3)+factors[0]*terminals[0]/2+factors[1]*terminals[1]/6)+NEAR
        need(price<BUDGET, "rational-plane profile fits available weighted envelope")
        profiles.append(dict(schema="regular-rational-plane-profile-v1",J=[low,high],
                             on_trace=on_trace,mass_floor=masses[low],heights=heights,
                             terminals=[fraction(x) for x in terminals],
                             weighted_envelope=price,reserve=BUDGET-price))
    index=dict(schema="regular-rational-plane-terminals-v1",J=[9965,E],rank=19,anchors=8,
               terminal_pair_dimension=3,pencil_plane_dimension=2,raw_cutoffs=[1,2],
               W44=W44,B_star=BUDGET,near=NEAR,threshold=THRESHOLD,large_fibres_max=2,
               source_certificate_sha256=SOURCE_PIN,compiler_sha256=digest(compiler_path.read_bytes()),
               all_terminals_covered=False,original_source_closed=False,prize_closed=False,
               profiles=[],mass_boxes=calls,maximum_envelope=max(p["weighted_envelope"] for p in profiles))
    return profiles,index


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    profiles,index=build()
    folder=NODE/"certificates"
    if args.write:
        folder.mkdir(exist_ok=True)
    for profile in profiles:
        filename=str(profile["J"][0])+".json"
        encoded=(json.dumps(profile,indent=2)+"\n").encode()
        path=folder/filename
        if args.write:
            need(not path.exists(),"refuse frozen profile replacement")
            path.write_bytes(encoded)
        need(path.read_bytes()==encoded,"exact frozen profile")
        index["profiles"].append(dict(path=filename,sha256=digest(encoded)))
    path=folder/"index.json"
    encoded=(json.dumps(index,indent=2)+"\n").encode()
    if args.write:
        need(not path.exists(),"refuse frozen index replacement")
        path.write_bytes(encoded)
    need(path.read_bytes()==encoded,"exact frozen index")
    print("PASS",len(profiles),"J profiles;",sum(len(p["heights"]) for p in profiles),"height gates;",
          index["mass_boxes"],"mass boxes;",2*index["mass_boxes"],"two-step LIST transitions")
    print("MAX WEIGHTED ENVELOPE",index["maximum_envelope"],"RESERVE",BUDGET-index["maximum_envelope"])
    print("INDEX",digest(encoded))
    print("Only rank-two rational-pencil-plane terminals; whole constant pencils and general terminals remain open")


if __name__=="__main__":
    main()
