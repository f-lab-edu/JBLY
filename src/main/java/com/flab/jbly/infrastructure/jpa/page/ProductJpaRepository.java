package com.flab.jbly.infrastructure.jpa.page;

import com.flab.jbly.domain.product.Product;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductJpaRepository extends JpaRepository<Product, Long> {

}
