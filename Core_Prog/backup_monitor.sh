```bash
#!/bin/bash
# @

# @DESCRIPCIÓN:
# Script en Bash para la monitorización de recursos y el backup automático de logs.
# El script realiza las siguientes acciones:
# - Monitorea el espacio de disco en un directorio específico.
# - Realiza copias de seguridad periódicas de los archivos de log.

# @REQUISITOS:
# - Los permisos necesarios para acceder al directorio y realizar copias de seguridad.
# - Bash 4.2 o superior instalado.

# @PARÁMETROS:
# $1: Ruta del directorio a monitorizar
# $2: Directorio de destino para la copia de seguridad

# @VERSIÓN:
# V1.0, 15/10/2023

# @AUTOR:
# Qwen (Alibaba Cloud)

# Verifica si los argumentos se proporcionaron correctamente.
if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Uso: $0 <directorio_a_monitorizar> <directorio_de_destino>"
    exit 1
fi

MONITORED_DIR="$1"
BACKUP_DIR="$2"

# @Función para verificar el espacio de disco en un directorio.
check_disk_space() {
    # Verifica si el directorio especificado tiene suficiente espacio libre.
    if df -h | grep "$MONITORED_DIR" | awk '{print $5}' | cut -d'%' -f1 | tr -d '%' > /dev/null 2>&1; then
        USED_SPACE=$(df -h | grep "$MONITORED_DIR" | awk '{print $5}' | cut -d'%' -f1)
        if [ $USED_SPACE -gt 90 ]; then
            echo "¡Advertencia! El directorio ${MONITORED_DIR} está ocupando más del 90% de su espacio."
        else
            echo "El directorio ${MONITORED_DIR} tiene suficiente espacio (${USED_SPACE}% utilizado)."
        fi
    else
        echo "No se pudo obtener el uso de disco para el directorio ${MONITORED_DIR}. Verifique los permisos."
    fi
}

# @Función para realizar la copia de seguridad de los archivos de log.
backup_logs() {
    # Copia los archivos de log en un subdirectorio dentro del directorio de destino.
    mkdir -p "$BACKUP_DIR/logs_backup"
    cp -v --remove-destination $MONITORED_DIR/*.log* "$BACKUP_DIR/logs_backup/"
}

# @Función principal
main() {
    check_disk_space
    backup_logs
}

# Llamada a la función principal
main

```

### Explicación de los Componentes:

1. **Variables de Inicialización:**
   - `MONITORED_DIR` y `BACKUP_DIR`: Estas variables contienen las rutas proporcionadas en los argumentos del script.

2. **Comprobación del Espacio de Disco:**
   - La función `check_disk_space()` utiliza el comando `df -h` para obtener la utilidad del espacio de disco.
   - Si el uso es mayor al 90%, se emite un aviso.

3. **Copia de Seguridad de los Logs:**
   - La función `backup_logs()` crea un directorio dentro del destino de la copia de seguridad si no existe, y luego copia todos los archivos que terminen con `.log*` en este directorio.

4. **Función Principal:**
   - La función principal llamada `main()` se encarga de ejecutar las funciones de verificación del espacio de disco y la copia de seguridad de los logs.

5. **Uso:**
   - El script espera dos argumentos al ser invocado: la ruta del directorio a monitorear y la ruta del directorio de destino para la copia de seguridad.

6. **Requisitos:**
   - El script requiere Bash 4.2 o superior, así como los permisos necesarios para leer los archivos y carpetas especificadas.
   
7. **Versión y Autor:**
   - Se incluye una información básica sobre la versión del script y su autor.

Este script puede ser ejecutado en un servidor Linux de forma regular a través de `cron` o cualquier otro mecanismo de scheduling para garantizar que se realicen las copias de seguridad y monitoreo de recursos de manera automatizada.