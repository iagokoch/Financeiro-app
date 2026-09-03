import json
import os
import sys
import time

PROTECTED = ["app/core/", "app/modules/auth/"]
UNLOCK_FILE = os.path.join(os.path.dirname(__file__), "..", "UNLOCK_EDIT")
UNLOCK_TTL_SECONDS = 15 * 60  # unlock expira em 15 min se não for usado


def is_unlocked():
    if not os.path.exists(UNLOCK_FILE):
        return False
    return (time.time() - os.path.getmtime(UNLOCK_FILE)) <= UNLOCK_TTL_SECONDS


data = json.load(sys.stdin)
path = data.get("tool_input", {}).get("file_path", "").replace("\\", "/")

if any(p in path for p in PROTECTED):
    if is_unlocked():
        os.remove(UNLOCK_FILE)  # consome o unlock, vale só 1 edição
        sys.exit(0)
    print(
        f"BLOCKED: '{path}' está em área protegida (core/ ou modules/auth/). "
        "Peça ao Iago para rodar o unlock no terminal antes de tentar de novo.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
