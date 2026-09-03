import json
import re
import sys

data = json.load(sys.stdin)
command = data.get("tool_input", {}).get("command", "")

if re.search(r"\.env\b", command) and not re.search(r"\.env\.example\b", command):
    print(
        "BLOCKED: comando tenta acessar o .env real. Segredos não podem passar pelo contexto do agente.",
        file=sys.stderr,
    )
    sys.exit(2)

sys.exit(0)
