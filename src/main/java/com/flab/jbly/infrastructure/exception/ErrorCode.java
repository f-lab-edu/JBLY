package com.flab.jbly.infrastructure.exception;

import lombok.AllArgsConstructor;
import lombok.Getter;

@Getter
@AllArgsConstructor
public enum ErrorCode {

    // 409 CONFLICT 중복된 리소스
    USER_DUPLICATION(409, "중복된 User 입니다."),
    USER_DOES_NOT_EXIST(500, "존재하는 User가 아닙니다."),

    // 500 INTERNAL_SERVER_ERROR
    ENCODER_FAILED_ERROR(500, "암호화 실패했습니다. "),
    INTERNAL_SERVER_ERROR(500, "서버 에러입니다."),

    // Not Allowed User Exception
    NOT_FOUND_USER_IN_LOGIN_ERROR(404,"로그인이 필요한 서비스입니다."),
    NOT_FOUND_USER_DELETE_PK_ERROR(500, "로그아웃 대상이 아닙니다."),

    // Auth Exception
    PASSWORD_MISMATCH_ERROR(500, "입력한 비밀번호가 일치하지 않습니다.");

    private final int status;
    private final String message;

}

