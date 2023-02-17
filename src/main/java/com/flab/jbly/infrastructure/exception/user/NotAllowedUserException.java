package com.flab.jbly.infrastructure.exception.user;

public class NotAllowedUserException extends IllegalArgumentException {

    public NotAllowedUserException() {
    }

    public NotAllowedUserException(String s) {
        super(s);
    }
}
