package com.flab.jbly.application.user.request;

public record SigninServiceRequest(
		String userId,
		String password
) {
}
