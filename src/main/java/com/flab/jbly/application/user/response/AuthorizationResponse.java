package com.flab.jbly.application.user.response;

import com.flab.jbly.domain.auth.Session;
import jakarta.validation.constraints.NotNull;

public record AuthorizationResponse(
    @NotNull
    Long userId
) {

    public static AuthorizationResponse fromSessionEntity(Session session) {
        return new AuthorizationResponse(
            session.getUserId()
        );
    }
}
