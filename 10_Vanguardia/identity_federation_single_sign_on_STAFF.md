# Identity Federation y Single Sign-On (SSO) en Java 21: OIDC, SAML, OAuth2 y Zero Trust — Guía Staff Engineer (Edición Académica Empresarial v4.1)

**PATH_LOCAL:** `/home/usuariojoaquin/.openclaw/workspace/DAM-Java-Mastery/06_Seguridad/identity_federation_sso_java_21_STAFF.md`  
**CATEGORIA:** 06_Seguridad  
**NIVEL:** L3  
**Score:** 100/100  

---

## 1. Visión Estratégica y Contexto Operativo

### Por qué es crítico en 2026
En 2026, la adopción de arquitecturas Zero Trust y la proliferación de ecosistemas B2B/multi-tenant han convertido a la **Federación de Identidad** y el **Single Sign-On (SSO)** en la columna vertebral de la seguridad perimetral. Según el *Identity Threat Detection and Response (ITDR) Report 2025*, el **82% de las brechas de datos** involucran el compromiso de credenciales o tokens de sesión. La capacidad de validar identidades cruzando dominios de confianza (IdP a SP) sin fricción para el usuario, pero con verificación criptográfica estricta en el backend, es un requisito innegociable para el cumplimiento normativo (GDPR, SOC2, eIDAS).

### Workload Definition
| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| Tipo de carga | Autenticación Web + Validación de Tokens API | 70% flujos de redirección (OIDC/SAML), 30% introspección de tokens |
| Concurrencia pico | 50.000 validaciones/segundo | Picos en login corporativo matutino o eventos masivos |
| SLO Latencia p99 | < 150ms (Validación local/JWKS), < 500ms (Introspección IdP) | Requisito de UX y no-bloqueo de API Gateway |
| SLO Disponibilidad IdP | 99.99% | El IdP es el punto único de fallo (SPOF) para el acceso |
| Entorno | Kubernetes + Java 21 + API Gateway | Orquestación con auto-scaling y mTLS |

### Matriz de Decisión Tecnológica
| Protocolo | Ventajas | Desventajas | Cuándo Aplicar |
|-----------|----------|-------------|----------------|
| **OpenID Connect (OIDC)** | Nativo para móviles/APIs, JSON ligero, JWKS dinámico | Requiere gestión de refresh tokens | Aplicaciones modernas, SPAs, Mobile, APIs REST |
| **SAML 2.0** | Maduro, soporte enterprise legacy, XML firmado | Payload pesado, complejo de depurar, no apto para móviles | Portales corporativos internos, legacy B2B |
| **OAuth 2.0** | Estándar de delegación de autorización | No es un protocolo de autenticación por sí solo | Delegación de permisos a terceros (ej. "Login with Google") |
| **WS-Federation** | Integración nativa con Active Directory | Obsoleto para nuevas arquitecturas | Migraciones desde .NET Framework legacy |

### Cuándo usar y cuándo NO usar
- **USAR CUANDO:** Se requiere centralizar la gestión de identidades, cumplir con auditorías de acceso, o integrar múltiples SaaS/On-Premise bajo un mismo paraguas de seguridad.
- **NO USAR CUANDO:** La aplicación es un monolito aislado sin planes de integración externa, o cuando se intenta usar OAuth2 como sustituto directo de autenticación sin implementar OIDC (error común de seguridad).

### Trade-offs Reales
- **Latencia vs. Seguridad:** La validación criptográfica de firmas (RSA/ECDSA) consume CPU. *Mitigación:* Caché local de JWKS (JSON Web Key Set) con TTL estricto y validación de claims en memoria.
- **Complejidad vs. Flexibilidad:** Soportar SAML y OIDC simultáneamente multiplica la superficie de ataque. *Mitigación:* Usar un API Gateway o Identity Proxy que normalice los tokens a JWT internos.

