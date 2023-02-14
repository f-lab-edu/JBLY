package com.flab.jbly.infrastructure.config;


import com.flab.jbly.application.user.AuthorizationService;
import com.flab.jbly.infrastructure.exception.NotAllowedUserException;
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
            throw new NotAllowedUserException("로그인이 필요합니다.");
        }
        return true;
    }
}
