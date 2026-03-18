# Guía Pedagógica: ArrayList vs HashSet en Java

En esta guía exploraremos dos de las estructuras de datos más fundamentales del framework de Colecciones de Java (`java.util`), comparando sus comportamientos, ventajas y casos de uso.

## 1. ArrayList (La Lista Dinámica)

Un `ArrayList` es como un array convencional, pero puede crecer o reducir su tamaño automáticamente.

### Características clave:
- **Ordenado:** Mantiene el orden de inserción.
- **Indexado:** Permite acceder a elementos por su posición (0, 1, 2...).
- **Permite Duplicados:** Puedes tener el mismo elemento varias veces.

### Ejemplo de Código paso a paso:

```java
import java.util.ArrayList;

public class EjemploArrayList {
    public static void main(String[] args) {
        // 1. Inicialización: Creamos una lista de Strings.
        ArrayList<String> listaFrutas = new ArrayList<>();

        // 2. Añadir elementos: Se guardan en el orden en que se añaden.
        listaFrutas.add("Manzana");
        listaFrutas.add("Pera");
        listaFrutas.add("Manzana"); // Duplicado permitido

        // 3. Acceso por índice: Obtenemos el primer elemento (índice 0).
        String primera = listaFrutas.get(0); 
        System.out.println("Primera fruta: " + primera); // Imprime: Manzana

        // 4. Recorrido: El orden se mantiene estrictamente.
        for (String fruta : listaFrutas) {
            System.out.println(fruta);
        }
    }
}
```

---

## 2. HashSet (El Conjunto Matemático)

Un `HashSet` implementa la interfaz `Set`. Se basa en una tabla hash para almacenar elementos.

### Características clave:
- **No Ordenado:** No garantiza que los elementos se mantengan en el orden en que se insertaron.
- **Sin Duplicados:** Si intentas añadir un elemento que ya existe, simplemente no lo añade.
- **Acceso Rápido:** Es extremadamente eficiente para buscar si un elemento existe.

### Ejemplo de Código paso a paso:

```java
import java.util.HashSet;

public class EjemploHashSet {
    public static void main(String[] args) {
        // 1. Inicialización: Creamos un conjunto de Strings.
        HashSet<String> conjuntoFrutas = new HashSet<>();

        // 2. Añadir elementos:
        conjuntoFrutas.add("Manzana");
        conjuntoFrutas.add("Pera");
        conjuntoFrutas.add("Manzana"); // Este duplicado será ignorado automáticamente

        // 3. Comprobación de existencia: Muy rápido gracias al hashing.
        if (conjuntoFrutas.contains("Pera")) {
            System.out.println("La pera está en el conjunto.");
        }

        // 4. Recorrido: El orden puede ser impredecible.
        for (String fruta : conjuntoFrutas) {
            System.out.println(fruta);
        }
        // Nota: Solo verás "Manzana" y "Pera" una vez.
    }
}
```

---

## Tabla Comparativa Resumida

| Característica | ArrayList | HashSet |
| :--- | :--- | :--- |
| **Interfaz** | `List` | `Set` |
| **Duplicados** | Permitidos | No permitidos |
| **Orden** | Mantiene orden de inserción | No garantiza orden |
| **Acceso** | Rápido por índice (`get(i)`) | No tiene índices |
| **Búsqueda** | Lenta (O(n)) si no sabes el índice | Muy rápida (O(1)) |

## ¿Cuándo usar cada uno?

- Usa **ArrayList** cuando el orden de los elementos sea importante o necesites acceder a ellos por su posición.
- Usa **HashSet** cuando quieras asegurar que no haya elementos repetidos y tu prioridad sea la velocidad de búsqueda.
