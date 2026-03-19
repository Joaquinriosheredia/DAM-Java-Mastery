```sql
-- archivo.sql

USE sales_database;

-- Ejemplo 1: Uso de subconsulta para filtrar resultados
SELECT customer_id, order_date, total_amount,
       (SELECT MAX(total_amount) FROM orders WHERE customer_id = t.customer_id AND order_date <= t.order_date) AS max_total_amount_so_far
FROM orders t
ORDER BY customer_id, order_date;

-- Ejemplo 2: Uso de window function para calcular la suma acumulativa por cliente
SELECT customer_id, order_date,
       SUM(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_total
FROM orders;

-- Ejemplo 3: Subconsulta en FROM clause para unir con otra tabla
SELECT o.customer_id, c.name, MAX(o.order_date) as latest_order_date
FROM (SELECT customer_id, order_date 
      FROM orders 
      WHERE order_date > '2023-01-01') o
JOIN customers c ON o.customer_id = c.id
GROUP BY o.customer_id, c.name;

-- Ejemplo 4: Uso de window function para calcular la media móvil
SELECT customer_id, order_date,
       AVG(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date ROWS BETWEEN 1 PRECEDING AND CURRENT ROW) AS rolling_average_total
FROM orders
ORDER BY customer_id, order_date;
```