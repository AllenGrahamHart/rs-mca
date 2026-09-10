"""Independent integer audit; no primary verifier or LIST-selector imports."""
import copy
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

NODE=Path(__file__).resolve().parent
PARENT=NODE.parent/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PIN="5fb6934b925a6f53b6a1063e61fdc684292d8249822cc9024d45e1fee091c991"
INDEX_PIN="432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
RANGES=[(9965,10964),(10965,11964),(11965,12964),(12965,13364),(13365,13964),
        (13965,14964),(14965,15964),(15965,16964),(16965,17964),(17965,18964),
        (18965,19964),(19965,20964),(20965,21499)]
FIXED=dict(schema="regular-terminal-rich-fibre-v1",J=[9965,21499],
           original_error_rank=12,actual_P2_rank=19,anchors=8,terminal_dimension=3,
           eigenvalues_field="original F",eigenspaces_max_dimension=1,
           root_mask="anchors plus F-eigenpolynomial roots; common zeros when e=0",
           intersection_scope="two actual complete joint cores on the remaining domain",
           raw_cutoffs=[1,2],parent_index_sha256=INDEX_PIN,
           unchanged_available_weight_maximum=272127061148955779,
           B_star=274980728111395087,near=134944,original_weights_unchanged=True,
           generic_degree_used=False,actual_core_witness=True,original_evaluation_flat_rank=9,
           whole_constant_upper_tail_open=True,rank19_closed=False,prize_closed=False)

def need(ok,why):
    if not ok:
        raise ValueError(why)

def sha(raw):
    return hashlib.sha256(raw).hexdigest()

