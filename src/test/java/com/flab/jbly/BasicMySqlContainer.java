package com.flab.jbly;

import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;

@Testcontainers
public class BasicMySqlContainer {

    private static final String MYSQL_VERSION = "mysql:8";

    @Container
    public static final MySQLContainer mysqlContainer = new MySQLContainer(MYSQL_VERSION);
}
