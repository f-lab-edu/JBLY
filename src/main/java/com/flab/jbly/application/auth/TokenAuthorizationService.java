package com.flab.jbly.application.auth;

import com.flab.jbly.application.auth.request.AuthorizationServiceRequest;
import com.flab.jbly.application.auth.response.AuthorizationResponse;
import com.flab.jbly.domain.auth.Token;
import com.flab.jbly.domain.auth.TokenRepository;
import jakarta.servlet.http.HttpServletRequest;
import java.util.UUID;

public class TokenAuthorizationService implements AuthorizationService {

    private final TokenRepository tokenRepository;

    public TokenAuthorizationService(TokenRepository tokenRepository) {
        this.tokenRepository = tokenRepository;
    }

    @Override
    public String login(AuthorizationServiceRequest request) {
        String token = UUID.randomUUID().toString();
        tokenRepository.save(Token.builder()
            .token(token)
            .memberId(request.getMemberId())
            .role(request.getRole())
            .build()
        );

        return token;
    }

    @Override
    public AuthorizationResponse getCurrentUser(HttpServletRequest request) {
        String token = String.valueOf(request.getHeaders("Authorization"));
        Token tokenById = tokenRepository.findByToken(token);

        if (tokenById == null) {
            return null;
        }
        return AuthorizationResponse.fromToken(tokenById);
    }

    @Override
    public void logout(HttpServletRequest request) {
        String token = String.valueOf(request.getHeaders("Authorization"));
        tokenRepository.deleteByToken(token);
    }
}
