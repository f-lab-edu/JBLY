package com.flab.jbly.domain.auth;

public interface SessionRepository {

    void save(Session session);

    Session findBySession(String Session);
}
