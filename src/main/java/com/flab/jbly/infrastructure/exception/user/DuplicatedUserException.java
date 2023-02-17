package com.flab.jbly.infrastructure.exception.user;

import com.flab.jbly.infrastructure.exception.ErrorCode;
import lombok.Getter;

@Getter
public class DuplicatedUserException extends RuntimeException {

    private ErrorCode errorCode;

    public DuplicatedUserException(String message, ErrorCode errorCode) {
        super(message);
        this.errorCode = errorCode;
    }
}
