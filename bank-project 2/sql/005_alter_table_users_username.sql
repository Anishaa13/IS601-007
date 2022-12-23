-- Active: 1663978686370@@db.ethereallab.app@3306@as4283
ALTER TABLE IS601_Users
ADD
    COLUMN username1 varchar(30) not null unique default (substring_index(email, '@', 1)) COMMENT 'Username field that defaults to the name of the email';