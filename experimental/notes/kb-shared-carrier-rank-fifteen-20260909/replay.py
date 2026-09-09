"""Bounded serial replay of frozen proofs; arithmetic is not proof review."""

import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = "f998e2205389157690fae7f3387aedc6cd6602a1135b2066283d552e9dd1829e"
PARENT = "41c49b58cb68b67db9dbaec36668555cef0e63ad"
ROOTS = ["mca_shared_carrier_rank_two_anchor",
         "rate_half_mca_low_pair_rank_twelve_payment",
         "rate_half_mca_low_pair_rank_fourteen_payment",
         "rate_half_mca_low_pair_rank_fifteen_payment",
         "rate_half_mca_low_pair_shared_rank_frontier"]
SUPPLIERS = {
    "low-core-flat-source-cumulative-20260908": "656b342982896233bf8f906b6ba93aae785c9179414d02f982f47b095a60027b",
    "kb-parameter-graph-spread-20260908": "b93f34d83b297e4370a4d6cb3b949432f99ebb4293b059fc7a926fd6b427ce1c",
    "kb-low-defect-rank-filtration-20260909": "bc3b337d2c369a06ab82d5d6d5a2fa8f9edfe2931f34e0244b94345286d42645",
    "kb-raw-mass-cubic-interval-20260909": "375c15045f34386d787b559a8705fc1c1f66653ce5a6568630a2d0f79ee75bbc",
    "kb-low-pair-pencil-payment-20260909": "c17dcfa6c844ceb0ae5f1a5bd578f4edd7b58d10048ae317528bfd37ebad43ce",
    "kb-dominant-pencil-rank-eleven-20260909": "8177b2bf76089547514d9d84f111eed4ada89d62c029bfa47e267ee6299f7416",
}
BOUNDS = {
    "rank_fifteen_bound": 274138707278280353, "reserve": 842020833114734,
    "shared_ten_pair_seventeen_bound": 274138707278280353,
    "shared_nine_direct_bound": 238911770855075395,
    "shared_nine_preexisting_graph_bound": 215295179262501741,
    "constant_complement_cap": 520000, "remaining_J": [9965, 21499],
    "surviving_shared_pair_ranks": [[10, r] for r in range(18, 21)]+[[11, r] for r in range(16, 23)],
}


def need(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_file(root, relative):
    need(isinstance(relative, str), "path type")
    path = PurePosixPath(relative)
    need(not path.is_absolute() and ".." not in path.parts and str(path) == relative, "canonical path")
    need(not any((root/Path(*path.parts[:i])).is_symlink()
                 for i in range(1, len(path.parts)+1)), "source symlink")
    target = root/path
    need(target.resolve().is_relative_to(root.resolve()) and target.is_file()
         and target.stat().st_size < 1024*1024, "missing/escaping/oversized source")
    return target.read_bytes()


def suppliers():
    sources, graph = {}, {}
    for packet, pin in SUPPLIERS.items():
        folder = ROOT.parent/packet
        data = checked_file(folder, "SOURCE_MANIFEST.json")
        need(digest(data) == pin, "changed supplier manifest")
        manifest = json.loads(data)
        graph.update(manifest.get("requirements", manifest.get("interval_extension_requirements", {})))
        for row in manifest["files"]:
            key = packet, row["path"]
            need(key not in sources and row["path"].startswith("source/"), "supplier identity")
            data = checked_file(folder, row["path"])
            need(digest(data) == row["sha256"], "changed published source")
            sources[key] = data
    need(len(sources) == 852, "published source inventory")
    return sources, graph


def validate(manifest, published, credited):
    need(manifest["schema"] == "kb-shared-carrier-rank-fifteen-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS, "snapshot pins")
    need(manifest["supplier_manifests"] == SUPPLIERS, "supplier pins")
    need(all(manifest[k] == v for k, v in BOUNDS.items()), "scope and bounds")
    need(manifest["inherited_proof_documents_compared"] == 261
         and manifest["published_source_hashes_checked"] == 852, "comparison inventory")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 47, "new source inventory")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()}
    need(actual == set(files), "missing/unlisted source")
    sources = {}
    for relative, row in files.items():
        need(relative == "source/"+row["origin_path"], "origin path")
        path = PurePosixPath(row["origin_path"])
        need(len(path.parts) >= 4 and path.parts[:2] == ("background", "nodes")
             and path.parts[2] in ROOTS, "unexpected source")
        data = checked_file(ROOT, relative)
        need(digest(data) == row["sha256"], "changed new source")
        sources[relative] = data
    need(sum(map(len, sources.values())) == manifest["source_bytes"] == 110889, "new source size")
    documents = {}
    for row in manifest["inherited_sources"]:
        key = row["node"], row["filename"]
        need(key not in documents, "duplicate inherited document")
        data = published[row["packet"], row["path"]]
        parts = PurePosixPath(row["path"]).parts
        need(parts[0] == "source" and parts[2] == "nodes"
             and parts[3] == row["node"] and "/".join(parts[4:]) == row["filename"], "inherited identity")
        need(digest(data) == row["sha256"], "inherited document pin")
        documents[key] = data
    need(len(documents) == 261, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 89 and set(graph) == set(manifest["origin_node_manifest_sha256"]), "closure inventory")
    for name, deps in graph.items():
        if name not in ROOTS:
            need(deps == credited[name], "inherited dependency drift")
            need(all((name, f) in documents for f in ("statement.md", "proof.md")), "missing inherited proof")
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

    visit(ROOTS[-1])
    need(done == set(graph), "unreachable dependency")
    return sources


