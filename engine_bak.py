import os
import sys
import requests
import subprocess
import re
from datetime import datetime
from tavily import TavilyClient

# --- CONFIGURACIÓN DE ÉLITE v11.8.2 ---
CONFIG = {
    "ollama_url": "http://localhost:11434/api/generate",
    "modelo": "qwen2.5:14b",
    "tavily_key": os.environ.get("TAVILY_KEY"),
    "skill_archivo": os.path.expanduser("~/AuthorityEngine/skills/skill_informe_40pag.md"),
    "repo_root": "/home/usuariojoaquin/.openclaw/workspace/DAM-Java-Mastery",
    "min_palabras_seccion": 800,
    "security_score_minimo": 75
}

tavily = TavilyClient(api_key=CONFIG["tavily_key"])

def log(mensaje, tipo="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = {"INFO": "[INFO]", "SUCCESS": "[OK]", "WARNING": "[WARN]", "ERROR": "[ERR]"}
    print(f"{prefix.get(tipo, '[...]')} {timestamp} - {mensaje}")

def calcular_sre_score(contenido):
    score = 100
    alertas = []
    if "TODO" in contenido or "implementar" in contenido.lower():
        score -= 20
        alertas.append("Detección de marcadores de posición (placeholders).")
    if "```java" not in contenido and "```python" not in contenido:
        score -= 20
        alertas.append("Ausencia de bloques de código fuente real.")
    if "```mermaid" not in contenido:
        score -= 15
        alertas.append("Ausencia de diagramas arquitectónicos Mermaid.")
    palabras = len(contenido.split())
    if palabras < 4000:
        score -= 15
        alertas.append(f"Densidad de contenido insuficiente para biblioteca ({palabras} palabras).")
    if "Benchmark" not in contenido and "Latencia" not in contenido:
        score -= 10
        alertas.append("Falta de métricas de rendimiento o comparativas.")
    for alerta in alertas:
        log(alerta, "WARNING")
    log(f"SRE Score Final: {score}/100", "SUCCESS" if score >= 75 else "ERROR")
    return score

def investigar_web(tema):
    log(f"Investigando estado del arte para: {tema}", "INFO")
    try:
        query = f"{tema} high level architecture 2026 benchmarks production implementation"
        search = tavily.search(query=query, search_depth="advanced")
        return "\n".join([res['content'] for res in search['results']])
    except Exception as e:
        log(f"Error en servicio Tavily: {e}", "WARNING")
        return "Contexto técnico general 2026 (Fallback)."

def llamar_ollama(prompt):
    payload = {
        "model": CONFIG["modelo"],
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 4096,
            "top_p": 0.1
        }
    }
    try:
        r = requests.post(CONFIG["ollama_url"], json=payload, timeout=900)
        return r.json().get("response", "")
    except Exception as e:
        log(f"Error en motor IA: {e}", "ERROR")
        return ""

def seleccionar_secciones_inteligentes(tema, num_secciones, todas_las_secciones):
    """
    La IA analiza el tema y selecciona/reordena las secciones más relevantes.
    Evita documentos genéricos y repetitivos.
    """
    prompt = f"""
    Analiza este tema técnico y selecciona las {num_secciones} secciones más relevantes 
    de esta lista maestra, ordenadas por prioridad para ESTE tema específico:
    
    Tema: '{tema}'
    
    Lista Maestra de Secciones:
    {chr(10).join(f"  {i+1}. {s}" for i, s in enumerate(todas_las_secciones))}
    
    Responde SOLO con los números de las secciones seleccionadas, separados por coma, 
    en orden de prioridad (ej: 5,2,11,6,1,9,3,12,7,14).
    No incluyas texto adicional, solo los números.
    """
    
    try:
        respuesta = llamar_ollama(prompt)
        # Extraer números de la respuesta
        numeros = [int(x.strip()) for x in respuesta.split(',') if x.strip().isdigit()]
        
        # Validar y seleccionar secciones
        secciones_seleccionadas = []
        for num in numeros:
            if 1 <= num <= len(todas_las_secciones):
                secciones_seleccionadas.append(todas_las_secciones[num - 1])
        
        # Si la IA no devolvió suficientes, rellenar con las restantes
        if len(secciones_seleccionadas) < num_secciones:
            for sec in todas_las_secciones:
                if sec not in secciones_seleccionadas:
                    secciones_seleccionadas.append(sec)
                    if len(secciones_seleccionadas) >= num_secciones:
                        break
        
        return secciones_seleccionadas[:num_secciones]
    
    except Exception as e:
        log(f"Error en selección inteligente: {e}. Usando orden default.", "WARNING")
        return todas_las_secciones[:num_secciones]


