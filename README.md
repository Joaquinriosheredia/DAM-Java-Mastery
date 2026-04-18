# 🚀 DAM-Java-Mastery | Staff Engineer Technical Library

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Joaquín_Ríos_Heredia-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/joaquinrios-dev-strategist/)
[![Portfolio](https://img.shields.io/badge/Portfolio-Web-blue?style=flat&logo=github)](https://joaquinriosheredia.github.io/DAM-Java-Mastery/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-lightgrey?style=flat&logo=github)](https://github.com/Joaquinriosheredia)
![Docs](https://img.shields.io/badge/Staff_Docs-47-green?style=flat)
![Score](https://img.shields.io/badge/Quality_Score-99%2F100-brightgreen?style=flat)
![Open Source](https://img.shields.io/badge/LangChain4j-Contributor-orange?style=flat)

Staff Engineer-level technical reference library on Java 21, distributed architectures, SRE, security and AI systems. Generated and maintained with **Authority Engine v21.0** — a hybrid local AI + cloud pipeline.

---

## ⚡ Authority Engine v21.0 — Production Pipeline

This repository is not generic documentation. Every document passes through a 4-layer pipeline before publishing:

```
Tavily API (real-time sources)
        ↓
Ollama + Qwen 7b on GPU RTX 4060
7.48 tok/s (CPU) → 48.55 tok/s (GPU) — 6x improvement
        ↓
Automated Quality Auditor (score 0-100, min threshold: 85)
        ↓
AWS Lambda (Python 3.12) + S3 + GitHub
Zero manual intervention — single command deployment
```

**Stack:** Python 3.12 · Ollama · Qwen 7b · AWS Lambda · S3 · boto3 · Tavily API · GitHub Actions

**Key metrics:**
- 47 Staff Engineer documents published
- Average quality score: 99/100
- GPU optimisation: 7.48 → 48.55 tok/s (6x)
- Full automation: local generation → S3 → GitHub with a single command

📄 [Architecture Decision Record — GPU Optimisation](./02_Arquitectura/ADR-001-GPU-Acceleration.md)

---

## 🤝 Open Source Contributions

| Project | Contribution | Status |
|---------|-------------|--------|
| [langchain4j/langchain4j-spring](https://github.com/langchain4j/langchain4j-spring) | Spring Boot starter for Chroma embedding store | [PR #185](https://github.com/langchain4j/langchain4j-spring/pull/185) Open |

---

## 📚 Document Index

### ☕ 01_Java_Core — Java 21 Advanced

| Document | Date |
|----------|------|
| [Clean Code & SOLID Principles with Java 21](./01_Java_Core/clean_code_y_solid_con_java_21_STAFF.md) | Apr 2026 |
| [JVM Garbage Collectors: G1, ZGC and Shenandoah in Production](./01_Java_Core/garbage_collectors_en_la_jvm_g1_zgc_y_shenandoah_en_produccion_STAFF.md) | Apr 2026 |
| [Java 21 Virtual Threads: Structured Concurrency and Massive Scalability](./01_Java_Core/java_21_virtual_threads_STAFF.md) | Apr 2026 |
| [Advanced Concurrency in Java 21: Locks, CAS, ForkJoin](./01_Java_Core/java_concurrencia_avanzada_STAFF.md) | Apr 2026 |
| [Java Memory Model for Production](./01_Java_Core/java_memory_model_produccion_STAFF.md) | Apr 2026 |
| [Real Memory Leaks in Java: Detection and Resolution](./01_Java_Core/memory_leaks_reales_en_java_deteccion_y_solucion_con_visualvm_STAFF.md) | Apr 2026 |
| [Latency Optimisation in Low-Latency Java Applications](./01_Java_Core/optimizacion_de_latencia_en_aplicaciones_java_de_baja_latencia_STAFF.md) | Apr 2026 |
| [Strategy & Observer Patterns with Java 21 Sealed Interfaces](./01_Java_Core/patrones_strategy_y_observer_en_java_21:_implementación_con_sealed_interfaces,_pattern_matching_sobre_records_y_desacoplamiento_funcional_sin_efectos_secundarios_STAFF.md) | Apr 2026 |
| [Advanced Profiling with JFR and Async Profiler](./01_Java_Core/profiling_avanzado_en_java_con_jfr_y_async_profiler_STAFF.md) | Apr 2026 |

---

### 🏛️ 02_Arquitectura — DDD, Hexagonal, Microservices

| Document | Date |
|----------|------|
| [Anti-patterns in Microservices with Java 21](./02_Arquitectura/anti-patterns_en_microservicios_y_como_evitarlos_con_java_21_STAFF.md) | Apr 2026 |
| [Reactive Microservices Architecture with Spring Boot 3.4 and R2DBC](./02_Arquitectura/arquitectura_de_microservicios_reactivos_con_spring_boot_3.3_y_r2dbc_STAFF.md) | Apr 2026 |
| [DDD and Hexagonal Architecture with Java 21](./02_Arquitectura/ddd_y_arquitectura_hexagonal_con_java_21_STAFF.md) | Apr 2026 |
| [Scalable System Design FAANG-Style](./02_Arquitectura/diseno_sistemas_escalables_faang_STAFF.md) | Apr 2026 |
| [Event-Driven Architecture & Transactional Outbox Pattern](./02_Arquitectura/event_driven_architecture_transactional_outbox_java_21_STAFF.md) | Apr 2026 |
| [Event Sourcing & CQRS with Java 21 and Spring Boot](./02_Arquitectura/event_sourcing_y_cqrs_con_java_21_y_spring_boot_STAFF.md) | Apr 2026 |
| [Idempotency in Distributed Systems with Java 21](./02_Arquitectura/idempotencia_sistemas_distribuidos_STAFF.md) | Apr 2026 |
| [Modular Monolith vs Microservices: Architecture Decision Guide](./02_Arquitectura/monolito_modular_vs_microservicios_STAFF.md) | Apr 2026 |
| [Distributed Rate Limiter with Redis and Java 21](./02_Arquitectura/rate_limiter_distribuido_con_redis_y_java_21_STAFF.md) | Apr 2026 |
| [Saga Pattern: Orchestration vs Choreography with Java 21](./02_Arquitectura/saga_pattern_orquestacion_vs_coreografia_con_java_21_STAFF.md) | Apr 2026 |
| [CAP Theorem and Data Consistency in Distributed Systems](./02_Arquitectura/teorema_cap_consistencia_sistemas_reales_STAFF.md) | Apr 2026 |
| [ADR-001: GPU Acceleration for Authority Engine](./02_Arquitectura/ADR-001-GPU-Acceleration.md) | Apr 2026 |

---

### 🌱 03_Spring_Ecosystem — Spring Boot, R2DBC, Security

| Document | Date |
|----------|------|
| [Distributed Observability with OpenTelemetry and Grafana](./03_Spring_Ecosystem/observabilidad_distribuida_en_spring_boot_3.3_con_opentelemetry_y_grafana_loki:_correlación_de_trazas_y_logs_STAFF.md) | Apr 2026 |
| [Resilience4j: Circuit Breaker, Retry and Bulkhead](./03_Spring_Ecosystem/resilience4j_circuit_breaker_retry_bulkhead_spring_boot_3_STAFF.md) | Apr 2026 |
| [Spring Boot 3.4 and R2DBC with Virtual Threads](./03_Spring_Ecosystem/spring_boot_34_r2dbc_virtual_threads_STAFF.md) | Apr 2026 |
| [Advanced Spring Security 6: Method-Level Auth and OAuth2](./03_Spring_Ecosystem/spring_security_6_avanzado_metodo_a_metodo_y_oauth2_resource_server_STAFF.md) | Apr 2026 |

---

### 🗄️ 04_Bases_de_Datos — PostgreSQL, Redis, MongoDB

| Document | Date |
|----------|------|
| [MongoDB with Java 21: Document Modelling and Aggregations](./04_Bases_de_Datos/mongodb_con_java_21_modelado_de_documentos_y_agregaciones_avanzadas_STAFF.md) | Apr 2026 |
| [JVM Optimisation and Distributed Cache with Redis](./04_Bases_de_Datos/optimizacion_jvm_y_cache_distribuida_redis_java_21_STAFF.md) | Apr 2026 |
| [Advanced PostgreSQL 17: Indexes, Partitioning and Query Optimisation](./04_Bases_de_Datos/postgresql_17_avanzado_indices_particionado_y_optimizacion_de_queries_STAFF.md) | Apr 2026 |
| [Advanced Redis: Streams, Pub/Sub and Messaging Patterns](./04_Bases_de_Datos/redis_avanzado_streams_pubsub_y_patrones_de_mensajeria_STAFF.md) | Apr 2026 |
| [Vector Search with pgvector and PostgreSQL 17 for AI Applications](./04_Bases_de_Datos/vector_search_con_pgvector_y_postgresql_17_para_aplicaciones_ia_STAFF.md) | Apr 2026 |

---

### ⚙️ 05_SRE_DevOps — Kubernetes, Terraform, Observability

| Document | Date |
|----------|------|
| [Chaos Engineering with Gremlin and Litmus on Kubernetes](./05_SRE_DevOps/chaos_engineering_con_gremlin_y_litmus_en_kubernetes_STAFF.md) | Apr 2026 |
| [Deadlocks in Production: Detection and Prevention](./05_SRE_DevOps/deadlocks_produccion_deteccion_STAFF.md) | Apr 2026 |
| [Production Debugging: Thread Dumps, Heap Dumps and Profiling](./05_SRE_DevOps/debugging_produccion_dumps_STAFF.md) | Apr 2026 |
| [Advanced Docker: Multi-stage Builds and Distroless for Java 21](./05_SRE_DevOps/docker_avanzado_java_21_optimizacion_STAFF.md) | Apr 2026 |
| [Infrastructure as Code with AWS CDK and Java 21](./05_SRE_DevOps/iac_aws_cdk_java_21_STAFF.md) | Apr 2026 |
| [Kubernetes Auto-scaling and Service Mesh 2026](./05_SRE_DevOps/kubernetes_auto-escalado_service_mesh_2026_STAFF.md) | Apr 2026 |
| [Advanced Linux Process Management](./05_SRE_DevOps/linux_gestion_avanzada_de_procesos_scheduling_y_senales_en_sistemas_productivos_STAFF.md) | Apr 2026 |
| [Kubernetes Deployment Patterns: Blue-Green, Canary and Rolling](./05_SRE_DevOps/patrones_de_despliegue_bluegreen_canary_y_rolling_con_kubernetes_STAFF.md) | Apr 2026 |
| [SLI, SLO and SLAs: Design and Application in Java Microservices](./05_SRE_DevOps/sli_slo_y_slas_diseno_y_aplicacion_real_en_microservicios_java_STAFF.md) | Apr 2026 |

---

### 🔐 06_Seguridad — JWT, OAuth2, Zero Trust

| Document | Date |
|----------|------|
| [JWT, OAuth2 and Zero Trust Security with Java 21](./06_Seguridad/jwt_oauth2_y_zero_trust_security_con_java_21_STAFF.md) | Apr 2026 |
| [Offensive Security and Microservices Auditing with Java 21](./06_Seguridad/seguridad_ofensiva_y_auditoria_de_microservicios_con_java_21_STAFF.md) | Apr 2026 |
| [Advanced Spring Security 6: Granular Method-Level Authorization](./06_Seguridad/spring_security_6_avanzado_metodo_a_metodo_oauth2_resource_server_STAFF.md) | Apr 2026 |
| [Zero Trust: Identity as the New Perimeter](./06_Seguridad/zero_trust_identidad_como_perimetro_java_21_STAFF.md) | Apr 2026 |

---

### 📊 07_BigData_Streaming — Kafka, Spark, Flink

| Document | Date |
|----------|------|
| [Apache Kafka Streams with Java 21: Real-time Stream Processing](./07_BigData_Streaming/apache_kafka_streams_con_java_21_STAFF.md) | Apr 2026 |
| [BigData ETL with Apache Spark and Java 21](./07_BigData_Streaming/bigdata_etl_apache_spark_y_java_21_STAFF.md) | Apr 2026 |
| [Data Mesh: Decentralised Data Ownership with Java 21](./07_BigData_Streaming/data_mesh:_descentralización_de_la_propiedad_del_dato_STAFF.md) | Apr 2026 |

---

### 🤖 08_IA_Agentes — RAG, LangChain4j, LLMOps

| Document | Date |
|----------|------|
| [Autonomous Agents with Long-term Memory and LangChain4j](./08_IA_Agentes/agentes_autonomos_memoria_largo_plazo_langchain4j_STAFF.md) | Apr 2026 |
| [Advanced RAG with Local Embeddings and Reranking in Java 21](./08_IA_Agentes/rag_avanzado_embeddings_locales_y_reranking_langchain4j_STAFF.md) | Apr 2026 |
| [Multi-Agent Systems with LangChain4j and Ollama](./08_IA_Agentes/sistemas_multi-agente_con_langchain4j_y_ollama_STAFF.md) | Apr 2026 |
| [Tool Calling and Function Calling with Qwen2.5 and LangChain4j](./08_IA_Agentes/tool_calling_function_calling_qwen2_5_langchain4j_STAFF.md) | Apr 2026 |

---

### 🔭 10_Vanguardia — Emerging Technologies 2026

| Document | Date |
|----------|------|
| [GraalVM Native Image: AOT Compilation for Spring Boot Java 21](./10_Vanguardia/graalvm_native_image_compilacion_aot_java_21_STAFF.md) | Apr 2026 |

---

## 📊 Repository Stats

| Metric | Value |
|--------|-------|
| Staff Engineer documents | 47 |
| Modules with content | 9 / 10 |
| Average quality score | 99 / 100 |
| GPU optimisation | 7.48 → 48.55 tok/s (6x) |
| Last updated | April 2026 |

---

## 👤 Author

**Joaquín Ríos Heredia**
Java 21 Engineer · AI & Agents · Cloud AWS · Backend

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/joaquinrios-dev-strategist/)

*Generated with Authority Engine v21.0 — Hybrid local AI pipeline + AWS cloud deployment*
