package com.flab.jbly.application.user.request;

import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@Builder
@AllArgsConstructor
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class SignUpServiceRequest {

    private String userId;

    private String password;

    private String name;

    private String phone;

    private String email;

    private String address;

}

