#!/usr/bin/env python3
"""
engine.py v21.0 — Motor de Autoridad con GPU + Prompts Dinámicos
Authority Engine — Joaquín Ríos Heredia

Cambios v21.0:
- Modelo cambiado a qwen2.5:7b (GPU completa, 6x más rápido)
- Prompts específicos por sección (cada sección pide exactamente lo que necesita)
- Búsquedas Tavily específicas por sección (contexto más preciso)
- Secciones dinámicas por complejidad del tema (5, 7, 9 o 12 secciones)
- Categorización corregida (tecnologías específicas antes que java 21)
"""

import os
import re
import json
import time
import requests
import hashlib
import atexit
import subprocess
from pathlib import Path
from datetime import datetime

# ================== CONFIG ==================
CONFIG = {
    "MODEL": "qwen2.5:7b",
    "OLLAMA_URL": "http://localhost:11434/api/generate",
    "CACHE_SEC_TTL": 7200,
    "MIN_WORDS": 300,
    "SCORE_ACCEPTABLE": 70,
    "SCORE_DEPLOY": 72,
    "REPO_ROOT": "/home/usuariojoaquin/.openclaw/workspace/DAM-Java-Mastery",
    "REVIEW_DIR": "_Review",
    "ELITE_DOMAINS": [
        "spring.io", "github.com", "stackoverflow.com", "baeldung.com",
        "oracle.com", "aws.amazon.com", "kubernetes.io", "kafka.apache.org",
        "docs.docker.com", "istio.io", "prometheus.io"
    ],
    "BASE_PROMPT": """
Senior Staff Engineer Java 21 / SRE

REGLAS INNEGOCIABLES:
- SOLO Java 21
- Incluir ```java``` con código real y compilable
- Incluir ```mermaid``` con graph TD o graph LR
- Prohibido setters — usar Records o constructores
- Records no usan extends
- Español técnico, directo, sin introducciones genéricas
- Mínimo 300 palabras por sección
"""
}

