package com.flab.jbly.infrastructure.exception;

import lombok.Getter;

@Getter
public class ErrorResponse {
    private String message;
    private int status;

    public ErrorResponse(ErrorCode errorCode) {
        this.status = errorCode.getStatus();
        this.message = errorCode.getMessage();
    }
}
