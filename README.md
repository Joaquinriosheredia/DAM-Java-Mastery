# 🚀 DAM-Java-Mastery | Biblioteca Técnica Staff Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Joaquín_Ríos_Heredia-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/joaquinrios-dev-strategist/)
[![Web](https://img.shields.io/badge/Web-DAM--Java--Mastery-blue?style=flat&logo=github)](https://joaquinriosheredia.github.io/DAM-Java-Mastery/)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-lightgrey?style=flat&logo=github)](https://github.com/Joaquinriosheredia)
![Documentos](https://img.shields.io/badge/Documentos_Staff-22-green?style=flat)
![Calidad](https://img.shields.io/badge/SRE_Score-94%2F100-brightgreen?style=flat)

Biblioteca de referencia técnica de nivel **Staff Engineer** sobre Java 21, arquitecturas de software, SRE, seguridad y sistemas distribuidos. Generada y mantenida con **Authority Engine v21.0** — pipeline híbrido de IA local + revisión académica.

---

## 🏭 Cómo se genera este contenido

Este repositorio no es documentación genérica. Cada documento pasa por un pipeline de tres capas antes de publicarse:

```
Tavily API (fuentes elite 2026)
        ↓
Ollama + Qwen 7b en GPU RTX 4060 (generación local, sin coste por token)
        ↓
Auditor automático (score mínimo 72/100)
        ↓
Revisión académica por Claude Pro (corrección de código, diagramas, nivel Staff)
        ↓
GitHub
```

**Stack técnico:** Python 3.12 · Ollama 0.20.0 · Qwen 2.5 7b · Tavily API · Claude Pro · RTX 4060 8GB

---









## 📚 Índice de Documentos por Módulo

### ☕ 01_Java_Core — Java 21 Avanzado

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Clean Code y Principios SOLID con Java 21](./01_Java_Core/clean_code_y_solid_con_java_21_STAFF.md) | 7 | 03/04/2026 |
| [Garbage Collectors en la JVM: G1, ZGC y Shenandoah en Producción](./01_Java_Core/garbage_collectors_en_la_jvm_g1_zgc_y_shenandoah_en_produccion_STAFF.md) | 6 | 04/04/2026 |
| [Java 21 Virtual Threads: Guía de Referencia Staff Engineer](./01_Java_Core/java_21_virtual_threads_STAFF.md) | 5 | 02/04/2026 |
| [Memory Leaks Reales en Java: Detección y Solución](./01_Java_Core/memory_leaks_reales_en_java_deteccion_y_solucion_con_visualvm_STAFF.md) | 6 | 04/04/2026 |
| [Patrones Strategy y Observer con Java 21: Sealed Interfaces y Pattern Matching](./01_Java_Core/patrones_strategy_y_observer_en_java_21:_implementación_con_sealed_interfaces,_pattern_matching_sobre_records_y_desacoplamiento_funcional_sin_efectos_secundarios_STAFF.md) | 7 | 03/04/2026 |
| [Profiling Avanzado en Java con JFR y Async Profiler](./01_Java_Core/profiling_avanzado_en_java_con_jfr_y_async_profiler_STAFF.md) | 6 | 04/04/2026 |

---

### 🏛️ 02_Arquitectura — DDD, Hexagonal, Microservicios

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Anti-patterns en Microservicios y Cómo Evitarlos con Java 21](./02_Arquitectura/anti-patterns_en_microservicios_y_como_evitarlos_con_java_21_STAFF.md) | 6 | 04/04/2026 |
| [Arquitectura de Microservicios Reactivos con Spring Boot 3.4 y R2DBC](./02_Arquitectura/arquitectura_de_microservicios_reactivos_con_spring_boot_3.3_y_r2dbc_STAFF.md) | 7 | 03/04/2026 |
| [DDD y Arquitectura Hexagonal con Java 21](./02_Arquitectura/ddd_y_arquitectura_hexagonal_con_java_21_STAFF.md) | 9 | 02/04/2026 |
| [Event-Driven Architecture y Transactional Outbox Pattern con Java 21](./02_Arquitectura/event_driven_architecture_transactional_outbox_java_21_STAFF.md) | 7 | 03/04/2026 |
| [Event Sourcing y CQRS con Java 21 y Spring Boot](./02_Arquitectura/event_sourcing_y_cqrs_con_java_21_y_spring_boot_STAFF.md) | 6 | 03/04/2026 |
| [Saga Pattern: Orquestación vs Coreografía con Java 21](./02_Arquitectura/saga_pattern_orquestacion_vs_coreografia_con_java_21_STAFF.md) | 8 | 04/04/2026 |

---

### 🌱 03_Spring_Ecosystem — Spring Boot, R2DBC, WebFlux

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Observabilidad Distribuida en Spring Boot 3.4 con OpenTelemetry y Grafana](./03_Spring_Ecosystem/observabilidad_distribuida_en_spring_boot_3.3_con_opentelemetry_y_grafana_loki:_correlación_de_trazas_y_logs_STAFF.md) | 7 | 03/04/2026 |
| [Spring Boot 3.4 y R2DBC con Virtual Threads](./03_Spring_Ecosystem/spring_boot_34_r2dbc_virtual_threads_STAFF.md) | 5 | 03/04/2026 |

---

### 🗄️ 04_Bases_de_Datos — PostgreSQL, Redis, MongoDB

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Optimización de Rendimiento en JVM y Caché Distribuida con Redis y Java 21](./04_Bases_de_Datos/optimizacion_jvm_y_cache_distribuida_redis_java_21_STAFF.md) | 7 | 03/04/2026 |

