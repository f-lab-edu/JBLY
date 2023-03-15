package com.flab.jbly.presentation.user.request;

import com.flab.jbly.application.user.command.LoginCommand;
import jakarta.validation.constraints.NotEmpty;
import org.springframework.util.Assert;

public record LoginRequest(
		@NotEmpty
		String userId,
		@NotEmpty
		String password
) {

	public LoginRequest {
		Assert.isTrue(userId.length() > 0, "로그인을 할 수 없습니다.");
		Assert.isTrue(password.length() > 7, "비밀번호는 8~16자 영문, 숫자, 특수문자를 사용하세요.");
	}

	public LoginCommand toCommand() {
				return new LoginCommand(
						this.userId,
						this.password
				);
		}
}
