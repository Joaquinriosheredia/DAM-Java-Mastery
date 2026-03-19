import json
import os
from datetime import datetime

config = {
    "meta": {
        "lastTouchedVersion": "2026.3.13",
        "lastTouchedAt": datetime.utcnow().isoformat() + "Z"
    },
    "auth": {
        "profiles": {
            "google:default": {"provider": "google", "mode": "api_key"},
            "openrouter:default": {"provider": "openrouter", "mode": "api_key"}
        }
    },
    "agents": {
        "defaults": {
            "model": {"primary": "ollama/qwen2.5:7b"},
            "workspace": "/home/usuariojoaquin/.openclaw/workspace"
        },
        "list": [
            {
                "id": "main",
                "name": "main",
                "model": "ollama/qwen2.5:7b",
                "workspace": "/home/usuariojoaquin/.openclaw/workspace"
            },
            {
                "id": "analyst",
                "name": "analyst",
                "model": "ollama/qwen2.5:7b",
                "workspace": "/home/usuariojoaquin/.openclaw/workspace"
            },
            {
                "id": "developer",
                "name": "developer",
                "model": "openrouter/deepseek/deepseek-coder",
                "workspace": "/home/usuariojoaquin/.openclaw/workspace"
            },
            {
                "id": "devops",
                "name": "devops",
                "model": "ollama/qwen2.5:7b",
                "workspace": "/home/usuariojoaquin/.openclaw/workspace"
            }
        ]
    },
    "gateway": {
        "port": 18789,
        "mode": "local",
        "bind": "loopback",
        "auth": {"mode": "token", "token": "a720d6730eab43f2fdc9a1fccb789b40e8641a321cd4c98a"}
    }
}

path = os.path.expanduser("~/.openclaw/openclaw.json")
with open(path, "w") as f:
    json.dump(config, f, indent=2)

print("✅ Configuración actualizada correctamente.")
