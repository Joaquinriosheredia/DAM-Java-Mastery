```java
// 

/**
 * Clase que implementa la sincronización de hilos usando semáforos y exclusión mutua.
 */
public class ThreadSynchronization {

    private final Semaphore semaphore;
    private final Object lock;

    /**
     * Constructor que inicializa el semáforo con un número específico de permisos
     * y crea un bloqueador para la exclusión mutua.
     *
     * @param permits el número de permisos iniciales del semáforo.
     */
    public ThreadSynchronization(int permits) {
        this.semaphore = new Semaphore(permits);
        this.lock = new Object();
    }

    /**
     * Método que simula una operación que necesita sincronización y exclusión mutua.
     *
     * @param threadName el nombre del hilo actual para identificación en la salida.
     */
    public void synchronizedOperation(String threadName) {
        // Adquirir un permiso del semáforo
        try {
            semaphore.acquire();
            System.out.println(threadName + " ha adquirido un permiso. Iniciando operación.");

            // Simulación de una operación crítica
            simulateCriticalOperation();

            System.out.println(threadName + " ha completado la operación.");
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
            throw new RuntimeException("Hilo interrumpido", e);
        } finally {
            // Liberar el permiso del semáforo
            semaphore.release();
            System.out.println(threadName + " ha liberado un permiso.");
        }
    }

    /**
     * Método que simula una operación crítica que debe ser segura.
     */
    private void simulateCriticalOperation() {
        synchronized (lock) { // Exclusión mutua mediante bloqueo
            try {
                Thread.sleep(1000); // Simulación de tiempo de procesamiento
                System.out.println(threadName + " está ejecutando la operación crítica.");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                throw new RuntimeException("Operación interrumpida", e);
            }
        }
    }

    /**
     * Método principal para demostrar el uso de la sincronización.
     *
     * @param args argumentos pasados al programa.
     */
    public static void main(String[] args) {
        ThreadSynchronization synchronization = new ThreadSynchronization(1);

        // Crear hilos
        Thread thread1 = new Thread(() -> synchronization.synchronizedOperation("Thread-1"));
        Thread thread2 = new Thread(() -> synchronization.synchronizedOperation("Thread-2"));

        // Iniciar hilos
        thread1.start();
        thread2.start();
    }
}
```

Este código implementa una solución para sincronizar la ejecución de múltiples hilos utilizando semáforos y exclusión mutua en Java. El `Semaphore` se utiliza para controlar el acceso simultáneo a un recurso, mientras que el bloqueo (`synchronized`) asegura que solo un hilo pueda acceder a una parte crítica del código a la vez.