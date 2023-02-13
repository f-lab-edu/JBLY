package com.flab.jbly.presentation.user;

import com.flab.jbly.application.user.LoginService;
import com.flab.jbly.presentation.user.request.LoginRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/login")
@RequiredArgsConstructor
public class LoginController {
		private final LoginService service;

		@GetMapping("")
		public String test(@RequestBody LoginRequest request) {
				service.login(request.toCommand());
				return "hello";
		}
}
