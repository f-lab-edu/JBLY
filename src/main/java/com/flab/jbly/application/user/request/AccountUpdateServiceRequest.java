package com.flab.jbly.application.user.request;

public record AccountUpdateServiceRequest(
    Long id,
    String userId,
    String password,
    String name,
    String phone,
    String email,
    String address
) {

}
