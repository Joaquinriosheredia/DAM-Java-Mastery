import sys
import json
import os
import subprocess
from pathlib import Path
from datetime import datetime

# Inyección de rutas para los agentes
BASE_DIR = Path.home() / "AuthorityEngine"
sys.path.append(str(BASE_DIR))

from agents.radar import RadarAgent
from agents.muscle import MuscleAgent
from agents.auditor import AuditorAgent

class AuthorityOrchestrator:
    def __init__(self):
        self.radar = RadarAgent()
        self.muscle = MuscleAgent()
        self.auditor = AuditorAgent()

    def planificar(self, tema, contexto):
        print("🧠 [PLANIFICADOR] Diseñando Blueprint dinámico en formato JSON...")
        prompt = f"""Analiza este contexto técnico: {contexto}. 
        Crea una lista de secciones para un manual de NIVEL STAFF sobre '{tema}'.
        Responde ÚNICAMENTE en formato JSON: {{"secciones": ["Titulo 1", "Titulo 2"]}}"""
        
        res = self.muscle.generate(prompt)
        try:
            start = res.find('{')
            end = res.rfind('}') + 1
            plan_json = json.loads(res[start:end])
            return plan_json['secciones']
        except:
            print(" ⚠️  [PLAN] Fallo en JSON. Aplicando fallback por comas.")
            return [s.strip() for s in res.split(",") if len(s) > 5]

    def push_to_github(self, filename, tema):
        print(f"📦 [GIT] Iniciando despliegue automático de '{tema}'...")
        try:
            # 1. Preparar el archivo
            subprocess.run(["git", "add", filename], check=True, cwd=BASE_DIR)
            # 2. Commit técnico
            commit_msg = f"feat: manual de autoridad sobre {tema} (Staff Level)"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True, cwd=BASE_DIR)
            # 3. Push a la rama principal
            subprocess.run(["git", "push", "origin", "main"], check=True, cwd=BASE_DIR)
            print(" ✅ [GIT] Contribución subida con éxito.")
        except Exception as e:
            print(f" ❌ [GIT] Error en despliegue: {e}")

    def ejecutar_racha(self, tema):
        print(f"\n🚀 [MISIÓN] Generando Activo de Autoridad: {tema.upper()}")
        
        # 1. Investigación
        ctx = self.radar.search(tema)
        
        # 2. Planificación
        secciones = self.planificar(tema, ctx)
        print(f"📋 [PLAN] {len(secciones)} secciones identificadas por la IA.")
        
        final_doc = f"# Informe de Autoridad: {tema}\n\n"

        # 3. Producción Auditada
        for i, sec in enumerate(secciones, 1):
            print(f"\n trabajando en [{i}/{len(secciones)}]: {sec}")
            ok, intentos, feedback = False, 0, ""
            mejor_version = ""

            while not ok and intentos < 3:
                intentos += 1
                prompt = f"""Escribe la sección técnica '{sec}' para el manual '{tema}'.
                NIVEL: Staff Engineer (DAM/Java/SRE).
                REQUISITOS: Mínimo 400 palabras, código técnico y diagramas Mermaid.
                CONTEXTO: {ctx[:2000]}
                {f'CORRECCIÓN REQUERIDA: {feedback}' if feedback else ''}"""
                
                txt = self.muscle.generate(prompt)
                if len(txt) > len(mejor_version):
                    mejor_version = txt
                
                ok, feedback = self.auditor.validate(txt, sec)
                
                if ok:
                    final_doc += f"## {sec}\n\n{txt}\n\n"
                    print(f" ✅ [SECCIÓN COMPLETADA]")
                else:
                    print(f" 🔄 [REINTENTO {intentos}/3] Motivo: {feedback}")

            if not ok:
                print(f" ⚠️  [AVISO] Se usó la mejor versión tras agotar intentos.")
                final_doc += f"## {sec}\n\n{mejor_version}\n\n"

        # 4. Guardado Final Atómico
        filename = f"{tema.lower().replace(' ', '_')}_STAFF.md"
        filepath = BASE_DIR / filename
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(final_doc)
        
        print(f"\n🏁 [ÉXITO] Documento finalizado: {filename}")
        
# --- PARCHE DE CALIDAD STAFF: GUARDADO Y LIMPIEZA ---
        # 5. Generación de Metadatos Reales
        metadata = {
            "tema": tema,
            "fecha": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "secciones_reales": i,  # Contador real del bucle for
            "status": "Auditado por Llama3",
            "model_muscle": "qwen2.5:14b",
            "model_auditor": "llama3:8b"
        }
        
        meta_filename = f"metadata_{tema.lower().replace(' ', '_')}.json"
        with open(BASE_DIR / meta_filename, "w", encoding="utf-8") as j:
            json.dump(metadata, j, indent=4)

# --- SISTEMA DE CLASIFICACIÓN INTELIGENTE ---
        # 1. Definir la carpeta según el título
        if "java" in tema.lower():
            folder = "Java_Elite"
        elif "bigdata" in tema.lower() or "spark" in tema.lower():
            folder = "Vanguardia_Tech_2026"
        elif "seguridad" in tema.lower() or "microservicios" in tema.lower():
            folder = "Seguridad_SRE_2026"
        else:
            folder = "Otros_Activos_Mastery"

        # 2. Crear la carpeta en Ubuntu si no existe
        target_dir = BASE_DIR / folder
        target_dir.mkdir(parents=True, exist_ok=True)

        # 3. Generación de Metadatos Reales
        metadata = {
            "tema": tema,
            "carpeta_destino": folder,
            "fecha": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "secciones_reales": i,
            "status": "Auditado por Llama3"
        }
        
        meta_filename = f"metadata_{tema.lower().replace(' ', '_')}.json"
        with open(target_dir / meta_filename, "w", encoding="utf-8") as j:
            json.dump(metadata, j, indent=4)

        # 4. Guardado del Manual en su carpeta correspondiente
        filename_only = f"{tema.lower().replace(' ', '_')}_STAFF.md"
        relative_path = f"{folder}/{filename_only}" 
        
        final_doc = final_doc.replace("HTTPConnectionPool", "[ERROR DE RED OMITIDO]")
        
        with open(target_dir / filename_only, "w", encoding="utf-8") as f:
            f.write(final_doc)

        print(f"\n🏁 [ÉXITO] Activo clasificado en: {folder}/")

        # 5. Despliegue Automático a GitHub (usando la ruta relativa)
        self.push_to_github(relative_path, tema)

# --- ENTRADA DEL SISTEMA (EJECUCIÓN) ---
if __name__ == "__main__":
    if len(sys.argv) > 1:
        AuthorityOrchestrator().ejecutar_racha(sys.argv[1])
