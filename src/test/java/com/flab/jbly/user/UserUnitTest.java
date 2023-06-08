package com.flab.jbly.user;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;

import com.flab.jbly.application.user.UserService;
import com.flab.jbly.infrastructure.encryption.Encryption;
import com.flab.jbly.infrastructure.exception.user.AccountMisMatchInfoException;
import com.flab.jbly.infrastructure.exception.user.DuplicatedUserException;
import com.flab.jbly.presentation.user.request.AccountDeleteRequest;
import com.flab.jbly.presentation.user.request.LoginRequest;
import java.util.stream.Stream;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

public class UserUnitTest {

    private UserService userService;
    private HashMapRepository repository = new HashMapRepository();

    @BeforeEach
    void setUp() {
        repository.clearDB();
        userService = new UserService(repository, new Encryption());
    }

    @DisplayName("회원 가입 성공하는 경우")
    @Test
    public void signUpSuccessTest() throws Exception {
        var request = UserSteps.AddUser();
        var userPk = 1L;
        userService.saveUser(request.toService());
        var user = repository.getUserById(userPk);
        assertThat(user.getId()).isEqualTo(userPk);
    }

    @DisplayName("회원 가입 실패하는 경우, 동일한 ID값이 입력될 경우 실패합니다.")
    @Test
    public void signUpFailTest() throws Exception {
        var user1 = UserSteps.AddUser();
        var user2 = UserSteps.AddUser();
        userService.saveUser(user1.toService());
        assertThatThrownBy(() -> userService.saveUser(user2.toService())).isInstanceOf(
            DuplicatedUserException.class);
    }

    @DisplayName("회원 계정 삭제 성공하는 경우")
    @Test
    public void deleteUserSuccessTest() throws Exception {
        var user = UserSteps.AddUser();
        userService.saveUser(user.toService());

        var request = UserSteps.deleteRequest();
        userService.deleteAccount(request.toService());

        assertThat(repository.getUserById(request.id())).isNull();
    }

    @DisplayName("아이디가 틀릴 경우 회원 계정 삭제 실패")
    @Test
    public void deleteUserFailTest() throws Exception {
        var signUpRequest = UserSteps.AddUser();
        userService.saveUser(signUpRequest.toService());

        var request = new AccountDeleteRequest(1L, "abc");
        assertThatThrownBy(() -> userService.deleteAccount(request.toService())).isInstanceOf(
            AccountMisMatchInfoException.class);
    }

    @DisplayName("회원 수정 성공 테스트")
    @Test
    public void updateSuccessTest() throws Exception {
        var signUpRequest = UserSteps.AddUser();
        userService.saveUser(signUpRequest.toService());
        var signUpUser = repository.getUserById(1L);
        String signUpUserId = signUpUser.getUserId();

        var updateRequest = UserSteps.updateRequest(1L);
        userService.update(updateRequest.toService());
        var updateUser = repository.getUserById(1L);

        assertThat(updateUser.getId()).isEqualTo(signUpUser.getId());
        assertThat(updateUser.getUserId()).isNotEqualTo(signUpUserId);
    }

    @DisplayName("회원 수정 실패 테스트")
    @Test
    public void updateFailTest() throws Exception {
        var signUpRequest = UserSteps.AddUser();
        userService.saveUser(signUpRequest.toService());

        var updateRequest = UserSteps.updateRequest(2L);

        assertThatThrownBy(() -> userService.update(updateRequest.toService())).isInstanceOf(
            NullPointerException.class);
    }


    @DisplayName("로그인 시 데이터의 타입이 안 맞을 경우 예외 발생")
    @ParameterizedTest
    @MethodSource("failLoginRequestSet")
    public void loginRequestExceptionTest(String userId, String pwd) throws Exception {
        assertThatThrownBy(() -> new LoginRequest(userId, pwd)).isInstanceOf(
            IllegalArgumentException.class);
    }

    @DisplayName("계정 삭제 요청 시 데이터의 타입이 안 맞을 경우 예외 발생")
    @ParameterizedTest
    @MethodSource("failDeleteRequestSet")
    public void accountDeleteRequestPKNotRequiredConditionTest(Long pk, String userId) throws Exception {
        assertThatThrownBy(() -> new AccountDeleteRequest(pk, userId)).isInstanceOf(
            IllegalArgumentException.class);
    }

    private static Stream<Arguments> failLoginRequestSet() {
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
