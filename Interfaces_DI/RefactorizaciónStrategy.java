```java
/**
 * Clase que implementa la estrategia para refactoring en un sistema legacy.
 * 
 * @version 1.0
 * @since 2023-08-XX
 */
public class RefactorizaciónStrategy {

    /**
     * Interfaz de Estrategia que define el método a refactorizar.
     */
    public interface RefactorizableStrategy {
        void refactorizarCódigo();
    }

    /**
     * Estrategia de refactoring basada en desacoplamiento y responsabilidad única.
     * 
     * @version 1.0
     * @since 2023-08-XX
     */
    public static class DesacoplarResponsabilidadesStrategy implements RefactorizableStrategy {
        @Override
        public void refactorizarCódigo() {
            // Implementación que refactoring el código legado para desacoplar responsabilidades.
            System.out.println("Desacoplando responsabilidades en el código legacy.");
        }
    }

    /**
     * Estrategia de refactoring basada en la separación del objeto y la lógica.
     * 
     * @version 1.0
     * @since 2023-08-XX
     */
    public static class SepararObjetoStrategy implements RefactorizableStrategy {
        @Override
        public void refactorizarCódigo() {
            // Implementación que refactoring el código legado para separar el objeto y la lógica.
            System.out.println("Separando el objeto y la lógica en el código legacy.");
        }
    }

    /**
     * Clase que define el contexto donde se aplica una estrategia de refactorización.
     */
    public static class Context {
        private RefactorizableStrategy strategy;

        /**
         * Constructor que inicializa el context con un strategy.
         *
         * @param strategy La estrategia a aplicar para la refactorización.
         */
        public Context(RefactorizableStrategy strategy) {
            this.strategy = strategy;
        }

        /**
         * Método que ejecuta la refactoring basada en la estrategia asignada.
         */
        public void ejecutarRefactorización() {
            if (strategy != null) {
                strategy.refactorizarCódigo();
            } else {
                System.out.println("Strategy no definida, refactorización no realizada.");
            }
        }
    }

    /**
     * Ejemplo de uso del pattern Strategy.
     */
    public static void main(String[] args) {
        // Creando un contexto y asignando una estrategia
        Context contexto = new Context(new DesacoplarResponsabilidadesStrategy());
        contexto.ejecutarRefactorización();

        // Cambiando la estrategia para otra refactoring
        contexto.setStrategy(new SepararObjetoStrategy());
        contexto.ejecutarRefactorización();
    }
}
```

Este código implementa el patrón de diseño Strategy para aplicar diferentes técnicas de refactorización a un código legacy. Cada clase implementa una interfaz `RefactorizableStrategy` que define la lógica de refactorización específica, y se utiliza un contexto (`Context`) para aplicar dichas estrategias dinámicamente.