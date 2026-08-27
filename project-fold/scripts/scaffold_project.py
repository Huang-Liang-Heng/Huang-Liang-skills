# -*- coding: utf-8 -*-
"""Project Fold v3 scaffold.

Usage:
    python scaffold_project.py <root> [small|standard|large] [generic|software|research|data|framework]

Creates only missing control-layer files/directories. It never moves or overwrites existing project assets.
"""
from pathlib import Path
import shutil
import sys

root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
profile = (sys.argv[2] if len(sys.argv) > 2 else "standard").lower()
kind = (sys.argv[3] if len(sys.argv) > 3 else "generic").lower()

# backward compatibility
if profile == "paper":
    profile = "large"

profiles = {
    "small": ["notes"],
    "standard": ["notes", ".handoff", "workspace"],
    "large": ["notes", ".handoff", "workspace/human", "workspace/ai"],
}

kind_dirs = {
    "generic": [],
    "software": ["src", "tests", "docs"],
    "research": ["inputs", "scripts", "outputs", "paper"],
    "data": ["inputs", "interim", "processed", "analysis", "outputs"],
    "framework": ["references", "materials", "components", "deliverables"],
}

if profile not in profiles:
    raise SystemExit("profile 必须是 small / standard / large")
if kind not in kind_dirs:
    raise SystemExit("kind 必须是 generic / software / research / data / framework")

root.mkdir(parents=True, exist_ok=True)
created = []

for rel in profiles[profile] + kind_dirs[kind]:
    path = root / rel
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        created.append(str(path))

skill_root = Path(__file__).resolve().parents[1]
template_dir = skill_root / "templates"
for name in ["PROJECT_MODEL.md", "PROJECT_STATE.md", "PROJECT_CONTEXT.md"]:
    dst = root / name
    if not dst.exists():
        shutil.copyfile(template_dir / name, dst)
        created.append(str(dst))

# Architecture is useful by default only for large projects; AI may later remove/ignore it if unnecessary.
if profile == "large":
    dst = root / "ARCHITECTURE.md"
    if not dst.exists():
        shutil.copyfile(template_dir / "ARCHITECTURE.md", dst)
        created.append(str(dst))

print("\n".join(created))
