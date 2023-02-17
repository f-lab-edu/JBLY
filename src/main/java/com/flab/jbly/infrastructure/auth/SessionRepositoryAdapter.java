package com.flab.jbly.infrastructure.auth;

import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.user.DoesNotAllowLogoutException;
import com.flab.jbly.infrastructure.exception.auth.SessionDoesNotExistException;
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
        try {
            repository.deleteById(id);
        } catch (Exception e) {
            throw new DoesNotAllowLogoutException("로그아웃 대상이 아닙니다.");
        }
    }
}
