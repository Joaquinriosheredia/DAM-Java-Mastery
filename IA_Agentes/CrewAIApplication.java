```java
package com.crewai.application;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = {"com.crewai"})
public class CrewAIApplication {

    public static void main(String[] args) {
        SpringApplication.run(CrewAIApplication.class, args);
    }
}
```