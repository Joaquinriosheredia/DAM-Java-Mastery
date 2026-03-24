```sql
-- Primero, asegurarnos de que el módulo pgvector esté instalado y funcione correctamente.
CREATE EXTENSION IF NOT EXISTS vector;

-- Supongamos tenemos una tabla llamada "products" con los siguientes campos:
-- id SERIAL PRIMARY KEY,
-- title TEXT,
-- description TEXT,
-- features VECTOR(512) -- Esto asume que tenemos un vector de características generado por alguna red neuronal

-- Creamos la tabla si no existe
CREATE TABLE IF NOT EXISTS products (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    features VECTOR(512)
);

-- Insertamos algunos ejemplos de datos (vector se genera por una herramienta externa, aquí es un ejemplo)
INSERT INTO products (title, description, features) VALUES 
('Laptop Gaming', 'Una laptop para juegos con alta configuración.', '[0.1, 0.2, ..., 0.3]'),
('Smartphone 5G', 'Un smartphone rápido con conectividad 5G.', '[0.4, 0.5, ..., 0.6]');

-- Ejemplo de una consulta híbrida que combina búsqueda vectorial y texto
SELECT 
    p.id,
    p.title,
    p.description,
    (p.features <-> '[0.3, 0.4, ..., 0.5]'::vector) AS distance -- Operador <-> para cálculo de distancia coseno entre vectores
FROM products p
WHERE
    to_tsvector('english', p.title || ' ' || p.description) @@ to_tsquery('english', 'gaming & smartphone') -- Búsqueda en texto usando tsvector y tsquery
ORDER BY distance LIMIT 10;
```