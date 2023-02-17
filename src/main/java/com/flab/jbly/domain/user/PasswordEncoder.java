package com.flab.jbly.domain.user;

public interface PasswordEncoder {

    String encrypt(String password);

    boolean matches(String password, String encodedPassword);
}
