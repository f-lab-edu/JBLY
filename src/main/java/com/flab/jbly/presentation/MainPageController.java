package com.flab.jbly.presentation;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/main")
public class MainPageController {

    @GetMapping("/page")
    public String mainPage() {
        return "This is Main Page";
    }
}
