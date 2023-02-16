package com.flab.jbly.presentation.controller.user;

import static com.flab.jbly.infra.common.ResponseEntityConstants.CONFLICT;
import static com.flab.jbly.infra.common.ResponseEntityConstants.OK;

import com.flab.jbly.application.command.UserSignUpCommand;
import com.flab.jbly.application.service.UserService;
import com.flab.jbly.presentation.request.UserSignUpRequest;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
@RequiredArgsConstructor
@RequestMapping("/users")
public class UserController {

    private final UserService userService;

    @PostMapping
    public void signUp(@RequestBody @Valid UserSignUpRequest request) {
       userService.saveUser(UserSignUpCommand
           .builder()
           .userId(request.getUserId())
           .password(request.getPassword())
           .name(request.getName())
           .phone(request.getPhone())
           .email(request.getEmail())
           .address(request.getAddress())
           .build());
    }

    @GetMapping("/{userId}/duplicate")
    public ResponseEntity<Void> isIdDuplicated(@PathVariable String userId) {
        boolean isIdDuplicated = userService.isUserExist(userId);
        if (isIdDuplicated) {
            return CONFLICT;
        }
        return OK;
    }
}
