package com.flab.jbly.infrastructure.encryption;

import static org.assertj.core.api.Assertions.assertThat;

<<<<<<< HEAD
=======
import com.flab.jbly.infrastructure.user.encryption.Encryption;
>>>>>>> 3c9437a475cb0b6cbd63a9ee3e952777c5231705
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

class EncryptionTest {

		private Encryption encryption;
		Logger logger = LoggerFactory.getLogger(this.getClass());

		@BeforeEach
		void setUp() {
				encryption = new Encryption();
		}

		@Test
		public void decodeTest() throws Exception {
				String plainText = "123";
				String password = "$2a$10$9ppHhId4lC1nu6XKLECU2uVZz.idsMNMJq9XVod0zJScvs6SJrd.y";
				assertThat(encryption.decode(plainText, password)).isTrue();
		}

}
