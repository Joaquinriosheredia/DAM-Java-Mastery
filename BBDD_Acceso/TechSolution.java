```java
/**
 * Nombre del archivo: GenericDAO.java
 *
 * Descripción:
 * Este archivo implementa un DAO (Data Access Object) genérico utilizando Hibernate y JPA.
 * El DAO proporciona una abstracción a nivel de persistencia para operaciones CRUD básicas,
 * lo que permite manejar diferentes entidades de manera uniforme sin modificar el código fuente
 * de cada entidad.
 *
 * Nota: Este es un ejemplo sencillo y puede ser extensible según las necesidades específicas del proyecto.
 */
package com.example.persistence;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.transaction.Transactional;
import java.io.Serializable;
import java.util.List; 

/**
 * @param <T> La clase de entidad generada
 * @param <ID> El tipo de identificador de la entidad
 */
public class GenericDAO<T, ID extends Serializable> {

    /**
     * Campo persistente para acceder al EntityManager.
     */
    @PersistenceContext
    private EntityManager entityManager;

    /**
     * Método que permite obtener una entidad por su id.
     *
     * @param id El identificador de la entidad a recuperar
     * @return La entidad recuperada o null si no existe
     */
    public T findById(ID id) {
        return entityManager.find(getEntityClass(), id);
    }

    /**
     * Método que permite guardar una nueva entidad.
     *
     * @param entity La entidad para persistir
     * @return La entidad persistida con su identificador asignado
     */
    @Transactional
    public T save(T entity) {
        if (entity.getId() == null) {
            entityManager.persist(entity);
        } else {
            return entityManager.merge(entity);
        }
        return entity;
    }

    /**
     * Método que permite eliminar una entidad.
     *
     * @param entity La entidad a eliminar
     */
    @Transactional
    public void delete(T entity) {
        if (entityManager.contains(entity)) {
            entityManager.remove(entity);
        } else {
            T attachedEntity = findById(entity.getId());
            if (attachedEntity != null) {
                entityManager.remove(attachedEntity);
            }
        }
    }

    /**
     * Método que permite listar todas las entidades de un determinado tipo.
     *
     * @return Una lista con todos los objetos persistidos
     */
    public List<T> findAll() {
        return entityManager.createQuery("FROM " + getEntityClass().getName()).getResultList();
    }

    /**
     * Método abstracto que devuelve la clase de entidad para las operaciones genéricas.
     *
     * @return Clase de la entidad concreta
     */
    protected abstract Class<T> getEntityClass();

}
```

Este código es una implementación de un DAO (Data Access Object) genérico utilizando Hibernate y JPA. Este archivo proporciona métodos básicos CRUD para interactuar con el persistente, permitiendo manejar diferentes entidades de manera uniforme. La anotación `@PersistenceContext` se utiliza para inyectar el contexto del EntityManager en tiempo de ejecución, lo que permite realizar operaciones de persistencia a través de este recurso.
