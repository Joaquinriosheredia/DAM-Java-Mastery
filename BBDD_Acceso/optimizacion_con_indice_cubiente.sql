```sql
-- 

-- Se crea una tabla ejemplo con múltiples columnas para demostrar el uso de índices cubrientes.
CREATE TABLE empleados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido1 VARCHAR(100) NOT NULL,
    apellido2 VARCHAR(100),
    fecha_nacimiento DATE,
    salario DECIMAL(10, 2)
);

-- Se insertan algunos datos de ejemplo en la tabla.
INSERT INTO empleados (nombre, apellido1, apellido2, fecha_nacimiento, salario)
VALUES 
('Juan', 'Perez', 'Garcia', '1985-03-14', 60000.00),
('Maria', 'Lopez', 'Martin', '1987-12-25', 55000.00),
('Carlos', 'Jimenez', NULL, '1990-01-11', 45000.00);

-- Se crea un índice cubierto para las columnas nombre y apellido1
CREATE INDEX idx_nombres_apellidos ON empleados (nombre, apellido1);

-- Consulta que utiliza el índice cubierto para obtener los datos de los empleados
SELECT * 
FROM empleados 
WHERE nombre = 'Juan' AND apellido1 = 'Perez';

/*
NOTAS:
- El índice cubierto para las columnas nombre y apellido1 permite a MySQL recuperar todas las columnas solicitadas sin necesidad de realizar un segundo acceso a la tabla.
- Esto puede reducir significativamente el tiempo de respuesta en consultas complejas que incluyen muchas columnas.
*/
```