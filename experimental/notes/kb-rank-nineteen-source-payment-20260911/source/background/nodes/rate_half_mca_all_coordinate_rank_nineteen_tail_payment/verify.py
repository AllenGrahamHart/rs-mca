"""Exact two-table all-coordinate rank19 source ledger; serial bounded replay."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
NODES=NODE.parent
PARENT=NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
GATE_PIN="7b58ecc95009ca1a680784343b7121c25feca5ed238c3e9797daa381cc637d51"
COMPILER_PIN="bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
R,D,S,BUDGET=1048576,67472,1048577,274980728111395087
STATES=[(s,c) for s in range(12) for c in range(min(3,s)+1)]
SCOPE=dict(
    schema="all-coordinate-rank19-source-v1",field="2130706433^6",
    agreement=1116048,target_epsilon="2^-128",J=[9965,21499],
    paid_J=[13965,21499],original_error_rank=12,actual_P2_rank_max_on_paid_tail=19,
    new_regular_rank=19,shared_dimension=11,degree_band_width=500,
    complement_box_width=10000,degree_excess="kappa=D-(s-1)",
    tables=["unrestricted","full_generic"],joint_rank_types=[0,1,2],
    regular_exception_types=["rank1 generic","rank2 possibly nonregular"],
    rank0_bound="kappa+floor(c/2)",rank_le1_and_regular_bad_bound="kappa+c",
    shared_carrier_joint_LIST=True,field_extension_used=False,
    nonconstant_line_inside_charge="one coordinate globally, not t per coordinate",
    local_antecedent="after proved whole-source pencil alternatives are removed",
    G33_small_degree_allowance="only eight-regular-anchor history and D<2*(H+1)",
    original_weights=True,full_gcd_and_slack=True,near=134944,
    parent_index_sha256=PARENT_PIN,gate_index_sha256=GATE_PIN,compiler_sha256=COMPILER_PIN,
    unrestricted_rank19_all_J_paid=False,whole_J_closed=False,prize_closed=False,
)


def need(ok,why):
    if not ok:raise ValueError(why)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def rat(x):
    x=Q(x)
    return [str(x.numerator),str(x.denominator)]


def dec(x):
    return Q(*map(int,x))


def index_bytes(x):
    return (json.dumps(x,indent=2)+"\n").encode()


def shard_bytes(rows):
    return ("\n".join(json.dumps(x,sort_keys=True,separators=(",",":")) for x in rows)+"\n").encode()


def line_counts(h,gate,t,j1):
    ct=R-D+t;den=D+1-t+h;top=(S+h-gate-1)//den
    need(1<=top<=32 and gate+1<=ct,"finite original line corridor")
    cases=[]
    for m in range(1,top+1):
        e=min(ct,S+h-m*den)
        need(e>=gate+1,"integer population feasible upper complement")
        value=t+m*e if h==0 else R+j1+(m-1)*e
        cases.append([m,e,min(m*ct,value)])
    return dict(cases=cases,bound=max(x[2] for x in cases))


def line_ledger(parent,gates):
    j1=parent["J"][1];maximum=j1-10
    cuts={1,maximum+1}
    for row in gates["bands"]:
        cuts.update(x for x in (row["low"],row["high"]+1) if 1<=x<=maximum+1)
    for row in parent["heights"][1:]:
        cuts.update(x for x in (row["height"][0],row["height"][1]+1) if 1<=x<=maximum+1)
    edges=sorted(cuts);rows=[]
    for low,end in zip(edges,edges[1:]):
        high=end-1
        gi=next(i for i,x in enumerate(gates["bands"]) if x["low"]<=low<=high<=x["high"])
        pi=next((i for i,x in enumerate(parent["heights"]) if x["height"][0]<=low<=high<=x["height"][1]),None)
        gate=max(gates["bands"][gi]["gate"],parent["heights"][pi]["gate"] if pi is not None else 0)
        rows.append(dict(height=[low,high],old_gate_row=gi,parent_height_row=pi,gate=gate,
                         cutoffs={str(t):line_counts(low,gate,t,j1) for t in (1,2)}))
    g=parent["heights"][0]["gate"]
    return dict(kind="lines",constant_gate=g,
                constant={str(t):line_counts(0,g,t,j1) for t in (1,2)},heights=rows)


def build():
    raw=(PARENT/"index.json").read_bytes();need(sha(raw)==PARENT_PIN,"parent index")
    refs=json.loads(raw)["profiles"];need(len(refs)==13,"all profiles")
    raw=(NODES/"rate_half_mca_coupled_pair_rank_frontier/gate_certificate.json").read_bytes()
    need(sha(raw)==GATE_PIN,"whole-height original gates");gates=json.loads(raw)
    cp=NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(cp.read_bytes())==COMPILER_PIN,"selector pin")
    spec=importlib.util.spec_from_file_location("all_coordinate_LIST_selector",cp)
    compiler=importlib.util.module_from_spec(spec);spec.loader.exec_module(compiler)
    shards,entries={},[];steps=bands_total=identities=size=height_rows=0
    tail_maximum=all_maximum=0;next_j=9965
    for ref in refs:
        need(ref["path"]==str(next_j)+".json","ordered original profiles")
        raw=(PARENT/ref["path"]).read_bytes();need(sha(raw)==ref["sha256"],"parent profile")
        old=json.loads(raw);j0,j1=old["J"];need(j0==next_j,"complete J");next_j=j1+1
        g=old["heights"][0]["gate"];H=(j1-1)//10
        intervals=[(a,min(a+499,j1-11)) for a in range(0,j1-10,500)]
        lines=line_ledger(old,gates);height_rows+=len(lines["heights"])
        rows=[dict(kind="profile",J=old["J"],parent_sha256=ref["sha256"]),lines];top=[]
        for t in (1,2):
            bands=[]
            for lo,hi in intervals:
                line=max([lines["constant"][str(t)]["bound"]]+
                         [x["cutoffs"][str(t)]["bound"] for x in lines["heights"] if x["height"][0]<=hi+1])
                base=[]
                for c in (1,2,3):
                    degree=c+hi;boxes=[]
                    for left in range(g+1,R-D+t+1,10000):
                        right=min(left+9999,R-D+t)
                        need(1<=D-t<=R-left and c<=degree and 2130706433**6>=R-left+degree,"same-field scalar corridor")
                        count,trace=compiler.compile_cap(R-left,D-t,degree,c);steps+=c
                        boxes.append(dict(e=[left,right],trace=[list(x) for x in trace],weight=t+right*count))
                    constant=max(x["weight"] for x in boxes)
                    item=dict(c=c,degree=degree,boxes=boxes,constant=constant)
                    if c>=2:
                        count,trace=compiler.compile_cap(R,D-t,degree,c);steps+=c
                        det=Q(R-degree+2,D-degree+2-t)*(R-D+t if c==2 else line)
                        joint=(R-D+t)*count
                        ff2=min(det,Q(joint));generic=ff2
                        small=c==3 and degree-1<2*(H+1)
                        if small:generic=min(generic,dec(old["terminals"][t-1]))
                        item.update(joint_trace=[list(x) for x in trace],determinant=rat(det),
                                    ff2=rat(ff2),generic_ff2=rat(generic),small_normalization=small)
                    base.append(item)
                bands.append(dict(kind="band",t=t,kappa=[lo,hi],line_cap=line,base=base))
                bands_total+=1
            U={};G={}
            for s,c in STATES:
                uv=[];gv=[]
                for i,(lo,hi) in enumerate(intervals):
                    if s==c:
                        if c==0:u=v=Q(R-D+t)
                        else:
                            base=bands[i]["base"][c-1];u=v=Q(base["constant"])
                            if c>=2:
                                u=max(u,dec(base["ff2"]));v=max(v,dec(base["generic_ff2"]))
                    else:
                        C=max(U[s-1,c][:i+1]);F=max(U[s-1,c-1][:i+1]) if c else C
                        Z=max(U[s-1,c-2][:i+1]) if c>=2 else max(C,F)
                        x1=max(Q(0),F-C);x0=max(Q(0),Z-max(C,F))
                        u=max(C,*[((R+s+x)*C+(x+c)*x1+(x+c//2)*x0)/(D+s+x-t) for x in (lo,hi)])
                        C=max(G[s-1,c][:i+1]);F=max(G[s-1,c-1][:i+1]) if c else C
                        T=max(U[s-1,c][:i+1]) if c>=2 else C
                        excess=max(Q(0),F-C,T-C)
                        v=max(C,*[((R+s+x)*C+(x+c)*excess)/(D+s+x-t) for x in (lo,hi)])
                        identities+=2
                    need(u>=0 and v>=0,"nonnegative state prices")
                    uv.append(u);gv.append(v)
                U[s,c]=uv;G[s,c]=gv
            for i,band in enumerate(bands):
                band.update(unrestricted=rat(U[11,3][i]),full_generic=rat(G[11,3][i]))
            top.append(max(G[11,3]));rows.extend(bands)
        total=Q(old["mass_floor"],3)+top[0]/2+top[1]/6
        price=total.numerator//total.denominator+134944
        all_maximum=max(all_maximum,price)
        paid=j0>=13965
        if paid:
            need(price<BUDGET,"advertised whole rank19 tail");tail_maximum=max(tail_maximum,price)
        rows.append(dict(kind="source",raw_prices=[rat(x) for x in top],
                         regular_source=price,paid_profile=paid,reserve=BUDGET-price))
        name=str(j0)+".jsonl";data=shard_bytes(rows);shards[name]=data;size+=len(data)
        entries.append(dict(path=name,sha256=sha(data),J=old["J"],regular_source=price))
    need(next_j==21500,"whole profile range")
    result=dict(SCOPE,profiles=entries,degree_bands=bands_total,scalar_and_joint_LIST_steps=steps,
                recurrence_identities=identities,state_count_per_table=42,line_height_rows=height_rows,
                source_bytes=size,tail_regular_maximum=tail_maximum,all_regular_recipe_maximum=all_maximum,
                combined_rank_le19_tail_bound=max(tail_maximum,274462040894062110,270000000000000000))
    need(result["combined_rank_le19_tail_bound"]<BUDGET,"original tail with source alternatives")
    return result,shards


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("--write",action="store_true");args=p.parse_args()
    index,shards=build();folder=NODE/"certificates"
    data={"index.json":index_bytes(index),**shards}
    if args.write:
        folder.mkdir(exist_ok=True);need(not any(folder.iterdir()),"refuse overwrite")
        for name,raw in data.items():(folder/name).write_bytes(raw)
    else:
        need({x.name for x in folder.iterdir()}==set(data),"exact certificate inventory")
        for name,raw in data.items():need((folder/name).read_bytes()==raw,"exact reconstruction: "+name)
    print("PASS",index["degree_bands"],"degree bands;",index["scalar_and_joint_LIST_steps"],"LIST steps;",
          index["recurrence_identities"],"two-table recurrence identities")
    for row in index["profiles"]:print(row["J"],row["regular_source"],flush=True)
    print("PAID RANK<=19 TAIL",index["combined_rank_le19_tail_bound"],"REGULAR MAX",index["tail_regular_maximum"])
    print("INDEX",sha(data["index.json"]),"BYTES",index["source_bytes"],"HEIGHT ROWS",index["line_height_rows"])
    print("Rank19 lower prefix and pair ranks20..22 remain; no whole J or Prize closes")


if __name__=="__main__":
    main()
