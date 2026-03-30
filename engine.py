import os
import sys
import json
import time
import shutil
import hashlib
import logging
import tempfile
import threading
import subprocess
import requests
import re

from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tavily import TavilyClient

# ================== CONFIGURACIÓN DINÁMICA (SRE) ==================
# Resolución dinámica del HOME para evitar hardcoding y asegurar portabilidad
HOME_DIR = Path.home()

CONFIG = {
    "OLLAMA_URL": "http://localhost:11434/api/generate",
    "MODEL": "qwen2.5:14b",
    "TAVILY_KEY": os.environ.get("TAVILY_KEY"),
    "REPO_ROOT": str(HOME_DIR / ".openclaw" / "workspace" / "DAM-Java-Mastery"),
    "CACHE_FILE": str(HOME_DIR / "AuthorityEngine" / "cache.json"),
    "SKILL_ARCHIVO": str(HOME_DIR / "AuthorityEngine" / "skills" / "skill_informe_40pag.md"),
    "LOG_FILE": str(HOME_DIR / "AuthorityEngine" / "engine.log"),
    "CACHE_TTL": 86400,  # 24 horas de validez para la investigación web
    "MAX_WORKERS": 4,    # Optimizado para los núcleos del Ryzen 7 5700X
    "RETRIES": 3,
    "MIN_WORDS": 400,
    "DRY_RUN": False
}

