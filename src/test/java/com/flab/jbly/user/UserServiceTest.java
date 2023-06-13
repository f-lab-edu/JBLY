package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.flab.jbly.application.user.SigninService;
import com.flab.jbly.application.user.UserService;
import com.flab.jbly.domain.user.UserRepository;
import com.flab.jbly.infrastructure.exception.user.EncoderNoSuchAlgorithmException;
import com.flab.jbly.presentation.user.request.SigninRequest;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class UserServiceTest {

    @Autowired
    private UserService userService;

    @Autowired
    private SigninService signinService;

    @Autowired
    private UserRepository userRepository;

    @AfterEach
    void tearDown() {
        userRepository.deleteAllInBatch();
    }

    @DisplayName("사용자 로그인을 테스트합니다.")
    @Test
    public void loginTest() throws Exception {
        // given
        var signUp = UserSteps.AddUser();
        userService.saveUser(signUp.toService());
        var loginRequest = UserSteps.logInUser();

        // when
        var loginResult = signinService.login(loginRequest.toService());

        // then
        assertThat(loginResult.userId()).isEqualTo(signUp.getUserId());
    }

    @DisplayName("사용자 로그인 실패를 테스트합니다.")
    @Test
    public void loginFailTest() throws Exception {

        var signUp = UserSteps.AddUser();
        userService.saveUser(signUp.toService());
        String userId = "yeun";
        String pw = "!abcd1234";

        SigninRequest signinRequest = new SigninRequest(userId, pw);

        assertThatThrownBy(() -> signinService.login(signinRequest.toService())).isInstanceOf(EncoderNoSuchAlgorithmException.class);
    }

}
