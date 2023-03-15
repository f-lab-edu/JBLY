package com.flab.jbly.user;

import com.flab.jbly.presentation.user.request.AccountDeleteRequest;
import com.flab.jbly.presentation.user.request.LoginRequest;
import com.flab.jbly.presentation.user.request.UserSignUpRequest;
import io.restassured.RestAssured;
import io.restassured.response.ExtractableResponse;
import io.restassured.response.Response;
import org.springframework.http.MediaType;

public class UserSteps {

    public static UserSignUpRequest AddUser() {
        String userId = "yeun";
        String password = "!1234abcd";
        String name = "수연";
        String phone = "010-1234-1234";
        String email = "lee@email.com";
        String address = "Seoul";

        return new UserSignUpRequest(userId, password, name,
            phone, email, address);
    }

    public static LoginRequest logInUser() {
        String userId = "yeun";
        String password = "!1234abcd";
        return new LoginRequest(userId, password);
    }

    public static AccountDeleteRequest deleteRequest() {
        Long id = 1L;
        String userId = "yeun";
        return new AccountDeleteRequest(id, userId);
    }

    public static ExtractableResponse<Response> signUpAccountApi(UserSignUpRequest request) {
        return RestAssured.given().log().headers()
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .body(request)
            .when()
            .post("/users")
            .then()
            .log().headers().extract();
    }

    public static ExtractableResponse<Response> deleteAccountApi(AccountDeleteRequest request) {
        return RestAssured.given().log().headers()
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .body(request)
            .when()
            .delete("/users/delete")
            .then()
            .log().headers().extract();
    }
}
