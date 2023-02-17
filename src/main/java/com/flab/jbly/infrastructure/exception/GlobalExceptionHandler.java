package com.flab.jbly.infrastructure.exception;

import com.flab.jbly.infrastructure.exception.user.DuplicatedUserException;
import com.flab.jbly.infrastructure.exception.user.EncoderNoSuchAlgorithmException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {

    private ErrorCode errorCode;
    private ErrorResponse errorResponse;

    @ExceptionHandler(EncoderNoSuchAlgorithmException.class)
    public final ResponseEntity<ErrorResponse> handleEncoderNoSuchAlgorithmException(
        EncoderNoSuchAlgorithmException e) {
        log.debug("암호화 실패", e);
        ErrorResponse response = new ErrorResponse(e.getErrorCode());
        return new ResponseEntity<>(response, HttpStatus.valueOf(e.getErrorCode().getStatus()));
    }


    @ExceptionHandler(DuplicatedUserException.class)
    public final ResponseEntity<ErrorResponse> handleDuplicatedUserException(
        DuplicatedUserException e) {
        log.debug("이미 존재하는 user 입니다.", e);
        ErrorResponse response = new ErrorResponse(e.getErrorCode());
        return new ResponseEntity<>(response, HttpStatus.valueOf(e.getErrorCode().getStatus()));
    }
}
