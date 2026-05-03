#!/usr/bin/env python3
"""
racha.py v13.0 — Director Maestro
Authority Engine — Joaquín Ríos Heredia

Cambios v13.0:
- Compatible con engine.py v20.0 (solo acepta 'tema')
- Elimina ruta_destino y modo como argumentos al engine
- La clasificación temática la hace engine.py internamente
- Mantiene métricas y logging
"""

import sys
import subprocess
import logging
import argparse
import json
from pathlib import Path
from datetime import datetime

# ── Config ────────────────────────────────────────────────────────────────────

BASE_PATH = Path.home()

CONFIG = {
    "engine_path":   BASE_PATH / "AuthorityEngine/engine.py",
    "log_file":      BASE_PATH / "AuthorityEngine/racha.log",
    "metrics_file":  BASE_PATH / "AuthorityEngine/racha_metrics.json",
}

# ── Logging ───────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(CONFIG["log_file"]),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("racha")

# ── Métricas ──────────────────────────────────────────────────────────────────

def guardar_metricas(tema: str, exito: bool, duracion):
    data = []
    if CONFIG["metrics_file"].exists():
        try:
            with open(CONFIG["metrics_file"], "r") as f:
                data = json.load(f)
        except:
            data = []

    data.append({
        "tema":         tema,
        "exito":        exito,
        "duracion_seg": duracion.total_seconds(),
        "timestamp":    datetime.now().isoformat()
    })

    with open(CONFIG["metrics_file"], "w") as f:
        json.dump(data, f, indent=2)

# ── Engine ────────────────────────────────────────────────────────────────────

def ejecutar_engine(tema: str) -> bool:
    """
    Llama a engine.py pasando solo el tema.
    engine.py v20.0 gestiona internamente la ruta y la categoría.
    """
    cmd = ["python3", "-u", str(CONFIG["engine_path"]), tema]
    log.info(f"🚀 Ejecutando: {' '.join(cmd)}")

    try:
        proceso = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        if proceso.stdout:
            for linea in proceso.stdout:
                sys.stdout.write(linea)
                sys.stdout.flush()

        proceso.wait()

        if proceso.returncode != 0:
            log.error(f"❌ Código salida: {proceso.returncode}")
            return False

        return True

    except Exception as e:
        log.exception(f"❌ Error crítico: {e}")
        return False

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="racha.py v13.0 — Genera borrador técnico en _Review/"
    )
    parser.add_argument("tema", help="Tema del documento a generar")
    parser.add_argument("--dry-run", action="store_true",
                        help="Simula la ejecución sin generar nada")

    args = parser.parse_args()
    tema = args.tema
    start = datetime.now()

    log.info(f"--- RACHA: {tema} ---")

    if not CONFIG["engine_path"].exists():
        log.error("❌ engine.py no encontrado")
        sys.exit(1)

    print(f"🎯 {tema}")
    print(f"📂 Destino: _Review/ → carpeta temática tras revisión Claude")

    if args.dry_run:
        print("🔍 Dry-run: sin cambios")
        sys.exit(0)

    exito = ejecutar_engine(tema)

    duracion = datetime.now() - start
    guardar_metricas(tema, exito, duracion)

    log.info(f"⏱ Tiempo: {duracion}")

    if exito:
        print(f"\n✅ Borrador en _Review/ — descárgalo de GitHub y adjúntalo a Claude")
    else:
        print(f"\n❌ ERROR — revisa ~/AuthorityEngine/racha.log")

# ── Entry ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