def generar_informe(tema, ruta_destino, modo, secciones_personalizadas=None):
    log(f"Iniciando Factory de Autoridad: {tema}", "INFO")
    os.makedirs(ruta_destino, exist_ok=True)

    if not os.path.exists(CONFIG["skill_archivo"]):
        log("Skill no encontrado. Verifique la ruta del archivo .md", "ERROR")
        return

    with open(CONFIG["skill_archivo"], "r", encoding="utf-8") as f:
        skill = f.read()

    contexto_web = investigar_web(tema)

    # --- INICIO DEL BLOQUE SÁNDWICH ---
    # 1. EL PAN DE ARRIBA (Obligatorio siempre)
    secciones_inicio = [
        "Visión Estratégica y ROI 2026",
        "Análisis del Estado del Arte y Tendencias de Mercado",
        "Arquitectura de Componentes y Patrones (Mermaid)"
    ]

    # 2. EL PAN DE ABAJO (Obligatorio siempre)
    secciones_fin = [
        "Roadmap de Evolución y Conclusiones Senior"
    ]

    # 3. EL RELLENO DINÁMICO (Filtrado Inteligente por Categoría)
    # Extraemos el nombre de la carpeta destino (ej: "Core_Backend", "Cloud_DevOps")
    carpeta_destino = os.path.basename(os.path.normpath(ruta_destino))

    # Diccionario de menús hiper-especializados
    menu_por_categoria = {
        "Core_Backend": [
            "Implementación Core de Alto Rendimiento (Java 21/Python)",
            "Patrones de Diseño Avanzados y Clean Code",
            "Gestión de Concurrencia y Programación Reactiva",
            "Optimización de rendimiento y profiling (CPU, memoria, GC)",
            "Gestión avanzada de memoria y tuning de JVM",
            "Gestión de deuda técnica y refactoring estratégico"
        ],
        "Cloud_DevOps": [
            "Escalabilidad Horizontal y Sharding de Datos",
            "Estrategias de Caching Distribuido (Redis/Memcached)",
            "Despliegue en Kubernetes y Orquestación de Contenedores",
            "Arquitecturas Serverless y Edge Computing",
            "Estrategias de CI/CD y Automatización de Pipelines"
        ],
        "Seguridad": [
            "Seguridad Avanzada, Blindaje y Gestión de Secretos",
            "Threat Modeling y Análisis de Vulnerabilidades",
            "Arquitecturas Zero Trust y Gestión de Identidades (IAM)",
            "Criptografía aplicada (TLS, hashing, encryption at rest)",
            "Seguridad en APIs (rate limiting, WAF, API gateways)"
        ],
        "BigData_Streaming": [
            "Procesamiento de Eventos y Streaming (Apache Kafka)",
            "Governanza de Datos, Data Mesh y Calidad",
            "Optimización de queries y tuning SQL",
            "Transacciones distribuidas y consistencia (CAP theorem)",
            "Patrones de persistencia (Outbox, Saga)"
        ],
        "IA_Agentes": [
            "Integración de Modelos IA y Arquitecturas RAG (Ollama/LangChain)",
            "Ingeniería de Prompts y Control de Alucinaciones",
            "Fine-tuning de Modelos Locales y Evaluación de Calidad",
            "Cost-Benefit Analysis y FinOps en Inferencia IA"
        ],
        "Arquitectura": [
            "Domain-Driven Design (DDD) y Modelado de Dominio",
            "Arquitecturas CQRS y Event Sourcing",
            "Arquitectura Hexagonal y Clean Architecture en profundidad",
            "Gestión de contratos y API Design (OpenAPI, GraphQL)",
            "Trade-offs arquitectónicos y toma de decisiones",
            "Impacto en negocio y alineación con producto"
        ],
        "SRE_Resiliencia": [
            "Estrategias de Testing, QA y Calidad SRE",
            "Monitoreo, Observabilidad (OpenTelemetry) y FinOps",
            "Resiliencia y Chaos Engineering en Producción",
            "Tracing distribuido y debugging en sistemas complejos",
            "Alerting inteligente basado en SLO/SLI",
            "Benchmarking y pruebas de carga (JMeter, k6)"
        ]
    }

    # Fallback: Menú genérico Staff Engineer si la carpeta no coincide con las de arriba
    menu_generico = [
        "Implementación Core de Alto Rendimiento",
        "Estrategia de Migración y Modernización de Legacy Systems",
        "Compliance y Regulaciones (GDPR, AI Act, HIPAA)",
        "Cost-Benefit Analysis y TCO",
        "Developer Experience (DX) y productividad de equipos",
        "Networking avanzado (TCP/IP, HTTP/2, gRPC)",
        "Balanceo de carga y estrategias de routing",
        "Gestión de latencia en sistemas distribuidos"
    ]

    # Asignar la lista de ingredientes basada en la carpeta
    secciones_tecnicas_disponibles = menu_por_categoria.get(carpeta_destino, menu_generico)

