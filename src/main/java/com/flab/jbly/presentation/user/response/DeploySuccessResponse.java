package com.flab.jbly.presentation.user.response;

import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class DeploySuccessResponse {

    String text;

    @Builder
    public DeploySuccessResponse(String text) {
        this.text = text;
    }
}
