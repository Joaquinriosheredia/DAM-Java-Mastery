# ROADMAP — DAM-Java-Mastery
# Temas pendientes ordenados por prioridad estratégica
# Ejecutar con: racha2026 "tema"
# Actualizado: 2026-04-25 (auto-sync ae-inventario)

# ═══════════════════════════════════════════════════════════════
# BLOQUE 1 — JAVA CORE (01_Java_Core/)
# Fundamentos del lenguaje y runtime para alta performance
# ═══════════════════════════════════════════════════════════════

- [x] Clean Code y SOLID con Java 21
- [x] Patrones Strategy y Observer: sealed interfaces, pattern matching, records
- [x] Garbage Collectors en la JVM: G1, ZGC y Shenandoah en produccion
- [x] Java 21 Virtual Threads: concurrencia estructurada y escalabilidad
- [x] Structured Concurrency y Scoped Values: Project Loom completo
- [x] Memory leaks reales en Java: deteccion y solucion con VisualVM
- [x] Profiling avanzado en Java con JFR y Async Profiler
- [x] Optimizacion de latencia en aplicaciones Java de baja latencia
- [x] Concurrencia Avanzada: Locks, CAS, ForkJoin y Concurrencia Estructurada
- [x] Java Memory Model (JMM): concurrencia, visibilidad y ordenamiento
- [x] Internals de HashMap y ConcurrentHashMap con Java 21
- [x] Optimistic vs Pessimistic Locking con Java 21
- [x] Deadlocks en Produccion: deteccion, prevencion y solucion
- [x] Debugging en Produccion: Thread Dumps, Heap Dumps y Profiling
- [ ] Foreign Function & Memory (FFM) API: reemplazo moderno de JNI
- [ ] Class Loading y JVM Internals: metaspace, CDS, JIT compilation
- [ ] Concurrency lock-free: VarHandle, Disruptor, false sharing
- [ ] Java 21 Migration Strategy: migracion incremental desde Java 8/11
- [ ] Reactive Programming: Project Reactor vs Virtual Threads decision framework
- [ ] Testing en Java 21: unit, integration, property-based, Testcontainers
- [x] Mocking vs Stubs vs Fakes: diferencias reales y estrategias de aislamiento
- [ ] Seguridad en Java: JWT, crypto moderna, secrets management

# ═══════════════════════════════════════════════════════════════
# BLOQUE 2 — ARQUITECTURA (02_Arquitectura/)
# System Design, patrones distribuidos y toma de decisiones
# ═══════════════════════════════════════════════════════════════

- [x] Saga Pattern: orquestacion vs coreografia con Java 21
- [x] Anti-patterns en microservicios y como evitarlos con Java 21
- [x] Rate limiter distribuido con Redis y Java 21
- [x] DDD y Arquitectura Hexagonal con Java 21
- [x] Event-Driven Architecture + Outbox Pattern
- [x] Event Sourcing y CQRS con Java 21 y Spring Boot
- [x] Arquitectura Clean vs Hexagonal vs Onion: guia de decision
- [x] Diseno de APIs: REST vs GraphQL vs gRPC con Java 21
- [x] Diseno de Sistemas Escalables tipo FAANG con Java 21
- [x] Domain Events y Event Storming con Java 21
- [x] Latencia vs Throughput: optimizacion de sistemas distribuidos Java 21
- [x] Patrones de Orquestacion Distribuida: Saga, Choreography y Orchestrator
- [x] Patrones de Reintento y Manejo de Fallos: Circuit Breakers y Backoff
- [x] Resiliencia: Timeouts y Circuit Breakers en sistemas distribuidos
- [x] Transacciones Distribuidas mas alla de Saga: consistencia y compensacion
- [x] Microservicios Reactivos: R2DBC + Virtual Threads
- [x] Monolito modular vs microservicios: cuando elegir cada uno
- [x] Consistencia eventual: problemas reales y soluciones con Java 21
- [x] Trade-offs CAP en sistemas reales con casos practicos Java
- [x] Diseno de APIs idempotentes en sistemas criticos con Spring Boot
- [ ] Diseno de un sistema de pagos resiliente con exactly-once semantics
- [ ] Arquitectura de un sistema de notificaciones distribuido con Java 21
- [ ] Diseno de un sistema tipo Uber a gran escala con Java 21
- [ ] API Versioning: estrategias de evolucion sin breaking changes
- [x] Backends for Frontends (BFF): GraphQL vs REST especificos por cliente
- [ ] Event-Driven Architecture: event-carried state transfer vs notification
- [x] Caching a escala: invalidacion, Caffeine vs Redis vs CDN
- [x] Multi-tenancy: discriminador vs bases separadas vs schemas separados
- [x] Arquitectura de sistemas IA en produccion: despliegue, observabilidad y fiabilidad
- [x] Backpressure en sistemas reactivos con Java 21: control de flujo y resiliencia
- [ ] Data residency y soberania: GDPR, Schrems II, region locking

