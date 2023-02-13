package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.LoginCommand;
import com.flab.jbly.domain.user.PasswordEncryption;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class LoginService {

		private final PasswordEncryption encryption;

		public void login(LoginCommand command) {
				// TODO: 2023/02/13 password encryption
				// TODO: 2023/02/13 session publishing
		}
}
