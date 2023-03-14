package com.flab.jbly.presentation.user.request;

import jakarta.validation.constraints.NotEmpty;

public record AccountDeleteRequest(

    @NotEmpty
    Long Id,
    @NotEmpty
    String userId
) {
}
