package com.flab.jbly.domain.product;

import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.repository.PagingAndSortingRepository;

public interface ProductPageRepository extends PagingAndSortingRepository<Product, Long> {

    Page<Product> findAll(Pageable pageable);
}
