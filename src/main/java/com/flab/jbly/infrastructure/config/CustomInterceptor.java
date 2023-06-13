package com.flab.jbly.infrastructure.config;


import com.flab.jbly.application.auth.AuthorizationService;
import com.flab.jbly.infrastructure.exception.ErrorCode;
import com.flab.jbly.infrastructure.exception.user.NotAllowedUserException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

@Component
@RequiredArgsConstructor
public class CustomInterceptor implements HandlerInterceptor {

    private final AuthorizationService service;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response,
        Object handler) throws Exception {
        var currentUser = service.getCurrentUser(request);

        if (currentUser == null) {
            throw new NotAllowedUserException("NotAllowedUserException", ErrorCode.NOT_FOUND_USER_IN_LOGIN_ERROR);
        }
        return true;
    }
}
