package com.flab.jbly.infrastructure.config;


import com.flab.jbly.application.auth.AuthorizationService;
import com.flab.jbly.application.auth.response.AuthorizationResponse;
import com.flab.jbly.infrastructure.common.Role;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.NotAllowedUserException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

@Component
public class SigninCheckInterceptor implements HandlerInterceptor {

    private final AuthorizationService service;

    public SigninCheckInterceptor(AuthorizationService service) {
        this.service = service;
    }

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
        Object handler) throws Exception {
        AuthorizationResponse currentUser = service.getCurrentUser(request);

        if (currentUser == null) {
            throw new NotAllowedUserException("NotAllowedUserException", ErrorCode.NOT_FOUND_USER_IN_LOGIN_ERROR);
        }

        if (currentUser.getRole() != Role.USER) {
            throw new IllegalArgumentException("사용자 권한이 없습니다.");
        }
        return true;
    }
}
