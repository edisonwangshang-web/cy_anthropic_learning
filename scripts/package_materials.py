#!/usr/bin/env python3
"""Build the learner workspace archive from its canonical source directory."""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "materials" / "learner-workspace"
TARGET = ROOT / "materials" / "learner-workspace.zip"
ARCHIVE_ROOT = Path("learner-workspace")


def main() -> int:
    files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    if not files:
        raise SystemExit(f"No learner materials found in {SOURCE}")

    with ZipFile(TARGET, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, ARCHIVE_ROOT / path.relative_to(SOURCE))

    print(f"Built {TARGET.relative_to(ROOT)} with {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
