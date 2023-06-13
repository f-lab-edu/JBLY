package com.flab.jbly.application.user;

import com.flab.jbly.application.user.request.SigninServiceRequest;
import com.flab.jbly.application.user.response.UserResponse;
import com.flab.jbly.domain.auth.Session;
import com.flab.jbly.domain.auth.TokenRepository;
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
public class SigninService {

    private final PasswordEncryption encryption;
    private final UserRepository repository;
    private final HttpSession httpSession;
    private final TokenRepository tokenRepository;

    Logger logger = LoggerFactory.getLogger(this.getClass());

    @Transactional
    public UserResponse login(SigninServiceRequest command) {
        var user = repository.findByUserId(command.userId());

        if (!encryption.decode(command.password(), user.getPassword())) {
            throw new EncoderNoSuchAlgorithmException("EncoderNoSuchAlgorithmException", ErrorCode.PASSWORD_MISMATCH_ERROR);
        }

        // TODO: 2023/02/14 Session SetAttribute 시 key-value refactoring 필요
        var session = Session.of(user.getId(), httpSession.getId());
//        tokenRepository.save(session);
        httpSession.setAttribute("session",session);
        return new UserResponse(user.getUserId());
    }
}
