package com.flab.jbly.domain.product;

import lombok.Getter;
import lombok.RequiredArgsConstructor;

@Getter
@RequiredArgsConstructor
public enum Category {
    TOP("상의"),
    BOTTOM("하의"),
    OUTWEAR("아우터"),
    SHOES("신발"),
    ACCESSORY("악세서리");

    private final String text;
}
