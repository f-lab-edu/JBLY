package com.flab.jbly.presentation.user;

import com.flab.jbly.application.user.UserService;
import com.flab.jbly.application.user.response.UserResponse;
import com.flab.jbly.presentation.ApiResponse;
import com.flab.jbly.presentation.user.request.AccountDeleteRequest;
import com.flab.jbly.presentation.user.request.AccountUpdateRequest;
import com.flab.jbly.presentation.user.request.SignUpRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.validation.Valid;
import java.io.IOException;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping
    public ApiResponse<UserResponse> signUp(@RequestBody @Valid SignUpRequest request) {
        return ApiResponse.create(userService.saveUser(request.toService()));
    }

    @GetMapping("/{userId}/duplicate")
    public ApiResponse<UserResponse> isIdDuplicated(@PathVariable String userId) {
        return ApiResponse.ok(userService.isUserExist(userId));
    }

    @DeleteMapping("/delete")
    public ApiResponse<UserResponse> delete(@RequestBody AccountDeleteRequest request) {
        return ApiResponse.ok(userService.deleteAccount(request.toService()));
    }

    @PatchMapping("/update")
    public ApiResponse<UserResponse> update(@RequestBody AccountUpdateRequest request) {
        return ApiResponse.ok(userService.update(request.toService()));
    }

    @PostMapping("")
    public void logout(HttpServletResponse response) throws IOException {
        // TODO: 2023/06/08 redis 사용한 인가 처리 적용 후 새롭게 구현해야합니다.
        userService.logout();
        response.sendRedirect("http://localhost:8080/main/page");
    }
}
