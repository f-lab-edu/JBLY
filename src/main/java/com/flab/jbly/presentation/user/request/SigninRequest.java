package com.flab.jbly.presentation.user.request;

import com.flab.jbly.application.user.request.SigninServiceRequest;
import org.springframework.util.Assert;

public record SigninRequest(
		String userId,
		String password
) {

	public SigninRequest {
		Assert.isTrue(userId.length() > 0, "로그인을 할 수 없습니다.");
		Assert.isTrue(password.length() > 7, "비밀번호는 8~16자 영문, 숫자, 특수문자를 사용하세요.");
	}

	public SigninServiceRequest toService() {
				return new SigninServiceRequest(
						this.userId,
						this.password
				);
		}
}
