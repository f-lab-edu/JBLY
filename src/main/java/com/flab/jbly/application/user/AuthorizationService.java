package com.flab.jbly.application.user;

import com.flab.jbly.application.user.result.AuthorizationResult;
import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.EmptySessionException;
import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthorizationService {

    private final SessionRepository repository;

    public AuthorizationResult getCurrentUser(HttpServletRequest request) {
        var session = (Session) request.getSession().getAttribute("user");
        if (session == null) {
            throw new EmptySessionException();
        }
        var currentUserSession = repository.findBySession(session.getSessionToken());
        return AuthorizationResult.fromSessionEntity(currentUserSession);
    }

}
