package com.flab.jbly.application.user.response;

import jakarta.validation.constraints.NotNull;

public record UserResponse(

    @NotNull
    String userId
) {

}
