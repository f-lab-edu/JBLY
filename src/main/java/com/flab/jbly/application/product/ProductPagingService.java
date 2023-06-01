package com.flab.jbly.application.product;

import com.flab.jbly.application.product.result.PagingDataResult;
import com.flab.jbly.domain.product.ProductPageRepository;
import com.flab.jbly.domain.product.ProductRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.PageRequest;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProductPagingService {

    private final ProductPageRepository pageRepository;
    private final ProductRepository productRepository;

    public PagingDataResult getPages(Long start, Long size) {
        var request = PageRequest.of(start.intValue() - 1, size.intValue());
        var pages = pageRepository.findAll(request);
        var totalPages = Math.floorDiv(productRepository.findAllProduct().size(), size.intValue());
        return new PagingDataResult(pages.getContent(), totalPages);
    }
}
