#!/usr/bin/env python3
"""
reorganizar_repo.py — Reorganizador del repositorio DAM-Java-Mastery
Joaquín Ríos Heredia

Crea la nueva estructura de carpetas, mueve todos los .md a su sitio
según temática detectada por keywords, y hace git commit de los cambios.

Uso: python3 reorganizar_repo.py [--dry-run]
"""

import os
import re
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# ── CONFIG ────────────────────────────────────────────────────────────────────

REPO = Path.home() / ".openclaw/workspace/DAM-Java-Mastery"
DRY_RUN = "--dry-run" in sys.argv

# Archivos .py que NO deben estar en el repo — se moverán a _Archive/sistema
ARCHIVOS_SISTEMA = {
    "engine.py", "engine_bak.py", "racha.py", "config.py",
    "generar_inventario.py", "repair_section.py", "reparar_config.py",
    "openclaw_v9.py", "racha.log", "engine.log", "racha_metrics.json",
    "cache.json", "pom.xml"
}

# Nueva estructura
NUEVA_ESTRUCTURA = [
    "01_Java_Core",
    "02_Arquitectura",
    "03_Spring_Ecosystem",
    "04_Bases_de_Datos",
    "05_SRE_DevOps",
    "06_Seguridad",
    "07_BigData_Streaming",
    "08_IA_Agentes",
    "09_Frontend_Mobile",
    "10_Vanguardia",
    "_Review",
    "_Archive",
]

# Reglas de clasificación: (keywords, carpeta_destino)
# Se evalúan en orden — la primera que coincide gana
REGLAS = [
    # Java Core
    (["virtual thread", "virtualthread", "loom", "structured concurrency",
      "records", "pattern matching", "sealed", "java 21", "jvm", "concurrencia",
      "executor", "thread pool", "hilos", "javafx", "factory", "observer",
      "strategy", "patrones", "design pattern"], "01_Java_Core"),

    # Arquitectura
    (["hexagonal", "ddd", "domain driven", "cqrs", "event sourcing",
      "saga", "bounded context", "clean architecture", "arquitectura",
      "monolito", "strangler", "value object", "agregado", "aggregate",
      "outbox", "transactional outbox", "microservicio", "microservice",
      "api gateway", "c4 model", "tolerante a fallo"], "02_Arquitectura"),

    # Spring Ecosystem
    (["spring boot", "spring", "r2dbc", "resilience4j", "circuit breaker",
      "opentelemetry", "micrometer", "actuator", "webflux", "reactive",
      "hibernate", "jpa", "jdbc"], "03_Spring_Ecosystem"),

    # Bases de Datos
    (["postgresql", "mongodb", "redis", "mysql", "sql", "nosql",
      "índice", "indice", "optimización de consul", "bbdd", "base de dato",
      "database", "pl/sql", "plsql"], "04_Bases_de_Datos"),

    # SRE DevOps
    (["kubernetes", "k8s", "docker", "terraform", "ansible", "prometheus",
      "grafana", "observabilidad", "observability", "sre", "chaos",
      "alta disponibilidad", "auto-escal", "service mesh", "loki",
      "ci/cd", "pipeline", "devops", "iac", "infraestructura como código",
      "kafka streams", "kafka stream"], "05_SRE_DevOps"),

    # Seguridad
    (["seguridad", "security", "jwt", "oauth", "zero trust", "tls",
      "vault", "hashicorp", "sbom", "cyclonedx", "devsecops",
      "bastionado", "vulnerabilidad", "supply chain", "secretos",
      "ciberseguridad", "autenticación", "autorización"], "06_Seguridad"),

    # BigData Streaming
    (["kafka", "spark", "flink", "pyspark", "hadoop", "streaming",
      "bigdata", "big data", "data lake", "datalake", "etl",
      "data mesh", "telemetría iot", "telemetria"], "07_BigData_Streaming"),

    # IA Agentes
    (["rag", "embeddings", "langchain", "ollama", "agente", "agent",
      "llm", "ia ", "inteligencia artificial", "computer use",
      "gobernanza ia", "auditoria de codigo generado"], "08_IA_Agentes"),

    # Frontend Mobile
    (["react", "angular", "vue", "frontend", "flutter", "android",
      "kotlin", "móvil", "movil", "i18n", "internacionalización",
      "formulario", "ux", "interfaz"], "09_Frontend_Mobile"),
]


# ── UTILIDADES ─────────────────────────────────────────────────────────────────

def log(msg):
    prefijo = "[DRY-RUN] " if DRY_RUN else ""
    print(f"{prefijo}{msg}")


def limpiar_nombre(ruta: Path) -> str:
    """Extrae un nombre legible del path para clasificación."""
    nombre = ruta.stem.lower()
    # Elimina prefijos de sistema
    nombre = re.sub(r'^(tech_|std_|deep_|doc_|elite_)', '', nombre)
    # Elimina timestamps al final
    nombre = re.sub(r'_\d{6,}$', '', nombre)
    nombre = re.sub(r'_20\d{6}_\d{4,}$', '', nombre)
    return nombre


def leer_titulo(ruta: Path) -> str:
    """Lee el título H1 del documento si existe."""
    try:
        for linea in ruta.read_text(encoding="utf-8", errors="ignore").splitlines()[:5]:
            if linea.startswith("# "):
                return linea[2:].strip().lower()
    except Exception:
        pass
    return ""


