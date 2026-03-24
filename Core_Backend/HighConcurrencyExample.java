package com.example.virtualthreads;

import java.lang.foreign.*;
import java.nio.ByteBuffer;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

public class HighConcurrencyExample {

    // Ejemplo de un servicio que se ejecutará en los threads virtuales.
    private static final String URL = "http://example.com/api";

    public static void main(String[] args) {
        int numThreads = 1000; // Número de hilos a crear
        ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor();
        
        for (int i = 0; i < numThreads; i++) {
            final String taskURL = URL + "?param=" + i;
            
            executor.submit(() -> {
                System.out.println("Executing request to " + taskURL);
                
                // Aquí iría la lógica para hacer una solicitud HTTP.
                // Como ejemplo, simplemente imprimimos el mensaje de inicio
                try {
                    Thread.sleep(100);  // Simula un trabajo que tarda 100 ms
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
                
                System.out.println("Request completed for " + taskURL);
            });
        }

        executor.shutdown();
        
        try {
            if (!executor.awaitTermination(5, TimeUnit.MINUTES)) {
                System.err.println("Timed out waiting for tasks to complete");
                executor.shutdownNow();
            }
        } catch (InterruptedException e) {
            executor.shutdownNow();
            Thread.currentThread().interrupt();
        }
    }
}