package com.flab.jbly.infrastructure.jpa.page;

import com.flab.jbly.domain.product.Product;
import com.flab.jbly.domain.product.ProductRepository;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Repository;

@Repository
@RequiredArgsConstructor
public class ProductRepositoryAdapter implements ProductRepository {

    private final ProductJpaRepository repository;


    @Override

    public List<Product> findAllProduct() {
        return repository.findAll();
    }
}
