```java
// Filename: SecureCommunicationClientServer.java

/**
 * Clase que implementa la comunicación cifrada cliente-servidor utilizando SSL/TLS sockets.
 */
public class SecureCommunicationClientServer {

    private final String SERVER_HOST;
    private final int SERVER_PORT;

    /**
     * Constructor de la clase SecureCommunicationClientServer.
     *
     * @param serverHost el host del servidor
     * @param serverPort el puerto del servidor
     */
    public SecureCommunicationClientServer(String serverHost, int serverPort) {
        this.SERVER_HOST = serverHost;
        this.SERVER_PORT = serverPort;
    }

    /**
     * Método que establece la conexión segura con el servidor y envía un mensaje.
     *
     * @param message el mensaje a enviar al servidor
     */
    public void sendSecureMessage(String message) {
        try (
            // Creación del contexto SSL para el socket cliente
            SSLContext sslContext = SSLContext.getInstance("TLS");
            KeyStore keyStore = KeyStore.getInstance("JKS");  // Suponiendo que se utiliza un archivo JKS para el almacenamiento de claves
            FileInputStream keyStoreFileInputStream = new FileInputStream("path/to/keystore.jks");
            // Carga del archivo keystore y configuración de la clave privada
            keyStore.load(keyStoreFileInputStream, "password".toCharArray());
            KeyManagerFactory kmf = KeyManagerFactory.getInstance(KeyManagerFactory.getDefaultAlgorithm());
            kmf.init(keyStore, "password".toCharArray());

            // Configuración del contexto SSL con los manejadores de claves
            sslContext.init(kmf.getKeyManagers(), null, new SecureRandom());

            // Creación del socket seguro al servidor
            SSLSocketFactory sslSocketFactory = sslContext.getSocketFactory();
            SSLSocket sslSocket = (SSLSocket) sslSocketFactory.createSocket(SERVER_HOST, SERVER_PORT);

            // Establecimiento de la conexión SSL y escritura del mensaje
            sslSocket.startHandshake();
            OutputStream outputStream = sslSocket.getOutputStream();
            BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(outputStream));
            writer.write(message);
            writer.flush();

            System.out.println("Mensaje enviado: " + message);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Método de prueba para enviar un mensaje a través del servidor seguro.
     */
    public static void main(String[] args) {
        SecureCommunicationClientServer secureComm = new SecureCommunicationClientServer("localhost", 8443);
        secureComm.sendSecureMessage("Hola, Servidor!");
    }
}
```

Este código Java proporciona una solución técnica profesional para establecer una comunicación cifrada cliente-servidor mediante SSL/TLS sockets. Utiliza un contexto SSL para crear el socket seguro y envía un mensaje al servidor encriptado.

### Notas:
- **Keystore**: Se asume que se utiliza un archivo JKS para almacenar las claves.
- **Password**: Las contraseñas de los archivos de almacenamiento de claves y la clave privada deben ser reemplazadas con valores seguros.
- **Error Handling**: Se maneja en el bloque `try-catch` para capturar posibles excepciones durante la operación.

Este código es un ejemplo básico y puede requerir ajustes adicionales según las necesidades específicas del proyecto.