package com.flab.jbly.domain.auth;

public interface TokenRepository {

    void save(Session session);

    Token findByToken(String token);

    void deleteByToken(String token);
}
