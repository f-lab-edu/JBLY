package com.flab.jbly.infrastructure.jpa.page;

import com.flab.jbly.domain.product.Product;
import com.flab.jbly.domain.product.ProductRepository;
import java.awt.print.Pageable;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.stereotype.Repository;

@Repository
@RequiredArgsConstructor
public class ProductRepositoryAdapter implements ProductRepository {

    private final ProductJpaRepository repository;

    @Override
    public Page<Product> findByProductType(String type, Pageable pageable) {
        return null;
    }
}
