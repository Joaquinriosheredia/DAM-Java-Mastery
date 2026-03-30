import sys
import requests

# CONFIGURACIÓN (Igual que tu openclaw)
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "qwen2.5:14b"

def reparar_seccion(archivo_path, nombre_seccion, tema):
    print(f"🔧 Reparando sección: {nombre_seccion}...")
    
    prompt = f"""
    Actúa como Staff Engineer. 
    TAREA: Redacta la sección completa de '{nombre_seccion}' para el informe de '{tema}'.
    REQUISITOS: 
    - Mínimo 1000 palabras.
    - Incluye diagramas Mermaid detallados (Arquitectura C4).
    - Usa rigor SOLID y DDD.
    - NO uses placeholders.
    """
    
    payload = {"model": MODELO, "prompt": prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload, timeout=600)
    contenido = response.json().get("response", "")

    # Insertar en el archivo (esto es cirugía manual)
    with open(archivo_path, "r") as f:
        lineas = f.readlines()

    with open(archivo_path, "w") as f:
        for linea in lineas:
            f.write(linea)
            # Buscamos donde empieza la sección 4 para pegar debajo
            if f"## 4. {nombre_seccion}" in linea:
                f.write(f"\n{contenido}\n")
    
    print("✅ Sección reparada con éxito.")

if __name__ == "__main__":
    # Cambia el nombre del archivo por el que se está generando ahora
    ruta = sys.argv[1]
    reparar_seccion(ruta, "Arquitectura de Sistemas: Diagramas Mermaid (SOLID/DDD)", "BigData: ETL con PySpark")
