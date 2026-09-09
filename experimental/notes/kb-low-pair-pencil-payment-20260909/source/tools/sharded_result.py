#!/usr/bin/env python3
"""Streaming writer and verifier for large exact-result ledgers."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any, Iterator


SCHEMA = "prize-sharded-result-v1"


class ShardedResultError(RuntimeError):
    """Raised when a sharded result is incomplete, corrupt, or unsafe."""


def _atomic_json(path: Path, payload: dict[str, Any]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True) + "\n"
    )
    os.replace(temporary, path)


class ShardedResultWriter:
    """Write compact JSONL shards and an atomically refreshed manifest."""

    def __init__(
        self,
        directory: Path,
        *,
        metadata: dict[str, Any] | None = None,
        shard_records: int = 5000,
    ) -> None:
        if shard_records <= 0:
            raise ValueError("shard_records must be positive")
        self.directory = Path(directory)
        self.shards_directory = self.directory / "shards"
        self.manifest_path = self.directory / "manifest.json"
        if self.manifest_path.exists():
            raise ShardedResultError(
                f"refusing to overwrite {self.manifest_path}"
            )
        self.shards_directory.mkdir(parents=True, exist_ok=True)
        self.shard_records = shard_records
        self.payload = {
            "schema": SCHEMA,
            "format": "jsonl",
            "complete": False,
            "metadata": metadata or {},
            "total_records": 0,
            "total_bytes": 0,
            "shards": [],
        }
        self._handle = None
        self._temporary = None
        self._final = None
        self._hash = None
        self._records = 0
        self._bytes = 0
        _atomic_json(self.manifest_path, self.payload)

    def _open_shard(self) -> None:
        index = len(self.payload["shards"])
        name = f"part-{index:05d}.jsonl"
        self._final = self.shards_directory / name
        self._temporary = self._final.with_suffix(".jsonl.tmp")
        self._handle = self._temporary.open("wb")
        self._hash = hashlib.sha256()
        self._records = 0
        self._bytes = 0

    def add(self, record: Any) -> None:
        if self.payload["complete"]:
            raise ShardedResultError("writer already completed")
        if self._handle is None:
            self._open_shard()
        line = (
            json.dumps(
                record, sort_keys=True, separators=(",", ":"),
                ensure_ascii=True,
            ) + "\n"
        ).encode()
        self._handle.write(line)
        self._hash.update(line)
        self._records += 1
        self._bytes += len(line)
        if self._records >= self.shard_records:
            self._finish_shard()

    def _finish_shard(self) -> None:
        if self._handle is None:
            return
        self._handle.flush()
        os.fsync(self._handle.fileno())
        self._handle.close()
        os.replace(self._temporary, self._final)
        entry = {
            "path": self._final.relative_to(self.directory).as_posix(),
            "records": self._records,
            "bytes": self._bytes,
            "sha256": self._hash.hexdigest(),
        }
        self.payload["shards"].append(entry)
        self.payload["total_records"] += self._records
        self.payload["total_bytes"] += self._bytes
        _atomic_json(self.manifest_path, self.payload)
        self._handle = None
        self._temporary = None
        self._final = None
        self._hash = None

    def close(self, *, complete: bool = True) -> Path:
        self._finish_shard()
        self.payload["complete"] = bool(complete)
        _atomic_json(self.manifest_path, self.payload)
        return self.manifest_path

    def __enter__(self) -> "ShardedResultWriter":
        return self

    def __exit__(self, exc_type, exc, traceback) -> None:
        self.close(complete=exc_type is None)


def load_manifest(path: Path) -> dict[str, Any]:
    path = Path(path)
    payload = json.loads(path.read_text())
    if payload.get("schema") != SCHEMA or payload.get("format") != "jsonl":
        raise ShardedResultError(f"{path}: schema/format")
    if not isinstance(payload.get("shards"), list):
        raise ShardedResultError(f"{path}: shards")
    return payload


def _shard_path(manifest_path: Path, relative: str) -> Path:
    root = manifest_path.resolve().parent
    path = (root / relative).resolve()
    try:
        path.relative_to(root)
    except ValueError as error:
        raise ShardedResultError(
            f"{manifest_path}: shard escapes result directory: {relative}"
        ) from error
    return path


def verify(
    manifest_path: Path,
    *,
    require_complete: bool = True,
) -> dict[str, int]:
    manifest_path = Path(manifest_path)
    payload = load_manifest(manifest_path)
    if require_complete and payload.get("complete") is not True:
        raise ShardedResultError(f"{manifest_path}: incomplete")
    total_records = 0
    total_bytes = 0
    seen = set()
    for index, entry in enumerate(payload["shards"]):
        if not isinstance(entry, dict):
            raise ShardedResultError(f"{manifest_path}: shard {index}")
        relative = entry.get("path")
        if not isinstance(relative, str) or relative in seen:
            raise ShardedResultError(f"{manifest_path}: shard path {index}")
        seen.add(relative)
        path = _shard_path(manifest_path, relative)
        if not path.is_file():
            raise ShardedResultError(f"{manifest_path}: missing {relative}")
        digest = hashlib.sha256()
        records = 0
        byte_count = 0
        with path.open("rb") as handle:
            for line_number, line in enumerate(handle, 1):
                digest.update(line)
                byte_count += len(line)
                try:
                    json.loads(line)
                except (json.JSONDecodeError, UnicodeDecodeError) as error:
                    raise ShardedResultError(
                        f"{relative}:{line_number}: invalid JSON"
                    ) from error
                records += 1
        if (
            records != entry.get("records")
            or byte_count != entry.get("bytes")
            or digest.hexdigest() != entry.get("sha256")
        ):
            raise ShardedResultError(
                f"{manifest_path}: custody mismatch {relative}"
            )
        total_records += records
        total_bytes += byte_count
    if (
        total_records != payload.get("total_records")
        or total_bytes != payload.get("total_bytes")
    ):
        raise ShardedResultError(f"{manifest_path}: aggregate mismatch")
    return {
        "shards": len(payload["shards"]),
        "records": total_records,
        "bytes": total_bytes,
    }


def iter_records(manifest_path: Path) -> Iterator[Any]:
    """Stream records after a separate successful verify() call."""
    manifest_path = Path(manifest_path)
    payload = load_manifest(manifest_path)
    for entry in payload["shards"]:
        path = _shard_path(manifest_path, entry["path"])
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                yield json.loads(line)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--allow-incomplete", action="store_true")
    args = parser.parse_args()
    try:
        counts = verify(
            args.manifest, require_complete=not args.allow_incomplete
        )
    except ShardedResultError as error:
        print(f"SHARDED_RESULT_FAIL {error}")
        return 1
    print(
        f"SHARDED_RESULT_PASS shards={counts['shards']} "
        f"records={counts['records']} bytes={counts['bytes']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
