# 🚀 DAM-Java-Mastery | Biblioteca Técnica Staff Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Joaquín_Ríos_Heredia-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/joaquinrios-dev-strategist/)
[![Web](https://img.shields.io/badge/Web-DAM--Java--Mastery-blue?style=flat&logo=github)](https://joaquinriosheredia.github.io/DAM-Java-Mastery/)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-lightgrey?style=flat&logo=github)](https://github.com/Joaquinriosheredia)
![Documentos](https://img.shields.io/badge/Documentos_Staff-43-green?style=flat)
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
| [Clean Code y Principios SOLID con Java 21: Arquitectura de Software Inmutable, V...](./01_Java_Core/clean_code_y_solid_con_java_21_STAFF.md) | 12 | 16/04/2026 |
| [Garbage Collectors en la JVM: G1, ZGC y Shenandoah en Producción con Java 21 — G...](./01_Java_Core/garbage_collectors_en_la_jvm_g1_zgc_y_shenandoah_en_produccion_STAFF.md) | 15 | 16/04/2026 |
| [Java 21 Virtual Threads: Concurrencia Estructurada y Escalabilidad Masiva en Pro...](./01_Java_Core/java_21_virtual_threads_STAFF.md) | 15 | 16/04/2026 |
| [Java Memory Model (JMM) Explicado para Producción: Concurrencia, Visibilidad y O...](./01_Java_Core/java_memory_model_produccion_STAFF.md) | 13 | 17/04/2026 |
| [Memory Leaks Reales en Java: Detección Forense, Análisis con JFR y Solución Estr...](./01_Java_Core/memory_leaks_reales_en_java_deteccion_y_solucion_con_visualvm_STAFF.md) | 15 | 16/04/2026 |
| [Optimización de Latencia en Aplicaciones Java de Baja Latencia: Ingeniería de Re...](./01_Java_Core/optimizacion_de_latencia_en_aplicaciones_java_de_baja_latencia_STAFF.md) | 15 | 16/04/2026 |
| [Patrones Strategy y Observer con Java 21: Sealed Interfaces, Pattern Matching y ...](./01_Java_Core/patrones_strategy_y_observer_en_java_21:_implementación_con_sealed_interfaces,_pattern_matching_sobre_records_y_desacoplamiento_funcional_sin_efectos_secundarios_STAFF.md) | 15 | 16/04/2026 |
| [Profiling Avanzado en Java: JFR, Async Profiler y Observabilidad de Rendimiento ...](./01_Java_Core/profiling_avanzado_en_java_con_jfr_y_async_profiler_STAFF.md) | 15 | 16/04/2026 |

---

### 🏛️ 02_Arquitectura — DDD, Hexagonal, Microservicios

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Anti-patterns en Microservicios y Cómo Evitarlos con Java 21 — Guía Staff Engine...](./02_Arquitectura/anti-patterns_en_microservicios_y_como_evitarlos_con_java_21_STAFF.md) | 15 | 16/04/2026 |
| [Arquitectura de Microservicios Reactivos con Spring Boot 3.4 y R2DBC: Concurrenc...](./02_Arquitectura/arquitectura_de_microservicios_reactivos_con_spring_boot_3.3_y_r2dbc_STAFF.md) | 15 | 16/04/2026 |
| [DDD y Arquitectura Hexagonal con Java 21: Diseño de Dominio Inmutable, Puertos T...](./02_Arquitectura/ddd_y_arquitectura_hexagonal_con_java_21_STAFF.md) | 15 | 16/04/2026 |
| [Event-Driven Architecture y Transactional Outbox Pattern con Java 21: Atomicidad...](./02_Arquitectura/event_driven_architecture_transactional_outbox_java_21_STAFF.md) | 15 | 16/04/2026 |
| [Event Sourcing y CQRS con Java 21 y Spring Boot: Inmutabilidad, Trazabilidad Tot...](./02_Arquitectura/event_sourcing_y_cqrs_con_java_21_y_spring_boot_STAFF.md) | 15 | 16/04/2026 |
| [Rate Limiter Distribuido con Redis y Java 21: Atomicidad, Resiliencia y Protecci...](./02_Arquitectura/rate_limiter_distribuido_con_redis_y_java_21_STAFF.md) | 15 | 16/04/2026 |
| [Saga Pattern: Orquestación vs Coreografía con Java 21 — Transacciones Distribuid...](./02_Arquitectura/saga_pattern_orquestacion_vs_coreografia_con_java_21_STAFF.md) | 15 | 16/04/2026 |

---

### 🌱 03_Spring_Ecosystem — Spring Boot, R2DBC, WebFlux

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Observabilidad Distribuida en Spring Boot 3.4 con OpenTelemetry y Grafana: Corre...](./03_Spring_Ecosystem/observabilidad_distribuida_en_spring_boot_3.3_con_opentelemetry_y_grafana_loki:_correlación_de_trazas_y_logs_STAFF.md) | 15 | 17/04/2026 |
| [Resilience4j en Spring Boot 3.4: Circuit Breaker, Retry y Bulkhead con Java 21 —...](./03_Spring_Ecosystem/resilience4j_circuit_breaker_retry_bulkhead_spring_boot_3_STAFF.md) | 15 | 17/04/2026 |
| [Spring Boot 3.4 y R2DBC con Virtual Threads: Concurrencia Reactiva vs Imperativa...](./03_Spring_Ecosystem/spring_boot_34_r2dbc_virtual_threads_STAFF.md) | 14 | 17/04/2026 |
| [Spring Security 6 Avanzado: Autorización Método a Método y OAuth2 Resource Serve...](./03_Spring_Ecosystem/spring_security_6_avanzado_metodo_a_metodo_y_oauth2_resource_server_STAFF.md) | 16 | 17/04/2026 |

---

### 🗄️ 04_Bases_de_Datos — PostgreSQL, Redis, MongoDB

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [MongoDB con Java 21: Modelado de Documentos, Agregaciones Avanzadas y Patrones d...](./04_Bases_de_Datos/mongodb_con_java_21_modelado_de_documentos_y_agregaciones_avanzadas_STAFF.md) | 15 | 17/04/2026 |
| [Optimización de JVM y Caché Distribuida con Redis y Java 21: Estrategias de Rend...](./04_Bases_de_Datos/optimizacion_jvm_y_cache_distribuida_redis_java_21_STAFF.md) | 15 | 17/04/2026 |
| [PostgreSQL 17 Avanzado: Índices, Particionado y Optimización de Queries con Java...](./04_Bases_de_Datos/postgresql_17_avanzado_indices_particionado_y_optimizacion_de_queries_STAFF.md) | 15 | 17/04/2026 |
| [Redis Avanzado: Streams, Pub/Sub y Patrones de Mensajería con Java 21 — Guía Sta...](./04_Bases_de_Datos/redis_avanzado_streams_pubsub_y_patrones_de_mensajeria_STAFF.md) | 15 | 17/04/2026 |
| [Vector Search con pgvector y PostgreSQL 17 para Aplicaciones IA: Indexación HNSW...](./04_Bases_de_Datos/vector_search_con_pgvector_y_postgresql_17_para_aplicaciones_ia_STAFF.md) | 15 | 17/04/2026 |

---

### ⚙️ 05_SRE_DevOps — Kubernetes, Terraform, Observabilidad

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Chaos Engineering con Gremlin y Litmus en Kubernetes: Resiliencia Proactiva y Va...](./05_SRE_DevOps/chaos_engineering_con_gremlin_y_litmus_en_kubernetes_STAFF.md) | 15 | 17/04/2026 |
| [Docker Avanzado: Multi-stage Builds, Imágenes Distroless y Optimización para Jav...](./05_SRE_DevOps/docker_avanzado_java_21_optimizacion_STAFF.md) | 15 | 17/04/2026 |
| [Infraestructura como Código (IaC) con AWS CDK y Java 21: Arquitectura Declarativ...](./05_SRE_DevOps/iac_aws_cdk_java_21_STAFF.md) | 12 | 17/04/2026 |
| [Kubernetes Auto-Escalado y Service Mesh en 2026: HPA, VPA, KEDA e Istio con Java...](./05_SRE_DevOps/kubernetes_auto-escalado_service_mesh_2026_STAFF.md) | 15 | 17/04/2026 |
| [Linux Gestión Avanzada de Procesos, Scheduling y Señales en Sistemas Productivos...](./05_SRE_DevOps/linux_gestion_avanzada_de_procesos_scheduling_y_senales_en_sistemas_productivos_STAFF.md) | 12 | 17/04/2026 |
| [Patrones de Despliegue en Kubernetes: Blue-Green, Canary y Rolling con Java 21 —...](./05_SRE_DevOps/patrones_de_despliegue_bluegreen_canary_y_rolling_con_kubernetes_STAFF.md) | 14 | 17/04/2026 |
| [SLI, SLO y SLAs: Diseño y Aplicación Real en Microservicios Java 21 — Guía Staff...](./05_SRE_DevOps/sli_slo_y_slas_diseno_y_aplicacion_real_en_microservicios_java_STAFF.md) | 14 | 17/04/2026 |

