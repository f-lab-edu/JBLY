package com.flab.jbly.domain.auth;

import com.flab.jbly.infrastructure.common.Role;
import java.io.Serializable;
import lombok.Getter;

@Getter
public class Token implements Serializable {

    private String token;
    private Long memberId;
    private Role role;

    public Token(String token, Long memberId, Role role) {
        this.token = token;
        this.memberId = memberId;
        this.role = role;
    }
}

