package com.flab.jbly.presentation.user;

import com.flab.jbly.presentation.user.request.UserLoginRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/login")
public class UserLoginController {

		Logger logger = LoggerFactory.getLogger(this.getClass());

		@GetMapping("")
		public String test(@RequestBody UserLoginRequest request) {
				logger.info(request.userId());
				logger.info(request.password());
				return "hello";
		}
}
