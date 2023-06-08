package com.flab.jbly.presentation.user.request;

import com.flab.jbly.application.user.request.AccountDeleteServiceRequest;
import org.springframework.util.Assert;

public record AccountDeleteRequest(
    Long id,
    String userId
) {

    public AccountDeleteRequest {
        Assert.isTrue(id > 0L,"존재할 수 없는 PK값입니다.");
        Assert.isTrue(userId.length() > 0, "사용자 ID는 필수 입력입니다.");
    }

    public AccountDeleteServiceRequest toCommand() {
        return new AccountDeleteServiceRequest(
            this.id,
            this.userId
        );
    }
}