---

### 🔐 06_Seguridad — JWT, OAuth2, Zero Trust

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [JWT, OAuth2 y Zero Trust Security con Java 21 y Spring Security 6 — Guía Staff E...](./06_Seguridad/jwt_oauth2_y_zero_trust_security_con_java_21_STAFF.md) | 14 | 17/04/2026 |
| [Seguridad Ofensiva y Auditoría de Microservicios con Java 21: Pentesting Automat...](./06_Seguridad/seguridad_ofensiva_y_auditoria_de_microservicios_con_java_21_STAFF.md) | 13 | 17/04/2026 |
| [Spring Security 6 Avanzado: Autorización Granular Método-a-Método y OAuth2 Resou...](./06_Seguridad/spring_security_6_avanzado_metodo_a_metodo_oauth2_resource_server_STAFF.md) | 12 | 17/04/2026 |
| [Zero Trust: La Identidad como Nuevo Perímetro con Java 21 y Spring Security 6 — ...](./06_Seguridad/zero_trust_identidad_como_perimetro_java_21_STAFF.md) | 12 | 17/04/2026 |

---

### 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21: Procesamiento de Streams en Tiempo Real, State...](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 13 | 17/04/2026 |
| [BigData ETL con Apache Spark y Java 21: Procesamiento Distribuido, Optimización ...](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 12 | 17/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21 — Guía Staff E...](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 8 | 17/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 13 | 17/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 14 | 17/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21: Arquitectura de Agent...](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 11 | 17/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 14 | 17/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 14 | 17/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21: Procesamiento de Streams en Tiempo Real, State...](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 13 | 17/04/2026 |
| [BigData ETL con Apache Spark y Java 21: Procesamiento Distribuido, Optimización ...](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 12 | 17/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21 — Guía Staff E...](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 8 | 17/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 13 | 17/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 14 | 17/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21: Arquitectura de Agent...](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 11 | 17/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 14 | 17/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 14 | 17/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 7 | 10/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 7 | 10/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 7 | 10/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 7 | 10/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 7 | 10/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21: Arquitectura de Transformación Masiva, C...](./07_BigData_Streaming/bigdata_etl_apache_spark_java_21_STAFF.md) | 7 | 10/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

### 🔭 10_Vanguardia — Tendencias y novedades 2026

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [GraalVM Native Image: Compilación AOT de Aplicaciones Spring Boot en Java 21 — G...](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | 7 | 10/04/2026 |

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21: Arquitectura de Transformación Masiva, C...](./07_BigData_Streaming/bigdata_etl_apache_spark_java_21_STAFF.md) | 7 | 10/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |
| [Tool Calling y Function Calling con Qwen2.5 y LangChain4j: Arquitectura de Agent...](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | 7 | 09/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Agentes Autónomos con Memoria a Largo Plazo y LangChain4j: Arquitectura de Persi...](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
| [Data Mesh: Descentralización de la Propiedad del Dato con Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | 7 | 03/04/2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [RAG Avanzado con Embeddings Locales y Reranking en Java 21: Arquitectura de Prec...](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | 7 | 09/04/2026 |
| [Sistemas Multi-Agente con LangChain4j y Ollama en Java 21](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | 7 | 03/04/2026 |

---

### 📱 09_Frontend_Mobile — Flutter, Android, Kotlin

*Próximamente*

---

## 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Documento | Secciones | Fecha |
|-----------|-----------|-------|
| [Apache Kafka Streams con Java 21](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | 5 | 02/04/2026 |
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| [BigData ETL con Apache Spark y Java 21 para Transformación Masiva](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | 6 | 07/04/2026 |
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
| Documentos Staff publicados | 43 |
| Módulos con contenido | 9 / 10 |
| Score SRE promedio | 94 / 100 |
| Secciones promedio por documento | 7 |
| Tiempo de generación por documento | ~6 minutos |
| Última actualización | 17/04/2026 |


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
