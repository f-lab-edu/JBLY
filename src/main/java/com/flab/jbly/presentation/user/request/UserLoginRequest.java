package com.flab.jbly.presentation.user.request;

import jakarta.validation.constraints.NotEmpty;

public record UserLoginRequest(
		@NotEmpty
		String userId,
		@NotEmpty
		String password
) {
}
