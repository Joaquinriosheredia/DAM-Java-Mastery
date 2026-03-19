```java
package es.joaquinportfolio;

import java.util.Optional;

/**
 * Clase que demuestra el uso de Optional para evitar errores de puntero nulo.
 */
public class OptionalExample {

    /**
     * Muestra cómo usar Optional para manejar la falta de datos de manera segura.
     *
     * @param value Valor a encapsular en Optional
     * @return Optional que puede contener el valor o estar vacío si el valor es null
     */
    public static Optional<String> safeGetString(String value) {
        return Optional.ofNullable(value);
    }

    /**
     * Ejemplo de cómo obtener un valor seguro de Optional.
     *
     * @param optional Valor encapsulado en Optional
     * @return El valor contenido o una cadena vacía si el Optional está vacío
     */
    public static String getValueOrDefault(Optional<String> optional) {
        return optional.orElse("");
    }

    /**
     * Método principal para ejecutar ejemplos.
     *
     * @param args Argumentos de la línea de comandos (no utilizado)
     */
    public static void main(String[] args) {
        Optional<String> empty = safeGetString(null);
        Optional<String> nonEmpty = safeGetString("Hola, mundo!");

        System.out.println(getValueOrDefault(empty));  // Debería imprimir: ""
        System.out.println(getValueOrDefault(nonEmpty));  // Debería imprimir: "Hola, mundo!"
    }
}
```