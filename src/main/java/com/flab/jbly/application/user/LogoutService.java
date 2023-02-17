package com.flab.jbly.application.user;

import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.infrastructure.exception.EmptySessionException;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class LogoutService {

    private final SessionRepository sessionRepository;
    private final HttpSession httpSession;


    @Transactional
    public void logout() {
        var session = (Session) httpSession.getAttribute("session");
        if (session == null) {
            throw new EmptySessionException();
        }
        sessionRepository.deleteById(session.getId());
        httpSession.invalidate();
    }
}
