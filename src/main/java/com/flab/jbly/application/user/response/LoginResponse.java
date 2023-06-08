package com.flab.jbly.application.user.response;

import jakarta.validation.constraints.NotNull;

public record LoginResponse(
		@NotNull
		String userId
) {

}
