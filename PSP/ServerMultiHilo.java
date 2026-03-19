```java
// 

/**
 * Clase principal que implementa un servidor multihilo para la gestión de peticiones concurrentes.
 *
 * @author [TuNombre]
 */
public class ServerMultiHilo {

    private final int puerto;
    private Thread[] hilosServidor;

    /**
     * Constructor de la clase ServerMultiHilo
     * 
     * @param puerto El número de puerto en el que el servidor escuchará las conexiones.
     */
    public ServerMultiHilo(int puerto) {
        this.puerto = puerto;
        iniciarServidor();
    }

    private void iniciarServidor() {
        try (ServerSocket serverSocket = new ServerSocket(puerto)) {
            System.out.println("Servidor iniciado. Esperando conexiones en el puerto " + puerto);

            // Crear un número determinado de hilos para manejar las conexiones concurrentes
            int numHilos = 5; // Puedes ajustar este valor según tus necesidades
            this.hilosServidor = new Thread[numHilos];

            for (int i = 0; i < numHilos; i++) {
                HilosManejador hilo = new HilosManejador(serverSocket.accept());
                hilosServidor[i] = new Thread(hilo);
                hilosServidor[i].start();
            }
        } catch (IOException e) {
            System.err.println("Error al iniciar el servidor: " + e.getMessage());
        }
    }

    /**
     * Clase interna que maneja cada conexión individual.
     */
    private class HilosManejador implements Runnable {

        private Socket cliente;

        public HilosManejador(Socket cliente) {
            this.cliente = cliente;
        }

        @Override
        public void run() {
            try (BufferedReader entrada = new BufferedReader(new InputStreamReader(cliente.getInputStream()));
                 PrintWriter salida = new PrintWriter(cliente.getOutputStream(), true)) {

                String requestLine = entrada.readLine();
                if (requestLine == null) {
                    throw new IOException("No se recibió una línea de solicitud válida");
                }

                System.out.println("Solicitud recibida: " + requestLine);
                // Aquí puedes procesar la solicitud del cliente y enviar la respuesta
                salida.println("HTTP/1.1 200 OK");
                salida.println("Content-Type: text/html; charset=UTF-8");
                salida.println();
                salida.println("<html><body><h1>Bienvenido al servidor multihilo</h1></body></html>");

            } catch (IOException e) {
                System.err.println("Error de entrada/salida: " + e.getMessage());
            } finally {
                try {
                    cliente.close();
                } catch (IOException e) {
                    // Ignorar, ya que el socket se cierra automáticamente al salir del bloque 'try'
                }
            }
        }
    }

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Uso: java ServerMultiHilo <puerto>");
            return;
        }

        int puerto = Integer.parseInt(args[0]);
        new ServerMultiHilo(puerto);
    }
}
```

Este código implementa un servidor multihilo básico en Java. Cada hilo maneja una conexión individual del cliente, permitiendo al servidor manejar múltiples conexiones simultáneamente. Se proporcionan los detalles de la estructura y el funcionamiento del servidor, incluyendo el manejo de excepciones y la interacción con el cliente a través de sockets.