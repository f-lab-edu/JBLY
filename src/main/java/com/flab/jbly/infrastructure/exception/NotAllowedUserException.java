package com.flab.jbly.infrastructure.exception;

public class NotAllowedUserException extends IllegalArgumentException {

    public NotAllowedUserException() {
    }

    public NotAllowedUserException(String s) {
        super(s);
    }
}
