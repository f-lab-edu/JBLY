package com.flab.jbly.application.product.response;

import com.flab.jbly.domain.product.Product;
import java.util.ArrayList;
import java.util.List;

public record PagingDataResponse(
    List<Product> data,
    int totalPage
) {

    public PagingDataResponse(List<Product> data, int totalPage) {
        this.data = new ArrayList<>();
        for (Product product : data) {
            this.data.add(product);
        }
        this.totalPage = totalPage;
    }
}
