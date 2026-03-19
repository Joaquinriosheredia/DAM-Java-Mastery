```java
package es.joaquin.portfolio;

import java.util.List;

/**
 * Interfaz genérica para la implementación de Data Access Objects (DAO).
 * 
 * @param <T> Tipo genérico que representará el tipo de entidad manejada por el DAO.
 */
public interface GenericDAO<T> {

    /**
     * Obtiene todos los registros de la base de datos.
     *
     * @return Una lista de entidades del tipo T.
     */
    List<T> findAll();

    /**
     * Obtiene un registro por su identificador único.
     *
     * @param id El identificador único del registro a buscar.
     * @return La entidad del tipo T con el ID especificado, o null si no se encuentra.
     */
    T findById(Long id);

    /**
     * Guarda una nueva entidad en la base de datos.
     *
     * @param entity La entidad del tipo T a guardar.
     * @return El objeto guardado, actualizado con cualquier identificador que pueda haber sido asignado por la base de datos.
     */
    T save(T entity);

    /**
     * Actualiza una entidad existente en la base de datos.
     *
     * @param entity La entidad del tipo T a actualizar.
     * @return El objeto actualizado, sin cambios si no se ha encontrado el registro correspondiente.
     */
    T update(T entity);

    /**
     * Elimina una entidad existente de la base de datos.
     *
     * @param id El identificador único de la entidad a eliminar.
     */
    void delete(Long id);
}
```