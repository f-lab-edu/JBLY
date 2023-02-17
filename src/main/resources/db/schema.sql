DROP TABLE IF EXISTS user;

CREATE TABLE user
(
    id        BIGINT      NOT NULL AUTO_INCREMENT,
    userId    VARCHAR(100)  NOT NULL,
    password  VARCHAR(500) NOT NULL,
    name      VARCHAR(100)  NOT NULL,
    phone     VARCHAR(100)  NOT NULL,
    email     VARCHAR(100)  NOT NULL,
    address   VARCHAR(100) NOT NULL,
    createdAt DATETIME     NOT NULL,
    updatedAt DATETIME     NOT NULL,

    PRIMARY KEY (id)
);
