-- Active: 1663978686370@@db.ethereallab.app@3306@as4283
CREATE TABLE
    IS601_Users(
        id int auto_increment PRIMARY KEY,
        email VARCHAR(60) unique,
        password VARCHAR(60) not null,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )