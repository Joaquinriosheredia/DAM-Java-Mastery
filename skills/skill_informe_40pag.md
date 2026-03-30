# DIRECTIVA DE EXTENSIÓN: INFORME STAFF v10.1
**Mínimo 20 secciones detalladas. PROHIBIDO resumir o usar lenguaje genérico.**

---

## 🎯 OBJETIVO DE ESTE SKILL

Generar informes técnicos de nivel Staff Engineer (20-40 páginas) que demuestren:
- Autoridad técnica verificable
- Código de producción ejecutable
- Validación SRE con Security Score
- Trazabilidad completa de decisiones

---

## 📋 ESTRUCTURA OBLIGATORIA (Mínimo 2 páginas por sección)

### 1. Portada Profesional y Control de Versiones
- Título del informe
- Autor: Joaquín Ríos Heredia — Staff Engineer
- Fecha de publicación
- Versión del documento (v1.0, v1.1, etc.)
- Estado: Borrador / Revisado / Publicado
- Enlace a repositorio GitHub

### 2. Resumen Ejecutivo (ROI y Valor Estratégico)
- Problema de negocio abordado
- Solución técnica propuesta
- ROI estimado (tiempo/coste ahorrado)
- Recomendaciones clave para CTOs/CEOs
- Métricas de éxito esperadas

### 3. Estado del Arte 2026: Tendencias en Big Data e IA
- Investigación web actualizada (fuentes 2025-2026)
- Comparativa con soluciones de años anteriores
- Tendencias emergentes (Project Loom, GraalVM, RAG, etc.)
- Citas de fuentes verificadas (documentación oficial, papers)

### 4. Arquitectura de Sistemas: Diagramas Mermaid (SOLID/DDD)
- Diagrama de contexto (C4 Model - Nivel 1)
- Diagrama de contenedores (C4 Model - Nivel 2)
- Diagrama de componentes (C4 Model - Nivel 3)
- Justificación de decisiones arquitectónicas
- Alternativas consideradas y por qué se descartaron

### 5. Implementación Técnica: Código Java 21 / PySpark (Sin placeholders)
- Scripts completos y ejecutables
- Sin comentarios tipo "// TODO: implementar"
- Manejo de errores incluido
- Logs estructurados
- Configuración de entorno (requirements.txt, pom.xml, etc.)

### 6. Auditoría SRE: Security Score y Análisis de Vulnerabilidades
- Security Score obtenido (mínimo 70/100)
- Vulnerabilidades detectadas y corregidas
- Herramientas de escaneo utilizadas (Snyk, OWASP ZAP, etc.)
- Compliance aplicado (GDPR, HIPAA, AI Act 2026)
- Log de auditoría completo (auditoria_sre_log.json)

### 7. Guía de Despliegue Paso a Paso (Instalación y Configuración)
- Requisitos previos (hardware, software, versiones)
- Instalación de dependencias
- Configuración de variables de entorno
- Primer despliegue de prueba
- Validación de instalación exitosa

### 8. Benchmarks de Rendimiento y Casos de Uso Reales
- Métricas de rendimiento (throughput, latencia, uso de recursos)
- Comparativa con alternativas (antes/después)
- 3-5 casos de uso anonimizados de producción
- Lecciones aprendidas de cada caso
- Gráficos de rendimiento (pueden ser ASCII o Mermaid)

### 9. Testing y Validación de Calidad
- Tests unitarios (cobertura mínima 80%)
- Tests de integración
- Tests de carga (JMeter, Gatling)
- Criterios de aceptación
- Evidencia de tests passing

### 10. Monitorización y Observabilidad en Producción
- Métricas clave a monitorizar (KPIs técnicos)
- Alertas configuradas (Prometheus, Grafana)
- Dashboards recomendados
- Runbook para incidentes comunes
- SLA/SLO definidos

### 11. Escalabilidad y Estrategias de Crecimiento
- Escalado horizontal vs. vertical
- Estrategias de caching (Redis, Memcached)
- Balanceo de carga
- Consideraciones de coste cloud (FinOps)
- Límites conocidos del sistema

