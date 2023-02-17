package com.flab.jbly.presentation.user;

import com.flab.jbly.application.user.LoginService;
import com.flab.jbly.application.user.result.LoginResult;
import com.flab.jbly.presentation.user.request.LoginRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/login")
@RequiredArgsConstructor
public class LoginController {

	private final LoginService service;

	@PostMapping("")
	public LoginResult login(@RequestBody LoginRequest request) {
		var result = service.login(request.toCommand());
		return result;
	}

	// AuthTest Signature
	@GetMapping("/sessionTest")
	public String sessionTest() {
		return "it's working";
	}
}
