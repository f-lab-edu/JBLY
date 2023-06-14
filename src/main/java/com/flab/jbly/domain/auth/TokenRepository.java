package com.flab.jbly.domain.auth;

public interface TokenRepository {

    void save(Token token);

    Token findByToken(String token);

    void deleteByToken(String token);
}
