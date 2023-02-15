package com.flab.jbly.presentation.user;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/logout")
public class LogoutController {

    @GetMapping("")
    public String logout() {
        // TODO: 2023/02/15 Need redirect main page
        return "Hello world";
    }
}
