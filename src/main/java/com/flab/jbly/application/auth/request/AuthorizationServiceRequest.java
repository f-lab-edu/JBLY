package com.flab.jbly.application.auth.request;

import com.flab.jbly.infrastructure.common.Role;
import lombok.Getter;

@Getter
public class AuthorizationServiceRequest {

    private final Long memberId;
    private final Role role;

    public AuthorizationServiceRequest(Long memberId, Role role) {
        this.memberId = memberId;
        this.role = role;
    }
}