def mutations(manifest, published, credited):
    cases = []
    replacements = {"schema": "wrong", "parent_commit": "0"*40, "snapshot_roots": [],
                    "supplier_manifests": {}, "inherited_sources": [], **{k: None for k in BOUNDS}}
    for key, value in replacements.items():
        bad = copy.deepcopy(manifest)
        bad[key] = value
        cases.append(bad)
    for key, value in (("path", "../../escape"), ("origin_path", "wrong"), ("sha256", "0"*64)):
        bad = copy.deepcopy(manifest)
        bad["files"][0][key] = value
        cases.append(bad)
    for mutation in ("duplicate", "missing", "cycle", "pin"):
        bad = copy.deepcopy(manifest)
        if mutation == "duplicate":
            bad["files"].append(bad["files"][0])
        elif mutation == "missing":
            bad["files"].pop()
        elif mutation == "cycle":
            bad["requirements"][ROOTS[0]].append(ROOTS[-1])
        else:
            bad["origin_node_manifest_sha256"][ROOTS[0]] = "0"*64
        cases.append(bad)
    for bad in cases:
        try:
            validate(bad, published, credited)
        except (ValueError, KeyError):
            continue
        raise ValueError("accepted malformed manifest")
    return len(cases)


def main():
    data = checked_file(ROOT, "SOURCE_MANIFEST.json")
    need(digest(data) == MANIFEST_HASH, "manifest pin")
    manifest = json.loads(data)
    published, credited = suppliers()
    sources = validate(manifest, published, credited)
    print("PASS 899 listed hashes; 261 inherited proof documents; 89-node acyclic closure;",
          mutations(manifest, published, credited), "malformed manifests rejected", flush=True)
    # Recreate the original relative imports from frozen bytes, never the research tree.
    borrowed = {}
    for packet in ("kb-low-pair-pencil-payment-20260909", "kb-dominant-pencil-rank-eleven-20260909"):
        additions = {path: data for (owner, path), data in published.items() if owner == packet}
        need(not set(borrowed).intersection(additions), "borrowed runtime collision")
        borrowed.update(additions)
    for name in ("mca_raw_margin_basis_mass", "mca_fiber_contraction_core_basis_resource"):
        relative = "source/critical/nodes/"+name+"/verify.py"
        matches = [data for (packet, path), data in published.items() if path == relative]
        need(bool(matches), "missing credited verifier")
        need(relative not in borrowed or borrowed[relative] == matches[-1], "credited verifier drift")
        borrowed[relative] = matches[-1]
    need(not set(borrowed).intersection(sources), "new runtime collision")
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="kb-shared-rank-replay-") as temp:
        runtime = Path(temp)
        for relative, data in {**borrowed, **sources}.items():
            path = runtime/relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        checks = [("background", name, f) for name in ROOTS
                  for f in (("verify.py",) if name == ROOTS[0] else ("verify.py", "verify_audit.py"))]
        checks += [("background", "rate_half_mca_low_pair_pencil_payment", "verify_audit.py"),
                   ("critical", "mca_raw_margin_basis_mass", "verify.py")]
        for section, name, filename in checks:
            path = runtime/"source"/section/"nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=runtime, env=env, check=True, timeout=20)
    print("PASS nine new focused checks plus inherited pencil and raw-margin checks")
    print("Other inherited arithmetic not freshly replayed; independent mathematical review due")
    print("No full degree interval, unrestricted MCA, ordinary LIST or Prize closure")


if __name__ == "__main__":
    main()
