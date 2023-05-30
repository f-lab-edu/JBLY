CREATE TABLE IF NOT EXISTS `users`(
    `id`        bigint       NOT NULL AUTO_INCREMENT,
    `userId`    varchar(100) NOT NULL,
    `address`   varchar(255) NOT NULL,
    `email`     varchar(255) NOT NULL,
    `name`      varchar(100) NOT NULL,
    `password`  varchar(500) NOT NULL,
    `phone`     varchar(255) NOT NULL,
    `modified_date_time` datetime(6) DEFAULT NULL,
    `created_date_time` datetime(6) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `product`
(
    `id` bigint NOT NULL AUTO_INCREMENT,
    `detail_html` longtext  NOT NULL,
    `detail_info` text  NOT NULL,
    `price` decimal(38,2) NOT NULL,
    `image` varchar(255)  NOT NULL,
    `product_name` varchar(255)  NOT NULL,
    `product_type` varchar(255)  NOT NULL,
    `shop_id` bigint NOT NULL,
    `shop_name` varchar(255)  NOT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE IF NOT EXISTS `session`(
    `id` bigint NOT NULL AUTO_INCREMENT,
    `session_token` varchar(255) DEFAULT NULL,
    `user_id` bigint NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
