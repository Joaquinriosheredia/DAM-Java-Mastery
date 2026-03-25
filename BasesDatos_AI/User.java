[CONTENIDO]
package com.example.graphdb.model;

import org.springframework.data.neo4j.core.schema.GeneratedValue;
import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;

@Node
public class User {

    @Id
    @GeneratedValue
    private Long id;
    private String name;
    private Integer age;

    // Getters and Setters

}