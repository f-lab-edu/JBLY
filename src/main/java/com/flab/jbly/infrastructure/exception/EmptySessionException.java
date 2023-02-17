package com.flab.jbly.infrastructure.exception;

public class EmptySessionException extends IllegalArgumentException {

    public EmptySessionException() {
    }

    public EmptySessionException(String s) {
        super(s);
    }
}
