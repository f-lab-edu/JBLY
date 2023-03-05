package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;

import com.flab.jbly.application.user.UserServiceImpl;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class UserServiceTest {

    @Autowired
    private UserServiceImpl userService;

    /*
    * Seed Data가 우선권을 갖고 있습니다. Seed Data 다음부터 Data가 쌓입니다.
    * */
    @DisplayName("사용자 회원가입 테스트")
    @Test
    public void signUpTest() throws Exception {
        var request = UserSteps.AddUser();
        var id = 1L;
        userService.saveUser(request.toCommand());
        var response = userService.getUserById(id);
        assertThat(response.getId()).isEqualTo(id);
    }


}
