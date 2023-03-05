package com.flab.jbly.user;

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

    public static ExtractableResponse<Response> signUpUserApi(UserSignUpRequest request) {
        return RestAssured.given().log().all()
            .contentType(MediaType.APPLICATION_JSON_VALUE)
            .body(request)
            .when()
            .post("/users")
            .then()
            .log().all().extract();
    }
}
