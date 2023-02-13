package com.flab.jbly.infrastructure.user.impl;

import com.flab.jbly.domain.user.PasswordEncryption;
import org.mindrot.jbcrypt.BCrypt;
import org.springframework.stereotype.Component;

@Component
public class Encryption implements PasswordEncryption {

		private static BCrypt bCrypt = new BCrypt();

		@Override
		public String encode(String plainText) {
				return bCrypt.hashpw(plainText, BCrypt.gensalt());
		}

		@Override
		public boolean decode(String plainText, String password) {
				return bCrypt.checkpw(plainText, password);
		}
}
