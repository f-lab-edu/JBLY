package com.flab.jbly.presentation.user.request;

import com.flab.jbly.application.user.command.LoginCommand;
import jakarta.validation.constraints.NotEmpty;

public record LoginRequest(
    @NotEmpty
    String userId,
    @NotEmpty
    String password
) {
    public LoginCommand toCommand() {
        return new LoginCommand(
            this.userId,
            this.password
        );
    }
}
