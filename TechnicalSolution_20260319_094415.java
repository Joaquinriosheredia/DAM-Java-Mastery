```java
package es.joaquin.portfolio;

import java.util.Optional;

public class UsoOptional {

    /**
     * Clase principal que demuestra el uso de Optional para manejar valores nulos.
     */
    
    public static void main(String[] args) {
        String nombre = null;
        
        // Uso de Optional para evitar NullPointerException
        Optional<String> optionalNombre = Optional.ofNullable(nombre);
        
        if (optionalNombre.isPresent()) {
            System.out.println("El nombre es: " + optionalNombre.get());
        } else {
            System.out.println("El nombre no está definido.");
        }
    }
}
```