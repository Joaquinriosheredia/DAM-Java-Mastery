#!/usr/bin/env python3
"""
racha.py v10.1 — Orquestador del Authority Engine
Clasificación por scoring con prioridades.
Importa configuración desde config.py — cero duplicación.
"""

import sys
import os
import subprocess
import logging
from pathlib import Path
from datetime import datetime

# Importar configuración centralizada
from config import CONFIG, FOLDER_PRIORITIES

# Setup logging
LOG_FILE = CONFIG["author_engine"] / "racha.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
log = logging.getLogger("racha")

def sanitizar_tema(tema: str) -> str:
    """
    Elimina caracteres de control que corrompen logs.
    Colapsa whitespace, elimina \n \t \r.
    """
    return " ".join(tema.split())

def match_keyword(keyword: str, texto: str) -> bool:
    """
    Matching por substring normalizado (sin regex).
    "kafka" matchea en "kafka streaming"
    "test" NO matchea en "testing" (porque "test" fue eliminado del config)
    """
    return keyword.lower() in texto.lower()

def clasificar_tema(tema: str) -> str:
    """
    Clasificación por scoring con max().
    Score = (prioridad * 100) + (len(keyword) * 2)
    Gana el score más alto — no el primero que aparece.
    
    Ejemplo: "Kafka streaming con testing y resiliencia"
    - kafka: (10 * 100) + (5 * 2) = 1010 → BigData_Streaming
    - streaming: (7 * 100) + (9 * 2) = 718 → BigData_Streaming
    - testing: (5 * 100) + (7 * 2) = 514 → Testing
    - resiliencia: (7 * 100) + (11 * 2) = 722 → SRE_Resiliencia
    ✅ Gana: kafka (1010) → BigData_Streaming
    
    SIN filtro de carpetas_reales — mkdir crea la carpeta si no existe.
    """
    tema_lower = tema.lower()
    mejor_score = -1
    mejor_folder = "Core_Backend"
    mejor_keyword = None
    todos_candidatos = []
    
    # Evaluar TODAS las keywords (SIN filtro de carpetas)
    for keyword, (folder, prioridad) in FOLDER_PRIORITIES.items():
        if match_keyword(keyword, tema_lower):
            score = (prioridad * 100) + (len(keyword) * 2)
            todos_candidatos.append({
                "keyword": keyword,
                "folder": folder,
                "prioridad": prioridad,
                "score": score
            })
            
            if score > mejor_score:
                mejor_score = score
                mejor_folder = folder
                mejor_keyword = keyword
    
    # Log de todos los candidatos (para debug)
    if todos_candidatos:
        todos_candidatos.sort(key=lambda x: x["score"], reverse=True)
        for c in todos_candidatos[:5]:  # Top 5
            log.info(f"🔍 Candidato: '{c['keyword']}' → {c['folder']} (prioridad={c['prioridad']}, len={len(c['keyword'])}, score={c['score']})")
        
        log.info(f"✅ MATCH FINAL: '{mejor_keyword}' → {mejor_folder} (score={mejor_score})")
    else:
        log.warning(f"⚠️ No match encontrado, usando default: Core_Backend")
    
    return mejor_folder

def ejecutar_engine(tema: str, ruta_destino: str, modo: str, secciones: int = None) -> bool:
    """Ejecuta engine.py con subprocess seguro y streaming en tiempo real."""
    script_motor = CONFIG["author_engine"] / "engine.py"

    cmd = ["python3", "-u", str(script_motor), tema, str(ruta_destino), modo]
    if secciones:
        cmd.append(str(secciones))

    log.info(f"🚀 Ejecutando: {' '.join(cmd)}")

    try:
        proceso = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        for linea in proceso.stdout:
            sys.stdout.write(linea)
            sys.stdout.flush()
            log.info(linea.strip())

        proceso.wait(timeout=3600)
        return proceso.returncode == 0

    except subprocess.TimeoutExpired:
        log.error("⏰ engine.py excedió el timeout de 1 hora")
        proceso.kill()
        return False
    except Exception as e:
        log.error(f"❌ Error ejecutando engine.py: {e}")
        return False

def main():
    log.info("=" * 60)
    log.info(f"Iniciando racha.py v10.1: {' '.join(sys.argv[1:])}")
    log.info("=" * 60)
    
    if len(sys.argv) < 2:
        print("❌ Uso: racha '[Tema]' [deep/std/manual] [--sections N] [--dry-run]")
        sys.exit(1)

    # Sanitizar tema (elimina caracteres de control)
    tema = sanitizar_tema(sys.argv[1])
    
    modo = "std"
    secciones_personalizadas = None
    dry_run = False
    
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.lower() in ["deep", "std", "manual"]:
            modo = arg.lower()
        elif arg == "--sections" and i + 1 < len(sys.argv):
            try:
                secciones_personalizadas = int(sys.argv[i + 1])
                i += 1
            except ValueError:
                pass
        elif arg == "--dry-run":
            dry_run = True
        i += 1

    if not CONFIG["repo_base"].exists():
        log.error(f"❌ Repositorio no encontrado: {CONFIG['repo_base']}")
        sys.exit(1)

    # SIN filtro de carpetas_reales — clasificamos primero, creamos después
    destino = clasificar_tema(tema)
    ruta_absoluta = CONFIG["repo_base"] / destino
    ruta_absoluta.mkdir(parents=True, exist_ok=True)  # Crea la carpeta si no existe
    
    log.info(f"🎯 Destino: {destino} → {ruta_absoluta}")
    print(f"🎯 [Director] Destino detectado: {destino}")
    
    if secciones_personalizadas:
        print(f"📊 [Config] Secciones personalizadas: {secciones_personalizadas}")
    
    if dry_run:
        print(f"🔍 [Dry-Run] Clasificación completada — no se ejecutó engine.py")
        log.info("✅ Dry-run completado exitosamente")
        sys.exit(0)  # ← Consistente con el resto del flujo

    exito = ejecutar_engine(tema, str(ruta_absoluta), modo, secciones_personalizadas)
    
    log.info("=" * 60)
    if exito:
        log.info("✅ PROCESO COMPLETADO EXITOSAMENTE")
        print("✅ [Racha] Proceso completado exitosamente")
    else:
        log.error("❌ PROCESO FALLÓ — Revisar logs para detalles")
        print("❌ [Racha] Proceso falló — Revisar logs en ~/AuthorityEngine/racha.log")
        sys.exit(1)

if __name__ == "__main__":
    main()
