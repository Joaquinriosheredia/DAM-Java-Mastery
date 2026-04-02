Spring Boot 3.4 y R2DBC con Virtual Threads
PATH_LOCAL: /home/usuariojoaquin/.openclaw/workspace/DAM-Java-Mastery/_Review/Spring_Boot_3.4_y_R2DBC_con_Virtual_Threads/report.md
CATEGORIA: 03_Spring_Ecosystem
Score: 95

Visión Estratégica
Spring Boot 3.4 consolida dos paradigmas de concurrencia que hasta ahora eran incompatibles en la práctica: el modelo reactivo de R2DBC/WebFlux y el modelo imperativo con Virtual Threads. Entender cuándo usar cada uno, y cómo combinarlos correctamente, es una decisión arquitectónica de nivel Staff.
El problema que resuelven juntos:
El modelo bloqueante tradicional (JDBC + Tomcat) escala mal bajo alta concurrencia porque cada hilo del OS cuesta 1-2 MB y el número de conexiones simultáneas está limitado por el pool de threads. R2DBC resuelve esto con backpressure reactivo. Virtual Threads lo resuelve con threads ligeros gestionados por la JVM. Son dos soluciones al mismo problema con trade-offs distintos.
CriterioJDBC + Virtual ThreadsR2DBC + WebFluxModelo de códigoImperativo, legibleReactivo, complejoLatencia bajo cargaMuy bajaMuy bajaCompatibilidad libreríasAltaLimitadaCurva de aprendizajeBajaAltaDebuggingSencilloComplejo
Regla práctica para equipos: Si el equipo domina programación reactiva y la aplicación es I/O-bound con miles de conexiones simultáneas, R2DBC + WebFlux. Si el equipo viene de Spring MVC clásico y quiere escalabilidad sin reescribir, JDBC + Virtual Threads es la migración menos dolorosa de Java 21.
Spring Boot 3.4 soporta ambos y permite combinarlos en la misma aplicación, lo que es el escenario más realista en migraciones incrementales.
mermaidgraph TD
    A[Cliente HTTP] --> B[Spring Boot 3.4]
    B --> C{Tipo de endpoint}
    C -->|Reactivo| D[WebFlux + R2DBC]
    C -->|Imperativo| E[Spring MVC + Virtual Threads]
    D --> F[R2DBC Connection Pool]
    E --> G[JDBC Connection Pool]
    F --> H[(PostgreSQL)]
    G --> H
    D --> I[Micrometer + Prometheus]
    E --> I

Arquitectura de Componentes
La arquitectura de una aplicación Spring Boot 3.4 con R2DBC se organiza en tres capas bien definidas. La clave está en no mezclar código bloqueante dentro del pipeline reactivo.
mermaidgraph TD
    subgraph Web Layer
        A[RouterFunction / WebFlux] --> B[Handler]
    end
    subgraph Service Layer
        B --> C[ReactiveCrudRepository]
        B --> D[R2dbcEntityTemplate]
    end
    subgraph Infrastructure
        C --> E[ConnectionPool R2DBC]
        D --> E
        E --> F[(PostgreSQL / MySQL)]
    end
    subgraph Observabilidad
        E --> G[R2DBC Pool Metrics]
        G --> H[Micrometer → Prometheus]
    end
Configuración de conexión R2DBC con pool en application.yml:
yamlspring:
  r2dbc:
    url: r2dbc:postgresql://localhost:5432/mibasedatos
    username: usuario
    password: secreto
    pool:
      initial-size: 5
      max-size: 20
      max-idle-time: 30m
      validation-query: SELECT 1
  threads:
    virtual:
      enabled: true  # Activa Virtual Threads en Spring MVC/Tomcat
Entidad y repositorio reactivo:
javaimport org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Table("pedidos")
public record Pedido(
    @Id Long id,
    String clienteId,
    String estado,
    java.math.BigDecimal total
) {}

public interface PedidoRepository extends ReactiveCrudRepository<Pedido, Long> {

    Flux<Pedido> findByClienteId(String clienteId);

    Flux<Pedido> findByEstado(String estado);

    Mono<Long> countByEstado(String estado);
}

Implementación Java 21
Implementación completa de un servicio reactivo con R2DBC, transacciones y manejo correcto de errores:
javaimport org.springframework.r2dbc.core.DatabaseClient;
import org.springframework.stereotype.Service;
import org.springframework.transaction.reactive.TransactionalOperator;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@Service
public class PedidoService {

    private final PedidoRepository repository;
    private final DatabaseClient databaseClient;
    private final TransactionalOperator txOperator;

    public PedidoService(
            PedidoRepository repository,
            DatabaseClient databaseClient,
            TransactionalOperator txOperator) {
        this.repository = repository;
        this.databaseClient = databaseClient;
        this.txOperator = txOperator;
    }

