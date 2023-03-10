package com.flab.jbly.domain.product;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.EnumType;
import jakarta.persistence.Enumerated;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import java.math.BigDecimal;
import lombok.AccessLevel;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Entity
@AllArgsConstructor
@Builder
@Getter
@Table(name = "product")
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "shopId", nullable = false)
    private Long shopId;

    @Column(name = "shopName", nullable = false)
    private String shopName;

    @Column(name = "productName", nullable = false)
    private String productName;

    @Column(name = "price", nullable = false)
    private BigDecimal price;

    @Enumerated(EnumType.STRING)
    @Column(name = "productType", nullable = false)
    private Category productType;

    @Column(name = "image", nullable = false)
    private String productImage;

    @Column(name = "detailInfo", nullable = false, columnDefinition = "TEXT")
    private String detailInfo;

    @Column(name = "detailHtml", nullable = false, columnDefinition = "LONGTEXT")
    private String detailHtml;

    public enum Category {
        TOP,
        BOTTOM,
        OUTWEAR,
        SHOES,
        ACCESSORY,
    }
}
