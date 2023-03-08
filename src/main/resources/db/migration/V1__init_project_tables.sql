CREATE TABLE if not exists `user`(
    `id`        bigint       NOT NULL AUTO_INCREMENT,
    `userId`    varchar(100) NOT NULL,
    `address`   varchar(255) NOT NULL,
    `email`     varchar(255) NOT NULL,
    `name`      varchar(100) NOT NULL,
    `password`  varchar(500) NOT NULL,
    `phone`     varchar(255) NOT NULL,
    `updatedAt` datetime(6) DEFAULT NULL,
    `createdAt` datetime(6) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

create table if not exists `session`(
    `id` bigint NOT NULL AUTO_INCREMENT,
    `sessionToken` varchar(255) DEFAULT NULL,
    `userId` bigint NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

create table if not exists `session`
(
    `id` bigint NOT NULL AUTO_INCREMENT,
    `detailHtml` longtext  NOT NULL,
    `detailInfo` text  NOT NULL,
    `price` decimal(38,2) NOT NULL,
    `image` varchar(255)  NOT NULL,
    `productName` varchar(255)  NOT NULL,
    `productType` varchar(255)  NOT NULL,
    `shopId` bigint NOT NULL,
    `shopName` varchar(255)  NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
