package com.flab.jbly.infrastructure.config;

import com.flab.jbly.application.auth.AuthorizationService;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/*
* WebMvcConfig는 HandlerInterceptor 를 Bean으로 등록하기 위해 사용됩니다.
* */
@Configuration
public class WebConfig implements WebMvcConfigurer {
    private final AuthorizationService authorizationService;
    public WebConfig(AuthorizationService authorizationService) {
        this.authorizationService = authorizationService;
    }

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(new SigninCheckInterceptor(authorizationService))
            .addPathPatterns() // 인가 처리를 수행할 URL 패턴을 지정합니다.
            .excludePathPatterns("/**"); // 예외로 처리할 URL 패턴을 지정합니다.
    }
}
