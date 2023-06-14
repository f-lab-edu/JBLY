package com.flab.jbly.application.user.request;

public record AccountDeleteServiceRequest(
    Long Id,
    String userId
) {

}
