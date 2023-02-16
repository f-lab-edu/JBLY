package com.flab.jbly.infra.exception.user;

import com.flab.jbly.infra.exception.ErrorCode;
import lombok.Getter;

@Getter
public class EncoderNoSuchAlgorithmException extends RuntimeException {
    private ErrorCode errorCode;

    public EncoderNoSuchAlgorithmException(String message, ErrorCode errorCode){
        super(message);
        this.errorCode = errorCode;
    }
}
