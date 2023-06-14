package com.flab.jbly.presentation.user;

import com.flab.jbly.application.user.SigninService;
import com.flab.jbly.application.user.response.UserResponse;
import com.flab.jbly.presentation.ApiResponse;
import com.flab.jbly.presentation.user.request.SigninRequest;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/signin")
public class SigninController {

	private final SigninService service;

	public SigninController(SigninService service) {
		this.service = service;
	}

	@PostMapping("")
	public ApiResponse<UserResponse> login(@RequestBody SigninRequest request) {
		return ApiResponse.ok(service.login(request.toService()));
	}
}