# ================== PROMPTS POR SECCIÓN ==================
PROMPTS_SECCION = {
    "Visión Estratégica": """
Escribe la sección VISIÓN ESTRATÉGICA sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Por qué este tema es crítico en 2026 (con datos concretos)
- Comparativa con alternativas (tabla markdown con 3-5 opciones)
- Cuándo usar y cuándo NO usar esta tecnología
- Trade-offs reales que un Staff Engineer debe conocer
- Un diagrama Mermaid que muestre el contexto arquitectónico
- Código Java 21 de ejemplo inicial
""",
    "Arquitectura de Componentes": """
Escribe la sección ARQUITECTURA DE COMPONENTES sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Diagrama Mermaid detallado de la arquitectura (subgraphs si aplica)
- Descripción de cada componente y su responsabilidad
- Patrones de diseño aplicados (con justificación)
- Configuración de producción en código Java 21 (Records, sin setters)
- Decisiones arquitectónicas clave y sus trade-offs
""",
    "Implementación Java 21": """
Escribe la sección IMPLEMENTACIÓN JAVA 21 sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Implementación completa y real (código que compile en Java 21)
- Usar Records para modelos de datos (sin setters)
- Usar Pattern Matching y Switch Expressions donde aplique
- Usar Virtual Threads si hay operaciones I/O
- Usar Sealed Interfaces si hay jerarquía de tipos
- Diagrama Mermaid del flujo de implementación
- Manejo de errores con tipos específicos
""",
    "Métricas y SRE": """
Escribe la sección MÉTRICAS Y SRE sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Métricas clave en formato tabla (nombre, descripción, umbral de alerta)
- Queries Prometheus/PromQL reales para monitorizar
- Diagrama Mermaid del flujo de observabilidad
- Código Java 21 para exponer métricas (Micrometer)
- Checklist SRE para producción (mínimo 5 puntos concretos)
- Errores más comunes en producción y cómo detectarlos
""",
    "Seguridad y Superficie de Ataque": """
Escribe la sección SEGURIDAD Y SUPERFICIE DE ATAQUE sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Principales vectores de ataque específicos de esta tecnología
- Diagrama Mermaid del modelo de amenazas
- Código Java 21 con implementación segura (sin vulnerabilidades)
- Configuración de seguridad recomendada para producción
- Checklist de hardening específico
""",
    "Validación y Estrategia de Pruebas": """
Escribe la sección VALIDACIÓN Y ESTRATEGIA DE PRUEBAS sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Pirámide de tests aplicada a este tema específico
- Código Java 21 con tests reales (JUnit 5, Mockito, Testcontainers)
- Diagrama Mermaid de la estrategia de testing
- Cobertura mínima recomendada y qué medir
- Pruebas de integración y contrato si aplica
""",
    "Rendimiento y Capacidad Crítica": """
Escribe la sección RENDIMIENTO Y CAPACIDAD CRÍTICA sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Benchmarks de referencia con números reales
- Cuellos de botella más comunes y cómo detectarlos
- Código Java 21 optimizado con Virtual Threads si aplica
- Diagrama Mermaid del flujo de optimización
- Configuración JVM recomendada para producción
- Herramientas de profiling recomendadas
""",
    "Patrones de Integración": """
Escribe la sección PATRONES DE INTEGRACIÓN sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Patrones de integración aplicables (con comparativa)
- Diagrama Mermaid de los flujos de integración
- Código Java 21 de implementación del patrón principal
- Manejo de fallos y reintentos
- Configuración de timeouts y circuit breakers
""",
    "Escalabilidad y Alta Disponibilidad": """
Escribe la sección ESCALABILIDAD Y ALTA DISPONIBILIDAD sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Estrategias de escalado horizontal y vertical
- Diagrama Mermaid de la topología de alta disponibilidad
- Configuración de producción multi-instancia en código
- SLOs recomendados (disponibilidad, latencia p99)
- Estrategia de recuperación ante fallos
""",
    "Migración y Compatibilidad": """
Escribe la sección MIGRACIÓN Y COMPATIBILIDAD sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Ruta de migración desde versiones anteriores paso a paso
- Diagrama Mermaid del proceso de migración
- Código Java 21 con compatibilidad hacia atrás si aplica
- Riesgos de la migración y cómo mitigarlos
- Checklist de validación post-migración
""",
    "Casos de Uso Avanzados": """
Escribe la sección CASOS DE USO AVANZADOS sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- 3 casos de uso reales de nivel Staff Engineer
- Diagrama Mermaid del caso de uso más complejo
- Código Java 21 del caso más representativo
- Antipatrones a evitar con explicación técnica
- Referencias a implementaciones open source reales
""",
    "Conclusiones": """
Escribe la sección CONCLUSIONES sobre el tema indicado.
CONTENIDO OBLIGATORIO:
- Resumen de los 3-5 puntos más críticos del documento
- Decisiones de diseño clave y cuándo aplicarlas
- Roadmap de adopción recomendado (fases concretas)
- Código Java 21 de ejemplo final que integre los conceptos
- Diagrama Mermaid del sistema completo
- Recursos oficiales recomendados
"""
}

# ================== BÚSQUEDAS TAVILY POR SECCIÓN ==================
QUERIES_SECCION = {
    "Visión Estratégica": "{tema} strategic overview architecture 2026",
    "Arquitectura de Componentes": "{tema} components architecture design patterns 2026",
    "Implementación Java 21": "{tema} java 21 implementation example virtual threads records",
    "Métricas y SRE": "{tema} prometheus metrics grafana monitoring production 2026",
    "Seguridad y Superficie de Ataque": "{tema} security vulnerabilities hardening best practices 2026",
    "Validación y Estrategia de Pruebas": "{tema} testing strategy junit testcontainers integration tests",
    "Rendimiento y Capacidad Crítica": "{tema} performance benchmark optimization tuning 2026",
    "Patrones de Integración": "{tema} integration patterns event driven microservices 2026",
    "Escalabilidad y Alta Disponibilidad": "{tema} scalability high availability kubernetes production",
    "Migración y Compatibilidad": "{tema} migration guide compatibility upgrade 2026",
    "Casos de Uso Avanzados": "{tema} advanced use cases real world examples staff engineer",
    "Conclusiones": "{tema} best practices production checklist 2026"
}

# ================== LOCK ==================
LOCK_FILE = "/tmp/engine.lock"

def acquire_lock():
    if os.path.exists(LOCK_FILE):
        try:
            with open(LOCK_FILE, "r") as f:
                pid = int(f.read().strip())
            os.kill(pid, 0)
            print("❌ Otro proceso en ejecución")
            exit(1)
        except:
            os.remove(LOCK_FILE)

    with open(LOCK_FILE, "w") as f:
        f.write(str(os.getpid()))

    atexit.register(lambda: os.remove(LOCK_FILE) if os.path.exists(LOCK_FILE) else None)

