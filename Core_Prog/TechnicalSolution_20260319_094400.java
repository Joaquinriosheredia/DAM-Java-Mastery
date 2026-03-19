```java
package es.joaquin.portfolio.service;

import es.joaquin.portfolio.exception.BusinessException;
import es.joaquin.portfolio.exception.DataIntegrityViolationException;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

/**
 * Clase ServiceExample que demuestra la gestión de excepciones personalizadas.
 */
public class ServiceExample {

    /**
     * Método que simula una operación de negocio y puede generar diferentes tipos
     * de excepciones personalizadas en distintas capas del sistema.
     *
     * @param id el identificador a procesar
     * @return un mensaje indicando si la operación fue exitosa o no.
     * @throws DataIntegrityViolationException si se viola una integridad de datos.
     * @throws BusinessException si ocurre una excepción relacionada con el negocio.
     */
    public String processOperation(int id) throws DataIntegrityViolationException, BusinessException {
        // Simulación de lógica de negocio
        if (id < 1) {
            throw new DataIntegrityViolationException("ID inválido. Debe ser mayor que cero.");
        }

        try {
            // Lógica compleja o llamada a otro servicio
            int result = complexBusinessLogic(id);
            
            if (result == -1) {
                throw new BusinessException("Ocurrió un error en la operación de negocio.", HttpStatus.INTERNAL_SERVER_ERROR);
            }
            
            return "Operación exitosa. ID: " + id;
        } catch (Exception e) {
            // Manejo genérico de excepciones
            throw new BusinessException("Error inesperado durante la operación.", HttpStatus.BAD_REQUEST, e);
        }
    }

    /**
     * Simulación de lógica compleja del negocio que puede fallar.
     *
     * @param id el identificador a procesar
     * @return -1 si ocurre un error o un valor válido.
     */
    private int complexBusinessLogic(int id) {
        // Lógica que simula una operación de negocio
        if (id > 5) {
            return -1;
        }
        return id + 10;
    }

}
```