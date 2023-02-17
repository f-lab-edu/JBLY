package com.flab.jbly.infrastructure.auth;

import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.DoesNotAllowLogoutException;
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
    public Session findBySession(String session) {
        return repository.findBySessionToken(session).orElseThrow(() -> new SessionDoesNotExistException("일치하는 Session 값이 없습니다."));
    }

    @Override
    public void deleteById(Long id) {
        if (id == null) {
            throw new DoesNotAllowLogoutException("삭제할 데이터를 찾을 수 없습니다.");
        }
        repository.deleteById(id);
    }
}
