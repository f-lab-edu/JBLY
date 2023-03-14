package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.flab.jbly.application.user.UserServiceImpl;
import com.flab.jbly.infrastructure.exception.user.DoesNotExistUserException;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class UserServiceTest {

    @Autowired
    private UserServiceImpl userService;

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
}
