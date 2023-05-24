package com.flab.jbly.presentation;

import com.flab.jbly.presentation.user.response.DeploySuccessResponse;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/main")
public class MainPageController {

    @CrossOrigin
    @GetMapping("/deploy-test")
    public DeploySuccessResponse mainPage() {
        return DeploySuccessResponse.builder()
            .text("Success Deploy")
            .build();
    }
}
