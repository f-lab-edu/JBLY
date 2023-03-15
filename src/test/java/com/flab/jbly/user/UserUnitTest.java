package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.flab.jbly.presentation.user.request.LoginRequest;
import java.util.stream.Stream;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

public class UserUnitTest {

    @DisplayName("사용자 로그인 시 데이터의 타입이 안 맞을 경우")
    @ParameterizedTest
    @MethodSource("failLoginDataSet")
    public void loginRequestExceptionTest(String userId, String pw) throws Exception {
        assertThatThrownBy(() -> new LoginRequest(userId, pw)).isInstanceOf(
                IllegalArgumentException.class)
            .hasMessage("로그인을 할 수 없습니다.");
    }

    @DisplayName("사용자 로그인 시 비밀번호가 조건에 맞지 않을 경우")
    @Test
    public void loginRequestPwdNotRequiredConditionTest() throws Exception {

    }

    private static Stream<Arguments> failLoginDataSet() {
        return Stream.of(
            Arguments.of("", "!1234abcd"),
            Arguments.of("", "")
        );
    }

}
