-- Active: 1663978686370@@db.ethereallab.app@3306@as4283
CREATE TABLE
    IF NOT EXISTS IS601_S_Orders(
        id int AUTO_INCREMENT PRIMARY KEY,
        user_id int,
        total_price float,
        address VARCHAR(200),
        payment_method VARCHAR(30),
        money_received float,
        first_name varchar(30),
        last_name varchar(15),
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES IS601_Users(id)
    )