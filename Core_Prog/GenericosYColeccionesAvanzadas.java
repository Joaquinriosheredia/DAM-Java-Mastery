```java
/**
 * Clase principal que implementa el uso de genéricos y colecciones avanzadas en Java.
 */
public class GenericosYColeccionesAvanzadas {

    /**
     * Muestra un ejemplo de cómo utilizar Listas Genéricas en Java.
     * 
     * @param genericList Lista genérica donde se almacenarán elementos.
     */
    public static <T> void mostrarGenerico(List<T> genericList) {
        for (T item : genericList) {
            System.out.println(item);
        }
    }

    /**
     * Muestra un ejemplo de cómo utilizar Mapas Genéricos en Java.
     * 
     * @param genericMap Mapa genérico donde se almacenarán pares clave-valor.
     */
    public static <K, V> void mostrarGenericoMap(Map<K, V> genericMap) {
        for (Map.Entry<K, V> entry : genericMap.entrySet()) {
            System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
        }
    }

    /**
     * Muestra un ejemplo de cómo utilizar Colecciones Avanzadas como HashSet y TreeSet.
     */
    public static void mostrarColeccionesAvanzadas() {
        // Uso de HashSet (colección sin duplicados no ordenada)
        Set<String> hashSet = new HashSet<>();
        hashSet.add("Apple");
        hashSet.add("Banana");
        hashSet.add("Cherry");
        hashSet.add("Date");

        System.out.println("HashSet: " + hashSet);

        // Uso de TreeSet (colección ordenada basada en la implementación natural o Comparator)
        Set<String> treeSet = new TreeSet<>();
        treeSet.add("Grape");
        treeSet.add("Honeydew");
        treeSet.add("Ivy");

        System.out.println("TreeSet: " + treeSet);
    }

    /**
     * Muestra un ejemplo de cómo utilizar Colecciones Avanzadas como PriorityQueue.
     */
    public static void mostrarPriorityQueue() {
        // Uso de PriorityQueue (cola de prioridad)
        Queue<String> priorityQueue = new PriorityQueue<>();
        priorityQueue.add("First");
        priorityQueue.add("Second");
        priorityQueue.add("Third");

        System.out.println("PriorityQueue: " + priorityQueue);

        // Recuperación ordenada basada en la prioridad
        while (!priorityQueue.isEmpty()) {
            System.out.println(priorityQueue.poll());
        }
    }

    /**
     * Muestra un ejemplo de cómo utilizar Colecciones Avanzadas como LinkedList.
     */
    public static void mostrarLinkedList() {
        // Uso de LinkedList (lista enlazada)
        List<String> linkedList = new LinkedList<>();
        linkedList.add("Last");
        linkedList.add("Middle");
        linkedList.add("First");

        System.out.println("LinkedList: " + linkedList);

        // Modificación y acceso
        linkedList.remove("Middle");
        linkedList.add(1, "NewMiddle");

        System.out.println("Modificado LinkedList: " + linkedList);
    }

    /**
     * Método principal que ejecuta las demostraciones de uso.
     */
    public static void main(String[] args) {
        // Ejecución de demostraciones
        mostrarGenerico(List.of(1, 2, 3));
        mostrarGenericoMap(Map.of("a", 1, "b", 2, "c", 3));
        mostrarColeccionesAvanzadas();
        mostrarPriorityQueue();
        mostrarLinkedList();
    }
}
```

Este código muestra ejemplos de cómo utilizar genéricos y colecciones avanzadas en Java, como `List`, `Map`, `Set`, `TreeSet`, `PriorityQueue` y `LinkedList`. Cada método es explicado con un comentario que describe su propósito.