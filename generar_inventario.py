#!/usr/bin/env python3
"""
Genera un informe completo de la estructura de AuthorityEngine
con metadatos y contenido de cada archivo.
"""


import os
import subprocess
from pathlib import Path
from datetime import datetime

BASE_DIR = Path.home() / "AuthorityEngine"
OUTPUT_FILE = BASE_DIR / "INVENTARIO_SISTEMA.md"

# Directorios a excluir
EXCLUDE_DIRS = {"__pycache__", ".git", "node_modules"}

def get_file_size(size_bytes):
    """Convierte bytes a formato legible."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f}TB"

def get_file_content(filepath, max_lines=100):
    """Lee el contenido del archivo (limitado para no saturar)."""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            total_lines = len(lines)
            content = ''.join(lines[:max_lines])
            if total_lines > max_lines:
                content += f"\n\n... ({total_lines - max_lines} líneas más)"
            return content, total_lines
    except Exception as e:
        return f"Error leyendo archivo: {e}", 0

def generate_report():
    """Genera el informe completo."""
    report = []
    
    # Header
    report.append("# 📊 INVENTARIO DEL SISTEMA — AuthorityEngine")
    report.append("")
    report.append(f"**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**Directorio Base:** `{BASE_DIR}`")
    report.append("")
    report.append("---")
    report.append("")
    
    # Estructura de directorios
    report.append("## 📁 Estructura de Directorios")
    report.append("")
    report.append("```")
    
    for root, dirs, files in os.walk(BASE_DIR):
        # Excluir directorios
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        level = root.replace(str(BASE_DIR), '').count(os.sep)
        indent = '│   ' * level
        report.append(f"{indent}📂 {os.path.basename(root)}/")
        
        sub_indent = '│   ' * (level + 1)
        for file in sorted(files):
            filepath = Path(root) / file
            size = get_file_size(filepath.stat().st_size)
            report.append(f"{sub_indent}📄 {file} ({size})")
    
    report.append("```")
    report.append("")
    report.append("---")
    report.append("")
    
    # Contenido de archivos Python
    report.append("## 📄 Contenido de Archivos Python")
    report.append("")
    
    py_files = sorted(BASE_DIR.glob("*.py"))
    
    for py_file in py_files:
        content, total_lines = get_file_content(py_file)
        size = get_file_size(py_file.stat().st_size)
        mtime = datetime.fromtimestamp(py_file.stat().st_mtime).strftime('%Y-%m-%d %H:%M')
        
        report.append(f"### `{py_file.name}` ({size}, {total_lines} líneas, modificado: {mtime})")
        report.append("")
        report.append("```python")
        report.append(content)
        report.append("```")
        report.append("")
        report.append("---")
        report.append("")
    
    # Contenido de archivos de texto (skills, logs, etc.)
    report.append("## 📝 Otros Archivos de Interés")
    report.append("")
    
    # Skills directory
    skills_dir = BASE_DIR / "skills"
    if skills_dir.exists():
        report.append("### Directorio `skills/`")
        report.append("")
        for skill_file in sorted(skills_dir.glob("*")):
            if skill_file.is_file():
                content, total_lines = get_file_content(skill_file)
                size = get_file_size(skill_file.stat().st_size)
                report.append(f"#### `{skill_file.name}` ({size})")
                report.append("")
                report.append("```")
                report.append(content)
                report.append("```")
                report.append("")
        report.append("---")
        report.append("")
    
    # Log file
    log_file = BASE_DIR / "racha.log"
    if log_file.exists():
        content, total_lines = get_file_content(log_file, max_lines=50)
        report.append(f"### `racha.log` (últimas {min(50, total_lines)} líneas)")
        report.append("")
        report.append("```")
        report.append(content)
        report.append("```")
        report.append("")
        report.append("---")
        report.append("")
    
    # Resumen
    report.append("## 📊 Resumen")
    report.append("")
    
    total_files = len(list(BASE_DIR.rglob("*")))
    total_py = len(list(BASE_DIR.glob("*.py")))
    total_size = sum(f.stat().st_size for f in BASE_DIR.rglob("*") if f.is_file())
    
    report.append("| Métrica | Valor |")
    report.append("|---------|-------|")
    report.append(f"| Total de archivos | {total_files} |")
    report.append(f"| Archivos Python | {total_py} |")
    report.append(f"| Tamaño total | {get_file_size(total_size)} |")
    report.append(f"| Fecha de generación | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} |")
    report.append("")
    
    # Guardar informe
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))
    
    print(f"✅ Informe generado: {OUTPUT_FILE}")
    print(f"📊 Tamaño del informe: {get_file_size(OUTPUT_FILE.stat().st_size)}")
    print(f"📁 Total de archivos escaneados: {total_files}")
    print(f"📄 Archivos Python documentados: {total_py}")

def subir_inventario_github():
    import shutil
    import subprocess
    from pathlib import Path
    from datetime import datetime

    print("\n🔄 Iniciando sincronización con GitHub...")
    try:
        # 1. Definimos las rutas exactas hacia la carpeta Utils
        repo_base = Path.home() / ".openclaw" / "workspace" / "DAM-Java-Mastery"
        carpeta_utils = repo_base / "Utils"
        
        # Nos aseguramos de que la carpeta existe
        carpeta_utils.mkdir(exist_ok=True)
        
        archivo_origen = Path.home() / "AuthorityEngine" / "INVENTARIO_SISTEMA.md"
        archivo_destino = carpeta_utils / "INVENTARIO_SISTEMA.md"
        
        # 2. Copiamos el archivo desde tu entorno local a la subcarpeta Utils
        shutil.copy(archivo_origen, archivo_destino)
        
        # 3. Ejecutamos Git apuntando específicamente a ese archivo dentro de Utils
        subprocess.run(["git", "add", "Utils/INVENTARIO_SISTEMA.md"], check=True, cwd=repo_base)
        
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        mensaje_commit = f"chore: Actualizacion de inventario en Utils [{fecha_actual}]"
        
        subprocess.run(["git", "commit", "-m", mensaje_commit], check=True, cwd=repo_base)
        subprocess.run(["git", "push"], check=True, cwd=repo_base)
        
        print("🚀 [SUCCESS] Inventario subido a DAM-Java-Mastery/Utils en GitHub correctamente.")
        
    except subprocess.CalledProcessError:
        print("⚠️ [INFO] No hay cambios nuevos en el inventario para subir.")
    except Exception as e:
        print(f"❌ [ERROR] Fallo en el volcado a Git: {e}")
if __name__ == "__main__":
    generate_report()
    subir_inventario_github()
