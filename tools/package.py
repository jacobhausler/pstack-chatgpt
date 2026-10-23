"""Build a Plugin Creator archive from the tracked plugin source."""
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

root = Path(__file__).resolve().parents[1]
source = root / "pstack"
version = json.loads((source / "plugin.json").read_text())["version"]
output = root / "dist" / f"pstack-{version}.zip"
output.parent.mkdir(exist_ok=True)
with ZipFile(output, "w", ZIP_DEFLATED) as archive:
    for path in sorted(source.rglob("*")):
        if not path.is_file() or any(part in {"__pycache__", ".git", "node_modules"} for part in path.parts):
            continue
        if path.suffix == ".pyc" or path.name == ".DS_Store":
            continue
        archive.write(path, path.relative_to(root))
print(output)
