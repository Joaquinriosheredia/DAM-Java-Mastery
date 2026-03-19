```java
/**
 * Filename: HiloRunnable.java
 */

package com.example.hilos;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

/**
 * Esta clase implementa la interfaz Runnable para crear un hilo que puede ser ejecutado en el sistema.
 * Permite gestionar estados y realizar tareas asincrónicas de manera efectiva utilizando hilos.
 */
public class HiloRunnable implements Runnable {

    private String nombreHilo;
    private boolean estaActivo;

    /**
     * Constructor que inicializa la tarea del hilo y su estado.
     *
     * @param nombreHilo el nombre identificador para este hilo
     * @param estaActivo indica si el hilo debe ejecutarse inmediatamente (true) o no (false)
     */
    public HiloRunnable(String nombreHilo, boolean estaActivo) {
        this.nombreHilo = nombreHilo;
        this.estaActivo = estaActivo;
    }

    /**
     * Este método es la implementación del Runnable y contiene el código a ejecutar en el hilo.
     *
     * @see java.lang.Runnable#run()
     */
    @Override
    public void run() {
        if (estaActivo) {
            System.out.println("Iniciando hilo: " + nombreHilo);
            try {
                // Simulación de una tarea con delay
                Thread.sleep(2000);
                System.out.println("Hilo " + nombreHilo + " ha finalizado su ejecución.");
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.err.println("El hilo " + nombreHilo + " fue interrumpido.");
            }
        }
    }

    /**
     * Método para iniciar la tarea del hilo de manera asíncrona.
     */
    public void ejecutarHilo() {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        executor.execute(this);
        executor.shutdown(); // Esperar a que el hilo termine antes de continuar
    }

    /**
     * Getter para la propiedad estaActivo.
     *
     * @return boolean true si el hilo debe ejecutarse, false en caso contrario.
     */
    public boolean isEstaActivo() {
        return estaActivo;
    }

    /**
     * Setter para la propiedad estaActivo.
     *
     * @param estaActivo el nuevo estado del hilo.
     */
    public void setEstaActivo(boolean estaActivo) {
        this.estaActivo = estaActivo;
    }
}
```

Este código implementa una clase `HiloRunnable` que ejecuta tareas de manera asincrónica utilizando hilos en Java, siguiendo los estándares y mejores prácticas recomendadas para la implementación de hilos con la interfaz Runnable.