# ================== LOG ==================
LOG_FILE = Path.home() / "AuthorityEngine/engine.log"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.now().isoformat()} {msg}\n")
    except:
        pass

# ================== LIMPIEZA ==================
def limpiar_texto(texto):
    texto = re.sub(r'[^\x00-\x7F\u00C0-\u017F\s]+', '', texto)
    texto = re.sub(r'(graph\s+[T|L][D|R|B|T]);', r'\1', texto, flags=re.I)
    texto = re.sub(r'```(java|mermaid)', r'\n```\1', texto)
    return texto

# ================== CACHE ==================
CACHE_FILE = Path.home() / "AuthorityEngine/section_cache.json"
CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

sec_cache = {}

def load_cache():
    global sec_cache
    if CACHE_FILE.exists():
        try:
            sec_cache = json.loads(CACHE_FILE.read_text())
        except:
            sec_cache = {}

def save_cache():
    CACHE_FILE.write_text(json.dumps(sec_cache))

def build_key(tema, seccion, prompt):
    return hashlib.md5(f"{tema}|{seccion}|{prompt}".encode()).hexdigest()

def get_cache(key):
    e = sec_cache.get(key)
    if not e:
        return None
    if time.time() - e["ts"] > CONFIG["CACHE_SEC_TTL"]:
        return None
    return e["content"]

def set_cache(key, content):
    sec_cache[key] = {"content": content, "ts": time.time()}
    save_cache()

# ================== WEB FALLBACKS ==================
def _buscar_hn(query: str) -> str:
    """Hacker News Algolia API — fallback si Tavily falla."""
    try:
        url = "http://hn.algolia.com/api/v1/search"
        r = requests.get(url, params={"query": query, "tags": "story", "hitsPerPage": 5}, timeout=10)
        r.raise_for_status()
        hits = r.json().get("hits", [])
        if not hits:
            return ""
        lines = [f"[HN] {h.get('title', '')} — {h.get('url', '')}" for h in hits if h.get("title")]
        return "\n".join(lines)
    except:
        return ""

def _buscar_github(query: str) -> str:
    """GitHub Search API — fallback si HN falla."""
    try:
        url = "https://api.github.com/search/repositories"
        headers = {"Accept": "application/vnd.github+json"}
        r = requests.get(url, params={"q": query, "sort": "stars", "per_page": 5},
                         headers=headers, timeout=10)
        r.raise_for_status()
        items = r.json().get("items", [])
        if not items:
            return ""
        lines = [
            f"[GitHub] {i['full_name']} ★{i['stargazers_count']} — {i.get('description', '')}"
            for i in items
        ]
        return "\n".join(lines)
    except:
        return ""

def _buscar_con_fallback(query: str, label: str) -> str:
    """Tavily → HN → GitHub → vacío."""
    # 1. Tavily
    try:
        from tavily import TavilyClient
        api_key = os.environ.get("TAVILY_KEY")
        if api_key:
            client = TavilyClient(api_key)
            res = client.search(
                query=query,
                search_depth="advanced",
                include_domains=CONFIG["ELITE_DOMAINS"],
                max_results=5
            )
            resultado = "\n".join([r["content"] for r in res["results"]])
            if resultado.strip():
                log(f"🌐 Tavily OK: {label}")
                return resultado
    except Exception as e:
        log(f"⚠️  Tavily falló ({label}): {e}")

    # 2. Hacker News
    resultado = _buscar_hn(query)
    if resultado.strip():
        log(f"🟠 HN fallback OK: {label}")
        return resultado

    # 3. GitHub
    resultado = _buscar_github(query)
    if resultado.strip():
        log(f"🐙 GitHub fallback OK: {label}")
        return resultado

    log(f"⚪ Sin contexto web: {label}")
    return ""

# ================== WEB POR SECCIÓN ==================
def investigar_web_seccion(tema: str, seccion: str) -> str:
    """Búsqueda específica para cada sección — Tavily → HN → GitHub — caché 2h."""
    key = build_key(tema, seccion, "web_sec_v2")
    cached = get_cache(key)
    if cached:
        return cached

    query_template = QUERIES_SECCION.get(seccion, "{tema} best practices 2026")
    query = query_template.format(tema=tema)
    resultado = _buscar_con_fallback(query, f"sec:{seccion}")

    if resultado:
        set_cache(key, resultado)
    return resultado

