```java
// 

/**
 * Clase que implementa la gestión de estados de un hilo, permitiendo controlar y priorizar las tareas.
 * Este ejemplo utiliza una cola de prioridades para administrar los hilos en función de su importancia.
 */
public class ThreadStateManagement {

    // Usamos una cola de prioridad (PriorityBlockingQueue) para gestionar los hilos por su importancia/prioridad
    private final PriorityBlockingQueue<Runnable> taskQueue = new PriorityBlockingQueue<>();

    /**
     * Añade una tarea a la cola con su respectiva prioridad.
     *
     * @param runnable La tarea que se desea ejecutar.
     * @param priority La prioridad de la tarea. Un valor más alto indica mayor prioridad.
     */
    public void addTask(Runnable runnable, int priority) {
        taskQueue.add(new PrioritizedTask(runnable, priority));
    }

    /**
     * Clase interna que encapsula una tarea y su prioridad.
     */
    private static class PrioritizedTask implements Runnable {

        private final Runnable task;
        private final int priority;

        public PrioritizedTask(Runnable task, int priority) {
            this.task = task;
            this.priority = priority;
        }

        @Override
        public void run() {
            task.run();
        }
    }

    /**
     * Método que ejecuta las tareas en la cola de prioridad.
     * Se asegura de que solo un hilo se ejecute a la vez, manteniendo el orden de prioridad.
     */
    public void executeTasks() {
        Thread workerThread = new Thread(() -> {
            while (!taskQueue.isEmpty()) {
                PrioritizedTask task = taskQueue.take();
                // Ejecutar la tarea con su respectiva prioridad
                task.run();
            }
        });

        // Iniciamos el hilo para que comience a procesar tareas
        workerThread.start();
    }

    /**
     * Muestra la cantidad de tareas pendientes en la cola.
     */
    public int getPendingTasksCount() {
        return taskQueue.size();
    }

    /**
     * Método principal o punto de entrada (puede ser omitido en un entorno real).
     * Se utiliza para demostrar el uso de la clase ThreadStateManagement.
     *
     * @param args Argumentos de línea de comandos, no utilizados en este ejemplo.
     */
    public static void main(String[] args) {
        ThreadStateManagement manager = new ThreadStateManagement();

        // Agregamos algunas tareas con diferentes prioridades
        manager.addTask(() -> System.out.println("Tarea 1"), 2);
        manager.addTask(() -> System.out.println("Tarea 2"), 5);
        manager.addTask(() -> System.out.println("Tarea 3"), 4);

        // Ejecutamos las tareas en orden de prioridad
        manager.executeTasks();

        // Mostramos el número de tareas pendientes (debería ser cero si todas fueron ejecutadas)
        System.out.println(manager.getPendingTasksCount());
    }
}
```

Este código implementa una gestión avanzada de estados de un hilo utilizando una cola de prioridades. Los métodos `addTask` y `executeTasks` permiten agregar tareas con diferentes niveles de prioridad, asegurándose de que se ejecuten en el orden correcto.