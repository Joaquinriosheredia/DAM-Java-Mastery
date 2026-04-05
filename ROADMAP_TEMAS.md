# ROADMAP — DAM-Java-Mastery
# Temas pendientes ordenados por prioridad estratégica
# Ejecutar con: racha2026 "tema
# Actualizado: 03/04/2026

# ═══════════════════════════════════════════════════════════════
# BLOQUE 1 — JAVA CORE (completar 01_Java_Core)
# Carpeta más visible — reclutadores la miran primero
# ═══════════════════════════════════════════════════════════════

- [x] Event Sourcing y CQRS con Java 21 y Spring Boot
- [ ] Garbage Collectors en la JVM: G1, ZGC y Shenandoah en produccion
- [ ] Profiling avanzado en Java con JFR y Async Profiler
- [x] Memory leaks reales en Java: deteccion y solucion con VisualVM
- [ ] Optimizacion de latencia en aplicaciones Java de baja latencia
- [ ] Structured Concurrency y Virtual Threads avanzados en Java 21

# ═══════════════════════════════════════════════════════════════
# BLOQUE 2 — ARQUITECTURA (completar 02_Arquitectura)
# Temas de System Design — diferencian Staff de Senior
# ═══════════════════════════════════════════════════════════════

- [x] Saga Pattern: orquestacion vs coreografia con Java 21
- [ ] Anti-patterns en microservicios y como evitarlos con Java 21
- [ ] Monolito modular vs microservicios: cuando elegir cada uno
- [ ] Consistencia eventual: problemas reales y soluciones con Java 21
- [ ] Trade-offs CAP en sistemas reales con casos practicos Java
- [ ] Diseno de APIs idempotentes en sistemas criticos con Spring Boot
- [ ] Diseno de un sistema de pagos resiliente con exactly-once semantics
- [ ] Arquitectura de un sistema de notificaciones distribuido con Java 21
- [ ] Rate limiter distribuido con Redis y Java 21
- [ ] Diseno de un sistema tipo Uber a gran escala con Java 21

# ═══════════════════════════════════════════════════════════════
# BLOQUE 3 — SPRING ECOSYSTEM (completar 03_Spring_Ecosystem)
# ═══════════════════════════════════════════════════════════════

- [ ] Resilience4j: Circuit Breaker Retry y Bulkhead en Spring Boot 3
- [ ] Spring Security 6 avanzado: metodo a metodo y OAuth2 Resource Server
- [ ] Spring Batch 5 para procesamiento masivo de datos con Java 21
- [ ] Testing avanzado en Spring Boot con JUnit 5 y Testcontainers

# ═══════════════════════════════════════════════════════════════
# BLOQUE 4 — BASES DE DATOS (completar 04_Bases_de_Datos)
# Carpeta vacia — una sola entrada ahora mismo
# ═══════════════════════════════════════════════════════════════

- [ ] PostgreSQL 17 avanzado: indices particionado y optimizacion de queries
- [x] Vector Search con pgvector y PostgreSQL 17 para aplicaciones IA
- [ ] MongoDB con Java 21: modelado de documentos y agregaciones avanzadas
- [ ] Redis avanzado: Streams pub-sub y patrones de mensajeria
- [ ] SurrealDB como alternativa multimodelo en produccion con Java

# ═══════════════════════════════════════════════════════════════
# BLOQUE 5 — SRE Y DEVOPS (completar 05_SRE_DevOps)
# ═══════════════════════════════════════════════════════════════

- [ ] SLI SLO y SLAs: diseno y aplicacion real en microservicios Java
- [ ] Alerting efectivo: como evitar el alert fatigue en Prometheus
- [ ] Chaos Engineering con Gremlin y Litmus en Kubernetes
- [ ] Patrones de despliegue: Blue-Green Canary y Rolling con Kubernetes
- [ ] Automatizacion de Infraestructura como Codigo con Ansible y Terraform
- [ ] Seguridad y Hardening de Servidores Ubuntu para Produccion
- [ ] Arquitectura multi-region activa-activa en AWS con Java 21
- [ ] Cost optimization en infraestructura cloud a gran escala
- [ ] Diseno de sistemas fault-tolerant en cloud con Spring Boot

# ═══════════════════════════════════════════════════════════════
# BLOQUE 6 — SEGURIDAD (completar 06_Seguridad)
# ═══════════════════════════════════════════════════════════════

- [ ] Zero Trust: la identidad como nuevo perimetro con Java 21
- [ ] Post-Quantum Cryptography: el fin de RSA y migracion con Java
- [ ] Secrets management con HashiCorp Vault en produccion
- [ ] Broken Access Control: casos reales y mitigacion con Spring Security
- [ ] Seguridad en APIs REST: ataques reales y defensa con Java 21
- [ ] Phishing Generativo e IA Ofensiva 2026: defensa tecnica
- [ ] Generacion automatica de SBOM con CycloneDX y Java 21

# ═══════════════════════════════════════════════════════════════
# BLOQUE 7 — BIGDATA Y STREAMING (completar 07_BigData_Streaming)
# ═══════════════════════════════════════════════════════════════

- [ ] BigData ETL con Apache Spark y Java 21 para transformacion masiva
- [ ] Orquestacion de Workflows complejos con Apache Airflow 2026
- [ ] Arquitecturas de Datos en Tiempo Real con Kafka y Flink
- [ ] Apache Flink con Java 21: procesamiento de streams stateful

# ═══════════════════════════════════════════════════════════════
# BLOQUE 8 — IA Y AGENTES (completar 08_IA_Agentes)
# ═══════════════════════════════════════════════════════════════

- [ ] RAG Avanzado con embeddings locales y reranking con LangChain4j
- [ ] Agentes Autonomos con memoria a largo plazo y LangChain4j
- [ ] Tool Calling y Function Calling con Qwen2.5 y LangChain4j
- [ ] Defensa contra Prompt Injection en agentes IA con Java
- [ ] Arquitectura RAG escalable en produccion con pgvector y Java 21
- [ ] Evaluacion de modelos LLM: metricas reales y benchmarks
- [ ] Cost control en sistemas con LLM: caching y optimizacion
- [ ] LLMOps: ciclo de vida de modelos en produccion con Java

# ═══════════════════════════════════════════════════════════════
# BLOQUE 9 — HEALTHTECH (nueva carpeta de alto valor)
# Nicho diferenciador — muy pocos repositorios cubren esto
# ═══════════════════════════════════════════════════════════════

- [ ] HAPI FHIR: Transformador HL7 v2 a FHIR Bundle con Java 21
- [ ] Interoperabilidad Sanitaria con FHIR R4 y Spring Boot
- [ ] Auditoria GDPR de accesos a datos clinicos con Java 21
- [ ] Sistemas Clinicos Seguros con HL7 y Java 21

# ═══════════════════════════════════════════════════════════════
# BLOQUE 10 — VANGUARDIA 2026 (10_Vanguardia)
# Tendencias que posicionan el perfil como referencia actual
# ═══════════════════════════════════════════════════════════════

- [ ] GraalVM Native Image: compilacion AOT de aplicaciones Spring Boot
- [ ] WebAssembly en el servidor con Java 21 y WasmEdge
- [ ] Platform Engineering: construir IDPs con Backstage y Java
- [ ] eBPF para observabilidad avanzada en Kubernetes 2026
- [ ] Serverless con Java 21: AWS Lambda SnapStart y Quarkus
