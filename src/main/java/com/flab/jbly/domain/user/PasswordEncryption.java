package com.flab.jbly.domain.user;

public interface PasswordEncryption {

		String encode(String plainText);

		boolean decode(String plainText, String password);

}
