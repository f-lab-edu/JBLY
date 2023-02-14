package com.flab.jbly.infrastructure.exception;

public class SessionDoesNotExistException extends IllegalArgumentException {

    public SessionDoesNotExistException() {
    }

    public SessionDoesNotExistException(String s) {
        super(s);
    }
}
