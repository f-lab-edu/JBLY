package com.flab.jbly.presentation.page.request;

import org.springframework.util.Assert;

public record ProductPageRequest(
    int startPage,
    int endPage
) {
    public ProductPageRequest {
        Assert.isTrue(startPage >0 , "페이지는 음수가 될 수 없습니다.");
        Assert.isTrue(endPage >0 , "페이지는 음수가 될 수 없습니다.");
    }
}
