```java
package es.joaquin.portfolio;

/**
 * Clase Singleton para la gestión de logs.
 *
 * @author Joaquín
 */
public class LoggerManager {

    /**
     * Instancia única del LoggerManager.
     */
    private static LoggerManager instance;

    /**
     * Objeto锁对象，用于线程同步。
     */
    private final Object lock = new Object();

    /**
     * Nombre del archivo log.
     */
    private String logFileName;

    /**
     * Constructor privado para prevenir la instanciación directa desde fuera de esta clase.
     */
    private LoggerManager() {
        // Inicialización de logFileName con un nombre predeterminado
        this.logFileName = "app.log";
    }

    /**
     * Método estático que proporciona acceso a la instancia única de LoggerManager.
     *
     * @return La única instancia de LoggerManager.
     */
    public static LoggerManager getInstance() {
        if (instance == null) {
            synchronized (lock) {
                if (instance == null) {
                    instance = new LoggerManager();
                }
            }
        }
        return instance;
    }

    /**
     * Configura el nombre del archivo de log.
     *
     * @param fileName El nuevo nombre del archivo de log.
     */
    public void setLogFileName(String fileName) {
        this.logFileName = fileName;
    }

    /**
     * Método ficticio para escribir un mensaje en el archivo de log.
     *
     * @param message El mensaje a registrar en el archivo de log.
     */
    public void logMessage(String message) {
        // Implementación ficticia para simular la escritura en el archivo
        System.out.println("Logging to " + logFileName + ": " + message);
    }
}
```