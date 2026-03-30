import json
from pathlib import Path
from tavily import TavilyClient

class RadarAgent:
    def __init__(self):
        self.config = self._load_config()
        self.api_key = self.config['api']['tavily_key']
        self.client = TavilyClient(api_key=self.api_key)

    def _load_config(self):
        config_path = Path.home() / "AuthorityEngine/config/settings.json"
        with open(config_path, 'r') as f:
            return json.load(f)

    def search(self, query):
        print(f" 🔍 [RADAR] Investigando tendencias técnicas 2026: {query}")
        try:
            # Búsqueda avanzada orientada a documentación de arquitectura
            res = self.client.search(
                query=f"{query} technical architecture guide 2026", 
                search_depth="advanced",
                max_results=5
            )
            context = "\n".join([r['content'] for r in res['results']])
            return context
        except Exception as e:
            print(f" ❌ [RADAR ERROR] Fallo en la búsqueda: {e}")
            return "No se pudo obtener contexto externo."

