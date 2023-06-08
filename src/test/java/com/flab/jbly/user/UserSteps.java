package com.flab.jbly.user;

import com.flab.jbly.presentation.user.request.AccountDeleteRequest;
import com.flab.jbly.presentation.auth.request.SigninRequest;
import com.flab.jbly.presentation.user.request.AccountUpdateRequest;
import com.flab.jbly.presentation.user.request.SignUpRequest;
import io.restassured.RestAssured;
import io.restassured.response.ExtractableResponse;
import io.restassured.response.Response;
import org.springframework.http.MediaType;

public class UserSteps {

    public static SignUpRequest AddUser() {
        String userId = "yeun";
        String password = "!1234abcd";
        String name = "수연";
        String phone = "010-1234-1234";
        String email = "lee@email.com";
        String address = "Seoul";

        return new SignUpRequest(userId, password, name,
            phone, email, address);
    }

    public static SigninRequest logInUser() {
        String userId = "yeun";
        String password = "!1234abcd";
        return new SigninRequest(userId, password);
    }

    public static AccountDeleteRequest deleteRequest() {
        Long id = 1L;
        String userId = "yeun";
        return new AccountDeleteRequest(id, userId);
    }

    public static AccountUpdateRequest updateRequest(Long id) {
        String userId = "susu";
        String password = "!abcd1234";
        String name = "연수";
        String phone = "010-1234-1234";
        String email = "lee@email.com";
        String address = "Seoul";
        return new AccountUpdateRequest(id, userId, password, name, phone, email, address);
    }

    public static ExtractableResponse<Response> signUpAccountApi(SignUpRequest request) {
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
