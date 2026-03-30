#!/usr/bin/env python3
"""
Configuración centralizada del Authority Engine.
Todos los scripts importan de aquí — cero duplicación.
"""

import os
from pathlib import Path

CONFIG = {
    # IA Local
    "ollama_url": "http://localhost:11434/api/generate",
    "modelo": "qwen2.5:14b",
    
    # Búsqueda Web
    "tavily_key": os.environ.get("TAVILY_KEY"),
    
    # Rutas
    "repo_base": Path.home() / ".openclaw" / "workspace" / "DAM-Java-Mastery",
    "author_engine": Path.home() / "AuthorityEngine",
    "skills": Path.home() / "AuthorityEngine" / "skills" / "skill_informe_40pag.md",
    
    # Umbrales de Calidad
    "security_score_minimo": 75,
    "min_palabras_seccion": 800,
    
    # Timeout (segundos)
    "ollama_timeout": 900,
    "tavily_timeout": 30,
}

# FOLDER_PRIORITIES con scoring
# Formato: "keyword": ("carpeta_destino", prioridad)
# Prioridad 10 = tecnologías específicas (evaluar primero)
# Prioridad 5 = términos genéricos (evaluar después)
# ⚠️ NOTA: NO incluir keywords de 2 letras como "ia" o "ai" (falsos positivos)
# ⚠️ NOTA: "test" eliminado (genera falsos positivos con "testing", "latest", etc.)
FOLDER_PRIORITIES = {
    # Prioridad 10: Tecnologías específicas
    "kafka": ("BigData_Streaming", 10),
    "spark": ("BigData_Streaming", 10),
    "flink": ("BigData_Streaming", 10),
    "spring boot": ("Core_Backend", 10),
    "springboot": ("Core_Backend", 10),
    "kubernetes": ("SRE_Resiliencia", 10),
    "k8s": ("SRE_Resiliencia", 10),
    "ollama": ("IA_Agentes", 10),
    "langchain": ("IA_Agentes", 10),
    "postgresql": ("BasesDatos", 10),
    "mongodb": ("BasesDatos", 10),
    "oauth2": ("Seguridad", 10),
    "jwt": ("Seguridad", 10),
    "zero trust": ("Seguridad", 10),
    "zerotrust": ("Seguridad", 10),
    "data lake": ("BigData_Streaming", 10),
    "datalake": ("BigData_Streaming", 10),
    
    # Prioridad 7: Términos semi-específicos
    "streaming": ("BigData_Streaming", 7),
    "bigdata": ("BigData_Streaming", 7),
    "big data": ("BigData_Streaming", 7),
    "microservicios": ("Core_Backend", 7),
    "microservices": ("Core_Backend", 7),
    "observability": ("SRE_Resiliencia", 7),
    "resilience": ("SRE_Resiliencia", 7),
    "chaos": ("SRE_Resiliencia", 7),
    "docker": ("Cloud_DevOps", 7),
    "terraform": ("Cloud_DevOps", 7),
    "aws": ("Cloud_DevOps", 7),
    "azure": ("Cloud_DevOps", 7),
    "gcp": ("Cloud_DevOps", 7),
    "redis": ("BasesDatos", 7),
    "postgres": ("BasesDatos", 7),
    "rag": ("IA_Agentes", 7),
    "embeddings": ("IA_Agentes", 7),
    "agentes": ("IA_Agentes", 7),
    "pyspark": ("BigData_Streaming", 7),
    "etl": ("BigData_Streaming", 7),
    "plsql": ("BBDD_Acceso", 7),
    "pl/sql": ("BBDD_Acceso", 7),
    
    # Prioridad 5: Términos genéricos + DAM Académico
    "testing": ("Testing", 5),
    # ❌ "test" ELIMINADO (falsos positivos)
    "junit": ("Testing", 5),
    "mockito": ("Testing", 5),
    "selenium": ("Testing", 5),
    "java": ("Core_Backend", 5),
    "backend": ("Core_Backend", 5),
    "spring": ("Core_Backend", 5),
    "cloud": ("Cloud_DevOps", 5),
    "devops": ("Cloud_DevOps", 5),
    "security": ("Seguridad", 5),
    "seguridad": ("Seguridad", 5),
    "oauth": ("Seguridad", 5),
    "sql": ("BasesDatos", 5),
    "database": ("BasesDatos", 5),
    "bbdd": ("BasesDatos", 5),
    "fhir": ("HealthTech", 5),
    "hl7": ("HealthTech", 5),
    "health": ("HealthTech", 5),
    "ddd": ("Arquitectura", 5),
    "cqrs": ("Arquitectura", 5),
    "arquitectura": ("Arquitectura", 5),
    "react": ("Frontend_UX", 5),
    "angular": ("Frontend_UX", 5),
    "vue": ("Frontend_UX", 5),
    "frontend": ("Frontend_UX", 5),
    "android": ("Android_Movil", 5),
    "kotlin": ("Android_Movil", 5),
    "movil": ("Android_Movil", 5),
    # DAM Académico
    "psp": ("PSP", 5),
    "hilos": ("PSP", 5),
    "concurrencia": ("PSP", 5),
    "javafx": ("Interfaces_DI", 5),
    "scene builder": ("Interfaces_DI", 5),
    "hibernate": ("BBDD_Acceso", 5),
    "jdbc": ("BBDD_Acceso", 5),
}
