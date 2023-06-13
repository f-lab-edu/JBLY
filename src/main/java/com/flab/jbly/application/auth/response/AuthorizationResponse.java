package com.flab.jbly.application.auth.response;

import com.flab.jbly.domain.auth.Token;
import com.flab.jbly.infrastructure.common.Role;
import lombok.Getter;

@Getter
public class AuthorizationResponse {

    private final Long memberId;
    private final Role role;

    public AuthorizationResponse(Long memberId, Role role) {
        this.memberId = memberId;
        this.role = role;
    }

    public static AuthorizationResponse fromToken(Token token) {
        return new AuthorizationResponse(token.getMemberId(), token.getRole());
    }
}
