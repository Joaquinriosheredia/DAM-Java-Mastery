```java
package com.example.database.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.util.List;

import javax.sql.DataSource;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.testcontainers.containers.PostgreSQLContainer;
import org.testcontainers.shaded.org.apache.commons.dbutils.QueryRunner;
import org.testcontainers.utility.DockerImageName;

public class DatabaseServiceTest {

    private static final PostgreSQLContainer<?> POSTGRES_CONTAINER = new PostgreSQLContainer<>(DockerImageName.parse("postgres:13.4-alpine"))
            .withDatabaseName("testdb")
            .withUsername("testuser")
            .withPassword("testpass");

    private DatabaseService databaseService;
    private DataSource dataSource;

    @BeforeAll
    public static void startPostgresContainer() {
        POSTGRES_CONTAINER.start();
    }

    @BeforeEach
    public void setup() throws Exception {
        // Crear el servicio con un contenedor de PostgreSQL en funcionamiento
        String dbUrl = "jdbc:postgresql://" + POSTGRES_CONTAINER.getContainerIpAddress() +
                ":" + POSTGRES_CONTAINER.getFirstMappedPort() + "/" + POSTGRES_CONTAINER.getDatabaseName();
        
        dataSource = new DataSource() { // Mocking the data source creation with container info
            @Override
            public Connection getConnection() throws SQLException {
                return DriverManager.getConnection(dbUrl, "testuser", "testpass");
            }
            
            // Implementar otras operaciones del DataSource según sea necesario.
        };
        
        databaseService = new DatabaseService(dataSource);
        
        // Creación de tabla y carga inicial de datos (ejemplo)
        QueryRunner runner = new QueryRunner();
        String createTableQuery = "CREATE TABLE IF NOT EXISTS users (" +
                "id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL)";
        runner.update(dataSource.getConnection(), createTableQuery);
    }

    @AfterEach
    public void tearDown() throws Exception {
        // Borrar datos o realizar otras acciones de limpieza aquí si es necesario.
    }
    
    @Test
    public void testRetrieveUsersShouldReturnListWithCorrectSize() throws Exception {
        // Insertar algunos usuarios en la base de datos (ejemplo)
        databaseService.insertUser("Alice");
        databaseService.insertUser("Bob");

        List<String> users = databaseService.retrieveAllUsers();
        
        assertEquals(2, users.size());
    }

    @Test
    public void testRetrieveNonExistingUserShouldThrowException() throws Exception {
        assertThrows(IllegalArgumentException.class, () -> databaseService.retrieveUserById(-1));
    }
    
    // Añadir más pruebas según sea necesario.
}
```