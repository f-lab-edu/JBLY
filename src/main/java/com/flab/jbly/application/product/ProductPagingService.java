package com.flab.jbly.application.product;

import com.flab.jbly.domain.product.Product;
import com.flab.jbly.domain.product.ProductPageRepository;
import java.util.List;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProductPagingService {

    private final ProductPageRepository repository;

    public List<Product> getPages(Long start, Long size) {
        var request = PageRequest.of(start.intValue() - 1, size.intValue());
        var pages = repository.findAll(request);
        return pages.getContent();
    }
}
