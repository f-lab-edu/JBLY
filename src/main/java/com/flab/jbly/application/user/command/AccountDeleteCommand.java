package com.flab.jbly.application.user.command;

public record AccountDeleteCommand(
    Long Id,
    String userId
) {

}
