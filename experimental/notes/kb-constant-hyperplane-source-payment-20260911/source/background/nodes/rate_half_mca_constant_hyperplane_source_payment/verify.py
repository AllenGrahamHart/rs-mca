"""Freeze a bounded exact constant-hyperplane source proof, with JSONL degree shards."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from math import prod
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
R,D,S,BUDGET=1048576,67472,1048577,274980728111395087
SCOPE=dict(
    schema="constant-hyperplane-source-v1",field="2130706433^6",
    agreement=1116048,target_epsilon="2^-128",J=[9965,21499],
    original_error_rank=12,actual_P2_rank=19,shared_dimension=11,
    constant_dimension=10,constant_dimension11_excluded=True,
    normalization_cap_required=False,
    local_antecedent="after proved whole-source pencil alternatives are removed",
    degree_excess="zeta=E-(s-2)",shared_stages=[4,5,6,7,8,9,10,11],
    degree_band_width=2000,mass_box_width=5000,complement_box_width=10000,
    large_mass_threshold=349525,large_mass_count_max=2,
    original_weights=True,full_gcd_and_slack=True,near=134944,
    parent_index_sha256=PARENT_PIN,compiler_sha256=COMPILER_PIN,
    whole_constant4_penultimate_paid=False,unrestricted_rank19_paid=False,prize_closed=False,
)


def need(ok,why):
    if not ok:
        raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def rational(x):
    x=Q(x)
    return [str(x.numerator),str(x.denominator)]


def decode(x):
    return Q(*map(int,x))


def index_bytes(x):
    return (json.dumps(x,indent=2)+"\n").encode()


def lines_bytes(rows):
    return ("\n".join(json.dumps(row,sort_keys=True,separators=(",",":")) for row in rows)+"\n").encode()


def build():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"original source index")
    sources=json.loads(raw)["profiles"]
    cp=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(cp.read_bytes())==COMPILER_PIN,"scalar selector pin")
    spec=importlib.util.spec_from_file_location("hyperplane_scalar_selector",cp)
    compiler=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(compiler)
    steps=0

    def trace(r,w,degree,dimension):
        nonlocal steps
        need(1<=w<=r and dimension<=degree and 2130706433**6>=r+degree,"same-field LIST")
        cap,proof=compiler.compile_cap(r,w,degree,dimension)
        steps+=dimension
        return cap,[list(x) for x in proof]

    def compression(t,gate,degree,dimension):
        boxes=[]
        for low,high in ((D+1-t,349525),(349526,S-gate-1)):
            for a in range(low,high+1,5000):
                b=min(a+4999,high)
                cap,proof=trace(b-1,D-t,degree,dimension)
                boxes.append(dict(x=[a,b],trace=proof))
        small=[x for x in boxes if x["x"][1]<=349525]
        large=[x for x in boxes if x["x"][0]>349525]
        alpha=max(Q((S-x["x"][0])*x["trace"][-1][-1],x["x"][0]) for x in small)
        beta=max([Q(0)]+[(S-x["x"][0])*x["trace"][-1][-1]-alpha*x["x"][0] for x in large])
        bound=t+S*alpha+2*beta
        return dict(degree=degree,dimension=dimension,boxes=boxes,
                    alpha=rational(alpha),beta=rational(beta),bound=rational(bound))

    def whole(t,gate,degree):
        boxes=[]
        for a in range(gate+1,R-D+t+1,10000):
            b=min(a+9999,R-D+t)
            cap,proof=trace(R-a,D-t,degree,3)
            boxes.append(dict(e=[a,b],trace=proof,weight=t+b*cap))
        return dict(degree=degree,boxes=boxes,bound=max(x["weight"] for x in boxes))

    shards,refs,max_source,next_j,band_count={},[],0,9965,0
    for source in sources:
        need(source["path"]==str(next_j)+".json","ordered source profiles")
        raw=(PARENT/source["path"]).read_bytes()
        need(sha(raw)==source["sha256"],"source profile hash")
        old=json.loads(raw)
        j0,j1=old["J"]
        need(j0==next_j,"no omitted J")
        next_j=j1+1
        gate=old["heights"][0]["gate"]
        need(D<=S-gate-1 and 349525<S-gate-1<S and 3*349526>S,"integer mass corridor")
        rows=[dict(kind="profile",J=old["J"],parent_sha256=source["sha256"],constant_gate=gate)]
        normalized=[];maxima={};total=Q(old["mass_floor"],3)
        for t,den in ((1,2),(2,6)):
            bands=[]
            for lo in range(0,j1-9,2000):
                hi=min(lo+1999,j1-10)
                c2=compression(t,gate,hi+2,2)
                u3=whole(t,gate,hi+3)
                c4=compression(t,gate,hi+4,4)
                c=decode(c2["bound"])
                gap=j1-10-lo
                p4=c+Q(gap,S)*max(Q(0),Q(u3["bound"])-c)
                bands.append(dict(kind="band",t=t,zeta=[lo,hi],root_count=gap,
                                  C2=c2,U3=u3,C4=c4,prices=[rational(p4)]))
                band_count+=1
            for s in range(5,12):
                previous_max=Q(0)
                for band in bands:
                    previous_max=max(previous_max,decode(band["prices"][s-5]))
                    full=Q(D+1-t,S)*decode(band["C4"]["bound"])
                    price=previous_max+Q(band["root_count"],R+s-3)*max(Q(0),full-previous_max)
                    band["prices"].append(rational(price))
            maxima[str(t)]=[rational(max(decode(b["prices"][i]) for b in bands)) for i in range(8)]
            final=decode(maxima[str(t)][-1]);normalized.append(rational(final))
            factor=prod(Q(R+ell,D-t+ell) for ell in range(1,9))
            total+=factor*final/den
            rows.extend(bands)
        value=total.numerator//total.denominator+134944
        need(value<=266908096047530929<BUDGET,"original-source payment")
        max_source=max(max_source,value)
        rows.append(dict(kind="source",stage_maxima=maxima,normalized=normalized,
                         whole_source=value,reserve=BUDGET-value))
        name=str(j0)+".jsonl";data=lines_bytes(rows);shards[name]=data
        refs.append(dict(path=name,sha256=sha(data),J=old["J"]))
    need(next_j==21500 and len(refs)==13 and max_source==266908096047530929,"full source maximum")
    index=dict(SCOPE,profiles=refs,degree_bands=band_count,scalar_LIST_steps=steps,
               residual_source_maximum=max_source,whole_source_bound=270000000000000000,
               combined_maximum_pencil10_bound=272127061148955779,
               source_bytes=sum(map(len,shards.values())))
    return index,shards


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args=parser.parse_args()
    index,shards=build()
    folder=NODE/"certificates"
    if args.write:
        need(not folder.exists(),"refuse frozen certificate overwrite")
        folder.mkdir()
        for name,data in shards.items():
            (folder/name).write_bytes(data)
        (folder/"index.json").write_bytes(index_bytes(index))
    need((folder/"index.json").read_bytes()==index_bytes(index),"exact index")
    for name,data in shards.items():
        need((folder/name).read_bytes()==data,"exact degree shard")
    print("PASS",index["degree_bands"],"degree bands;",index["scalar_LIST_steps"],"scalar LIST steps")
    print("RESIDUAL SOURCE MAX",index["residual_source_maximum"],"WITH ALTERNATIVES",index["whole_source_bound"])
    print("MAXIMUM-PENCIL10 SOURCE CAP",index["combined_maximum_pencil10_bound"])
    print("INDEX",sha(index_bytes(index)),"SHARD BYTES",index["source_bytes"])
    print("Intermediate allowances are not universal; unrestricted rank19 and both Prizes remain open")


if __name__=="__main__":
    main()
