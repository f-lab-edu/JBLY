package com.flab.jbly.application.user;

import com.flab.jbly.application.user.result.AuthorizationResult;
import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.EmptySessionException;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthorizationService {

    private final SessionRepository repository;
    private final HttpSession session;

    public AuthorizationResult getCurrentUser() {
        var session = (Session) this.session.getAttribute("user");
        if (session == null) {
            throw new EmptySessionException();
        }
        repository.findById(session.getId());
        return AuthorizationResult.fromSessionEntity(session);
    }

}