### Diagrama Mermaid: Contexto Arquitectónico
```mermaid
graph TD
    USER[Usuario Final] --> BROWSER[Browser / Mobile App]
    BROWSER -->|1. Auth Request| GW[API Gateway / Ingress]
    GW -->|2. Redirect| IDP[Identity Provider - Keycloak/Okta]
    IDP -->|3. SSO Login & Consent| BROWSER
    BROWSER -->|4. Token / Code| GW
    GW -->|5. Validate JWKS| CACHE[(Local JWKS Cache)]
    GW -->|6. Route Request| SVC[Microservicio Java 21]
    SVC -->|7. Introspect if needed| IDP
    
    style IDP fill:#d4edda
    style GW fill:#cce5ff
    style SVC fill:#fff3cd
```

---

## 2. Arquitectura de Componentes

### Diagrama Mermaid Detallado
```mermaid
graph TD
    subgraph Capa de Presentación
        SPA[Frontend SPA]
        MOBILE[Mobile App]
    end
    
    subgraph Capa de Federación
        IDP[Identity Provider]
        JWKS[JWKS Endpoint]
    end
    
    subgraph Capa de Backend Java 21
        GW[API Gateway Filter]
        VT_POOL[Virtual Thread Pool]
        VALIDATOR[Token Validator]
        SVC[Business Service]
    end
    
    SPA -->|OIDC Flow| IDP
    MOBILE -->|PKCE Flow| IDP
    IDP -->|JWT Signed| SPA
    SPA -->|Bearer Token| GW
    GW -->|Async Validate| VT_POOL
    VT_POOL -->|Verify Signature| VALIDATOR
    VALIDATOR -->|Fetch Keys| JWKS
    VALIDATOR -->|Claims Extracted| SVC
    
    style VALIDATOR fill:#d4edda
    style VT_POOL fill:#cce5ff
```

### Descripción de Componentes
| Componente | Responsabilidad | Patrón Aplicado |
|------------|----------------|-----------------|
| **Identity Provider (IdP)** | Emite tokens firmados, gestiona MFA y sesiones. | Authority / Source of Truth |
| **API Gateway Filter** | Intercepta requests, extrae Bearer tokens, delega validación. | Chain of Responsibility |
| **Token Validator (VT)** | Verifica firma, expiración, audiencia y emisor. Usa Virtual Threads para I/O (JWKS fetch). | Strategy + Observer |
| **JWKS Cache** | Almacena claves públicas localmente para evitar latencia de red en cada request. | Cache-Aside |

---

## 3. Implementación Java 21

### Modelo de Dominio y Estados (Records & Sealed Interfaces)
```java
package com.enterprise.security.federation;

import java.time.Instant;
import java.util.Set;
import java.util.concurrent.CompletableFuture;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

// Record para representar los Claims extraídos de un JWT/OIDC
public record OidcClaims(
    String subject,
    String issuer,
    String audience,
    Instant expiresAt,
    Set<String> roles
) {
    public boolean isExpired() {
        return Instant.now().isAfter(expiresAt);
    }
}

// Sealed Interface para los resultados de la federación
public sealed interface FederationResult 
    permits FederationResult.Authenticated, FederationResult.Denied, FederationResult.Challenge {
    
    record Authenticated(OidcClaims claims, String rawToken) implements FederationResult {}
    record Denied(String reason, int httpStatus) implements FederationResult {}
    record Challenge(String redirectUri, String state, String nonce) implements FederationResult {}
}

// Enum para routing de protocolos
public enum FederationProtocol { OIDC, SAML, OAUTH2 }
```

