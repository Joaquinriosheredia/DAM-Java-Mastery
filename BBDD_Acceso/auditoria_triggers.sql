```sql
-- 

/*
    Este script crea triggers para auditoría automática en tablas críticas.

    @author Desarrollador Senior de BBDD
    @version 1.0
*/

-- Definición del trigger para INSERT
CREATE OR REPLACE TRIGGER trg_audit_insert_tabla1
AFTER INSERT ON tabla1
FOR EACH ROW
DECLARE
BEGIN
    -- Inserta un nuevo registro en la tabla auditoria con los datos del INSERT
    INSERT INTO auditoria (fecha_hora, accion, id_tabla, columna1, columna2)
    VALUES (SYSDATE, 'INSERT', :NEW.id, :NEW.columna1, :NEW.columna2);
END;
/

-- Definición del trigger para UPDATE
CREATE OR REPLACE TRIGGER trg_audit_update_tabla1
AFTER UPDATE ON tabla1
FOR EACH ROW
DECLARE
BEGIN
    -- Inserta un nuevo registro en la tabla auditoria con los datos antes y después de la actualización
    INSERT INTO auditoria (fecha_hora, accion, id_tabla, columna_antigua, columna_nueva)
    VALUES (SYSDATE, 'UPDATE', :OLD.id, :OLD.columna1 || ' -> ' || :NEW.columna1,
                                                    :OLD.columna2 || ' -> ' || :NEW.columna2);
END;
/

-- Definición del trigger para DELETE
CREATE OR REPLACE TRIGGER trg_audit_delete_tabla1
AFTER DELETE ON tabla1
FOR EACH ROW
DECLARE
BEGIN
    -- Inserta un nuevo registro en la tabla auditoria con los datos antes de la eliminación
    INSERT INTO auditoria (fecha_hora, accion, id_tabla, columna_antigua)
    VALUES (SYSDATE, 'DELETE', :OLD.id, :OLD.columna1 || ', ' || :OLD.columna2);
END;
/
```

Este script SQL crea triggers para insertar, actualizar y eliminar registros en la tabla `auditoria` cada vez que ocurren cambios en la tabla `tabla1`. Los datos relevantes se capturan y se registran con la hora de la acción, el tipo de operación (INSERT, UPDATE o DELETE) y los valores antes y después del cambio.