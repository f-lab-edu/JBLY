package com.flab.jbly.infrastructure.auth;

import com.flab.jbly.domain.user.Session;
import com.flab.jbly.domain.user.SessionRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

@Repository
@RequiredArgsConstructor
public class SessionRepositoryAdapter implements SessionRepository {

    private final SessionJpaRepository repository;

    @Override
    public void save(Session session) {
        repository.save(session);
    }
}
