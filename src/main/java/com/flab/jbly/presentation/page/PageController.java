package com.flab.jbly.presentation.page;

import com.flab.jbly.application.product.ProductPagingService;
import com.flab.jbly.application.product.response.PagingDataResponse;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1")
public class PageController {

    private final ProductPagingService service;

    @CrossOrigin
    @GetMapping("/product")
    public ResponseEntity<PagingDataResponse> getPages(
        @RequestParam Long page,
        @RequestParam Long size) {
        return ResponseEntity.ok(service.getPages(page, size));
    }

}
