package com.flab.jbly;

import com.redis.testcontainers.RedisContainer;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.MySQLContainer;
import org.testcontainers.junit.jupiter.Container;
import org.testcontainers.junit.jupiter.Testcontainers;
import org.testcontainers.utility.DockerImageName;

@Testcontainers
public class BasicMySqlContainer {

    private static final String MYSQL_VERSION = "mysql:8";
    private static final String REDIS_VERSION = "redis:7.0.11";

    @Container
    public static final MySQLContainer MY_SQL_CONTAINER = new MySQLContainer(MYSQL_VERSION);

    @Container
    public static final RedisContainer REDIS_CONTAINER = new RedisContainer(DockerImageName.parse(REDIS_VERSION)).withExposedPorts(6379);

    @DynamicPropertySource
    private static void registerRedisProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.data.redis.host", REDIS_CONTAINER::getHost);
        registry.add("spring.data.redis.port",
            () -> REDIS_CONTAINER.getMappedPort(6379).toString());
    }
}
