package com.flab.jbly.presentation.user.request;

import org.springframework.util.Assert;

public record UpdateRequest(
    Long id,
    String userId,
    String password,
    String name,
    String phone,
    String email,
    String address
) {

    public UpdateRequest {
        Assert.isTrue(id > 0L,"존재할 수 없는 PK값입니다.");
        Assert.isTrue(userId.length() > 0, "사용자 ID는 필수 입력입니다.");
        Assert.isTrue(password.length() > 7, "비밀번호는 8~16자 영문, 숫자, 특수문자를 사용하세요.");
        Assert.isTrue(name.length() > 0, "필수적으로 입력해야합니다.");
        Assert.isTrue(phone.length() > 0, "필수적으로 입력해야합니다.");
        Assert.isTrue(email.length() > 0, "필수적으로 입력해야합니다.");
        Assert.isTrue(address.length() > 0, "필수적으로 입력해야합니다.");
    }
}
