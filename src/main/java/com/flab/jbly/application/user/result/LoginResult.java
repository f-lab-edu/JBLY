package com.flab.jbly.application.user.result;

import jakarta.validation.constraints.NotNull;

public record LoginResult(
		@NotNull
		String userId
) {

}