---

### ⚙️ 05_SRE_DevOps — Kubernetes, Terraform, Observabilidad

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Kubernetes: Auto-escalado y Service Mesh en 2026](./05_SRE_DevOps/kubernetes_auto-escalado_service_mesh_2026_STAFF.md) | 5 | 03/04/2026 |

---

### 🔐 06_Seguridad — JWT, OAuth2, Zero Trust

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [JWT, OAuth2 y Zero Trust Security con Java 21 y Spring Security](./06_Seguridad/jwt_oauth2_y_zero_trust_security_con_java_21_STAFF.md) | 9 | 02/04/2026 |
| [Seguridad Ofensiva y Auditoría de Microservicios con Java 21](./06_Seguridad/seguridad_ofensiva_y_auditoria_de_microservicios_con_java_21_STAFF.md) | 9 | 03/04/2026 |

---

### 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |
| [BigData ETL con Apache Spark y Java 21](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 03/04/2026 |
---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

*Próximamente*

---

## 📊 Estadísticas del Repositorio

| Métrica | Valor |
|---------|-------|
| Documentos Staff publicados | 22 |
| Módulos con contenido | 8 / 9 |
| Score SRE promedio | 94 / 100 |
| Secciones promedio por documento | 7 |
| Tiempo de generación por documento | ~6 minutos |
| Última actualización | 04/04/2026 |


## 🎯 Criterios de Calidad

Cada documento publicado en este repositorio cumple obligatoriamente:

- ✅ Código Java 21 real y compilable (Records, Virtual Threads, Pattern Matching)
- ✅ Diagramas de arquitectura Mermaid válidos (graph TD / graph LR)
- ✅ Inmutabilidad total — prohibidos los setters, uso de Records
- ✅ Métricas SRE con queries Prometheus reales
- ✅ Checklist de producción con al menos 5 puntos concretos
- ✅ Score mínimo 72/100 en el auditor automático

---

## 👤 Autor

**Joaquín Ríos Heredia**
Staff Engineer · Java 21 · SRE · Cloud Native · GenAI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/joaquinrios-dev-strategist/)

---

*Generado con Authority Engine v21.0 — Pipeline híbrido IA local + revisión académica*
