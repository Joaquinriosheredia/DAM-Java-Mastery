package com.joaquin.resilience.controller;

import com.joaquin.resilience.service.ExternalApiService;
import io.github.resilience4j.circuitbreaker.annotation.CircuitBreaker;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class ResilienceController {

    @Autowired
    private ExternalApiService apiService;

    /**
     * Endpoint protegido por Circuit Breaker.
     * Si el servicio falla repetidamente, se activa el 'fallbackMethod'.
     */
    @GetMapping("/api/check-connection")
    @CircuitBreaker(name = "backendAPI", fallbackMethod = "fallbackForApi")
    public String checkApi() {
        return apiService.callExternalApi();
    }

    /**
     * Respuesta de emergencia (Fallback). 
     * Esto es lo que evita que el usuario vea un error 404 o 500.
     */
    public String fallbackForApi(Exception e) {
        return "SISTEMA RESILIENTE: La API externa no responde, " +
               "activando modo de contingencia local. Motivo: " + e.getMessage();
    }
}
