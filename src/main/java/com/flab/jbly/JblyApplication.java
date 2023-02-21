package com.flab.jbly;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;


@SpringBootApplication(exclude={DataSourceAutoConfiguration.class})
public class JblyApplication {

    public static void main(String[] args) {
        SpringApplication.run(JblyApplication.class, args);
    }

}