### 12. Seguridad y Gestión de Secretos
- HashiCorp Vault o alternativas
- Rotación de credenciales
- Encriptación en reposo y tránsito
- Access control (RBAC, IAM)
- Audit logging de accesos

### 13. Integración Continua y Despliegue Continuo (CI/CD)
- Pipeline de GitHub Actions / GitLab CI
- Validaciones automáticas pre-merge
- Estrategias de deployment (blue-green, canary)
- Rollback automático en caso de fallo
- Tiempo estimado de deployment

### 14. Gestión de Datos y Estrategia de Backup
- Política de backups (frecuencia, retención)
- Recovery Point Objective (RPO)
- Recovery Time Objective (RTO)
- Pruebas de restauración
- Consideraciones GDPR (derecho al olvido)

### 15. Documentación de API (si aplica)
- OpenAPI/Swagger specification
- Ejemplos de requests/responses
- Autenticación requerida
- Rate limiting
- Versionado de API

### 16. Análisis de Costes y FinOps
- Estimación de costes cloud mensuales
- Optimizaciones aplicadas
- Comparativa de proveedores (AWS vs. Azure vs. GCP)
- Recomendaciones de ahorro
- ROI del proyecto

### 17. Riesgos Técnicos y Mitigación
- Riesgos identificados (probabilidad × impacto)
- Plan de mitigación para cada riesgo
- Single points of failure (SPOF)
- Disaster recovery plan
- Contactos de escalado

### 18. Mantenimiento y Evolución del Sistema
- Frecuencia de actualizaciones
- Política de deprecated features
- Roadmap de mejoras futuras
- Technical debt identificado
- Criterios para refactorización

### 19. Conclusiones Técnicas y Roadmap Evolutivo
- Hallazgos principales del informe
- Recomendaciones finales
- Próximos pasos (corto/medio/largo plazo)
- Inversión estimada para evolución
- Métricas de éxito a revisar

### 20. Glosario y Referencias Técnicas
- Definición de acrónimos y términos técnicos
- Bibliografía completa (50+ referencias)
- Enlaces a documentación oficial
- Repositorios GitHub relacionados
- Recursos adicionales para profundizar

---

## 🛑 REGLAS DE CALIDAD OBLIGATORIAS

| Regla | Requisito | Validación |
|-------|-----------|------------|
| **Longitud mínima** | 20 páginas (40+ con anexos) | Contar líneas/secciones |
| **Código ejecutable** | 0 placeholders | Verificar "// TODO" ausentes |
| **Security Score** | ≥70/100 | Auditoría SRE obligatoria |
| **Fuentes verificadas** | Mínimo 50 referencias | Enlaces activos 2025-2026 |
| **Diagramas** | Mínimo 5 diagramas | Mermaid o ASCII |
| **Casos de uso** | Mínimo 3 casos reales | Anonimizados si es necesario |
| **Tests** | Cobertura 80%+ | Informe de JaCoCo o similar |
| **Tono** | Profesional, técnico, accesible | Sin jerga innecesaria |

---

## ⚠️ PROHIBIDO BAJO ESTE SKILL

- ❌ Resumir secciones para ahorrar espacio
- ❌ Usar lenguaje genérico ("depende del caso")
- ❌ Placeholders en código ("// implementar aquí")
- ❌ Fuentes anteriores a 2024 (obsoletas)
- ❌ Security Score <70/100
- ❌ Diagramas sin explicación
- ❌ Claims sin evidencia o métricas

---

## ✅ TONO Y ESTILO REQUERIDO

| Aspecto | Requisito |
|---------|-----------|
| **Nivel técnico** | Staff Engineer (asume conocimiento previo) |
| **Accesibilidad** | Explicar conceptos complejos con ejemplos |
| **Métricas** | Todo claim debe tener número asociado |
| **Evidencia** | Enlaces a GitHub, logs, screenshots |
| **Honestidad** | Admitir limitaciones y trade-offs |
| **Acción** | Cada sección debe tener takeaway práctico |

---

## 📊 CHECKLIST DE VALIDACIÓN PRE-ENTREGA

Antes de marcar este informe como completado, verifica:
