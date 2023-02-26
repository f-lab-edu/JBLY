package com.flab.jbly.domain.product;

import java.awt.print.Pageable;
import org.springframework.data.domain.Page;

public interface ProductRepository {

    Page<Product> findByProductType(String type, Pageable pageable);
}
