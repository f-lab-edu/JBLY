package com.flab.jbly.domain.auth;

public interface SessionRepository {

    void save(Session session);

    Session findById(Long id);
}
