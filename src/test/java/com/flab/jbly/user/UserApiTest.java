package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;

import com.flab.jbly.ApiTest;
import com.flab.jbly.presentation.user.request.SignUpRequest;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.springframework.http.HttpStatus;

public class UserApiTest extends ApiTest {

    @DisplayName("사용자 회원가입 API TEST")
    @Test
    public void signUpApiTest() throws Exception {
        SignUpRequest request = UserSteps.AddUser();
        // api 전송
        var response = UserSteps.signUpAccountApi(request);
        assertThat(response.statusCode()).isEqualTo(HttpStatus.CREATED.value());
    }
    @DisplayName("사용자 회원 탈퇴 성공 API TEST")
    @Test
    public void deleteAccountTest() throws Exception {
        var signUpRequest = UserSteps.AddUser();
        UserSteps.signUpAccountApi(signUpRequest);
        var request = UserSteps.deleteRequest();
        var response = UserSteps.deleteAccountApi(request);
        assertThat(response.statusCode()).isEqualTo(HttpStatus.OK.value());
    }

    // TODO: 2023/03/15 회원 가입 실패 테스트
}
