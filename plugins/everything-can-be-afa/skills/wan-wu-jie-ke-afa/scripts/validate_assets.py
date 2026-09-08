#!/usr/bin/env python3
"""Validate an Afa reference-asset manifest without third-party packages."""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
import sys
from pathlib import Path


SUPPORTED = {".jpg", ".jpeg", ".png", ".webp"}


def image_size(path: Path) -> tuple[int, int] | None:
    data = path.read_bytes()[:32]
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        return struct.unpack(">II", data[16:24])
    if data[:2] == b"\xff\xd8":
        with path.open("rb") as fh:
            fh.read(2)
            while True:
                marker = fh.read(1)
                if not marker:
                    return None
                if marker != b"\xff":
                    continue
                code = fh.read(1)
                while code == b"\xff":
                    code = fh.read(1)
                if code in {bytes([x]) for x in range(0xC0, 0xC4)} | {bytes([x]) for x in range(0xC5, 0xC8)} | {bytes([x]) for x in range(0xC9, 0xCC)} | {bytes([x]) for x in range(0xCD, 0xD0)}:
                    length = int.from_bytes(fh.read(2), "big")
                    segment = fh.read(length - 2)
                    if len(segment) >= 5:
                        return int.from_bytes(segment[3:5], "big"), int.from_bytes(segment[1:3], "big")
                    return None
                length_bytes = fh.read(2)
                if len(length_bytes) != 2:
                    return None
                fh.seek(int.from_bytes(length_bytes, "big") - 2, 1)
    return None


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    manifest_path = args.manifest.resolve()
    root = manifest_path.parent
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    hashes: dict[str, str] = {}

    for item in data.get("assets", []):
        slot = item.get("slot", "<unnamed>")
        raw_path = item.get("path")
        if not raw_path:
            message = f"{slot}: path is empty"
            (errors if item.get("required") else warnings).append(message)
            continue
        path = (root / raw_path).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            errors.append(f"{slot}: path escapes assets directory")
            continue
        if not path.is_file():
            errors.append(f"{slot}: file not found: {raw_path}")
            continue
        if path.suffix.lower() not in SUPPORTED:
            errors.append(f"{slot}: unsupported type {path.suffix}")
            continue
        file_hash = digest(path)
        if file_hash in hashes:
            warnings.append(f"{slot}: duplicates {hashes[file_hash]}")
        else:
            hashes[file_hash] = slot
        size = image_size(path)
        if size is None:
            warnings.append(f"{slot}: dimensions unavailable; inspect manually")
        elif max(size) < int(item.get("min_long_edge", 0)):
            errors.append(f"{slot}: {size[0]}x{size[1]} is below the required long edge")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {len(data.get('assets', []))} slots: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
