package com.flab.jbly.infrastructure.redis;

import com.flab.jbly.domain.auth.Token;
import com.flab.jbly.domain.auth.TokenRepository;
import java.util.concurrent.TimeUnit;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Repository;

@Repository
public class TokenRedisTemplate implements TokenRepository {

    private final RedisTemplate<String, Token> redisTemplate;
    private static final long DEFAULT_LIFE_TIME = 240;

    public TokenRedisTemplate(RedisTemplate<String, Token> redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @Override
    public void save(Token token) {
        redisTemplate.opsForValue()
            .set(token.getToken(), token, DEFAULT_LIFE_TIME, TimeUnit.MINUTES);
    }

    @Override
    public Token findByToken(String token) {
        if (token == null) {
            throw new IllegalArgumentException("token is null");
        }
        Object tokenObj = redisTemplate.opsForValue().get(token);
        return (Token) tokenObj;
    }

    @Override
    public void deleteByToken(String token) {
        redisTemplate.delete(token);
    }
}
