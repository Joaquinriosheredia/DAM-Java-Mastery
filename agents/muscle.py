import json
import requests
import time
from pathlib import Path

class MuscleAgent:
    def __init__(self):
        self.config_path = Path.home() / "AuthorityEngine/config/settings.json"
        with open(self.config_path, 'r') as f:
            config = json.load(f)
        
        self.url = config['llm']['ollama_url']
        self.model = config['llm']['model_main']
        # Sincronización con la nueva estructura del JSON
        self.retries = config['standards']['max_retries']

    def generate(self, prompt):
        payload = {"model": self.model, "prompt": prompt, "stream": False}
        
        for i in range(self.retries):
            try:
                # Timeout de 900s para permitir que el 14B piense secciones densas
                response = requests.post(self.url, json=payload, timeout=900)
                response.raise_for_status()
                return response.json().get("response", "").strip()
            
            except (requests.exceptions.RequestException, Exception) as e:
                print(f" ⚠️  [MUSCLE] Reintento {i+1}/{self.retries} debido a: {e}")
                time.sleep(5)
                
        return "ERROR: No se pudo generar contenido tras agotar reintentos."
