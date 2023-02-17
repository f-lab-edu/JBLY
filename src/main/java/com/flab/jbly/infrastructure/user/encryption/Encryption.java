<<<<<<< HEAD:src/main/java/com/flab/jbly/infrastructure/impl/Encryption.java
package com.flab.jbly.infrastructure.impl;
=======
package com.flab.jbly.infrastructure.user.encryption;
>>>>>>> 3c9437a475cb0b6cbd63a9ee3e952777c5231705:src/main/java/com/flab/jbly/infrastructure/user/encryption/Encryption.java

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
