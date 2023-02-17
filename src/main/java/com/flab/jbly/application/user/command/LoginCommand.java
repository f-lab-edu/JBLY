package com.flab.jbly.application.user.command;

public record LoginCommand(
		String userId,
		String password
) {
}
