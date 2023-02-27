package com.flab.jbly.application.product.result;

import com.flab.jbly.domain.product.Product;
import java.util.ArrayList;
import java.util.List;

public record PagingDataResult(
    List<Product> data,
    int totalPage
) {

    public PagingDataResult(List<Product> data, int totalPage) {
        this.data = new ArrayList<>();
        for (Product product : data) {
            this.data.add(product);
        }
        this.totalPage = totalPage;
    }
}
