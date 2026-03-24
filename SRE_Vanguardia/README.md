# eBPF para Observabilidad de Bajo Nivel Con Cilium

## Introducción

Este proyecto busca implementar una solución robusta y eficiente utilizando tecnologías como **eBPF (Extended Berkeley Packet Filter)** en combinación con la herramienta de observabilidad de red y contenedorización **Cilium**. El objetivo es proporcionar un sistema capaz de realizar recopilación de métricas, monitoreo y análisis detallado a nivel de kernel para entornos de redes complejas y sistemas distribuidos.

## Justificación Técnica (2026)

A medida que los sistemas operativos avanzan, la necesidad de herramientas más sofisticadas para observar el comportamiento del sistema en tiempo real se vuelve cada vez más crítica. eBPF es una tecnología relativamente nueva pero altamente prometedora, permitiendo a los desarrolladores y administradores de sistemas implementar funcionalidades complejas como rastreo de tráfico de red, recopilación de métricas y monitoreo sin necesidad de modificar el kernel del sistema. Esto no solo simplifica la gestión y mantenimiento del sistema operativo, sino que también mejora significativamente su rendimiento y seguridad.

### Casos de Uso

1. **Recopilación de Métricas Detalladas:** Implementar funcionalidades para recoger datos detallados sobre el uso de recursos del sistema, incluyendo CPU, memoria, red, etc.
2. **Monitoreo en Tiempo Real:** Proporcionar información actualizada sobre el estado del sistema operativo y las aplicaciones corriendo en tiempo real.
3. **Análisis Complejo:** Permitir la realización de análisis detallados para optimización del rendimiento y diagnóstico de problemas.

## Arquitectura Profunda

La solución se basa principalmente en dos pilares fundamentales:

- **eBPF** proporciona los módulos necesarios para interactuar directamente con el núcleo del sistema.
- **Cilium**, que utiliza eBPF, es responsable de la implementación y gestión práctica de estas funcionalidades.

### Componentes Principales

1. **ebpf-metrics**: Módulo encargado de recoger métricas de bajo nivel como uso de CPU, memoria, red.
2. **cilium-agent**: Herramienta central que coordina las operaciones entre eBPF y el sistema operativo.
3. **collector-service**: Servicio para colectar datos enviados por los módulos eBPF.

## Implementación

El proyecto incluye varios archivos de código fuente escritos en C, junto con scripts de configuración necesarios para su implementación en entornos Linux. A continuación se detallan algunos ejemplos específicos:

### Configuración del Entorno

Antes de proceder a la instalación y ejecución del proyecto, asegúrate de tener instalado eBPF y Cilium correctamente.

```bash
sudo apt-get install linux-headers-$(uname -r)
git clone https://github.com/cilium/cilium.git
cd cilium
make dev-all
```

### Archivos de Código

#### ebpf-metrics.c
[CONTENIDO]