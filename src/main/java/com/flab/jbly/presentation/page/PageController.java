package com.flab.jbly.presentation.page;

import com.flab.jbly.application.product.ProductPagingService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/product/list")
public class PageController {

    private final ProductPagingService service;

    @GetMapping
    public void getPages() {
        service.getPages();
    }

}
