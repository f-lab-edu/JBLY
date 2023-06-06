package com.flab.jbly.infrastructure.redis;

import static org.assertj.core.api.Assertions.assertThat;

import java.util.Set;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.data.redis.core.SetOperations;
import org.springframework.data.redis.core.ValueOperations;

@SpringBootTest
public class RedisTemplateTest {

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @DisplayName("Redis(key-value) 기본 동작 검증")
    @Test
    public void redisStringTypeTest() throws Exception {
        // given
        ValueOperations<String, String> valueOperations = redisTemplate.opsForValue();
        String key = "hello";

        // when
        valueOperations.set(key,"world");

        // then
        assertThat(valueOperations.get(key)).isEqualTo("world");
    }

    @DisplayName("Redis(key-setValue) 동작 검증")
    @Test
    public void redisSetTypeTest() throws Exception {
        // given
        SetOperations<String, String> setOperations = redisTemplate.opsForSet();
        String key = "setKey";

        // when
        setOperations.add(key, "h", "e", "l", "l", "o");

        // then
        Set<String> members = setOperations.members(key);
        Long size = setOperations.size(key);

        assertThat(members).containsOnly("h", "e", "l", "o");
        assertThat(size).isEqualTo(4);
    }


}
