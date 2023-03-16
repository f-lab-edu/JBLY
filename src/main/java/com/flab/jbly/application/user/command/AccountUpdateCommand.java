package com.flab.jbly.application.user.command;

public record AccountUpdateCommand(
    Long id,
    String userId,
    String password,
    String name,
    String phone,
    String email,
    String address
) {

}
