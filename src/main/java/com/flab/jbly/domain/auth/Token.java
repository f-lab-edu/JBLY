package com.flab.jbly.domain.auth;

import com.flab.jbly.infrastructure.common.Role;
import java.io.Serializable;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class Token implements Serializable {

    private String token;
    private Long memberId;
    private Role role;

    @Builder
    public Token(String token, Long memberId, Role role) {
        this.token = token;
        this.memberId = memberId;
        this.role = role;
    }
}

