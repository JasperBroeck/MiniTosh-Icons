#!/usr/bin/env python3
"""Assemble the MiniTosh gallery into _site/.

- Copies site/index.html
- Copies every base icon (regular .svg file) into _site/icons/
- Writes _site/icons.json with each base icon and the names that link to it

Test locally:
    python3 scripts/build-site.py
    python3 -m http.server -d _site
"""
import json
import os
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "apps" / "scalable"
LINKS = SRC / "links"
OUT = ROOT / "_site"


def main():
    if not SRC.is_dir():
        sys.exit(f"Missing folder: {SRC}")

    base = {}      # base name -> source file
    aliases = {}   # base name -> [link names]

    for folder in (SRC, LINKS):
        if not folder.is_dir():
            continue
        for p in sorted(folder.glob("*.svg")):
            if p.is_symlink():
                target = Path(os.path.realpath(p))
                if not target.exists():
                    print(f"warning: broken link skipped: {p.relative_to(ROOT)}")
                    continue
                aliases.setdefault(target.stem, []).append(p.stem)
            else:
                base[p.stem] = p

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "icons").mkdir(parents=True)

    for name, path in base.items():
        shutil.copyfile(path, OUT / "icons" / f"{name}.svg")

    data = [
        {"name": name, "aliases": sorted(set(aliases.get(name, [])), key=str.lower)}
        for name in sorted(base, key=str.lower)
    ]
    (OUT / "icons.json").write_text(json.dumps(data, indent=1), encoding="utf-8")
    shutil.copyfile(ROOT / "site" / "index.html", OUT / "index.html")

    print(f"Built {len(data)} icons into {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
