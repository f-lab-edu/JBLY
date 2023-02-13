package com.flab.jbly.application.user;

import com.flab.jbly.application.user.command.LoginCommand;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Service;

@Service
public class LoginService {

		Logger logger = LoggerFactory.getLogger(this.getClass());

		public void login(LoginCommand command) {

				logger.info("service layer is working");

		}
}
