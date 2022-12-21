-- Active: 1663978686370@@db.ethereallab.app@3306@as4283
CREATE TABLE
    IS601_Sample(
        id int auto_increment PRIMARY KEY,
        name VARCHAR(20) unique,
        val VARCHAR(40),
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    )