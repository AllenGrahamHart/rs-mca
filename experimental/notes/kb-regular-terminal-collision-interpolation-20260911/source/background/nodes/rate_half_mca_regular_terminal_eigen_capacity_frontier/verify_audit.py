"""Independent rational whole-box audit; no primary or selector imports."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
PARENT=NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN="4c8ddb8396ce996e92fba3e12d6d96e87867668161e2cbbe710bf3de2dac501f"
PARENT_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
OLD_PIN="5fb6934b925a6f53b6a1063e61fdc684292d8249822cc9024d45e1fee091c991"
R,D=1048576,67472
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]
SCOPE=dict(J=[9965,21499],original_error_rank=12,actual_P2_rank=19,anchors=8,
           terminal_dimension=3,pencil_free=True,eigenvalues_field="original F",
           eigenspaces_max_dimension=1,raw_cutoffs=[1,2],
           primitive_degree="kappa=1+actual max degree(U0/G), all 3..J1-8",
           gcd_excess="v=J-8-kappa-distinct nonanchor G roots, includes degree slack, every v>=0",
           root_mask="anchors, domain gcd roots, then primitive F-eigenpolynomial roots",
           capacities="hereditary actual eigenlines and arbitrary affine planes",
           selected_pairs="exactly floor(L_t/(1048576-67472+t))+1",
           natural_intersection_cap="min(H,kappa-2)",energy_gate="S0>=N0 and strict energy",
           original_weights_unchanged=True,actual_core_witness=True,
           original_evaluation_flat_rank=9,automatic_primitive_degree="kappa<=H+2",
           excess_primitive_degree="kappa>=H+3",generic_degree_used=False,
           available_weight_maximum=272127061148955779,B_star=274980728111395087,near=134944,
           whole_constant_upper_tail_open=True,rank19_closed=False,whole_degree_closed=False,
           prize_closed=False)

def need(ok,why):
    if not ok:
        raise ValueError(why)

def integer(x):
    return type(x) is int

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def load_parents():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN,"parent index custody")
    parent=json.loads(raw)
    need(len(parent["profiles"])==13,"parent coverage")
    out=[]
    maximum=0
    for ref,ends in zip(parent["profiles"],RANGES):
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent shard custody")
        p=json.loads(raw)
        need(p["J"]==list(ends),"parent degree interval")
        price=Q(p["mass_floor"],3)
        for t,divisor in ((1,2),(2,6)):
            factor=Q(1)
            for j in range(1,9):
                factor*=Q(R+j,D-t+j)
            price+=factor*Q(*map(int,p["terminals"][t-1]))/divisor
        value=price.numerator//price.denominator+134944
        need(value==p["weighted_envelope"]<=272127061148955779,"unchanged original envelope")
        maximum=max(maximum,value)
        out.append(dict(J=p["J"],gate=p["heights"][0]["gate"],
                        allowances=p["terminals"],sha256=ref["sha256"]))
    need(maximum==272127061148955779,"available-weight maximum")
    return out

def validate_index(data):
    keys={"schema","parent_index_sha256","scope","profiles","uniform_caps", "profile_count",
          "spectral_gate_count","cutoff_count","box_count"}
    need(set(data)==keys and data["schema"]=="regular-eigen-capacity-index-v1","index schema")
    need(data["parent_index_sha256"]==PARENT_PIN,"parent index pin")
    need(json.dumps(data["scope"],sort_keys=True)==json.dumps(SCOPE,sort_keys=True),"scope and types")
    need(data["profile_count"]==13 and data["spectral_gate_count"]==52 and data["cutoff_count"]==104,
         "index counts")
    need(len(data["profiles"])==13 and data["uniform_caps"]==[2108,1985,1948,1866],"profile summary")
    for row,ends in zip(data["profiles"],RANGES):
        need(set(row)=={"path","sha256","J","H"} and row["J"]==list(ends)
             and row["path"]==str(ends[0])+".json","ordered shard identity")
        need(type(row["sha256"]) is str and len(row["sha256"])==64,"shard digest")

def box_values(lo,hi,q2,h,m,q1,e,t):
    if hi<=h+2:
        u,w=1,-2
    else:
        need(lo>=h+3,"natural/fixed box must split")
        u,w=0,h
    c2=2*(0,Q(q2),Q(q2+q1),Q(3*q2,2))[e]
    need(c2.denominator==1,"integer doubled cost")
    c2=int(c2)
    def s(x):
        return 2*m*(D+x-t)-(x-1)*c2
    def energy(x):
        n=R+x
        return s(x)**2-2*n*s(x)-4*n*m*(m-1)*(u*x+w)
    # Recover coefficients from exact evaluations, independently of the primary expansion.
    c=energy(0)
    a=(energy(2)-2*energy(1)+c)//2
    b=energy(1)-a-c
    vertex=Q(-b,2*a) if a>0 else None
    inside=vertex is not None and lo<=vertex<=hi
    return dict(kappa=[lo,hi],q2=q2,H_affine=[u,w],root_cost_twice=c2,
                S_twice=[s(0),s(1)-s(0)],energy4=[c,b,a],
                S_margin_endpoints=[s(x)-2*(R+x) for x in (lo,hi)],
                energy4_endpoints=[energy(x) for x in (lo,hi)],
                vertex_discriminant=4*a*c-b*b if inside else None),energy,vertex if inside else None

def validate_profile(data,parent,old):
    need(set(data)=={"schema","J","primitive_degree","parent_sha256","original_constant_gate","spectra"},
         "profile fields")
    need(data["schema"]=="regular-eigen-capacity-profile-v1" and data["J"]==parent["J"],"profile identity")
    kmax=parent["J"][1]-8
    need(data["primitive_degree"]==[3,kmax] and data["parent_sha256"]==parent["sha256"],
         "all primitive degrees and parent custody")
    g=data["original_constant_gate"]
    need(integer(g) and g==parent["gate"],"original constant-pencil gate")
    need(len(data["spectra"])==4,"all spectral types")
    count=0
    for e,spectrum in enumerate(data["spectra"]):
        need(set(spectrum)=={"e","H","cutoffs"} and integer(spectrum["e"])
             and spectrum["e"]==e,"spectrum fields")
        h=spectrum["H"]
        need(integer(h) and h>old["spectra"][e]["max_intersection"],"strict improvement")
        need(len(spectrum["cutoffs"])==2,"both original cutoffs")
        for t,cut in enumerate(spectrum["cutoffs"],1):
            need(set(cut)=={"t","allowance","original_pair_weight","M","q1","boxes"}
                 and integer(cut["t"]) and cut["t"]==t,"cutoff fields")
            need(cut["allowance"]==parent["allowances"][t-1],"unchanged allowance")
            top,bottom=map(int,cut["allowance"])
            weight=cut["original_pair_weight"]
            need(integer(weight) and weight==R-D+t,"original one-pair weight")
            m,q1=cut["M"],cut["q1"]
            need(integer(m) and m>=2 and (m-1)*weight*bottom<=top<m*weight*bottom,
                 "first unaffordable actual pair count")
            need(integer(q1) and q1*(D+1-t)<=R-g<(q1+1)*(D+1-t),"eigenline pair capacity")
            cursor=3
            for box in cut["boxes"]:
                lo,hi=box["kappa"]
                q2=box["q2"]
                need(all(integer(x) for x in (lo,hi,q2)) and lo==cursor<=hi<=kmax,
                     "complete primitive-degree box coverage")
                need(q2>=2*q1,"twice-line plane capacity")
                for x in (lo,hi):
                    den=D-x+2-t
                    need(den>0 and q2*den<=R-x+2<(q2+1)*den,"exact plane-capacity floor")
                expected,energy,vertex=box_values(lo,hi,q2,h,m,q1,e,t)
                need(json.dumps(box,sort_keys=True)==json.dumps(expected,sort_keys=True),
                     "independent direct-energy reconstruction")
                need(min(box["S_margin_endpoints"])>=0,"S0>=N0 all-gcd gate")
                need(energy(lo)>0 and energy(hi)>0 and (vertex is None or energy(vertex)>0),
                     "strict whole-box energy")
                cursor=hi+1
                count+=1
            need(cursor==kmax+1,"primitive upper endpoint")
    return count

def reprice(spectrum,h):
    spectrum["H"]=h
    for cut in spectrum["cutoffs"]:
        merged=[]
        for box in cut["boxes"]:
            lo,hi=box["kappa"]
            if merged and merged[-1][2]==box["q2"]:
                merged[-1][1]=hi
            else:
                merged.append([lo,hi,box["q2"]])
        new=[]
        for lo,hi,q2 in merged:
            ranges=[]
            if lo<=min(hi,h+2):
                ranges.append((lo,min(hi,h+2)))
            if max(lo,h+3)<=hi:
                ranges.append((max(lo,h+3),hi))
            for a,b in ranges:
                new.append(box_values(a,b,q2,h,cut["M"],cut["q1"],spectrum["e"],cut["t"])[0])
        cut["boxes"]=new

def mutations(index,profile,parent,old):
    count=0
    def reject(check,bad,reason=None):
        nonlocal count
        try:
            check(bad)
        except (ValueError,KeyError,TypeError) as error:
            if reason is not None:
                need(str(error)==reason,"mutation hit wrong gate: "+str(error))
            count+=1
            return
        raise ValueError("accepted corrupted claim")
    for key in SCOPE:
        bad=copy.deepcopy(index)
        bad["scope"][key]=None
        reject(validate_index,bad)
    for key,value in (("schema","wrong"),("parent_index_sha256","0"*64),
                      ("profiles",[]),("uniform_caps",[0]*4),("cutoff_count",0)):
        bad=copy.deepcopy(index)
        bad[key]=value
        reject(validate_index,bad)
    check=lambda data:validate_profile(data,parent,old)
    for mode in ("domain-gcd-only","bad-parent","pencil-gate","missing-spectrum","bool-H",
                 "wrong-t","reset-weight","raise-allowance","wrong-M","line-weight",
                 "box-hole","bad-plane","undercharge-roots","bad-natural-cap","bad-S",
                 "stale-energy","raised-H-recomputed"):
        bad=copy.deepcopy(profile)
        spec=bad["spectra"][3]
        cut=spec["cutoffs"][1]
        box=cut["boxes"][0]
        if mode=="domain-gcd-only": bad["primitive_degree"][0]=bad["J"][0]-8
        elif mode=="bad-parent": bad["parent_sha256"]="0"*64
        elif mode=="pencil-gate": bad["original_constant_gate"]+=1
        elif mode=="missing-spectrum": bad["spectra"].pop()
        elif mode=="bool-H": spec["H"]=True
        elif mode=="wrong-t": cut["t"]=7
        elif mode=="reset-weight": cut["original_pair_weight"]-=1
        elif mode=="raise-allowance": cut["allowance"][0]=str(int(cut["allowance"][0])+1)
        elif mode=="wrong-M": cut["M"]+=1
        elif mode=="line-weight": cut["q1"]*=cut["original_pair_weight"]
        elif mode=="box-hole": box["kappa"][0]+=1
        elif mode=="bad-plane": box["q2"]+=1
        elif mode=="undercharge-roots": box["root_cost_twice"]=2*box["q2"]
        elif mode=="bad-natural-cap": box["H_affine"]=[0,spec["H"]]
        elif mode=="bad-S": box["S_twice"][0]+=1
        elif mode=="stale-energy": box["energy4_endpoints"][0]+=1
        else: reprice(spec,spec["H"]+1)
        reject(check,bad,"strict whole-box energy" if mode=="raised-H-recomputed" else None)
    return count

def gcd_slack_control():
    # Small degree/domain identity, not an official large-agreement source.
    p,j,delta,g,kappa=101,30,8,4,5
    anchors=set(range(8))
    roots={x for x in range(p) if (x-9)**2*(x*x+2)%p==0}
    need(roots=={9},"repeated root plus irreducible factor control")
    z=len(roots-anchors)
    slack=j-9-delta
    v=slack+g-z
    r=p-j
    need((slack,z,v)==(13,1,16) and p-8-z==r+kappa+v,
         "retain actual-degree slack and nondomain gcd degree")
    need(p-8-z!=r+kappa+g-z,"gcd roots alone do not determine the domain shift")

def main():
    raw=(NODE/"certificates/index.json").read_bytes()
    need(sha(raw)==PIN,"new index custody")
    index=json.loads(raw)
    validate_index(index)
    parents=load_parents()
    old_raw=(NODE.parent/"rate_half_mca_regular_terminal_rich_fibre_frontier/certificate.json").read_bytes()
    need(sha(old_raw)==OLD_PIN,"previous frontier custody")
    old=json.loads(old_raw)
    count=0
    uniform=[None]*4
    for row,parent,previous in zip(index["profiles"],parents,old["profiles"]):
        raw=(NODE/"certificates"/row["path"]).read_bytes()
        need(sha(raw)==row["sha256"],"new profile custody")
        data=json.loads(raw)
        need([s["H"] for s in data["spectra"]]==row["H"],"index gate agreement")
        count+=validate_profile(data,parent,previous)
        for e,h in enumerate(row["H"]):
            uniform[e]=h if uniform[e] is None else min(uniform[e],h)
    need(count==index["box_count"]==704 and uniform==index["uniform_caps"],"whole index census")
    rejected=mutations(index,data,parents[-1],old["profiles"][-1])
    gcd_slack_control()
    print("PASS independent",count,"whole-box inequalities; 104 cutoff bounds; 52 strict improvements")
    print("PASS",rejected,"scope/coverage/price mutations, including a fully recomputed raised-H failure")
    print("PASS repeated/nondomain gcd roots and unused polynomial-degree slack control")
    print("UNIFORM",uniform,"unchanged original available-weight maximum 272127061148955779")
    print("All-gcd and actual-owner geometry rely on written proofs; no unrestricted source or Prize closure")

if __name__=="__main__":
    main()
