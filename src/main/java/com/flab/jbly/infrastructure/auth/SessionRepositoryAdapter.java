package com.flab.jbly.infrastructure.auth;

import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.SessionDoesNotExistException;
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

    @Override
    public Session findById(Long id) {
        return repository.findById(id).orElseThrow(() -> new SessionDoesNotExistException("일치하는 Session 값이 없습니다."));
    }

}
