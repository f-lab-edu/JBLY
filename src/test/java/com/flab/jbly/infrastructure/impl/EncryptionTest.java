package com.flab.jbly.infrastructure.impl;

import static org.assertj.core.api.Assertions.assertThat;

import com.flab.jbly.infrastructure.user.encryption.Encryption;
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
