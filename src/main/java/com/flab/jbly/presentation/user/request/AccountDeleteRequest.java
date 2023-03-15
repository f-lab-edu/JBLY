package com.flab.jbly.presentation.user.request;

import com.flab.jbly.application.user.command.AccountDeleteCommand;
import jakarta.validation.constraints.NotEmpty;
import org.springframework.util.Assert;

public record AccountDeleteRequest(

    @NotEmpty
    Long Id,
    @NotEmpty
    String userId
) {

    public AccountDeleteRequest {
        Assert.isTrue(Id > 0L,"존재할 수 없는 PK값입니다.");
        Assert.isTrue(userId.length() > 0, "사용자 ID는 필수 입력입니다.");
    }

    public AccountDeleteCommand toCommand() {
        return new AccountDeleteCommand(
            this.Id,
            this.userId
        );
    }
}
