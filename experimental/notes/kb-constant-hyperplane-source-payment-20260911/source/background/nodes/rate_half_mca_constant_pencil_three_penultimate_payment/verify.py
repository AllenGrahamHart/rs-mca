"""Exact finite prices for maximal constant-three penultimate enclosures."""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path

NODE = Path(__file__).resolve().parent
NODES = NODE.parent
PARENT = NODES/"rate_half_mca_regular_rational_plane_terminal_bounds/certificates"
PARENT_PIN = "432929b5a53e7eb049a2c4280a4278af68b3bb4e69793effb3d15621d7742cba"
COMPILER_PIN = "bac33f24d1f34760518406185fcc9850d4fc61f5441486f94237e13b99eb8ca8"
R, D0 = 1048576, 67472
SCOPE = dict(
    schema="constant-three-penultimate-v1", J=[9965,21499],
    field="2130706433^6", agreement=1116048, target_epsilon="2^-128",
    original_error_rank=12, actual_P2_rank=19, anchors=7, pair_shared=[5,4],
    constant_pencil_dimension=3, constant_pencil_dimension4_excluded=True,
    normalization_cap_required=False,
    local_allowance_antecedent="after proved whole-source pencil alternatives are removed",
    primitive_shared_degree_max="J-8", scalar_primitive_degree="E>=2",
    exceptional_coordinates="at most D-E, not D",
    ordinary_children="rank-two3/3 with constant plane; use height-zero C_t",
    degree_cut=12000, complement_box_width=10000,
    original_weights=True, full_gcd_and_slack=True,
    whole_constant_terminal_tail_paid=False, all_rank19_sources_paid=False, prize_closed=False,
    parent_index_sha256=PARENT_PIN, compiler_sha256=COMPILER_PIN,
)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, indent=2)+"\n").encode()


def pair(value):
    value = Q(value)
    return [str(value.numerator), str(value.denominator)]


def decode(value):
    return Q(*map(int, value))


def build():
    raw = (PARENT/"index.json").read_bytes()
    need(sha(raw)==PARENT_PIN, "original source index")
    refs = json.loads(raw)["profiles"]
    cp = NODES/"list_padded_johnson_dimension_descent/compiler.py"
    need(sha(cp.read_bytes())==COMPILER_PIN, "selector provenance")
    spec = importlib.util.spec_from_file_location("constant_three_selector", cp)
    compiler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(compiler)
    shards, entries, steps, bands, next_j = {}, [], 0, 0, 9965
    gaps = []
    for ref in refs:
        need(ref["path"]==str(next_j)+".json", "ordered original profile")
        raw = (PARENT/ref["path"]).read_bytes()
        need(sha(raw)==ref["sha256"], "original profile hash")
        old = json.loads(raw)
        j0,j1 = old["J"]
        need(j0==next_j, "whole original degree coverage")
        next_j = j1+1
        k, gate = j1-8, old["heights"][0]["gate"]
        shard = dict(J=old["J"],parent_sha256=ref["sha256"],constant_gate=gate,cutoffs={})
        for t in (1,2):
            cap = decode(old["heights"][0]["cutoffs"][str(t)]["terminal"])
            allowance = decode(old["terminals"][t-1])
            need(0<=cap<=allowance and gate+1<=R-D0+t, "height-zero price and legal union")
            rows = []
            for e0,e1 in ((2,min(11999,k)),(12000,k)):
                if e0>e1:
                    continue
                boxes = []
                for a in range(gate+1,R-D0+t+1,10000):
                    b = min(a+9999,R-D0+t)
                    r,w,degree = R-a,D0-t,e1+1
                    need(1<=w<=r and degree>=3 and 2130706433**6>=r+degree, "same-field scalar LIST")
                    count,trace = compiler.compile_cap(r,w,degree,3)
                    boxes.append(dict(e=[a,b],trace=[list(x) for x in trace],weight=t+b*count))
                    steps += 3
                upper = max(box["weight"] for box in boxes)
                extra = (k-e0)*max(Q(0),upper-cap)
                gap = (R+1)*(allowance-cap)-extra
                need(gap>0, "degree-sensitive original price")
                rows.append(dict(E=[e0,e1],boxes=boxes,whole_constant_weight=upper,
                                 exceptional_excess=pair(extra),gap=pair(gap)))
                gaps.append(gap)
                bands += 1
            shard["cutoffs"][str(t)] = dict(constant_plane_price=pair(cap),allowance=pair(allowance),bands=rows)
        data = encode(shard)
        name = str(j0)+".json"
        shards[name] = data
        entries.append(dict(path=name,sha256=sha(data),J=old["J"]))
    need(next_j==21500 and len(shards)==13, "all source degrees")
    index = dict(SCOPE,profiles=entries,profile_prices=26,degree_bands=bands,
                 scalar_LIST_steps=steps,minimum_gap=pair(min(gaps)))
    return index,shards


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write",action="store_true")
    args = parser.parse_args()
    index,shards = build()
    folder = NODE/"certificates"
    if args.write:
        need(not folder.exists(), "refuse frozen certificate overwrite")
        folder.mkdir()
        for name,data in shards.items():
            (folder/name).write_bytes(data)
        (folder/"index.json").write_bytes(encode(index))
    need((folder/"index.json").read_bytes()==encode(index), "exact frozen index")
    for name,data in shards.items():
        need((folder/name).read_bytes()==data, "exact frozen shard")
    print("PASS26 original prices;",index["degree_bands"],"degree bands;",index["scalar_LIST_steps"],"LIST steps")
    print("MIN GAP",index["minimum_gap"],"INDEX",sha(encode(index)))
    print("Maximal constant3 penultimate class paid without normalization cap; constant4 and both Prizes open")


if __name__ == "__main__":
    main()
