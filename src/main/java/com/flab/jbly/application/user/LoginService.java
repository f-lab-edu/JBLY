package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.LoginCommand;
import com.flab.jbly.application.user.result.LoginResult;
import com.flab.jbly.domain.user.PasswordEncryption;
import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.infrastructure.exception.UserPasswordNotMatchedException;
import lombok.RequiredArgsConstructor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class LoginService {

		private final PasswordEncryption encryption;
		private final UserRepository repository;

		Logger logger = LoggerFactory.getLogger(this.getClass());

		public LoginResult login(LoginCommand command) {
				User user = repository.findByUserId(command.userId());

				if (!encryption.decode(command.password(), user.getPassword())) {
						throw new UserPasswordNotMatchedException("입력한 비밀번호가 일치하지 않습니다.");
				}
				return new LoginResult(user.getUserId());
		}
}
