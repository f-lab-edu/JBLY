package com.flab.jbly.infrastructure.exception;

public class DoesNotAllowLogoutException extends IllegalArgumentException {

    public DoesNotAllowLogoutException() {
    }

    public DoesNotAllowLogoutException(String s) {
        super(s);
    }
}