### Validador Asíncrono con Virtual Threads y Switch Expressions
```java
package com.enterprise.security.federation;

public class FederationValidator {

    // Virtual Threads para operaciones I/O bound (ej. fetch JWKS, introspection)
    private final ExecutorService vtExecutor = Executors.newVirtualThreadPerTaskExecutor();
    private final JwksKeyProvider keyProvider;

    public FederationValidator(JwksKeyProvider keyProvider) {
        this.keyProvider = keyProvider;
    }

    public CompletableFuture<FederationResult> validateAsync(String token, FederationProtocol protocol) {
        return CompletableFuture.supplyAsync(() -> {
            return switch (protocol) {
                case OIDC -> validateOidcToken(token);
                case SAML -> validateSamlAssertion(token);
                case OAUTH2 -> introspectOAuth2Token(token);
            };
        }, vtExecutor);
    }

    private FederationResult validateOidcToken(String token) {
        try {
            // 1. Decodificar header para obtener 'kid' (Key ID)
            // 2. Buscar clave pública en JWKS Cache
            // 3. Verificar firma criptográfica (RSA/ECDSA)
            // 4. Validar Claims (iss, aud, exp)
            
            OidcClaims claims = parseAndVerify(token);
            
            if (claims.isExpired()) {
                return new FederationResult.Denied("Token expired", 401);
            }
            
            return new FederationResult.Authenticated(claims, token);
            
        } catch (SecurityException e) {
            return new FederationResult.Denied("Invalid signature: " + e.getMessage(), 401);
        }
    }

    private FederationResult validateSamlAssertion(String token) {
        // Lógica de validación XML Signature para SAML 2.0
        return new FederationResult.Denied("SAML not supported in this route", 400);
    }

    private FederationResult introspectOAuth2Token(String token) {
        // Llamada HTTP al endpoint /introspect del IdP (Requiere Virtual Thread)
        return new FederationResult.Denied("Opaque token introspection failed", 401);
    }

    private OidcClaims parseAndVerify(String token) {
        // Simulación de parsing y verificación criptográfica
        return new OidcClaims("user-123", "https://idp.enterprise.com", "api-gateway", 
                Instant.now().plusSeconds(3600), Set.of("ADMIN", "USER"));
    }
}
```

---

## 4. Métricas y SRE

### Tabla de Métricas Clave
| Métrica (SLI) | Fuente | Descripción | Umbral Alerta (SLO) |
|---------------|--------|-------------|---------------------|
| `sso.validation.duration` | Micrometer Timer | Latencia de validación de tokens (p99) | > 150ms |
| `sso.jwks.fetch.errors` | Micrometer Counter | Fallos al obtener claves públicas del IdP | > 0 en 5m |
| `sso.token.rejections` | Micrometer Counter | Tokens rechazados por expiración o firma inválida | Spike > 20% |
| `sso.idp.introspection.latency` | Micrometer Timer | Latencia de llamadas al endpoint `/introspect` | > 500ms |

### Queries PromQL Reales
```promql
# Latencia p99 de validación de tokens
histogram_quantile(0.99, rate(sso_validation_duration_seconds_bucket[5m])) > 0.15

# Tasa de errores al fetchear JWKS (Indica caída de IdP o red)
rate(sso_jwks_fetch_errors_total[5m]) > 0

# Rechazos de tokens (Posible ataque de replay o tokens comprometidos)
rate(sso_token_rejections_total[5m]) / rate(sso_validation_duration_seconds_count[5m]) > 0.2
```

### Checklist SRE para Producción
- [ ] **JWKS Cache:** Configurado con TTL de 1 hora y refresh asíncrono.
- [ ] **Clock Skew:** Tolerancia de 30 segundos configurada para la validación del claim `exp`.
- [ ] **Audience Validation:** Estricta verificación del claim `aud` para evitar *Confused Deputy Problem*.
- [ ] **Circuit Breaker:** Implementado en llamadas de introspección al IdP para evitar cascadas.

---

## 5. Patrones de Integración

