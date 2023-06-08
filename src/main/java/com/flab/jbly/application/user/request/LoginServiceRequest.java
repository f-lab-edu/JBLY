package com.flab.jbly.application.user.request;

public record LoginServiceRequest(
		String userId,
		String password
) {
}
