package com.flab.jbly.infrastructure.config;

import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
@RequiredArgsConstructor
public class WebConfig implements WebMvcConfigurer {

    /*
    * - logout Page에 접근하기 위해선 session을 가져야 접근할 수 있습니다.
    * - 회원 가입 url, main page url을 excludePath에 추가해야합니다.
    * */

    private final SigninCheckInterceptor interceptor;

    @Override
    public void addInterceptors(InterceptorRegistry registry) {
        registry.addInterceptor(interceptor)
            .addPathPatterns() // /**
            .excludePathPatterns("/**"); // /main/page","/login","/users/**
        // Product 개발을 위해 모든 url을 열어뒀습니다. 개발 후 다시 변경해야합니다.
    }
}