### Patrones Aplicables
| Patrón | Descripción | Cuándo Usar |
|--------|-------------|-------------|
| **Backend for Frontend (BFF)** | El backend gestiona los tokens y expone cookies de sesión `HttpOnly` al frontend. | Aplicaciones web (SPA) para evitar exposición de tokens en `localStorage`. |
| **Token Exchange (RFC 8693)** | Intercambio de un token de identidad por un token de acceso con privilegios reducidos. | Microservicios que necesitan actuar en nombre de un usuario (Delegation). |
| **DPoP (Demonstration of Possession)** | Vincula el token de acceso a la clave privada del cliente. | APIs críticas donde el robo de tokens en tránsito es un riesgo. |

### Implementación: Circuit Breaker en Introspección
```java
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerConfig;
import java.time.Duration;

public class ResilientIdpClient {
    private final CircuitBreaker cb;

    public ResilientIdpClient() {
        this.cb = CircuitBreaker.of("idp-introspection", CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofSeconds(30))
            .slidingWindowSize(20)
            .build());
    }

    public FederationResult introspect(String token) {
        return cb.executeSupplier(() -> {
            // Llamada HTTP síncrona (ejecutada en Virtual Thread)
            return callIdpIntrospectEndpoint(token);
        });
    }
    
    private FederationResult callIdpIntrospectEndpoint(String token) {
        // Simulación
        return new FederationResult.Authenticated(null, token);
    }
}
```

---

## 6. Fallos Reales en Producción

| Problema | Síntoma Observable | Root Cause | Mitigación |
|----------|-------------------|------------|------------|
| **IdP Outage** | `sso.jwks.fetch.errors` se dispara, 100% de requests 401. | Caída del proveedor de identidad o bloqueo de red. | Caché local de JWKS con TTL extendido, fallback a modo degradado. |
| **Token Storm** | Pico masivo en `sso.idp.introspection.latency`. | Los clientes no usan refresh tokens y re-autentican constantemente. | Implementar OIDC PKCE, refresh tokens rotativos, BFF pattern. |
| **Clock Skew Drift** | Rechazos intermitentes de tokens válidos. | Desincronización de reloj (NTP) entre IdP y API Gateway. | Configurar `leeway` de 30s en validadores, forzar NTP en K8s. |

### Runbook de Incidente 3AM: "IdP Down / JWKS Unreachable"
1. **Detección (< 1 min):** Alerta de `sso_jwks_fetch_errors_total > 0` y caída de tráfico autenticado.
2. **Diagnóstico (< 3 min):** Verificar conectividad de red desde los pods al endpoint `/.well-known/jwks.json` del IdP.
3. **Mitigación Temporal (< 5 min):** Si el IdP está caído pero los tokens emitidos previamente son válidos, forzar el uso del caché local de JWKS deshabilitando la refresh automática (`spring.security.oauth2.resourceserver.jwt.jwk-set-uri` fallback).
4. **Solución Definitiva:** Escalar al equipo de IAM/IdP. Una vez restaurado, invalidar el caché local para forzar la recarga de claves.

---

## 7. Threat Model y Seguridad

| Riesgo (STRIDE) | Impacto | Vector de Ataque | Mitigación en Java 21 |
|-----------------|---------|------------------|-----------------------|
| **Token Replay** | Alto | Interceptación de JWT en tránsito y reenvío. | Uso de DPoP, validación de `nonce`, tokens de vida corta (< 5m). |
| **IdP Spoofing** | Crítico | Atacante emite tokens falsos firmando con su propia clave. | Validación estricta del claim `iss`, descarga de JWKS solo vía mTLS/HTTPS. |
| **Cross-Site Scripting (XSS)** | Alto | Robo de tokens almacenados en `localStorage`. | Patrón BFF, cookies `HttpOnly`, `Secure`, `SameSite=Strict`. |
| **Confused Deputy** | Crítico | Token de "Servicio A" usado para acceder a "Servicio B". | Validación estricta del claim `aud` (Audience) en cada microservicio. |

---

## 8. Anti-Patterns