def parents():
    raw=(PARENT/"index.json").read_bytes()
    need(sha(raw)==INDEX_PIN,"parent index custody")
    index=json.loads(raw)
    out=[]
    maximum=0
    for ref,ends in zip(index["profiles"],RANGES):
        raw=(PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"],"parent profile custody")
        p=json.loads(raw)
        need(p["J"]==list(ends),"parent range")
        factors=[]
        for t in (1,2):
            factor=Q(1)
            for j in range(1,9):
                factor*=Q(1048576+j,67472-t+j)
            factors.append(factor)
        allowance=[Q(int(a),int(b)) for a,b in p["terminals"]]
        price=Q(p["mass_floor"],3)+factors[0]*allowance[0]/2+factors[1]*allowance[1]/6
        integer=price.numerator//price.denominator+134944
        need(integer==p["weighted_envelope"]<=272127061148955779,"unchanged original envelope")
        maximum=max(maximum,integer)
        out.append(dict(J=p["J"],terminals=p["terminals"],sha256=ref["sha256"]))
    need(len(out)==len(index["profiles"])==13 and maximum==272127061148955779,
         "complete inherited available-weight envelope")
    return out

def validate(data,prior):
    need(set(data)==set(FIXED)|{"uniform_intersection_caps","profiles"},"schema fields")
    for key,value in FIXED.items():
        need(type(data[key]) is type(value) and data[key]==value,"scope: "+key)
    need(type(data["profiles"]) is list and len(data["profiles"])==13,"profile inventory")
    uniform=[None]*4
    checks=0
    for row,parent,ends in zip(data["profiles"],prior,RANGES):
        need(set(row)=={"J","parent_sha256","spectra"} and row["J"]==list(ends)==parent["J"],
             "exact profile coverage")
        need(row["parent_sha256"]==parent["sha256"],"parent profile pin")
        need(type(row["spectra"]) is list and len(row["spectra"])==4,"spectral coverage")
        lo,hi=ends
        for e,s in enumerate(row["spectra"]):
            need(set(s)=={"e","bad_bound","max_intersection","cutoffs"},"spectral fields")
            need(type(s["e"]) is int and s["e"]==e,"original-field spectral count")
            # These four expanded budgets are independent of the primary formula.
            bad=(hi-3,hi-1,2*hi-10,3*hi-19)[e]
            need(type(s["bad_bound"]) is int and s["bad_bound"]==bad,"root and anchor budget")
            h=s["max_intersection"]
            need(type(h) is int and 0<h<=lo-10,"nonvacuous integer intersection cap")
            uniform[e]=h if uniform[e] is None else min(uniform[e],h)
            need(set(s["cutoffs"])=={"1","2"},"both raw cutoffs")
            for t in (1,2):
                v=s["cutoffs"][str(t)]
                need(set(v)=={"reduced_n","reduced_agreement","numerator","denominator",
                              "pair_cap","original_pair_weight","terminal_weight","allowance"},
                     "cutoff fields")
                need(all(type(v[k]) is int for k in set(v)-{"allowance"}),"exact integer data")
                n=1048576+hi-bad
                a=67472+hi-t-bad
                need(v["reduced_n"]==n and v["reduced_agreement"]==a and 0<a<=n,
                     "auxiliary coordinate deletion only")
                den=a*a-n*h
                num=n*(a-h)
                need(a>h>=0 and den>0 and (v["denominator"],v["numerator"])==(den,num),
                     "strict positive Johnson denominator")
                cap=v["pair_cap"]
                need(cap>=1 and cap*den<=num<(cap+1)*den,"exact Johnson floor")
                weight=1048576-67472+t
                need(v["original_pair_weight"]==weight and v["terminal_weight"]==cap*weight,
                     "original weights cannot be reset")
                need(v["allowance"]==parent["terminals"][t-1],"unaltered allowance")
                top,bottom=map(int,v["allowance"])
                need(bottom>0 and cap*weight*bottom<=top,"below the original allowance")
                # For all J in this profile, A-b is no smaller than its high endpoint.
                low_bad=(lo-3,lo-1,2*lo-10,3*lo-19)[e]
                need(67472+lo-t-low_bad>=a and n-a==weight,"whole-profile monotonicity")
                checks+=1
    need(data["uniform_intersection_caps"]==uniform==[1913,1913,1022,169],
         "four whole-gap consequences")
    return checks

def mutations(data,prior):
    count=0
    def rejected(bad):
        nonlocal count
        try:
            validate(bad,prior)
        except (ValueError,KeyError,TypeError):
            count+=1
            return
        raise ValueError("accepted corrupted scope or inequality")
    for key in FIXED:
        bad=copy.deepcopy(data)
        bad[key]=None
        rejected(bad)
    for mode in ("hole","spectral-hole","bool-h","wrong-root-budget","reset-weight",
                 "bad-floor","raised-allowance","duplicate-profile","parent-pin",
                 "recomputed-too-large-intersection"):
        bad=copy.deepcopy(data)
        row=bad["profiles"][4]
        s=row["spectra"][3]
        v=s["cutoffs"]["1"]
        if mode=="hole":
            row["J"][0]+=1
        elif mode=="spectral-hole":
            row["spectra"].pop()
        elif mode=="bool-h":
            s["max_intersection"]=True
        elif mode=="wrong-root-budget":
            s["bad_bound"]-=1
        elif mode=="reset-weight":
            v["original_pair_weight"]-=8
        elif mode=="bad-floor":
            v["pair_cap"]-=1
        elif mode=="raised-allowance":
            v["allowance"]=[str(10**30),"1"]
        elif mode=="duplicate-profile":
            bad["profiles"][5]=copy.deepcopy(row)
        elif mode=="parent-pin":
            row["parent_sha256"]="0"*64
        else:
            # Recompute every dependent number, so stale arithmetic is not the rejection.
            s["max_intersection"]+=1
            h=s["max_intersection"]
            for v in s["cutoffs"].values():
                n,a=v["reduced_n"],v["reduced_agreement"]
                v["numerator"]=n*(a-h)
                v["denominator"]=a*a-n*h
                v["pair_cap"]=v["numerator"]//v["denominator"]
                v["terminal_weight"]=v["pair_cap"]*v["original_pair_weight"]
        rejected(bad)
    return count

def main():
    raw=(NODE/"certificate.json").read_bytes()
    need(sha(raw)==PIN,"frozen certificate custody")
    data=json.loads(raw)
    prior=parents()
    print("PASS independent",validate(data,prior),"exact Johnson floors and original-weight gates")
    print("PASS 52 spectral thresholds; 13 complete J profiles; unchanged eight-anchor envelope")
    print("PASS",mutations(data,prior),"scope/coverage/price mutations rejected")
    print("No primary/helper imports; actual two-core witness, not an unoccupied or generic fibre")
    print("Pencil-free rich fibres, whole constant upper tail and both Prize problems remain open")

if __name__=="__main__":
    main()