# ================== LOGGING PROFESIONAL ==================
os.makedirs(os.path.dirname(CONFIG["LOG_FILE"]), exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(CONFIG["LOG_FILE"], encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)

def log(msg, level="info"):
    getattr(logging, level)(msg)

# ================== AUDITOR SRE (CALIDAD TÉCNICA) ==================
def calcular_sre_score(resultados):
    """
    Evalúa la calidad del contenido generado basándose en criterios de Staff Engineer.
    Penaliza placeholders, falta de código o brevedad excesiva.
    """
    if not resultados: 
        return 0
    score_total = 0
    for texto in resultados.values():
        s = 100
        # Penalización por falta de bloques de código
        if "```" not in texto: 
            s -= 30
        # Penalización por marcadores de posición (placeholders)
        if re.search(r'\b(TODO|FIXME|PENDIENTE|IMPLEMENTAR)\b', texto.upper()): 
            s -= 20
        # Penalización por densidad de contenido insuficiente
        if len(texto.split()) < CONFIG["MIN_WORDS"]: 
            s -= 20
        score_total += max(0, s)
    return score_total // len(resultados)

# ================== GESTIÓN DE CACHÉ ATÓMICA ==================
cache_lock = threading.Lock()

def gestionar_cache(tema, datos=None):
    """
    Maneja la persistencia de investigaciones web para optimizar el uso de la API de Tavily.
    Utiliza un Lock para evitar condiciones de carrera en modo multihilo.
    """
    with cache_lock:
        cache = {}
        if os.path.exists(CONFIG["CACHE_FILE"]):
            try:
                with open(CONFIG["CACHE_FILE"], "r", encoding="utf-8") as f:
                    cache = json.load(f)
            except: 
                pass
        
        key = hashlib.md5(tema.encode()).hexdigest()
        
        # Guardar en caché si se proporcionan datos nuevos
        if datos:
            cache[key] = {"data": datos, "ts": time.time()}
            with open(CONFIG["CACHE_FILE"], "w", encoding="utf-8") as f:
                json.dump(cache, f, indent=2, ensure_ascii=False)
            return datos
        
        # Recuperar de la caché si no ha expirado (TTL)
        entry = cache.get(key)
        if entry and (time.time() - entry["ts"] < CONFIG["CACHE_TTL"]):
            return entry["data"]
            
    return None

# ================== INVESTIGACIÓN Y MOTOR IA ==================
def investigar_web(tema):
    """Realiza una búsqueda avanzada del estado del arte para alimentar el contexto de la IA."""
    log(f"Investigando en la red: {tema}")
    if not CONFIG["TAVILY_KEY"]: 
        return "Contexto limitado offline."
    try:
        tavily = TavilyClient(api_key=CONFIG["TAVILY_KEY"])
        res = tavily.search(query=f"{tema} high level architecture 2026 benchmarks", search_depth="advanced")
        return "\n".join([r['content'] for r in res['results']])
    except Exception as e:
        log(f"Error Tavily: {e}", "warning")
        return "Contexto técnico general."

def call_ollama(prompt):
    """Envía peticiones al modelo local con lógica de reintentos y filtro de idioma."""
    for i in range(CONFIG["RETRIES"]):
        try:
            r = requests.post(
                CONFIG["OLLAMA_URL"],
                json={
                    "model": CONFIG["MODEL"], 
                    "prompt": prompt, 
                    "stream": False, 
                    "options": {"temperature": 0.2, "num_predict": 4096}
                },
                timeout=600
            )
            text = r.json().get("response", "").strip()
            
            # Filtro de seguridad para detectar fugas de idiomas asiáticos (Qwen Leak)
            if re.search(r'[\u3040-\u30ff\u4e00-\u9fff\uac00-\ud7af]', text):
                log("Fuga de idioma detectada en el output. Reintentando...", "warning")
                continue
                
            return text
            
        except Exception as e:
            log(f"Error en el motor IA (Intento {i+1}): {e}", "warning")
            
    return "ERROR: La generación ha fallado tras múltiples reintentos."

def seleccionar_secciones_inteligentes(tema, num_secciones, todas_las_secciones):
    """Infiere qué módulos técnicos son más pertinentes para el tema actual mediante IA."""
    prompt = f"""Analiza el tema '{tema}' y selecciona las {num_secciones} secciones más relevantes de esta lista:
    {chr(10).join(f"{i+1}. {s}" for i, s in enumerate(todas_las_secciones))}
    Responde ÚNICAMENTE con los números separados por coma (ej: 1,4,5)."""
    try:
        respuesta = call_ollama(prompt)
        numeros = [int(x.strip()) for x in respuesta.split(',') if x.strip().isdigit()]
        seleccionadas = [todas_las_secciones[n-1] for n in numeros if 1 <= n <= len(todas_las_secciones)]
        
        # Relleno de seguridad para asegurar que el informe no quede incompleto
        while len(seleccionadas) < num_secciones:
            for sec in todas_las_secciones:
                if sec not in seleccionadas:
                    seleccionadas.append(sec)
                    if len(seleccionadas) == num_secciones: break
                    
        return seleccionadas[:num_secciones]
    except:
        return todas_las_secciones[:num_secciones]

# ================== SEGURIDAD OPERATIVA Y GIT ==================
def safe_write(path, content):
    """Implementa escritura atómica para evitar archivos corruptos si el proceso se interrumpe."""
    folder = os.path.dirname(path)
    os.makedirs(folder, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", dir=folder, delete=False, encoding="utf-8") as tmp:
        tmp.write(content)
        temp_name = tmp.name
    # os.replace es atómico dentro de la misma partición
    os.replace(temp_name, path)

def git_sync_and_push(msg):
    """Protocolo de sincronización SRE para garantizar un historial de Git limpio y sin conflictos."""
    if CONFIG["DRY_RUN"]: 
        return log("Modo DRY_RUN activo: No se realizará el empuje a GitHub.")
        
    try:
        os.chdir(CONFIG["REPO_ROOT"])
        log("Sincronizando con el repositorio remoto (Pull Rebase)...")
        # Pull con rebase para evitar commits de merge innecesarios
        subprocess.run(["git", "pull", "--rebase", "origin", "main"], check=True, capture_output=True, timeout=120)
        
        # Verificar si hay cambios pendientes antes de proceder
        if not subprocess.check_output(["git", "status", "--porcelain"]): 
            return log("No hay cambios locales para subir. El repositorio ya está al día.")
            
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True, timeout=120)
        
        log("Activo sincronizado con éxito en GitHub.", "success")
        
    except Exception as e:
        log(f"Error crítico en el flujo de Git: {e}", "error")

# ================== GENERACIÓN ASÍNCRONA (v16.2 VISUAL) ==================
def generate_section(sec, tema, contexto, skill_txt):
    """Genera un capítulo individual con feedback visual en tiempo real."""
    log(f" ⚙️  [TRABAJANDO] Generando sección: {sec}...", "info")
    
    prompt = f"""{skill_txt}
    CONTEXTO EXTERNO: {contexto}
    TAREA: Escribe el capítulo técnico '{sec}' para el manual '{tema}'.
    REQUISITOS CRÍTICOS (SRE):
    1. PROHIBICIÓN DE PLACEHOLDERS (TODO, FIXME, implementar).
    2. CÓDIGO EJECUTABLE: Usa Java 21 o Python 3.12 según corresponda.
    3. DIAGRAMAS MERMAID: Usa 'flowchart TD'. Subgraphs deben terminar en _Box.
    4. TONO: Directo, Staff Engineer, orientado a métricas y arquitectura."""

    inicio_seccion = time.time()
    content = call_ollama(prompt)
    
    if len(content.split()) < CONFIG.get("MIN_WORDS", 400):
        log(f" ⚠️  Densidad baja en '{sec}'. Reintentando extensión...", "warning")
        content = call_ollama(prompt + "\nPOR FAVOR: Proporciona una explicación mucho más técnica y detallada.")

    tiempo_sec = round(time.time() - inicio_seccion, 2)
    log(f" ✅ [FINALIZADO] {sec} (Completado en {tiempo_sec}s)", "info")
    
    return sec, content

def generate_report(tema, ruta_destino, modo, secciones_param=None):
    """Orquestador con Feedback de Fases."""
    log(f"🚀 [FASE 1] Iniciando Factory v16.2: {tema.upper()}")
    os.makedirs(ruta_destino, exist_ok=True)

    # 1. Carga de Skill
    skill_txt = ""
    if os.path.exists(CONFIG["SKILL_ARCHIVO"]):
        with open(CONFIG["SKILL_ARCHIVO"], "r", encoding="utf-8") as f:
            skill_txt = f.read()
    else:
        log(" ⚠️  No se encontró el archivo de Skill. Usando base.", "warning")

    # 2. Obtención de Contexto
    log(f"🔍 [FASE 2] Radar activado. Consultando la red (Tavily)...", "info")
    contexto = gestionar_cache(tema) or investigar_web(tema)
    gestionar_cache(tema, contexto)
    log(f" 📡 [FASE 3] Contexto recibido ({len(contexto)} bytes). Mapeando hilos...")

    # 3. Construcción del Sándwich
    inicio = ["Visión Estratégica y ROI 2026", "Análisis del Estado del Arte", "Arquitectura de Componentes (Mermaid)"]
    fin = ["Roadmap de Evolución y Conclusiones Senior"]
    carpeta_destino = os.path.basename(os.path.normpath(ruta_destino))
    
    menus_tecnicos = {
        "Core_Backend": ["Implementación Core de Alto Rendimiento", "Patrones de Diseño Avanzados", "Gestión de Concurrencia"],
        "Cloud_DevOps": ["Escalabilidad Horizontal", "Estrategias de Caching", "Despliegue Continuo"],
        "Seguridad": ["Seguridad Avanzada y Gestión de Secretos", "Threat Modeling", "Arquitectura Zero Trust"],
        "BigData_Streaming": ["Procesamiento de Eventos Kafka", "Data Mesh", "Optimización Spark"],
        "IA_Agentes": ["Arquitecturas RAG", "Ingeniería de Prompts", "Fine-tuning"],
        "Arquitectura": ["DDD Profundo", "CQRS y Event Sourcing", "Arquitectura Hexagonal"],
        "SRE_Resiliencia": ["Testing QA SRE", "Observabilidad OpenTelemetry", "Chaos Engineering"]
    }
    menu_default = ["Implementación Core", "Developer Experience (DX)", "Networking Avanzado"]
    opciones_relleno = menus_tecnicos.get(carpeta_destino, menu_default)

    num_total = secciones_param if secciones_param else (16 if modo == "deep" else 7)
    num_relleno = max(0, num_total - len(inicio) - len(fin))
    relleno = opciones_relleno[:num_relleno]
    secciones_finales = inicio + relleno + fin

    # 4. Fase de Ejecución Paralela
    log(f"🧵 [FASE 4] Desplegando {CONFIG['MAX_WORKERS']} trabajadores para {len(secciones_finales)} capítulos.")
    
    results = {}
    with ThreadPoolExecutor(max_workers=CONFIG["MAX_WORKERS"]) as executor:
        futures = {executor.submit(generate_section, s, tema, contexto, skill_txt): s for s in secciones_finales}
        for f in as_completed(futures):
            sec, res = f.result()
            results[sec] = res

    log(f"📝 [FASE 5] Consolidando documento y ejecutando Auditoría SRE...")


    # 5. Ensamblado, Auditoría y Publicación
    score = calcular_sre_score(results)
    header = f"# {tema.upper()}\n\n**Documentación Técnica de Referencia | Autor: Joaquín Ríos Heredia (Staff Engineer)**\n**Repositorio:** [DAM-Java-Mastery](https://github.com/Joaquinriosheredia/DAM-Java-Mastery)\n**SRE Score: {score}/100**\n\n---\n"
    
    # Mantener el orden semántico original
    full_content = header
    for i, s in enumerate(secciones_finales, 1):
        full_content += f"## {i}. {s}\n\n{results.get(s, 'Fallo en la generación de este capítulo.')}\n\n"

    # Generación de nombre de archivo con marca de tiempo
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_fichero = f"{modo}_{tema.lower().replace(' ','_')}_{timestamp}.md"
    ruta_fichero = os.path.join(ruta_destino, nombre_fichero)
    
    safe_write(ruta_fichero, full_content)

    # Empuje final a GitHub
    git_sync_and_push(f"docs({modo}): {tema} (SRE Score: {score})")

# ================== ENRUTADOR AUTOMÁTICO Y CLI ==================
def obtener_ruta_automatica(tema):
    base = "/home/usuariojoaquin/.openclaw/workspace/DAM-Java-Mastery"
    t = tema.lower()
    if any(x in t for x in ["java", "backend", "spring", "api", "maven"]): return f"{base}/Core_Backend"
    if any(x in t for x in ["seguridad", "ciber", "hacking", "oauth2"]): return f"{base}/Seguridad"
    if any(x in t for x in ["cloud", "devops", "kubernetes", "docker"]): return f"{base}/Cloud_DevOps"
    if any(x in t for x in ["sre", "resiliencia", "grafana", "prometheus"]): return f"{base}/SRE_Resiliencia"
    if any(x in t for x in ["ia", "agente", "python", "ollama"]): return f"{base}/IA_Agentes"
    if any(x in t for x in ["seo", "marketing", "web"]): return f"{base}/SEO_Marketing"
    return f"{base}/Core_Backend"

if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[2].lower() == "deep":
        tema = sys.argv[1]
        ruta = obtener_ruta_automatica(tema)
        log(f"MODO DEEP: 16 secciones en {ruta}")
        generate_report(tema, ruta, "deep", 16)
    elif len(sys.argv) == 2:
        tema = sys.argv[1]
        ruta = obtener_ruta_automatica(tema)
        log(f"MODO MANUAL: 7 secciones en {ruta}")
        generate_report(tema, ruta, "manual", 7)
    elif len(sys.argv) >= 4:
        generate_report(sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv)>4 else None)