    // Consulta simple reactiva
    public Flux<Pedido> obtenerPedidosPorCliente(String clienteId) {
        return repository.findByClienteId(clienteId)
            .doOnError(e -> log.error("Error obteniendo pedidos: {}", e.getMessage()));
    }

    // Inserción con transacción reactiva
    public Mono<Pedido> crearPedido(Pedido pedido) {
        return repository.save(pedido)
            .as(txOperator::transactional)
            .doOnSuccess(p -> log.info("Pedido creado: {}", p.id()));
    }

    // Consulta con DatabaseClient para SQL custom
    public Flux<Pedido> pedidosPendientesMayorDe(java.math.BigDecimal importe) {
        return databaseClient.sql("""
                SELECT id, cliente_id, estado, total
                FROM pedidos
                WHERE estado = 'PENDIENTE'
                AND total > :importe
                ORDER BY total DESC
                """)
            .bind("importe", importe)
            .mapProperties(Pedido.class)
            .all();
    }
}
Controlador WebFlux que expone los endpoints reactivos:
javaimport org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/api/pedidos")
public class PedidoController {

    private final PedidoService service;

    public PedidoController(PedidoService service) {
        this.service = service;
    }

    @GetMapping(value = "/cliente/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public Flux<Pedido> porCliente(@PathVariable String id) {
        return service.obtenerPedidosPorCliente(id);
    }

    @PostMapping
    public Mono<Pedido> crear(@RequestBody Pedido pedido) {
        return service.crearPedido(pedido);
    }

    // Server-Sent Events para streaming reactivo real
    @GetMapping(value = "/stream/pendientes",
                produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<Pedido> streamPendientes() {
        return service.pedidosPendientesMayorDe(java.math.BigDecimal.ZERO);
    }
}

Métricas y SRE
R2DBC expone métricas del pool de conexiones automáticamente via Micrometer cuando Spring Boot Actuator está en el classpath. Las métricas más importantes para monitorizar:
mermaidgraph TD
    A[R2DBC Connection Pool] --> B[r2dbc.pool.acquired]
    A --> C[r2dbc.pool.pending]
    A --> D[r2dbc.pool.idle]
    A --> E[r2dbc.pool.max.allocated]
    B --> F[Prometheus]
    C --> F
    D --> F
    E --> F
    F --> G[Grafana Dashboard]
    G --> H{Alertas}
    H -->|pending alto| I[Escalar pool o BD]
    H -->|acquired = max| J[Cuello de botella detectado]
Queries Prometheus para monitorizar el pool R2DBC:
promql# Conexiones pendientes (esperando conexión disponible)
r2dbc_pool_pending{name="connectionPool"}

# Ratio de utilización del pool
r2dbc_pool_acquired / r2dbc_pool_max_allocated

# Tiempo medio de adquisición de conexión (p95)
histogram_quantile(0.95,
  rate(r2dbc_pool_acquire_duration_seconds_bucket[5m])
)
Configuración de Actuator para exponer métricas R2DBC:
yamlmanagement:
  endpoints:
    web:
      exposure:
        include: health,metrics,prometheus,startup
  metrics:
    export:
      prometheus:
        enabled: true
  endpoint:
    health:
      show-details: always
Checklist SRE para R2DBC en producción:

max-size del pool debe ser ≤ max_connections configurado en PostgreSQL por instancia de aplicación
Configurar validation-query: SELECT 1 para detectar conexiones muertas antes de usarlas
Activar spring.r2dbc.pool.max-idle-time para liberar conexiones inactivas y no agotar conexiones en la BD
Alertar cuando r2dbc_pool_pending > 0 durante más de 5 segundos sostenidos
En Virtual Threads + Spring MVC, monitorizar jvm_threads_live_threads — no debe crecer indefinidamente


Conclusiones
Spring Boot 3.4 con R2DBC representa la opción más madura para aplicaciones Java con alta concurrencia de I/O en 2026. Los tres puntos críticos que un Staff Engineer debe dominar son: el modelo de backpressure reactivo (nunca bloquear dentro de un pipeline Flux/Mono), la configuración correcta del pool de conexiones R2DBC (el tamaño del pool es el parámetro más importante para el rendimiento), y la observabilidad del pool via Micrometer.
La combinación con Virtual Threads no es un reemplazo de R2DBC sino complementaria: Virtual Threads activos en spring.threads.virtual.enabled=true benefician a los componentes bloqueantes que aún existan en la aplicación (schedulers, listeners síncronos), mientras R2DBC maneja el acceso a datos de forma reactiva.
El error más común en producción es configurar max-size del pool R2DBC mayor que max_connections de PostgreSQL dividido entre el número de instancias de la aplicación. Esto provoca errores de conexión bajo carga que son difíciles de diagnosticar sin las métricas correctas de Micrometer.
