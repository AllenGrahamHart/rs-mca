"""Offline bounded replay of the raw-one rank19 source-tail theorem."""

import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = "6077c2be5adb36136cd3ad062e1a278c07616fed053085a28b4a740a1759bae7"
PARENT = "526f819ac2cf1525a90370e39e04ccab90bfe4c2"
PRIOR = "kb-constant-projection-source-payment-20260911"
HELPER_HASH = "849fcfb5ea95d69d82d3bbbb21e2ebc556fa71628810dd67741294a9180afebf"
ROOTS = ["rate_half_mca_raw_one_rank_nineteen_source_tail_payment"]
SCOPE=dict(
    schema="raw-one-rank19-source-tail-v1",field="2130706433^6",
    n=2097152,k=1048576,agreement=1116048,target_epsilon="2^-128",
    original_error_rank=12,raw_weight_J=[9965,21499],paid_J=[20618,21499],
    actual_family="P1: pairs assigned original raw exactly one",
    actual_P1_pair_affine_rank_max=19,P2_rank_restriction=False,P2_projection_restriction=False,
    residual_antecedent="after paid original whole-source pencil alternatives",
    enclosure_pair_dimension=19,shared_dimension=11,actual_enclosure_occupation_required=False,
    generic_augmentation="one ORIGINAL-field constant vector when generic rank is10 and actual rank<=18",
    proper_carrier_bound=78301130139301820,small_projection_bound=31878195092556089,
    quadratic_contained_mass=89070753921055403,quadratic_moving_labels=21490,
    generic_raw_one_bound=180336660306614524,
    inherited_table_use="t=1 weighted enclosures only; no inherited whole P2 source conclusion",
    lower_J_inherited_in_G=False,upper_degree=21499,normalization_history="eight actual regular ancestors at G33",
    U_nonregular_children_retained=True,original_owners_weights_field=True,extra_anchor_factor=False,
    original_near=134944,source_identity="floor((original min(raw,9) resource+N1)/2)+near",
    source_alternatives="MAXIMUM",whole_source_bound=274978423712566784,reserve=2304398828303,
    J20617_unsafe_claim=False,all_original_rank12_sources_closed=False,
    active_v4_atom=False,ordinary_LIST_closed=False,adjacent_safe_row_closed=False,prize_closed=False,
)
SCOPE.update(lane="K3 / DIRECT", unit="Entire original distinct bad-slope set",
             quantifier="Every complete post-near source and every valid original owner assignment at the printed scope",
             B_star="274980728111395087", covered_J_integers=882)


def need(ok, why):
    if not ok:
        raise ValueError(why)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def load_prior():
    path = ROOT.parent/PRIOR/"replay.py"
    need(not path.is_symlink() and path.stat().st_size < 65536, "prior helper path")
    need(digest(path.read_bytes()) == HELPER_HASH, "prior helper pin")
    spec = importlib.util.spec_from_file_location("frozen_branch_custody", path)
    branch = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(branch)
    prior, published, graph, pins = branch.load_prior()
    raw = prior.checked_file(branch.ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == branch.MANIFEST_HASH, "parent manifest pin")
    manifest = json.loads(raw)
    sources = branch.validate(manifest, prior, published, graph, pins)
    published.update({(PRIOR, path): data for path, data in sources.items()})
    graph.update(manifest["requirements"])
    need(len(published) == 1729, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-raw-one-rank19-source-tail-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 462
         and manifest["published_source_hashes_checked"] == 1729, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 12, "new file inventory")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()}
    need(actual == set(files), "unlisted/missing source")
    sources = {}
    for relative, row in files.items():
        need(relative == "source/"+row["origin_path"], "origin identity")
        parts = PurePosixPath(row["origin_path"]).parts
        need(len(parts) >= 4 and parts[:2] == ("background", "nodes")
             and parts[2] in ROOTS, "source scope")
        data = prior.checked_file(ROOT, relative)
        need(digest(data) == row["sha256"], "new source pin")
        sources[relative] = data
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 66201,
         "source byte inventory")
    documents = {}
    for row in manifest["inherited_sources"]:
        key = row["node"], row["filename"]
        need(key not in documents, "duplicate inherited document")
        data = published[row["packet"], row["path"]]
        parts = PurePosixPath(row["path"]).parts
        need(parts[0] == "source" and parts[2] == "nodes" and parts[3] == row["node"]
             and "/".join(parts[4:]) == row["filename"], "inherited identity")
        need(digest(data) == row["sha256"], "inherited document pin")
        documents[key] = data
    need(len(documents) == 462, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 141 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
         "closure inventory")
    for name, deps in graph.items():
        if name not in ROOTS:
            need(deps == credited[name], "inherited dependency drift")
            need(all((name, f) in documents for f in ("statement.md", "proof.md")),
                 "missing inherited proof")
            continue
        prefix = "source/background/nodes/"+name+"/"
        data = sources[prefix+"node.json"]
        need(digest(data) == manifest["origin_node_manifest_sha256"][name], "new node provenance")
        node = json.loads(data)
        need(node["node"]["id"] == name and node["node"]["status"] == "PROVED"
             and [edge["from"] for edge in node["requires"]] == deps, "new node status/graph")
        need(all(prefix+f in sources for f in ("statement.md", "proof.md", "transport.md")), "missing new proof")
    active, done = set(), set()

    def visit(name):
        need(name not in active, "dependency cycle")
        if name in done:
            return
        active.add(name)
        for child in graph[name]:
            visit(child)
        active.remove(name)
        done.add(name)

    for name in ROOTS:
        visit(name)
    need(done == set(graph), "unreachable dependency")
    return sources