# ═══════════════════════════════════════════════════════════════
# BLOQUE 3 — SPRING ECOSYSTEM (03_Spring_Ecosystem/)
# Framework principal y ecosistema de integracion
# ═══════════════════════════════════════════════════════════════

- [x] Resilience4j: Circuit Breaker, Retry y Bulkhead en Spring Boot 3
- [x] Observabilidad con OpenTelemetry, Prometheus y Grafana
- [x] Spring Boot Reactivo: R2DBC + Virtual Threads optimizacion
- [x] Spring Security 6 avanzado: metodo a metodo y OAuth2 Resource Server
- [ ] Spring Batch 5 para procesamiento masivo de datos con Java 21
- [x] Testing avanzado en Spring Boot con JUnit 5 y Testcontainers
- [x] Spring Boot Performance Tuning en Produccion
- [x] Spring Cloud: Config, Gateway y Service Discovery
- [ ] Spring Cloud Gateway: rate limiting, auth centralizada, multi-cluster
- [ ] Spring for Apache Kafka: producers, consumers, streams, exactly-once
- [ ] Spring Data JDBC vs JPA: decisiones de persistencia y performance
- [x] Event Sourcing y CQRS con Spring Boot (mover de Arquitectura si aplica)

# ═══════════════════════════════════════════════════════════════
# BLOQUE 4 — BASES DE DATOS (04_Bases_de_Datos/)
# Persistencia, modelado y optimizacion de datos
# ═══════════════════════════════════════════════════════════════

- [x] PostgreSQL 17 avanzado: indices, particionado y optimizacion de queries
- [x] Vector Search con pgvector y PostgreSQL 17 para aplicaciones IA
- [x] MongoDB con Java 21: modelado de documentos y agregaciones avanzadas
- [x] Redis avanzado: Streams, pub-sub y patrones de mensajeria
- [x] Optimizacion JVM + Redis Cache: estrategias de cacheo distribuido
- [ ] SurrealDB como alternativa multimodelo en produccion con Java
- [ ] Database migrations a escala: Flyway vs Liquibase, zero-downtime DDL
- [ ] Change Data Capture (CDC): Debezium con PostgreSQL y Kafka
- [ ] Connection pooling avanzado: HikariCP tuning y troubleshooting

# ═══════════════════════════════════════════════════════════════
# BLOQUE 5 — SRE Y DEVOPS (05_SRE_DevOps/)
# [NOTA: 05_SRE_DevOps_Cloud/ debe consolidarse aqui o renombrarse]
# Operaciones, observabilidad, fiabilidad y cloud
# ═══════════════════════════════════════════════════════════════

- [x] Chaos Engineering con Gremlin y Litmus en Kubernetes
- [x] Patrones de despliegue: Blue-Green, Canary y Rolling con Kubernetes
- [x] Docker avanzado: multi-stage builds, distroless, optimizacion Java 21
- [x] Kubernetes auto-escalado: HPA, VPA, cluster autoscaling
- [x] IaC con AWS CDK en Java 21: infraestructura programable
- [x] SLI, SLO y SLAs: diseno y aplicacion real en microservicios Java
- [x] Alerting efectivo: como evitar el alert fatigue en Prometheus
- [x] Linux: Gestion Avanzada de Procesos, Scheduling y Senales
- [x] Observabilidad: metricas, logs, trazas y alerting en SRE
- [x] Postmortems de Fallos Reales en Produccion: analisis forense y prevencion
- [ ] Automatizacion de Infraestructura como Codigo con Ansible y Terraform
- [ ] Seguridad y Hardening de Servidores Ubuntu para Produccion
- [ ] Arquitectura multi-region activa-activa en AWS con Java 21
- [ ] Cost optimization en infraestructura cloud a gran escala
- [ ] Diseno de sistemas fault-tolerant en cloud con Spring Boot
- [ ] Observability-driven development: metricas como requisito funcional
- [ ] Capacity planning: forecasting basado en trafico y seasonality
- [ ] Disaster Recovery: RTO/RPO definidos, runbooks automatizados, game days
- [ ] FinOps avanzado: tagging strategy, chargeback, reserved instances
- [ ] GitOps: ArgoCD/Flux, drift detection, progressive delivery

