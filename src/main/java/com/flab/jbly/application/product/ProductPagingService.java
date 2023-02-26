package com.flab.jbly.application.product;

import com.flab.jbly.domain.product.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProductPagingService {

    private final ProductRepository repository;

    public void getPages() {

    }
}