def mutations(manifest, prior, published, graph, pins):
    cases = []
    for key, value in {"schema": "wrong", "parent_commit": "0"*40, "snapshot_roots": [],
                       "supplier_manifests": {}, "inherited_sources": [], "source_bytes": 0}.items():
        bad = copy.deepcopy(manifest)
        bad[key] = value
        cases.append(bad)
    for key in SCOPE:
        bad = copy.deepcopy(manifest)
        bad["scope"][key] = None
        cases.append(bad)
    for key, value in (("path", "../../escape"), ("origin_path", "wrong"), ("sha256", "0"*64)):
        bad = copy.deepcopy(manifest)
        bad["files"][0][key] = value
        cases.append(bad)
    for mode in ("duplicate", "missing", "cycle", "pin", "proof-pin"):
        bad = copy.deepcopy(manifest)
        if mode == "duplicate":
            bad["files"].append(bad["files"][0])
        elif mode == "missing":
            bad["files"].pop()
        elif mode == "cycle":
            bad["requirements"][ROOTS[0]].append(ROOTS[0])
        elif mode == "pin":
            bad["origin_node_manifest_sha256"][ROOTS[0]] = "0"*64
        else:
            bad["inherited_sources"][0]["sha256"] = "0"*64
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, prior, published, graph, pins)
        except (ValueError, KeyError, TypeError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    prior, published, graph, pins = load_prior()
    raw = prior.checked_file(ROOT, "SOURCE_MANIFEST.json")
    need(digest(raw) == MANIFEST_HASH, "manifest pin")
    manifest = json.loads(raw)
    sources = validate(manifest, prior, published, graph, pins)
    print("PASS 1741 listed source hashes; 462 inherited proof documents; 141-node acyclic closure;",
          mutations(manifest, prior, published, graph, pins), "malformed manifests rejected", flush=True)

    # Earlier amendments were checked by their own frozen custody validators.
    runtime_sources = {}
    for (_, relative), data in published.items():
        parts = PurePosixPath(relative).parts
        if (len(parts) >= 5 and parts[0] == "source" and parts[2] == "nodes"
                and parts[3] in manifest["requirements"]):
            runtime_sources[relative] = data
    need(not set(runtime_sources).intersection(sources), "new node runtime collision")
    runtime_sources.update(sources)
    checks = [
        (ROOTS[0], "verify.py"), (ROOTS[0], "verify_audit.py"),
        ("mca_all_coordinate_pair_rank_descent", "verify.py"),
        ("mca_small_pair_terminal_weight_bounds", "verify.py"),
        ("rate_half_mca_low_raw_hyperplane_payment", "verify_audit.py"),
        ("pair_space_polynomial_projection_dichotomy", "verify.py"),
        ("rate_half_mca_inherited_normalization_frontier", "verify_audit.py"),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-raw-one-rank19-") as temp:
        runtime = Path(temp)
        for relative, data in runtime_sources.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS two new and five inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("P1 rank<=19 pays J20618..21499 with P2 unrestricted; other classes and both Prizes remain open")


if __name__ == "__main__":
    main()
