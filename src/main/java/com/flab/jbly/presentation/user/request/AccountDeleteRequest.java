package com.flab.jbly.presentation.user.request;

import com.flab.jbly.application.user.command.AccountDeleteCommand;
import jakarta.validation.constraints.NotEmpty;

public record AccountDeleteRequest(

    @NotEmpty
    Long Id,
    @NotEmpty
    String userId
) {

    public AccountDeleteCommand toCommand() {
        return new AccountDeleteCommand(
            this.Id,
            this.userId
        );
    }
}