def investigar_web_general(tema: str) -> str:
    """Búsqueda general para contexto base — Tavily → HN → GitHub — caché 2h."""
    key = build_key(tema, "general", "web_gen_v2")
    cached = get_cache(key)
    if cached:
        return cached

    query = f"{tema} architecture best practices {datetime.now().year}"
    resultado = _buscar_con_fallback(query, "general")

    if resultado:
        set_cache(key, resultado)
    return resultado

# ================== OLLAMA ==================
def call_ollama(prompt):
    try:
        r = requests.post(
            CONFIG["OLLAMA_URL"],
            json={"model": CONFIG["MODEL"], "prompt": prompt, "stream": False},
            timeout=300
        )
        text = r.json().get("response", "")
        return limpiar_texto(text.strip())
    except:
        return "ERROR_IA"

# ================== AUDITOR ==================
def evaluar(texto):
    if not texto or texto == "ERROR_IA":
        return 0, ["error"]

    score = 100
    errores = []

    if len(texto.split()) < CONFIG["MIN_WORDS"]:
        score -= 40
        errores.append("texto_corto")

    if "```java" not in texto.lower():
        score -= 30
        errores.append("falta_bloque_java")

    if "```mermaid" not in texto.lower():
        score -= 30
        errores.append("falta_bloque_mermaid")
    else:
        if not re.search(r'graph\s+(TD|LR)', texto, re.I):
            score -= 30
            errores.append("mermaid_sin_cabecera_graph_TD_o_LR")

    if re.search(r'\bset[A-Z]\w*\(', texto):
        score -= 20
        errores.append("setter_detectado")

    if re.search(r'\brecord\b.*extends', texto, re.I):
        score -= 40
        errores.append("record_no_puede_usar_extends")

    return max(score, 0), errores

# ================== GIT PUSH A _Review ==================
def git_push_review(path, tema, score):
    try:
        os.chdir(CONFIG["REPO_ROOT"])

        result = subprocess.run(
            ["git", "pull", "--rebase"],
            capture_output=True, text=True
        )
        if result.returncode != 0:
            log("⚠️  git pull conflicto — abortando rebase")
            subprocess.run(["git", "rebase", "--abort"], check=False)
            return

        subprocess.run(["git", "add", path], check=True)
        subprocess.run(["git", "commit", "-m",
            f"draft: {tema} (Score:{score}) — pendiente revisión Claude"],
            check=True)
        subprocess.run(["git", "push"], check=True)

        log("✅ Borrador publicado en _Review/ en GitHub")
    except Exception as e:
        log(f"⚠️  Git fallo: {e}")

# ================== CATEGORIZACIÓN ==================
def get_categoria(tema):
    tema_lower = tema.lower()

    if any(kw in tema_lower for kw in ["kafka", "spark", "flink",
        "streaming", "bigdata", "data mesh", "pyspark", "hadoop"]):
        return "07_BigData_Streaming"
    elif any(kw in tema_lower for kw in ["kubernetes", "docker", "terraform",
        "prometheus", "grafana", "sre", "devops", "observabilidad", "k8s",
        "helm", "argocd", "istio"]):
        return "05_SRE_DevOps"
    elif any(kw in tema_lower for kw in ["seguridad", "jwt", "oauth",
        "zero trust", "vault", "sbom", "ciberseguridad", "tls", "mtls",
        "devsecops"]):
        return "06_Seguridad"
    elif any(kw in tema_lower for kw in ["rag", "embeddings", "langchain",
        "ollama", "agente", "llm", "ia generativa", "fine-tuning",
        "vector", "chromadb", "langchain4j"]):
        return "08_IA_Agentes"
    elif any(kw in tema_lower for kw in ["react", "angular", "flutter",
        "android", "frontend", "móvil", "kotlin", "swing", "javafx",
        "typescript", "vue"]):
        return "09_Frontend_Mobile"
    elif any(kw in tema_lower for kw in ["hexagonal", "ddd", "cqrs",
        "event sourcing", "saga", "arquitectura", "microservicio", "monolito",
        "clean architecture"]):
        return "02_Arquitectura"
    elif any(kw in tema_lower for kw in ["spring", "r2dbc", "resilience4j",
        "circuit breaker", "opentelemetry", "webflux", "spring boot",
        "spring security", "spring batch"]):
        return "03_Spring_Ecosystem"
    elif any(kw in tema_lower for kw in ["sql", "postgresql", "mongodb",
        "redis", "bbdd", "base de dato", "índice", "mysql", "cassandra",
        "elasticsearch", "neo4j", "pgvector"]):
        return "04_Bases_de_Datos"
    elif any(kw in tema_lower for kw in ["virtual thread", "records", "loom",
        "sealed", "pattern matching", "java 21", "concurrencia", "executor",
        "jvm", "graalvm", "structured concurrency"]):
        return "01_Java_Core"

    return "10_Vanguardia"