# ═══════════════════════════════════════════════════════════════
# BLOQUE 6 — SEGURIDAD (06_Seguridad/)
# Seguridad aplicada, zero trust y compliance
# ═══════════════════════════════════════════════════════════════

- [x] Zero Trust: la identidad como nuevo perimetro con Java 21
- [x] JWT y OAuth2: implementacion segura y Zero Trust
- [x] Seguridad ofensiva y auditoria de aplicaciones Java
- [ ] Post-Quantum Cryptography: el fin de RSA y migracion con Java
- [ ] Secrets management con HashiCorp Vault en produccion
- [ ] Broken Access Control: casos reales y mitigacion con Spring Security
- [ ] Seguridad en APIs REST: ataques reales y defensa con Java 21
- [ ] Phishing Generativo e IA Ofensiva 2026: defensa tecnica
- [ ] Generacion automatica de SBOM con CycloneDX y Java 21
- [ ] Supply chain security: SLSA framework, signed commits, reproducible builds
- [ ] Container security: distroless, non-root, read-only rootfs, seccomp
- [ ] Threat modeling: STRIDE para arquitecturas Java, attack trees
- [ ] Security chaos engineering: validando controles en produccion
- [ ] OWASP API Security Top 10 2026: mitigaciones especificas Java/Spring

# ═══════════════════════════════════════════════════════════════
# BLOQUE 7 — BIGDATA Y STREAMING (07_BigData_Streaming/)
# Procesamiento distribuido de datos masivos
# ═══════════════════════════════════════════════════════════════

- [x] BigData ETL con Apache Spark y Java 21: transformacion masiva
- [x] Apache Kafka Streams: procesamiento stateful de eventos
- [x] Data Mesh: arquitectura de datos distribuida y federada
- [ ] Orquestacion de Workflows complejos con Apache Airflow 2026
- [ ] Arquitecturas de Datos en Tiempo Real con Kafka y Flink
- [ ] Apache Flink con Java 21: procesamiento de streams stateful
- [ ] Kafka Streams vs Kafka Connect: arquitectura de integracion
- [ ] Optimizacion de Spark: AQE, broadcast joins, skew handling

# ═══════════════════════════════════════════════════════════════
# BLOQUE 8 — DATA ENGINEERING (08_Data_Engineering/) [NUEVO]
# Gobernanza, calidad y arquitectura de datos moderna
# ═══════════════════════════════════════════════════════════════

- [ ] Data Contracts: calidad en origen vs en destino, shift-left
- [ ] Data Mesh: domain-oriented distributed data, federated governance
- [ ] Lakehouse Architecture: Iceberg vs Delta Lake vs Hudi
- [ ] Real-time Analytics: ClickHouse, Druid o Pinot con Java
- [ ] Data Lineage y catalogo: Apache Atlas, DataHub, OpenLineage
- [ ] Feature Stores: Feast, Tecton, MLflow para ML en produccion
- [ ] Batch vs Streaming: decision framework, Lambda y Kappa architectures

# ═══════════════════════════════════════════════════════════════
# BLOQUE 9 — IA Y AGENTES (09_IA_Agentes/)
# Inteligencia artificial aplicada con Java
# ═══════════════════════════════════════════════════════════════

- [x] RAG Avanzado con embeddings locales y reranking con LangChain4j
- [x] Agentes Autonomos con memoria a largo plazo y LangChain4j
- [x] Tool Calling y Function Calling con Qwen2.5 y LangChain4j
- [x] Sistemas Multi-Agente: coordinacion y comunicacion
- [ ] Defensa contra Prompt Injection en agentes IA con Java
- [ ] Arquitectura RAG escalable en produccion con pgvector y Java 21
- [ ] Evaluacion de modelos LLM: metricas reales y benchmarks
- [ ] Cost control en sistemas con LLM: caching y optimizacion
- [ ] LLMOps: ciclo de vida de modelos en produccion con Java
- [ ] Multi-agent systems: coordinacion, consenso, conflict resolution
- [ ] Embeddings optimization: quantization, dimensionality reduction
- [ ] Fine-tuning vs RAG vs Prompt Engineering: decision framework
- [ ] Observability en LLMs: tracing de chains, evaluacion de context
- [ ] Ethical AI y bias detection: metricas de fairness en produccion

# ═══════════════════════════════════════════════════════════════
# BLOQUE 10 — HEALTHTECH (10_HealthTech/)
# Sistemas clinicos, interoperabilidad y regulacion sanitaria
# ═══════════════════════════════════════════════════════════════

