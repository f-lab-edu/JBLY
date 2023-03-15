package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.flab.jbly.presentation.user.request.AccountDeleteRequest;
import com.flab.jbly.presentation.user.request.LoginRequest;
import java.util.stream.Stream;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

public class UserUnitTest {

    @DisplayName("사용자 로그인 시 데이터의 타입이 안 맞을 경우")
    @ParameterizedTest
    @MethodSource("failLoginDataSet")
    public void loginRequestExceptionTest(String userId, String pwd) throws Exception {
        assertThatThrownBy(() -> new LoginRequest(userId, pwd)).isInstanceOf(IllegalArgumentException.class);
    }

    @DisplayName("사용자 계정 삭제 시 PK 값이 존재하지 않을 경우")
    @ParameterizedTest
    @MethodSource("failDeleteRequestSet")
    public void accountDeleteRequestPKNotRequiredConditionTest() throws Exception {
        Long pk = 0L;
        assertThatThrownBy(() -> new AccountDeleteRequest(pk,"abc")).isInstanceOf(IllegalArgumentException.class);
    }

    private static Stream<Arguments> failLoginDataSet() {
        return Stream.of(
            Arguments.of("", "!1234abcd"),
            Arguments.of("abcd", ""),
            Arguments.of("", "")
        );
    }

    private static Stream<Arguments> failDeleteRequestSet() {
        return Stream.of(
            Arguments.of(0L, "abc"),
            Arguments.of(1L, "")
        );
    }
}
