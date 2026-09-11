"""Offline bounded replay of constant-hyperplane original-source payments."""

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
MANIFEST_HASH = "68d245f2a6c2dd34674e847865a7da21d3338c68f0355b66d132e1f7769a5f47"
PARENT = "d8ab3ac67f71bd95fbc698543d38a2305d3045de"
PRIOR = "kb-penultimate-graded-pencil-payment-20260911"
HELPER_HASH = "e6cce9aa8eccbb40114f527f7695d47fdf05eb57cc16ef2b7f092d3833d9b385"
ROOTS = ["pair_space_constant_pencil_three_child_ledger","rate_half_mca_constant_pencil_three_penultimate_payment","mca_constant_hyperplane_primitive_degree_descent","rate_half_mca_constant_hyperplane_source_payment"]
SCOPE = dict(
    lane="K3 / DIRECT", object="MCA", agreement=1116048,
    field="2130706433^6", target_epsilon="2^-128",
    original_error_rank=12, shared_carrier_dimension=11, J=[9965,21499],
    actual_P2_rank=19, generic_projection="full",
    B_star="274980728111395087", near=134944, raw_cutoffs=[1,2],
    original_source_class="constant10-dimensional subspace and NO constant11",
    constant_source_bound="270000000000000000",
    residual_source_maximum="266908096047530929",
    combined_maximum_pencil10_bound="272127061148955779",
    combined_source_reserve="2853666962439308",
    original_source_remainder="maximum pencil dimension8 or9, OR full constant11",
    excessive_original_field_projection_rank9=False,
    normalization_cap_required=False,
    local_allowance_antecedent="Residual source AFTER proved whole-source pencil alternatives are removed",
    whole_source_alternatives="Combine whole-source caps by MAXIMUM, never addition",
    penultimate_class="constant3 but NO constant4",
    penultimate_prices=26, penultimate_degree_bands=48, penultimate_LIST_steps=5238,
    minimum_penultimate_gap="2464185717588779767135/12274496849",
    shared_stages=[4,5,6,7,8,9,10,11], degree_excess="zeta=E-(s-2)",
    root_count="at most D-E; bounded by J1-10-zeta_low on each band",
    source_degree_bands=218, source_LIST_steps=119988,
    original_weights_unchanged=True, higher_raw_and_near_included_once=True,
    actual_pencil_occupation_assumed=False,
    all_intermediate_prices_fit_old_Lt=False,
    full_constant4_penultimate_paid=False,
    all_rank19_sources_covered=False, rank19_closed=False,
    active_v4_atom=False, whole_degree_closed=False, prize_closed=False,
)


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
    need(len(published) == 1508, "inherited source inventory")
    return prior, published, graph, dict(pins, **{PRIOR: branch.MANIFEST_HASH})


def validate(manifest, prior, published, credited, pins):
    need(manifest["schema"] == "kb-constant-hyperplane-source-payment-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS,
         "snapshot identity")
    need(manifest["supplier_manifests"] == pins, "supplier pins")
    need(json.dumps(manifest["scope"], sort_keys=True) == json.dumps(SCOPE, sort_keys=True),
         "scope and types")
    need(manifest["inherited_proof_documents_compared"] == 423
         and manifest["published_source_hashes_checked"] == 1508, "inherited counts")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 71, "new file inventory")
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
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 3767421,
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
    need(len(documents) == 423, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 133 and set(graph) == set(manifest["origin_node_manifest_sha256"]),
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
        need(all(prefix+f in sources for f in ("statement.md", "proof.md")), "missing new proof")
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
            bad["requirements"][ROOTS[0]].append(ROOTS[1])
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
    print("PASS 1579 listed source hashes; 423 inherited proof documents; 133-node acyclic closure;",
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
        (ROOTS[0], "verify.py"),
        (ROOTS[1], "verify.py"), (ROOTS[1], "verify_audit.py"),
        (ROOTS[2], "verify.py"),
        (ROOTS[3], "verify.py"), (ROOTS[3], "verify_audit.py"),
        ("rate_half_mca_regular_rational_plane_terminal_bounds", "verify_audit.py"),
        ("rate_half_mca_regular_terminal_actual_span_frontier", "verify_audit.py"),
        ("pair_space_nonconstant_pencil_regular_children", "verify.py"),
        ("rate_half_mca_nonconstant_pencil_penultimate_payment", "verify.py"),
    ]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-constant-hyperplane-") as temp:
        runtime = Path(temp)
        for relative, data in runtime_sources.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        for name, filename in checks:
            path = runtime/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS six new and four inherited focused checks from frozen sources")
    print("Other inherited arithmetic not freshly replayed; external mathematical review due")
    print("Original rank19 maximum pencil dimensions8/9 or full constant11 remain; both Prizes open")


if __name__ == "__main__":
    main()
