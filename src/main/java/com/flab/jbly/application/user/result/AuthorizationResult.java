package com.flab.jbly.application.user.result;

import com.flab.jbly.domain.auth.Session;
import jakarta.validation.constraints.NotNull;

public record AuthorizationResult(
    @NotNull
    Long userId
) {

    public static AuthorizationResult fromSessionEntity(Session session) {
        return new AuthorizationResult(
            session.getUserId()
        );
    }
}