# Determinar total de secciones
    if modo == "deep":
        num_total_secciones = int(secciones_personalizadas) if secciones_personalizadas else 10
    elif modo == "manual":
        num_total_secciones = 6
    else:
        # ESTÁNDAR JOAQUÍN: 4 fijas + 3 módulos técnicos elegidos por IA
        num_total_secciones = 7

    # Calcular cuántas secciones técnicas necesitamos que elija la IA
    secciones_a_elegir = num_total_secciones - len(secciones_inicio) - len(secciones_fin)

    # Selección inteligente SOLO para el relleno
    if modo == "deep" and secciones_a_elegir > 0:
        secciones_elegidas = seleccionar_secciones_inteligentes(tema, secciones_a_elegir, secciones_tecnicas_disponibles)
    else:
        # Si pide pocas secciones, coge las primeras por defecto
        secciones_elegidas = secciones_tecnicas_disponibles[:max(0, secciones_a_elegir)]

    # ENSAMBLAR EL SÁNDWICH FINAL
    secciones = secciones_inicio + secciones_elegidas + secciones_fin
    # --- FIN DEL BLOQUE SÁNDWICH ---

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_fichero = f"{modo}_{tema.lower().replace(' ', '_')}_{timestamp}.md"
    ruta_fichero = os.path.join(ruta_destino, nombre_fichero)

    with open(ruta_fichero, "w", encoding="utf-8") as f:
        f.write(f"# {tema.upper()}\n\n")
        f.write(f"**Documentación Técnica de Referencia | Autor: Joaquín Ríos Heredia (Staff Engineer)**\n")
        f.write(f"**Repositorio:** [DAM-Java-Mastery](https://github.com/Joaquinriosheredia/DAM-Java-Mastery)\n\n---\n\n")

        for i, sec in enumerate(secciones, 1):
            log(f"Construyendo Capítulo {i}/{len(secciones)}: {sec}", "INFO")
            prompt = f"""{skill}

CONTEXTO: {contexto_web}

TAREA: Escribe el capítulo técnico '{sec}' para el tema '{tema}'.

REQUISITOS CRÍTICOS DE PLATAFORMA (SRE):
1. PROHIBICIÓN ABSOLUTA DE PLACEHOLDERS: Cero tolerancia a "TODO", "FIXME", "implementar" o "pendiente". Código incompleto es motivo de rechazo.
2. OBSERVABILIDAD Y RENDIMIENTO: Es obligatorio documentar benchmarks esperados (latencia, throughput, consumo de memoria).
3. ESTÁNDAR DE CÓDIGO: Implementación robusta y funcional en Java 21 o Python 3.12.
4. DISEÑO DE SISTEMAS (MERMAID ESTRICTO): 
   - Usa SOLO sintaxis oficial soportada nativamente por GitHub ('graph TD', 'flowchart TD', 'sequenceDiagram'). 
   - PROHIBIDO inventar etiquetas inexistentes como 'c4systemdiagram' o 'c4componentdiagram'. Para diagramas C4, usa 'flowchart TD' con subgraphs.
   - REGLA CRÍTICA DE PARSEO: Todo el texto dentro de los nodos que contenga espacios, paréntesis o símbolos especiales DEBE ir obligatoriamente entre comillas dobles. Ejemplo correcto: NodoA["Texto con (Paréntesis) y / Barras"]. Ejemplo incorrecto: NodoA[Texto con (Paréntesis)].
5. COMUNICACIÓN: Formato Staff Engineer. Directo al dato, sin introducciones genéricas ni frases de relleno.

Si la información contextual es insuficiente para generar código listo para producción, detalla el bloqueador técnico exacto en lugar de falsear la implementación.
"""
            contenido = llamar_ollama(prompt)
            f.write(f"## {i}. {sec}\n\n{contenido}\n\n")
            f.flush()

    with open(ruta_fichero, "r", encoding="utf-8") as f:
        texto_final = f.read()

    score_final = calcular_sre_score(texto_final)

    if score_final >= CONFIG["security_score_minimo"]:
        log("Iniciando sincronización con repositorio remoto...", "INFO")
        try:
            os.chdir(CONFIG["repo_root"])
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", f"docs({modo}): {tema} (SRE Score: {score_final})"], check=True)
            subprocess.run(["git", "push"], check=True)
            log("Activo publicado exitosamente en GitHub.", "SUCCESS")
        except Exception as e:
            log(f"Error en flujo Git: {e}", "ERROR")
    else:
        log(f"Activo rechazado por calidad insuficiente (Score: {score_final}). No se realizará el Push.", "ERROR")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python3 engine.py '[Tema]' '[Ruta]' '[modo]' '[secciones]'")
    else:
        # NUEVO: Leer el 4º parámetro de la terminal si existe
        secciones_param = int(sys.argv[4]) if len(sys.argv) > 4 else None
        generar_informe(sys.argv[1], sys.argv[2], sys.argv[3], secciones_personalizadas=secciones_param)
