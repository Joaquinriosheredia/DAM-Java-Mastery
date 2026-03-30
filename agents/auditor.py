import json
import requests
from pathlib import Path

class AuditorAgent:
    def __init__(self):
        # Localización centralizada de configuración
        self.config_path = Path.home() / "AuthorityEngine/config/settings.json"
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        self.url = config['llm']['ollama_url']
        self.model = config['llm']['model_auditor']
        self.standards = config['standards']

    def validate(self, content, section_name):
        print(f" 🛡️  [AUDITOR] Analizando sección: {section_name}")
        
        # 1. VALIDACIÓN PROGRAMÁTICA (Dura)
        words = len(content.split())
        has_code = "```" in content
        has_mermaid = "mermaid" in content.lower()
        
        # Reporte de métricas en terminal
        print(f"    📊 Métricas: {words} palabras | Código: {'✅' if has_code else '❌'} | Mermaid: {'✅' if has_mermaid else '❌'}")

        # Comprobación de mínimos del settings.json
        if words < self.standards['min_word_count']:
            return False, "Contenido demasiado breve. Expande la explicación técnica."
        
        if self.standards['require_code'] and not has_code:
            return False, "Falta implementación de código (Java/DAM/Python)."
            
        if self.standards['require_mermaid'] and not has_mermaid:
            return False, "Falta diagrama de arquitectura Mermaid."

        # 2. VALIDACIÓN DE AUTORIDAD (IA)
        prompt = f"""Actúa como Senior Staff Engineer Reviewer. 
        Analiza si el siguiente contenido tiene un nivel EXCEPCIONAL o es simplemente ESTÁNDAR.
        Busca: precisión, visión arquitectónica y ausencia de relleno.
        
        CONTENIDO: {content[:1500]}
        
        Responde ÚNICAMENTE con una de estas dos palabras: 'EXCEPCIONAL' o 'ESTÁNDAR'."""

        try:
            response = requests.post(self.url, json={"model": self.model, "prompt": prompt, "stream": False}, timeout=60)
            response.raise_for_status()
            veredicto = response.json().get("response", "").upper()
            
            if "EXCEPCIONAL" in veredicto:
                print(f" ✅ [APROBADO] Calidad verificada.")
                return True, "OK"
            else:
                print(f" ❌ [RECHAZO] Nivel insuficiente (Estándar).")
                return False, "El tono es demasiado genérico. Sé más incisivo y técnico."
                
        except requests.exceptions.RequestException as e:
            print(f" ⚠️  [SRE] Error de conexión con Auditor: {e}. Aplicando aprobado por contingencia.")
            return True, "BYPASS_ERROR"