- [x] HAPI FHIR: Transformador HL7 v2 a FHIR Bundle con Java 21
- [x] Interoperabilidad Sanitaria con FHIR R4 y Spring Boot
- [ ] Auditoria GDPR de accesos a datos clinicos con Java 21
- [ ] Sistemas Clinicos Seguros con HL7 y Java 21
- [ ] DICOM processing: imagenes medicas en arquitecturas cloud
- [ ] Clinical Decision Support: reglas clinicas, alertas inteligentes
- [ ] HIPAA compliance tecnico: encryption, audit logs, access controls

# ═══════════════════════════════════════════════════════════════
# BLOQUE 11 — FINTECH SYSTEMS (11_FinTech_Systems/) [NUEVO]
# Sistemas financieros criticos, alta precision y compliance
# ═══════════════════════════════════════════════════════════════

- [ ] Ledger Accounting: double-entry invariants en sistemas distribuidos
- [ ] Distributed Transactions: Saga vs 2PC vs TCC, compensaciones
- [ ] Currency handling: precision decimal, FX rates, rounding policies
- [ ] PCI-DSS compliance en arquitecturas cloud-native
- [ ] Real-time fraud detection: rules engines vs ML inference &lt;100ms
- [ ] SEPA/SWIFT integration: mensajeria financiera internacional
- [ ] Blockchain para enterprise: Hyperledger Fabric, R3 Corda con Java
- [ ] Open Banking: PSD2, APIs de terceros, consent management

# ═══════════════════════════════════════════════════════════════
# BLOQUE 12 — PLATFORM ENGINEERING (12_Platform_Engineering/) [NUEVO]
# Construccion de plataformas internas, IDPs y developer experience
# ═══════════════════════════════════════════════════════════════

- [ ] Internal Developer Platform (IDP): arquitectura y go-to-market interno
- [ ] API Gateway como Producto: Kong vs AWS API GW vs Envoy/Traefik
- [ ] Service Mesh: Istio, Linkerd, Cilium — decision arquitectonica
- [ ] Event Catalog y Schema Governance con AsyncAPI
- [ ] Feature Flags a escala: Unleash vs LaunchDarkly vs OpenFeature
- [ ] Developer Portals: Backstage, service catalog, docs-like-code
- [ ] Golden Paths: templates, starter kits, paved roads
- [ ] Platform metrics: DORA, developer experience surveys, adoption

# ═══════════════════════════════════════════════════════════════
# BLOQUE 13 — LEGACY MODERNIZATION (13_Legacy_Modernization/) [NUEVO]
# Estrategias de migracion y evolucion de sistemas enterprise
# ═══════════════════════════════════════════════════════════════

- [ ] Strangler Fig Pattern: migracion incremental de monolitos
- [ ] Database decomposition: de monolito DB a microservicios
- [ ] Replatforming vs Refactoring vs Rearchitecting: decision framework
- [ ] Java EE/Jakarta EE modernizacion: de WebLogic a Spring Boot
- [ ] COBOL/Mainframe integration: JZOS, IBM MQ, modernizacion gradual
- [ ] SOAP a REST: estrategias de migration de servicios legacy

# ═══════════════════════════════════════════════════════════════
# BLOQUE 14 — PERFORMANCE ENGINEERING (14_Performance_Engineering/) [NUEVO]
# Cultura de performance, testing y optimizacion continua
# ═══════════════════════════════════════════════════════════════

- [ ] Performance Budgets: definicion y enforcement en CI/CD
- [ ] Load Testing a escala: k6, Gatling, distributed JMeter
- [ ] Traffic Shadowing y Mirroring: validar sin riesgo en produccion
- [ ] Autoscaling predictivo: ML-based vs rule-based, pre-warming
- [ ] Database performance: query optimization, index tuning, partitioning
- [ ] JVM tuning avanzado: JIT logs, compiler directives, AOT caching

# ═══════════════════════════════════════════════════════════════
# BLOQUE 15 — VANGUARDIA 2026 (15_Vanguardia/)
# Tendencias emergentes y tecnologias experimentales
# ═══════════════════════════════════════════════════════════════

- [x] GraalVM Native Image: compilacion AOT de aplicaciones Spring Boot
- [ ] WebAssembly en el servidor con Java 21 y WasmEdge
- [ ] eBPF para observabilidad avanzada en Kubernetes 2026
- [ ] Serverless con Java 21: AWS Lambda SnapStart y Quarkus
- [ ] Project Valhalla: value types y primitive classes preview
- [ ] Project Lilliput: pointers comprimidos, menor footprint
- [ ] Project Babylon: Java como host de lenguajes y ML
- [ ] Quantum Computing: Qiskit y Java, preparacion para era post-cuantica