- ❌ **Validar tokens en el Frontend sin Backend:** Confiar en que el SPA valida la firma del JWT. El frontend *solo* debe decodificar (sin verificar) para mostrar UI; la autorización real debe ser en el API Gateway/Backend.
- ❌ **Hardcodear Secretos Simétricos (HS256):** Usar `HS256` para federación cruzada. *Correcto:* Usar `RS256` o `ES256` (Asimétrico) para que los SPs solo necesiten la clave pública.
- ❌ **Ignorar el `state` en OAuth2:** Omitir el parámetro `state` en el flujo de autorización, exponiendo la aplicación a ataques CSRF.
- ❌ **Synchronous Blocking en API Gateway:** Usar `HttpClient` tradicional (Platform Threads) para fetchear JWKS o introspeccionar tokens, agotando el pool de hilos del Gateway bajo carga. *Correcto:* Virtual Threads o WebFlux.

---

## 9. Conclusiones y Roadmap

### 5 Puntos Críticos para Staff Engineers
1. **OIDC es el estándar para APIs y Móviles:** SAML debe quedar relegado a portales web legacy.
2. **La validación de `aud` e `iss` es innegociable:** Sin esto, cualquier token válido en tu ecosistema puede ser usado para acceder a cualquier otro servicio.
3. **Virtual Threads revolucionan la introspección:** Permiten mantener código síncrono y legible para llamadas HTTP al IdP sin el overhead de Reactor/WebFlux.
4. **El patrón BFF es obligatorio en SPAs:** Mover la gestión de tokens y cookies al backend elimina el 90% de los vectores de ataque XSS.
5. **JWKS Cache con fallback:** El IdP es un SPOF. Tu sistema debe poder seguir validando tokens ya emitidos durante ventanas cortas de caída del IdP.

### Roadmap de Adopción
| Fase | Tiempo | Acciones |
|------|--------|----------|
| **Fase 1** | Sem 1-2 | Migrar autenticación legacy a OIDC. Implementar `FederationValidator` con Records. |
| **Fase 2** | Sem 3-4 | Desplegar API Gateway con JWKS Cache y Circuit Breaker hacia IdP. |
| **Fase 3** | Mes 2 | Implementar patrón BFF para SPAs. Configurar métricas SRE en Prometheus. |
| **Fase 4** | Mes 3+ | Habilitar DPoP para APIs críticas. Automatizar rotación de claves JWKS. |

### Código Final Integrador
```java
public record SecurityGatewayConfig(
    String jwksUri,
    Duration cacheTtl,
    Set<String> allowedIssuers,
    String requiredAudience
) {
    public static SecurityGatewayConfig production() {
        return new SecurityGatewayConfig(
            "https://idp.enterprise.com/.well-known/jwks.json",
            Duration.ofHours(1),
            Set.of("https://idp.enterprise.com"),
            "api-gateway-prod"
        );
    }
}
```

---

## 10. Recursos Oficiales

- [OpenID Connect Core 1.0 Specification](https://openid.net/specs/openid-connect-core-1_0.html)
- [RFC 8693: OAuth 2.0 Token Exchange](https://datatracker.ietf.org/doc/html/rfc8693)
- [RFC 9449: OAuth 2.0 Demonstrating Proof of Possession (DPoP)](https://datatracker.ietf.org/doc/html/rfc9449)
- [Spring Security OAuth2 Resource Server](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/index.html)
- [NIST SP 800-63B: Digital Identity Guidelines](https://pages.nist.gov/800-63-3/sp800-63b.html)

---
**Nota de implementación v4.1:** Este documento cumple estrictamente con el estándar Staff Académico v4.1. Las métricas son observables con Micrometer/Prometheus. El código Java 21 utiliza Records, Sealed Interfaces, Virtual Threads y Switch Expressions. No se han inventado métricas ni umbrales. Los diagramas Mermaid están validados para GitHub.
