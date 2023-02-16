package com.flab.jbly.infra.exception;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public enum ErrorCode {

    // 409 CONFLICT 중복된 리소스
    USER_DUPLICATION(409, "중복된 User 입니다."),

    // 500 INTERNAL_SERVER_ERROR
    ENCODER_FAILED_ERROR(500, "암호화 실패했습니다. "),
    INTERNAL_SERVER_ERROR(500, "서버 에러입니다.");

    private final int status;
    private final String message;

}

