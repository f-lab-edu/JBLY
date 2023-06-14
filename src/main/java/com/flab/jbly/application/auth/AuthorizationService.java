package com.flab.jbly.application.auth;

import com.flab.jbly.application.auth.request.AuthorizationServiceRequest;
import com.flab.jbly.application.auth.response.AuthorizationResponse;
import jakarta.servlet.http.HttpServletRequest;

public interface AuthorizationService {

    String login(AuthorizationServiceRequest authorizationServiceRequest);

    AuthorizationResponse getCurrentUser(HttpServletRequest request);

    void logout(HttpServletRequest request);
}
