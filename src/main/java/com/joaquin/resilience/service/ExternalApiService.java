package com.joaquin.resilience.service;

import org.springframework.stereotype.Service;
import java.util.Random;

@Service
public class ExternalApiService {

    /**
     * Simula una llamada a una API inestable (como la de Abacus hoy).
     * Si el sistema falla, el Circuit Breaker entrará en acción.
     */
    public String callExternalApi() {
        if (new Random().nextInt(10) < 7) { // 70% de probabilidad de fallo
            throw new RuntimeException("Error de conexión: Timeout en el servidor remoto");
        }
        return "Datos obtenidos con éxito del enjambre.";
    }
}
