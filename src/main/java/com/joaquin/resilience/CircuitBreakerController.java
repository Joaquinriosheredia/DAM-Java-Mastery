package com.joaquin.resilience;

import io.github.resilience4j.circuitbreaker.annotation.CircuitBreaker;
import io.github.resilience4j.retry.annotation.Retry;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.time.Instant;

/**
 * ARQUITECTURA DE ALTA DISPONIBILIDAD - JOAQUÍN RÍOS HEREDIA
 * Implementación de patrones de resiliencia para sistemas distribuidos.
 */
@RestController
@RequestMapping("/resilience")
public class CircuitBreakerController {

    private static final Logger log = LoggerFactory.getLogger(CircuitBreakerController.class);
    private static final String EXTERNAL_SERVICE = "abacus-external-service";

    @GetMapping("/external-call")
    @CircuitBreaker(name = EXTERNAL_SERVICE, fallbackMethod = "fallbackExternalCall")
    @Retry(name = EXTERNAL_SERVICE)
    public String callExternalService() {
        log.info("Iniciando solicitud al clúster remoto de Abacus...");
        
        // Simulación de la interrupción de infraestructura actual
        throw new RuntimeException("Remote Instance cluster-proxy-pa-002 Timeout");
    }

    /**
     * MÉTODO DE CONTINGENCIA (FALLBACK)
     * Se ejecuta automáticamente cuando el Circuit Breaker detecta el fallo persistente.
     */
    public String fallbackExternalCall(Exception ex) {
        log.warn("Capa de resiliencia activada. Redirigiendo tráfico a nodos locales.");
        
        return """
               {
                 "status": "DEGRADED_MODE",
                 "engineer": "Joaquín Ríos Heredia",
                 "incident_report": "%s",
                 "mitigation_strategy": "Circuit Breaker + Exponential Retry",
                 "timestamp": "%s"
               }
               """.formatted(ex.getMessage(), Instant.now());
    }
}
