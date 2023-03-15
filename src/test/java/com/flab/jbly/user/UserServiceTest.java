package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.flab.jbly.application.user.LoginService;
import com.flab.jbly.application.user.UserServiceImpl;
import com.flab.jbly.infrastructure.exception.user.DoesNotExistUserException;
import com.flab.jbly.infrastructure.exception.user.EncoderNoSuchAlgorithmException;
import com.flab.jbly.presentation.user.request.LoginRequest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.DirtiesContext;

@SpringBootTest
@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_EACH_TEST_METHOD)
class UserServiceTest {

    @Autowired
    private UserServiceImpl userService;

    @Autowired
    private LoginService loginService;

    @DisplayName("사용자 회원가입 테스트")
    @Test
    public void signUpTest() throws Exception {
        var request = UserSteps.AddUser();
        var id = 1L;
        userService.saveUser(request.toCommand());
        var response = userService.getUserById(id);
        assertThat(response.getId()).isEqualTo(id);
    }

    @DisplayName("사용자 회원 탈퇴 시 pk로 회원을 찾으면 Exception이 발생합니다.")
    @Test
    public void accountDeleteTest() throws Exception {
        var signUp = UserSteps.AddUser();
        var id = 1L;
        userService.saveUser(signUp.toCommand());
        userService.deleteUserAccount(id);
        assertThatThrownBy(() -> userService.getUserById(id)).isInstanceOf(
            DoesNotExistUserException.class);
    }

    @DisplayName("사용자 로그인을 테스트합니다.")
    @Test
    public void loginTest() throws Exception {
        // given
        var signUp = UserSteps.AddUser();
        userService.saveUser(signUp.toCommand()); // db 적재
        var loginRequest = UserSteps.logInUser();

        // when
        var loginResult = loginService.login(loginRequest.toCommand());

        // then
        assertThat(loginResult.userId()).isEqualTo(signUp.getUserId());
    }

    @DisplayName("사용자 로그인 실패를 테스트합니다.")
    @Test
    public void loginFailTest() throws Exception {

        var signUp = UserSteps.AddUser();
        userService.saveUser(signUp.toCommand());
        String userId = "yeun";
        String pw = "!abcd1234";

        var loginRequest = new LoginRequest(userId, pw);

        assertThatThrownBy(() -> loginService.login(loginRequest.toCommand())).isInstanceOf(EncoderNoSuchAlgorithmException.class);
    }

}
