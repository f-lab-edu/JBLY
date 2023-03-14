package com.flab.jbly.presentation.user;

import static com.flab.jbly.infrastructure.common.ResponseEntityConstants.OK;

import com.flab.jbly.application.user.UserService;
import com.flab.jbly.infrastructure.common.ResponseEntityConstants;
import com.flab.jbly.presentation.user.request.AccountDeleteRequest;
import com.flab.jbly.presentation.user.request.UserSignUpRequest;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
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
    public ResponseEntity<Void> signUp(@RequestBody @Valid UserSignUpRequest request) {
        userService.saveUser(request.toCommand());
        return ResponseEntityConstants.CREATED;
    }

    @GetMapping("/{userId}/duplicate")
    public ResponseEntity<Void> isIdDuplicated(@PathVariable String userId) {
        userService.isUserExist(userId);
        return OK;
    }

    @DeleteMapping("/delete")
    public void delete(@RequestBody AccountDeleteRequest request) {
        return;
    }
}