# ================== NOMBRE DE ARCHIVO ==================
def nombre_archivo(tema: str) -> str:
    nombre = tema.lower()
    nombre = re.sub(r'[^\w\s]', '', nombre)
    nombre = re.sub(r'\s+', '_', nombre.strip())
    return nombre[:80] + ".md"

# ================== SECCIONES DINÁMICAS ==================
def obtener_secciones_maestras(tema: str) -> list[str]:
    """
    Número de secciones dinámico según complejidad del tema:
    - 5 secciones: temas simples (un patrón, una feature)
    - 7 secciones: temas de implementación media
    - 9 secciones: temas de arquitectura compleja
    - 12 secciones: guías completas de sistemas
    """
    tema_lower = tema.lower()

    # Base siempre presente
    secciones_base = [
        "Visión Estratégica",
        "Arquitectura de Componentes",
        "Implementación Java 21",
        "Métricas y SRE",
    ]

    # Sección contextual según tema
    if any(kw in tema_lower for kw in ["seguridad", "auth", "jwt",
        "oauth", "encript", "tls", "iam", "zero trust"]):
        secciones_base.append("Seguridad y Superficie de Ataque")
    elif any(kw in tema_lower for kw in ["test", "junit", "mockito",
        "validaci", "qa", "pruebas", "testing"]):
        secciones_base.append("Validación y Estrategia de Pruebas")
    elif any(kw in tema_lower for kw in ["rendimiento", "latencia",
        "throughput", "optimizaci", "tuning", "benchmark"]):
        secciones_base.append("Rendimiento y Capacidad Crítica")

    # 5 secciones: temas simples (un patrón concreto, una feature pequeña)
    temas_simples = ["factory", "singleton", "observer", "strategy",
                     "decorator", "builder", "proxy", "adapter"]
    if any(kw in tema_lower for kw in temas_simples):
        secciones_base.append("Conclusiones")
        return secciones_base  # 5 secciones

    # 7 secciones: temas de implementación media
    temas_medios = ["spring boot", "r2dbc", "webflux", "junit",
                    "mockito", "redis", "postgresql", "mongodb"]
    if any(kw in tema_lower for kw in temas_medios):
        secciones_base.append("Patrones de Integración")
        secciones_base.append("Conclusiones")
        return secciones_base  # 7 secciones

    # 9 secciones: temas de arquitectura compleja
    temas_complejos = ["kafka", "kubernetes", "microservicio", "ddd",
                       "hexagonal", "event sourcing", "cqrs", "saga",
                       "arquitectura", "spring security", "oauth"]
    if any(kw in tema_lower for kw in temas_complejos):
        secciones_base.append("Patrones de Integración")
        secciones_base.append("Escalabilidad y Alta Disponibilidad")
        secciones_base.append("Casos de Uso Avanzados")
        secciones_base.append("Conclusiones")
        return secciones_base  # 9 secciones

    # 12 secciones: guías completas de sistemas
    temas_completos = ["guía completa", "manual completo", "arquitectura completa",
                       "sistema completo", "plataforma", "ecosistema"]
    if any(kw in tema_lower for kw in temas_completos):
        secciones_base.append("Patrones de Integración")
        secciones_base.append("Escalabilidad y Alta Disponibilidad")
        secciones_base.append("Rendimiento y Capacidad Crítica")
        secciones_base.append("Migración y Compatibilidad")
        secciones_base.append("Casos de Uso Avanzados")
        secciones_base.append("Seguridad y Superficie de Ataque")
        secciones_base.append("Conclusiones")
        return secciones_base  # 12 secciones

    # Default: 7 secciones
    secciones_base.append("Patrones de Integración")
    secciones_base.append("Conclusiones")
    return secciones_base

# ================== CONTEXTO RESUMIDO ==================
def extraer_contexto_clave(results_dict: dict) -> str:
    contexto = ""
    for sec, contenido in list(results_dict.items())[-2:]:
        resumen = "\n".join(contenido.split("\n")[:5])
        contexto += f"\n--- RESUMEN {sec} ---\n{resumen}...\n"
    return contexto

