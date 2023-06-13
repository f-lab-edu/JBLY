package com.flab.jbly.application.auth.response;

import com.flab.jbly.infrastructure.common.Role;
import jakarta.validation.constraints.NotNull;

public record AuthorizationResponse(
    @NotNull
    Long userId,
    @NotNull
    Role role
) {
}
