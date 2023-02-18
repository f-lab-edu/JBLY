package com.flab.jbly.infrastructure.exception.user;

public class DoesNotAllowLogoutException extends IllegalArgumentException {

    public DoesNotAllowLogoutException() {
    }

    public DoesNotAllowLogoutException(String s) {
        super(s);
    }
}
