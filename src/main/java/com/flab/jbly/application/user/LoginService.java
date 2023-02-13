package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.LoginCommand;
import com.flab.jbly.domain.user.PasswordEncryption;
import com.flab.jbly.domain.user.User;
import com.flab.jbly.domain.user.UserRepository;
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

		public void login(LoginCommand command) {
				User user = repository.findByUserId(command.userId());
				logger.info("Using Jpa and check userId. UserId is =" + user.getUserId());
		}
}
