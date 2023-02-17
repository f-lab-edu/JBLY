package com.flab.jbly.presentation.user;

import com.flab.jbly.application.user.LogoutService;
import jakarta.servlet.http.HttpServletResponse;
import java.io.IOException;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/logout")
@RequiredArgsConstructor
public class LogoutController {

    private final LogoutService logoutService;

    @PostMapping
    public void logout(HttpServletResponse response) throws IOException {
        // TODO: 2023/02/15 Need redirect main page
        logoutService.logout();
        response.sendRedirect("http://localhost:8080/main/page");
    }
}