def clasificar(ruta: Path) -> str:
    """Devuelve la carpeta destino según el contenido del archivo."""
    nombre = limpiar_nombre(ruta)
    titulo = leer_titulo(ruta)
    texto = f"{nombre} {titulo} {str(ruta).lower()}"

    for keywords, carpeta in REGLAS:
        if any(kw in texto for kw in keywords):
            return carpeta

    return "10_Vanguardia"  # destino por defecto


def mover(origen: Path, destino_dir: Path):
    """Mueve un archivo, resolviendo conflictos de nombre."""
    destino_dir.mkdir(parents=True, exist_ok=True)
    destino = destino_dir / origen.name

    # Si ya existe un archivo con ese nombre, añade sufijo
    if destino.exists() and destino != origen:
        sufijo = datetime.now().strftime("%H%M%S")
        destino = destino_dir / f"{origen.stem}_{sufijo}{origen.suffix}"

    if not DRY_RUN:
        shutil.move(str(origen), str(destino))

    return destino


def git_commit(mensaje: str):
    if DRY_RUN:
        log(f"Git commit simulado: {mensaje}")
        return
    try:
        subprocess.run(["git", "add", "-A"], cwd=REPO, check=True)
        subprocess.run(["git", "commit", "-m", mensaje], cwd=REPO, check=True)
        subprocess.run(["git", "push"], cwd=REPO, check=True)
        log("✅ Git push OK")
    except subprocess.CalledProcessError as e:
        log(f"⚠️  Git error: {e}")


# ── MAIN ───────────────────────────────────────────────────────────────────────

def main():
    if not REPO.exists():
        print(f"❌ Repositorio no encontrado: {REPO}")
        sys.exit(1)

    log(f"📂 Repositorio: {REPO}")
    log(f"🔍 Analizando 134 documentos...\n")

    # 1. Crear nueva estructura de carpetas
    for carpeta in NUEVA_ESTRUCTURA:
        path = REPO / carpeta
        if not path.exists():
            log(f"📁 Creando: {carpeta}/")
            if not DRY_RUN:
                path.mkdir(parents=True, exist_ok=True)

    # 2. Recoger todos los .md excepto README e INVENTARIO
    todos_md = [
        f for f in REPO.rglob("*.md")
        if f.name not in ("README.md", "INVENTARIO_MAESTRO.md", "INVENTARIO_SISTEMA.md")
        and "__pycache__" not in str(f)
        and "venv" not in str(f)
    ]

    movidos = {}  # carpeta_destino -> lista de archivos

    for md in sorted(todos_md):
        # Ignorar los que ya están en la nueva estructura
        partes = md.relative_to(REPO).parts
        if partes[0] in NUEVA_ESTRUCTURA:
            continue

        carpeta_destino = clasificar(md)
        destino_dir = REPO / carpeta_destino
        destino = mover(md, destino_dir)

        movidos.setdefault(carpeta_destino, []).append(md.name)
        log(f"  {'→' if not DRY_RUN else '→?'} {md.relative_to(REPO)}  →  {carpeta_destino}/")

    # 3. Limpiar carpetas vacías antiguas
    carpetas_antiguas = [
        "Arquitectura", "Arquitectura_Vanguardia",
        "BasesDatos", "BasesDatos_AI",
        "BigData_LMSGI", "BigData_Streaming",
        "Core_Backend", "Core_Ingenieria", "Core_Prog",
        "Frontend_UX", "HealthTech", "IA_Agentes",
        "Ingenieria_DAM", "Ingenieria_DAM_Academico",
        "Interfaces_DI", "Interfaces_Movil",
        "Java_Elite", "Otros_Activos_Mastery",
        "PSP", "SRE_Resiliencia", "SRE_Vanguardia",
        "Seguridad", "Seguridad_2026", "Sistemas_IPE",
        "Testing", "Vanguardia_Tech", "Vanguardia_Tech_2026",
        "Production", "Review_Needed",
    ]

    for nombre in carpetas_antiguas:
        carpeta = REPO / nombre
        if carpeta.exists():
            # Solo eliminar si está vacía
            archivos_restantes = list(carpeta.rglob("*"))
            if not archivos_restantes:
                log(f"🗑  Eliminando carpeta vacía: {nombre}/")
                if not DRY_RUN:
                    carpeta.rmdir()
            else:
                log(f"⚠️  {nombre}/ no está vacía ({len(archivos_restantes)} items) — revisar manualmente")

    # 4. Resumen
    print(f"\n{'─'*60}")
    print(f"RESUMEN DE REORGANIZACIÓN")
    print(f"{'─'*60}")
    total = sum(len(v) for v in movidos.values())
    print(f"Total documentos movidos: {total}")
    for carpeta, archivos in sorted(movidos.items()):
        print(f"  {carpeta}/  →  {len(archivos)} documentos")

    if DRY_RUN:
        print(f"\n[DRY-RUN] Ningún archivo fue modificado.")
        print("Ejecuta sin --dry-run para aplicar los cambios.")
        return

    # 5. Git commit
    print()
    git_commit(f"refactor: reorganización temática del repositorio [{datetime.now().strftime('%Y-%m-%d')}]")
    log("✅ Reorganización completada.")


if __name__ == "__main__":
    main()
