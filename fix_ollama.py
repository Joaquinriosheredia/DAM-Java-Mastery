import json
import os
from datetime import datetime

# Carga el JSON actual
path = os.path.expanduser("~/.openclaw/openclaw.json")
with open(path, "r") as f:
    config = json.load(f)

# Elimina el perfil de ollama si existe (no se necesita)
if "ollama:default" in config.get("auth", {}).get("profiles", {}):
    del config["auth"]["profiles"]["ollama:default"]

# Asegura que defaults y list usen el modelo correcto sin provider explícito para Ollama
for agent in config["agents"]["list"]:
    if "ollama" in agent["model"]:
        # Ollama usa solo el modelo directo, sin "provider" separado
        if "provider" in agent:
            del agent["provider"]

# Fallback global a Ollama
config["agents"]["defaults"]["model"]["primary"] = "ollama/qwen2.5:7b"

# Guarda el JSON limpio
with open(path, "w") as f:
    json.dump(config, f, indent=2)

print("✅ JSON corregido: perfil de Ollama eliminado (no necesita auth).")
print("Prueba ahora con devops.")
