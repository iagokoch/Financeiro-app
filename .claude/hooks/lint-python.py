import json
import subprocess
import sys

data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "")

if path.endswith(".py"):
    subprocess.run(
        ["uv", "run", "--project", "backend", "ruff", "check", "--fix", path],
        check=False,
    )

sys.exit(0)
