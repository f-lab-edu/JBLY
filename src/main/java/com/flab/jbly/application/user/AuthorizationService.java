package com.flab.jbly.application.user;

import com.flab.jbly.application.user.result.AuthorizationResult;
import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.auth.EmptySessionException;
import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthorizationService {

    private final SessionRepository repository;

    public AuthorizationResult getCurrentUser(HttpServletRequest request) {
        // TODO: 2023/02/14 Casting Exception 발생
        var session = (Session) request.getSession().getAttribute("session");
        if (session == null) {
            throw new EmptySessionException();
        }
        var currentUserSession = repository.findBySession(session.getSessionToken());
        return AuthorizationResult.fromSessionEntity(currentUserSession);
    }

}
