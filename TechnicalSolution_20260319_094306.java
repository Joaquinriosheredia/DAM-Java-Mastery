```java
package es.joaquin.portfolio;

import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * Clase Singleton para la gestión de logs.
 *
 * @author Joaquín
 */
public final class LogGestor {

    private static final Logger LOGGER = Logger.getLogger(LogGestor.class.getName());
    private static volatile LogGestor instance;
    private static final Object MONITOR = new Object();

    /**
     * Constructor privado para evitar la instancia directa de la clase.
     */
    private LogGestor() {
        // Constructor vacío
    }

    /**
     * Método estático para obtener la única instancia de LogGestor.
     *
     * @return La instancia única de LogGestor
     */
    public static LogGestor getInstance() {
        if (instance == null) {
            synchronized (MONITOR) {
                if (instance == null) {
                    instance = new LogGestor();
                }
            }
        }
        return instance;
    }

    /**
     * Método para registrar un mensaje de log.
     *
     * @param message El mensaje a registrar
     */
    public void registerLog(String message) {
        try (FileWriter writer = new FileWriter("logs/log.txt", true)) {
            writer.write(LocalDateTime.now() + " - " + message + "\n");
            LOGGER.log(Level.INFO, message);
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "Error al registrar el log: {0}", e.getMessage());
        }
    }
}
```