"""Verify frozen suppliers and six focused checks, not mathematical acceptance."""

import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
MANIFEST_HASH = "c17dcfa6c844ceb0ae5f1a5bd578f4edd7b58d10048ae317528bfd37ebad43ce"
PARENT = "d8e33c45a79f90f5345df20c0670a55743f1692e"
ROOTS = ["mca_joint_pair_affine_incidence", "rate_half_mca_low_pair_affine_span_payment",
         "mca_compatible_domain_tuple_refund", "rate_half_mca_low_pair_pencil_payment"]
SUPPLIERS = {
    "low-core-flat-source-cumulative-20260908": "656b342982896233bf8f906b6ba93aae785c9179414d02f982f47b095a60027b",
    "kb-parameter-graph-spread-20260908": "b93f34d83b297e4370a4d6cb3b949432f99ebb4293b059fc7a926fd6b427ce1c",
    "kb-low-defect-rank-filtration-20260909": "bc3b337d2c369a06ab82d5d6d5a2fa8f9edfe2931f34e0244b94345286d42645",
    "kb-raw-mass-cubic-interval-20260909": "375c15045f34386d787b559a8705fc1c1f66653ce5a6568630a2d0f79ee75bbc",
}
HELPERS = {"tools/sharded_result.py",
           "background/nodes/list_padded_johnson_dimension_descent/compiler.py"}


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
    sources, graph, count = {}, {}, 0
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
            count += 1
    need(count == 769, "published source inventory")
    return sources, graph


def validate(manifest, published, credited):
    need(manifest["schema"] == "kb-low-pair-pencil-payment-v1", "schema")
    need(manifest["parent_commit"] == PARENT and manifest["snapshot_roots"] == ROOTS, "snapshot pins")
    need(manifest["supplier_manifests"] == SUPPLIERS, "supplier pins")
    need(manifest["pair_span_bound"] == 257846243054097181
         and manifest["pencil_bound"] == 274136923022229951
         and manifest["pencil_reserve"] == 843805089165136
         and manifest["remaining_J"] == [9965, 21499], "scope and bounds")
    need(manifest["inherited_proof_documents_compared"] == 242
         and manifest["published_source_hashes_checked"] == 769, "comparison inventory")
    files = {row["path"]: row for row in manifest["files"]}
    need(len(files) == len(manifest["files"]) == 47, "new source inventory")
    actual = {str(p.relative_to(ROOT)) for p in (ROOT/"source").rglob("*") if p.is_file()}
    need(actual == set(files), "missing/unlisted source")
    sources = {}
    for relative, row in files.items():
        need(relative == "source/"+row["origin_path"], "origin path")
        path = PurePosixPath(row["origin_path"])
        need(str(path) in HELPERS or (len(path.parts) >= 4 and path.parts[:2] == ("background", "nodes")
                                     and path.parts[2] in ROOTS), "unexpected source")
        data = checked_file(ROOT, relative)
        need(digest(data) == row["sha256"], "changed new source")
        sources[relative] = data
    documents = {}
    for row in manifest["inherited_sources"]:
        key = row["node"], row["filename"]
        need(key not in documents, "duplicate inherited document")
        data = published[row["packet"], row["path"]]
        parts = PurePosixPath(row["path"]).parts
        need(parts[:1] == ("source",) and parts[2] == "nodes"
             and parts[3] == row["node"] and "/".join(parts[4:]) == row["filename"], "inherited identity")
        need(digest(data) == row["sha256"], "inherited document pin")
        documents[key] = data
    need(len(documents) == 242, "inherited proof inventory")
    graph = manifest["requirements"]
    need(len(graph) == 80 and set(graph) == set(manifest["origin_node_manifest_sha256"]), "closure inventory")
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


def mutations(manifest, published, credited):
    cases = []
    for key, value in (("schema", "wrong"), ("parent_commit", "0"*40),
                       ("snapshot_roots", []), ("supplier_manifests", {}),
                       ("pair_span_bound", 0), ("pencil_bound", 0),
                       ("pencil_reserve", 0), ("remaining_J", [1, 21499]),
                       ("inherited_sources", [])):
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
    validate(manifest, published, credited)
    print("PASS 816 listed hashes; 242 inherited proof documents; 80-node acyclic closure;",
          mutations(manifest, published, credited), "malformed manifests rejected", flush=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    for name in ROOTS:
        filenames = ("verify.py", "verify_audit.py") if name in (ROOTS[1], ROOTS[3]) else ("verify.py",)
        for filename in filenames:
            path = ROOT/"source/background/nodes"/name/filename
            command = [sys.executable, "-B"]+(["-O"] if sys.flags.optimize else [])+[str(path)]
            subprocess.run(command, cwd=ROOT, env=env, check=True, timeout=20)
    print("PASS six focused checks; inherited arithmetic suites not freshly replayed")
    print("External mathematical review due; unrestricted MCA, LIST and both Prizes remain open")


if __name__ == "__main__":
    main()