# ═══════════════════════════════════════════════════════════════
# ACCIONES DE CONSOLIDACION PENDIENTES
# ═══════════════════════════════════════════════════════════════

## URGENTES (antes de continuar publicando)

1. [x] Consolidar carpeta 05_SRE_DevOps_Cloud/ en 05_SRE_DevOps/
   - Mover contenido de Cloud a DevOps o renombrar a 05_SRE_DevOps_Cloud
   - Eliminar duplicados si existen

2. [x] Verificar duplicados y eliminar:
   - BigData ETL Spark (verificar si hay 2 archivos)
   - Event Sourcing y CQRS (en Arquitectura y Spring)
   - SLI/SLOs (verificar ubicacion correcta)

3. [ ] Actualizar indices README.md en cada carpeta con links reales

## IMPORTANTES (calidad del corpus)

4. [ ] Crear cross-references entre documentos relacionados
   - Ej: Virtual Threads -&gt; Structured Concurrency
   - Ej: Docker avanzado -&gt; Kubernetes auto-escalado

5. [ ] Estandarizar formato de todos los documentos:
   - Headers consistentes (Visión Estratégica, Arquitectura, Implementacion)
   - Tablas comparativas donde aplique
   - Diagramas Mermaid para arquitectura
   - Checklist SRE al final

6. [ ] Generar "Master Index" global en raiz del repositorio
   - Matriz de temas vs nivel de dificultad
   - Rutas de aprendizaje recomendadas por objetivo (Staff, Senior, Arquitecto)

# ═══════════════════════════════════════════════════════════════
# LEYENDA
# ═══════════════════════════════════════════════════════════════

# [x] Completado y publicado (verificado en repo)
# [~] En progreso / borrador activo
# [ ] Pendiente de inicio

# Prioridad visual:
# 🔴 Critico: diferenciador de carrera, visible para Staff+
# 🟡 Importante: completa el perfil, esperado en entrevistas tecnicas
# 🟢 Complementario: valor agregado, nicho especializado

# ═══════════════════════════════════════════════════════════════
# METRICAS DE EXITO DEL ROADMAP
# ═══════════════════════════════════════════════════════════════

# Objetivo 2026:
# - 60% de temas completados (nivel Senior fuerte)
# - 80% de temas completados (nivel Staff Engineer)
# - 100% de bloques con al menos 3 temas completados (perfil completo)

# Estado actual (aproximado):
# - Total temas: ~108
# - Completados: ~35 (32%)
# - En progreso: ~5
# - Pendientes: ~68

# Cobertura objetivo por area:
# - Java Core: 100% (fundamento no negociable) → Actual: ~60%
# - Arquitectura: 80% (diferenciador principal) → Actual: ~45%
# - Spring Ecosystem: 80% (framework principal) → Actual: ~40%
# - Datos: 70% (escala y persistencia) → Actual: ~55%
# - SRE/DevOps: 70% (operaciones modernas) → Actual: ~35%
# - Seguridad: 70% (compliance y riesgo) → Actual: ~30%
# - BigData/Streaming: 60% (especializacion valiosa) → Actual: ~40%
# - IA/Agentes: 60% (tendencia 2026) → Actual: ~35%
# - Fintech/HealthTech: 40% cada uno (nichos diferenciadores) → Actual: ~25%
# - Platform Engineering: 60% (tendencia ascendente) → Actual: 0%
# - Legacy Modernization: 50% (enterprise real) → Actual: 0%
# - Performance Engineering: 60% (cultura tecnica) → Actual: 0%
# - Vanguardia: 30% (visionario, no critico) → Actual: ~15%

# ═══════════════════════════════════════════════════════════════
# NOTAS DE VERSION
# ═══════════════════════════════════════════════════════════════

# v3.0 (2026-04-10)
# - Sincronizado con estado real del repositorio
# - Marcados [x] todos los temas verificados como publicados
# - Identificados duplicados y contenido faltante en roadmap anterior
# - Anadida seccion de "Acciones de Consolidacion Pendientes"
# - Recalculadas metricas de exito con estado actual real (~32% completado)
# - Numeracion de bloques ajustada para consistencia (1-15 consecutivos)

# v2.0 (2026-04-10)
# - Reorganizacion de 10 a 16 bloques especializados
# - Ampliacion de temas totales

# v1.0 (2026-04-03)
# - Estructura inicial con 10 bloques
# - 47 temas definidos