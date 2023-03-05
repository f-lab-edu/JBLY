package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;

import com.flab.jbly.ApiTest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;

public class UserApiTest extends ApiTest {

    @DisplayName("사용자 회원가입 API TEST")
    @Test
    public void signUpApiTest() throws Exception {
        var request = UserSteps.AddUser();
        // api 전송
        var response = UserSteps.signUpUserApi(request);
        assertThat(response.statusCode()).isEqualTo(HttpStatus.CREATED.value());
    }
}
