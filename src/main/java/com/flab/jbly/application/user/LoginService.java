package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.LoginCommand;
import com.flab.jbly.application.user.result.LoginResult;
import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.SessionRepository;
import com.flab.jbly.domain.user.PasswordEncryption;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.EncoderNoSuchAlgorithmException;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class LoginService {

    private final PasswordEncryption encryption;
    private final UserRepository repository;
    private final HttpSession httpSession;
    private final SessionRepository sessionRepository;

    Logger logger = LoggerFactory.getLogger(this.getClass());

    @Transactional
    public LoginResult login(LoginCommand command) {
        var user = repository.findByUserId(command.userId());

        if (!encryption.decode(command.password(), user.getPassword())) {
            throw new EncoderNoSuchAlgorithmException("EncoderNoSuchAlgorithmException", ErrorCode.PASSWORD_MISMATCH_ERROR);
        }

        // TODO: 2023/02/14 Session SetAttribute 시 key-value refactoring 필요
        var session = Session.of(user.getId(), httpSession.getId());
        sessionRepository.save(session);
        httpSession.setAttribute("session",session);
        return new LoginResult(user.getUserId());
    }
}