# ================== GENERACIÓN ==================
def generar_seccion(tema, sec, contexto_general, results_previos):
    contexto_prev  = extraer_contexto_clave(results_previos)
    contexto_seccion = investigar_web_seccion(tema, sec)
    prompt_seccion = PROMPTS_SECCION.get(sec, "Escribe esta sección con código Java 21 y diagrama Mermaid.")

    prompt = f"""{CONFIG["BASE_PROMPT"]}

{prompt_seccion}

CONTEXTO WEB GENERAL:
{contexto_general}

CONTEXTO WEB ESPECÍFICO PARA ESTA SECCIÓN:
{contexto_seccion}

CONTEXTO DE SECCIONES ANTERIORES:
{contexto_prev}

TEMA: {tema}
SECCIÓN A ESCRIBIR: {sec}
"""

    key = build_key(tema, sec, prompt)
    cached = get_cache(key)

    if cached:
        score, _ = evaluar(cached)
        if score >= CONFIG["SCORE_ACCEPTABLE"]:
            log(f"📦 Cache hit: {sec}")
            return cached, score

    log(f"🤖 Generando → {sec}")
    contenido = call_ollama(prompt)
    score, errores = evaluar(contenido)

    if score < CONFIG["SCORE_ACCEPTABLE"]:
        errores_str = ", ".join(errores)
        log(f"🔁 Reintento {sec} — errores: {errores_str}")
        prompt += f"\nCORRECCIÓN URGENTE: Fallos detectados: {errores_str}. Corrige todos estos fallos."
        contenido = call_ollama(prompt)
        score, errores = evaluar(contenido)

    if score >= CONFIG["SCORE_ACCEPTABLE"]:
        set_cache(key, contenido)

    return contenido, score

# ================== MAIN ==================
def generate_report(tema):
    acquire_lock()
    load_cache()

    log(f"🚀 {tema}")

    contexto_general = investigar_web_general(tema)
    secciones = obtener_secciones_maestras(tema)

    log(f"📋 Secciones: {len(secciones)} → {', '.join(secciones)}")

    results = {}
    scores  = []

    for sec in secciones:
        contenido, score = generar_seccion(tema, sec, contexto_general, results)
        results[sec] = contenido
        if score >= 50:
            scores.append(score)
        log(f"{'✅' if score >= CONFIG['SCORE_ACCEPTABLE'] else '⚠️ '} {sec}: {score}")

    total    = sum(scores) // len(scores) if scores else 0
    categoria = get_categoria(tema)

    review_dir = os.path.join(
        CONFIG["REPO_ROOT"],
        CONFIG["REVIEW_DIR"],
        tema.replace(" ", "_").replace("/", "-")
    )
    os.makedirs(review_dir, exist_ok=True)

    archivo = nombre_archivo(tema)
    path    = os.path.join(review_dir, archivo)

    with open(path, "w") as f:
        f.write(f"# {tema}\n\n")
        f.write(f"PATH_LOCAL: {path}\n")
        f.write(f"CATEGORIA: {categoria}\n")
        f.write(f"Score: {total}\n\n")
        f.write("---\n\n")
        for k, v in results.items():
            f.write(f"## {k}\n\n{v}\n\n")

    log(f"📝 Borrador guardado: {path}")
    log(f"📂 Categoría: {categoria}")
    log(f"📊 Score: {total} | Secciones: {len(secciones)}")

    git_push_review(path, tema, total)

    # Guardar score en historico JSON
    import json as _json
    from datetime import datetime as _dt
    hist_file = Path.home() / "AuthorityEngine/score_historico.json"
    hist = []
    if hist_file.exists():
        try:
            hist = _json.loads(hist_file.read_text())
        except:
            hist = []
    hist.append({
        "tema": tema,
        "score": total,
        "categoria": categoria,
        "secciones": len(secciones),
        "fecha": _dt.now().strftime("%Y-%m-%d %H:%M"),
        "aprobado": total >= CONFIG["SCORE_DEPLOY"]
    })
    hist_file.write_text(_json.dumps(hist, ensure_ascii=False, indent=2))

    log(f"")
    log(f"─────────────────────────────────────────")
    log(f"✅ BORRADOR LISTO — {len(secciones)} secciones")
    log(f"1. Descarga desde GitHub (_Review/)")
    log(f"2. Adjúntalo a Claude en el chat")
    log(f"3. Claude lo refina")
    log(f"4. nano + git push para publicar")
    log(f"─────────────────────────────────────────")

# ================== RUN ==================
if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 2:
        generate_report(sys.argv[1])
    else:
        print("uso: python engine.py 'tema'")
